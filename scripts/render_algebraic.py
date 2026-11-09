#!/usr/bin/env python3
"""Source-checked presentation for Algebraic Architectures V3.

The canonical document is immutable. This renderer verifies the exact table
inventory and structured source passages before applying publication layouts.
No task content, benchmark value, or record field is synthesized.
"""
from __future__ import annotations

from html import escape, unescape
import re

from render_lambek import mathml

HEADERS = {
    1: ("ID", "Contribution", "Publication claim"),
    2: ("Reader", "Recommended path"),
    3: ("Regime", "Meaning", "Required evidence"),
    4: ("Risk", "Diagnostic case", "Audit question"),
    5: ("Area", "Structural lesson", "ArchitectureSpec implication"),
    6: ("Field", "Purpose"),
    7: ("Step", "Action", "Output"),
    8: ("Pilot family", "Core validator", "Failure signal"),
    9: ("Objection", "Answer"),
    10: ("Failure mode", "Meaning", "Required response"),
    11: ("Criterion", "Decision rule"),
    12: ("Source anchor", "Use in Essay 5"),
    13: ("Area", "Revision"),
}
ROWS = (6, 5, 5, 6, 8, 10, 7, 6, 7, 7, 9, 9, 8)
CAPTIONS = {
    1: "Table 1. Contributions and publication claims.",
    2: "Table 2. Recommended reading paths.",
    3: "Table 3. Architecture satisfaction regimes and evidence.",
    4: "Table 4. Structural risks and diagnostic questions.",
    5: "Table 5. Architectural precedents and structural lessons.",
    6: "Table 6. Architecture Specification Catalog fields.",
    7: "Table 7. Architecture comparison protocol.",
    8: "Table 8. Pilot tasks and validation signals.",
    9: "Table 9. Objections and responses.",
    10: "Table 10. Failure modes and required responses.",
    11: "Table 11. Kill criteria and decision rules.",
    12: "Table 12. Scientific source anchors and their roles.",
    13: "Table 13. Editorial changes from v0.2 to v0.3.",
}
SECTION_IDS = {
    "1": "position-in-the-compositional-intelligence-series",
    "2": "thesis-and-boundary-conditions",
    "3": "formal-core.-architecture-as-satisfaction-of-structure",
    "4": "architecturespec-v0.3",
    "5": "underbias-overbias-and-cost-structure",
    "6": "state-of-the-art-landscape-and-source-use",
    "7": "worked-examples",
    "7.1": "sets",
    "7.2": "molecules-and-3d-atomistic-systems",
    "7.3": "long-context-sequence-modeling",
    "7.4": "graph-structured-scientific-systems",
    "7.5": "algorithms-and-proof-states",
    "7.6": "scientific-protocols-and-effectful-architectures",
    "8": "architecture-specification-catalog-v0.3",
    "9": "architecture-comparison-protocol",
    "10": "benchmark-obligations",
    "11": "strongest-objections",
    "12": "failure-modes-and-kill-criteria",
    "13": "relationship-to-essay-6.-quantitative-curry-howard",
    "14": "conclusion",
}
APPENDIX_IDS = {
    "A": "appendix-a.-architecturespec-record",
    "B": "appendix-b.-architecture-mismatch-report",
    "C": "appendix-c.-catalog-item-example",
    "D": "appendix-d.-source-map-and-verification-queue",
    "E": "appendix-e.-editorial-changes-from-v0.2-to-v0.3",
}
EXAMPLE_IDS = (
    "sets",
    "molecules-and-3d-atomistic-systems",
    "long-context-sequence-modeling",
    "graph-structured-scientific-systems",
    "algorithms-and-proof-states",
    "scientific-protocols-and-effectful-architectures",
)
RECORDS = (
    ("architecture_spec:", 27, "appendix-a.-architecturespec-record"),
    ("architecture_mismatch_report:", 25,
     "appendix-b.-architecture-mismatch-report"),
    ("catalog_item:", 22, "appendix-c.-catalog-item-example"),
)
TABLE = re.compile(
    r'(?P<start><div aria-labelledby="table-(?P<n>\d+)-caption" '
    r'class="table-scroll" data-columns="\d+" role="group" tabindex="0">)'
    r'(?P<table><table data-source-table="\d+" id="table-\d+">'
    r'[\s\S]*?</table>)(?P<end></div>)'
)
BLOCK = re.compile(r'<blockquote>\s*<p>(?P<lines>[\s\S]*?)</p>\s*</blockquote>')
TAG = re.compile(r"<[^>]+>")
FIELD = re.compile(r"^([A-Za-z][\w.-]*:)(?: (.*))?$")


