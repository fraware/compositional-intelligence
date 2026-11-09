#!/usr/bin/env python3
"""Source-verified publication layout for Effectful and Conceptual Intelligence V3.

This module changes only generated presentation. The canonical manuscript fragment
is immutable. All tables, scientific statements, and technical records originate
in that source, with fail-closed checks for unexpected inventories.
"""
from __future__ import annotations

from html import escape, unescape
import re

from render_lambek import mathml

HEADERS = {
    1: ("ID", "Contribution", "Publication claim"),
    2: ("Reader", "Recommended path"),
    3: ("Symbol", "Meaning", "Operational role"),
    4: ("Phase", "Question", "Failure exposed"),
    5: ("Effect class", "Typical operation", "Required record field"),
    6: ("Ledger field group", "Purpose"),
    7: ("Level", "Plan maturity"),
    8: ("Transfer field", "Question"),
    9: ("Security failure", "Effect-control diagnosis"),
    10: ("Component", "Benchmark obligation"),
    11: ("Metric", "Definition"),
    12: ("Objection", "Response"),
    13: ("Failure mode", "Meaning"),
    14: ("Criterion", "Decision rule"),
    15: ("Essay", "Core contribution"),
    16: ("Field", "Specification"),
    17: ("Field", "Specification"),
    18: ("Field", "Specification"),
    19: ("Claim", "Level", "Treatment"),
}
ROWS = (6, 5, 9, 4, 10, 7, 6, 7, 7, 7, 9, 8, 10, 10, 7, 8, 15, 14, 5)
CAPTIONS = {
    1: "Table 1. Contributions and publication claims.",
    2: "Table 2. Recommended reading paths.",
    3: "Table 3. Typed-action judgment symbols and roles.",
    4: "Table 4. Execution phases and exposed failures.",
    5: "Table 5. Effect classes and required records.",
    6: "Table 6. Typed Action Ledger field groups.",
    7: "Table 7. Plan maturity levels.",
    8: "Table 8. Conceptual transfer evaluation fields.",
    9: "Table 9. Security failures and effect-control diagnoses.",
    10: "Table 10. Benchmark components and obligations.",
    11: "Table 11. Benchmark evaluation metrics.",
    12: "Table 12. Objections and responses.",
    13: "Table 13. Effectful execution failure taxonomy.",
    14: "Table 14. Kill criteria and decision rules.",
    15: "Table 15. Contributions across the essay series.",
    16: "Table 16. Typed Action Ledger schema.",
    17: "Table 17. Effectful Agent Benchmark schema.",
    18: "Table 18. Concept Transfer Record schema.",
    19: "Table 19. Claims, evidential levels, and treatments.",
}
CORRUPT_CAPTIONS = {2: "Table 1.", 11: "Table 10.", 13: "Table 12."}
SECTION_IDS = {
    "1": "position-in-the-compositional-intelligence-series",
    "2": "evaluation-unit-for-agent-action",
    "3": "the-typed-action-judgment",
    "4": "execution-phases",
    "5": "effect-taxonomy",
    "6": "handlers-validators-and-authority",
    "7": "typed-action-ledger",
    "8": "memory-tools-plans-and-skills",
    "8.1": "memory-as-effect",
    "8.2": "tools-as-typed-interfaces",
    "8.3": "plans-as-state-transition-programs",
    "8.4": "skills-as-reusable-effectful-programs",
    "9": "conceptual-intelligence-as-controlled-transfer",
    "10": "security-as-effect-control",
    "11": "effectful-agent-benchmark-v0.2",
    "12": "diagnostic-cases",
    "13": "objections-and-failure-modes",
    "14": "kill-criteria-and-series-synthesis",
    "14.1": "kill-criteria",
    "14.2": "series-synthesis",
}
APPENDIX_IDS = {
    "A": "appendix-a.-typed-action-ledger-schema",
    "B": "appendix-b.-effectful-agent-benchmark-schema",
    "C": "appendix-c.-concept-transfer-record-schema",
    "D": "appendix-d.-claim-ledger",
    "E": "appendix-e.-source-use-notes",
}
STAGES = (
    "membership", "generation", "transformation", "language",
    "architecture", "warrant", "action",
)
# Exact source transcription for all standalone formal expressions.
EXPRESSION_TEX = {
    "Gamma; M; E; C |- a : Pre -> Post ! eps @ rho": (
        r"\begin{gathered}"
        r"\Gamma;M;E;C\vdash a:\\"
        r"\mathrm{Pre}\to\mathrm{Post}\;!\,\varepsilon@\rho"
        r"\end{gathered}"
    ),
    "handler(eps, rho, Pre, C, E) -> authorize | deny | ask | sandbox | escalate": (
        r"\begin{gathered}"
        r"\operatorname{handler}(\varepsilon,\rho,\mathrm{Pre},C,E)\to\\"
        r"\operatorname{authorize}\mid\operatorname{deny}\mid\operatorname{ask}\\"
        r"\mid\operatorname{sandbox}\mid\operatorname{escalate}"
        r"\end{gathered}"
    ),
    "validator(Post, observed_state_delta, frame_conditions) -> pass | fail | partial | unknown": (
        r"\begin{gathered}"
        r"\operatorname{validator}(\mathrm{Post},\\"
        r"\mathrm{observed\_state\_delta},\\"
        r"\mathrm{frame\_conditions})\to\\"
        r"\operatorname{pass}\mid\operatorname{fail}\\"
        r"\mid\operatorname{partial}\mid\operatorname{unknown}"
        r"\end{gathered}"
    ),
    "Gamma; M; E; C |- write_memory(m) : M -> M + {m} ! memory_write @ rho": (
        r"\begin{gathered}"
        r"\Gamma;M;E;C\vdash\operatorname{write\_memory}(m):\\"
        r"M\to M+\{m\}\;!\,\operatorname{memory\_write}@\rho"
        r"\end{gathered}"
    ),
    "Gamma; M; E; C |- pi : Pre_0 -> Post_n ! (eps_1 + ... + eps_n) @ rho": (
        r"\begin{gathered}"
        r"\Gamma;M;E;C\vdash\pi:\\"
        r"\mathrm{Pre}_{0}\to\mathrm{Post}_{n}\\"
        r"!\,(\varepsilon_1+\cdots+\varepsilon_n)@\rho"
        r"\end{gathered}"
    ),
    "skill s : Pre -> Post ! eps": (
        r"\operatorname{skill}\;s:\mathrm{Pre}\to\mathrm{Post}\;!\,\varepsilon"
    ),
    "concept_transfer : SourceDomain -> TargetDomain": (
        r"\begin{gathered}"
        r"\operatorname{concept\_transfer}:\\"
        r"\mathrm{SourceDomain}\to\mathrm{TargetDomain}"
        r"\end{gathered}"
    ),
}
SOURCE_NOTES = (
    "- Hoare logic, PDDL, monads, algebraic effects, and effect-system sources support the technical background for preconditions, postconditions, planning effects, and computational effects. They do not establish the Typed Action Ledger proposal.",
    "- ReAct and Toolformer support the context in which language models interleave reasoning with action or learn tool-use patterns. They do not establish type-and-effect records for agents.",
    "- WebArena, OSWorld, tau-bench, AgentDojo, and AgentRewardBench support the need for richer trajectory-level evaluation. They do not validate the proposed Effectful Agent Benchmark.",
    "- Security sources support prompt-injection and untrusted-tool-result risks. The effect-control taxonomy is an original synthesis in this essay.",
    "- Conceptual-transfer records are proposed as a way to control analogy and abstraction where transfer affects explanation, planning, memory, scientific claims, or action.",
)
TABLE = re.compile(
    r'(?P<start><div aria-labelledby="table-(?P<n>\d+)-caption" '
    r'class="table-scroll" data-columns="\d+" role="group" tabindex="0">)'
    r'(?P<table><table data-source-table="\d+" id="table-\d+">'
    r'[\s\S]*?</table>)(?P<end></div>)'
)
TAG = re.compile(r"<[^>]+>")


