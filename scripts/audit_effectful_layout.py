#!/usr/bin/env python3
"""Audit Effectful and Conceptual Intelligence in screen and print layouts.

Verify source-derived tables, accessible captions, MathML, sequence direction,
responsive scroll guidance and printable reading-column bounds.
The authoritative manuscript and its source-bound renderer remain unchanged.
"""
from __future__ import annotations

import argparse
from io import BytesIO
from pathlib import Path

from playwright.sync_api import sync_playwright
from pypdf import PdfReader

from render_effectful import CAPTIONS

WIDTHS = (320, 375, 650, 651, 768, 820, 828, 829, 1000, 1001, 1440)
STAGES = ("membership", "generation", "transformation", "language",
          "architecture", "warrant", "action")
STYLESHEET = '<link rel="stylesheet" href="../style.css">'


def publication_html(site: Path) -> str:
    """Inline the published CSS for a deterministic network-free browser audit."""
    html = (site / "essays" / "effectful-and-conceptual-intelligence.html").read_text(
        encoding="utf-8"
    )
    css = (site / "style.css").read_text(encoding="utf-8")
    if html.count(STYLESHEET) != 1:
        raise ValueError("Unexpected Effectful stylesheet reference")
    return html.replace(STYLESHEET, "<style>\n" + css + "\n</style>")


def inspect(page) -> dict:
    """Measure visibility, table inventories and browser-computed geometry."""
    return page.evaluate("""() => {
        const root = document.querySelector('.article-content');
        const source = [...root.querySelectorAll(
            '.table-scroll[data-ef-alternative="mobile"]')];
        const mobile = [...root.querySelectorAll('.ef-mobile')];
        const hints = [...root.querySelectorAll('.ef-hint')];
        const sequence = [...root.querySelectorAll('.ef-sequence ol > li')];
        const math = [...root.querySelectorAll('.ef-math')];
        const shown = el => getComputedStyle(el).display !== 'none';
        const nativeOverflow = source.filter(shown).flatMap(el => {
            const table = el.querySelector('table');
            const box = el.getBoundingClientRect();
            const inner = table.getBoundingClientRect();
            if (inner.right > box.right + 2 || inner.width > box.width + 2 ||
                table.scrollWidth > table.clientWidth + 2 ||
                el.scrollWidth > el.clientWidth + 2) return [table.id];
            return [];
        });
        const stageArrows = sequence.slice(0,-1).every((el,i) => {
            const arrow = getComputedStyle(el, '::after');
            const now = el.getBoundingClientRect();
            const next = sequence[i+1].getBoundingClientRect();
            const y = now.bottom - Number.parseFloat(arrow.bottom);
            return arrow.content.includes('↓') &&
                Number.isFinite(y) && y > now.bottom && y <= next.top + 3;
        });
        const sourceCaps = source.every((el,i) => {
            const n = i+1;
            const label = root.querySelector('#table-' + n + '-caption');
            const caption = el.querySelector('table > caption');
            return label && label.textContent.startsWith('Table ' + n + '.') &&
                label.classList.contains('ef-caption') &&
                caption && caption.textContent === label.textContent &&
                el.getAttribute('aria-labelledby') === label.id;
        });
        const mathFits = math.every(el => {
            const node = el.querySelector('math');
            const box = el.getBoundingClientRect();
            const inner = node?.getBoundingClientRect();
            return inner && node.getAttribute('alttext') &&
                inner.width > 4 && inner.left >= box.left-2 &&
                inner.right <= box.right+2 &&
                box.left >= -2 && box.right <= innerWidth+2;
        });
        return {
            sourceCount: source.length,
            sourceRows: source.reduce((s,el) =>
                s + el.querySelectorAll('tbody tr').length, 0),
            sourceCells: source.reduce((s,el) =>
                s + el.querySelectorAll('tbody td').length, 0),
            sourceShown: source.filter(shown).length,
            mobileCount: mobile.length,
            mobileShown: mobile.filter(shown).length,
            mobileCards: root.querySelectorAll('.ef-card').length,
            mobileFields: root.querySelectorAll('.ef-field').length,
            hintShown: hints.filter(shown).length,
            screenScroll: source.filter(shown).filter(el =>
                el.scrollWidth > el.clientWidth).length,
            sourceCaps,
            stages: sequence.map(el => el.textContent.trim()),
            stageArrows,
            mathCount: math.length,
            mathFits,
            notesCount: root.querySelectorAll('.ef-source-notes > li').length,
            nativeOverflow,
            mobileOverflow: mobile.filter(shown).filter(el =>
                el.scrollWidth > el.clientWidth + 1).length,
            printCaptionsStayWithTables: [...root.querySelectorAll('.ef-caption')]
                .every(el => ['avoid','avoid-page'].includes(
                    getComputedStyle(el).breakAfter)),
            printNotesStayTogether: ['avoid','avoid-page'].includes(
                getComputedStyle(root.querySelector('.ef-source-notes')).breakInside),
            pageOverflow: document.documentElement.scrollWidth > innerWidth + 1,
        };
    }""")


