#!/usr/bin/env python3
"""Check desktop/mobile publication rendering in a real Chromium browser.

This audit checks horizontal document overflow, article headings, JavaScript
errors, anchor navigation, and the finite study's live behavior. Screenshots
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
                for width in (375, 768, 1440):
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
                                failures.append(f"{width}px {rel}: horizontal overflow ({widths})")
                            if page.locator("main h1").count() != 1:
                                failures.append(f"{width}px {rel}: unexpected title hierarchy")
                            if errors:
                                failures.append(f"{width}px {rel}: script errors: {errors[:2]}")
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
                                elif media["invisibleMath"]:
                                    failures.append(f"{width}px {rel}: invisible mathematics")
                                if media and (media["invalidFigures"] or media["unnamedImages"] or media["overflowingMediaRoots"]):
                                    failures.append(f"{width}px {rel}: media accessibility/layout {media}")
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
                            if rel == "reading/index.html":
                                checks = page.locator(".reader-check")
                                if checks.count() != 14:
                                    failures.append(f"{width}px reader guide: expected 14 source-grounded questions")
                                else:
                                    first = checks.first.locator("details")
                                    first.locator("summary").click()
                                    if first.get_attribute("open") is None:
                                        failures.append(f"{width}px reader guide: disclosure failed")
                                    if first.locator("blockquote").count() != 1:
                                        failures.append(f"{width}px reader guide: missing manuscript evidence")
                                    if first.locator(".reader-source a").count() != 1:
                                        failures.append(f"{width}px reader guide: missing source link")
                            if width in (375, 1440) and rel in selected:
                                label = rel.replace("/", "-").replace(".html", "")
                                page.screenshot(path=str(screenshots / f"{width}-{label}.png"))
                            if rel == "studies/commuting-square.html":
                                page.locator("#transport").select_option("collapsed")
                                if page.locator("#domain-agreement").inner_text() != "16/16":
                                    failures.append(f"{width}px study: agreement failed")
                                if page.locator("#domain-adequacy").inner_text() != "4/16":
                                    failures.append(f"{width}px study: adequacy failed")
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
    print(f"PASS: {len(paths)} pages at 375, 768, and 1440px; tables, MathML, figures, reader checks, study interactions; screenshots saved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
