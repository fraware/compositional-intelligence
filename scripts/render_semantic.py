#!/usr/bin/env python3
"""Source-bound rendering of the original Semantic Participation V3 manuscript.

The canonical manuscript and all twelve HTML source tables remain unchanged.
This module adds mobile presentations, semantic record formatting, and a
readable sequence, with strict assertions for source tables and field counts.
"""

from __future__ import annotations

from html import escape, unescape
import re

_HEADERS: dict[int, tuple[str, ...]] = {
    1: ("ID", "Contribution", "Publication claim"),
    2: ("Reader", "Recommended path"),
    3: ("Governing claim",),
    4: ("Domain", "Local success", "Membership condition"),
    5: ("Threshold", "What it establishes", "Membership question"),
    6: ("Epistemic type", "Meaning", "Permitted use"),
    7: ("Dimension", "Diagnostic question"),
    8: ("Status", "Required record"),
    9: ("Track", "Input", "Primary metric", "Diagnostic value"),
    10: ("Objection", "Response protocol"),
    11: ("Failure mode", "Meaning"),
    12: ("Claim", "Level", "Treatment"),
}
_ROW_COUNTS = {
    1: 6, 2: 5, 3: 1, 4: 5, 5: 7, 6: 14,
    7: 8, 8: 4, 9: 5, 10: 7, 11: 7, 12: 6,
}
_SEQUENCE = (
    "membership", "generation", "transformation", "language",
    "architecture", "warrant", "action",
)
_TABLE = re.compile(
    r'(?P<start><div aria-labelledby="table-(?P<number>\d+)-caption" '
    r'class="table-scroll" data-columns="(?P<columns>\d+)" '
    r'role="group" tabindex="0">)'
    r'(?P<contents><table data-source-table="\d+" id="table-\d+">'
    r'[\s\S]*?</table>)(?P<end></div>)'
)
_ROW = re.compile(r'<tr\b[^>]*>([\s\S]*?)</tr>')
_CELL = re.compile(r'<td(?P<attrs>[^>]*)>(?P<inner>[\s\S]*?)</td>')
_TH = re.compile(r'<th\b[^>]*>([\s\S]*?)</th>')
_BLOCK = re.compile(r'<blockquote>\s*<p>(?P<content>[\s\S]*?)</p>\s*</blockquote>')
_BR = re.compile(r'<br\s*/?>', re.I)
_TAG = re.compile(r'<[^>]+>')
_SCHEMA_STARTS = {
    "SemanticEnvironment E = {": "SemanticEnvironment definition",
    "ArtifactRecord a = {": "ArtifactRecord definition",
    "semantic_participation_item:": "Semantic Participation benchmark item",
}
_HINT_TEXT = "Scroll horizontally to see all table columns."


def _plain(html: str) -> str:
    """Recover the rendered source text while ignoring formatting markup."""
    return unescape(_TAG.sub("", html)).strip()


def _record(headers: tuple[str, ...], values: list[str], *, number: int,
            special: str = "") -> str:
    """Present one source row with unchanged HTML cell contents."""
    if len(headers) != len(values):
        raise ValueError(f"Table {number} mobile field count differs from source")
    fields = "".join(
        '<div class="sp-record-field"><dt>' + escape(header) +
        "</dt><dd>" + value + "</dd></div>"
        for header, value in zip(headers, values, strict=True)
    )
    return (f'<dl class="sp-mobile-record sp-mobile-record-{number}{special}">'
            + fields + "</dl>")


def _render_epistemic_type_table(rows: list[str]) -> str:
    """Retain the type/control division encoded by the original merged cells."""
    items: list[str] = []
    for i, row in enumerate(rows):
        cells = list(_CELL.finditer(row))
        if i < 9:
            if (len(cells) != 3 or
                [m.group("attrs").strip() for m in cells] !=
                    ["", 'colspan="2"', ""]):
                raise ValueError(f"Epistemic type row {i + 1} differs from V3")
            items.append(_record(
                ("Epistemic type", "Meaning", "Permitted use"),
                [c.group("inner") for c in cells], number=6,
            ))
        elif i == 9:
            if (len(cells) != 2 or
                [c.group("attrs").strip() for c in cells] !=
                    ['colspan="2"', 'colspan="2"'] or
                [_plain(c.group("inner")) for c in cells] !=
                    ["Type transition", "Required control"]):
                raise ValueError("Epistemic transition section differs from V3")
            items.append(
                '<div class="sp-transition-head">'
                + '<span>' + cells[0].group("inner") + "</span>"
                + '<span>' + cells[1].group("inner") + "</span></div>"
            )
        else:
            if (len(cells) != 2 or
                [c.group("attrs").strip() for c in cells] !=
                    ['colspan="2"', 'colspan="2"']):
                raise ValueError(f"Epistemic transition row {i + 1} differs from V3")
            items.append(_record(
                ("Type transition", "Required control"),
                [c.group("inner") for c in cells], number=6,
                special=" sp-transition-record",
            ))
    return "".join(items)


