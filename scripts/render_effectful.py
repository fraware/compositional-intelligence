#!/usr/bin/env python3
"""Accessible presentation of the final Effectful and Conceptual Intelligence essay.

The authored Markdown is the publication source. This renderer derives compact
mobile records from its nine semantic HTML tables without changing table data.
All mobile records are generated from the same Pandoc table cells.
"""
from __future__ import annotations

from html import escape, unescape
import re

from render_lambek import mathml

TABLE_COUNT = 9
TABLE_GROUP = re.compile(
    r'<div class="table-scroll"[^>]*>[\s\S]*?</table>\s*</div>', re.I
)
TAG = re.compile(r"<[^>]+>")


def _label(markup: str) -> str:
    """Convert header-cell markup to a human-readable definition-list term."""
    return unescape(TAG.sub("", markup)).strip()


def _mobile_records(table_group: str, number: int) -> tuple[str, int, int]:
    """Create mobile definitions from native table headers and authored rows."""
    table = re.search(r"<table\b[^>]*>[\s\S]*?</table>", table_group, re.I)
    if table is None or f'id="table-{number}"' not in table.group():
        raise ValueError(f"Effectful table {number} missing its source identifier")

    thead = re.search(r"<thead\b[^>]*>(.*?)</thead>", table.group(), re.I | re.S)
    tbody = re.search(r"<tbody\b[^>]*>(.*?)</tbody>", table.group(), re.I | re.S)
    if thead is None or tbody is None:
        raise ValueError(f"Effectful table {number} lacks semantic sections")

    headers = [
        _label(cell)
        for cell in re.findall(r"<th\b[^>]*>(.*?)</th>", thead.group(1), re.I | re.S)
    ]
    if not (2 <= len(headers) <= 4) or any(not item for item in headers):
        raise ValueError(f"Effectful table {number} has invalid column headings")

    rows = re.findall(r"<tr\b[^>]*>(.*?)</tr>", tbody.group(1), re.I | re.S)
    if not rows:
        raise ValueError(f"Effectful table {number} has no data rows")

    cards: list[str] = []
    total_fields = 0
    for row in rows:
        values = re.findall(r"<td\b[^>]*>(.*?)</td>", row, re.I | re.S)
        if len(values) != len(headers):
            raise ValueError(f"Effectful table {number} has an incomplete row")
        total_fields += len(values)
        fields = "".join(
            '<div class="ef-field"><dt>' + escape(label) +
            "</dt><dd>" + value + "</dd></div>"
            for label, value in zip(headers, values, strict=True)
        )
        cards.append('<dl class="ef-card">' + fields + "</dl>")
    alternative = (
        f'<section class="ef-mobile ef-mobile-{number}" '
        f'aria-labelledby="table-{number}-caption">' +
        "".join(cards) + "</section>"
    )
    return alternative, len(rows), total_fields


def render_effectful_and_conceptual_intelligence(body: str) -> str:
    """Keep native tables for desktop/print and derive accessible mobile records.

    Reject any unexpected source inventory, missing caption, or mismatched table
    columns. Native table data is never edited; mobile data uses these same cells.
    """
    # Publication-only MathML for the authored typed-action judgment.
    # Preserve the exact original expression as alternative text.
    judgment = "Γ; M; E; C ⊢ a : Pre → Post ! ε @ ρ"
    code = "<code>" + judgment + "</code>"
    if body.count(code) != 2:
        raise ValueError("Effectful action judgment transcription changed")
    latex = (
        r"\Gamma;M;E;C\vdash a:\mathrm{Pre}\to\mathrm{Post}"
        r"\;!\,\varepsilon@\rho"
    )
    body = body.replace(code, mathml(judgment, latex))
    matches = list(TABLE_GROUP.finditer(body))
    if len(matches) != TABLE_COUNT:
        raise ValueError(
            f"Expected {TABLE_COUNT} Effectful manuscript tables, found {len(matches)}"
        )
    total_rows = total_fields = 0
    for number, match in reversed(list(enumerate(matches, 1))):
        group = match.group()
        marker = f'id="table-{number}-caption"'
        if body.count(marker) != 1:
            raise ValueError(f"Effectful table {number} lacks a unique caption")
        alternative, rows, fields = _mobile_records(group, number)
        total_rows += rows
        total_fields += fields
        group = group.replace(
            'class="table-scroll"',
            'class="table-scroll" data-ef-alternative="mobile"',
            1,
        )
        hint = (
            '<p class="ef-hint">Scroll horizontally to see all columns.</p>'
            if 'data-columns="3"' in group else ""
        )
        body = body[:match.start()] + hint + group + alternative + body[match.end():]

    body = body.replace(
        'class="table-display-caption"',
        'class="table-display-caption ef-caption"',
    )
    # Match the full native table-caption numbering in the visible heading.
    body, corrected = re.subn(
        r'(<span class="table-caption-number">Table [0-9]+)(</span>)',
        r'\1.\2', body,
    )
    if corrected != TABLE_COUNT:
        raise ValueError("Effectful visible table numbers are incomplete")
    if (body.count('class="ef-card"') != total_rows or
            body.count('class="ef-field"') != total_fields or
            body.count('data-ef-alternative="mobile"') != TABLE_COUNT or
            body.count('class="table-display-caption ef-caption"') != TABLE_COUNT):
        raise ValueError("Effectful mobile-table reconstruction is incomplete")
    return body
