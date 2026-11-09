#!/usr/bin/env python3
"""Regression checks for the author-supplied V3 manuscript source.

The original DOCX identifiers and hashes are recorded in sources/originals.json.
Tests bind the committed publication sources to their recorded hashes and
validate deterministic presentation. They do not independently read DOCX bytes.
"""
from __future__ import annotations

import hashlib
from html import unescape
from html.parser import HTMLParser
import json
import re
import unittest

import build_site as publication
from render_science import FORMULAE, enhance_scientific_presentation, render_source_math
from check_originals import Paragraphs, overlap, phrases, tokens
from render_synthesis import render_synthesis_figures
from render_preface import render_preface
from render_semantic import render_semantic_participation, _HEADERS, _ROW_COUNTS



class _PrefaceCellText(HTMLParser):
    """Extract authored table cells and mobile alternatives, retaining TeX sources."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tables: dict[int, list[list[str]]] = {}
        self.mobile: dict[str, list[list[str]]] = {}
        self.table_id: int | None = None
        self.table_rows: list[list[str]] = []
        self.table_row: list[str] | None = None
        self.table_cell: list[str] | None = None
        self.section: str | None = None
        self.section_rows: list[list[str]] = []
        self.record: list[str] | None = None
        self.field: list[str] | None = None
        self.in_math = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        if tag == "table" and data.get("data-source-table"):
            self.table_id = int(data["data-source-table"])
            self.table_rows = []
        if tag == "tr" and self.table_id is not None:
            self.table_row = []
        if tag in {"th", "td"} and self.table_row is not None:
            self.table_cell = []
        if tag == "section" and "preface-mobile-records" in (
            data.get("class") or ""
        ).split():
            self.section = data.get("aria-label")
            self.section_rows = []
        if tag == "dl" and self.section is not None and "preface-mobile-record" in (
            data.get("class") or ""
        ).split():
            self.record = []
        if tag == "dd" and self.record is not None:
            self.field = []
        if tag == "math":
            self.in_math = True
            original = data.get("alttext")
            if original is not None:
                if self.table_cell is not None:
                    self.table_cell.append(original)
                if self.field is not None:
                    self.field.append(original)

    def handle_data(self, data: str) -> None:
        if not self.in_math:
            if self.table_cell is not None:
                self.table_cell.append(data)
            if self.field is not None:
                self.field.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "math":
            self.in_math = False
        if tag in {"th", "td"} and self.table_cell is not None:
            self.table_row.append("".join(self.table_cell))
            self.table_cell = None
        if tag == "tr" and self.table_id is not None and self.table_row is not None:
            self.table_rows.append(self.table_row)
            self.table_row = None
        if tag == "table" and self.table_id is not None:
            self.tables[self.table_id] = self.table_rows
            self.table_id = None
        if tag == "dd" and self.field is not None:
            self.record.append("".join(self.field))
            self.field = None
        if tag == "dl" and self.record is not None:
            self.section_rows.append(self.record)
            self.record = None
        if tag == "section" and self.section is not None:
            self.mobile[self.section] = self.section_rows
            self.section = None


def _preface_cell(value: str, *, mobile: bool = False) -> str:
    """Normalize rendered whitespace; the mobile arrow is the source's ->."""
    if mobile:
        value = value.replace("→", "->")
        value = re.sub(r";\s*", "; ", value)
    return re.sub(r"\s+", " ", unescape(value)).strip()


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
        self.assertEqual(rendered.count('<dl class="preface-mobile-record'), 44)
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
        self.assertEqual(rendered.count('data-preface-alternative="mobile"'), 7)
        self.assertEqual(rendered.count('<dl class="preface-mobile-record'), 44)
        self.assertEqual(rendered.count('class="preface-record-field"'), 118)
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
        self.assertEqual(page.count('<dl class="preface-mobile-record'), 44)
        self.assertIn("Table 5. Mathematical notation and its interpretation.", page)
        self.assertIn("Table 6. Publication steps, actions, and gates.", page)
        self.assertNotIn("Notation, Reading — Notation, Reading", page)
        self.assertIn('aria-label="Original eight-stage artifact lifecycle"', page)
        self.assertNotIn('<p class="byline">', page)


    def test_preface_all_table_cells_match_source_and_mobile_copies(self) -> None:
        """Check every table cell, not merely table or MathML element counts."""
        slug, title, category, description = publication.ESSAYS[1]
        source = (publication.ROOT / "essays" / f"{slug}.md").read_text(
            encoding="utf-8"
        )
        original, _ = publication.source_to_body(source, title, [])
        published = publication.render_essay(
            slug, title, category, description, 1, []
        )
        before = _PrefaceCellText()
        before.feed(original)
        after = _PrefaceCellText()
        after.feed(published)
        self.assertEqual(set(before.tables), set(range(1, 8)))
        self.assertEqual(set(after.tables), set(range(1, 8)))
        total = 0
        for number in range(1, 8):
            with self.subTest(table=number):
                source_rows = before.tables[number]
                published_rows = after.tables[number]
                normalized = lambda rows: [
                    [_preface_cell(cell) for cell in row] for row in rows
                ]
                self.assertEqual(normalized(source_rows), normalized(published_rows))
                total += sum(len(row) for row in source_rows)
        self.assertEqual(total, 137)

        names = {
            1: "Publication order and reading links",
            2: "Foundational layers and questions",
            3: "Core terms and definitions",
            4: "Claim protocol levels and treatment",
            5: "Mathematical notation and reading",
            6: "Publication steps and gates",
            7: "Canonical schemas and artifacts",
        }
        self.assertEqual(set(after.mobile), set(names.values()))
        total_fields = 0
        for number, label in names.items():
            with self.subTest(mobile_table=number):
                original_rows = before.tables[number][1:]
                mobile_rows = after.mobile[label]
                normalized_source = [
                    [_preface_cell(cell, mobile=True) for cell in row]
                    for row in original_rows
                ]
                normalized_mobile = [
                    [_preface_cell(cell, mobile=True) for cell in row]
                    for row in mobile_rows
                ]
                self.assertEqual(normalized_source, normalized_mobile)
                total_fields += sum(len(row) for row in mobile_rows)
        self.assertEqual(total_fields, 118)


    def test_semantic_participation_mobile_tables_are_source_equivalent(self) -> None:
        """All original cells survive, and every mobile cell is copied verbatim."""
        slug, title, _, _ = publication.ESSAYS[2]
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
                self.assertEqual(source_table.group(), published_table)
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
                for original_row, record in zip(rows_to_copy, records, strict=True):
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
        slug, title, category, description = publication.ESSAYS[2]
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
        self.assertEqual(output.count('class="sp-source-schema"'), 4)
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
        slug, title, category, description = publication.ESSAYS[2]
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



if __name__ == "__main__":
    unittest.main()
