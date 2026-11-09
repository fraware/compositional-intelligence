#!/usr/bin/env python3
"""Check source-faithful sequences and print representation of Typed Generativity.

The original manuscript-derived tables remain in the built page. At narrow
print widths, their complete source-derived mobile records are used to avoid
truncated four-column tables. Browser checks cover both sides of the 650px
breakpoint and the two exact authored progression sequences.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from playwright.sync_api import sync_playwright

_WIDTHS = (320, 375, 650, 651, 768, 1440)
_STAGES = (
    ("semantic membership", "target-type inference",
     "candidate inhabitant", "transformation preservation"),
    ("Gamma", "infer A", "construct t : A",
     "validate/repair", "semantic participation"),
)
_STYLESHEET_LINK = '<link rel="stylesheet" href="../style.css">'


def _rendered_page(site: Path) -> str:
    """Inline the built stylesheet for deterministic, network-free browser QA."""
    page_file = site / "essays" / "typed-generativity.html"
    css_file = site / "style.css"
    html = page_file.read_text(encoding="utf-8")
    css = css_file.read_text(encoding="utf-8")
    if html.count(_STYLESHEET_LINK) != 1:
        raise ValueError("Unexpected Typed Generativity stylesheet reference")
    return html.replace(_STYLESHEET_LINK, "<style>\n" + css + "\n</style>")


def _inspect(page) -> dict:
    """Measure source and alternative visibility, overflow, and arrow geometry."""
    return page.evaluate("""() => {
        const article = document.querySelector(".article-content");
        const sources = [...article.querySelectorAll(
            '.table-scroll[data-tg-alternative="mobile"]')];
        const alternatives = [...article.querySelectorAll(".tg-mobile-records")];
        const hints = [...article.querySelectorAll(".tg-scroll-hint")];
        const visible = el => getComputedStyle(el).display !== "none";
        const displayed = [...sources,...alternatives].filter(visible);
        const sequences = [...article.querySelectorAll(".tg-sequence")].map(group => {
            const nodes = [...group.querySelectorAll("ol > li")];
            const bounds = group.getBoundingClientRect();
            return {
                labels: nodes.map(node => node.textContent.trim()),
                vertical: nodes.slice(1).every((node,i) =>
                    node.getBoundingClientRect().top >
                    nodes[i].getBoundingClientRect().bottom),
                arrows: nodes.slice(0,-1).every((node,i) => {
                    const now = node.getBoundingClientRect();
                    const next = nodes[i+1].getBoundingClientRect();
                    const pseudo = getComputedStyle(node,"::after");
                    const x = now.left + Number.parseFloat(pseudo.left);
                    const y = now.bottom - Number.parseFloat(pseudo.bottom);
                    return pseudo.content.includes("↓") &&
                        Number.isFinite(x) && Number.isFinite(y) &&
                        x > bounds.left && x < bounds.right &&
                        y > now.bottom && y <= next.top + 2;
                }),
                fits: bounds.left >= -1 && bounds.right <= innerWidth + 1,
            };
        });
        return {
            sourceCount: sources.length,
            sourceRows: sources.reduce((sum,e) =>
                sum + e.querySelectorAll("tbody tr").length, 0),
            sourceShown: sources.filter(visible).length,
            alternativesCount: alternatives.length,
            alternativesShown: alternatives.filter(visible).length,
            mobileRows: article.querySelectorAll(".tg-mobile-record").length,
            mobileFields: article.querySelectorAll(".tg-record-field").length,
            hintsShown: hints.filter(visible).length,
            contentOverflow: displayed.filter(e =>
                e.scrollWidth > e.clientWidth + 1).length,
            pageOverflow: document.documentElement.scrollWidth > innerWidth + 1,
            sequences,
        };
    }""")


def _check(width: int, mode: str, observed: dict) -> list[str]:
    """Return informative failures without concealing independent defects."""
    failures: list[str] = []
    prefix = f"{width}px {mode}"
    narrow = width <= 650
    expected_source = 0 if narrow else 15
    expected_alternative = 15 if narrow else 0
    for field, expected in (
        ("sourceCount", 15),
        ("sourceRows", 81),
        ("alternativesCount", 15),
        ("mobileRows", 81),
        ("mobileFields", 227),
        ("sourceShown", expected_source),
        ("alternativesShown", expected_alternative),
    ):
        if observed[field] != expected:
            failures.append(f"{prefix}: {field}={observed[field]}, expected {expected}")
    if observed["pageOverflow"]:
        failures.append(f"{prefix}: full-page horizontal overflow")
    if mode == "print":
        if observed["contentOverflow"]:
            failures.append(
                f"{prefix}: {observed['contentOverflow']} clipped scientific tables/records"
            )
        if observed["hintsShown"]:
            failures.append(f"{prefix}: screen-only table scroll hints appear in print")
    if len(observed["sequences"]) != 2:
        failures.append(f"{prefix}: expected exactly two source sequences")
    else:
        for index, (sequence, expected) in enumerate(
            zip(observed["sequences"], _STAGES, strict=True), start=1
        ):
            if sequence["labels"] != list(expected):
                failures.append(f"{prefix}: sequence {index} changed its source stages")
            for test in ("vertical", "arrows", "fits"):
                if not sequence[test]:
                    failures.append(f"{prefix}: sequence {index} fails {test}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", type=Path, help="Built publication directory")
    parser.add_argument("--screenshots", type=Path, default=None)
    args = parser.parse_args()
    site = args.site.resolve()
    markup = _rendered_page(site)
    screenshots = args.screenshots.resolve() if args.screenshots else None
    if screenshots is not None:
        screenshots.mkdir(parents=True, exist_ok=True)

    failures: list[str] = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        try:
            for width in _WIDTHS:
                context = browser.new_context(
                    viewport={"width": width, "height": 900},
                    device_scale_factor=1,
                    reduced_motion="reduce",
                )
                try:
                    page = context.new_page()
                    page.set_content(markup, wait_until="load")
                    failures.extend(_check(width, "screen", _inspect(page)))
                    if screenshots is not None and width in (320, 1440):
                        for index, sequence in enumerate(
                            page.locator(".tg-sequence").all(), start=1
                        ):
                            sequence.screenshot(
                                path=str(screenshots / f"{width}-typed-sequence-{index}.png")
                            )
                    page.emulate_media(media="print")
                    failures.extend(_check(width, "print", _inspect(page)))
                    if screenshots is not None and width in (320, 1440):
                        selector = (
                            ".tg-mobile-table-5" if width <= 650
                            else '.table-scroll[data-tg-alternative="mobile"]:has(#table-5)'
                        )
                        page.locator(selector).screenshot(
                            path=str(screenshots / f"{width}-typed-print-table-5.png")
                        )
                finally:
                    context.close()
        finally:
            browser.close()
    if failures:
        for message in failures:
            print("FAIL:", message)
        return 1
    print(
        "PASS: Typed Generativity: six screen and print widths, two "
        "directional source sequences, 15 source tables, "
        "81 records and 227 source-exact data fields"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
