#!/usr/bin/env python3
"""Source-faithful presentation for the Functorial Consistency V3 essay.

The authorial manuscript and its nineteen tables remain unchanged. The
original ASCII square is rendered as a responsive semantic figure. Source
tables retain their native structure, while small screens display exact
copies of each authored data cell in an accessible definition-list layout.
All transformations fail closed if the V3 source structure changes.
"""

from __future__ import annotations

from html import escape, unescape
import re


HEADERS: dict[int, tuple[str, ...]] = {
    1: ("ID", "Contribution", "Technical content"),
    2: ("Field", "Meaning", "Required annotation"),
    3: ("Regime", "Acceptance relation", "Validator"),
    4: ("Evaluation family", "Primary question", "Additional requirement introduced here"),
    5: ("Family", "Definition", "Initial domains"),
    6: ("Metric", "Question", "Signal"),
    7: ("Failure label", "Definition", "Repair implication"),
    8: ("Field", "Type or value", "Purpose"),
    9: ("Field", "Purpose"),
    10: ("Domain", "Seed items", "Primary equivalence regime"),
    11: ("Step", "Action", "Acceptance criterion"),
    12: ("Phase", "Work product"),
    13: ("Objection", "Operational response", "Required test"),
    14: ("Failure mode", "Adverse evidence", "Decision"),
    15: ("Criterion", "Decision rule"),
    16: ("Field", "Entry"),
    17: ("ID", "Domain", "Square", "Equivalence regime"),
    18: ("Rubric dimension", "Review question"),
    19: ("Area", "Revision"),
}

ROW_COUNTS: dict[int, int] = {
    1: 5, 2: 8, 3: 6, 4: 5, 5: 8,
    6: 9, 7: 12, 8: 16, 9: 13, 10: 5,
    11: 8, 12: 6, 13: 7, 14: 8, 15: 7,
    16: 15, 17: 5, 18: 6, 19: 7,
}

SOURCE_TABLE_LABELS: dict[int, str] = {
    **{index: str(index) for index in range(1, 16)},
    16: "A1", 17: "B1", 18: "C1", 19: "E1",
}

_TABLE = re.compile(
    r'(?P<opening><div aria-labelledby="table-(?P<n>\d+)-caption" '
    r'class="table-scroll" data-columns="(?P<columns>\d+)" '
    r'role="group" tabindex="0">)'
    r'(?P<table><table data-source-table="\d+" id="table-\d+">'
    r'[\s\S]*?</table>)(?P<closing></div>)'
)
_TBODY = re.compile(r"<tbody>([\s\S]*?)</tbody>")
_THEAD = re.compile(r"<thead>([\s\S]*?)</thead>")
_ROW = re.compile(r"<tr\b[^>]*>([\s\S]*?)</tr>")
_TH = re.compile(r"<th\b[^>]*>([\s\S]*?)</th>")
_TD = re.compile(r"<td(?:\s[^>]*)?>([\s\S]*?)</td>")
_TAG = re.compile(r"<[^>]+>")
_SCROLL_HINT = "Scroll sideways to view every table column."

_SOURCE_SQUARE = re.compile(
    r"<blockquote>\s*<p>"
    r"source object x -- f --&gt; transformed source f\(x\)<br\s*/>\s*"
    r"\| \|<br\s*/>\s*T T<br\s*/>\s*v v<br\s*/>\s*"
    r"target object T\(x\) -- g --&gt; transformed target g\(T\(x\)\)<br\s*/>\s*"
    r"<br\s*/>\s*Evaluation condition<br\s*/>\s*"
    r"T\(f\(x\)\) ~ g\(T\(x\)\)</p>\s*</blockquote>"
)


def render_functorial_diagram(body: str) -> str:
    """Turn the original ASCII square into a labeled two-path diagram.

    The diagram retains the original four objects, transformation labels,
    vertical transports and independent target-equivalence condition.
    """
    matches = list(_SOURCE_SQUARE.finditer(body))
    if len(matches) != 1:
        raise ValueError(
            "Functorial Consistency original commutation square is missing or changed"
        )
    diagram = (
        '<figure class="fc-commuting" '
        'aria-label="Commutation square for two typed construction paths">'
        '<div class="fc-square-grid">'
        '<div class="fc-square-node fc-source-node">'
        '<span class="fc-node-description">source object</span>'
        '<span class="fc-node-math">x</span></div>'
        '<div class="fc-horizontal-arrow" role="img" '
        'aria-label="source-side transformation f"><span aria-hidden="true">f →</span></div>'
        '<div class="fc-square-node fc-source-node">'
        '<span class="fc-node-description">transformed source</span>'
        '<span class="fc-node-math">f(x)</span></div>'
        '<div class="fc-down-arrow" role="img" '
        'aria-label="translation T"><span aria-hidden="true">T ↓</span></div>'
        '<div class="fc-square-relation" role="img" '
        'aria-label="Paths compared under the stated equivalence regime">'
        '<span aria-hidden="true">∼</span></div>'
        '<div class="fc-down-arrow" role="img" '
        'aria-label="translation T"><span aria-hidden="true">T ↓</span></div>'
        '<div class="fc-square-node fc-target-node">'
        '<span class="fc-node-description">target object</span>'
        '<span class="fc-node-math">T(x)</span></div>'
        '<div class="fc-horizontal-arrow" role="img" '
        'aria-label="target-side transformation g"><span aria-hidden="true">g →</span></div>'
        '<div class="fc-square-node fc-target-node">'
        '<span class="fc-node-description">transformed target</span>'
        '<span class="fc-node-math">g(T(x))</span></div>'
        '</div>'
        '<figcaption>'
        '<span class="fc-condition-label">Evaluation condition</span>'
        '<span class="fc-condition-formula">T(f(x)) ~ g(T(x))</span>'
        '</figcaption></figure>'
    )
    match = matches[0]
    return body[:match.start()] + diagram + body[match.end():]


