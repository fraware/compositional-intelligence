#!/usr/bin/env python3
"""Regression tests for source-bound scientific publication metadata.

These tests check provenance, failure behavior, and retained HTML semantics.
They do not assess the validity of the research hypotheses.
"""

from __future__ import annotations

import copy
import json
import unittest

import build_site as publication


class PublicationMetadataTests(unittest.TestCase):
    """Assert that manuscript provenance and interpretive limits fail closed."""

    @classmethod
    def setUpClass(cls) -> None:
        """Read checked-in metadata without network access."""
        cls.tables = json.loads((publication.ROOT / "tables" / "captions.json").read_text(encoding="utf-8"))
        cls.guide = json.loads((publication.ROOT / "reading" / "guide.json").read_text(encoding="utf-8"))


    def test_reader_guide_grounded_questions(self) -> None:
        """Every expert-reader interpretation is attached to a matching source paragraph."""
        publication.validate_reader_guide(self.guide)
        self.assertEqual(len(self.guide["entries"]), 7)
        self.assertEqual(sum(len(entry["checks"]) for entry in self.guide["entries"]), 14)

    def test_reader_guide_rejects_wrong_section(self) -> None:
        """A true passage cited to an unrelated section is invalid evidence."""
        changed = copy.deepcopy(self.guide)
        changed["entries"][0]["checks"][0]["evidence"]["section"] = (
            "semantic-participation#3-from-output-quality-to-semantic-membership"
        )
        with self.assertRaisesRegex(ValueError, "Unmatched reading-guide evidence"):
            publication.validate_reader_guide(changed)

    def test_reader_guide_rejects_unbalanced_question_inventory(self) -> None:
        """No series concept may silently lose its diagnostic question."""
        changed = copy.deepcopy(self.guide)
        changed["entries"][4]["checks"].pop()
        with self.assertRaisesRegex(ValueError, "Expected two independent reader questions"):
            publication.validate_reader_guide(changed)

    def test_reader_guide_renders_native_disclosures(self) -> None:
        """Questions, explanatory passages, and manuscript links are independently inspectable."""
        rendered = publication.render_reader_guide(self.guide)
        self.assertEqual(rendered.count('class="reader-check"'), 14)
        self.assertEqual(rendered.count('class="reader-source"'), 14)
        self.assertIn("<details><summary>", rendered)
        self.assertIn('href="../essays/semantic-participation.html#5-3-semantic-membership"', rendered)

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
        self.assertEqual(count, 106)

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
        self.assertIn('class="visually-hidden">One explicit scientific-table description.', rendered)


if __name__ == "__main__":
    unittest.main()