_LOCAL_SECTIONS: dict[str, str] = {
    "1": "position-in-the-compositional-intelligence-series",
    "2": "governing-claim",
    "3": "from-output-quality-to-semantic-membership",
    "4": "the-seven-thresholds",
    "5": "formal-core",
    "6": "lean-as-operational-exemplar",
    "7": "epistemic-types",
    "8": "library-improvement-delta",
    "9": "worked-case-studies",
    "10": "semantic-participation-bench-v0.3",
    "11": "relationship-to-functorial-consistency",
    "12": "strongest-objections-and-response-protocol",
    "13": "failure-modes-and-kill-criteria",
    "14": "conclusion",
}
_LOCAL_APPENDICES = {
    "A": "appendix-a.-minimal-artifactrecord-schema",
    "B": "appendix-b.-minimal-transportrecord-schema",
    "C": "appendix-c.-claim-ledger",
    "D": "appendix-d.-source-use-notes",
}


def _link_reader_map(body: str) -> str:
    """Link original references only where a matching heading exists.

    The V3 source mentions Section 6.1, absent from its section hierarchy.
    Preserve this authored reference as text, not a misleading hyperlink.
    """
    table = re.compile(
        r'(?P<start><table data-source-table="2" id="table-2">)'
        r'(?P<content>[\s\S]*?)(?P<end></table>)'
    )
    found_tables = list(table.finditer(body))
    if len(found_tables) != 1:
        raise ValueError("Original Semantic Participation reader map changed")
    match = found_tables[0]
    content = match.group("content")
    rows = re.compile(
        r'(?P<lead><tr\b[^>]*>\s*<td>(?P<reader>[^<]+)</td>\s*<td>)'
        r'(?P<route>[^<]+)(?P<tail></td>\s*</tr>)'
    )
    found_rows = list(rows.finditer(content))
    if len(found_rows) != 5:
        raise ValueError("Reader map must retain five original pathways")
    for row in reversed(found_rows):
        original = row.group("route")
        reader = row.group("reader")
        if reader == "Series reader":
            if "Section 8" not in original:
                raise ValueError("Series reader Section 8 target changed")
            revised = original.replace(
                "Section 8",
                'Section <a href="#library-improvement-delta">8</a>', 1,
            )
        else:
            if not original.startswith("Sections "):
                raise ValueError("Reader map has unexpected path format")

            def link_number(number: re.Match[str]) -> str:
                fragment = _LOCAL_SECTIONS.get(number.group())
                if fragment is None:
                    return number.group()
                return '<a href="#' + escape(fragment, quote=True) + '">' + number.group() + '</a>'

            revised = re.sub(r'\b\d+(?:\.\d+)?\b', link_number, original)
            for key, fragment in _LOCAL_APPENDICES.items():
                revised = revised.replace(
                    "Appendix " + key,
                    'Appendix <a href="#' + escape(fragment, quote=True) +
                    '">' + key + '</a>', 1,
                )
        content = content[:row.start("route")] + revised + content[row.end("route"):]
    if content.count('<a href="#') != 22 or "6.1" not in content:
        raise ValueError("Reader pathways differ from manuscript sections")
    return (
        body[:match.start()] + match.group("start") + content +
        match.group("end") + body[match.end():]
    )


