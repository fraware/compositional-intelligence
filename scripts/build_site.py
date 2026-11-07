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


def source_link(value: str) -> str:
    """Resolve a source-section reference in the seven-concept metadata."""
    slug, sep, anchor = value.partition("#")
    if not sep or not re.fullmatch(r"[a-z0-9-]+", slug) or not re.fullmatch(r"[a-z0-9-]+", anchor):
        raise ValueError(f"Invalid section reference: {value}")
    return f"../essays/{slug}.html#{anchor}"


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
<a href="../index.html#essays">Essays</a><a href="../atlas/">Concept Atlas</a><a href="../essays/compositional-intelligence.html">The thesis</a>
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


def render_tables(body: str) -> str:
    """Provide scope and concise captions, preferring explicit manuscript table titles.

    Existing prose labels remain visible. Fallback captions use the current
    section and column headers, without inventing an unseen manuscript title.
    """
    section = "Article"
    counter = 0
    result: list[str] = []
    position = 0
    tokens = re.compile(r"<h[23]\b[^>]*>.*?</h[23]>|<table\b[^>]*>.*?</table>", re.S | re.I)
    for match in tokens.finditer(body):
        result.append(body[position:match.start()])
        token = match.group()
        if token.lower().startswith("<h"):
            section = heading_text(token)
            result.append(token)
        else:
            counter += 1
            previous = body[:match.start()]
            last_para = list(re.finditer(r"<p(?:\s+[^>]*)?>(.*?)</p>\s*$", previous, re.S))
            label = ""
            if last_para:
                text = heading_text(last_para[-1].group(1))
                table_match = TABLE_NAME.match(text)
                if table_match:
                    label = text
            if not label:
                headers = [heading_text(t) for t in re.findall(r"<th\b[^>]*>(.*?)</th>", token, re.S | re.I)]
                header_summary = ", ".join(t for t in headers[:3] if t)
                label = f"Table {counter} in {section}" + (f": {header_summary}" if header_summary else "")
            if not re.search(r"<caption\b", token, re.I):
                token = re.sub(r"(<table\b[^>]*>)",
                               lambda m: m.group(1) + '\n<caption class="visually-hidden">' + esc(label) + "</caption>",
                               token, count=1, flags=re.I)
            token = re.sub(r"<th(?![^>]*\bscope=)", '<th scope="col"', token, flags=re.I)
            result.append(token)
        position = match.end()
    result.append(body[position:])
    return "".join(result)


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


def source_to_body(markdown: str, expected_title: str) -> tuple[str, str]:
    """Render the authored Markdown to HTML with a fixed Pandoc release."""
    match = TITLE_AUTHOR.match(markdown)
    if not match or match.group(1) != expected_title:
        raise ValueError(f"Manuscript title/author mismatch: expected {expected_title}")
    source_body = markdown[match.end():]
    command = ["pandoc", "--from=markdown+raw_html", "--to=html5", "--mathml", "--wrap=none"]
    rendered = subprocess.run(command, input=source_body, text=True, capture_output=True, check=True)
    body = render_tables(rendered.stdout.rstrip() + "\n")
    for ident in MARKDOWN_SECTION.findall(source_body):
        if f'id="{ident}"' not in body:
            raise ValueError(f"Missing rendered heading anchor {ident!r}: {expected_title}")
    return body, hashlib.sha256(markdown.encode("utf-8")).hexdigest()


def render_essay(slug: str, title: str, category: str, description: str, position: int) -> str:
    """Render a manuscript with source provenance, toc, and sequential links."""
    manuscript = (ROOT / "essays" / (slug + ".md")).read_text(encoding="utf-8")
    body, digest = source_to_body(manuscript, title)
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
            '<p class="article-atlas-link"><a href="../atlas/#' + esc(slug) + '">Explore this concept in the Atlas</a></p>' +
            '</header><div class="article-content" id="article-content">\n' +
            render_toc(body) + body + '</div>\n' +
            '<nav class="article-pager" aria-label="Essay navigation">' + prev_link + next_link + '</nav>' +
            '</article>\n' + footer())


def validate_concepts(data: dict) -> None:
    """Fail closed on missing concepts, malformed edges, or unsupported section IDs."""
    concepts = data["concepts"]
    ids = [item["id"] for item in concepts]
    expected = [row[0] for row in ESSAYS[2:]]
    if data.get("schema_version") != 1 or ids != expected or len(ids) != len(set(ids)):
        raise ValueError("Concept atlas must contain the seven series concepts in publication order")
    source_ids = {}
    for item in concepts:
        slug = item["id"]
        src = (ROOT / "essays" / (slug + ".md")).read_text(encoding="utf-8")
        source_ids[slug] = set(MARKDOWN_SECTION.findall(src))
        if not item["question"] or not item["summary"] or len(item["sections"]) < 2:
            raise ValueError(f"Incomplete concept record: {slug}")
        for section in item["sections"]:
            if section["id"] not in source_ids[slug]:
                raise ValueError(f"Unverified source section: {slug}#{section['id']}")
    edges = set()
    if len(data["relations"]) < 7:
        raise ValueError("Concept connections missing")
    for relation in data["relations"]:
        frm, to = relation["from"], relation["to"]
        if frm not in source_ids or to not in source_ids or frm == to:
            raise ValueError(f"Invalid concept connection {frm} -> {to}")
        if (frm, to) in edges or len(relation["evidence"]) < 2:
            raise ValueError("Duplicate or unsupported conceptual connection")
        edges.add((frm, to))
        seen = set()
        for ref in relation["evidence"]:
            slug, _, anchor = ref.partition("#")
            if slug not in (frm, to) or anchor not in source_ids[slug]:
                raise ValueError(f"Unsupported connection evidence: {ref}")
            seen.add(slug)
        if seen != {frm, to}:
            raise ValueError(f"Connection must cite both endpoints: {frm} -> {to}")