def clean_captions(body: str) -> str:
    """Repair conversion-only captions with wording derived from source tables."""
    for n, label in CAPTIONS.items():
        visible = re.compile(
            rf'(<p class="table-display-caption" id="table-{n}-caption">)'
            r'(?P<text>[^<]*)(</p>)'
        )
        matches = list(visible.finditer(body))
        if len(matches) != 1:
            raise ValueError(f"Original table caption {n} missing or duplicated")
        original = unescape(matches[0].group("text"))
        if n in CORRUPT_CAPTIONS:
            if len(original) < 600 or not original.startswith(CORRUPT_CAPTIONS[n]):
                raise ValueError(f"Unexpected source caption corruption at table {n}")
        elif not original.startswith(f"Table {n}."):
            raise ValueError(f"Original table number at table {n} changed")
        body = visible.sub(
            lambda m: m.group(1).replace(
                'class="table-display-caption"',
                'class="table-display-caption ef-caption"'
            ) + escape(label) + m.group(3),
            body,
            count=1,
        )
        native = re.compile(
            rf'(<table data-source-table="{n}" id="table-{n}">'
            r'<caption class="visually-hidden">)[^<]*(</caption>)'
        )
        if len(native.findall(body)) != 1:
            raise ValueError(f"Native source caption for table {n} missing")
        body = native.sub(
            lambda m: m.group(1) + escape(label) + m.group(2),
            body,
            count=1,
        )
    return body


