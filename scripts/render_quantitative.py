#!/usr/bin/env python3
"""Source-bound publication formatting for Quantitative Curry-Howard V3.

The authoritative essay fragment is immutable. Convert only exact source
notations, inventories, and record structures; unexpected changes abort the build.
All published alternatives retain the source rows, cells, and original line order.
"""
from __future__ import annotations

from html import escape, unescape
import re

from render_lambek import mathml

HEADERS = {
    1: ("ID", "Contribution", "Publication claim"),
    2: ("Reader", "Recommended path"),
    3: ("Field", "Question answered", "Failure addressed"),
    4: ("Source area", "What it contributes", "Use in this essay"),
    5: ("Domain", "Candidate artifact", "Validator", "Primary metric"),
    6: ("Metric", "Definition", "Why it matters"),
    7: ("Failure mode", "Meaning", "Diagnostic case"),
    8: ("Objection", "Best answer", "Operational test"),
    9: ("Criterion", "Decision rule"),
    10: ("Source class", "Use boundary"),
}
ROWS = (6, 5, 9, 6, 5, 6, 8, 6, 7, 6)
CAPTIONS = {
    1: "Table 1. Contributions and publication claims.",
    2: "Table 2. Recommended reading paths.",
    3: "Table 3. Evidence record fields and failure cases.",
    4: "Table 4. Scientific precedents and their evidential roles.",
    5: "Table 5. Benchmark domains, validators, and metrics.",
    6: "Table 6. Evaluation metrics and their definitions.",
    7: "Table 7. Quantitative evidence failure taxonomy.",
    8: "Table 8. Objections, responses, and operational tests.",
    9: "Table 9. Kill criteria and decision rules.",
    10: "Table 10. Source classes and evidential boundaries.",
}
SECTIONS = {
    "1": "position-in-the-compositional-intelligence-series",
    "2": "thesis-and-scope-conditions",
    "3": "classical-curry-howard-and-the-candidate-layer",
    "4": "the-quantitative-judgment",
    "5": "four-layers-of-quantitative-curry-howard",
    "5.1": "quantitative-search-over-formal-objects",
    "5.2": "soft-logical-satisfaction",
    "5.3": "probabilistic-warrant",
    "5.4": "calibrated-semantic-participation",
    "6": "quantitative-evidence-record-v0.2",
    "7": "state-of-the-art-landscape-and-source-control",
    "8": "worked-examples",
    "8.1": "lean-proof-search",
    "8.2": "differentiable-constraints",
    "8.3": "probabilistic-scientific-claim",
    "8.4": "reasoning-trace-verification",
    "8.5": "code-synthesis-with-quantitative-evidence",
    "9": "quantitative-curry-howard-bench-v0.2",
    "10": "failure-taxonomy",
    "11": "strongest-objections",
    "12": "kill-criteria",
    "13": "conclusion-and-transition-to-essay-7",
}
APPENDICES = {
    "A": "appendix-a.-quantitative_judgment-schema",
    "B": "appendix-b.-benchmark-item-schema",
    "C": "appendix-c.-source-use-warnings",
}
EXAMPLES = (
    "lean-proof-search",
    "differentiable-constraints",
    "probabilistic-scientific-claim",
    "reasoning-trace-verification",
    "code-synthesis-with-quantitative-evidence",
)
RECORDS = (
    ("appendix-a.-quantitative_judgment-schema", "quantitative_judgment:", 20),
    ("appendix-b.-benchmark-item-schema", "qch_benchmark_item:", 13),
)
SEQ = (
    "artifact membership",
    "target-type inference",
    "transformation preservation",
    "architecture specification",
    "quantitative warrant",
)
PIPELINE = (
    "infer target A",
    "construct candidate t",
    "score candidate under theta",
    "validate where available",
    "calibrate scores against outcomes",
    "repair failures using diagnostics",
    "assign epistemic type",
    "record permitted use",
)
JUDGMENTS = {
    "Gamma |- t : A": r"\Gamma\vdash t:A",
    "Gamma |-_theta t : A |> Q": r"\Gamma\vdash_{\theta}t:A\triangleright Q",
    "P_theta(tactic | proof_state)": r"P_{\theta}(\mathrm{tactic}\mid\mathrm{proof\_state})",
    "diagnostics(t, A, Gamma)": r"\operatorname{diagnostics}(t,A,\Gamma)",
}
TABLE = re.compile(
    r'(?P<start><div aria-labelledby="table-(?P<n>\d+)-caption" '
    r'class="table-scroll" data-columns="\d+" role="group" tabindex="0">)'
    r'(?P<table><table data-source-table="\d+" id="table-\d+">'
    r'[\s\S]*?</table>)(?P<end></div>)'
)
BLOCK = re.compile(r'<blockquote>\s*(?P<lines>(?:<p>[\s\S]*?</p>\s*)+)</blockquote>')
TAG = re.compile(r"<[^>]+>")
FIELD = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*:)(?: (.+))?$")


