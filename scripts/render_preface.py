#!/usr/bin/env python3
"""Source-preserving presentation and reading links for the V3 Series Preface.

Original manuscript files stay untouched. Strict source assertions prevent
automatic reflow or cross-links from drifting away from authored records.
"""

from __future__ import annotations

from html import escape, unescape
import re

_STAGES = (
    "Output", "candidate artifact", "typed candidate", "transformed artifact",
    "validated artifact", "warranted artifact", "reusable artifact", "effectful action",
)
_LIFECYCLE = re.compile(
    r'<p>The lifecycle used throughout the suite is diagnostic\. '
    r'(?P<chain>Output(?: -&gt; [a-z ]+){7})\. '
    r'(?P<continuation>The sequence exposes [^<]+)</p>'
)
_DOCUMENT_LINKS = (
    ("Main synthesis paper", "compositional-intelligence.html"),
    ("Essay 0 - Series Preface", "series-preface.html"),
    ("Essay 1 - Semantic Participation", "semantic-participation.html"),
    ("Essay 2 - Typed Generativity", "typed-generativity.html"),
    ("Essay 3 - Functorial Consistency", "functorial-consistency.html"),
    ("Essay 4 - Lambek Machines", "lambek-machines.html"),
    ("Essay 5 - Algebraic Architectures", "algebraic-architectures.html"),
    ("Essay 6 - Quantitative Curry-Howard", "quantitative-curry-howard.html"),
    ("Essay 7 - Effectful and Conceptual Intelligence", "effectful-and-conceptual-intelligence.html"),
)
# Source tables have column headings, with no authored captions.
# These are assistive-technology descriptions, not added manuscript prose.
_ACCESSIBLE_TABLE_LABELS = (
    "Table 1. Publication order, documents, and roles.",
    "Table 2. Foundational layers, questions, and canonical schemas.",
    "Table 3. Core terms and their definitions.",
    "Table 4. Claim levels, meanings, and treatment.",
    "Table 5. Mathematical notation and its interpretation.",
    "Table 6. Publication steps, actions, and gates.",
    "Table 7. Canonical schemas and associated artifacts.",
)
_MOBILE_TABLES = {
    5: (("Notation", "Reading"), "Mathematical notation and reading"),
    7: (("Layer", "Schema", "Artifact"), "Canonical schemas and artifacts"),
}
_SCROLL_HINT = "Scroll sideways to view all columns."


def _render_lifecycle(body: str) -> str:
    """Reflow the eight authored stages, keeping all original words in order."""
    found = list(_LIFECYCLE.finditer(body))
    if len(found) != 1:
        raise ValueError("Series Preface lifecycle source is missing or duplicated")
    match = found[0]
    stages = tuple(s.strip() for s in unescape(match.group("chain")).split(" -> "))
    if stages != _STAGES:
        raise ValueError("Series Preface lifecycle differs from V3 source")
    items = "".join("<li>" + escape(s) + "</li>" for s in stages)
    output = (
        "<p>The lifecycle used throughout the suite is diagnostic.</p>\n"
        '<div class="ci-lifecycle preface-lifecycle" role="group" '
        'aria-label="Original eight-stage artifact lifecycle">'
        "<ol>" + items + "</ol></div>\n"
        "<p>" + match.group("continuation") + "</p>"
    )
    return body[:match.start()] + output + body[match.end():]


def _link_publication_order(body: str) -> str:
    """Link source document titles to their existing local reading pages."""
    table = re.compile(
        r'(?P<opening><table data-source-table="1" id="table-1">)'
        r'(?P<content>[\s\S]*?)(?P<closing></table>)'
    )
    found = list(table.finditer(body))
    if len(found) != 1:
        raise ValueError("Source publication-order table has changed")
    match = found[0]
    content = match.group("content")
    for title, target in _DOCUMENT_LINKS:
        original = "<td>" + escape(title) + "</td>"
        if content.count(original) != 1:
            raise ValueError("Source reading-map title changed: " + title)
        content = content.replace(
            original, '<td><a href="' + escape(target, quote=True) + '">' +
            escape(title) + "</a></td>", 1
        )
    return (
        body[:match.start()] + match.group("opening") + content +
        match.group("closing") + body[match.end():]
    )


def _name_and_explain_tables(body: str) -> str:
    """Normalize generated labels and show overflow guidance above each table."""
    for number, label in enumerate(_ACCESSIBLE_TABLE_LABELS, 1):
        label_id = f"table-{number}-caption"
        label_pattern = re.compile(
            rf'<p class="table-display-caption" id="{label_id}">[^<]+</p>'
        )
        if len(label_pattern.findall(body)) != 1:
            raise ValueError(f"Table {number} accessible label changed")
        body = label_pattern.sub(
            lambda _: f'<p class="table-display-caption" id="{label_id}">' +
            escape(label) + "</p>", body, count=1,
        )
        native = re.compile(
            rf'(?P<start><table data-source-table="{number}" id="table-{number}">\s*'
            r'<caption class="visually-hidden">)[^<]+(?P<end></caption>)'
        )
        if len(native.findall(body)) != 1:
            raise ValueError(f"Table {number} native caption changed")
        body = native.sub(
            lambda match: match.group("start") + escape(label) +
            match.group("end"), body, count=1,
        )
        wrapper = re.compile(
            rf'<div aria-labelledby="{label_id}" class="table-scroll" '
            r'data-columns="[23]" role="group" tabindex="0">'
        )
        if len(wrapper.findall(body)) != 1:
            raise ValueError(f"Table {number} scroll container changed")
        hint = f"preface-table-{number}-scroll-hint"
        cue = (
            f'<p id="{hint}" class="table-scroll-hint preface-scroll-hint">' +
            escape(_SCROLL_HINT) + "</p>\n"
        )
        body = wrapper.sub(
            lambda match: cue + match.group()[:-1] +
            f' aria-describedby="{hint}">', body, count=1,
        )
    return body