def clean_captions(body: str) -> str:
    """Repair conversion-only labels; reject an unexpected source inventory."""
    for n, caption in CAPTIONS.items():
        visible = re.compile(
            rf'(<p class="table-display-caption" id="table-{n}-caption">)'
            r'[^<]*(</p>)'
        )
        matches = list(visible.finditer(body))
        if len(matches) != 1:
            raise ValueError(f"Algebraic table {n} visible caption changed")
        source_caption = matches[0].group()
        if n == 11 and (
            len(source_caption) < 700 or
            "Table 10. Failure mode" not in source_caption
        ):
            raise ValueError("Unexpected original Table 11 caption anomaly")
        body = visible.sub(
            lambda m: m.group(1) + escape(caption) + m.group(2), body, count=1
        )
        native = re.compile(
            rf'(<table data-source-table="{n}" id="table-{n}">'
            r'<caption class="visually-hidden">)[^<]*(</caption>)'
        )
        if len(native.findall(body)) != 1:
            raise ValueError(f"Algebraic table {n} native caption changed")
        body = native.sub(
            lambda m: m.group(1) + escape(caption) + m.group(2), body, count=1
        )
    return body


def link_reader_map(body: str) -> str:
    """Link actual heading targets, preserving the nonexistent authored 6.1."""
    pattern = re.compile(
        r'(<table data-source-table="2" id="table-2">)'
        r'([\s\S]*?)(</table>)'
    )
    matches = list(pattern.finditer(body))
    if len(matches) != 1:
        raise ValueError("Algebraic reader map missing")
    match = matches[0]
    rows = re.compile(
        r'(<tr\b[^>]*>\s*<td>[^<]*</td>\s*<td>)([^<]*)(</td>\s*</tr>)'
    )
    content = match.group(2)
    row_matches = list(rows.finditer(content))
    if len(row_matches) != 5:
        raise ValueError("Algebraic reader map row inventory changed")
    for row in reversed(row_matches):
        text = row.group(2)
        if "Read after Essay 4 and before Essay 6" in text:
            linked = text.replace(
                "Essay 4", '<a href="lambek-machines.html">Essay 4</a>', 1
            ).replace(
                "Essay 6", '<a href="quantitative-curry-howard.html">Essay 6</a>', 1
            )
        else:
            linked = re.sub(
                r'\b\d+(?:\.\d+)?\b',
                lambda m: (
                    '<a href="#' + SECTION_IDS[m.group()] + '">' +
                    m.group() + '</a>'
                ) if m.group() in SECTION_IDS else m.group(),
                text
            )
            for letter, target in APPENDIX_IDS.items():
                linked = linked.replace(
                    "Appendix " + letter,
                    'Appendix <a href="#' + target + '">' + letter + '</a>',
                    1
                )
        content = content[:row.start(2)] + linked + content[row.end(2):]
    if "6.1" not in content or ">6.1</a>" in content:
        raise ValueError("Unsupported source Section 6.1 must remain unlinked")
    return (
        body[:match.start()] + match.group(1) + content +
        match.group(3) + body[match.end():]
    )


def _lines(markup: str) -> list[str]:
    if re.search(r"<(?!br\s*/?>)", markup, re.I):
        raise ValueError("Unexpected markup inside a source block quotation")
    return [unescape(part) for part in re.split(r"<br\s*/?>", markup)]


def _source_code(text: str) -> str:
    return "<code>" + escape(text).replace("_", "_<wbr>") + "</code>"


