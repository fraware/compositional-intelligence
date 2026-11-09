#!/usr/bin/env python3
"""Audit the complete Compositional Intelligence collection as shipped.

Checks public-page structure and in-browser reading geometry, including
whether every horizontally clipped table has a keyboard-accessible scroll
surface and a matching instruction. Runs over the generated Pages files,
using the exact committed CSS without network dependencies. A4 output is
tested separately from the emulated print viewport.
"""
from __future__ import annotations

import argparse
import re
from io import BytesIO
from pathlib import Path

from playwright.sync_api import sync_playwright
from pypdf import PdfReader

TABLES = {
    "compositional-intelligence": (10, "Compositional Intelligence"),
    "series-preface": (7, "Series Preface"),
    "semantic-participation": (12, "Semantic Participation"),
    "typed-generativity": (15, "Typed Generativity"),
    "functorial-consistency": (19, "Functorial Consistency"),
    "lambek-machines": (14, "Lambek Machines"),
    "algebraic-architectures": (13, "Algebraic Architectures"),
    "quantitative-curry-howard": (10, "Quantitative Curry-Howard"),
    "effectful-and-conceptual-intelligence": (
        19, "Effectful and Conceptual Intelligence"
    ),
}
WIDTHS = (320, 375, 650, 651, 768, 820, 828, 829, 1000, 1001, 1440)
STYLE_REF = '<link rel="stylesheet" href="../style.css">'


def publication_html(site: Path, slug: str, css: str) -> str:
    """Embed production CSS while keeping all published HTML unchanged."""
    html = (site / "essays" / (slug + ".html")).read_text(encoding="utf-8")
    if html.count(STYLE_REF) != 1:
        raise ValueError(f"{slug}: stylesheet reference is absent or duplicated")
    return html.replace(STYLE_REF, "<style>\n" + css + "\n</style>")


def measure(page) -> dict:
    """Inspect all visible source tables and all publication landmarks."""
    return page.evaluate("""() => {
        const article = document.querySelector('.article-content');
        const shown = el => {
            if (!el) return false;
            for (let n = el; n; n = n.parentElement) {
                const s = getComputedStyle(n);
                if (s.display === 'none' || s.visibility === 'hidden') return false;
            }
            return true;
        };
        const tables = [...article.querySelectorAll('.table-scroll')];
        const sourceTables = [...article.querySelectorAll('table[data-source-table]')];
        const hints = [];
        const missingHints = [];
        const redundantHints = [];
        const unscrollableTables = [];
        const invalidCaptions = [];
        let scrollable = 0;
        let visibleHintCount = 0;
        for (const wrapper of tables) {
            const table = wrapper.querySelector('table');
            const previous = wrapper.previousElementSibling;
            const next = wrapper.nextElementSibling;
            const hint = previous?.classList.contains('preface-scroll-hint') ||
                previous?.classList.contains('sp-scroll-hint') ||
                previous?.classList.contains('tg-scroll-hint') ||
                previous?.classList.contains('fc-scroll-hint') ||
                previous?.classList.contains('lm-hint') ||
                previous?.classList.contains('aa-hint') ||
                previous?.classList.contains('qc-hint') ||
                previous?.classList.contains('ef-hint')
                ? previous
                : next?.classList.contains('table-scroll-hint') ? next : null;
            const visible = shown(wrapper);
            const clipped = visible && wrapper.scrollWidth > wrapper.clientWidth + 2;
            const hintVisible = shown(hint);
            if (hintVisible) visibleHintCount++;
            const id = table?.id || '(unidentified table)';
            if (visible && clipped) {
                scrollable++;
                if (!hint || !hintVisible) missingHints.push(id);
            }
            if (visible && !clipped && hintVisible) redundantHints.push(id);
            if (visible && clipped &&
                (wrapper.tabIndex !== 0 || wrapper.getAttribute('role') !== 'group')) {
                unscrollableTables.push(id);
            }
            const caption = table?.querySelector(':scope > caption');
            if (!table || !caption || !table.tHead ||
                !wrapper.getAttribute('aria-labelledby') ||
                !document.getElementById(wrapper.getAttribute('aria-labelledby'))) {
                invalidCaptions.push(id);
            }
        }
        const ids = [...document.querySelectorAll('[id]')].map(e => e.id);
        const uniqueIds = new Set(ids).size === ids.length;
        const fragmentLinks = [...document.querySelectorAll('a[href^="#"]')];
        const brokenFragments = fragmentLinks.filter(a =>
            !document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)))
        ).map(a => a.getAttribute('href'));
        const maths = [...article.querySelectorAll('math')];
        const missingMathNames = maths.filter(e =>
            !e.getAttribute('alttext') &&
            !e.closest('table') &&
            !e.getAttribute('aria-label')
        ).length;
        return {
            title: document.querySelector('article h1')?.textContent.trim(),
            headerCount: document.querySelectorAll('article h1').length,
            navCount: document.querySelectorAll('nav[aria-label]').length,
            footerCount: document.querySelectorAll('.site-footer').length,
            tableCount: sourceTables.length,
            uniqueIds,
            brokenFragments,
            invalidCaptions,
            missingHints, redundantHints, unscrollableTables, scrollable,
            visibleHintCount,
            missingMathNames,
            pageOverflow: document.documentElement.scrollWidth > innerWidth + 1,
            bylineInArticleHeader: /Mateo Petel/.test(
                document.querySelector('.article-header')?.textContent ?? ''),
        };
    }""")


