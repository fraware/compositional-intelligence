#!/usr/bin/env python3
"""Check Quantitative Curry-Howard screen and print publication fidelity.

The source-bound renderer retains ten native tables and their complete
source-derived mobile alternatives. This browser audit verifies their
exclusive visibility, the eight-stage sequential diagram, and responsive
record layout at both sides of the breakpoint.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from playwright.sync_api import sync_playwright

WIDTHS = (320, 375, 650, 651, 768, 1000, 1001, 1440)
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
STYLESHEET_LINK = '<link rel="stylesheet" href="../style.css">'


def inline_publication_styles(site: Path) -> str:
    """Load the generated page with its exact committed CSS, without networking."""
    page = (site / "essays" / "quantitative-curry-howard.html").read_text(
        encoding="utf-8"
    )
    style = (site / "style.css").read_text(encoding="utf-8")
    if page.count(STYLESHEET_LINK) != 1:
        raise ValueError("Unexpected Quantitative Curry-Howard stylesheet link")
    return page.replace(STYLESHEET_LINK, "<style>\n" + style + "\n</style>")


def inspect(page) -> dict:
    """Return measurements from the browser's computed styles and geometry."""
    return page.evaluate("""() => {
        const article = document.querySelector(".article-content");
        const sources = [...article.querySelectorAll(
            '.table-scroll[data-qc-alternative="mobile"]')];
        const alternatives = [...article.querySelectorAll(".qc-mobile")];
        const hints = [...article.querySelectorAll(".qc-hint")];
        const pipeline = article.querySelector(".qc-pipeline");
        const steps = [...(pipeline?.querySelectorAll("ol > li") ?? [])];
        const schema = [...article.querySelectorAll(".qc-schema")];
        const exampleLabels = [...article.querySelectorAll(".qc-example-field dt")];
        const shown = e => getComputedStyle(e).display !== "none";
        const displays = [...sources, ...alternatives].filter(shown);
        const bounds = pipeline?.getBoundingClientRect();
        const math = [...article.querySelectorAll(".qc-math math")];
        return {
            sourceCount: sources.length,
            sourceRows: sources.reduce((sum,el) =>
                sum + el.querySelectorAll("tbody tr").length, 0),
            sourceCells: sources.reduce((sum,el) =>
                sum + el.querySelectorAll("tbody td").length, 0),
            sourceShown: sources.filter(shown).length,
            mobileCount: alternatives.length,
            mobileShown: alternatives.filter(shown).length,
            mobileRows: article.querySelectorAll(".qc-card").length,
            mobileFields: article.querySelectorAll(".qc-field").length,
            hintShown: hints.filter(shown).length,
            pipelineText: steps.map(el => el.textContent.trim()),
            sequenceVertical: steps.slice(1).every((el,i) =>
                el.getBoundingClientRect().top >
                steps[i].getBoundingClientRect().bottom),
            sequenceArrows: steps.slice(0,-1).every(el =>
                getComputedStyle(el, "::after").content.includes("↓")),
            sequenceFits: !!bounds && bounds.left >= -1 &&
                bounds.right <= innerWidth + 1,
            mathFits: math.length === 3 && math.every(el => {
                const rect = el.getBoundingClientRect();
                return rect.width > 0 && rect.left >= -1 &&
                    rect.right <= innerWidth + 1;
            }),
            schemaCount: schema.length,
            schemaLines: article.querySelectorAll(".qc-schema-line").length,
            exampleLabelWraps: exampleLabels.filter(el => {
                const height = el.getBoundingClientRect().height;
                const oneLine = Number.parseFloat(getComputedStyle(el).lineHeight);
                return height > oneLine * 1.25;
            }).map(el => el.textContent.trim()),
            schemaHeight: schema[0]?.getBoundingClientRect().height ?? 0,
            schemaOverflow: schema.filter(el =>
                el.scrollWidth > el.clientWidth + 1).length,
            visibleRecordOverflow: displays.filter(el =>
                el.classList.contains("qc-mobile") &&
                el.scrollWidth > el.clientWidth + 1).length,
            nativePrintOverflow: sources.filter(shown).flatMap(el => {
                const table = el.querySelector("table");
                const outer = el.getBoundingClientRect();
                const inner = table?.getBoundingClientRect();
                if (!inner || inner.width > outer.width + 2 ||
                    inner.right > outer.right + 2 ||
                    table.scrollWidth > table.clientWidth + 2 ||
                    el.scrollWidth > el.clientWidth + 2) {
                    return [table?.id ?? "missing-table"];
                }
                return [];
            }),
            pageOverflow: document.documentElement.scrollWidth > innerWidth + 1,
        };
    }""")