def _blocks(markup: str) -> list[str]:
    """Decode the originally separate paragraphs without dropping source text."""
    lines = re.findall(r"<p>([^<]*)</p>", markup)
    if not lines:
        raise ValueError("Expected original plain source paragraphs")
    if len(lines) != len(re.findall(r"<p>", markup)):
        raise ValueError("Nested markup in original source block")
    return [unescape(line) for line in lines]


def _code(text: str) -> str:
    """Wrap source code verbatim, with optional breaks only after underscores."""
    return "<code>" + escape(text).replace("_", "_<wbr>") + "</code>"


def captions(body: str) -> str:
    """Replace conversion-generated labels, never table contents."""
    for n, label in CAPTIONS.items():
        pattern = re.compile(
            rf'(<p class="table-display-caption" id="table-{n}-caption">)'
            r'[^<]*(</p>)'
        )
        if len(pattern.findall(body)) != 1:
            raise ValueError(f"Missing original table caption {n}")
        body = pattern.sub(
            lambda m: m.group(1) + escape(label) + m.group(2), body, count=1
        )
        native = re.compile(
            rf'(<table data-source-table="{n}" id="table-{n}">'
            r'<caption class="visually-hidden">)[^<]*(</caption>)'
        )
        if len(native.findall(body)) != 1:
            raise ValueError(f"Missing native source table caption {n}")
        body = native.sub(
            lambda m: m.group(1) + escape(label) + m.group(2), body, count=1
        )
    return body


def reader_map(body: str) -> str:
    """Navigate only existing targets, preserving the five original rows."""
    pattern = re.compile(
        r'(<table data-source-table="2" id="table-2">)'
        r'([\s\S]*?)(</table>)'
    )
    found = list(pattern.finditer(body))
    if len(found) != 1:
        raise ValueError("Reader map table missing")
    match = found[0]
    content = match.group(2)
    row = re.compile(
        r'(<tr\b[^>]*>\s*<td>[^<]*</td>\s*<td>)([^<]*)(</td>\s*</tr>)'
    )
    rows = list(row.finditer(content))
    if len(rows) != 5:
        raise ValueError("Reader map row count changed")
    for item in reversed(rows):
        raw = item.group(2)
        if "Read after Essay 5 and prior to Essay 7" in raw:
            linked = raw.replace(
                "Essay 5", '<a href="algebraic-architectures.html">Essay 5</a>', 1
            ).replace(
                "Essay 7",
                '<a href="effectful-and-conceptual-intelligence.html">Essay 7</a>',
                1,
            )
        else:
            linked = re.sub(
                r"\b\d+(?:\.\d+)?\b",
                lambda m: (
                    '<a href="#' + SECTIONS[m.group()] + '">' +
                    m.group() + '</a>'
                ) if m.group() in SECTIONS else m.group(),
                raw,
            )
            for letter, anchor in APPENDICES.items():
                linked = linked.replace(
                    "Appendix " + letter,
                    'Appendix <a href="#' + anchor + '">' + letter + '</a>',
                    1,
                )
        content = content[:item.start(2)] + linked + content[item.end(2):]
    return (
        body[:match.start()] + match.group(1) + content +
        match.group(3) + body[match.end():]
    )


def _sequence(lines: list[str]) -> str:
    if len(lines) != 1 or tuple(lines[0].split(" -> ")) != SEQ:
        raise ValueError("Five-stage series sequence changed")
    return (
        '<div class="qc-sequence" role="group" '
        'aria-label="Authored evidence dependency sequence"><ol>' +
        "".join("<li>" + escape(v) + "</li>" for v in SEQ) +
        "</ol></div>"
    )


