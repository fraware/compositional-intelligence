#!/usr/bin/env python3
"""Regression tests for source-bound scientific publication metadata.

These tests check provenance, failure behavior, and retained HTML semantics.
They do not assess the validity of the research hypotheses.
"""

from __future__ import annotations

import json
import unittest

import build_site as publication


class PublicationMetadataTests(unittest.TestCase):
    """Assert that manuscript provenance and interpretive limits fail closed."""

    @classmethod
    def setUpClass(cls) -> None:
        """Read checked-in metadata without network access."""
        cls.tables = json.loads((publication.ROOT / "tables" / "captions.json").read_text(encoding="utf-8"))


    def test_removed_editorial_page_excluded(self) -> None:
        """The removed guide is excluded from the public inventory."""
        page = publication.header(
            "Test", "Publication metadata", publication.BASE + "essays/series-preface.html")
        self.assertNotIn("reading/", page)
        self.assertNotIn("reading/", publication.render_sitemap())
        self.assertFalse((publication.ROOT / "reading" / "guide.json").exists())

    def test_original_preface_retained_and_added_study_removed(self) -> None:
        """Publish Essay 0 while excluding the later site-only demonstration."""
        self.assertIn("series-preface", [row[0] for row in publication.ESSAYS])
        self.assertTrue((publication.ROOT / "essays" / "series-preface.md").is_file())
        self.assertNotIn("commuting-square", publication.render_sitemap())
        self.assertNotIn("studies/", publication.render_sitemap())
        self.assertFalse((publication.ROOT / "docs" / "studies" / "commuting-square.html").exists())
        self.assertFalse((publication.ROOT / "docs" / "studies" / "commuting-square.mjs").exists())

    def test_appendix_schemas_are_preformatted_in_manuscripts(self) -> None:
        """Canonical manuscript schemas must retain readable line structure."""
        counts = {
            "compositional-intelligence": 7,
            "lambek-machines": 4,
            "typed-generativity": 4,
            "semantic-participation": 1,
            "quantitative-curry-howard": 1,
            "effectful-and-conceptual-intelligence": 2,
        }
        for slug, expected in counts.items():
            source = (publication.ROOT / "essays" / f"{slug}.md").read_text(encoding="utf-8")
            self.assertEqual(source.count("```text\n"), expected,
                             f"{slug}: missing preformatted schema")

    def test_mathml_display_is_keyboard_scrollable(self) -> None:
        """MathML is preserved in a named, focusable overflow container."""
        sample = (
            '<p><math display="block" xmlns="http://www.w3.org/1998/Math/MathML">'
            '<semantics><mi>x</mi><annotation encoding="application/x-tex">x'
            '</annotation></semantics></math></p>'
        )
        rendered = publication.render_math(sample)
        self.assertIn('class="math-scroll"', rendered)
        self.assertIn('role="group" tabindex="0"', rendered)
        self.assertIn('<math display="block"', rendered)
        self.assertIn('encoding="application/x-tex"', rendered)
        self.assertNotIn('<p><math', rendered)

    def test_inline_mathml_is_not_wrapped(self) -> None:
        """Display handling leaves text-flow equations intact."""
        raw = '<p>Term <math display="inline"><mi>x</mi></math>.</p>'
        self.assertEqual(publication.render_math(raw), raw)


    def test_original_synthesis_subtitle_is_retained(self) -> None:
        """The source subtitle is shown without adding a new editorial deck."""
        self.assertEqual(
            publication.ORIGINAL_ARTICLE_SUBTITLES["compositional-intelligence"],
            "Typed Artifacts, Structured Worlds, and Effectful AI",
        )

    def test_synthesis_math_cells_are_semantic_and_source_preserving(self) -> None:
        """Render exactly four synopsis judgments without altering Markdown."""
        source = (publication.ROOT / "essays" / "compositional-intelligence.md").read_text(
            encoding="utf-8"
        )
        raw_cells = (
            "w_i -&gt; tau_i -&gt; pi -&gt; pi",
            "A |= S",
            '<span class="inline-notation">Γ ⊢<sub>θ</sub> t : A ▷ Q</span>',
            "Γ; M; E; C ⊢_spec a : Pre → Post ! ε @ ρ",
        )
        for cell in raw_cells:
            self.assertEqual(source.count("<td>" + cell + "</td>"), 1)
        rendered = publication.render_synthesis_table_math(
            "".join("<td>" + cell + "</td>" for cell in raw_cells)
        )
        self.assertEqual(rendered.count('<math display="inline"'), 4)
        self.assertEqual(rendered.count('encoding="application/x-tex"'), 4)
        self.assertIn("<mo>⊨</mo>", rendered)
        self.assertIn("<msub><mo>⊢</mo><mtext>spec</mtext></msub>", rendered)
        for cell in raw_cells:
            self.assertNotIn("<td>" + cell + "</td>", rendered)
        with self.assertRaisesRegex(ValueError, "formula cell changed"):
            publication.render_synthesis_table_math("<table></table>")


    def test_figures_have_explicit_source_captions(self) -> None:
        """The conceptual diagrams are self-describing rather than plaintext pseudo-figures."""
        for slug, count in [("compositional-intelligence", 2), ("lambek-machines", 2)]:
            source = (publication.ROOT / "essays" / f"{slug}.md").read_text(encoding="utf-8")
            self.assertEqual(source.count("<figure "), count)
            self.assertEqual(source.count("<figcaption "), count)

    def test_all_table_captions_are_source_bound(self) -> None:
        """Every manuscript table must have a complete and matching description."""
        count = 0
        for slug, entries in self.tables["essays"].items():
            manuscript = (publication.ROOT / "essays" / f"{slug}.md").read_text(encoding="utf-8")
            publication.verify_table_catalog(manuscript, entries, slug)
            count += len(entries)
        self.assertEqual(count, 105)

    def test_table_change_requires_caption_review(self) -> None:
        """Even a minimally altered source table invalidates its prior fingerprint."""
        slug = "functorial-consistency"
        manuscript = (publication.ROOT / "essays" / f"{slug}.md").read_text(encoding="utf-8")
        self.assertIn("<table>", manuscript)
        changed = manuscript.replace("<table>", '<table data-edited="true">', 1)
        with self.assertRaisesRegex(ValueError, "changed; review"):
            publication.verify_table_catalog(changed, self.tables["essays"][slug], slug)

    def test_missing_table_caption_is_rejected(self) -> None:
        """The renderer cannot silently substitute generic table descriptions."""
        with self.assertRaisesRegex(ValueError, "caption catalogue"):
            publication.render_tables("<table><tr><th>Header</th></tr></table>", [])

    def test_authored_table_labels_become_accessible_captions(self) -> None:
        """Printed table labels are merged into a single nonduplicated caption."""
        content = (
            "<p>Table B2. Formal proof obligations.</p>\n"
            "<table><thead><tr><th>Condition</th><th>Test</th></tr></thead>"
            "<tbody><tr><td>Coverage</td><td>Pass</td></tr></tbody></table>"
        )
        output = publication.render_tables(
            content, [{"caption": "Formal assumptions and their acceptance checks"}],
        )
        self.assertNotIn("<p>Table B2", output)
        self.assertEqual(output.count('Table B2</span>'), 1)
        self.assertIn('data-columns="2"', output)
        self.assertIn('<thead>', output)
        self.assertIn('</thead>', output)
        self.assertIn('<p id="table-1-caption" class="table-display-caption">', output)
        self.assertIn('<caption class="visually-hidden">', output)
        self.assertIn('aria-labelledby="table-1-caption"', output)

    def test_synthesis_preserves_authored_table_titles(self) -> None:
        """Original table captions are presented verbatim without editorial substitutions."""
        source = (
            "<p>Table. Output failures and missing artifact conditions.</p>\n"
            "<table><thead><tr><th>Domain</th></tr></thead>"
            "<tbody><tr><td>Formalization</td></tr></tbody></table>"
        )
        rendered = publication.render_tables(
            source,
            [{"caption": "Examples of local success and missing artifact conditions"}],
            preserve_source_labels=True,
        )
        original = "Table. Output failures and missing artifact conditions."
        self.assertEqual(rendered.count(original), 2)  # visible and native caption
        self.assertNotIn("Examples of local success", rendered)
        self.assertIn('class="table-display-caption">' + original + '</p>', rendered)
        self.assertIn('<caption class="visually-hidden">' + original + '</caption>', rendered)
        self.assertIn('aria-labelledby="table-1-caption"', rendered)

    def test_synthesis_unlabelled_tables_retain_accessible_captions(self) -> None:
        """Original unlabeled appendix tables keep a useful accessible name."""
        source = (
            "<h3 id=\"claim-levels\">Claim levels</h3>"
            "<table><thead><tr><th>Level</th></tr></thead>"
            "<tbody><tr><td>L1</td></tr></tbody></table>"
        )
        rendered = publication.render_tables(
            source,
            [{"caption": "Claim levels and their publication treatment"}],
            preserve_source_labels=True,
        )
        self.assertIn("Table 1</span> Claim levels", rendered)
        self.assertIn('<caption class="visually-hidden">', rendered)


    def test_malformed_table_without_section_is_rejected(self) -> None:
        """The publication must reject missing thead instead of emitting malformed HTML."""
        with self.assertRaisesRegex(ValueError, "intact semantic header"):
            publication.render_tables(
                "<table><tr><th>Column</th></tr></table>",
                [{"caption": "Test heading and data with intact structure"}],
            )

    def test_record_schemas_preserve_lines_without_changing_quotes(self) -> None:
        """Structured notations gain line layout, while quoted prose stays prose."""
        source = (
            "<blockquote><p>Record = {<br /> id: string<br /> "
            "target: type<br /> status: reviewed<br />}</p></blockquote>"
        )
        output = publication.render_schema_blocks(source)
        self.assertIn('class="record-schema"', output)
        self.assertIn("id: string\n", output)
        self.assertIn("target: type\n", output)
        original = "<blockquote><p>A scientific claim with no typed fields.</p></blockquote>"
        self.assertEqual(publication.render_schema_blocks(original), original)

    def test_rendered_table_preserves_semantics(self) -> None:
        """An HTML table stays a table inside a named keyboard-scrollable group."""
        rendered = publication.render_tables(
            "<h2 id=\"t\">Test</h2><table><thead><tr><th>Column</th></tr></thead>"
            "<tbody><tr><td>Value</td></tr></tbody></table>",
            [{"caption": "One explicit scientific-table description."}],
        )
        self.assertIn('<table id="table-1">', rendered)
        self.assertIn('<th scope="col">', rendered)
        self.assertIn('role="group"', rendered)
        self.assertIn('tabindex="0"', rendered)
        self.assertIn('<thead>', rendered)
        self.assertIn('</thead>', rendered)
        self.assertNotIn('<th scope="col"ead', rendered)
        self.assertIn('class="table-display-caption"', rendered)
        self.assertIn('class="visually-hidden"', rendered)
        self.assertIn('data-columns="1"', rendered)
        self.assertIn('Table 1</span> One explicit scientific-table description.', rendered)
        self.assertIn('aria-labelledby="table-1-caption"', rendered)


    def test_notation_guard_excludes_mathml_and_preformatted_records(self) -> None:
        """MathML annotations and code records are not misread as broken prose."""
        from verify_notation import BROKEN, VisibleNotation

        parser = VisibleNotation()
        parser.feed(
            '<p>Readable expression <math><semantics>'
            '<mi>x</mi><annotation encoding="application/x-tex">P_theta'
            '</annotation></semantics></math>.</p>'
            '<pre><code>P_theta(A,t | c)</code></pre>'
        )
        parser.close()
        self.assertFalse(any(
            expression.search(fragment)
            for fragment in parser.visible
            for expression in BROKEN.values()
        ))
        self.assertEqual(len(parser.records), 1)

    def test_notation_guard_catches_raw_mathematical_transcriptions(self) -> None:
        """An escaped or ASCII-only formula in displayed prose must fail."""
        from verify_notation import BROKEN, VisibleNotation

        parser = VisibleNotation()
        parser.feed("<p>P_theta(A,t | c) is the joint probability.</p>")
        parser.close()
        self.assertTrue(any(
            expression.search(fragment)
            for fragment in parser.visible
            for expression in BROKEN.values()
        ))


if __name__ == "__main__":
    unittest.main()
