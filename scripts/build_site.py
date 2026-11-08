#!/usr/bin/env python3
"""Build the static publication directly from the canonical Markdown manuscripts.

Usage:
  python3 scripts/build_site.py --output _site
  python3 scripts/build_site.py --output _site --reproducibility-check

Requires Pandoc 3.1.13. All rendering inputs are checked into this repository.
No dynamic network access is used by the builder.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://fraware.github.io/compositional-intelligence/"
PANDOC_VERSION = "3.1.13"

# Publication order, short editorial descriptions, and the original section labels.
ESSAYS = [
    ("compositional-intelligence", "Compositional Intelligence", "Synthesis",
     "A framework for the evaluation of AI-generated artifacts in structured worlds."),
    ("series-preface", "Series Preface", "Orientation",
     "The aims, scope, and conceptual sequence of the essay collection."),
    ("semantic-participation", "Semantic Participation", "01 · Foundations",
     "Conditions under which generated artifacts become participants in structured environments."),
    ("typed-generativity", "Typed Generativity", "02 · Foundations",
     "Generation as construction of candidate artifacts with declared types."),
    ("functorial-consistency", "Functorial Consistency", "03 · Foundations",
     "Evaluation of structure-preserving transformations across representations."),
    ("lambek-machines", "Lambek Machines", "04 · Language",
     "Typed composition and grammatical structure in language models."),
    ("algebraic-architectures", "Algebraic Architectures", "05 · Architectures",
     "The relationship of neural model architecture to task structure."),
    ("quantitative-curry-howard", "Quantitative Curry–Howard", "06 · Evidence",
     "The status of scores, uncertainty, and evidence in typed reasoning."),
    ("effectful-and-conceptual-intelligence", "Effectful and Conceptual Intelligence",
     "07 · Action", "Agent action, authority, effects, and conceptual transfer."),
]

HEADINGS = re.compile(r"<h([23])\b[^>]*\bid=\"([^\"]+)\"[^>]*>(.*?)</h\1>", re.S)
TABLE = re.compile(r"<table\b[^>]*>[\s\S]*?</table>", re.I)
TABLE_NAME = re.compile(r"^Table\s+([A-Za-z]?\d+[A-Za-z]?)\.\s*(.+?)\s*$", re.I)
MARKDOWN_SECTION = re.compile(r"^#{2,4}\s+.*?\{#([a-z0-9-]+)\}\s*$", re.M)
TITLE_AUTHOR = re.compile(r"\A# ([^\n]+)\n\n\*Mateo Petel\*\n\n", re.M)


def esc(value: str) -> str:
    """Escape an authored string for an HTML text or quoted-attribute context."""
    return html.escape(value, quote=True)


def header(title: str, description: str, canonical: str, *, document_type: str = "article") -> str:
    """Provide a stable, privacy-preserving document head and shared navigation."""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#ffffff">
<meta name="description" content="{esc(description)}">
<meta name="author" content="Mateo Petel">
<meta property="og:type" content="{esc(document_type)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{esc(canonical)}">
<link rel="canonical" href="{esc(canonical)}">
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../style.css">
<title>{esc(title)} · Compositional Intelligence</title>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><div class="container header-inner">
<a class="brand" href="../index.html">Compositional Intelligence</a>
<nav class="header-nav" aria-label="Primary navigation">
<a href="../index.html#essays">Essays</a><a href="../essays/compositional-intelligence.html">The thesis</a>
</nav></div></header>
<main class="container" id="main">
"""


def footer() -> str:
    """Provide the common copyright footer without client-side dependencies."""
    return """</main>
<footer class="site-footer"><div class="container"><span>Compositional Intelligence · Mateo Petel</span><span>© 2026 Mateo Petel</span></div></footer>
</body></html>
"""


def heading_text(raw: str) -> str:
    """Remove the limited inline markup from a generated heading label."""
    return html.unescape(re.sub(r"<[^>]+>", "", raw)).strip()


