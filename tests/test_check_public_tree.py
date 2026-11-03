"""Unit tests for the public-repository content allowlist."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from check_public_tree import PUBLIC_SAFE_FILES, unsafe_paths  # noqa: E402


class PublicTreeTests(unittest.TestCase):
    def test_all_reviewed_paths_are_allowed(self) -> None:
        self.assertEqual(unsafe_paths(list(PUBLIC_SAFE_FILES)), [])

    def test_unpublished_material_is_rejected(self) -> None:
        unpublished = [
            "sources/Essay1.docx",
            "editorial/candidate/synthesis-review.html",
            "qa/audit.json",
            "site/index.html",
            "site/essays/semantic-participation.html",
            "site/content-manifest.json",
            "docs/private-notes.md",
        ]
        self.assertEqual(unsafe_paths(unpublished), sorted(unpublished))

    def test_path_tricks_are_rejected(self) -> None:
        for suspicious in ("./README.md", "site\\style.css", "SITE/style.css", "../README.md"):
            with self.subTest(path=suspicious):
                self.assertEqual(unsafe_paths([suspicious]), [suspicious])


if __name__ == "__main__":
    unittest.main()