def _mobile_scientific_records(body: str) -> str:
    """Build small-screen definitions directly from original table cells.

    Desktop retains the canonical HTML tables and native MathML. The 13
    stacked mobile records are derived from those same source cells.
    """
    for number, (headers, label) in _MOBILE_TABLES.items():
        pattern = re.compile(
            rf'(?P<wrapper><div aria-labelledby="table-{number}-caption" '
            rf'class="table-scroll" data-columns="{len(headers)}" '
            r'role="group" tabindex="0" '
            rf'aria-describedby="preface-table-{number}-scroll-hint">'
            rf'(?P<content>[\s\S]*?<table data-source-table="{number}" '
            rf'id="table-{number}">[\s\S]*?</table>)</div>)'
        )
        found = list(pattern.finditer(body))
        if len(found) != 1:
            raise ValueError(f"Table {number} source wrapper differs from V3")
        match = found[0]
        content = match.group("content")
        heading = re.search(r"<thead>([\s\S]*?)</thead>", content)
        if heading is None:
            raise ValueError(f"Missing table {number} headings")
        names = tuple(unescape(name) for name in re.findall(
            r'<th scope="col"><strong>([^<]+)</strong></th>', heading.group(1)
        ))
        if names != headers:
            raise ValueError(f"Table {number} headings differ from V3")
        tbody = re.search(r"<tbody>([\s\S]*?)</tbody>", content)
        if tbody is None:
            raise ValueError(f"Table {number} source rows missing")
        rows = re.findall(r"<tr\b[^>]*>([\s\S]*?)</tr>", tbody.group(1))
        expected = 6 if number == 5 else 7
        if len(rows) != expected:
            raise ValueError(f"Table {number} row count differs from V3")
        cards: list[str] = []
        for index, row in enumerate(rows):
            values = re.findall(r"<td>([\s\S]*?)</td>", row)
            if len(values) != len(headers):
                raise ValueError(f"Table {number} source cell count changed")
            if number == 7 and index == 4:
                # The architecture chain gets line-break-friendly presentation
                # in the mobile copy; the original MathML remains in the table.
                chain = re.compile(
                    r'<math\b[^>]*alttext="TaskSpec -&gt; ArchitectureType '
                    r'-&gt; ArchitectureInstance"[^>]*>[\s\S]*?</math>'
                )
                if len(chain.findall(values[1])) != 1:
                    raise ValueError("Architecture schema differs from V3")
                values[1] = chain.sub(
                    '<span class="preface-architecture-source">'
                    "TaskSpec → ArchitectureType → ArchitectureInstance;</span>",
                    values[1], count=1,
                )
                if "</span>; " not in values[1]:
                    raise ValueError("Architecture specification separator changed")
                values[1] = values[1].replace(
                    "</span>; ",
                    '</span><span class="preface-architecture-satisfaction">',
                    1,
                ) + "</span>"
            fields = "".join(
                '<div class="preface-record-field"><dt>' + escape(name) +
                "</dt><dd>" + value + "</dd></div>"
                for name, value in zip(headers, values, strict=True)
            )
            cards.append('<dl class="preface-mobile-record">' + fields + "</dl>")
        alternative = (
            '<section class="preface-mobile-records" aria-label="' +
            escape(label, quote=True) + '">' + "".join(cards) + "</section>"
        )
        wrapper = match.group("wrapper").replace(
            'class="table-scroll"',
            'class="table-scroll" data-preface-alternative="mobile"', 1,
        )
        body = body[:match.start()] + wrapper + alternative + body[match.end():]
        cue = re.compile(
            rf'(<p id="preface-table-{number}-scroll-hint" '
            r'class="table-scroll-hint preface-scroll-hint")'
        )
        if len(cue.findall(body)) != 1:
            raise ValueError(f"Table {number} mobile cue missing")
        body = cue.sub(r'\1 data-mobile-alternative="true"', body, count=1)
    return body


def render_preface(body: str) -> str:
    """Enhance only the preface, without changing its canonical V3 source."""
    if body.count('<table data-source-table=') != 7:
        raise ValueError("Series Preface must retain all seven source tables")
    body = _render_lifecycle(body)
    body = _link_publication_order(body)
    body = _name_and_explain_tables(body)
    body = _mobile_scientific_records(body)
    if body.count('class="table-scroll-hint preface-scroll-hint"') != 7:
        raise ValueError("Series Preface is missing table scrolling cues")
    return body