def verify_table_catalog(markdown: str, captions: list[dict[str, str]], title: str) -> None:
    """Keep table descriptions attached to the exact manuscript table they describe."""
    original_tables = list(TABLE.finditer(markdown))
    if len(original_tables) != len(captions):
        raise ValueError(f"{title}: table catalogue count differs from manuscript")
    for index, (match, entry) in enumerate(zip(original_tables, captions, strict=True), 1):
        digest = hashlib.sha256(match.group().encode("utf-8")).hexdigest()
        label = entry.get("caption", "")
        if digest != entry.get("source_sha256"):
            raise ValueError(f"{title}: table {index} changed; review its accessible description")
        if not isinstance(label, str) or len(label.strip()) < 20:
            raise ValueError(f"{title}: table {index} lacks a meaningful description")


def render_tables(body: str, captions: list[dict[str, str]]) -> str:
    """Render validated native tables with intact sectioning and readable captions.

    Existing manuscript labels become the visible caption's table number.
    The source-bound descriptive caption supplies the accessible table name.
    Column counts are retained for responsive layout and browser assertions.
    """
    counter = 0
    result: list[str] = []
    position = 0
    tokens = re.compile(r"<h[23]\b[^>]*>.*?</h[23]>|<table\b[^>]*>.*?</table>", re.S | re.I)
    preceding_label = re.compile(
        r"<p>Table(?:\s+([A-Za-z]?\d+[A-Za-z]?))?\.\s*[^<]*</p>\s*$", re.I
    )
    for match in tokens.finditer(body):
        before = body[position:match.start()]
        token = match.group()
        if not token.lower().startswith("<table"):
            result.extend((before, token))
            position = match.end()
            continue

        counter += 1
        if counter > len(captions):
            raise ValueError("Rendered table exceeds source-bound caption catalogue")
        description = captions[counter - 1]["caption"]
        label_match = preceding_label.search(before)
        number = label_match.group(1) if label_match and label_match.group(1) else str(counter)
        if label_match:
            before = before[:label_match.start()] + "\n"
        result.append(before)

        first_row = re.search(r"<tr\b[^>]*>(.*?)</tr>", token, re.I | re.S)
        if not first_row:
            raise ValueError(f"Table {counter} has no header row")
        header = first_row.group(1)
        cells = re.findall(r"<(?:th|td)\b([^>]*)>", header, re.I)
        if not cells:
            raise ValueError(f"Table {counter} has no header cells")
        columns = 0
        for attrs in cells:
            colspan = re.search(r'\bcolspan\s*=\s*["\x27]?(\d+)', attrs, re.I)
            columns += int(colspan.group(1)) if colspan else 1
        if not (1 <= columns <= 12):
            raise ValueError(f"Table {counter} has invalid column count: {columns}")

        token = re.sub(
            r"<table\b([^>]*)>",
            lambda m: f'<table id="table-{counter}"{m.group(1)}>',
            token, count=1, flags=re.I,
        )
        if re.search(r"<caption\b", token, re.I):
            raise ValueError(f"Table {counter} unexpectedly contains a prior caption")
        caption_text = "Table " + str(number) + ". " + description
        # The visual caption is outside the scroll region, so its complete
        # wording stays in view on narrow screens. Native table caption
        # semantics remain available to assistive technology.
        token = re.sub(
            r"(<table\b[^>]*>)",
            lambda m: m.group(1) + "\n" +
            '<caption class="visually-hidden">' + esc(caption_text) + "</caption>",
            token, count=1, flags=re.I,
        )

        # Crucially, match <th> only. A previous expression also matched <thead>,
        # corrupting every table header while leaving superficial counts unchanged.
        token = re.sub(
            r"<th\b([^>]*)>",
            lambda m: ('<th' +
                       ('' if re.search(r'\bscope\s*=', m.group(1), re.I) else ' scope="col"') +
                       m.group(1) + '>'),
            token, flags=re.I,
        )
        if not re.search(r"<thead\b", token, re.I) or not re.search(r"</thead>", token, re.I):
            raise ValueError(f"Table {counter} lacks intact semantic header structure")

        result.append(
            f'<p id="table-{counter}-caption" class="table-display-caption">'
            f'<span class="table-caption-number">Table {esc(number)}</span> '
            f'{esc(description)}</p>\n'
            f'<div class="table-scroll" data-columns="{columns}" tabindex="0" '
            f'role="group" aria-labelledby="table-{counter}-caption">'
            + "\n" + token + "\n</div>\n"
        )
        if columns >= 2:
            result.append('<p class="table-scroll-hint">Scroll sideways for remaining columns.</p>\n')
        position = match.end()
    result.append(body[position:])
    if counter != len(captions):
        raise ValueError(f"Rendered {counter} tables, expected {len(captions)}")
    return "".join(result)