def failures(width: int, mode: str, actual: dict) -> list[str]:
    """Report individual presentation or fidelity defects."""
    label = f"{mode} at {width}px"
    compact = width <= 650
    scroll_cues = 5 if mode == "screen" and 651 <= width <= 828 else 0
    expected = {
        "sourceCount": 19, "sourceRows": 154, "sourceCells": 342,
        "sourceShown": 0 if compact else 19,
        "mobileCount": 19, "mobileShown": 19 if compact else 0,
        "mobileCards": 154, "mobileFields": 342,
        "hintShown": scroll_cues,
        "mathCount": 7, "notesCount": 5,
    }
    issues = [
        f"{label}: {key}={actual[key]} expected {want}"
        for key, want in expected.items() if actual[key] != want
    ]
    if actual["stages"] != list(STAGES):
        issues.append(f"{label}: source sequence changed")
    for field in ("stageArrows", "sourceCaps", "mathFits"):
        if not actual[field]:
            issues.append(f"{label}: {field} failed")
    if actual["mobileOverflow"] or actual["pageOverflow"]:
        issues.append(f"{label}: mobile records or page overflow")
    if mode == "print" and actual["nativeOverflow"]:
        issues.append(
            f"{label}: printed source tables exceed the reading column: "
            f"{actual['nativeOverflow']}"
        )
    if mode == "print" and not actual["printCaptionsStayWithTables"]:
        issues.append(f"{label}: table caption print-pagination policy missing")
    if mode == "print" and not actual["printNotesStayTogether"]:
        issues.append(f"{label}: source notes print-pagination policy missing")
    if mode == "screen" and actual["screenScroll"] != scroll_cues:
        issues.append(f"{label}: scroll guidance does not match table overflow")
    return issues



def audit_a4_document(page) -> list[str]:
    """Verify A4 PDF pages keep every original table caption with its data.

    Viewport bounds do not establish page-break fidelity. Render an A4 document
    and inspect its extracted page text, without depending on a fixed page count.
    """
    pdf = page.pdf(
        format="A4",
        print_background=True,
        margin={"top": "12mm", "bottom": "12mm", "left": "12mm", "right": "12mm"},
    )
    reader = PdfReader(BytesIO(pdf))
    pages = [" ".join((p.extract_text() or "").split()) for p in reader.pages]
    issues: list[str] = []
    if not 1 <= len(pages) <= 60:
        issues.append(f"A4: unexpected number of print pages ({len(pages)})")

    for number, caption in CAPTIONS.items():
        occurrences = [i for i, text in enumerate(pages) if caption in text]
        if len(occurrences) != 1:
            issues.append(
                f"A4: Table {number} has {len(occurrences)} caption occurrences"
            )
            continue
        page_index = occurrences[0]
        following = pages[page_index].split(caption, 1)[1].strip()
        if len(following) < 25:
            issues.append(
                f"A4: Table {number} caption is stranded on page {page_index + 1}"
            )

    notes_title = "Appendix E. Source-use notes"
    note_pages = [i for i, text in enumerate(pages) if notes_title in text]
    note_starts = (
        "Hoare logic, PDDL, monads, algebraic effects",
        "ReAct and Toolformer support the context",
        "WebArena, OSWorld, tau-bench, AgentDojo",
        "Security sources support prompt-injection and",
        "Conceptual-transfer records are proposed as a",
    )
    if len(note_pages) != 1:
        issues.append("A4: Appendix E heading is absent or duplicated")
    else:
        note_text = pages[note_pages[0]]
        for fragment in note_starts:
            if fragment not in note_text:
                issues.append(
                    f"A4: source-use note separated from its appendix: {fragment}"
                )
    return issues


def main() -> int:
    """Audit 11 responsive widths in both media modes."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", type=Path)
    parser.add_argument("--screenshots", type=Path, default=None)
    args = parser.parse_args()
    markup = publication_html(args.site.resolve())
    screenshots = args.screenshots.resolve() if args.screenshots else None
    if screenshots:
        screenshots.mkdir(parents=True, exist_ok=True)

    issues: list[str] = []
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
                    issues.extend(failures(width, "screen", inspect(page)))
                    if screenshots and width in (320, 375, 768, 1440):
                        page.locator(".ef-math-1").screenshot(path=str(
                            screenshots / f"{width}-effectful-action-judgment.png"
                        ))
                    page.emulate_media(media="print")
                    issues.extend(failures(width, "print", inspect(page)))
                    if width == 1440:
                        issues.extend(audit_a4_document(page))
                    if screenshots and width in (320, 1000, 1001, 1440):
                        selector = (
                            ".ef-mobile-1" if width <= 650 else
                            '.table-scroll[data-ef-alternative="mobile"]:has(#table-1)'
                        )
                        page.locator(selector).screenshot(path=str(
                            screenshots / f"{width}-effectful-print-table-1.png"
                        ))
                finally:
                    context.close()
        finally:
            browser.close()
    if issues:
        for issue in issues:
            print("FAIL:", issue)
        return 1
    print(
        "PASS: Effectful and Conceptual Intelligence: 11 screen/print widths, "
        "19 source tables, 154 records, 342 fields, 7 judgments, 5 source notes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
