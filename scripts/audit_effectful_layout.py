#!/usr/bin/env python3
"""Verify final Effectful essay tables, mobile parity, anchors, and A4 output.

The visual audit compares every native table row to its mobile definition list
at eleven viewport widths and under print media. The manuscript itself is
supplied by the canonical essays/ Markdown source.
"""
from __future__ import annotations

import argparse
from io import BytesIO
from pathlib import Path

from playwright.sync_api import sync_playwright
from pypdf import PdfReader

TABLE_COUNT = 9
WIDTHS = (320, 375, 650, 651, 768, 820, 828, 829, 1000, 1001, 1440)
STYLESHEET = '<link rel="stylesheet" href="../style.css">'


def publication_html(site: Path) -> str:
    """Inline the committed CSS for deterministic, network-free measurement."""
    page = (site / "essays" / "effectful-and-conceptual-intelligence.html").read_text(
        encoding="utf-8"
    )
    css = (site / "style.css").read_text(encoding="utf-8")
    if page.count(STYLESHEET) != 1:
        raise ValueError("Unexpected Effectful stylesheet reference")
    return page.replace(STYLESHEET, "<style>\n" + css + "\n</style>")


def inspect(page) -> dict:
    """Check source-to-mobile text equivalence and computed presentation."""
    return page.evaluate("""() => {
        const root = document.querySelector(".article-content");
        const sources = [...root.querySelectorAll(
            '.table-scroll[data-ef-alternative="mobile"]')];
        const mobiles = [...root.querySelectorAll(".ef-mobile")];
        const isShown = el => {
            for (let node = el; node; node = node.parentElement) {
                const style = getComputedStyle(node);
                if (style.display === "none" || style.visibility === "hidden") return false;
            }
            return true;
        };
        const clean = el => el.textContent.replace(/\\s+/g, " ").trim();
        let matching = sources.length === mobiles.length;
        let rows = 0, fields = 0;
        sources.forEach((group, index) => {
            const table = group.querySelector("table");
            const mobile = mobiles[index];
            const n = index + 1;
            const caption = root.querySelector("#table-" + n + "-caption");
            const headings = [...(table?.querySelectorAll("thead th") ?? [])].map(clean);
            const originals = [...(table?.querySelectorAll("tbody tr") ?? [])];
            const cards = [...(mobile?.querySelectorAll(".ef-card") ?? [])];
            rows += originals.length;
            fields += originals.reduce((s, row) =>
                s + row.querySelectorAll("td").length, 0);
            if (!table || table.id !== "table-" + n ||
                !caption || !caption.classList.contains("ef-caption") ||
                !group.getAttribute("aria-labelledby")?.includes(caption.id) ||
                mobile?.getAttribute("aria-labelledby") !== caption.id ||
                originals.length !== cards.length) matching = false;
            originals.forEach((row, i) => {
                const cells = [...row.querySelectorAll("td")].map(clean);
                const labels = [...cards[i].querySelectorAll("dt")].map(clean);
                const values = [...cards[i].querySelectorAll("dd")].map(clean);
                if (JSON.stringify(cells) !== JSON.stringify(values) ||
                    JSON.stringify(headings) !== JSON.stringify(labels)) matching = false;
            });
        });
        const ids = [...document.querySelectorAll("[id]")].map(el => el.id);
        const anchorIds = new Set(ids);
        return {
            tables: sources.length,
            mobileTables: mobiles.length,
            rows,
            fields,
            sourceShown: sources.filter(isShown).length,
            mobileShown: mobiles.filter(isShown).length,
            captions: root.querySelectorAll(".ef-caption").length,
            anchorCount: ids.length,
            uniqueAnchors: anchorIds.size === ids.length,
            matching,
            pageOverflow: document.documentElement.scrollWidth > innerWidth + 2,
            mobileOverflow: mobiles.filter(isShown).some(el =>
                el.scrollWidth > el.clientWidth + 2),
            title: root.querySelector("h2")?.textContent.trim() || ""
        };
    }""")


def failures(width: int, mode: str, result: dict) -> list[str]:
    """Describe failed parity or responsive-visibility obligations."""
    compact = width <= 650  # Narrow print also uses source-equivalent cards.
    expected_source = 0 if compact else TABLE_COUNT
    expected_mobile = TABLE_COUNT if compact else 0
    issues: list[str] = []
    if result["tables"] != TABLE_COUNT or result["mobileTables"] != TABLE_COUNT:
        issues.append("wrong table inventory")
    if not result["matching"]:
        issues.append("native and mobile table data differ")
    if result["captions"] != TABLE_COUNT:
        issues.append("missing accessible table captions")
    if result["sourceShown"] != expected_source:
        issues.append("incorrect native-table visibility")
    if result["mobileShown"] != expected_mobile:
        issues.append("incorrect mobile-card visibility")
    if not result["uniqueAnchors"]:
        issues.append("duplicate HTML identifiers")
    if result["pageOverflow"] or result["mobileOverflow"]:
        issues.append("horizontal overflow")
    return [f"{mode} {width}px: {issue} ({result})" for issue in issues]


def main() -> int:
    """Audit eleven viewport widths and one printed A4 document."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", type=Path)
    parser.add_argument("--screenshots", type=Path)
    args = parser.parse_args()
    html = publication_html(args.site.resolve())
    screenshots = args.screenshots.resolve() if args.screenshots else None
    if screenshots:
        screenshots.mkdir(parents=True, exist_ok=True)

    problems: list[str] = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        try:
            for width in WIDTHS:
                context = browser.new_context(
                    viewport={"width": width, "height": 900},
                    device_scale_factor=1, reduced_motion="reduce"
                )
                try:
                    page = context.new_page()
                    page.set_content(html, wait_until="load")
                    screen = inspect(page)
                    problems.extend(failures(width, "screen", screen))
                    if screenshots and width in (320, 375, 768, 1440):
                        page.screenshot(
                            path=str(screenshots / f"{width}-effectful-final.png"),
                            full_page=True
                        )
                    page.emulate_media(media="print")
                    problems.extend(failures(width, "print", inspect(page)))
                    if width == 1440:
                        output = PdfReader(BytesIO(page.pdf(
                            format="A4", print_background=True,
                            margin={"top":"12mm","bottom":"12mm",
                                    "left":"12mm","right":"12mm"}
                        )))
                        if not output.pages or not any(
                            "Effectful and Conceptual Intelligence" in (
                                p.extract_text() or ""
                            ) for p in output.pages
                        ):
                            problems.append("A4 output lacks the essay")
                finally:
                    context.close()
        finally:
            browser.close()

    if problems:
        for issue in problems:
            print("FAIL:", issue)
        return 1
    print("PASS: Effectful essay, nine tables, mobile parity and A4 layout")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