def render_schema_blocks(body: str) -> str:
    """Preserve the authored line breaks in structured manuscript records.

    Only plain-text multiline blockquotes are transformed. Ordinary quoted
    arguments and paragraphs retain their original blockquote semantics.
    """
    block = re.compile(r"<blockquote>\s*(.*?)\s*</blockquote>", re.S | re.I)
    def convert(match: re.Match[str]) -> str:
        raw = match.group(1)
        if "<a " in raw or "<math" in raw or "<table" in raw:
            return match.group()
        lines = re.sub(r"<br\s*/?>", "\n", raw, flags=re.I)
        lines = re.sub(r"</p>\s*<p>", "\n", lines, flags=re.I)
        lines = re.sub(r"</?p>", "", lines, flags=re.I)
        if re.search(r"<[A-Za-z]", lines):
            return match.group()
        plain = html.unescape(lines).strip()
        pieces = [line.strip() for line in plain.split("\n") if line.strip()]
        if len(pieces) < 3 or (len(pieces) < 5 and not any(
            symbol in pieces[0] for symbol in ("=", ":", "{")
        )):
            return match.group()
        if any(len(line) > 350 for line in pieces):
            return match.group()
        return ('<div class="record-schema" role="group" tabindex="0" '
                'aria-label="Structured record or notation">'
                '<pre><code>' + esc("\n".join(pieces)) +
                '</code></pre></div>')
    return block.sub(convert, body)


def render_math(body: str) -> str:
    """Place Pandoc's semantic display MathML inside accessible scroll regions.

    This preserves native MathML and its embedded TeX annotation. Chromium
    renders the expression; keyboard users can reach a horizontal overflow
    region without cropping the formula or forcing page-level overflow.
    """
    pattern = re.compile(r'<p>\s*(<math\b[^>]*\bdisplay="block"[^>]*>.*?</math>)\s*</p>', re.S)
    def wrap(match: re.Match[str]) -> str:
        return ('<div class="math-scroll" role="group" tabindex="0" '
                'aria-label="Displayed mathematical expression">' +
                match.group(1) + '</div>')
    return pattern.sub(wrap, body)


def render_toc(body: str) -> str:
    """Construct section navigation from the exact anchors in the generated page."""
    sections = []
    for level, ident, title in HEADINGS.findall(body):
        label = heading_text(title)
        if int(level) == 2 and label not in {"Abstract", "References"}:
            sections.append((ident, label))
    if not sections:
        return ""
    links = "".join(f'<li><a href="#{esc(ident)}">{esc(label)}</a></li>' for ident, label in sections)
    return f'<nav class="article-toc" aria-label="On this page"><details><summary>On this page</summary><ol>{links}</ol></details></nav>\n'


def source_to_body(markdown: str, expected_title: str, table_captions: list[dict[str, str]]) -> tuple[str, str]:
    """Render the authored Markdown to HTML with a fixed Pandoc release."""
    match = TITLE_AUTHOR.match(markdown)
    if not match or match.group(1) != expected_title:
        raise ValueError(f"Manuscript title/author mismatch: expected {expected_title}")
    source_body = markdown[match.end():]
    verify_table_catalog(source_body, table_captions, expected_title)
    command = ["pandoc", "--from=markdown+raw_html", "--to=html5", "--mathml", "--wrap=none"]
    rendered = subprocess.run(command, input=source_body, text=True, capture_output=True, check=True)
    body = render_schema_blocks(render_tables(render_math(rendered.stdout.rstrip() + "\n"), table_captions))
    for ident in MARKDOWN_SECTION.findall(source_body):
        if f'id="{ident}"' not in body:
            raise ValueError(f"Missing rendered heading anchor {ident!r}: {expected_title}")
    return body, hashlib.sha256(markdown.encode("utf-8")).hexdigest()