def _stages(lines: list[str], expected: tuple[str, ...], label: str) -> str:
    if len(lines) != 1 or tuple(lines[0].split(" -> ")) != expected:
        raise ValueError(f"Authored composition stages changed in {label}")
    return (
        '<div class="aa-sequence" role="group" aria-label="' +
        escape(label, quote=True) + '"><ol>' +
        "".join("<li>" + escape(stage) + "</li>" for stage in expected) +
        "</ol></div>"
    )


def _specification(lines: list[str]) -> str:
    if len(lines) != 10 or lines[0] != (
        "ArchitectureSpec = (O, T, Sigma, L, G, R, Phi, E, V)"
    ):
        raise ValueError("Source ArchitectureSpec tuple changed")
    symbols = ("O", "T", "Sigma", "L", "G", "R", "Phi", "E", "V")
    items = []
    for symbol, original in zip(symbols, lines[1:], strict=True):
        if not original.startswith(symbol + " "):
            raise ValueError(f"Source ArchitectureSpec {symbol} changed")
        details = original[len(symbol) + 1:]
        items.append(
            '<div class="aa-spec-field"><dt>' + escape(symbol) + '</dt>'
            '<dd>' + escape(details) + "</dd></div>"
        )
    formula = mathml(
        lines[0],
        r"\operatorname{ArchitectureSpec}=(O,T,\Sigma,L,G,R,\Phi,E,V)"
    )
    return (
        '<section class="aa-specification" role="group" '
        'aria-label="Authored ArchitectureSpec tuple and fields">'
        '<div class="aa-spec-formula">' + formula + "</div>"
        '<dl>' + "".join(items) + "</dl></section>"
    )


def _example(lines: list[str], identifier: str) -> str:
    if len(lines) not in {3, 4}:
        raise ValueError(f"Unexpected worked example source length: {identifier}")
    fields = []
    for original in lines:
        match = re.fullmatch(r"([^:]+): (.+)", original)
        if match is None:
            raise ValueError(f"Unexpected worked example field in {identifier}")
        name, value = match.groups()
        fields.append(
            '<div class="aa-example-field"><dt>' + escape(name) + '</dt>'
            '<dd>' + escape(value) + "</dd></div>"
        )
    return (
        '<dl class="aa-example" aria-label="Authored worked example ' +
        escape(identifier, quote=True) + '">' +
        "".join(fields) + "</dl>"
    )


def _record(lines: list[str], expected: tuple[str, int, str]) -> str:
    heading, count, anchor = expected
    if len(lines) != count or lines[0] != heading:
        raise ValueError(f"Unexpected appendix record lines in {anchor}")
    items = []
    for line in lines[1:]:
        kind = "bullet" if line.startswith("- ") else "field"
        field = FIELD.fullmatch(line) if kind == "field" else None
        if kind == "field" and field is None:
            raise ValueError(f"Invalid source record line in {anchor}: {line}")
        if field is not None:
            name, value = field.groups()
            content = '<span class="aa-record-name">' + _source_code(name) + "</span>"
            if value is not None:
                content += (
                    ' <span class="aa-record-value">' + _source_code(value) +
                    "</span>"
                )
        else:
            content = _source_code(line)
        items.append(
            '<li class="aa-record-line aa-record-' + kind + '">' +
            content + "</li>"
        )
    return (
        '<div class="aa-record" role="group" aria-label="Source record ' +
        escape(heading[:-1], quote=True) + '">'
        '<p class="aa-record-title">' + _source_code(heading) + "</p>"
        '<ol class="aa-record-lines">' + "".join(items) +
        "</ol></div>"
    )


