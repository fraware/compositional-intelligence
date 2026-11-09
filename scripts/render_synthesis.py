#!/usr/bin/env python3
"""Typeset the two diagrams authored in the flagship V3 manuscript.

The eight-stage lifecycle is transcribed from the authored arrow sequence.
The commuting-square is represented by the original Word table, retaining
all original table IDs, cells and accessibility captions, inside a semantic
figure. Visual arrows explain the existing source transformation labels.

No manuscript file is edited, and mismatching source fragments fail closed.
"""

from __future__ import annotations

from html import escape, unescape
import re

_LIFECYCLE = re.compile(
    r'<p><strong>(?P<first>[\s\S]*?)<br\s*/?>\s*</strong>'
    r'(?P<second>[\s\S]*?)</p>\s*'
    r'<p>(?P<caption>Figure\. From output to artifact\.[^<]+)</p>'
)
_SQUARE = re.compile(
    r'(?P<label><p class="table-display-caption" id="table-5-caption">'
    r'[\s\S]*?</p>)\s*'
    r'(?P<table><div aria-labelledby="table-5-caption" '
    r'class="table-scroll"[\s\S]*?<table data-source-table="5" '
    r'id="table-5">[\s\S]*?</table></div>)\s*'
    r'<p>(?P<caption>Figure\. Functorial Consistency square\.[^<]+)</p>'
)

_STAGES = (
    "output",
    "candidate artifact",
    "typed candidate",
    "transformed artifact",
    "validated artifact",
    "warranted artifact",
    "reusable artifact",
    "effectful action",
)
_SQUARE_CELLS = (
    "source object x",
    "transformed source f(x)",
    "target object T(x)",
    "transformed target g(T(x))",
    "-- f --&gt;",
    "-- g --&gt;",
)


def _lifecycle_figure(match: re.Match[str]) -> str:
    """Convert the original arrow-delimited stages into an ordered figure."""
    text = unescape(
        re.sub(r"\s+", " ", match.group("first") + " " + match.group("second"))
    ).strip()
    stages = tuple(part.strip() for part in text.split("->"))
    if stages != _STAGES:
        raise ValueError("Flagship lifecycle source stages have changed")
    caption = match.group("caption")
    items = "".join("<li>" + escape(stage) + "</li>" for stage in stages)
    return (
        '<figure class="ci-source-figure ci-lifecycle" '
        'aria-labelledby="ci-lifecycle-caption">'
        '<ol aria-label="Original artifact lifecycle">' + items + "</ol>"
        '<figcaption id="ci-lifecycle-caption">' + caption +
        "</figcaption></figure>"
    )


def _square_figure(match: re.Match[str]) -> str:
    """Retain the source Word table while clarifying its directional arrows."""
    table = match.group("table")
    for text in _SQUARE_CELLS:
        if text not in table:
            raise ValueError("Flagship commuting-square source changed: " + text)
    if table.count("<td>| T</td>") != 2:
        raise ValueError("Expected two source-to-target arrows")
    if table.count("<strong>-- f --&gt;</strong>") != 1:
        raise ValueError("Expected one source-side arrow")
    if table.count("<td>-- g --&gt;</td>") != 1:
        raise ValueError("Expected one target-side arrow")
    table = table.replace(
        "<strong>-- f --&gt;</strong>",
        '<strong class="ci-right-arrow" aria-label="source-side transformation f">'
        '<span aria-hidden="true">⟶</span> <var aria-hidden="true">f</var></strong>'
    ).replace(
        "<td>-- g --&gt;</td>",
        '<td><span class="ci-right-arrow" aria-label="target-side transformation g">'
        '<span aria-hidden="true">⟶</span> <var aria-hidden="true">g</var></span></td>'
    ).replace(
        "<td>| T</td>",
        '<td><span class="ci-down-arrow" aria-label="transport T downward">'
        '<span aria-hidden="true">↓</span> <var aria-hidden="true">T</var></span></td>'
    )
    # A source-equivalent compact grid prevents horizontal clipping at phone
    # widths. Split mathematical symbols across markup nodes to preserve a
    # static, accessible fallback when the full table is visually suppressed.
    mobile = (
        '<div class="ci-commuting-mobile" role="group" '
        'aria-label="Source and target transformation paths">'
        '<div class="ci-commuting-mobile-grid">'
        '<span class="ci-square-object">source object <var>x</var></span>'
        '<span class="ci-square-arrow">→ <var>f</var></span>'
        '<span class="ci-square-object">transformed source '
        '<var>f</var>(<var>x</var>)</span>'
        '<span class="ci-square-arrow ci-square-down">↓ <var>T</var></span>'
        '<span class="ci-square-spacer" aria-hidden="true"></span>'
        '<span class="ci-square-arrow ci-square-down">↓ <var>T</var></span>'
        '<span class="ci-square-object">target object <var>T</var>(<var>x</var>)</span>'
        '<span class="ci-square-arrow">→ <var>g</var></span>'
        '<span class="ci-square-object">transformed target '
        '<var>g</var>(<var>T</var>(<var>x</var>))</span>'
        '</div></div>'
    )
    return (
        '<figure class="ci-source-figure ci-commuting" '
        'aria-labelledby="ci-commuting-caption">'
        + match.group("label") + table + mobile
        + '<figcaption id="ci-commuting-caption">' + match.group("caption") +
        "</figcaption></figure>"
    )


