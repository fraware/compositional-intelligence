#!/usr/bin/env python3
"""Regression checks for the author-supplied V3 manuscript source.

The original DOCX identifiers and hashes are recorded in sources/originals.json.
Tests bind the committed publication sources to their recorded hashes and
validate deterministic presentation. They do not independently read DOCX bytes.
"""
from __future__ import annotations

import hashlib
import json
import re
import unittest

import build_site as publication
from render_science import FORMULAE, enhance_scientific_presentation, render_source_math
from check_originals import Paragraphs, overlap, phrases, tokens
from render_synthesis import render_synthesis_figures
from render_preface import render_preface


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
            "series-preface": "1. Purpose of the Series",
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

    def test_flagship_rendering_is_scoped_and_accessible(self) -> None:
        """The flagship typesetting does not alter another essay's diagrams."""
        page = publication.render_essay(*publication.ESSAYS[0], position=0, table_captions=[])
        self.assertIn('class="ci-source-figure ci-lifecycle"', page)
        self.assertIn('class="ci-source-figure ci-commuting"', page)
        self.assertEqual(page.count("<figcaption"), 2)
        self.assertIn('alttext="S = (E_s, E_t, x, f, T, g, epsilon)"', page)
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

    def test_flagship_browser_title_is_not_repeated(self) -> None:
        """The flagship page's browser tab shows the essay title once."""
        page = publication.render_essay(
            *publication.ESSAYS[0], position=0, table_captions=[]
        )
        self.assertIn("<title>Compositional Intelligence</title>", page)
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


    def test_preface_original_lifecycle_and_order_are_readable(self) -> None:
        """The V3 preface lifecycle and the nine existing essays are navigable."""
        slug, title, category, description = publication.ESSAYS[1]
        original = (publication.ROOT / "essays" / f"{slug}.md").read_text(
            encoding="utf-8"
        )
        body, _ = publication.source_to_body(original, title, [])
        enhanced = enhance_scientific_presentation(body)
        rendered = render_preface(enhanced)

        self.assertEqual(rendered.count('class="ci-lifecycle preface-lifecycle"'), 1)
        self.assertEqual(rendered.count('<dl class="preface-mobile-record'), 23)
        self.assertEqual(rendered.count('<table data-source-table='), 7)
        self.assertIn("The sequence exposes the status transitions", rendered)
        self.assertEqual(rendered.count('class="table-scroll-hint preface-scroll-hint"'), 7)
        for target_slug, _, _, _ in publication.ESSAYS:
            with self.subTest(target=target_slug):
                self.assertIn(f'href="{target_slug}.html"', rendered)
        with self.assertRaises(ValueError):
            render_preface(rendered)

    def test_preface_math_tables_have_original_cells_and_mobile_readings(self) -> None:
        """The phone view retains every notation row and its scientific meaning."""
        slug, title, _, _ = publication.ESSAYS[1]
        original = (publication.ROOT / "essays" / f"{slug}.md").read_text(
            encoding="utf-8"
        )
        body, _ = publication.source_to_body(original, title, [])
        rendered = render_preface(enhance_scientific_presentation(body))
        self.assertEqual(rendered.count('data-preface-alternative="mobile"'), 3)
        self.assertEqual(rendered.count('<dl class="preface-mobile-record'), 23)
        self.assertEqual(rendered.count('class="preface-record-field"'), 63)
        self.assertIn('class="preface-architecture-source"', rendered)
        self.assertIn('class="preface-architecture-satisfaction"', rendered)
        self.assertIn("TaskSpec → ArchitectureType → ArchitectureInstance;", rendered)
        self.assertIn('id="table-5"', rendered)
        self.assertIn('id="table-7"', rendered)
        self.assertEqual(rendered.count('class="visually-hidden"'), 7)

    def test_preface_accessible_captions_and_unchanged_source(self) -> None:
        """Captions added by conversion remain metadata, not invented prose."""
        slug, title, category, description = publication.ESSAYS[1]
        source_file = publication.ROOT / "essays" / f"{slug}.md"
        digest = hashlib.sha256(source_file.read_bytes()).hexdigest()
        self.assertEqual(digest, self.documents[slug]["markdown_sha256"])
        page = publication.render_essay(
            slug, title, category, description, 1, []
        )
        self.assertEqual(page.count('<dl class="preface-mobile-record'), 23)
        self.assertIn("Table 5. Mathematical notation and its interpretation.", page)
        self.assertIn("Table 6. Publication steps, actions, and gates.", page)
        self.assertNotIn("Notation, Reading — Notation, Reading", page)
        self.assertIn('aria-label="Original eight-stage artifact lifecycle"', page)
        self.assertNotIn('<p class="byline">', page)



if __name__ == "__main__":
    unittest.main()
