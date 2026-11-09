#!/usr/bin/env python3
"""Check that the deployed essay bodies preserve the uploaded V3 source text.

The document originals intentionally contain plain-text mathematical schemas.
These are not silently rewritten into newer or different mathematical claims.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import build_site

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site" / "essays"


def main() -> int:
    originals = json.loads(
        (ROOT / "sources" / "originals.json").read_text(encoding="utf-8")
    )["documents"]
    problems: list[str] = []
    for slug, title, _, _ in build_site.ESSAYS:
        path = ROOT / "essays" / f"{slug}.md"
        published = SITE / f"{slug}.html"
        if not published.is_file():
            problems.append(f"{slug}: published page is missing")
            continue
        original = originals[slug]
        source = path.read_text(encoding="utf-8")
        if hashlib.sha256(path.read_bytes()).hexdigest() != original["markdown_sha256"]:
            problems.append(f"{slug}: source differs from the converted original")
            continue
        body, _ = build_site.source_to_body(source, title, [])
        if slug == "compositional-intelligence":
            body = build_site.render_synthesis_figures(body)
        if slug == "functorial-consistency":
            body = build_site.render_functorial_diagram(body)
        body = build_site.enhance_scientific_presentation(body)
        if slug == "series-preface":
            body = build_site.render_preface(body)
        if slug == "semantic-participation":
            body = build_site.render_semantic_participation(body)
        if slug == "typed-generativity":
            body = build_site.render_typed_generativity(body)
        if slug == "functorial-consistency":
            body = build_site.render_functorial_tables(body)
        page = published.read_text(encoding="utf-8")
        if body not in page:
            problems.append(f"{slug}: displayed essay body differs from source HTML")
        if page.count('<h1>') != 1:
            problems.append(f"{slug}: multiple visible titles")
        if '<p class="byline">' in page:
            problems.append(f"{slug}: author name appears beneath essay title")
    if problems:
        for problem in problems:
            print("FAIL:", problem)
        return 1
    print(f"PASS: {len(originals)} hashed publication sources match their typeset HTML bodies")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