_SOURCE_LABEL_IDS = (1, 2, 3, 4, 6, 7, 8)
_GENERATED_ACCESSIBLE_CAPTIONS = {
    5: "Table 5. Source and target objects in the Functorial Consistency square.",
    9: "Table 9. Claim levels, meanings, and publication treatment.",
    10: "Table 10. Epistemic types and their meanings.",
}


def _improve_source_table_labels(body: str) -> str:
    """Keep each authored caption once and preserve the table's native caption.

    The DOCX conversion duplicated seven source captions as separate hidden
    paragraphs. Each original caption becomes the table group's accessible
    label. Synthetic catalogue descriptions remain only on tables lacking an
    authored caption.
    """
    for number in _SOURCE_LABEL_IDS:
        pattern = re.compile(
            r'(?P<source><p>(?P<text>Table\.[^<]+)</p>)\s*'
            rf'<p class="table-display-caption" id="table-{number}-caption">'
            r'(?P<duplicate>[^<]+)</p>'
        )
        found = list(pattern.finditer(body))
        if len(found) != 1:
            raise ValueError(f"Missing or duplicated authored table label {number}")
        item = found[0]
        if unescape(item.group("text")) != unescape(item.group("duplicate")):
            raise ValueError(f"Source table {number} caption differs from conversion")
        preserved = (
            f'<p id="table-{number}-caption" '
            f'class="table-display-caption source-visible-caption">'
            f'{item.group("text")}</p>'
        )
        body = body[:item.start()] + preserved + body[item.end():]

    # Only the conversion-generated (non-authorial) accessibility captions
    # are clarified; the authored headings and all table cells are retained.
    for number, label in _GENERATED_ACCESSIBLE_CAPTIONS.items():
        title = re.compile(
            rf'<p class="table-display-caption" id="table-{number}-caption">'
            r'[^<]+</p>'
        )
        title_matches = list(title.finditer(body))
        if len(title_matches) != 1:
            raise ValueError(f"Missing generated label for table {number}")
        body = title.sub(
            lambda _: (f'<p class="table-display-caption" '
                       f'id="table-{number}-caption">{escape(label)}</p>'),
            body, count=1
        )

        native = re.compile(
            rf'(?P<table><table\b[^>]*\bid="table-{number}"[^>]*>\s*)'
            r'<caption class="visually-hidden">[^<]+</caption>'
        )
        native_matches = list(native.finditer(body))
        if len(native_matches) != 1:
            raise ValueError(f"Missing native caption for table {number}")
        body = native.sub(
            lambda match: (match.group("table") +
                           '<caption class="visually-hidden">' +
                           escape(label) + '</caption>'),
            body, count=1
        )
    return body



_SCROLLABLE_TABLES = (1, 2, 3, 4, 6, 7, 8, 9, 10)
_SCROLL_HINT = "Swipe or scroll sideways to view all columns."


def _label_scrollable_source_tables(body: str) -> str:
    """Add a mobile-only, accessible scroll cue to each actual data table.

    The source-derived commuting square has its own compact mobile grid and
    therefore has no instruction suggesting sideways scrolling.
    """
    for number in _SCROLLABLE_TABLES:
        pattern = re.compile(
            rf'(?P<wrapper><div aria-labelledby="table-{number}-caption" '
            r'class="table-scroll" data-columns="\d+" role="group" '
            r'tabindex="0"><table\b[\s\S]*?</table></div>)'
        )
        matches = list(pattern.finditer(body))
        if len(matches) != 1:
            raise ValueError(
                f"Expected one source scientific table {number}, found {len(matches)}"
            )
        wrapper = matches[0].group("wrapper")
        described = wrapper.replace(
            'tabindex="0">',
            f'tabindex="0" aria-describedby="table-{number}-scroll-hint">',
            1,
        )
        hint = (
            f'<p id="table-{number}-scroll-hint" '
            'class="table-scroll-hint">' + escape(_SCROLL_HINT) + '</p>'
        )
        match = matches[0]
        body = body[:match.start()] + described + hint + body[match.end():]
    return body


def render_synthesis_figures(body: str) -> str:
    """Render precisely two figures, rejecting ambiguous source conversions."""
    lifecycle = list(_LIFECYCLE.finditer(body))
    square = list(_SQUARE.finditer(body))
    if len(lifecycle) != 1 or len(square) != 1:
        raise ValueError(
            f"Flagship source figure inventory changed: "
            f"lifecycle={len(lifecycle)}, square={len(square)}"
        )
    body = _LIFECYCLE.sub(_lifecycle_figure, body, count=1)
    body = _SQUARE.sub(_square_figure, body, count=1)
    body = _improve_source_table_labels(body)
    body = _label_scrollable_source_tables(body)
    if body.count('<figure class="ci-source-figure') != 2:
        raise ValueError("Flagship source figures were not rendered exactly")
    return body
