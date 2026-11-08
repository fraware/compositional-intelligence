#!/usr/bin/env python3
"""Independently inspect publication text against privately supplied V3 DOCX files.

This optional command checks the original file hashes, table inventory and
source paragraph overlap. It never uploads or modifies the DOCX files.
Lexical overlap is a diagnostic, not proof of full textual or semantic identity.
"""
from __future__ import annotations

import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import unicodedata
from xml.etree import ElementTree
from zipfile import BadZipFile, ZipFile

ROOT = Path(__file__).resolve().parents[1]
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def tokens(value: str) -> list[str]:
    """Normalize typography for reproducible source phrase comparison."""
    return re.findall(r"[\w]+", unicodedata.normalize("NFKC", value).casefold())


def phrases(words: list[str], size: int = 5) -> set[tuple[str, ...]]:
    """Return contiguous n-grams in source order."""
    return {tuple(words[i:i + size]) for i in range(len(words) - size + 1)}


def read_word(path: Path) -> tuple[list[str], int]:
    """Read text and table counts directly from the standard DOCX XML."""
    with ZipFile(path) as archive:
        root = ElementTree.fromstring(archive.read("word/document.xml"))
    paragraphs: list[str] = []
    for paragraph in root.iter(W + "p"):
        chunks = []
        for node in paragraph.iter():
            if node.tag == W + "t":
                chunks.append(node.text or "")
            elif node.tag in {W + "tab", W + "br", W + "cr"}:
                chunks.append(" ")
        if "".join(chunks).strip():
            paragraphs.append("".join(chunks))
    return paragraphs, sum(1 for _ in root.iter(W + "tbl"))


class Paragraphs(HTMLParser):
    """Collect authored HTML paragraphs without generated table labels."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.values: list[str] = []
        self.current: list[str] | None = None
        self.skip = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "p" and self.current is None:
            self.current = []
            self.skip = "table-display-caption" in (dict(attrs).get("class") or "")
        elif tag == "br" and self.current is not None:
            self.current.append(" ")

    def handle_data(self, data: str) -> None:
        if self.current is not None:
            self.current.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "p" and self.current is not None:
            if not self.skip:
                text = "".join(self.current)
                if len(tokens(text)) >= 15:
                    self.values.append(text)
            self.current = None
            self.skip = False


def overlap(paragraph: str, original: set[tuple[str, ...]]) -> float:
    """Measure source-supported contiguous five-token phrases."""
    words = tokens(paragraph)
    count = max(0, len(words) - 4)
    if count == 0:
        return 1.0
    return sum(tuple(words[i:i + 5]) in original for i in range(count)) / count


def audit(slug: str, record: dict, files_by_hash: dict[str, Path],
          threshold: float) -> list[str]:
    """Cross-check one source independently and identify review obligations."""
    expected = record["source_sha256"]
    original = files_by_hash.get(expected)
    if original is None:
        return [f"{slug}: original DOCX with SHA-256 {expected} is unavailable"]
    manuscript_path = ROOT / "essays" / (slug + ".md")
    source = manuscript_path.read_text(encoding="utf-8")
    if hashlib.sha256(manuscript_path.read_bytes()).hexdigest() != record["markdown_sha256"]:
        return [f"{slug}: committed publication source hash differs from manifest"]
    try:
        doc_paragraphs, table_count = read_word(original)
    except (BadZipFile, KeyError, ElementTree.ParseError, OSError) as exc:
        return [f"{slug}: cannot parse original DOCX: {exc}"]
    _, sep, body = source.partition("-->")
    if not sep or "AUTHORITATIVE-DOCX SHA256 " not in source[:source.index(sep)]:
        return [f"{slug}: missing publication source marker"]
    reader = Paragraphs()
    reader.feed(body)
    source_phrases = phrases(tokens(" ".join(doc_paragraphs)))
    scores = [overlap(text, source_phrases) for text in reader.values]
    passing = sum(score >= threshold for score in scores)
    print(f"{slug}: authentic DOCX SHA-256 confirmed; "
          f"paragraph overlap {passing}/{len(scores)} at {threshold:.0%}; "
          f"DOCX tables {table_count}")
    problems: list[str] = []
    if slug != "compositional-intelligence" and table_count != record["table_count"]:
        problems.append(f"{slug}: table counts differ: DOCX {table_count}, "
                        f"publication {record['table_count']}")
    for text, score in zip(reader.values, scores, strict=True):
        if score < threshold:
            problems.append(f"{slug}: paragraph needs inspection ({score:.0%} overlap): "
                            f"{text.strip()[:130]!r}")
    return problems


def main() -> int:
    """Audit only local originals, without introducing sensitive files to Git."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--original-dir", type=Path, required=True)
    parser.add_argument("--slug", action="append", help="Optional essay slug; repeatable")
    parser.add_argument("--min-overlap", type=float, default=0.90)
    args = parser.parse_args()
    if not 0 < args.min_overlap <= 1:
        parser.error("--min-overlap must be in (0, 1]")
    manifest = json.loads((ROOT / "sources" / "originals.json").read_text(
        encoding="utf-8"))["documents"]
    slugs = args.slug or list(manifest)
    if any(slug not in manifest for slug in slugs):
        parser.error("unknown essay slug")
    files_by_hash = {
        hashlib.sha256(path.read_bytes()).hexdigest(): path
        for path in sorted(args.original_dir.glob("*.docx")) if path.is_file()
    }
    findings: list[str] = []
    for slug in slugs:
        findings.extend(audit(slug, manifest[slug], files_by_hash, args.min_overlap))
    if findings:
        for finding in findings:
            print("REVIEW:", finding)
        print(f"REVIEW REQUIRED: {len(findings)} findings")
        return 1
    print(f"PASS: {len(slugs)} original DOCX hashes and lexical comparisons audited")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
