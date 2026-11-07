#!/usr/bin/env python3
"""Detect residual source-notation and record-layout defects in published essays.

This is an editorial presentation audit, not a mathematical proof checker.
MathML expressions and preformatted record definitions are deliberately
excluded from textual-pattern checks; they have their own structural tests.
"""

from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ESSAYS = ROOT / "_site" / "essays"

# Disallow broken TeX escaping and ASCII transcriptions of specific central
# judgments. Other ordinary words such as "theta" are intentionally allowed.
BROKEN = {
    "raw probability notation": re.compile(r"\bP_theta\b"),
    "raw effect judgment": re.compile(r"\bGamma\s*;\s*M\s*;\s*E\s*;\s*C\b"),
    "raw probability pushforward": re.compile(r"\bg_#Law\b"),
    "unrendered TeX escapes": re.compile(r"\\(?:[|>_\[\]]|Gamma\b|theta\b|vdash\b|epsilon\b|rho\b)"),
    "plain-text benchmark record": re.compile(
        r"^\s*(?:type_first_item|target_type_record|candidate_inhabitant_record|"
        r"lambek_benchmark_item|lambek_model_output):\s*$"
    ),
}

REQUIRED_RECORDS: dict[str, tuple[str, ...]] = {
    "typed-generativity": (
        "type_first_item:", "target_type_record:", "candidate_inhabitant_record:",
    ),
    "lambek-machines": (
        "lambek_benchmark_item:", "lambek_model_output:",
        "lambek_machine_record:", "functorial_language_consistency_item:",
    ),
    "semantic-participation": ("TransportRecord rho_T = {",),
    "quantitative-curry-howard": ("Q = (",),
    "effectful-and-conceptual-intelligence": (
        "handler(eps, rho, Pre, C, E)", "validator(Post, observed_state_delta, frame_conditions)",
    ),
}

IGNORED = {"math", "pre", "code", "script", "style", "svg"}


class VisibleNotation(HTMLParser):
    """Extract displayed prose and structured code without reading MathML annotations."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.visible: list[str] = []
        self.records: list[str] = []
        self._pre: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.stack.append(tag)
        if tag == "pre":
            self._pre = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "pre" and self._pre is not None:
            self.records.append("".join(self._pre))
            self._pre = None
        if tag in self.stack:
            # HTMLParser is a token parser, so tolerate an otherwise malformed
            # close while letting the independent DOM checks reject it.
            index = len(self.stack) - 1 - self.stack[::-1].index(tag)
            del self.stack[index:]

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        pass

    def handle_data(self, data: str) -> None:
        if self._pre is not None:
            self._pre.append(data)
        if not any(tag in IGNORED for tag in self.stack):
            normalized = " ".join(data.split())
            if normalized:
                self.visible.append(normalized)


def main() -> int:
    """Audit every generated manuscript page and return failure on broken notation."""
    pages = sorted(ESSAYS.glob("*.html"))
    issues: list[str] = []
    if len(pages) != 9:
        issues.append(f"Expected nine essays, found {len(pages)}")
    record_count = 0
    for page in pages:
        audit = VisibleNotation()
        audit.feed(page.read_text(encoding="utf-8"))
        audit.close()
        record_count += len(audit.records)
        for fragment in audit.visible:
            for label, expression in BROKEN.items():
                if expression.search(fragment):
                    issues.append(f"{page.stem}: {label}: {fragment[:110]}")
        record_text = "\n".join(audit.records)
        for required in REQUIRED_RECORDS.get(page.stem, ()):
            if required not in record_text:
                issues.append(f"{page.stem}: record missing from preformatted output: {required}")
    if issues:
        for issue in issues:
            print("FAIL:", issue)
        return 1
    print(f"PASS: notation and structured-record audit, {len(pages)} essays, "
          f"{record_count} preformatted records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
