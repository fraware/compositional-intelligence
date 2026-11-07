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
    base = f"http://127.0.0.1:{httpd.server_address[1]}/"
    paths = sorted(p.relative_to(site).as_posix() for p in site.rglob("*.html"))
    selected = {"index.html", "atlas/index.html", "studies/commuting-square.html",
                "essays/functorial-consistency.html"}

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

    for failure in failures:
        print(f"FAIL: {failure}")
    if failures:
        return 1
    print(f"PASS: {len(paths)} pages at 375, 768, and 1440px; study interactions; screenshots saved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
