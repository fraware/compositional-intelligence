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


if __name__ == "__main__":
    unittest.main()
