"""Local regression tests for the public-repository Git tree preflight."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from check_public_tree import (  # noqa: E402
    PUBLIC_SAFE_FILES,
    parse_index,
    parse_tree,
    unsafe_paths,
    validate_content,
    validate_repository,
)


def run_git(root: Path, *args: str) -> None:
    """Run a Git command inside an isolated test repository."""
    subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True)


class PublicTreeUnitTests(unittest.TestCase):
    def test_reviewed_files_allowed(self) -> None:
        self.assertEqual(unsafe_paths(list(PUBLIC_SAFE_FILES)), [])

    def test_unpublished_files_rejected(self) -> None:
        unpublished = ["sources/Essay1.docx", "site/index.html", "site/essays/a.html", "qa/audit.json"]
        self.assertEqual(unsafe_paths(unpublished), sorted(unpublished))

    def test_traversal_and_lookalike_paths_rejected(self) -> None:
        for suspicious in ("./README.md", "site\\style.css", "SITE/style.css", "../README.md"):
            with self.subTest(path=suspicious):
                self.assertEqual(unsafe_paths([suspicious]), [suspicious])

    def test_index_and_tree_parser_handle_tabs_in_names(self) -> None:
        name = "README\tpreview.md"
        self.assertEqual(parse_index(f"100644 {'0'*40} 0\t{name}\0".encode())[0].path, name)
        self.assertEqual(parse_tree(f"100644 blob {'0'*40}\t{name}\0".encode())[0].path, name)

    def test_reject_disguised_payloads(self) -> None:
        examples = [
            ("README.md", b"PK\x03\x04fake"),
            ("README.md", b"\x00binary"),
            ("README.md", b"\xffbinary"),
            ("README.md", b"version https://git-lfs.github.com/spec/v1\n"),
            ("site/style.css", b"@import 'https://remote.test/font.css';"),
            ("site/style.css", b"body{background:url(https://remote.test/bg.png)}"),
            ("site/favicon.svg", b'<svg xmlns="http://www.w3.org/2000/svg"><script/></svg>'),
            ("site/favicon.svg", b'<svg xmlns="http://www.w3.org/2000/svg" onload="alert(1)"/>'),
            ("site/favicon.svg", b"<svg>"),
        ]
        for path, content in examples:
            with self.subTest(path=path, content=content[:30]):
                self.assertTrue(validate_content(path, content))

    def test_benign_content(self) -> None:
        self.assertFalse(validate_content("site/style.css", b"body{color:#111}"))
        self.assertFalse(validate_content("README.md", b"# Compositional Intelligence\n"))
        self.assertFalse(validate_content("site/favicon.svg", b'<svg xmlns="http://www.w3.org/2000/svg"/>'))


class PublicTreeIntegrationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        run_git(self.root, "init", "-q")
        run_git(self.root, "config", "user.name", "Public tree test")
        run_git(self.root, "config", "user.email", "test@example.invalid")
        (self.root / "README.md").write_text("# Safe publication foundation\n", encoding="utf-8")
        run_git(self.root, "add", "README.md")
        run_git(self.root, "commit", "-qm", "initial")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_valid_committed_and_index_entries_pass(self) -> None:
        checked, issues = validate_repository(self.root)
        self.assertEqual(checked, 2)
        self.assertEqual(issues, [])

    def test_staged_unpublished_html_is_rejected(self) -> None:
        (self.root / "site").mkdir()
        (self.root / "site/index.html").write_text("<h1>unpublished</h1>", encoding="utf-8")
        run_git(self.root, "add", "site/index.html")
        _, issues = validate_repository(self.root)
        self.assertTrue(any("site/index.html" in issue for issue in issues))

    def test_staged_disguised_binary_is_rejected(self) -> None:
        (self.root / "README.md").write_bytes(b"%PDF-1.7\nfake")
        run_git(self.root, "add", "README.md")
        _, issues = validate_repository(self.root)
        self.assertTrue(any("binary or archive-like" in issue for issue in issues))

    def test_committed_unsafe_page_cannot_be_hidden_by_deleting_from_index(self) -> None:
        (self.root / "site").mkdir()
        (self.root / "site/index.html").write_text("Secret manuscript", encoding="utf-8")
        run_git(self.root, "add", "site/index.html")
        run_git(self.root, "commit", "-qm", "bad commit")
        run_git(self.root, "rm", "site/index.html")
        _, issues = validate_repository(self.root)
        self.assertTrue(any("HEAD:site/index.html" in issue for issue in issues))

    def test_staged_symlink_at_allowed_path_is_rejected(self) -> None:
        (self.root / "docs").mkdir()
        (self.root / "docs/RELEASE.md").symlink_to("../README.md")
        run_git(self.root, "add", "docs/RELEASE.md")
        _, issues = validate_repository(self.root)
        self.assertTrue(any("prohibited Git mode 120000" in issue for issue in issues))


if __name__ == "__main__":
    unittest.main()
