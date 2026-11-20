#!/usr/bin/env python3
"""Regression checks for the author-supplied V3 manuscript source.

The original DOCX identifiers and hashes are recorded in sources/originals.json.
Tests bind the committed publication sources to their recorded hashes and
validate deterministic presentation. They do not independently read DOCX bytes.
"""
from __future__ import annotations

import hashlib
from html import escape, unescape
import json
import re
import unittest

import build_site as publication
from render_science import FORMULAE, enhance_scientific_presentation, render_source_math
from check_originals import Paragraphs, overlap, phrases, tokens
from render_synthesis import render_synthesis_figures
from render_references import render_synthesis_references
from render_semantic import render_semantic_participation, _HEADERS, _ROW_COUNTS
from render_typed import render_typed_generativity, _HEADERS as TG_HEADERS, _ROW_COUNTS as TG_ROWS
from render_functorial import render_functorial_diagram, render_functorial_tables, HEADERS as FC_HEADERS, ROW_COUNTS as FC_ROWS, SOURCE_TABLE_LABELS



class ManuscriptFidelityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.documents = json.loads(
            (publication.ROOT / "sources" / "originals.json").read_text(encoding="utf-8")
        )["documents"]

    def test_inventory_matches_original_uploads(self) -> None:
        self.assertEqual(
            set(self.documents),
            {row[0] for row in publication.ESSAYS},
        )

    def test_exact_uploaded_source_derivatives(self) -> None:
        for slug, title, _, _ in publication.ESSAYS:
            with self.subTest(slug=slug):
                record = self.documents[slug]
                source_file = publication.ROOT / "essays" / f"{slug}.md"
                contents = source_file.read_text(encoding="utf-8")
                self.assertEqual(
                    hashlib.sha256(source_file.read_bytes()).hexdigest(),
                    record["markdown_sha256"],
                )
                if slug in {"lambek-machines", "algebraic-architectures"}:
                    self.assertTrue(contents.startswith(f"# {title}\n\n## Abstract\n"))
                    self.assertNotIn("AUTHORITATIVE-DOCX SHA256", contents)
                    body, digest = publication.source_to_body(contents, title, [])
                    self.assertEqual(digest, record["markdown_sha256"])
                    self.assertEqual(body.count("<table "), record["publication_table_count"])
                    self.assertEqual(body.count('class="table-scroll"'), record["publication_table_count"])
                    self.assertEqual(body.count('class="visually-hidden"'), record["publication_table_count"])
                    self.assertEqual(
                        len(re.findall("<h2|<h3", body)), record["publication_heading_count"]
                    )
                    continue
                provenance = (
                    "<!-- AUTHORITATIVE-DOCX SHA256 "
                    + record["source_sha256"]
                    + "; source "
                    + record["source_docx"]
                    + " -->"
                )
                self.assertIn(provenance, contents)
                self.assertTrue(contents.startswith(f"# {title}\n\n*Mateo Petel*\n\n"))
                body, digest = publication.source_to_body(contents, title, [])
                self.assertEqual(digest, record["markdown_sha256"])
                self.assertTrue(body.startswith('<h2 id="abstract">Abstract</h2>'))
                self.assertEqual(body.count("<table "), record["table_count"])
                self.assertEqual(body.count('class="table-scroll"'), record["table_count"])
                self.assertEqual(body.count('class="visually-hidden"'), record["table_count"])
                self.assertEqual(
                    len(re.findall("<h2|<h3", body)), record["heading_count"]
                )

    def test_derived_table_labels_do_not_appear_as_manuscript_prose(self) -> None:
        """The table names introduced for accessibility are visually suppressed."""
        css = (publication.ROOT / "docs" / "style.css").read_text(encoding="utf-8")
        pattern = r"\.article-content \.table-display-caption\s*\{([^}]+)\}"
        rule = re.search(pattern, css)
        self.assertIsNotNone(rule)
        self.assertRegex(rule.group(1), r"position\s*:\s*absolute")
        self.assertRegex(rule.group(1), r"clip(?:-path)?\s*:")

    def test_public_pages_omit_the_author_byline(self) -> None:
        for index, (slug, title, category, description) in enumerate(publication.ESSAYS):
            with self.subTest(slug=slug):
                page = publication.render_essay(
                    slug, title, category, description, index, []
                )
                self.assertIn(f"<h1>{publication.esc(title)}</h1>", page)
                self.assertNotIn('<p class="byline">', page)
                self.assertNotIn('<p class="author">', page)

    def test_source_document_theories_are_preserved(self) -> None:
        samples = {
            "semantic-participation": "Member_E(a)",
            "typed-generativity": "P_theta(t : A",
            "functorial-consistency": "T(f(x))",
            "lambek-machines": "Lambek Auxiliary Supervision",
            "algebraic-architectures": "ArchitectureSpec",
            "quantitative-curry-howard": "quantitative_judgment",
            "effectful-and-conceptual-intelligence": "Typed Action Ledger",
            "compositional-intelligence": "This paper introduces Compositional Intelligence",
        }
        for slug, passage in samples.items():
            with self.subTest(slug=slug):
                self.assertIn(
                    passage,
                    (publication.ROOT / "essays" / f"{slug}.md").read_text(encoding="utf-8"),
                )

    def test_semantic_math_for_each_source(self) -> None:
        """Whitelisted mathematics is typeset and annotated in every essay."""
        for slug, title, _, _ in publication.ESSAYS:
            with self.subTest(slug=slug):
                source = (publication.ROOT / "essays" / f"{slug}.md").read_text(
                    encoding="utf-8"
                )
                body, _ = publication.source_to_body(source, title, [])
                enhanced = enhance_scientific_presentation(body)
                self.assertGreater(enhanced.count("<math "), 0)
                self.assertIn('encoding="application/x-tex"', enhanced)
                self.assertIn('alttext="', enhanced)
                self.assertEqual(enhanced, enhance_scientific_presentation(body))

    def test_whitelist_does_not_rewrite_unrecognized_content(self) -> None:
        """Tag attributes and other equations remain untouched."""
        source = '<p data-note="P_theta(t : A | Gamma)">Unknown_X(z) + 1</p>'
        self.assertEqual(render_source_math(source), source)
        converted = render_source_math("<p>P_theta(t : A | Gamma).</p>")
        self.assertIn('alttext="P_theta(t : A | Gamma)"', converted)
        self.assertIn('class="math-scroll"', converted)
        self.assertIn('display="block"', converted)
        css = (publication.ROOT / "docs" / "style.css").read_text(encoding="utf-8")
        rule = re.search(r'\.article-content math\[display="inline"\]\s*\{([^}]+)\}', css)
        self.assertIsNotNone(rule)
        self.assertIn("overflow-x:auto", rule.group(1))

    def test_record_fields_have_preserved_source_order(self) -> None:
        """DOCX paragraph-encoded fields become one readable record."""
        source = ("<p>artifact_record:</p>\n<p>id: string</p>\n"
                  "<p>kind: string</p>\n<p>validation_status: string</p>\n"
                  "<p>repair: string</p>")
        formatted = enhance_scientific_presentation(source)
        self.assertIn('class="record-schema"', formatted)
        self.assertIn("artifact_record:\nid: string\nkind: string", formatted)
        self.assertIn("repair: string</code>", formatted)
        self.assertEqual(len(FORMULAE), len(dict(FORMULAE)))

    def test_display_math_does_not_absorb_adjacent_paragraphs(self) -> None:
        """A formula followed by prose must never engulf the next paragraph."""
        original = (
            "<p>P_theta(t : A | Gamma) is a source transcription.</p>"
            "<p>The comparison uses T(f(x)) ≈ g(T(x)).</p>"
        )
        enhanced = render_source_math(original)
        self.assertEqual(enhanced.count("<p>"), 2)
        self.assertEqual(enhanced.count("</p>"), 2)
        self.assertIn("is a source transcription.</p>", enhanced)
        self.assertIn("The comparison uses ", enhanced)


    def test_hidden_table_labels_keep_literal_source_notation(self) -> None:
        """Only readable manuscript content receives mathematical markup."""
        text = (
            '<p class="table-display-caption">P_theta(t : A | Gamma)</p>'
            '<caption class="visually-hidden">P_theta(t : A | Gamma)</caption>'
            '<p>P_theta(t : A | Gamma)</p>'
        )
        rendered = render_source_math(text)
        self.assertEqual(rendered.count("<math "), 1)
        self.assertIn('<p class="table-display-caption">P_theta(t : A | Gamma)</p>', rendered)
        self.assertIn('<caption class="visually-hidden">P_theta(t : A | Gamma)</caption>', rendered)

    def test_independent_docx_audit_text_extraction(self) -> None:
        """The optional original-DOCX audit excludes generated table labels."""
        reader = Paragraphs()
        example = "An AI-generated theorem requires a precisely stated formal target, explicit assumptions, appropriate dependencies, and an independent validation procedure before downstream reuse."
        reader.feed('<p>' + example + '</p>')
        reader.feed('<p class="table-display-caption">' + example + '</p>')
        self.assertEqual(reader.values, [example])
        index = phrases(tokens(example))
        self.assertEqual(overlap(example, index), 1.0)
        self.assertLess(overlap("Different provenance sentences require review and validation.", index), 0.9)



    def test_flagship_figures_preserve_source_table_and_stage_text(self) -> None:
        """The original two diagrams are exposed as captioned figures."""
        title = "Compositional Intelligence"
        manuscript = (publication.ROOT / "essays" / "compositional-intelligence.md").read_text(
            encoding="utf-8"
        )
        original, _ = publication.source_to_body(manuscript, title, [])
        rendered = render_synthesis_figures(original)
        self.assertEqual(rendered.count('<figure class="ci-source-figure'), 2)
        self.assertEqual(rendered.count("<figcaption"), 2)
        self.assertEqual(rendered.count("<table "), 10)
        self.assertIn('id="table-5"', rendered)
        self.assertIn("Figure. From output to artifact.", rendered)
        self.assertIn("Figure. Functorial Consistency square.", rendered)
        self.assertIn('aria-label="transport T downward"', rendered)
        self.assertIn('class="ci-commuting-mobile-grid"', rendered)
        self.assertEqual(rendered.count('class="ci-square-object"'), 4)
        self.assertEqual(rendered.count('class="ci-square-arrow'), 4)
        self.assertNotIn("<p><strong>output -&gt;", rendered)
        with self.assertRaises(ValueError):
            render_synthesis_figures(rendered)

    def test_flagship_outline_follows_section_semantics(self) -> None:
        """Reset DOCX list counters and nest appendix headings without source edits."""
        manuscript = (
            publication.ROOT / "essays" / "compositional-intelligence.md"
        ).read_text(encoding="utf-8")
        original, _ = publication.source_to_body(
            manuscript, "Compositional Intelligence", []
        )
        self.assertIn('<ol start="6" type="1">', original)
        self.assertIn('<ol start="15" type="1">', original)
        rendered = render_synthesis_figures(original)
        self.assertNotIn('<ol start="6" type="1">', rendered)
        self.assertNotIn('<ol start="15" type="1">', rendered)
        self.assertEqual(rendered.count('<ol type="1">'), 3)
        self.assertIn(
            '<h2 id="appendix-materials-from-the-synthesis-paper">Appendix</h2>',
            rendered,
        )
        for ident in ("claim-levels-and-epistemic-types",
                      "minimal-schema-summaries"):
            self.assertIn(f'<h3 id="{ident}">', rendered)
        for ident in ("claim-levels", "epistemic-types", "artifactrecord",
                      "targettyperecord", "functorialconsistencyitem",
                      "architecturespec", "quantitativejudgmentrecord",
                      "typedactionledgerentry", "concepttransferrecord"):
            self.assertIn(f'<h4 id="{ident}">', rendered)
        self.assertEqual(rendered.count("<table "), original.count("<table "))

    def test_flagship_rendering_is_scoped_and_accessible(self) -> None:
        """The flagship typesetting does not alter another essay's diagrams."""
        page = publication.render_essay(*publication.ESSAYS[0], position=0, table_captions=[])
        self.assertIn('class="ci-source-figure ci-lifecycle"', page)
        self.assertIn('class="ci-source-figure ci-commuting"', page)
        self.assertEqual(page.count("<figcaption"), 2)
        self.assertIn('alttext="S = (E_s, E_t, x, f, T, g, epsilon, V)"', page)
        self.assertIn('alttext="P_theta(A, t | Gamma) = P_theta(A | Gamma) P_theta(t | A, Gamma)"', page)
        self.assertNotIn('class="byline"', page)


    def test_math_display_punctuation_and_multi_expression_safety(self) -> None:
        """Mathematical punctuation stays attached and unrelated math stays separate."""
        single = render_source_math("<p>P_theta(t : A | Gamma).</p>")
        self.assertEqual(single.count('class="math-scroll"'), 1)
        self.assertIn('class="math-display-expression"', single)
        self.assertIn('<span class="math-display-punctuation">.</span>', single)
        self.assertNotIn("</math>.</div>", single)

        multiple = render_source_math("<p>P_theta(t : A | Gamma), A |= S.</p>")
        self.assertEqual(multiple.count("<math "), 2)
        self.assertNotIn('class="math-scroll"', multiple)
        self.assertIn("</math>, ", multiple)

        combined = render_source_math(
            "<p>TaskSpec -&gt; ArchitectureType -&gt; ArchitectureInstance, A |= S.</p>"
        )
        self.assertEqual(combined.count("<math "), 1)
        self.assertEqual(combined.count('class="math-scroll"'), 1)
        self.assertIn("ArchitectureInstance, A |= S", combined)

    def test_original_typed_action_judgment_is_typeset(self) -> None:
        """The synthesis uses the exact authored typed-action transcription."""
        original = (
            "<p>Gamma; M; E; C ⊢ a : Pre -&gt; Post ! epsilon @ rho.</p>"
        )
        rendered = render_source_math(original)
        self.assertEqual(rendered.count('class="math-scroll"'), 1)
        self.assertIn("Gamma; M; E; C ⊢ a : Pre -&gt; Post ! epsilon @ rho", rendered)
        self.assertIn('encoding="application/x-tex"', rendered)

    def test_source_table_labels_are_not_repeated_visually(self) -> None:
        """Retain original caption paragraphs as the single group labels."""
        manuscript = (
            publication.ROOT / "essays" / "compositional-intelligence.md"
        ).read_text(encoding="utf-8")
        original, _ = publication.source_to_body(
            manuscript, "Compositional Intelligence", []
        )
        rendered = render_synthesis_figures(original)
        for number in (1, 2, 3, 4, 6, 7, 8):
            with self.subTest(number=number):
                self.assertIn(
                    f'<p id="table-{number}-caption" '
                    'class="table-display-caption source-visible-caption">',
                    rendered,
                )
                self.assertEqual(
                    rendered.count(f'id="table-{number}-caption"'), 1
                )
        self.assertEqual(rendered.count("source-visible-caption"), 7)
        self.assertIn("Table 9. Claim levels, meanings, and publication treatment.", rendered)
        self.assertIn("Table 10. Epistemic types and their meanings.", rendered)

    def test_synthesis_revised_claims_have_exact_source_scope(self) -> None:
        """Keep the proposed mathematics, comparative evidence, and tests bounded."""
        source = (
            publication.ROOT / "essays" / "compositional-intelligence.md"
        ).read_text(encoding="utf-8")
        self.assertEqual(source.count(
            "S = (E_s, E_t, x, f, T, g, epsilon, V)"
        ), 1)
        self.assertEqual(source.count(
            "P_theta(A, t | Gamma) = P_theta(A | Gamma) P_theta(t | A, Gamma)"
        ), 1)
        self.assertEqual(source.count(
            "<td>w_i -&gt; tau_i -&gt; pi -&gt; [[pi]]</td>"
        ), 1)
        for phrase in (
            "Agreement on a finite collection of squares alone does not establish functoriality.",
            "The acceptance relation need not be symmetric",
            "Metamorphic testing already evaluates relations",
            "Its diagnostic advantage over a well-designed metamorphic test remains an empirical hypothesis.",
            "The evaluator must record path agreement and each path's independently assessed validity as separate observations.",
            "Attributing that disagreement to a particular translation or transformation additionally depends on independently justified reference relations",
            "agreement alone does not establish the correctness of either path",
            "Revised by the evaluated system",
        ):
            if phrase == "Revised by the evaluated system":
                self.assertNotIn(phrase, source)
            else:
                self.assertIn(phrase, source)
        page = publication.render_essay(
            *publication.ESSAYS[0], position=0, table_captions=[]
        )
        self.assertIn('alttext="S = (E_s, E_t, x, f, T, g, epsilon, V)"',page)
        self.assertIn(
            'alttext="P_theta(A, t | Gamma) = P_theta(A | Gamma) P_theta(t | A, Gamma)"',
            page,
        )
        self.assertNotIn(
            "non-commutation reported conditional on both paths passing",
            source,
        )
        self.assertIn("A worked commutation test", page)
        self.assertIn("Pilot identifiability and controls", page)
        self.assertIn("Segura et al., 2016", page)
        self.assertEqual(page.count('data-source-table='), 10)


    def test_synthesis_citations_have_exact_bibliographic_targets(self) -> None:
        """All cited works resolve to one primary-source bibliography entry."""
        catalogue_path = (
            publication.ROOT / "sources" / "synthesis_references.json"
        )
        entries = json.loads(catalogue_path.read_text(encoding="utf-8"))[
            "references"
        ]
        self.assertEqual(len(entries), 35)
        keys = [entry["key"] for entry in entries]
        self.assertEqual(len(keys), len(set(keys)))
        page = publication.render_essay(
            *publication.ESSAYS[0], position=0, table_captions=[]
        )
        self.assertEqual(page.count('<h2 id="references">'), 1)
        self.assertEqual(page.count('class="bibliography-entry"'), 35)
        for key in keys:
            with self.subTest(key=key):
                self.assertEqual(page.count(f'id="ref-{key}"'), 1)
                self.assertIn(f'href="#ref-{key}"', page)
        self.assertIn(
            "AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories",
            page,
        )
        self.assertIn("A Foundation for Differentiable Logics using Dependent Type Theory",page)
        self.assertIn("The Lean Language Reference",page)

    def test_flagship_browser_title_is_not_repeated(self) -> None:
        """The flagship page's browser tab shows the essay title once."""
        page = publication.render_essay(
            *publication.ESSAYS[0], position=0, table_captions=[]
        )
        self.assertIn("<title>Compositional Intelligence | A Framework for AI</title>", page)
        self.assertNotIn(
            "<title>Compositional Intelligence · Compositional Intelligence</title>",
            page,
        )


    def test_flagship_mobile_tables_have_discoverable_scroll_cues(self) -> None:
        """Every horizontal scientific table advertises its off-screen columns."""
        original = (
            publication.ROOT / "essays" / "compositional-intelligence.md"
        ).read_text(encoding="utf-8")
        source, _ = publication.source_to_body(
            original, "Compositional Intelligence", []
        )
        markup = render_synthesis_figures(source)
        self.assertEqual(markup.count('class="table-scroll-hint"'), 9)
        for number in (1, 2, 3, 4, 6, 7, 8, 9, 10):
            with self.subTest(number=number):
                self.assertIn(
                    f'aria-describedby="table-{number}-scroll-hint"',
                    markup,
                )
                self.assertIn(
                    f'id="table-{number}-scroll-hint"', markup
                )
        self.assertNotIn('id="table-5-scroll-hint"', markup)



    def test_collection_navigation_metadata_and_browser_titles(self) -> None:
        """Differentiate search titles without changing authored page headings."""
        for index, (slug, title, category, description) in enumerate(publication.ESSAYS):
            with self.subTest(slug=slug):
                page = publication.render_essay(
                    slug, title, category, description,
                    position=index, table_captions=[]
                )
                self.assertEqual(
                    re.findall(r"<title>([^<]*)</title>", page),
                    [publication.discovery.CONCEPTS[slug]["seo_title"]]
                )
                self.assertEqual(
                    re.findall(r'<meta property="og:title" content="([^"]+)"',page),
                    [escape(title)]
                )
                self.assertEqual(
                    re.findall(r'<link rel="canonical" href="([^"]+)"',page),
                    [publication.BASE + f"essays/{slug}.html"]
                )
                self.assertEqual(page.count('class="article-toc"'), 1)
                self.assertEqual(page.count('aria-label="Essay navigation"'), 1)
                self.assertNotIn('class="byline"', page)
                self.assertEqual(page.count("<h1>"), 1)


    def test_discovery_index_is_source_grounded_and_schema_valid(self) -> None:
        """Each generated article has one non-executable discovery graph."""
        metadata = publication.discovery
        metadata.validate_inventory(publication.ESSAYS)
        self.assertEqual(len(set(data["seo_title"] for data in metadata.CONCEPTS.values())), 8)
        for position, (slug, title, category, description) in enumerate(publication.ESSAYS):
            with self.subTest(slug=slug):
                page = publication.render_essay(
                    slug, title, category, description,
                    position=position, table_captions=[],
                )
                match = re.search(
                    r'<script type="application/ld\+json">(.*?)</script>', page, re.S
                )
                self.assertIsNotNone(match)
                self.assertEqual(page.count('<script type="application/ld+json">'), 1)
                graph = json.loads(match.group(1))["@graph"]
                article = next(item for item in graph if item["@type"] == "Article")
                self.assertEqual(article["headline"], title)
                self.assertEqual(
                    article["url"], publication.BASE + "essays/" + slug + ".html"
                )
                self.assertEqual(article["author"]["@id"], metadata.AUTHOR_ID)
                self.assertNotIn("datePublished", article)
                self.assertNotIn("dateModified", article)
                self.assertEqual(article["keywords"], metadata.CONCEPTS[slug]["topics"])
                self.assertIn("<h1>" + escape(title) + "</h1>", page)
                self.assertIn('rel="canonical"', page)
                self.assertIn('href="../corpus.json"', page)
                self.assertNotIn('<script src=', page)

        overview = metadata.homepage_graph(publication.ESSAYS)["@graph"]
        items = next(item for item in overview if item["@type"] == "ItemList")
        self.assertEqual(
            [x["position"] for x in items["itemListElement"]],
            list(range(1, 9)),
        )
        concepts = metadata.render_concepts(publication.ESSAYS)
        self.assertEqual(concepts.count('class="concept-entry"'), 8)
        self.assertIn('<h1>Concepts in Compositional Intelligence</h1>', concepts)
        self.assertEqual(concepts.count('type="application/ld+json"'), 1)

    def test_flagship_source_exact_mobile_table_parity(self) -> None:
        """All nine source data tables have lossless mobile records; square stays intact."""
        import render_synthesis

        slug, title, category, description = publication.ESSAYS[0]
        manuscript = (publication.ROOT / "essays" / f"{slug}.md").read_text(
            encoding="utf-8"
        )
        original, _ = publication.source_to_body(manuscript, title, [])
        scientific = enhance_scientific_presentation(
            render_synthesis_figures(original)
        )
        styled = render_synthesis.render_synthesis_mobile_tables(scientific)
        page = publication.render_essay(slug,title,category,description,0,[])
        linked = render_synthesis_references(
            styled, publication.ROOT / "sources" / "synthesis_references.json"
        )
        self.assertIn(linked,page)
        self.assertEqual(page.count('class="ci-data-mobile ci-data-mobile-'),9)
        self.assertEqual(page.count('class="ci-data-card"'),52)
        self.assertEqual(page.count('class="ci-data-field"'),151)
        self.assertEqual(page.count('data-ci-alternative="mobile"'),9)
        self.assertEqual(page.count('class="ci-commuting-mobile"'),1)
        total_rows=total_cells=0
        for number in (1,2,3,4,6,7,8,9,10):
            with self.subTest(table=number):
                source_table = re.search(
                    rf'<table data-source-table="{number}" id="table-{number}">'
                    r'[\s\S]*?</table>', scientific
                )
                published_table = re.search(
                    rf'<table data-source-table="{number}" id="table-{number}">'
                    r'[\s\S]*?</table>', styled
                )
                self.assertIsNotNone(source_table)
                self.assertIsNotNone(published_table)
                self.assertEqual(source_table.group(),published_table.group())
                source_head = re.search(
                    r'<thead>([\s\S]*?)</thead>', source_table.group()
                )
                self.assertIsNotNone(source_head)
                labels = [
                    unescape(re.sub(r"<[^>]+>", "", value)).strip()
                    for value in re.findall(
                        r'<th\b[^>]*>([\s\S]*?)</th>', source_head.group(1)
                    )
                ]
                self.assertEqual(
                    len(labels), render_synthesis._SOURCE_DATA_COLUMNS[number]
                )
                rows = re.findall(
                    r'<tr\b[^>]*>([\s\S]*?)</tr>',
                    re.search(
                        r'<tbody>([\s\S]*?)</tbody>',source_table.group()
                    ).group(1)
                )
                expected = [
                    re.findall(r'<td(?:\s[^>]*)?>([\s\S]*?)</td>',row)
                    for row in rows
                ]
                cards = re.search(
                    rf'<section class="ci-data-mobile ci-data-mobile-{number}" '
                    rf'aria-labelledby="table-{number}-caption">'
                    r'([\s\S]*?)</section>',styled
                )
                self.assertIsNotNone(cards)
                mobile_rows = re.findall(
                    r'<dl class="ci-data-card">([\s\S]*?)</dl>',cards.group(1)
                )
                self.assertEqual(len(mobile_rows),len(expected))
                for row,card in zip(expected,mobile_rows,strict=True):
                    self.assertEqual(
                        row,
                        re.findall(r'<dd>([\s\S]*?)</dd>',card)
                    )
                    self.assertEqual(
                        re.findall(r'<dt>([^<]*)</dt>',card),
                        labels,
                        "Mobile data labels must match every original column"
                    )
                    total_cells+=len(row)
                total_rows+=len(mobile_rows)
        self.assertEqual((total_rows,total_cells),(52,151))
        with self.assertRaises(ValueError):
            render_synthesis.render_synthesis_mobile_tables(styled)

    def test_semantic_participation_mobile_tables_are_source_equivalent(self) -> None:
        """All original cells survive, and every mobile cell is copied verbatim."""
        slug, title, _, _ = publication.ESSAYS[1]
        source = (publication.ROOT / "essays" / f"{slug}.md").read_text(
            encoding="utf-8"
        )
        original, _ = publication.source_to_body(source, title, [])
        enhanced = enhance_scientific_presentation(original)
        rendered = render_semantic_participation(enhanced)
        self.assertEqual(rendered.count('data-sp-alternative="mobile"'), 12)
        self.assertEqual(rendered.count('<dl class="sp-mobile-record'), 74)
        self.assertEqual(rendered.count('class="sp-record-field"'), 190)
        original_cells = 0
        copied_cells = 0
        for number in range(1, 13):
            with self.subTest(table=number):
                source_table = re.search(
                    rf'<table data-source-table="{number}" id="table-{number}">'
                    r'[\s\S]*?</table>', enhanced,
                )
                output_table = re.search(
                    rf'<table data-source-table="{number}" id="table-{number}">'
                    r'[\s\S]*?</table>', rendered,
                )
                self.assertIsNotNone(source_table)
                self.assertIsNotNone(output_table)
                published_table = output_table.group()
                if number == 2:
                    published_table = re.sub(r"</?a\b[^>]*>", "", published_table)
                # Native captions were synthesized during conversion, not
                # authored DOCX cells. Compare exact source structure
                # without these publication-only accessibility descriptions.
                def without_generated_caption(text: str) -> str:
                    return re.sub(
                        r'<caption class="visually-hidden">[^<]*</caption>',
                        '<caption class="visually-hidden"></caption>',
                        text,
                    )
                self.assertEqual(
                    without_generated_caption(source_table.group()),
                    without_generated_caption(published_table),
                )
                source_rows = re.findall(
                    r'<tr\b[^>]*>([\s\S]*?)</tr>',
                    re.search(
                        r'<tbody>([\s\S]*?)</tbody>', source_table.group()
                    ).group(1),
                )
                self.assertEqual(len(source_rows), _ROW_COUNTS[number])
                source_fields = [
                    re.findall(r'<td(?:\s[^>]*)?>([\s\S]*?)</td>', row)
                    for row in source_rows
                ]
                original_cells += sum(len(row) for row in source_fields)
                mobile = re.search(
                    rf'<section class="sp-mobile-records sp-mobile-table-{number}" '
                    rf'aria-labelledby="table-{number}-caption">'
                    r'([\s\S]*?)</section>',
                    rendered,
                )
                self.assertIsNotNone(mobile)
                records = re.findall(
                    r'<dl class="sp-mobile-record[^"]*">([\s\S]*?)</dl>',
                    mobile.group(1),
                )
                rows_to_copy = (
                    [row for i, row in enumerate(source_fields) if i != 9]
                    if number == 6 else source_fields
                )
                self.assertEqual(len(records), len(rows_to_copy))
                source_heading = re.search(
                    r"<thead>([\s\S]*?)</thead>", source_table.group()
                )
                self.assertIsNotNone(source_heading)
                source_labels = [
                    unescape(re.sub(r"<[^>]+>", "", item)).strip()
                    for item in re.findall(
                        r"<th\b[^>]*>([\s\S]*?)</th>",
                        source_heading.group(1),
                    )
                ]
                for record_index, (original_row, record) in enumerate(
                    zip(rows_to_copy, records, strict=True)
                ):
                    record_labels = re.findall(r"<dt>([^<]+)</dt>", record)
                    if number == 6:
                        # Original table 6 contains two separately named
                        # regions in one table. Its tenth row is a subheading.
                        expected_labels = (
                            source_labels[:3] if record_index < 9
                            else ["Type transition", "Required control"]
                        )
                    else:
                        expected_labels = source_labels
                    self.assertEqual(
                        record_labels, expected_labels,
                        f"Table {number}, mobile record {record_index + 1}: "
                        "source column labels differ"
                    )
                    mobile_cells = re.findall(
                        r'<dd>([\s\S]*?)</dd>', record,
                    )
                    if number == 2:
                        mobile_cells = [
                            re.sub(r"</?a\b[^>]*>", "", cell)
                            for cell in mobile_cells
                        ]
                    self.assertEqual(original_row, mobile_cells)
                    copied_cells += len(mobile_cells)
        self.assertEqual(original_cells, 192)
        self.assertEqual(copied_cells, 190)
        self.assertIn('class="sp-transition-head"', rendered)
        self.assertIn("Type transition", rendered)
        self.assertIn("Required control", rendered)

    def test_semantic_participation_formal_objects_remain_source_bound(self) -> None:
        """Author's sequence, memberships and schema fields stay legible."""
        slug, title, category, description = publication.ESSAYS[1]
        source = (publication.ROOT / "essays" / f"{slug}.md").read_text(
            encoding="utf-8"
        )
        body, _ = publication.source_to_body(source, title, [])
        enhanced = enhance_scientific_presentation(body)
        output = render_semantic_participation(enhanced)
        self.assertEqual(output.count('class="sp-sequence"'), 1)
        self.assertIn('aria-label="Original membership-to-action sequence"', output)
        self.assertIn('class="sp-criterion"', output)
        self.assertIn('class="sp-transport"', output)
        self.assertEqual(
            len(re.findall(r'class="sp-source-schema(?:\s|")', output)), 4
        )
        self.assertEqual(output.count('class="sp-schema-entry"'), 10)
        self.assertIn("SemanticEnvironment E = {", output)
        self.assertIn("ArtifactRecord a = {", output)
        self.assertIn("TransportRecord rho_T = {", output)
        self.assertIn("semantic_participation_item:", output)
        self.assertIn('class="sp-proof-example"', output)
        self.assertIn("expected shape", output)
        self.assertIn("f y &lt;= f x", output)
        self.assertIn('alttext="T : (a, E_s) -&gt; (b, E_t, rho_T)"', output)
        self.assertIn('alttext="Delta_L(c) = F(L + c) - F(L)"', output)
        self.assertEqual(output.count('<table data-source-table='), 12)
        self.assertEqual(
            len(re.findall(r'<h2\b|<h3\b', output)),
            self.documents[slug]["heading_count"],
        )
        with self.assertRaises(ValueError):
            render_semantic_participation(output)
        page = publication.render_essay(
            slug, title, category, description, 2, [],
        )
        self.assertIn(output, page)
        self.assertNotIn('<p class="byline">', page)


    def test_semantic_reader_map_links_without_changing_author_text(self) -> None:
        """Link all existing targets; retain the source's unresolved 6.1 reference."""
        slug, title, category, description = publication.ESSAYS[1]
        page = publication.render_essay(
            slug, title, category, description, 2, [],
        )
        table = re.search(
            r'<table data-source-table="2" id="table-2">[\s\S]*?</table>',
            page,
        )
        self.assertIsNotNone(table)
        links = re.findall(r'<a href="#([^"]+)">([^<]+)</a>', table.group())
        self.assertEqual(len(links), 22)
        for fragment, label in links:
            with self.subTest(fragment=fragment):
                self.assertIn(f'id="{fragment}"', page)
                self.assertTrue(label.strip())
        self.assertIn("6.1", table.group())
        self.assertNotIn('>6.1</a>', table.group())
        mobile = re.search(
            r'<section class="sp-mobile-records sp-mobile-table-2" '
            r'aria-labelledby="table-2-caption">([\s\S]*?)</section>',
            page,
        )
        self.assertIsNotNone(mobile)
        self.assertEqual(mobile.group().count('href="#'), 22)


    def test_semantic_environment_source_field_definitions_are_exact(self) -> None:
        """All ten technical fields retain their original names and meanings."""
        slug, title, _, _ = publication.ESSAYS[1]
        manuscript = (
            publication.ROOT / "essays" / f"{slug}.md"
        ).read_text(encoding="utf-8")
        original, _ = publication.source_to_body(manuscript, title, [])
        rendered = render_semantic_participation(
            enhance_scientific_presentation(original)
        )
        block = re.search(
            r'<blockquote>\s*<p>SemanticEnvironment E = \{<br\s*/?>'
            r'([\s\S]*?)<br\s*/?>\s*\}</p>\s*</blockquote>',
            original,
        )
        self.assertIsNotNone(block)
        source_lines = [
            unescape(line).strip()
            for line in re.split(r"<br\s*/?>", block.group(1))
        ]
        formatted = re.search(
            r'<dl class="sp-environment-fields">([\s\S]*?)</dl>',
            rendered,
        )
        self.assertIsNotNone(formatted)
        pairs = re.findall(
            r'<div class="sp-schema-entry"><dt><code>([^<]+)</code></dt>'
            r'<dd>([\s\S]*?)</dd></div>',
            formatted.group(1),
        )
        self.assertEqual(len(pairs), 10)
        recovered = [
            unescape(field) + " " + unescape(
                re.sub(r"<[^>]+>", "", meaning)
            )
            for field, meaning in pairs
        ]
        self.assertEqual(recovered, source_lines)

    def test_semantic_table_captions_are_concise_and_source_neutral(self) -> None:
        """The twelve generated captions describe the original tables once."""
        from render_semantic import _ACCESSIBLE_TABLE_CAPTIONS

        slug, title, category, description = publication.ESSAYS[1]
        page = publication.render_essay(
            slug, title, category, description, 2, [],
        )
        for number, caption in _ACCESSIBLE_TABLE_CAPTIONS.items():
            with self.subTest(table=number):
                self.assertEqual(
                    page.count(
                        f'<p class="table-display-caption" id="table-{number}-caption">'
                        f'{caption}</p>'
                    ), 1,
                )
                self.assertEqual(
                    page.count(
                        '<caption class="visually-hidden">' +
                        caption + '</caption>'
                    ), 1,
                )
        self.assertNotIn(
            "Governing claim — Governing claim", page
        )

    def test_semantic_governing_claim_keeps_accessible_field_label(self) -> None:
        """Mobile-only CSS visually clips the original label, without hiding it."""
        css = (publication.ROOT / "docs" / "style.css").read_text(
            encoding="utf-8"
        )
        rule = re.search(
            r'\.article-content \.sp-mobile-table-3 '
            r'\.sp-record-field dt\s*\{([^}]*)\}',
            css,
        )
        self.assertIsNotNone(rule)
        self.assertNotIn("display:none", rule.group(1))
        self.assertIn("position:absolute", rule.group(1))
        self.assertIn("clip-path:inset(50%)", rule.group(1))


    def test_typed_generativity_preserves_every_source_table_cell(self) -> None:
        """All 227 Word-derived data cells are reproduced exactly on phones."""
        slug, title, category, description = publication.ESSAYS[2]
        manuscript = (publication.ROOT / "essays" / f"{slug}.md").read_text(
            encoding="utf-8"
        )
        original, _ = publication.source_to_body(manuscript, title, [])
        source = enhance_scientific_presentation(original)
        page = publication.render_essay(
            slug, title, category, description, 3, []
        )
        self.assertEqual(page.count('data-tg-alternative="mobile"'), 15)
        self.assertEqual(page.count('<dl class="tg-mobile-record">'), 81)
        self.assertEqual(page.count('class="tg-record-field"'), 227)
        self.assertEqual(sum(TG_ROWS.values()), 81)
        self.assertEqual(len(TG_HEADERS), 15)

        total_source = 0
        total_mobile = 0
        for n in range(1, 16):
            with self.subTest(table=n):
                pattern = (
                    rf'<table data-source-table="{n}" id="table-{n}">'
                    r'[\s\S]*?</table>'
                )
                original_table = re.search(pattern, source)
                published_table = re.search(pattern, page)
                self.assertIsNotNone(original_table)
                self.assertIsNotNone(published_table)
                src_html = original_table.group()
                out_html = published_table.group()
                if n == 2:
                    # V5 has a real Section 7.4. Remove renderer-added links
                    # before the table's original cell content is compared.
                    out_html = re.sub(r'</?a\b[^>]*>', '', out_html)

                def strip_source_symbol_math(html: str) -> str:
                    return re.sub(
                        r'<math display="inline" alttext="([^"]+)">'
                        r'<semantics>[\s\S]*?</semantics></math>',
                        lambda match: unescape(match.group(1)),
                        html,
                    )

                if n == 3:
                    original_symbol_math = re.findall(
                        r'<td><math display="inline" alttext="([^"]+)">',
                        out_html,
                    )
                    self.assertEqual(
                        original_symbol_math,
                        ["Gamma", "A", "t", "theta", "P_theta"],
                    )
                    out_html = strip_source_symbol_math(out_html)

                def without_generated_caption(html: str) -> str:
                    return re.sub(
                        r'<caption class="visually-hidden">[^<]*</caption>',
                        '<caption class="visually-hidden"></caption>', html,
                    )
                self.assertEqual(
                    without_generated_caption(src_html),
                    without_generated_caption(out_html),
                )
                source_body = re.search(r'<tbody>([\s\S]*?)</tbody>', src_html)
                self.assertIsNotNone(source_body)
                rows = re.findall(
                    r'<tr\b[^>]*>([\s\S]*?)</tr>', source_body.group(1)
                )
                self.assertEqual(len(rows), TG_ROWS[n])
                cells = [
                    re.findall(r'<td(?:\s[^>]*)?>([\s\S]*?)</td>', row)
                    for row in rows
                ]
                total_source += sum(len(row) for row in cells)
                mobile = re.search(
                    rf'<section class="tg-mobile-records tg-mobile-table-{n}" '
                    rf'aria-labelledby="table-{n}-caption">'
                    r'([\s\S]*?)</section>', page,
                )
                self.assertIsNotNone(mobile)
                cards = re.findall(
                    r'<dl class="tg-mobile-record">([\s\S]*?)</dl>',
                    mobile.group(1),
                )
                self.assertEqual(len(cards), len(rows))
                head = re.search(r"<thead>([\s\S]*?)</thead>", src_html)
                self.assertIsNotNone(head)
                labels = [
                    unescape(re.sub(r"<[^>]*>", "", cell)).strip()
                    for cell in re.findall(
                        r"<th\b[^>]*>([\s\S]*?)</th>", head.group(1)
                    )
                ]
                self.assertEqual(tuple(labels), TG_HEADERS[n])
                for original_cells, card in zip(cells, cards, strict=True):
                    self.assertEqual(
                        re.findall(r"<dt>([^<]+)</dt>", card),
                        labels,
                        f"Typed table {n}: mobile field labels must match source headers",
                    )
                    values = re.findall(r'<dd>([\s\S]*?)</dd>', card)
                    if n == 2:
                        values = [
                            re.sub(r'</?a\b[^>]*>', '', value)
                            for value in values
                        ]
                    if n == 3:
                        values = [strip_source_symbol_math(value) for value in values]
                    self.assertEqual(original_cells, values)
                    total_mobile += len(values)
        self.assertEqual(total_source, 227)
        self.assertEqual(total_mobile, 227)

    def test_typed_generativity_structural_readability(self) -> None:
        """Original sequences, domain cases, and record schemas remain exact."""
        slug, title, category, description = publication.ESSAYS[2]
        manuscript = (publication.ROOT / "essays" / f"{slug}.md").read_text(
            encoding="utf-8"
        )
        original, _ = publication.source_to_body(manuscript, title, [])
        source = enhance_scientific_presentation(original)
        rendered = render_typed_generativity(source)
        self.assertEqual(rendered.count('class="tg-sequence"'), 2)
        self.assertEqual(rendered.count('<div class="tg-domain-example"'), 4)
        self.assertEqual(rendered.count('class="tg-example-line"'), 13)
        self.assertEqual(rendered.count('class="tg-record-pair"'), 1)
        self.assertEqual(rendered.count('class="tg-type-schema"'), 4)
        self.assertEqual(rendered.count('class="tg-schema-field"'), 45)

        originals = re.findall(
            r'<div class="record-schema" role="group" tabindex="0" '
            r'aria-label="Source record [^"]+">'
            r'<pre><code>([\s\S]*?)</code></pre></div>', source,
        )
        self.assertEqual(len(originals), 3)
        first, second, third = originals
        target, candidate = second.split('\n\ncandidate_inhabitant_record:\n')
        expected = {
            "type_first_item": first,
            "target_type_record": target,
            "candidate_inhabitant_record": "candidate_inhabitant_record:\n" + candidate,
            "typed_generativity_benchmark_item": third,
        }
        actual = re.findall(
            r'<div class="tg-type-schema" role="group" '
            r'aria-label="Source record ([^"]+)">'
            r'<div class="tg-schema-title"><code>([^<]+)</code></div>'
            r'<dl class="tg-schema-fields">([\s\S]*?)</dl></div>',
            rendered,
        )
        self.assertEqual(len(actual), 4)
        self.assertEqual({label for label, _, _ in actual}, set(expected))
        for label, heading, fields_html in actual:
            with self.subTest(record=label):
                fields = re.findall(
                    r'<div class="tg-schema-field"><dt><code>([^<]+)</code></dt>'
                    r'<dd><code>([^<]+)</code></dd></div>',
                    fields_html,
                )
                recovered = unescape(heading) + '\n' + '\n'.join(
                    unescape(field) + ' ' + unescape(value)
                    for field, value in fields
                )
                self.assertEqual(recovered, expected[label])
        for source_case, published_case in zip(
            re.findall(r'<p>(Prompt:[\s\S]*?)</p>', source),
            re.findall(
                r'<div class="tg-domain-example"[^>]*>'
                r'[\s\S]*?</div></div>', rendered,
            ),
            strict=True,
        ):
            source_lines = re.split(r'<br\s*/?>\s*', source_case)
            rendered_lines = re.findall(
                r'<div class="tg-example-line">([\s\S]*?)</div>',
                published_case,
            )
            self.assertEqual(source_lines, rendered_lines)

        page = publication.render_essay(
            slug, title, category, description, 3, [],
        )
        self.assertIn(rendered, page)
        with self.assertRaises(ValueError):
            render_typed_generativity(rendered)

    def test_typed_reader_map_links_only_existing_targets(self) -> None:
        """Verify reader-map anchors including the authored Section 7.4."""
        slug, title, category, description = publication.ESSAYS[2]
        page = publication.render_essay(
            slug, title, category, description, 3, [],
        )
        table = re.search(
            r'<table data-source-table="2" id="table-2">[\s\S]*?</table>',
            page,
        )
        self.assertIsNotNone(table)
        anchors = re.findall(
            r'<a href="#([^"]+)"(?:\s+[^>]*)?>([^<]+)</a>', table.group(),
        )
        self.assertEqual(len(anchors), 23)
        for fragment, text in anchors:
            with self.subTest(target=fragment):
                self.assertIn(f'id="{fragment}"', page)
                self.assertTrue(text)
        self.assertIn(
            '<a href="semantic-participation.html">Essay 1</a>',
            table.group(),
        )
        self.assertIn(
            '<a href="functorial-consistency.html">Essay 3</a>',
            table.group(),
        )
        self.assertIn(
            '<a href="#identification-and-analysis-protocol">7.4</a>',
            table.group(),
        )
        self.assertNotIn('data-source-reference="7.4"', table.group())
        self.assertIn(
            "Sections 6.4, 7.4, 8, 9, and 11",
            (publication.ROOT / "essays" / "typed-generativity.md").read_text(
                encoding="utf-8"
            ),
        )
        self.assertEqual(
            page.count('class="tg-scroll-hint"'), 15,
        )


    def test_typed_symbol_math_retains_original_transcriptions(self) -> None:
        """Each source symbol is readable as mathematics, never renamed."""
        slug, title, category, description = publication.ESSAYS[2]
        page = publication.render_essay(
            slug, title, category, description, 3, [],
        )
        symbols = ["Gamma", "A", "t", "theta", "P_theta"]
        table = re.search(
            r'<table data-source-table="3" id="table-3">[\s\S]*?</table>',
            page,
        )
        mobile = re.search(
            r'<section class="tg-mobile-records tg-mobile-table-3" '
            r'aria-labelledby="table-3-caption">[\s\S]*?</section>',
            page,
        )
        self.assertIsNotNone(table)
        self.assertIsNotNone(mobile)
        for label, html in (("table", table.group()), ("mobile", mobile.group())):
            with self.subTest(location=label):
                tokens = re.findall(
                    r'<math display="inline" alttext="([^"]+)">',
                    html,
                )
                self.assertEqual(tokens, symbols)
                self.assertEqual(
                    html.count('encoding="application/x-tex"'), 5
                )
                self.assertIn('<mi>Γ</mi>', html)
                self.assertIn('<mi>θ</mi>', html)
                self.assertIn(
                    '<msub><mi>P</mi><mi>θ</mi></msub>', html,
                )

    def test_typed_long_record_heading_keeps_one_line_on_320px(self) -> None:
        """Prevent another orphan colon in the longest technical schema title."""
        stylesheet = (publication.ROOT / "docs" / "style.css").read_text(
            encoding="utf-8"
        )
        match = re.search(
            r'@media\s*\(max-width:375px\)\s*\{[\s\S]*?'
            r'\.article-content \.tg-type-schema'
            r'\[aria-label="Source record typed_generativity_benchmark_item"\]'
            r' \.tg-schema-title\s*\{([^}]*)\}',
            stylesheet,
        )
        self.assertIsNotNone(match)
        self.assertIn("font-size:clamp(12.5px,3.9vw,14px)", match.group(1))
        self.assertIn(
            "grid-template-columns:minmax(180px,290px) minmax(0,1fr);",
            stylesheet,
        )


    def test_functorial_original_tables_match_every_mobile_field(self) -> None:
        """Preserve all 419 source cells across 19 source tables and mobile views."""
        slug, title, category, description = publication.ESSAYS[3]
        text = (publication.ROOT / "essays" / f"{slug}.md").read_text(
            encoding="utf-8"
        )
        source, _ = publication.source_to_body(text, title, [])
        source = publication.enhance_scientific_presentation(
            render_functorial_diagram(source)
        )
        rendered = render_functorial_tables(source)
        page = publication.render_essay(slug, title, category, description, 4, [])
        self.assertIn(rendered, page)
        self.assertEqual(page.count('data-fc-alternative="mobile"'), 19)
        self.assertEqual(page.count('<dl class="fc-mobile-record">'), 156)
        self.assertEqual(page.count('class="fc-record-field"'), 419)
        self.assertEqual(sum(FC_ROWS.values()), 156)

        source_cells = 0
        mobile_cells = 0
        for number in range(1, 20):
            with self.subTest(table=number):
                regex = (
                    rf'<table data-source-table="{number}" id="table-{number}">'
                    r'[\s\S]*?</table>'
                )
                original = re.search(regex, source)
                output = re.search(regex, rendered)
                self.assertIsNotNone(original)
                self.assertIsNotNone(output)
                def generated_caption_empty(html: str) -> str:
                    return re.sub(
                        r'<caption class="visually-hidden">[^<]*</caption>',
                        '<caption class="visually-hidden"></caption>',
                        html,
                    )
                self.assertEqual(
                    generated_caption_empty(original.group()),
                    generated_caption_empty(output.group()),
                )
                tbody = re.search(r'<tbody>([\s\S]*?)</tbody>', original.group())
                self.assertIsNotNone(tbody)
                rows = re.findall(r'<tr\b[^>]*>([\s\S]*?)</tr>', tbody.group(1))
                self.assertEqual(len(rows), FC_ROWS[number])
                original_cells = [
                    re.findall(r'<td(?:\s[^>]*)?>([\s\S]*?)</td>', row)
                    for row in rows
                ]
                self.assertTrue(all(len(row) == len(FC_HEADERS[number])
                                    for row in original_cells))
                mobile = re.search(
                    rf'<section class="fc-mobile-records fc-mobile-table-{number}" '
                    rf'aria-labelledby="table-{number}-caption">'
                    r'([\s\S]*?)</section>', rendered
                )
                self.assertIsNotNone(mobile)
                cards = re.findall(
                    r'<dl class="fc-mobile-record">([\s\S]*?)</dl>',
                    mobile.group(1)
                )
                self.assertEqual(len(cards), len(original_cells))
                for row, card in zip(original_cells, cards, strict=True):
                    mobile_values = re.findall(r'<dd>([\s\S]*?)</dd>', card)
                    if number in (8, 9):
                        mobile_values = [
                            re.sub(r'</?span\b[^>]*>', '', cell)
                            for cell in mobile_values
                        ]
                    self.assertEqual(row, mobile_values)
                    source_cells += len(row)
                    mobile_cells += len(row)
        self.assertEqual(source_cells, 419)
        self.assertEqual(mobile_cells, 419)
        self.assertEqual(page.count('class="fc-field-attribute"'), 12)
        self.assertEqual(page.count('class="fc-field-object"'), 12)

    def test_functorial_diagram_preserves_original_path_condition(self) -> None:
        """Retain both authorial routes and their explicitly qualified agreement."""
        slug, title, category, description = publication.ESSAYS[3]
        text = (publication.ROOT / "essays" / f"{slug}.md").read_text(
            encoding="utf-8"
        )
        source, _ = publication.source_to_body(text, title, [])
        self.assertIn("T(f(x)) ~ g(T(x))</p>", source)
        self.assertIn("source object x -- f --&gt;", source)
        diagram = render_functorial_diagram(source)
        self.assertEqual(diagram.count('class="fc-commuting"'), 1)
        self.assertEqual(diagram.count('class="fc-square-node'), 4)
        self.assertEqual(diagram.count('class="fc-horizontal-arrow"'), 2)
        self.assertEqual(diagram.count('class="fc-down-arrow"'), 2)
        self.assertEqual(diagram.count('class="fc-square-relation"'), 1)
        self.assertIn('aria-label="Paths compared under the stated equivalence regime"', diagram)
        self.assertEqual(diagram.count('<figcaption>'), 1)
        self.assertIn('class="fc-condition-formula">T(f(x)) ~ g(T(x))', diagram)
        self.assertIn('class="fc-node-math">g(T(x))</span>', diagram)
        self.assertNotIn("source object x -- f --&gt;", diagram)
        with self.assertRaises(ValueError):
            render_functorial_diagram(diagram)
        page = publication.render_essay(slug, title, category, description, 4, [])
        self.assertIn('alttext="T(f(x)) ~ g(T(x))"', page)
        self.assertIn('encoding="application/x-tex"', page)
        self.assertEqual(page.count('class="fc-commuting"'), 1)
        self.assertEqual(page.count('<figcaption>'), 1)

    def test_functorial_captions_preserve_original_visible_labels(self) -> None:
        """Reader-visible captions remain authored; AT captions describe the same table."""
        slug, title, category, description = publication.ESSAYS[3]
        source, _ = publication.source_to_body(
            (publication.ROOT / "essays" / f"{slug}.md").read_text(
                encoding="utf-8"
            ), title, []
        )
        page = publication.render_essay(slug, title, category, description, 4, [])
        for number, label in SOURCE_TABLE_LABELS.items():
            with self.subTest(table=number):
                visible = re.search(
                    rf'<p>(Table {label}\. [^<]+)</p>',
                    source
                )
                self.assertIsNotNone(visible)
                self.assertIn(visible.group(), page)
                paragraph = re.search(
                    rf'<p class="table-display-caption" '
                    rf'id="table-{number}-caption">([^<]+)</p>',
                    page
                )
                self.assertIsNotNone(paragraph)
                self.assertEqual(paragraph.group(1).split(" — ")[0],
                                 visible.group(1))
                self.assertGreaterEqual(len(paragraph.group(1)), 30)
                self.assertIn(
                    '<caption class="visually-hidden">' +
                    paragraph.group(1) + '</caption>',
                    page
                )
        self.assertEqual(page.count('class="fc-scroll-hint"'), 19)



    def test_lambek_editorial_publication(self) -> None:
        """Validate the new source-based scientific presentation and test artifact."""
        slug, title, category, description = publication.ESSAYS[4]
        source = (publication.ROOT / "essays" / f"{slug}.md").read_text(encoding="utf-8")
        body, digest = publication.source_to_body(source, title, [])
        page = publication.render_essay(slug, title, category, description, 4, [])
        self.assertEqual(digest, hashlib.sha256(source.encode("utf-8")).hexdigest())
        self.assertEqual(body.count('class="table-scroll"'), 4)
        self.assertEqual(page.count('<table id="table-'), 4)
        self.assertGreater(body.count("<math "), 5)
        self.assertIn('alttext="', page)
        self.assertIn('encoding="application/x-tex"', page)
        annotations = re.findall(
            r'<annotation encoding="application/x-tex">(.*?)</annotation>',
            page, re.S,
        )
        self.assertGreater(len(annotations), 5)
        for annotation in annotations:
            self.assertNotIn("<math", annotation, "MathML annotation cannot nest MathML")
        self.assertIn("A limit of the commutation test", page)
        self.assertIn("Minimal FLC validator contract", page)
        self.assertNotIn('class="lm-square-figure"', page)
        for number in range(1, 5):
            with self.subTest(table=number):
                self.assertIn(f'id="table-{number}-caption"', page)
                self.assertIn(f'id="table-{number}"', page)
        candidate = re.search(r"\x60{3}json\s*([\s\S]*?)\x60{3}", source)
        self.assertIsNotNone(candidate)
        self.assertEqual(json.loads(candidate.group(1))["annotation_status"],
                         "illustrative_unvalidated")


    def test_algebraic_editorial_presentation(self) -> None:
        """The editorial essay retains mathematics, references, and a structured example."""
        slug, title, category, description = publication.ESSAYS[5]
        source = (publication.ROOT / "essays" / f"{slug}.md").read_text(encoding="utf-8")
        body, _ = publication.source_to_body(source, title, [])
        page = publication.render_essay(slug, title, category, description, 5, [])
        self.assertEqual(len(re.findall(r"<h[23]\b", body)), 17)
        self.assertEqual(body.count("<table "), 0)
        self.assertGreaterEqual(page.count('class="math-scroll"'), 11)
        self.assertEqual(page.count('display="block"'), 11)
        for heading in ("preservation-under-composition", "molecular-energy-and-forces",
                        "how-the-proposal-would-be-tested", "references"):
            self.assertIn(f'id="{heading}"', page)
        self.assertIn("atomistic_energy_force_v1", page)
        self.assertIn("Architecture Specification Catalog", page)
        self.assertNotIn('class="aa-mobile"', page)
        self.assertNotIn("AUTHORITATIVE-DOCX SHA256", source)

    def test_quantitative_source_bound_presentation(self) -> None:
        """Quantitative judgments and every cell/record retain exact source text."""
        import render_quantitative as quantitative

        slug, title, category, description = publication.ESSAYS[6]
        source = (publication.ROOT / "essays" / f"{slug}.md").read_text(
            encoding="utf-8"
        )
        original, _ = publication.source_to_body(source, title, [])
        rendered = quantitative.render_quantitative_curry_howard(original)
        page = publication.render_essay(slug, title, category, description, 7, [])
        self.assertEqual(page.count('class="qc-sequence"'), 1)
        self.assertEqual(page.count('class="qc-math"'), 3)
        self.assertEqual(page.count('class="qc-layers"'), 1)
        self.assertEqual(page.count('class="qc-layer"'), 3)
        self.assertEqual(page.count('class="qc-tuple"'), 1)
        self.assertEqual(page.count('class="qc-pipeline"'), 1)
        self.assertEqual(page.count('class="qc-example"'), 5)
        self.assertEqual(page.count('class="qc-example-field"'), 16)
        self.assertEqual(page.count('class="qc-schema"'), 2)
        self.assertEqual(page.count('class="qc-schema-line"'), 31)
        self.assertEqual(page.count('data-qc-alternative="mobile"'), 10)
        self.assertEqual(page.count('class="qc-card"'), 64)
        self.assertEqual(page.count('class="qc-field"'), 179)
        self.assertIn(
            '<a href="#quantitative-search-over-formal-objects">5.1</a>',
            rendered
        )
        self.assertIn(
            '<a href="#probabilistic-scientific-claim">8.3</a>',
            rendered
        )

        original_blocks = list(quantitative.BLOCK.finditer(original))
        self.assertEqual(len(original_blocks), 14)
        for i, block in enumerate(original_blocks):
            lines = quantitative._blocks(block.group("lines"))
            with self.subTest(source_block=i + 1):
                if i == 0:
                    self.assertEqual(tuple(lines[0].split(" -> ")), quantitative.SEQ)
                    for stage in quantitative.SEQ:
                        self.assertIn("<li>" + stage + "</li>", rendered)
                elif i == 1 or i == 3 or i == 6:
                    self.assertEqual(len(lines), 1)
                    self.assertIn(
                        'alttext="' + lines[0].replace(">", "&gt;") + '"',
                        rendered
                    )
                elif i == 2:
                    layer = re.findall(
                        r'<div class="qc-layer"><dt>([^<]*)</dt>'
                        r'<dd>([\s\S]*?)</dd></div>', rendered
                    )
                    self.assertEqual(len(layer), 3)
                    self.assertEqual(
                        [label + ": " + unescape(re.search(
                            r'alttext="([^"]+)"', value
                        ).group(1)) for label, value in layer],
                        lines
                    )
                elif i == 4:
                    record = re.search(
                        r'<div class="qc-tuple"[^>]*>'
                        r'<div class="qc-tuple-start">(.*?)</div>'
                        r'<div class="qc-tuple-members">([\s\S]*?)</div>'
                        r'<div class="qc-tuple-end">(.*?)</div>'
                        r'</div>',
                        rendered
                    )
                    self.assertIsNotNone(record)
                    self.assertEqual(record.group(1), "Q = (")
                    self.assertEqual(record.group(3), ")")
                    fields = [
                        unescape(re.sub(r"<[^>]+>", "", value))
                        for value in re.findall(
                            r'<span class="qc-tuple-member"><code>'
                            r'([\s\S]*?)</code></span>',record.group(2)
                        )
                    ]
                    self.assertEqual(len(fields), 11)
                    self.assertEqual(
                        ", ".join(field.removesuffix(",") for field in fields),
                        lines[0].removeprefix("Q = (") + " " +
                        lines[1].removesuffix(")")
                    )
                    self.assertTrue(all(field.endswith(",") for field in fields[:-1]))
                    self.assertFalse(fields[-1].endswith(","))
                elif i == 5:
                    self.assertEqual(tuple(lines), quantitative.PIPELINE)
                    pipe = re.search(
                        r'<div class="qc-pipeline"[^>]*><ol>([\s\S]*?)'
                        r'</ol></div>', rendered
                    )
                    self.assertIsNotNone(pipe)
                    self.assertEqual(
                        re.findall(r"<li>([^<]+)</li>", pipe.group(1)),
                        lines
                    )
                elif i <= 11:
                    anchor = quantitative.EXAMPLES[i - 7]
                    example = re.search(
                        r'<dl class="qc-example" aria-label="Authored example ' +
                        re.escape(anchor) + r'">([\s\S]*?)</dl>', rendered
                    )
                    self.assertIsNotNone(example)
                    entries = re.findall(
                        r'<div class="qc-example-field"><dt>([^<]+)</dt>'
                        r'<dd>([^<]+)</dd></div>', example.group(1)
                    )
                    self.assertEqual(
                        [key + " = " + unescape(value) for key, value in entries],
                        lines
                    )
                else:
                    anchor, heading, length = quantitative.RECORDS[i - 12]
                    self.assertEqual(len(lines), length)
                    schema = re.search(
                        r'<div class="qc-schema" role="group" '
                        r'aria-label="Source record ' +
                        re.escape(heading[:-1]) +
                        r'">([\s\S]*?)</ol></div>', rendered
                    )
                    self.assertIsNotNone(schema)
                    first = re.search(
                        r'<p class="qc-schema-heading">([\s\S]*?)</p>',
                        schema.group(1)
                    )
                    self.assertIsNotNone(first)
                    clean = lambda value: unescape(
                        re.sub(r"<[^>]+>", "", value)
                    )
                    recovered = [clean(first.group(1))]
                    recovered += [
                        clean(value) for value in re.findall(
                            r'<li class="qc-schema-line">([\s\S]*?)</li>',
                            schema.group(1)
                        )
                    ]
                    self.assertEqual(recovered, lines)

        cell_count = 0
        for n in range(1, 11):
            with self.subTest(source_table=n):
                pattern = (
                    rf'<table data-source-table="{n}" id="table-{n}">'
                    r'[\s\S]*?</table>'
                )
                original_table = re.search(pattern, original)
                rendered_table = re.search(pattern, rendered)
                self.assertIsNotNone(original_table)
                self.assertIsNotNone(rendered_table)

                def neutralize(markup: str) -> str:
                    markup = re.sub(
                        r'<caption class="visually-hidden">[^<]*</caption>',
                        '<caption></caption>', markup
                    )
                    return re.sub(
                        r'<a href="[^"]+">([^<]+)</a>', r'\1', markup
                    )

                self.assertEqual(
                    neutralize(original_table.group()),
                    neutralize(rendered_table.group()),
                )
                tbody = re.search(
                    r'<tbody>([\s\S]*?)</tbody>',original_table.group()
                )
                self.assertIsNotNone(tbody)
                source_rows = re.findall(
                    r'<tr\b[^>]*>([\s\S]*?)</tr>',tbody.group(1)
                )
                self.assertEqual(len(source_rows),quantitative.ROWS[n - 1])
                source_values = [
                    re.findall(r'<td(?:\s[^>]*)?>([\s\S]*?)</td>',row)
                    for row in source_rows
                ]
                alt = re.search(
                    rf'<section class="qc-mobile qc-mobile-{n}" '
                    rf'aria-labelledby="table-{n}-caption">'
                    r'([\s\S]*?)</section>',rendered
                )
                self.assertIsNotNone(alt)
                cards = re.findall(
                    r'<dl class="qc-card">([\s\S]*?)</dl>',alt.group(1)
                )
                self.assertEqual(len(cards),len(source_rows))
                for original_row,card in zip(source_values,cards,strict=True):
                    copied = re.findall(r'<dd>([\s\S]*?)</dd>',card)
                    self.assertEqual(
                        original_row,
                        [re.sub(r'<a href="[^"]+">([^<]+)</a>',r'\1',value)
                         for value in copied],
                    )
                    cell_count += len(copied)
                self.assertIn(
                    f'id="table-{n}-caption">' + quantitative.CAPTIONS[n],
                    rendered,
                )
        self.assertEqual(cell_count,179)
        with self.assertRaises(ValueError):
            quantitative.render_quantitative_curry_howard(rendered)
        # The publication renderer must refuse any source-field drift.
        corrupted_tuple = original.replace(
            "Q = (score, probability, uncertainty, margin, loss, calibration, "
            "validation_status,",
            "Q = (score, probability, uncertainty, margin, loss, calibration, "
            "unrecognized_status,",
            1
        )
        self.assertNotEqual(original, corrupted_tuple)
        with self.assertRaises(ValueError):
            quantitative.render_quantitative_curry_howard(corrupted_tuple)
        corrupted_record = original.replace(
            "<p>calibration_status: string</p>",
            "<p>calibration_status: number</p>",
            1
        )
        self.assertNotEqual(original, corrupted_record)
        with self.assertRaises(ValueError):
            quantitative.render_quantitative_curry_howard(corrupted_record)




    def test_effectful_source_bound_presentation(self) -> None:
        """Every formal record and scientific table matches the committed V3 source."""
        import render_effectful as effectful

        slug, title, category, description = publication.ESSAYS[7]
        source = (publication.ROOT / "essays" / f"{slug}.md").read_text(
            encoding="utf-8"
        )
        original, _ = publication.source_to_body(source, title, [])
        rendered = effectful.render_effectful_and_conceptual_intelligence(original)
        page = publication.render_essay(slug, title, category, description, 8, [])
        self.assertEqual(page.count('class="ef-sequence"'), 1)
        self.assertEqual(page.count('class="ef-math ef-math-'), 7)
        self.assertEqual(page.count('class="table-display-caption ef-caption"'), 19)
        self.assertEqual(page.count('data-ef-alternative="mobile"'), 19)
        self.assertEqual(page.count('class="ef-card"'), 154)
        self.assertEqual(page.count('class="ef-field"'), 342)
        self.assertEqual(page.count('class="ef-source-notes"'), 1)

        with self.subTest("series sequence"):
            chain = re.search(
                r'<div class="ef-sequence"[^>]*><ol>'
                r'([\s\S]*?)</ol></div>', rendered
            )
            self.assertIsNotNone(chain)
            self.assertEqual(
                re.findall(r"<li>([^<]*)</li>", chain.group(1)),
                list(effectful.STAGES)
            )

        with self.subTest("MathML source equivalence"):
            formulas = re.findall(
                r'<div class="ef-math ef-math-\d+"[^>]*>'
                r'([\s\S]*?)</div>', rendered
            )
            self.assertEqual(len(formulas), 7)
            for i, (source_expression, formula) in enumerate(
                    zip(effectful.EXPRESSION_TEX, formulas, strict=True), 1):
                self.assertEqual(
                    re.findall(r'<math\b[^>]*alttext="([^"]+)"', formula),
                    [escape(source_expression, quote=True).replace(
                        "&#x27;", "&#x27;"
                    )]
                )
                self.assertIn(
                    'encoding="application/x-tex"', formula,
                    f"MathML missing semantic annotation at {i}"
                )
            # A semantic regression in the earlier version dropped one "|"
            # across the explicit line breaks in each alternative list.
            for index, count in ((1, 4), (2, 3)):
                formula = formulas[index]
                annotation = re.search(
                    r'<annotation encoding="application/x-tex">'
                    r'([\s\S]*?)</annotation>', formula
                )
                self.assertIsNotNone(annotation)
                self.assertEqual(
                    unescape(annotation.group(1)).count(r"\mid"),
                    count,
                    f"Lost an original alternative separator at MathML {index + 1}"
                )
                visible_alternatives = re.findall(
                    r'<(?:mi|mo)>∣</(?:mi|mo)>', formula
                )
                self.assertEqual(
                    len(visible_alternatives), count,
                    f"MathML rendering lost a source alternative at {index + 1}"
                )

        with self.subTest("source-use notes"):
            original_notes = re.search(
                r'<blockquote>([\s\S]*?)</blockquote>', original
            )
            self.assertIsNotNone(original_notes)
            notes = re.findall(
                r"<p>([^<]*)</p>", original_notes.group(1)
            )
            self.assertEqual(
                tuple(unescape(text) for text in notes),
                effectful.SOURCE_NOTES
            )
            styled = re.search(
                r'<ul class="ef-source-notes">([\s\S]*?)</ul>',
                rendered
            )
            self.assertIsNotNone(styled)
            self.assertEqual(
                re.findall(r"<li>([^<]*)</li>",styled.group(1)),
                [line[2:] for line in effectful.SOURCE_NOTES]
            )

        self.assertIn(
            '<a href="#effectful-agent-benchmark-v0.2">11</a>',
            rendered
        )
        self.assertIn(
            '<a href="#appendix-a.-typed-action-ledger-schema">A</a>',
            rendered
        )
        self.assertIn(
            '<a href="quantitative-curry-howard.html">Essay 6</a>',
            rendered
        )
        total_rows, total_cells = 0, 0
        for n in range(1, 20):
            with self.subTest(table=n):
                source_table = re.search(
                    rf'<table data-source-table="{n}" id="table-{n}">'
                    r'[\s\S]*?</table>', original
                )
                html_table = re.search(
                    rf'<table data-source-table="{n}" id="table-{n}">'
                    r'[\s\S]*?</table>', rendered
                )
                self.assertIsNotNone(source_table)
                self.assertIsNotNone(html_table)

                def normalize(value: str) -> str:
                    value = re.sub(
                        r'<caption class="visually-hidden">[^<]*</caption>',
                        '<caption></caption>', value
                    )
                    return re.sub(
                        r'<a href="[^"]+">([^<]+)</a>', r'\1', value
                    )

                self.assertEqual(
                    normalize(source_table.group()),
                    normalize(html_table.group())
                )
                tbody = re.search(
                    r'<tbody>([\s\S]*?)</tbody>', source_table.group()
                )
                self.assertIsNotNone(tbody)
                rows = re.findall(
                    r'<tr\b[^>]*>([\s\S]*?)</tr>',tbody.group(1)
                )
                self.assertEqual(len(rows),effectful.ROWS[n - 1])
                source_values = [
                    re.findall(
                        r'<td(?:\s[^>]*)?>([\s\S]*?)</td>',row
                    ) for row in rows
                ]
                alt = re.search(
                    rf'<section class="ef-mobile ef-mobile-{n}" '
                    rf'aria-labelledby="table-{n}-caption">'
                    r'([\s\S]*?)</section>', rendered
                )
                self.assertIsNotNone(alt)
                cards = re.findall(
                    r'<dl class="ef-card">([\s\S]*?)</dl>',
                    alt.group(1)
                )
                self.assertEqual(len(cards), len(rows))
                for values, card in zip(source_values,cards,strict=True):
                    derived = re.findall(
                        r'<dd>([\s\S]*?)</dd>', card
                    )
                    self.assertEqual(
                        values,
                        [
                            re.sub(
                                r'<a href="[^"]+">([^<]+)</a>',r'\1',v
                            ) for v in derived
                        ],
                    )
                    total_cells += len(derived)
                total_rows += len(cards)
                self.assertIn(
                    f'id="table-{n}-caption">' + effectful.CAPTIONS[n],
                    rendered,
                )
        self.assertEqual((total_rows,total_cells), (154,342))
        for n in (2,11,13):
            self.assertNotIn(
                f'<p class="table-display-caption" id="table-{n}-caption">',
                rendered
            )
        with self.assertRaises(ValueError):
            effectful.render_effectful_and_conceptual_intelligence(rendered)

        with self.subTest("source drift detection"):
            damaged = original.replace(
                "<p>concept_transfer : SourceDomain -&gt; TargetDomain</p>",
                "<p>concept_transfer : SourceDomain -&gt; OtherDomain</p>",
                1
            )
            self.assertNotEqual(damaged, original)
            with self.assertRaises(ValueError):
                effectful.render_effectful_and_conceptual_intelligence(damaged)


if __name__ == "__main__":
    unittest.main()
