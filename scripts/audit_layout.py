#!/usr/bin/env python3
"""Check desktop/mobile publication rendering in a real Chromium browser.

This audit checks horizontal document overflow, article headings, JavaScript
errors, and anchor navigation. Screenshots
are retained as a separate CI artifact for human visual inspection.
"""

from __future__ import annotations

import argparse
import contextlib
import functools
import http.server
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    """Serve only the generated publication without request log noise."""

    def log_message(self, format: str, *args: object) -> None:
        return


def main() -> int:
    """Fail on measurable browser regressions at desktop and mobile widths."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", type=Path)
    parser.add_argument("--screenshots", type=Path, default=Path("_qa"))
    args = parser.parse_args()
    site = args.site.resolve()
    screenshots = args.screenshots.resolve()
    screenshots.mkdir(parents=True, exist_ok=True)
    if not site.joinpath("index.html").is_file():
        raise FileNotFoundError(f"No generated homepage at {site}")

    handler = functools.partial(QuietHandler, directory=str(site))
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    failures: list[str] = []
    scrollable_tables = 0
    base = f"http://127.0.0.1:{httpd.server_address[1]}/"
    paths = sorted(p.relative_to(site).as_posix() for p in site.rglob("*.html"))
    # Capture every publication page at narrow and wide widths for human review.
    selected = set(paths)

    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            try:
                for width in (320, 375, 768, 1440):
                    context = browser.new_context(
                        viewport={"width": width, "height": 850},
                        device_scale_factor=1,
                        reduced_motion="reduce",
                    )
                    page = context.new_page()
                    errors: list[str] = []
                    page.on("pageerror", lambda error: errors.append(str(error)))
                    try:
                        for rel in paths:
                            errors.clear()
                            response = page.goto(base + rel, wait_until="networkidle")
                            if response is None or response.status != 200:
                                failures.append(f"{width}px {rel}: failed HTTP response")
                                continue
                            page.locator("main h1").first.wait_for()
                            widths = page.evaluate("""() => ({
                                scroll: document.documentElement.scrollWidth,
                                viewport: window.innerWidth
                            })""")
                            if widths["scroll"] > widths["viewport"] + 1:
                                offenders = page.evaluate("""() => [...document.querySelectorAll("body *")]
                                    .filter(e => {
                                        const r = e.getBoundingClientRect();
                                        return r.right > window.innerWidth + 1 && r.width > 0;
                                    })
                                    .slice(0, 8)
                                    .map(e => ({
                                        element: e.tagName.toLowerCase(),
                                        className: typeof e.className === "string" ? e.className : "",
                                        width: Math.round(e.getBoundingClientRect().width),
                                        right: Math.round(e.getBoundingClientRect().right)
                                    }))""")
                                failures.append(f"{width}px {rel}: horizontal overflow ({widths}); elements: {offenders}")
                            if page.locator("main h1").count() != 1:
                                failures.append(f"{width}px {rel}: unexpected title hierarchy")
                            if errors:
                                failures.append(f"{width}px {rel}: script errors: {errors[:2]}")
                            if rel == "index.html" or rel.startswith("essays/"):
                                typography = page.evaluate("""() => ({
                                    display: getComputedStyle(document.querySelector("h1")).fontFamily,
                                    prose: getComputedStyle(document.body).fontFamily,
                                    background: getComputedStyle(document.body).backgroundColor
                                })""")
                                if ("Baskerville" not in typography["display"] or
                                    "Palatino" not in typography["prose"] or
                                    typography["background"] != "rgb(250, 249, 246)"):
                                    failures.append(f"{width}px {rel}: editorial typography regression")
                            if rel.startswith("essays/"):
                                media = page.evaluate("""() => {
                                    const article = document.querySelector(".article-content");
                                    if (!article) return null;
                                    const boxes = [...article.querySelectorAll(
                                        "figure, .table-scroll, .math-scroll, pre, img"
                                    )];
                                    const math = [...article.querySelectorAll("math[display=block]")];
                                    return {
                                        displayMath: math.length,
                                        mathScrolls: article.querySelectorAll(".math-scroll").length,
                                        clippedDisplayMath: [...article.querySelectorAll(".math-scroll")]
                                          .filter(e => e.scrollWidth > e.clientWidth + 2).length,
                                        invalidInlineMath: [...article.querySelectorAll('math[display="inline"]')]
                                          .filter(e => {
                                            const r = e.getBoundingClientRect();
                                            const p = e.closest("p,li,blockquote");
                                            const pr = p ? p.getBoundingClientRect() : null;
                                            return r.width < 4 || r.height < 4 ||
                                              r.width > window.innerWidth + 1 ||
                                              (pr && r.right > pr.right + 4 && !e.closest(".table-scroll"));
                                          }).length,
                                        invisibleMath: math.filter(e => {
                                            const r = e.getBoundingClientRect();
                                            return r.width < 4 || r.height < 4 ||
                                                getComputedStyle(e).visibility === "hidden";
                                        }).length,
                                        invalidFigures: [...article.querySelectorAll("figure")].filter(e => {
                                            const caption = e.querySelector("figcaption");
                                            if (!caption) return true;
                                            return caption.getBoundingClientRect().height < 5;
                                        }).length,
                                        unnamedImages: [...article.querySelectorAll("img")].filter(
                                            e => !e.hasAttribute("alt")).length,
                                        overflowingMediaRoots: boxes.filter(e => {
                                            const r = e.getBoundingClientRect();
                                            return r.left < -2 || r.right > innerWidth + 2;
                                        }).map(e => e.tagName + "." + e.className).slice(0, 4)
                                    };
                                }""")
                                if media is None or media["displayMath"] != media["mathScrolls"]:
                                    failures.append(f"{width}px {rel}: missing MathML scroll wrappers")
                                elif media["invisibleMath"] or media["invalidInlineMath"]:
                                    failures.append(f"{width}px {rel}: clipped or invisible mathematics {media}")
                                if width <= 375 and media and media["clippedDisplayMath"]:
                                    failures.append(f"{width}px {rel}: display formulas require sideways scrolling {media}")
                                if media and (media["invalidFigures"] or media["unnamedImages"] or media["overflowingMediaRoots"]):
                                    failures.append(f"{width}px {rel}: media accessibility/layout {media}")
                                table_structure = page.evaluate("""() => ({
                                    invalid: [...document.querySelectorAll(".article-content .table-scroll")]
                                      .filter(w => {
                                        const t = w.querySelector("table");
                                        const label = w.previousElementSibling;
                                        if (!t || !t.tHead || !t.tBodies.length ||
                                            !t.caption || !t.caption.classList.contains("visually-hidden") ||
                                            !label || !label.classList.contains("table-display-caption") ||
                                            label.id !== w.getAttribute("aria-labelledby")) return true;
                                        const headers = t.tHead.querySelectorAll("th[scope=col]");
                                        const count = Number(w.dataset.columns);
                                        if (!Number.isInteger(count) || count < 1 ||
                                            headers.length < 1 || headers.length > count) return true;
                                        if (t.querySelector("th[ead]")) return true;
                                        if (getComputedStyle(label).display === "none" ||
                                            label.getBoundingClientRect().height < 10) return true;
                                        if (innerWidth <= 375 && count >= 2 &&
                                            t.getBoundingClientRect().width < 550) return true;
                                        return false;
                                      }).length
                                })""")
                                if table_structure["invalid"]:
                                    failures.append(
                                        f"{width}px {rel}: invalid or cramped semantic tables "
                                        f"({table_structure['invalid']})"
                                    )
                                tables = page.locator(".table-scroll")
                                for table in tables.all():
                                    if table.get_attribute("tabindex") != "0" or table.get_attribute("role") != "group":
                                        failures.append(f"{width}px {rel}: inaccessible scroll container")
                                        break
                                if width == 375:
                                    for table in tables.all():
                                        sizing = table.evaluate("(e) => ({scroll: e.scrollWidth, client: e.clientWidth})")
                                        if sizing["scroll"] > sizing["client"] + 1:
                                            scrollable_tables += 1
                                            table.focus()
                                            page.keyboard.press("ArrowRight")
                                            page.wait_for_timeout(150)
                                            moved = table.evaluate("(e) => e.scrollLeft")
                                            if moved <= 0:
                                                failures.append(f"{width}px {rel}: table cannot scroll with keyboard")
                                            break
                            if width in (320, 375, 1440) and rel in selected:
                                label = rel.replace("/", "-").replace(".html", "")
                                # Capture the actual scientific media, not only the article header.
                                if rel.startswith("essays/"):
                                    for index, equation in enumerate(page.locator(".math-scroll").all(), start=1):
                                        equation.screenshot(
                                            path=str(screenshots / f"{width}-{label}-equation-{index:02d}.png")
                                        )
                                    inline_paragraphs = page.locator(
                                        '.article-content p:has(math[display="inline"])'
                                    )
                                    for index, paragraph in enumerate(inline_paragraphs.all()[:3], start=1):
                                        paragraph.screenshot(
                                            path=str(screenshots / f"{width}-{label}-inline-{index:02d}.png")
                                        )
                                    for index, figure in enumerate(page.locator(".article-content figure").all(), start=1):
                                        figure.screenshot(
                                            path=str(screenshots / f"{width}-{label}-figure-{index:02d}.png")
                                        )
                                    first_table = page.locator(".table-scroll").first
                                    if first_table.count():
                                        first_table.evaluate("(e) => { e.scrollLeft = 0; }")
                                        first_table.screenshot(
                                            path=str(screenshots / f"{width}-{label}-table-01.png")
                                        )
                                # Scroll checks and disclosure interactions may alter the viewport.
                                # Capture the actual page top deterministically.
                                page.evaluate("window.scrollTo(0, 0)")
                                page.wait_for_timeout(60)
                                page.screenshot(path=str(screenshots / f"{width}-{label}.png"))
                    finally:
                        context.close()
            finally:
                browser.close()
    finally:
        httpd.shutdown()
        httpd.server_close()
        thread.join(timeout=2)

    if scrollable_tables == 0:
        failures.append("No horizontally scrollable scientific table exercised at mobile width")
    for failure in failures:
        print(f"FAIL: {failure}")
    if failures:
        return 1
    print(f"PASS: {len(paths)} pages at 320, 375, 768, and 1440px; semantic tables, MathML, and figures; screenshots saved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
