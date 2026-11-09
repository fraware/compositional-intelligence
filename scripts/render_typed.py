#!/usr/bin/env python3
"""Faithful reading layouts for the original Typed Generativity V3 manuscript.

All source HTML tables and original manuscript paragraphs remain available.
Desktop retains every original table; narrow screens use matching definition
records derived solely from table cells. Unexpected source changes fail closed.
"""

from __future__ import annotations

from html import escape, unescape
import re


_HEADERS: dict[int, tuple[str, ...]] = {
    1: ("ID", "Contribution", "Publication claim"),
    2: ("Reader", "Recommended path"),
    3: ("Symbol", "Meaning", "Example"),
    4: ("Prompt family", "Candidate target types", "Typical target-type failure"),
    5: ("Level", "Definition", "Current status", "Main test"),
    6: ("Failure", "Meaning"),
    7: ("Candidate target type", "Validation criterion"),
    8: ("Failure", "Meaning"),
    9: ("Condition", "Instruction pattern", "Purpose"),
    10: ("Metric", "Definition", "Interpretation"),
    11: ("Record", "Core question", "Primary downstream use"),
    12: ("Source area", "What it supports", "Boundary"),
    13: ("Objection", "Response standard", "Operational test"),
    14: ("Failure", "Meaning", "Repair path"),
    15: ("Level", "Meaning", "Example"),
}
_ROW_COUNTS: dict[int, int] = {
    1: 6, 2: 5, 3: 5, 4: 5, 5: 3,
    6: 4, 7: 5, 8: 5, 9: 5, 10: 9,
    11: 3, 12: 6, 13: 7, 14: 8, 15: 5,
}
_CAPTIONS: dict[int, str] = {
    1: "Table 1. Contributions and publication claims.",
    2: "Table 2. Recommended reading paths for different audiences.",
    3: "Table 3. Generation schema symbols, meanings, and examples.",
    4: "Table 4. Prompt families, target types, and typical failures.",
    5: "Table 5. Three levels of typed generation and their tests.",
    6: "Table 6. Code generation failure categories and meanings.",
    7: "Table 7. Explanation target types and validation criteria.",
    8: "Table 8. Scientific protocol generation failure categories.",
    9: "Table 9. Type-First Prompting Harness conditions and purposes.",
    10: "Table 10. Type-First Prompting Harness metrics and interpretation.",
    11: "Table 11. Target-type and candidate-inhabitant record roles.",
    12: "Table 12. Research traditions, contributions, and boundaries.",
    13: "Table 13. Objections to Typed Generativity and response tests.",
    14: "Table 14. Typed generation failure taxonomy and repair paths.",
    15: "Table 15. Claim levels, meanings, and examples.",
}
_TABLE = re.compile(
    r'(?P<start><div aria-labelledby="table-(?P<n>\d+)-caption" '
    r'class="table-scroll" data-columns="(?P<columns>\d+)" '
    r'role="group" tabindex="0">)'
    r'(?P<contents><table data-source-table="\d+" id="table-\d+">'
    r'[\s\S]*?</table>)(?P<end></div>)'
)
_ROWS = re.compile(r"<tr\b[^>]*>([\s\S]*?)</tr>")
_CELLS = re.compile(r"<td(?:\s[^>]*)?>([\s\S]*?)</td>")
_HEADERS_HTML = re.compile(r"<th\b[^>]*>([\s\S]*?)</th>")
_TAGS = re.compile(r"<[^>]+>")
_STAGE_SEQUENCES: dict[str, tuple[str, ...]] = {
    "semantic membership": (
        "semantic membership", "target-type inference",
        "candidate inhabitant", "transformation preservation",
    ),
    "Gamma": (
        "Gamma", "infer A", "construct t : A",
        "validate/repair", "semantic participation",
    ),
}
_EXAMPLE_SHAPES: tuple[tuple[str, ...], ...] = (
    ("Prompt:", "A =", "constraints =", "t ="),
    ("Prompt:", "A =", "constraints =", "t ="),
    ("Prompt:", "A ="),
    ("Prompt:", "A =", "constraints ="),
)
_HINT = "Scroll horizontally to read every table column."