def _mobile_tables(body: str) -> str:
    """Produce twelve accessible, source-derived table views."""
    matches = list(_TABLE.finditer(body))
    if len(matches) != len(_HEADERS):
        raise ValueError(f"Semantic Participation has {len(matches)} tables, expected 12")
    table_numbers = [int(m.group("number")) for m in matches]
    if table_numbers != list(range(1, 13)):
        raise ValueError("Semantic Participation table order differs from V3")
    for m in reversed(matches):
        number = int(m.group("number"))
        content = m.group("contents")
        names = tuple(_plain(x) for x in _TH.findall(
            re.search(r'<thead>([\s\S]*?)</thead>', content).group(1)
        ))
        if names != _HEADERS[number]:
            raise ValueError(f"Table {number} headers differ from V3: {names}")
        raw_body = re.search(r'<tbody>([\s\S]*?)</tbody>', content)
        if raw_body is None:
            raise ValueError(f"Table {number} is missing original body")
        rows = _ROW.findall(raw_body.group(1))
        if len(rows) != _ROW_COUNTS[number]:
            raise ValueError(f"Table {number} source row count changed")
        if number == 6:
            cards = _render_epistemic_type_table(rows)
        else:
            cards = "".join(
                _record(_HEADERS[number], [c.group("inner") for c in _CELL.finditer(row)],
                        number=number)
                for row in rows
            )
        original_wrapper = m.group("start").replace(
            'class="table-scroll"',
            'class="table-scroll" data-sp-alternative="mobile"', 1,
        )
        original_wrapper = original_wrapper[:-1] + (
            f' aria-describedby="sp-table-{number}-hint">'
        )
        hint = (
            f'<p id="sp-table-{number}-hint" class="sp-scroll-hint">'
            + escape(_HINT_TEXT) + '</p>'
        )
        alternative = (
            f'<section class="sp-mobile-records sp-mobile-table-{number}" '
            f'aria-labelledby="table-{number}-caption">'
            + cards + '</section>'
        )
        # Source table survives intact for desktop, assistive table navigation,
        # and independent source-cell comparison.
        replacement = (
            hint + original_wrapper + content + m.group("end") + alternative
        )
        body = body[:m.start()] + replacement + body[m.end():]
    return body


def _render_sequence(body: str) -> str:
    """Typeset the author's seven-stage sequence without inventing a caption."""
    found = [
        m for m in _BLOCK.finditer(body)
        if _plain(m.group("content")).startswith("membership -> generation ->")
    ]
    if len(found) != 1:
        raise ValueError("Source membership-to-action sequence changed")
    match = found[0]
    parts = tuple(s.strip() for s in _plain(match.group("content")).split("->"))
    if parts != _SEQUENCE:
        raise ValueError("Sequence stages differ from author manuscript")
    items = "".join("<li>" + escape(s) + "</li>" for s in parts)
    replacement = (
        '<div class="sp-sequence" role="group" '
        'aria-label="Original membership-to-action sequence">'
        '<ol>' + items + "</ol></div>"
    )
    return body[:match.start()] + replacement + body[match.end():]


def _source_schema(text_html: str, label: str) -> str:
    """Render source records with authored line breaks and exact field text."""
    if re.search(r'<(?!br\s*/?>)', text_html, re.I):
        raise ValueError(f"Unexpected HTML inside source schema {label}")
    lines = [
        unescape(x).strip()
        for x in _BR.split(text_html)
    ]
    if len(lines) < 10:
        raise ValueError(f"Source schema {label} is missing fields")
    return (
        '<div class="sp-source-schema" role="group" tabindex="0" '
        'aria-label="' + escape(label, quote=True) + '">'
        '<pre><code>' + escape("\n".join(lines)) +
        "</code></pre></div>"
    )


def _render_schemas(body: str) -> str:
    """Distinguish authored technical definitions from explanatory quotations."""
    count = 0
    def transform(match: re.Match[str]) -> str:
        nonlocal count
        source = match.group("content")
        first = unescape(_BR.split(source)[0]).strip()
        label = _SCHEMA_STARTS.get(first)
        if label is None:
            return match.group()
        count += 1
        return _source_schema(source, label)
    body = _BLOCK.sub(transform, body)
    if count != len(_SCHEMA_STARTS):
        raise ValueError(f"Expected three source technical schemas; got {count}")
    return body