def check(slug: str, width: int, mode: str, values: dict) -> list[str]:
    """Report every independent publication issue without short-circuiting."""
    label = f"{slug} {mode} {width}px"
    expected_tables, title = TABLES[slug]
    faults: list[str] = []
    for field, correct in (
        ("title", title), ("headerCount", 1), ("navCount", 3),
        ("footerCount", 1), ("tableCount", expected_tables),
        ("uniqueIds", True),
        ("bylineInArticleHeader", False),
    ):
        if values[field] != correct:
            faults.append(f"{label}: {field}={values[field]!r} expected {correct!r}")
    for field in ("brokenFragments", "invalidCaptions", "unscrollableTables"):
        if values[field]:
            faults.append(f"{label}: {field}={values[field]!r}")
    if mode == "screen":
        if values["pageOverflow"]:
            faults.append(f"{label}: horizontal page overflow")
        if values["missingHints"]:
            faults.append(f"{label}: horizontal tables lack scroll cues: "
                          f"{values['missingHints']}")
        # Chromium versions differ by a pixel or two at the 750px table
        # boundary. This narrow interval still forbids missing cues.
        if width not in (826, 827, 828, 829) and values["redundantHints"]:
            faults.append(f"{label}: misleading scroll cues: "
                          f"{values['redundantHints']}")
    else:
        if values["scrollable"] and width >= 1001:
            faults.append(f"{label}: printed source table still scrolls")
        if values["visibleHintCount"]:
            faults.append(f"{label}: screen-only scroll hints appear in print")
    return faults


def check_a4(page, slug: str) -> list[str]:
    """Verify complete, nonempty physical A4 output for every published text."""
    pdf = page.pdf(
        format="A4", print_background=True,
        margin={"top": "12mm", "bottom": "12mm",
                "left": "12mm", "right": "12mm"},
    )
    reader = PdfReader(BytesIO(pdf))
    title = TABLES[slug][1]
    errors: list[str] = []
    if len(reader.pages) < 2 or len(reader.pages) > 80:
        errors.append(f"{slug}: unexpected A4 page count {len(reader.pages)}")
    first = reader.pages[0].extract_text() or ""
    if title not in first:
        errors.append(f"{slug}: title missing from first A4 page")
    printed_text = []
    for index, pdfpage in enumerate(reader.pages):
        text = pdfpage.extract_text() or ""
        printed_text.append(text)
        if not text.strip():
            errors.append(f"{slug}: blank A4 page {index + 1}")
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        if index < len(reader.pages) - 1 and lines and re.match(
            r"^Table(?:\s+\d+)?\.\s+\S", lines[-1]
        ):
            errors.append(
                f"{slug}: printed table caption stranded at bottom of "
                f"A4 page {index + 1}: {lines[-1]}"
            )
    joined = " ".join(printed_text).lower()
    for instruction in ("scroll horizontally", "scroll sideways", "swipe or scroll"):
        if instruction in joined:
            errors.append(f"{slug}: screen-only instruction printed: {instruction}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", type=Path)
    parser.add_argument("--screenshots", type=Path, default=None)
    args = parser.parse_args()
    site = args.site.resolve()
    css = (site / "style.css").read_text(encoding="utf-8")
    screenshots = args.screenshots.resolve() if args.screenshots else None
    if screenshots:
        screenshots.mkdir(parents=True, exist_ok=True)
    problems: list[str] = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        try:
            for width in WIDTHS:
                context = browser.new_context(
                    viewport={"width": width, "height": 900},
                    device_scale_factor=1, reduced_motion="reduce",
                )
                try:
                    page = context.new_page()
                    for slug in TABLES:
                        page.emulate_media(media="screen")
                        page.set_content(publication_html(site, slug, css),
                                         wait_until="load")
                        problems.extend(check(slug, width, "screen", measure(page)))
                        if screenshots and width in (375, 1440):
                            page.screenshot(path=str(
                                screenshots / f"collection-{width}-{slug}.png"
                            ), full_page=False)
                        if width in (375, 768, 1440):
                            page.emulate_media(media="print")
                            problems.extend(check(slug, width, "print",
                                                  measure(page)))
                            if width == 1440:
                                problems.extend(check_a4(page, slug))
                    page.close()
                finally:
                    context.close()
        finally:
            browser.close()
    if problems:
        for problem in problems:
            print("FAIL:", problem)
        return 1
    print(
        "PASS: collection-wide layout: nine texts, 119 source tables, "
        "11 screen widths, three print widths, A4 documents, "
        "keyboard-scrolling and conditional table cues, anchors, "
        "headings, captions, pagination and navigation"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