def _text(html: str) -> str:
    """Extract human-readable text from the source's inline formatting."""
    return unescape(_TAGS.sub("", html)).strip()


def _source_captions(body: str) -> str:
    """Improve only generated accessibility captions, never authored table cells."""
    for number, caption in _CAPTIONS.items():
        paragraph = re.compile(
            rf'<p class="table-display-caption" id="table-{number}-caption">'
            r'[^<]*</p>'
        )
        native = re.compile(
            rf'(?P<start><table data-source-table="{number}" id="table-{number}">'
            r'\s*<caption class="visually-hidden">)[^<]*'
            r'(?P<end></caption>)'
        )
        if len(paragraph.findall(body)) != 1 or len(native.findall(body)) != 1:
            raise ValueError(f"Source table {number} generated captions changed")
        body = paragraph.sub(
            lambda _match: (
                f'<p class="table-display-caption" id="table-{number}-caption">'
                + escape(caption) + "</p>"
            ), body, count=1,
        )
        body = native.sub(
            lambda match: (
                match.group("start") + escape(caption) + match.group("end")
            ), body, count=1,
        )
    return body


def _reader_targets(body: str) -> tuple[dict[str, str], dict[str, str]]:
    """Read the true section and appendix anchors from the current manuscript."""
    numbers: dict[str, str] = {}
    appendices: dict[str, str] = {}
    pattern = re.compile(r'<h[23] id="([^"]+)">([^<]+)</h[23]>')
    for fragment, text in pattern.findall(body):
        section = re.match(r"(\d+(?:\.\d+)?)\.?\s", text)
        if section:
            numbers[section.group(1)] = fragment
        appendix = re.match(r"Appendix ([A-Z])\.\s", text)
        if appendix:
            appendices[appendix.group(1)] = fragment
    if set(numbers) != {
        *(str(i) for i in range(1, 13)),
        "6.1", "6.2", "6.3", "6.4", "6.5", "7.1", "7.2", "7.3",
    } or set(appendices) != {"A", "B", "C"}:
        raise ValueError("Source section/appendix inventory differs from V3")
    return numbers, appendices


def _link_reading_paths(body: str) -> str:
    """Make existing headings navigable, preserving the unresolved 7.4 citation."""
    numbers, appendices = _reader_targets(body)
    table = re.compile(
        r'(?P<open><table data-source-table="2" id="table-2">)'
        r'(?P<content>[\s\S]*?)(?P<close></table>)'
    )
    found = list(table.finditer(body))
    if len(found) != 1:
        raise ValueError("Typed Generativity reading map source changed")
    match = found[0]
    rows = re.compile(
        r'(?P<before><tr\b[^>]*>\s*<td>(?P<reader>[^<]+)</td>\s*<td>)'
        r'(?P<route>[^<]+)(?P<after></td>\s*</tr>)'
    )
    content = match.group("content")
    sources = list(rows.finditer(content))
    if len(sources) != 5:
        raise ValueError("Expected five original reader paths")
    for item in reversed(sources):
        route = item.group("route")
        if item.group("reader") == "Series reader":
            if route != "Read after Essay 1 and before Essay 3":
                raise ValueError("Original sequence of neighboring essays changed")
            linked = (
                'Read after <a href="semantic-participation.html">Essay 1</a>'
                ' and before <a href="functorial-consistency.html">Essay 3</a>'
            )
        else:
            if not route.startswith("Sections "):
                raise ValueError("Original section references changed")

            def link_section(number: re.Match[str]) -> str:
                raw = number.group()
                if raw not in numbers:
                    return raw
                return '<a href="#' + escape(numbers[raw], quote=True) + '">' + raw + "</a>"

            linked = re.sub(r"\b\d+(?:\.\d+)?\b", link_section, route)
            for key, anchor in appendices.items():
                linked = linked.replace(
                    "Appendix " + key,
                    'Appendix <a href="#' + escape(anchor, quote=True) +
                    '">' + key + "</a>", 1,
                )
        content = content[:item.start("route")] + linked + content[item.end("route"):]
    if "7.4" not in content or ">7.4</a>" in content:
        raise ValueError("Unresolved authorial 7.4 reference was overwritten")
    return body[:match.start()] + match.group("open") + content + match.group("close") + body[match.end():]