def _formula(lines: list[str], expected: str, label: str) -> str:
    if lines != [expected]:
        raise ValueError(f"Original {label} judgment changed")
    return (
        '<div class="qc-math" role="group" aria-label="' +
        escape(label, quote=True) + '">' +
        mathml(expected, JUDGMENTS[expected]) + "</div>"
    )


def _layers(lines: list[str]) -> str:
    expected = (
        "candidate layer: Gamma |-_theta t : A |> Q",
        "validation layer: Gamma |- t : A",
        "failure layer: diagnostics(t, A, Gamma)",
    )
    if tuple(lines) != expected:
        raise ValueError("The three original evidence layers changed")
    items = []
    for line in lines:
        name, value = line.split(": ", 1)
        items.append(
            '<div class="qc-layer"><dt>' + escape(name) + "</dt><dd>" +
            mathml(value, JUDGMENTS[value]) + "</dd></div>"
        )
    return (
        '<dl class="qc-layers" aria-label="Authored candidate, validation, '
        'and failure distinctions">' + "".join(items) + "</dl>"
    )


def _tuple(lines: list[str]) -> str:
    expected = (
        "Q = (score, probability, uncertainty, margin, loss, calibration, validation_status,",
        "diagnostics, repair_distance, epistemic_type, permitted_use)",
    )
    if tuple(lines) != expected:
        raise ValueError("Quantitative evidence tuple changed")
    return (
        '<div class="qc-tuple" role="group" '
        'aria-label="Authored quantitative evidence tuple">' +
        "".join('<p>' + _code(line) + "</p>" for line in lines) +
        "</div>"
    )


def _pipeline(lines: list[str]) -> str:
    if tuple(lines) != PIPELINE:
        raise ValueError("Authored eight-stage quantitative pipeline changed")
    return (
        '<div class="qc-pipeline" role="group" '
        'aria-label="Authored evidence-processing workflow">'
        '<ol>' + "".join("<li>" + escape(v) + "</li>" for v in lines) +
        "</ol></div>"
    )


def _example(lines: list[str], name: str) -> str:
    if len(lines) not in {3, 4}:
        raise ValueError(f"Malformed worked example {name}")
    elements = []
    for line in lines:
        match = re.fullmatch(r"(Gamma|A|t|Q) = (.+)", line)
        if not match:
            raise ValueError(f"Unexpected source example field: {line}")
        key, value = match.groups()
        elements.append(
            '<div class="qc-example-field"><dt>' + escape(key) +
            "</dt><dd>" + escape(value) + "</dd></div>"
        )
    return (
        '<dl class="qc-example" aria-label="Authored example ' +
        escape(name, quote=True) + '">' +
        "".join(elements) + "</dl>"
    )


def _record(lines: list[str], name: str, count: int) -> str:
    if len(lines) != count or lines[0] != name:
        raise ValueError(f"Original source record {name} changed")
    fields = []
    for line in lines[1:]:
        match = FIELD.fullmatch(line)
        if not match:
            raise ValueError(f"Unexpected source field {line}")
        key, value = match.groups()
        fields.append(
            '<li class="qc-schema-line"><span class="qc-schema-name">' +
            _code(key) + "</span>" + (
                ' <span class="qc-schema-value">' + _code(value) + "</span>"
                if value is not None else ""
            ) + "</li>"
        )
    return (
        '<div class="qc-schema" role="group" '
        'aria-label="Source record ' + escape(name[:-1], quote=True) + '">'
        '<p class="qc-schema-heading">' + _code(lines[0]) + "</p>"
        '<ol class="qc-schema-lines">' + "".join(fields) +
        "</ol></div>"
    )