def _text(html: str) -> str:
    """Read a source header without altering authored punctuation."""
    return unescape(_TAG.sub("", html)).strip()


def _source_captions(body: str) -> str:
    """Keep the authorial caption visible; align generated AT captions to it."""
    for number, label in SOURCE_TABLE_LABELS.items():
        paragraph = re.compile(
            rf'(?P<original><p>(?P<caption>Table {label}\. [^<]+)</p>)\s*'
            rf'<p class="table-display-caption" id="table-{number}-caption">'
            r'[^<]*</p>'
        )
        found = list(paragraph.finditer(body))
        if len(found) != 1:
            raise ValueError(
                f"Original visible table {number} caption changed"
            )
        original = found[0].group("original")
        authored_caption = found[0].group("caption")
        # Accessible metadata derived from actual source headings, when an
        # authored caption is too short for the publication's descriptor check.
        accessible_caption = (
            authored_caption if len(authored_caption.strip()) >= 30 else
            authored_caption + " — " + ", ".join(HEADERS[number])
        )
        replacement = (
            original + "\n" +
            f'<p class="table-display-caption" id="table-{number}-caption">' +
            accessible_caption + "</p>"
        )
        body = paragraph.sub(lambda _: replacement, body, count=1)

        native = re.compile(
            rf'(?P<opening><table data-source-table="{number}" id="table-{number}">'
            r'\s*<caption class="visually-hidden">)[^<]*'
            r'(?P<end></caption>)'
        )
        if len(native.findall(body)) != 1:
            raise ValueError(f"Original table {number} native caption changed")
        body = native.sub(
            lambda m: m.group("opening") + accessible_caption + m.group("end"),
            body, count=1,
        )
    return body


def render_functorial_tables(body: str) -> str:
    """Render 156 mobile source rows with all 419 original data cells."""
    body = _source_captions(body)
    source_tables = list(_TABLE.finditer(body))
    if [int(m.group("n")) for m in source_tables] != list(range(1, 20)):
        raise ValueError("Original 19-table inventory or order has changed")

    for match in reversed(source_tables):
        number = int(match.group("n"))
        table = match.group("table")
        thead = _THEAD.search(table)
        tbody = _TBODY.search(table)
        if thead is None or tbody is None:
            raise ValueError(f"Table {number} lacks native sections")
        headers = tuple(_text(c) for c in _TH.findall(thead.group(1)))
        if headers != HEADERS[number] or len(headers) != int(match.group("columns")):
            raise ValueError(f"Table {number} headers differ from original V3")
        rows = _ROW.findall(tbody.group(1))
        if len(rows) != ROW_COUNTS[number]:
            raise ValueError(f"Table {number} row count differs from original V3")
        cards: list[str] = []
        for row in rows:
            cells = _TD.findall(row)
            if len(cells) != len(headers):
                raise ValueError(f"Table {number} source cell structure changed")
            fields: list[str] = []
            for index, (header, cell) in enumerate(
                zip(headers, cells, strict=True)
            ):
                mobile_cell = cell
                if number in (8, 9) and index == 0 and "." in cell:
                    # The model-output and benchmark-item schemas contain
                    # dotted field paths. Keep the exact text, with a natural
                    # reading break at the already-authored dot separator.
                    name, attribute = cell.split(".", 1)
                    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", name) or not re.fullmatch(
                        r"[A-Za-z][A-Za-z0-9_]*", attribute
                    ):
                        raise ValueError(
                            f"Unexpected dotted field in table {number}: {cell}"
                        )
                    mobile_cell = (
                        '<span class="fc-field-object">' + escape(name + ".") +
                        '</span><span class="fc-field-attribute">' +
                        escape(attribute) + '</span>'
                    )
                fields.append(
                    '<div class="fc-record-field"><dt>' + escape(header) +
                    '</dt><dd>' + mobile_cell + '</dd></div>'
                )
            card_fields = "".join(fields)
            cards.append('<dl class="fc-mobile-record">' + card_fields + '</dl>')

        hint_id = f"fc-table-{number}-scroll-hint"
        wrapper = match.group("opening").replace(
            'class="table-scroll"',
            'class="table-scroll" data-fc-alternative="mobile"', 1
        )
        wrapper = wrapper[:-1] + f' aria-describedby="{hint_id}">'
        hint = (
            f'<p class="fc-scroll-hint" id="{hint_id}">' +
            escape(_SCROLL_HINT) + "</p>\n"
        )
        mobile = (
            f'<section class="fc-mobile-records fc-mobile-table-{number}" '
            f'aria-labelledby="table-{number}-caption">' +
            "".join(cards) + "</section>"
        )
        replacement = hint + wrapper + table + match.group("closing") + mobile
        body = body[:match.start()] + replacement + body[match.end():]
    if body.count('data-fc-alternative="mobile"') != 19:
        raise ValueError("Missing Functorial Consistency mobile table")
    if body.count('<dl class="fc-mobile-record">') != 156:
        raise ValueError("Mobile row count differs from original V3")
    if body.count('class="fc-record-field"') != 419:
        raise ValueError("Mobile data-cell count differs from original V3")
    if body.count('class="fc-field-attribute"') != 12:
        raise ValueError("Dotted source field inventory differs from V3")
    return body