def render_atlas(data: dict) -> str:
    """Render the curated graph as accessible, linkable prose, not a decorative network."""
    intro = (
        '<header class="article-header atlas-header"><p class="breadcrumb">'
        '<a href="../index.html">Essays</a> / Concept Atlas</p>'
        '<p class="kicker">Seven concepts · Source-anchored connections</p>'
        '<h1>Concept Atlas</h1>'
        '<p class="deck">A second reading path through Compositional Intelligence.</p></header>'
        '<div class="atlas-intro"><p>The series examines artifact membership, construction, '
        'transformation, language, architecture, warrant, and action. Each concept below '
        'links to exact sections in the published manuscripts. The relationships identify '
        'the editorial structure of the research program; they are not mathematical '
        'implications or empirical results.</p></div>'
    )
    entries = []
    for c in data["concepts"]:
        links = "".join(
            f'<li><a href="{esc(source_link(c["id"] + "#" + s["id"]))}">{esc(s["label"])}</a></li>'
            for s in c["sections"]
        )
        entries.append(
            f'<li id="{esc(c["id"])}" class="atlas-entry">'
            f'<span class="atlas-num">{esc(c["number"])}</span>'
            '<div class="atlas-content">'
            f'<p class="category">{esc(c["role"])}</p>'
            f'<h2>{esc(c["title"])}</h2>'
            f'<p class="atlas-question">{esc(c["question"])}</p>'
            f'<p class="atlas-summary">{esc(c["summary"])}</p>'
            f'<p class="atlas-link-title">Read in the manuscript</p>'
            f'<ul class="atlas-sections">{links}</ul>'
            f'<p><a class="atlas-read" href="../essays/{esc(c["id"])}.html">Complete essay</a></p>'
            '</div></li>'
        )
    relations = []
    names = {c["id"]: c["title"] for c in data["concepts"]}
    for index, r in enumerate(data["relations"], start=1):
        evidence = " · ".join(
            f'<a href="{esc(source_link(ref))}">Source {n}</a>'
            for n, ref in enumerate(r["evidence"], start=1)
        )
        relations.append(
            f'<li id="relation-{index}" class="atlas-relation">'
            f'<p class="atlas-relation-names"><a href="#{esc(r["from"])}">{esc(names[r["from"]])}</a>'
            f' <span aria-hidden="true">→</span> <a href="#{esc(r["to"])}">{esc(names[r["to"]])}</a></p>'
            f'<p>{esc(r["label"])}</p><p class="atlas-evidence">{evidence}</p></li>'
        )
    return (
        header("Concept Atlas", "Source-anchored guide to the seven central concepts and their relationships.",
               BASE + "atlas/") +
        '<article>' + intro +
        '<section class="atlas-core" aria-labelledby="atlas-core-heading">'
        '<h2 class="atlas-section-title" id="atlas-core-heading">The seven concepts</h2>'
        '<ol class="atlas-list">' + "".join(entries) + '</ol></section>'
        '<section class="atlas-relations-section" aria-labelledby="atlas-relations-heading">'
        '<h2 class="atlas-section-title" id="atlas-relations-heading">Conceptual connections</h2>'
        '<p>Each connection is supported by passages in both essays. Follow those '
        'passages to evaluate its exact scope.</p>'
        '<ol class="atlas-relations">' + "".join(relations) + '</ol></section>'
        '</article>\n' + footer()
    )


def render_sitemap() -> str:
    """Generate the public sitemap from the same declared publication inventory."""
    paths = [""] + [f"essays/{row[0]}.html" for row in ESSAYS] + [
        "studies/commuting-square.html", "atlas/"
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
    (output / "essays").mkdir(parents=True)
    (output / "atlas").mkdir(parents=True)
    for index, row in enumerate(ESSAYS):
        slug = row[0]
        (output / "essays" / (slug + ".html")).write_text(
            render_essay(*row, position=index), encoding="utf-8")
    data = json.loads((ROOT / "atlas" / "concepts.json").read_text(encoding="utf-8"))
    validate_concepts(data)
    (output / "atlas" / "index.html").write_text(render_atlas(data), encoding="utf-8")
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
    print(f"Built {len(ESSAYS)} essays, 7 Atlas records, and one concept study into {output}")


if __name__ == "__main__":
    main()