def render_essay(slug: str, title: str, category: str, description: str, position: int, table_captions: list[dict[str, str]]) -> str:
    """Render a manuscript with source provenance, toc, and sequential links."""
    manuscript = (ROOT / "essays" / (slug + ".md")).read_text(encoding="utf-8")
    body, digest = source_to_body(manuscript, title, table_captions)
    before = ESSAYS[position - 1] if position > 0 else None
    after = ESSAYS[position + 1] if position < len(ESSAYS) - 1 else None
    prev_link = (f'<div class="previous"><span>Previous</span><a href="{esc(before[0])}.html">{esc(before[1])}</a></div>'
                 if before else '<div></div>')
    next_link = (f'<div class="next"><span>Next</span><a href="{esc(after[0])}.html">{esc(after[1])}</a></div>'
                 if after else '<div></div>')
    src_meta = f'<meta name="source-sha256" content="{digest}">\n'
    head = header(title, description, BASE + "essays/" + slug + ".html")
    head = head.replace("</head>", src_meta + "</head>", 1)
    return (head +
            '<article><header class="article-header"><p class="breadcrumb"><a href="../index.html">Essays</a> / ' +
            esc(category) + '</p><h1>' + esc(title) + '</h1><p class="byline">Mateo Petel</p>' +
            '</header><div class="article-content" id="article-content">\n' +
            render_toc(body) + body + '</div>\n' +
            '<nav class="article-pager" aria-label="Essay navigation">' + prev_link + next_link + '</nav>' +
            '</article>\n' + footer())


def render_sitemap() -> str:
    """Generate the public sitemap from the same declared publication inventory."""
    paths = [""] + [f"essays/{row[0]}.html" for row in ESSAYS] + [
        "studies/commuting-square.html"
    ]
    root = ElementTree.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for path in paths:
        item = ElementTree.SubElement(root, "url")
        ElementTree.SubElement(item, "loc").text = BASE + path
    ElementTree.indent(root, space="  ")
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + ElementTree.tostring(root, encoding="unicode") + "\n"


def build(output: Path) -> None:
    """Construct a fresh publication directory without modifying source files."""
    if output.resolve() in {ROOT.resolve(), (ROOT / "docs").resolve()}:
        raise ValueError("Build directory cannot replace the repository or source assets")
    pandoc = subprocess.run(["pandoc", "--version"], capture_output=True, text=True, check=True)
    if not pandoc.stdout.splitlines()[0].strip() == "pandoc " + PANDOC_VERSION:
        raise RuntimeError(f"Pandoc {PANDOC_VERSION} required; found {pandoc.stdout.splitlines()[0]}")
    if output.exists():
        shutil.rmtree(output)
    shutil.copytree(ROOT / "docs", output)
    # The manuscript renderer, not any preexisting snapshot, owns published essay pages.
    shutil.rmtree(output / "essays", ignore_errors=True)
    shutil.rmtree(output / "atlas", ignore_errors=True)
    shutil.rmtree(output / "reading", ignore_errors=True)
    (output / "essays").mkdir(parents=True)
    catalogue = json.loads((ROOT / "tables" / "captions.json").read_text(encoding="utf-8"))
    if catalogue.get("schema_version") != 1 or set(catalogue["essays"]) != {row[0] for row in ESSAYS} - {"series-preface"}:
        raise ValueError("Table caption catalogue does not match the manuscript inventory")
    for index, row in enumerate(ESSAYS):
        slug = row[0]
        (output / "essays" / (slug + ".html")).write_text(
            render_essay(*row, position=index, table_captions=catalogue["essays"].get(slug, [])),
            encoding="utf-8")
    (output / "sitemap.xml").write_text(render_sitemap(), encoding="utf-8")


def file_digests(path: Path) -> dict[str, str]:
    """Hash all generated files, indexed by their relative path."""
    return {p.relative_to(path).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(path.rglob("*")) if p.is_file()}


def main() -> None:
    """Build and optionally prove deterministic output in two isolated directories."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "_site")
    parser.add_argument("--reproducibility-check", action="store_true")
    args = parser.parse_args()
    output = args.output.resolve()
    build(output)
    if args.reproducibility_check:
        with tempfile.TemporaryDirectory(prefix="ci-publication-") as tmp:
            second = Path(tmp) / "site"
            build(second)
            if file_digests(output) != file_digests(second):
                raise RuntimeError("Non-deterministic publication output detected")
    print(f"Built {len(ESSAYS)} essays, one concept study into {output}")


if __name__ == "__main__":
    main()