_SYMBOLS: dict[str, tuple[str, str]] = {
    "Gamma": ("<mi>Γ</mi>", r"\Gamma"),
    "A": ("<mi>A</mi>", "A"),
    "t": ("<mi>t</mi>", "t"),
    "theta": ("<mi>θ</mi>", r"\theta"),
    "P_theta": ("<msub><mi>P</mi><mi>θ</mi></msub>", r"P_{\theta}"),
}


def _typeset_source_symbols(body: str) -> str:
    """Typeset five authored symbol cells with reversible source transcriptions.

    Source tokens remain in the MathML alttext attributes. LaTeX annotations
    identify the symbols for accessible mathematical rendering and inspection.
    Every source table, row, and paragraph remains unchanged.
    """
    pattern = re.compile(
        r'(?P<start><table data-source-table="3" id="table-3">)'
        r'(?P<content>[\s\S]*?)(?P<end></table>)'
    )
    found = list(pattern.finditer(body))
    if len(found) != 1:
        raise ValueError("Typed Generativity source symbol table changed")
    match = found[0]
    content = match.group("content")
    for original, (mathml, latex) in _SYMBOLS.items():
        literal = "<td>" + original + "</td>"
        if content.count(literal) != 1:
            raise ValueError(f"Missing or repeated original source symbol {original}")
        replacement = (
            '<td><math display="inline" alttext="' +
            escape(original, quote=True) +
            '"><semantics>' + mathml +
            '<annotation encoding="application/x-tex">' +
            escape(latex) + '</annotation></semantics></math></td>'
        )
        content = content.replace(literal, replacement, 1)
    return (
        body[:match.start()] + match.group("start") + content +
        match.group("end") + body[match.end():]
    )


def _render_sequences(body: str) -> str:
    """Typeset the two exact arrow-separated source sequences."""
    for first, stages in _STAGE_SEQUENCES.items():
        original = " -&gt; ".join(escape(item) for item in stages)
        pattern = "<p>" + original + "</p>"
        if body.count(pattern) != 1:
            raise ValueError("Typed Generativity authored sequence changed: " + first)
        items = "".join("<li>" + escape(stage) + "</li>" for stage in stages)
        replacement = (
            '<div class="tg-sequence" role="group" '
            'aria-label="Original typed generation sequence">'
            "<ol>" + items + "</ol></div>"
        )
        body = body.replace(pattern, replacement, 1)
    return body


def _render_examples(body: str) -> str:
    """Group the four authored domain prompts without editing any words."""
    matches = list(re.finditer(r'<p>Prompt:([\s\S]*?)</p>', body))
    if len(matches) != 4:
        raise ValueError("Expected four original domain prompt examples")
    for index, match in reversed(list(enumerate(matches))):
        lines = re.split(r'<br\s*/?>\s*', "Prompt:" + match.group(1))
        prefixes = _EXAMPLE_SHAPES[index]
        if len(lines) != len(prefixes):
            raise ValueError(f"Domain example {index + 1} row count changed")
        if any(not line.startswith(prefix) for line, prefix in zip(lines, prefixes)):
            raise ValueError(f"Domain example {index + 1} fields changed")
        inner = "".join(
            '<div class="tg-example-line">' + line + "</div>"
            for line in lines
        )
        replacement = (
            f'<div class="tg-domain-example" role="group" '
            f'aria-label="Original domain example {index + 1}">'
            + inner + "</div>"
        )
        body = body[:match.start()] + replacement + body[match.end():]
    return body