def reader_map(body: str) -> str:
    """Link the source reader map only to actual headings and neighboring essays."""
    expression = re.compile(
        r'(<table data-source-table="2" id="table-2">)'
        r'([\s\S]*?)(</table>)'
    )
    matches = list(expression.finditer(body))
    if len(matches) != 1:
        raise ValueError("Effectful source reader map missing")
    match = matches[0]
    content = match.group(2)
    row_pattern = re.compile(
        r'(<tr\b[^>]*>\s*<td>[^<]*</td>\s*<td>)([^<]*)(</td>\s*</tr>)'
    )
    rows = list(row_pattern.finditer(content))
    if len(rows) != 5:
        raise ValueError("Effectful source reader-map inventory changed")
    for row in reversed(rows):
        text = row.group(2)
        if "Read after Essay 6;" in text:
            linked = text.replace(
                "Essay 6", '<a href="quantitative-curry-howard.html">Essay 6</a>',
                1
            )
            linked = re.sub(
                r"Section 14\b",
                'Section <a href="#' + SECTION_IDS["14"] + '">14</a>',
                linked,
                count=1,
            )
        else:
            linked = re.sub(
                r"\b\d+(?:\.\d+)?\b",
                lambda m: (
                    '<a href="#' + SECTION_IDS[m.group()] + '">' +
                    m.group() + "</a>"
                ) if m.group() in SECTION_IDS else m.group(),
                text,
            )
            for letter, target in APPENDIX_IDS.items():
                linked = linked.replace(
                    "Appendix " + letter,
                    'Appendix <a href="#' + target + '">' + letter + "</a>",
                    1
                )
        content = content[:row.start(2)] + linked + content[row.end(2):]
    return (
        body[:match.start()] + match.group(1) + content +
        match.group(3) + body[match.end():]
    )


def _sequence(body: str) -> str:
    """Show the seven original dependencies as a directed reading sequence."""
    source = '<p>' + " -&gt; ".join(STAGES) + "</p>"
    if body.count(source) != 1:
        raise ValueError("Authored seven-stage essay synthesis changed")
    replacement = (
        '<div class="ef-sequence" role="group" '
        'aria-label="Authored seven-stage intelligence sequence">'
        '<ol>' + "".join("<li>" + escape(stage) + "</li>" for stage in STAGES) +
        "</ol></div>"
    )
    return body.replace(source, replacement, 1)


def _formulas(body: str) -> str:
    """Add semantic MathML to exact authored formal judgments."""
    for i, (text, latex) in enumerate(EXPRESSION_TEX.items(), 1):
        source = "<p>" + escape(text, quote=False) + "</p>"
        if body.count(source) != 1:
            raise ValueError(f"Original effectful formula {i} missing or changed")
        rendered = (
            f'<div class="ef-math ef-math-{i}" role="group" '
            'aria-label="Source formal expression">' +
            mathml(text, latex) + "</div>"
        )
        body = body.replace(source, rendered, 1)
    return body


