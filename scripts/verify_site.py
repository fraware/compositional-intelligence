#!/usr/bin/env python3
"""Verify the publication artifact using only the Python standard library.

This checks the source manifest, generated-site navigation, manuscript
provenance, bibliographic anchors, and basic semantic accessibility. It does not assert that GitHub Pages is deployed,
that external URLs are reachable, or that research claims are validated.
"""

from __future__ import annotations

import collections
import hashlib
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"
URL = "https://fraware.github.io/compositional-intelligence/"


class Document(HTMLParser):
    """Collect structural evidence from a single static HTML document."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.links: list[str] = []
        self.canonicals: list[str] = []
        self.og_urls: list[str] = []
        self.lang: str | None = None
        self.main = 0
        self.h1 = 0
        self.tables = 0
        self.theads = 0
        self.tbodies = 0
        self.invalid_captions: list[str] = []
        self.header_markup_errors: list[str] = []
        self.table_column_counts: list[int] = []
        self.maths = 0
        self.display_maths = 0
        self.annotations = 0
        self.figures = 0
        self.figcaptions = 0
        self.math_scrolls = 0
        self.invalid_math_scrolls: list[str] = []
        self.captions = 0
        self.caption_texts: list[str] = []
        self._in_caption = False
        self.table_ids: list[str | None] = []
        self.table_wrappers = 0
        self.invalid_table_wrappers: list[str] = []
        self.th = 0
        self.scoped_th = 0
        self.scripts = 0
        self.script_sources: list[tuple[str | None, str | None]] = []
        self.source_hashes: list[str] = []
        self.unsafe_attributes: list[str] = []
        self.noindex = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        if tag == "html":
            self.lang = data.get("lang")
        if tag == "main":
            self.main += 1
        if tag == "h1":
            self.h1 += 1
        if tag == "math":
            self.maths += 1
            if data.get("display") == "block":
                self.display_maths += 1
        if tag == "annotation" and data.get("encoding") == "application/x-tex":
            self.annotations += 1
        if tag == "figure":
            self.figures += 1
        if tag == "figcaption":
            self.figcaptions += 1
        if tag == "div" and "math-scroll" in (data.get("class") or "").split():
            self.math_scrolls += 1
            if data.get("role") != "group" or data.get("tabindex") != "0" or not data.get("aria-label"):
                self.invalid_math_scrolls.append("Missing MathML scroll semantics")
        if tag == "thead":
            self.theads += 1
        if tag == "tbody":
            self.tbodies += 1
        if tag == "table":
            self.tables += 1
            self.table_ids.append(data.get("id"))
        if tag == "div" and "table-scroll" in (data.get("class") or "").split():
            self.table_wrappers += 1
            columns = data.get("data-columns")
            if columns is None or not columns.isdecimal() or not (1 <= int(columns) <= 12):
                self.invalid_table_wrappers.append("Missing valid table column count")
            else:
                self.table_column_counts.append(int(columns))
            if data.get("role") != "group" or data.get("tabindex") != "0" or not data.get("aria-label"):
                self.invalid_table_wrappers.append("Missing keyboard scrolling or accessible name")
        if tag == "caption":
            self.captions += 1
            if "table-caption" not in (data.get("class") or "").split():
                self.invalid_captions.append("Table caption must be visible")
            self._in_caption = True
            self.caption_texts.append("")
        if tag == "th":
            self.th += 1
            if "ead" in data or data.get("scope") not in {"col", "row"}:
                self.header_markup_errors.append("Malformed or unscoped table header")
            if data.get("scope") in {"col", "row"}:
                self.scoped_th += 1
        if tag == "script":
            self.scripts += 1
            self.script_sources.append((data.get("src"), data.get("type")))
        if tag == "meta" and data.get("name") == "source-sha256":
            self.source_hashes.append(data.get("content") or "")
        if "id" in data and data["id"]:
            self.ids.append(data["id"])
        if tag in {"a", "link"} and data.get("href") is not None:
            self.links.append(data["href"] or "")
        if tag in {"img", "script"} and data.get("src") is not None:
            self.links.append(data["src"] or "")
        if tag == "link" and data.get("rel") == "canonical":
            self.canonicals.append(data.get("href", ""))
        if tag == "meta" and data.get("property") == "og:url":
            self.og_urls.append(data.get("content", ""))
        if tag == "meta" and data.get("name") == "robots" and "noindex" in (data.get("content") or "").lower():
            self.noindex = True
        for key in data:
            if key.lower().startswith("on") or key.lower().startswith("data-review"):
                self.unsafe_attributes.append(key)

    def handle_data(self, data: str) -> None:
        if self._in_caption:
            self.caption_texts[-1] += data

    def handle_endtag(self, tag: str) -> None:
        if tag == "caption":
            self._in_caption = False


def parse_html(path: Path) -> Document:
    """Parse HTML into the structural audit representation."""
    document = Document()
    document.feed(path.read_text(encoding="utf-8"))
    document.close()
    return document


def check_manifest(issues: list[str]) -> None:
    """Validate every file against the release SHA-256 manifest."""
    manifest = ROOT / "SHA256SUMS"
    if not manifest.is_file():
        issues.append("Missing SHA256SUMS")
        return
    seen: set[str] = set()
    for line_number, line in enumerate(manifest.read_text(encoding="utf-8").splitlines(), 1):
        parts = line.split("  ", 1)
        if len(parts) != 2 or len(parts[0]) != 64:
            issues.append(f"Invalid checksum entry on line {line_number}")
            continue
        expected, rel = parts
        if rel in seen:
            issues.append(f"Duplicate manifest path: {rel}")
        seen.add(rel)
        target = (ROOT / rel).resolve()
        if not target.is_relative_to(ROOT) or not target.is_file():
            issues.append(f"Missing or unsafe manifest target: {rel}")
            continue
        actual = hashlib.sha256(target.read_bytes()).hexdigest()
        if actual != expected:
            issues.append(f"Checksum mismatch: {rel}")
    published = {
        p.relative_to(ROOT).as_posix()
        for p in ROOT.rglob("*")
        if p.is_file() and ".git" not in p.parts and p != manifest
    }
    # Repo-owned deployment scripts are reviewed source, not part of the
    # original publication checksum set. All published reading files are.
    published = {p for p in published if not p.startswith(("scripts/", ".github/", "_site/", "__pycache__/")) and "/__pycache__/" not in p}
    for path in sorted(published - seen):
        issues.append(f"Published file absent from checksum manifest: {path}")
    for path in sorted(seen - published):
        issues.append(f"Manifest contains an unexpected path: {path}")


def main() -> int:
    """Return nonzero if any local release assertion fails."""
    issues: list[str] = []
    check_manifest(issues)
    pages = sorted(SITE.rglob("*.html"))
    essays = sorted((ROOT / "essays").glob("*.md"))
    if len(pages) != 12 or len(essays) != 9:
        issues.append(f"Expected 12 HTML pages and 9 Markdown essays, got {len(pages)} and {len(essays)}")
    if not (SITE / "index.html").is_file() or not (SITE / ".nojekyll").is_file():
        issues.append("Missing HTML entrypoint or .nojekyll")
    documents = {p: parse_html(p) for p in pages}
    canonical_set: set[str] = set()
    total_tables = 0
    total_links = 0
    total_display_maths = 0
    total_figures = 0
    expected_media = {
        "compositional-intelligence": (6, 2),
        "semantic-participation": (1, 0),
        "typed-generativity": (1, 0),
        "functorial-consistency": (1, 0),
        "lambek-machines": (1, 2),
        "algebraic-architectures": (1, 0),
        "quantitative-curry-howard": (3, 0),
        "effectful-and-conceptual-intelligence": (3, 0),
        "series-preface": (0, 0),
    }

    for page, doc in documents.items():
        relative = page.relative_to(SITE).as_posix()
        target_canonical = URL if relative == "index.html" else URL + ("reading/" if relative == "reading/index.html" else relative)
        canonical_set.add(target_canonical)
        if doc.lang != "en" or doc.main != 1 or doc.h1 != 1 or doc.noindex:
            issues.append(f"Incorrect document semantics: {relative}")
        if doc.canonicals != [target_canonical] or doc.og_urls != [target_canonical]:
            issues.append(f"Canonical/OG URL mismatch: {relative}")
        if doc.unsafe_attributes:
            issues.append(f"Unexpected event handler in {relative}")
        allowed_scripts = [("./commuting-square.mjs", "module")] if relative == "studies/commuting-square.html" else []
        if doc.script_sources != allowed_scripts:
            issues.append(f"Unexpected script inclusion in {relative}")
        duplicates = [id_ for id_, n in collections.Counter(doc.ids).items() if n > 1]
        if duplicates:
            issues.append(f"Duplicate identifiers in {relative}: {duplicates[:3]}")
        if doc.maths != doc.annotations or doc.display_maths != doc.math_scrolls:
            issues.append(f"Unusable MathML or non-scrollable display equation: {relative}")
        if doc.invalid_math_scrolls:
            issues.append(f"Non-keyboard-accessible equation: {relative}")
        if doc.figures != doc.figcaptions:
            issues.append(f"Figure missing visible caption: {relative}")
        if relative.startswith("essays/"):
            slug = page.stem
            if (doc.display_maths, doc.figures) != expected_media[slug]:
                issues.append(f"Equation/figure inventory does not match publication: {relative} "
                              f"got {doc.display_maths} equations and {doc.figures} figures")
        total_display_maths += doc.display_maths
        total_figures += doc.figures
        if (doc.tables != doc.captions or doc.tables != doc.theads or
            doc.tables != doc.tbodies or doc.th != doc.scoped_th or
            doc.header_markup_errors or doc.invalid_captions):
            issues.append(f"Malformed HTML table section/header/caption in {relative}")
        if (doc.tables != doc.table_wrappers or doc.invalid_table_wrappers or
            doc.tables != len(doc.table_column_counts)):
            issues.append(f"Table scrolling accessibility mismatch: {relative}")
        if doc.tables and doc.table_ids != [f"table-{n}" for n in range(1, doc.tables + 1)]:
            issues.append(f"Unstable table identifiers in {relative}")
        if any(len(label.strip()) < 30 or not label.strip().startswith("Table ")
               for label in doc.caption_texts):
            issues.append(f"Missing or uninformative visible table caption: {relative}")
        if relative.startswith("essays/"):
            manuscript = ROOT / "essays" / page.with_suffix(".md").name
            if not manuscript.is_file():
                issues.append(f"Missing Markdown source for {relative}")
            else:
                expected_hash = hashlib.sha256(manuscript.read_bytes()).hexdigest()
                if doc.source_hashes != [expected_hash]:
                    issues.append(f"Source provenance mismatch: {relative}")
        elif doc.source_hashes:
            issues.append(f"Unexpected manuscript provenance on {relative}")
        total_tables += doc.tables
        total_links += len(doc.links)

        for raw in doc.links:
            split = urlsplit(raw)
            if split.scheme in {"http", "https", "mailto", "tel"}:
                continue
            if split.scheme or split.netloc or raw.startswith("//"):
                issues.append(f"Unsafe link in {relative}: {raw}")
                continue
            file_path = (page.parent / unquote(split.path)).resolve() if split.path else page
            if file_path.is_dir():
                file_path = file_path / "index.html"
            if not file_path.is_relative_to(SITE) or not file_path.is_file():
                issues.append(f"Missing local link in {relative}: {raw}")
                continue
            if split.fragment and file_path.suffix.lower() == ".html":
                destination = documents.get(file_path)
                if destination is None:
                    destination = parse_html(file_path)
                if unquote(split.fragment) not in destination.ids:
                    issues.append(f"Broken anchor in {relative}: {raw}")

    sitemap = SITE / "sitemap.xml"
    if sitemap.is_file():
        namespace = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
        try:
            root = ElementTree.parse(sitemap).getroot()
            urls = [x.text for x in root.findall(f".//{namespace}loc")]
            if len(urls) != 12 or set(urls) != canonical_set:
                issues.append("Sitemap URLs differ from public HTML canonicals")
        except ElementTree.ParseError as exc:
            issues.append(f"Invalid sitemap: {exc}")
    else:
        issues.append("Missing sitemap")

    if issues:
        for issue in issues:
            print(f"FAIL: {issue}")
        print(f"FAIL: {len(issues)} publication checks failed")
        return 1
    print(f"PASS: {len(pages)} HTML pages, {len(essays)} sources, {total_links} links, {total_tables} tables, {total_display_maths} display equations, {total_figures} figures; checksums and sitemap verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