def _separate_source_records(body: str) -> str:
    """Separate the two original record definitions in Section 8."""
    record = re.compile(
        r'(?P<outer><div class="record-schema" role="group" tabindex="0" '
        r'aria-label="Source record target_type_record"><pre><code>'
        r'(?P<text>[\s\S]*?)</code></pre></div>)'
    )
    matches = list(record.finditer(body))
    if len(matches) != 1:
        raise ValueError("Original pair of Section 8 technical records changed")
    match = matches[0]
    split = "\n\ncandidate_inhabitant_record:\n"
    if match.group("text").count(split) != 1:
        raise ValueError("Original candidate inhabitant record boundary changed")
    first, second = match.group("text").split(split)
    if not first.startswith("target_type_record:\n") or not second.startswith("task_id: string\n"):
        raise ValueError("Original target/candidate record source changed")
    if first.count("\n") != 10 or second.count("\n") != 9:
        raise ValueError("Record field inventory differs from source")
    def box(label: str, content: str) -> str:
        return (
            '<div aria-label="Source record ' + escape(label, quote=True) +
            '" class="record-schema tg-source-record" role="group" tabindex="0">'
            "<pre><code>" + content + "</code></pre></div>"
        )
    separated = (
        '<div class="tg-record-pair">' +
        box("target_type_record", first) +
        box("candidate_inhabitant_record",
            "candidate_inhabitant_record:\n" + second) +
        "</div>"
    )
    return body[:match.start()] + separated + body[match.end():]


def _mobile_tables(body: str) -> str:
    """Derive exactly 81 mobile rows and 227 fields from 15 original tables."""
    matches = list(_TABLE.finditer(body))
    if [int(m.group("n")) for m in matches] != list(range(1, 16)):
        raise ValueError("Typed Generativity original source table inventory changed")
    for match in reversed(matches):
        number = int(match.group("n"))
        content = match.group("contents")
        thead = re.search(r"<thead>([\s\S]*?)</thead>", content)
        tbody = re.search(r"<tbody>([\s\S]*?)</tbody>", content)
        if not thead or not tbody:
            raise ValueError(f"Source table {number} missing structural sections")
        headers = tuple(_text(s) for s in _HEADERS_HTML.findall(thead.group(1)))
        if headers != _HEADERS[number] or len(headers) != int(match.group("columns")):
            raise ValueError(f"Source table {number} headers differ from V3: {headers}")
        rows = _ROWS.findall(tbody.group(1))
        if len(rows) != _ROW_COUNTS[number]:
            raise ValueError(f"Source table {number} row count differs from V3")
        cards: list[str] = []
        for row in rows:
            values = _CELLS.findall(row)
            if len(values) != len(headers):
                raise ValueError(f"Source table {number} cell count differs from header")
            fields = "".join(
                '<div class="tg-record-field"><dt>' + escape(header) +
                '</dt><dd>' + value + '</dd></div>'
                for header, value in zip(headers, values, strict=True)
            )
            cards.append('<dl class="tg-mobile-record">' + fields + '</dl>')
        wrapper = match.group("start").replace(
            'class="table-scroll"',
            'class="table-scroll" data-tg-alternative="mobile"', 1,
        )
        wrapper = wrapper[:-1] + f' aria-describedby="tg-table-{number}-hint">'
        hint = (
            f'<p id="tg-table-{number}-hint" class="tg-scroll-hint">'
            + escape(_HINT) + "</p>"
        )
        alt = (
            f'<section class="tg-mobile-records tg-mobile-table-{number}" '
            f'aria-labelledby="table-{number}-caption">'
            + "".join(cards) + "</section>"
        )
        body = (
            body[:match.start()] + hint + wrapper +
            content + match.group("end") + alt + body[match.end():]
        )
    if body.count('data-tg-alternative="mobile"') != 15:
        raise ValueError("Source-derived mobile table count differs from V3")
    if body.count('<dl class="tg-mobile-record">') != 81:
        raise ValueError("Source-derived mobile row count differs from V3")
    if body.count('class="tg-record-field"') != 227:
        raise ValueError("Source-derived mobile cell count differs from V3")
    return body