def _source_notes(body: str) -> str:
    """Render five original publication-source warnings as a proper list."""
    markup = re.compile(
        r'<blockquote>\s*(?P<paragraphs>(?:<p>[\s\S]*?</p>\s*)+)</blockquote>'
    )
    matches = list(markup.finditer(body))
    if len(matches) != 1:
        raise ValueError("Expected one source-use quotation with five bullet lines")
    match = matches[0]
    paragraphs = re.findall(
        r"<p>([^<]*)</p>", match.group("paragraphs")
    )
    if tuple(unescape(line) for line in paragraphs) != SOURCE_NOTES:
        raise ValueError("Original source-use notes changed")
    if '<h2 id="appendix-e.-source-use-notes">' not in body[:match.start()]:
        raise ValueError("Source-use notes outside expected appendix")
    replacement = (
        '<ul class="ef-source-notes">' +
        "".join("<li>" + escape(line[2:]) + "</li>" for line in SOURCE_NOTES) +
        "</ul>"
    )
    return body[:match.start()] + replacement + body[match.end():]


def tables(body: str) -> str:
    """Duplicate source data cells into responsive DL records without edits."""
    matches = list(TABLE.finditer(body))
    if [int(m.group("n")) for m in matches] != list(range(1, 20)):
        raise ValueError("Effectful source 19-table inventory changed")
    total_cells = 0
    total_rows = 0
    for match in reversed(matches):
        n = int(match.group("n"))
        source_table = match.group("table")
        thead = re.search(r"<thead>([\s\S]*?)</thead>", source_table)
        tbody = re.search(r"<tbody>([\s\S]*?)</tbody>", source_table)
        if not thead or not tbody:
            raise ValueError(f"Missing scientific table structure at {n}")
        headings = tuple(
            unescape(TAG.sub("", part)).strip()
            for part in re.findall(
                r"<th\b[^>]*>([\s\S]*?)</th>", thead.group(1)
            )
        )
        if headings != HEADERS[n]:
            raise ValueError(f"Original table {n} source headings changed")
        rows = re.findall(
            r"<tr\b[^>]*>([\s\S]*?)</tr>", tbody.group(1)
        )
        if len(rows) != ROWS[n - 1]:
            raise ValueError(f"Unexpected authored row count at table {n}")
        cards = []
        total_rows += len(rows)
        for row in rows:
            values = re.findall(r"<td(?:\s[^>]*)?>([\s\S]*?)</td>", row)
            if len(values) != len(headings):
                raise ValueError(f"Unexpected table {n} data-cell count")
            total_cells += len(values)
            fields = "".join(
                '<div class="ef-field"><dt>' + escape(name) + "</dt>"
                "<dd>" + value + "</dd></div>"
                for name, value in zip(headings, values, strict=True)
            )
            cards.append('<dl class="ef-card">' + fields + "</dl>")
        hint = (
            f'<p class="ef-hint" id="ef-hint-{n}">'
            'Scroll horizontally to see all table columns.</p>'
        )
        start = match.group("start").replace(
            'class="table-scroll"',
            'class="table-scroll" data-ef-alternative="mobile"',
            1,
        )
        start = start[:-1] + f' aria-describedby="ef-hint-{n}">'
        alternative = (
            f'<section class="ef-mobile ef-mobile-{n}" '
            f'aria-labelledby="table-{n}-caption">' +
            "".join(cards) + "</section>"
        )
        body = (
            body[:match.start()] + hint + start + source_table +
            match.group("end") + alternative + body[match.end():]
        )
    if total_rows != 154 or total_cells != 342:
        raise ValueError("Original authored 154 rows and 342 cells changed")
    return body


def render_effectful_and_conceptual_intelligence(body: str) -> str:
    """Transform presentation only after verifying the source structures."""
    for transform in (clean_captions, reader_map, _sequence, _formulas,
                      _source_notes, tables):
        body = transform(body)
    checks = {
        'class="ef-caption"': 0,  # Caption carries both names.
        'class="table-display-caption ef-caption"': 19,
        'data-ef-alternative="mobile"': 19,
        'class="ef-card"': 154,
        'class="ef-field"': 342,
        'class="ef-sequence"': 1,
        'class="ef-math ef-math-': 7,
        'class="ef-source-notes"': 1,
    }
    if any(body.count(marker) != n for marker, n in checks.items()):
        raise ValueError("Incomplete effectful source-derived publication")
    return body