def _render_membership_criterion(body: str) -> str:
    """Keep the author's conjunctions distinct without rewriting the criterion."""
    found = [
        m for m in _BLOCK.finditer(body)
        if 'alttext="Member_E(a)"' in m.group("content") and
        "ValidOrReviewable_E(a)" in m.group("content")
    ]
    if len(found) != 1:
        raise ValueError("Semantic membership criterion changed")
    m = found[0]
    parts = _BR.split(m.group("content"))
    if len(parts) != 7 or not parts[0].endswith(" ="):
        raise ValueError("Membership predicate has unexpected conjunction structure")
    expected = (
        "Expressible_E(a)", "and ValidOrReviewable_E(a)",
        "and Aligned(a, b, rho)", "and Composable_E(a)",
        "and TypedWarrant_E(a)", "and Reusable_E(a)",
    )
    if tuple(_plain(x) for x in parts[1:]) != expected:
        raise ValueError("Membership condition has changed")
    items = "".join("<li>" + x + "</li>" for x in parts[1:])
    replacement = (
        '<div class="sp-criterion" role="group" '
        'aria-label="Source semantic membership criterion">'
        '<div class="sp-criterion-head">' + parts[0] + '</div>'
        '<ol>' + items + '</ol></div>'
    )
    return body[:m.start()] + replacement + body[m.end():]


def _render_transport(body: str) -> str:
    """Separate the source-to-target formula from its unchanged record schema."""
    found = [
        m for m in _BLOCK.finditer(body)
        if "TransportRecord rho_T = {" in m.group("content")
    ]
    if len(found) != 1:
        raise ValueError("Semantic transport definition changed")
    m = found[0]
    parts = re.split(r'<br\s*/?>\s*<br\s*/?>', m.group("content"), maxsplit=1)
    if len(parts) != 2 or not parts[1].lstrip().startswith("TransportRecord rho_T = {"):
        raise ValueError("Transport definition no longer matches source structure")
    mapping = parts[0].strip()
    if 'alttext="T : (a, E_s) -&gt; (b, E_t, rho_T)"' not in mapping:
        raise ValueError("Transport source mapping changed")
    record = _source_schema(parts[1].strip(), "TransportRecord definition")
    replacement = (
        '<div class="sp-transport" role="group" '
        'aria-label="Semantic transport with preservation record">'
        '<div class="sp-transport-mapping">' + mapping + "</div>"
        + record + "</div>"
    )
    return body[:m.start()] + replacement + body[m.end():]



def _render_extreme_value_example(body: str) -> str:
    """Distinguish the author's informal comparison and formal witness shape."""
    found = [
        m for m in _BLOCK.finditer(body)
        if m.group("content").startswith(
            "supremum existence is weaker than the existence of x"
        )
    ]
    if len(found) != 1:
        raise ValueError("Original Extreme Value Theorem example changed")
    m = found[0]
    parts = re.split(
        r'<br\s*/?>\s*<br\s*/?>\s*expected shape\s*<br\s*/?>',
        m.group("content"), maxsplit=1,
    )
    if len(parts) != 2:
        raise ValueError("Missing authorial expected-shape separator")
    prose = unescape(parts[0]).strip()
    witness = unescape(parts[1]).strip()
    if not witness.startswith("exists x in Icc a b,") or "f y <= f x" not in witness:
        raise ValueError("Witness example differs from original notation")
    replacement = (
        '<div class="sp-proof-example" role="group" '
        'aria-label="Source Extreme Value Theorem comparison">'
        '<p>' + escape(prose) + '</p>'
        '<p class="sp-proof-example-label">expected shape</p>'
        '<pre><code>' + escape(witness) + '</code></pre></div>'
    )
    return body[:m.start()] + replacement + body[m.end():]


def render_semantic_participation(body: str) -> str:
    """Enhance only this essay; fail closed on unexpected source structure."""
    body = _render_sequence(body)
    body = _render_membership_criterion(body)
    body = _render_transport(body)
    body = _render_schemas(body)
    body = _render_extreme_value_example(body)
    body = _link_reader_map(body)
    body = _mobile_tables(body)
    if body.count('data-sp-alternative="mobile"') != 12:
        raise ValueError("Missing source-derived mobile table")
    if body.count('<dl class="sp-mobile-record') != 74:
        raise ValueError("Mobile record count differs from original twelve tables")
    if body.count('<div class="sp-record-field"') != 190:
        raise ValueError("Mobile field count differs from original table rows")
    return body
