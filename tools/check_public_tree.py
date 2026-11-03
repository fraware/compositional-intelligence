#!/usr/bin/env python3
"""Validate committed and staged content against a strict public-file allowlist.

This is a local publication preflight, not an access-control mechanism. In a
public repository every pushed commit is already readable before this check
runs. Review staged diffs and commit history independently before pushing.
"""

from __future__ import annotations

import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path

PUBLIC_SAFE_FILES = frozenset(
    {
        ".gitignore",
        "README.md",
        "docs/RELEASE.md",
        "site/favicon.svg",
        "site/style.css",
        "tools/check_public_tree.py",
        "tests/test_check_public_tree.py",
    }
)
MAX_FILE_BYTES = 50_000
ALLOWED_MODE = "100644"  # Refuse symlinks, submodules and executable Git objects.
BLOCKED_MAGIC = (b"PK\x03\x04", b"%PDF-", b"\x89PNG", b"GIF8", b"\x7fELF", b"MZ")
BLOCKED_TOKENS = (
    re.compile(r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----"),
    re.compile(r"github_pat_[A-Za-z0-9_]{30,}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9]{30,}"),
    re.compile(r"sk-[A-Za-z0-9_-]{30,}"),
)


@dataclass(frozen=True)
class GitEntry:
    """A file entry in Git's index or a committed tree."""

    path: str
    mode: str
    sha: str
    stage: int = 0


def unsafe_paths(paths: list[str]) -> list[str]:
    """Return file paths not explicitly allowed for public publication."""
    return sorted({path for path in paths if path not in PUBLIC_SAFE_FILES})


def git(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[bytes]:
    """Run Git with byte-preserving output and without shell interpolation."""
    return subprocess.run(
        ["git", "-C", str(root), *args],
        check=check,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def parse_index(raw: bytes) -> list[GitEntry]:
    """Parse NUL-delimited Git index records."""
    entries: list[GitEntry] = []
    for record in filter(None, raw.split(b"\0")):
        metadata, path = record.split(b"\t", 1)
        mode, sha, stage = metadata.decode("ascii").split(" ")
        entries.append(GitEntry(path.decode("utf-8", "surrogateescape"), mode, sha, int(stage)))
    return entries


def parse_tree(raw: bytes) -> list[GitEntry]:
    """Parse NUL-delimited committed-tree records."""
    entries: list[GitEntry] = []
    for record in filter(None, raw.split(b"\0")):
        metadata, path = record.split(b"\t", 1)
        mode, _kind, sha = metadata.decode("ascii").split(" ")
        # Non-blob Git objects (e.g. submodules) are rejected by the mode check.
        entries.append(GitEntry(path.decode("utf-8", "surrogateescape"), mode, sha))
    return entries


def validate_content(path: str, data: bytes) -> list[str]:
    """Perform bounded content checks on an allowlisted Git blob.

    These checks catch obvious binary payloads, credential formats, and remote
    resource references. They cannot establish that arbitrary prose is safe to
    publish; manuscript disclosure review is a separate human obligation.
    """
    issues: list[str] = []
    if len(data) > MAX_FILE_BYTES:
        return [f"exceeds {MAX_FILE_BYTES} byte limit"]
    if b"\x00" in data or data.startswith(BLOCKED_MAGIC):
        return ["binary or archive-like payload in text-only location"]
    try:
        content = data.decode("utf-8", "strict")
    except UnicodeDecodeError:
        return ["content is not valid UTF-8"]
    if content.startswith("version https://git-lfs.github.com/spec/v1"):
        issues.append("Git LFS pointer prohibited")
    for token in BLOCKED_TOKENS:
        if token.search(content):
            issues.append("possible private key or access credential")
            break
    if path.endswith(".css") and re.search(r"@import\b|url\s*\(", content, re.I):
        issues.append("external or inlined CSS resources are not reviewed")
    if path.endswith(".svg"):
        try:
            svg = ET.fromstring(content)
            for element in svg.iter():
                tag = element.tag.split("}")[-1].lower()
                if tag in {"script", "foreignobject", "image", "use", "animate", "set"}:
                    issues.append("unreviewed SVG element")
                    break
                if any(key.split("}")[-1].lower() in {"href", "src"} or key.lower().startswith("on")
                       for key in element.attrib):
                    issues.append("unreviewed SVG external reference or event handler")
                    break
        except ET.ParseError:
            issues.append("invalid SVG XML")
    return issues


def validate_repository(root: Path) -> tuple[int, list[str]]:
    """Check every committed HEAD blob and staged index blob, failing closed."""
    issues: list[str] = []
    if git(root, "rev-parse", "--is-inside-work-tree").stdout.strip() != b"true":
        raise ValueError("path is not a Git worktree")
    index = parse_index(git(root, "ls-files", "--stage", "-z").stdout)
    head_exists = git(root, "rev-parse", "-q", "--verify", "HEAD^{commit}", check=False).returncode == 0
    committed = parse_tree(git(root, "ls-tree", "-r", "-z", "HEAD").stdout) if head_exists else []
    inspected: set[tuple[str, str]] = set()
    checked = 0
    for label, entries in (("HEAD", committed), ("index", index)):
        for entry in entries:
            checked += 1
            item = f"{label}:{entry.path}"
            if entry.path not in PUBLIC_SAFE_FILES:
                issues.append(f"{item}: outside public allowlist")
                continue
            if entry.stage != 0:
                issues.append(f"{item}: unresolved merge-index entry")
                continue
            if entry.mode != ALLOWED_MODE:
                issues.append(f"{item}: prohibited Git mode {entry.mode}")
                continue
            if (entry.path, entry.sha) in inspected:
                continue
            inspected.add((entry.path, entry.sha))
            size = int(git(root, "cat-file", "-s", entry.sha).stdout.strip())
            if size > MAX_FILE_BYTES:
                issues.append(f"{item}: exceeds {MAX_FILE_BYTES} byte limit")
                continue
            blob = git(root, "cat-file", "blob", entry.sha).stdout
            for issue in validate_content(entry.path, blob):
                issues.append(f"{item}: {issue}")
    return checked, sorted(set(issues))


def main() -> int:
    """Return 0 only if the committed and staged public trees are safe."""
    root = Path(__file__).resolve().parents[1]
    try:
        count, issues = validate_repository(root)
    except (OSError, subprocess.CalledProcessError, ValueError) as exc:
        print(f"Public preflight could not inspect Git objects: {exc}", file=sys.stderr)
        return 2
    if issues:
        print("Public repository preflight rejected the following entries:", file=sys.stderr)
        for issue in issues:
            print(f"  {issue}", file=sys.stderr)
        return 1
    print(f"Public repository preflight passed ({count} committed and staged records).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