def structures(body: str) -> str:
    """Convert all fourteen original blockquotations in their exact order."""
    found = list(BLOCK.finditer(body))
    if len(found) != 14:
        raise ValueError("Original quantitative blockquote inventory changed")
    for i, match in reversed(list(enumerate(found))):
        lines = _blocks(match.group("lines"))
        if i == 0:
            replace = _sequence(lines)
        elif i == 1:
            replace = _formula(lines, "Gamma |- t : A", "Exact Curry-Howard judgment")
        elif i == 2:
            replace = _layers(lines)
        elif i == 3:
            replace = _formula(
                lines, "Gamma |-_theta t : A |> Q", "Quantitative candidate judgment"
            )
        elif i == 4:
            replace = _tuple(lines)
        elif i == 5:
            replace = _pipeline(lines)
        elif i == 6:
            replace = _formula(
                lines, "P_theta(tactic | proof_state)", "Source proof-search score"
            )
        elif i <= 11:
            anchor = EXAMPLES[i - 7]
            if f'<h3 id="{anchor}">' not in body[:match.start()]:
                raise ValueError(f"Missing original worked-example heading {anchor}")
            replace = _example(lines, anchor)
        else:
            anchor, name, count = RECORDS[i - 12]
            if f'<h2 id="{anchor}">' not in body[:match.start()]:
                raise ValueError(f"Missing original record section {anchor}")
            replace = _record(lines, name, count)
        body = body[:match.start()] + replace + body[match.end():]
    return body


def tables(body: str) -> str:
    """Preserve source HTML tables and derive exactly 64 mobile records."""
    matches = list(TABLE.finditer(body))
    if [int(m.group("n")) for m in matches] != list(range(1, 11)):
        raise ValueError("Original ten-table inventory changed")
    total = 0
    for match in reversed(matches):
        number = int(match.group("n"))
        table = match.group("table")
        head = re.search(r"<thead>([\s\S]*?)</thead>", table)
        main = re.search(r"<tbody>([\s\S]*?)</tbody>", table)
        if not head or not main:
            raise ValueError(f"Malformed quantitative source table {number}")
        headers = tuple(
            unescape(TAG.sub("", cell)).strip()
            for cell in re.findall(r"<th\b[^>]*>([\s\S]*?)</th>", head.group(1))
        )
        if headers != HEADERS[number]:
            raise ValueError(f"Unexpected source headers at table {number}")
        rows = re.findall(r"<tr\b[^>]*>([\s\S]*?)</tr>", main.group(1))
        if len(rows) != ROWS[number - 1]:
            raise ValueError(f"Unexpected source rows at table {number}")
        mobile = []
        for row in rows:
            values = re.findall(r"<td(?:\s[^>]*)?>([\s\S]*?)</td>", row)
            if len(values) != len(headers):
                raise ValueError(f"Unexpected cell inventory at table {number}")
            total += len(values)
            fields = "".join(
                '<div class="qc-field"><dt>' + escape(label) +
                "</dt><dd>" + value + "</dd></div>"
                for label, value in zip(headers, values, strict=True)
            )
            mobile.append('<dl class="qc-card">' + fields + "</dl>")
        hint = (
            f'<p class="qc-hint" id="qc-hint-{number}">'
            'Scroll horizontally to see all table columns.</p>'
        )
        opening = match.group("start").replace(
            'class="table-scroll"', 'class="table-scroll" '
            'data-qc-alternative="mobile"', 1
        )
        opening = opening[:-1] + f' aria-describedby="qc-hint-{number}">'
        alternative = (
            f'<section class="qc-mobile qc-mobile-{number}" '
            f'aria-labelledby="table-{number}-caption">' +
            "".join(mobile) + "</section>"
        )
        body = (
            body[:match.start()] + hint + opening + table +
            match.group("end") + alternative + body[match.end():]
        )
    if total != 179:
        raise ValueError("Original quantitative table data cells changed")
    return body


def render_quantitative_curry_howard(body: str) -> str:
    """Present source mathematics, records, navigation, and tables without edits."""
    for conversion in (captions, reader_map, structures, tables):
        body = conversion(body)
    if (
        body.count('data-qc-alternative="mobile"') != 10 or
        body.count('class="qc-card"') != 64 or
        body.count('class="qc-field"') != 179 or
        body.count('class="qc-example"') != 5 or
        body.count('class="qc-schema"') != 2 or
        body.count('class="qc-layer"') != 3 or
        body.count('class="qc-pipeline"') != 1
    ):
        raise ValueError("Incomplete quantitative publication transformations")
    return body
