#!/usr/bin/env python3
"""Reject unpublished manuscript material in the public repository tree.

This preflight allowlist checks Git-tracked paths, including staged additions. It
is advisory until the repository separately enforces an appropriate CI policy.
Do not treat it as authorization to publish research material.
"""

from __future__ import annotations

import subprocess
import sys
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


def unsafe_paths(paths: list[str]) -> list[str]:
    """Return all repository paths outside the explicitly reviewed allowlist."""
    return sorted({path for path in paths if path not in PUBLIC_SAFE_FILES})


def tracked_paths(root: Path) -> list[str]:
    """List version-controlled files without losing spaces or Unicode names."""
    result = subprocess.run(
        ["git", "-C", str(root), "ls-files", "-z", "--cached"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return [path.decode("utf-8", errors="surrogateescape") for path in result.stdout.split(b"\0") if path]


def main() -> int:
    """Fail closed if the checkout cannot be inspected or contains other paths."""
    root = Path(__file__).resolve().parents[1]
    try:
        paths = tracked_paths(root)
    except (OSError, subprocess.CalledProcessError) as exc:
        print(f"Unable to inspect Git index: {exc}", file=sys.stderr)
        return 2
    unsafe = unsafe_paths(paths)
    if unsafe:
        print("Public repository preflight rejected the following paths:", file=sys.stderr)
        for path in unsafe:
            print(f"  {path}", file=sys.stderr)
        return 1
    print(f"Public repository preflight passed ({len(paths)} tracked files).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
