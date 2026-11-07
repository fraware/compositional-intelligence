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
        cls.atlas = json.loads((publication.ROOT / "atlas" / "concepts.json").read_text(encoding="utf-8"))
        cls.tables = json.loads((publication.ROOT / "tables" / "captions.json").read_text(encoding="utf-8"))

    def test_atlas_excerpts_are_exact_and_section_local(self) -> None:
        """Every cited passage occurs inside the declared manuscript section."""
        publication.validate_concepts(self.atlas)
        self.assertEqual(len(self.atlas["concepts"]), 7)
        self.assertEqual(len(self.atlas["relations"]), 8)
        self.assertEqual(sum(len(r["evidence"]) for r in self.atlas["relations"]), 16)

    def test_invalid_atlas_passage_rejected(self) -> None:
        """A plausible-looking but unsupported passage must fail publication."""
        tampered = copy.deepcopy(self.atlas)
        tampered["relations"][0]["evidence"][0]["excerpt"] = "This statement is absent from the source section."
        with self.assertRaisesRegex(ValueError, "Unmatched manuscript evidence excerpt"):
            publication.validate_concepts(tampered)

    def test_unsupported_relation_type_rejected(self) -> None:
        """Conceptual relationships must use the defined, bounded categories."""
        tampered = copy.deepcopy(self.atlas)
        tampered["relations"][0]["kind"] = "mathematically-proven"
        with self.assertRaisesRegex(ValueError, "Unknown conceptual relationship type"):
            publication.validate_concepts(tampered)

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