def render_structures(body: str) -> str:
    """Recognize and typeset all twelve source blockquote structures."""
    matches = list(BLOCK.finditer(body))
    if len(matches) != 12:
        raise ValueError("Expected exactly twelve Algebraic source structures")
    chain_one = (
        "artifact membership", "target-type inference",
        "transformation preservation", "language structure",
        "architecture specification"
    )
    chain_two = (
        "TaskSpec", "ArchitectureType", "ArchitectureInstance"
    )
    for i, match in reversed(list(enumerate(matches))):
        lines = _lines(match.group("lines"))
        if i == 0:
            replacement = _stages(lines, chain_one, "Series composition sequence")
        elif i == 1:
            replacement = _stages(lines, chain_two, "Architecture design sequence")
        elif i == 2:
            replacement = _specification(lines)
        elif 3 <= i <= 8:
            identifier = EXAMPLE_IDS[i - 3]
            if f'<h3 id="{identifier}">' not in body[:match.start()]:
                raise ValueError(f"Missing source worked-example heading: {identifier}")
            replacement = _example(lines, identifier)
        else:
            expected = RECORDS[i - 9]
            if f'<h2 id="{expected[2]}">' not in body[:match.start()]:
                raise ValueError(f"Missing source record heading: {expected[2]}")
            replacement = _record(lines, expected)
        body = body[:match.start()] + replacement + body[match.end():]
    return body


def render_tables(body: str) -> str:
    """Produce responsive records directly from all 231 source data cells."""
    matches = list(TABLE.finditer(body))
    if [int(m.group("n")) for m in matches] != list(range(1, 14)):
        raise ValueError("Algebraic thirteen-table inventory changed")
    cells_seen = 0
    for match in reversed(matches):
        n = int(match.group("n"))
        source_table = match.group("table")
        thead = re.search(r"<thead>([\s\S]*?)</thead>", source_table)
        tbody = re.search(r"<tbody>([\s\S]*?)</tbody>", source_table)
        if not thead or not tbody:
            raise ValueError(f"Malformed source table {n}")
        headings = tuple(
            unescape(TAG.sub("",part)).strip()
            for part in re.findall(r"<th\b[^>]*>([\s\S]*?)</th>",thead.group(1))
        )
        if headings != HEADERS[n]:
            raise ValueError(f"Unexpected original headings for table {n}")
        rows = re.findall(r"<tr\b[^>]*>([\s\S]*?)</tr>",tbody.group(1))
        if len(rows) != ROWS[n - 1]:
            raise ValueError(f"Unexpected original row count for table {n}")
        cards = []
        for row in rows:
            values = re.findall(r"<td(?:\s[^>]*)?>([\s\S]*?)</td>",row)
            if len(values) != len(headings):
                raise ValueError(f"Malformed source row in table {n}")
            cells_seen += len(values)
            fields = "".join(
                '<div class="aa-field"><dt>' + escape(label) +
                "</dt><dd>" + value + "</dd></div>"
                for label,value in zip(headings,values,strict=True)
            )
            cards.append('<dl class="aa-card">' + fields + "</dl>")
        hint = (
            f'<p class="aa-hint" id="aa-hint-{n}">'
            'Scroll horizontally to see all table columns.</p>'
        )
        start = match.group("start").replace(
            'class="table-scroll"',
            'class="table-scroll" data-aa-alternative="mobile"',
            1
        )
        start = start[:-1] + f' aria-describedby="aa-hint-{n}">'
        mobile = (
            f'<section class="aa-mobile aa-mobile-{n}" '
            f'aria-labelledby="table-{n}-caption">' +
            "".join(cards) + "</section>"
        )
        body = (
            body[:match.start()] + hint + start + source_table +
            match.group("end") + mobile + body[match.end():]
        )
    if cells_seen != 231:
        raise ValueError("Algebraic original data-cell inventory changed")
    return body


def render_algebraic_architectures(body: str) -> str:
    """Apply only the auditable transformations licensed by the source."""
    for conversion in (
        clean_captions, link_reader_map, render_structures, render_tables
    ):
        body = conversion(body)
    if (
        body.count('data-aa-alternative="mobile"') != 13 or
        body.count('class="aa-card"') != 93 or
        body.count('class="aa-field"') != 231 or
        body.count('class="aa-spec-field"') != 9 or
        body.count('class="aa-example"') != 6 or
        body.count('class="aa-record"') != 3
    ):
        raise ValueError("Incomplete Algebraic source-derived publication")
    return body