_SCHEMA_FIELDS: dict[str, tuple[str, ...]] = {
    "type_first_item": (
        "task_id", "domain", "prompt", "intended_target_type",
        "candidate_target_types", "constraints", "invalid_target_type_examples",
        "valid_inhabitant_criteria", "checker_or_validator",
        "human_review_fields", "ambiguity_status",
        "semantic_participation_target",
    ),
    "target_type_record": (
        "task_id", "context_summary", "candidate_target_types",
        "selected_target_type", "selection_rationale", "constraints",
        "invalid_target_examples", "validator_or_review_method",
        "ambiguity_status", "downstream_environment",
    ),
    "candidate_inhabitant_record": (
        "task_id", "selected_target_type", "candidate",
        "validation_status", "validator", "alignment_status",
        "repair_trace", "epistemic_type", "permitted_use",
        "transformation_tests",
    ),
    "typed_generativity_benchmark_item": (
        "id", "domain", "prompt", "intended_target_type",
        "candidate_target_types", "constraints", "invalid_target_examples",
        "valid_inhabitant_criteria", "validator",
        "semantic_participation_target", "transformation_tests",
        "reviewer_guidelines", "failure_labels",
    ),
}


def _format_source_schemas(body: str) -> str:
    """Typeset each exact source record as a field/type definition list.

    Keep the original source text in the manuscript. Re-render only four
    source-bound declarations, rejecting unexpected field names and counts.
    """
    pattern = re.compile(
        r'<div [^>]*class="record-schema(?: tg-source-record)?"[^>]*>'
        r'<pre><code>(?P<source>[\s\S]*?)</code></pre></div>'
    )
    matches = list(pattern.finditer(body))
    if len(matches) != len(_SCHEMA_FIELDS):
        raise ValueError(
            f"Typed Generativity record inventory changed: {len(matches)}"
        )
    recovered: set[str] = set()
    for match in reversed(matches):
        lines = match.group("source").split("\n")
        heading = lines[0]
        if not heading.endswith(":"):
            raise ValueError("Source record declaration is missing its name")
        key = heading[:-1]
        if key not in _SCHEMA_FIELDS or key in recovered:
            raise ValueError(f"Unknown or repeated typed source record: {key}")
        recovered.add(key)
        fields: list[str] = []
        observed: list[str] = []
        for line in lines[1:]:
            label, separator, value = line.partition(": ")
            if not separator or not label or not value:
                raise ValueError(f"Malformed field in source record {key}: {line}")
            observed.append(label)
            fields.append(
                '<div class="tg-schema-field"><dt><code>' +
                escape(unescape(label + ":")) + '</code></dt><dd><code>' +
                escape(unescape(value)) + '</code></dd></div>'
            )
        if tuple(observed) != _SCHEMA_FIELDS[key]:
            raise ValueError(
                f"Fields in source record {key} differ from V3 source"
            )
        replacement = (
            '<div class="tg-type-schema" role="group" '
            'aria-label="Source record ' + escape(key, quote=True) + '">'
            '<div class="tg-schema-title"><code>' + escape(heading) +
            '</code></div><dl class="tg-schema-fields">' +
            ''.join(fields) + '</dl></div>'
        )
        body = body[:match.start()] + replacement + body[match.end():]
    if recovered != set(_SCHEMA_FIELDS):
        raise ValueError("Typed Generativity record definitions are incomplete")
    return body


def render_typed_generativity(body: str) -> str:
    """Render the V3 Typed Generativity text without modifying its manuscript."""
    body = _source_captions(body)
    body = _link_reading_paths(body)
    body = _typeset_source_symbols(body)
    body = _render_sequences(body)
    body = _render_examples(body)
    body = _separate_source_records(body)
    body = _format_source_schemas(body)
    body = _mobile_tables(body)
    return body