def check(width: int, mode: str, result: dict) -> list[str]:
    """Report independent failures without masking earlier failures."""
    errors: list[str] = []
    compact = width <= (1000 if mode == "print" else 650)
    label = f"{mode} at {width}px"
    expected_source = 0 if compact else 10
    expected_mobile = 10 if compact else 0
    expected_hints = 7 if mode == "screen" and width > 650 else 0
    for field, expected in (
        ("sourceCount", 10),
        ("sourceRows", 64),
        ("sourceCells", 179),
        ("sourceShown", expected_source),
        ("mobileCount", 10),
        ("mobileShown", expected_mobile),
        ("mobileRows", 64),
        ("mobileFields", 179),
        ("hintShown", expected_hints),
        ("schemaCount", 2),
        ("schemaLines", 31),
    ):
        if result[field] != expected:
            errors.append(
                f"{label}: {field}={result[field]}, expected {expected}"
            )
    if result["pipelineText"] != list(PIPELINE):
        errors.append(f"{label}: eight authored steps or their order changed")
    for field in (
        "sequenceVertical", "sequenceArrows", "sequenceFits", "mathFits"
    ):
        if not result[field]:
            errors.append(f"{label}: {field} failed")
    if result["exampleLabelWraps"]:
        errors.append(
            f"{label}: source symbols wrap in example labels "
            f"{result['exampleLabelWraps']}"
        )
    if width <= 375 and result["schemaHeight"] > 1500:
        errors.append(
            f"{label}: first appendix record consumes "
            f"{result['schemaHeight']:.0f}px of vertical reading space"
        )
    if result["schemaOverflow"] or result["visibleRecordOverflow"]:
        errors.append(f"{label}: schema or mobile records overflow their bounds")
    if result["pageOverflow"]:
        errors.append(f"{label}: document overflows the viewport")
    if mode == "print" and result["hintShown"]:
        errors.append(f"{label}: screen-only scroll hint leaked into print")
    if mode == "print" and result["nativePrintOverflow"]:
        errors.append(
            f"{label}: native source tables exceed their printable reading column "
            f"{result['nativePrintOverflow']}"
        )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", type=Path, help="Built publication directory")
    parser.add_argument("--screenshots", type=Path, default=None)
    args = parser.parse_args()
    markup = inline_publication_styles(args.site.resolve())
    screenshots = args.screenshots.resolve() if args.screenshots else None
    if screenshots is not None:
        screenshots.mkdir(parents=True, exist_ok=True)

    errors: list[str] = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        try:
            for width in WIDTHS:
                context = browser.new_context(
                    viewport={"width": width, "height": 900},
                    device_scale_factor=1,
                    reduced_motion="reduce",
                )
                try:
                    page = context.new_page()
                    page.set_content(markup, wait_until="load")
                    errors.extend(check(width, "screen", inspect(page)))
                    if screenshots is not None and width in (320, 1440):
                        page.locator(".qc-pipeline").screenshot(
                            path=str(screenshots / f"{width}-qch-pipeline.png")
                        )
                        page.locator(".qc-schema").first.screenshot(
                            path=str(screenshots / f"{width}-qch-schema.png")
                        )
                    page.emulate_media(media="print")
                    errors.extend(check(width, "print", inspect(page)))
                    if screenshots is not None and width in (320, 1000, 1001, 1440):
                        target = (
                            ".qc-mobile-5" if width <= 1000 else
                            '.table-scroll[data-qc-alternative="mobile"]:has(#table-5)'
                        )
                        page.locator(target).screenshot(
                            path=str(screenshots / f"{width}-qch-print-table-5.png")
                        )
                finally:
                    context.close()
        finally:
            browser.close()
    if errors:
        for error in errors:
            print("FAIL:", error)
        return 1
    print(
        "PASS: Quantitative Curry-Howard: eight screen and print widths, "
        "eight source-ordered steps, 10 native tables, "
        "64 mobile records and 179 data fields"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
