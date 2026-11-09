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
                                if page.locator(".article-header .byline").count():
                                    failures.append(f"{width}px {rel}: author byline appears beneath essay title")
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
                                        detachedMathPunctuation: [...article.querySelectorAll(".math-scroll")]
                                          .filter(e => [...e.childNodes].some(node =>
                                            node.nodeType === 3 && node.textContent.trim() === ".")).length,
                                        malformedDisplayMath: [...article.querySelectorAll(".math-scroll")]
                                          .filter(e => e.querySelectorAll('math[display="block"]').length !== 1 ||
                                            !e.querySelector(".math-display-expression")).length,
                                        invalidInlineMath: [...article.querySelectorAll('math[display="inline"]')]
                                          .filter(e => {
                                            const sourceSquare = e.closest(".ci-commuting .table-scroll");
                                            if (sourceSquare && getComputedStyle(sourceSquare).display === "none") {
                                              return false;
                                            }
                                             const alternate = e.closest(
                                               ".preface-mobile-records, .table-scroll[data-preface-alternative='mobile'], .sp-mobile-records, .table-scroll[data-sp-alternative='mobile'], .tg-mobile-records, .table-scroll[data-tg-alternative='mobile'], .fc-mobile-records, .table-scroll[data-fc-alternative='mobile']"
                                             );
                                             if (alternate && getComputedStyle(alternate).display === "none") {
                                               return false;
                                             }
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
                                elif (media["invisibleMath"] or media["invalidInlineMath"] or
                                      media["detachedMathPunctuation"] or media["malformedDisplayMath"]):
                                    failures.append(f"{width}px {rel}: malformed or invisible mathematics {media}")
                                # Wide formulas are intentionally scrollable. Assert
                                # keyboard operability instead of rejecting valid math.
                                if width == 375 and media and media["clippedDisplayMath"]:
                                    for equation in page.locator(".math-scroll").all():
                                        size = equation.evaluate("(e) => ({scroll:e.scrollWidth, client:e.clientWidth})")
                                        if size["scroll"] > size["client"] + 2:
                                            equation.evaluate("(e) => { e.scrollLeft = 0; }")
                                            equation.focus()
                                            page.keyboard.press("ArrowRight")
                                            page.wait_for_timeout(180)
                                            if equation.evaluate("(e) => e.scrollLeft") <= 0:
                                                failures.append(f"{width}px {rel}: formula cannot scroll with keyboard")
                                            break
                                if media and (media["invalidFigures"] or media["unnamedImages"] or media["overflowingMediaRoots"]):
                                    failures.append(f"{width}px {rel}: media accessibility/layout {media}")
                                if rel == "essays/compositional-intelligence.html":
                                    square = page.evaluate("""() => {
                                        const source = document.querySelector(".ci-commuting .table-scroll");
                                        const mobile = document.querySelector(".ci-commuting-mobile");
                                        const grid = mobile?.querySelector(".ci-commuting-mobile-grid");
                                        if (!source || !mobile || !grid) return null;
                                        const bounds = grid.getBoundingClientRect();
                                        return {
                                            sourceVisible: getComputedStyle(source).display !== "none",
                                            mobileVisible: getComputedStyle(mobile).display !== "none",
                                            objects: grid.querySelectorAll(".ci-square-object").length,
                                            arrows: grid.querySelectorAll(".ci-square-arrow").length,
                                            withinViewport: bounds.left >= -1 &&
                                                bounds.right <= innerWidth + 1
                                        };
                                    }""")
                                    if (square is None or square["objects"] != 4 or
                                        square["arrows"] != 4 or not square["withinViewport"] or
                                        (width <= 650 and
                                         (not square["mobileVisible"] or square["sourceVisible"])) or
                                        (width > 650 and
                                         (square["mobileVisible"] or not square["sourceVisible"]))):
                                        failures.append(f"{width}px {rel}: inadequate mobile commuting square {square}")
                                if rel == "essays/compositional-intelligence.html":
                                    cues = page.evaluate("""() => {
                                        const wrappers = [...document.querySelectorAll(
                                            ".article-content .table-scroll"
                                        )].filter(w => w.querySelector("table")?.id !== "table-5");
                                        return {
                                            count: wrappers.length,
                                            invalid: wrappers.filter(w => {
                                                const hint = w.nextElementSibling;
                                                if (!hint || !hint.classList.contains("table-scroll-hint") ||
                                                    w.getAttribute("aria-describedby") !== hint.id ||
                                                    !hint.textContent.includes("all columns")) return true;
                                                const visible = getComputedStyle(hint).display !== "none" &&
                                                    hint.getBoundingClientRect().height >= 10;
                                                return innerWidth <= 650 ? !visible : visible;
                                            }).length
                                        };
                                    }""")
                                    if cues["count"] != 9 or cues["invalid"]:
                                        failures.append(
                                            f"{width}px {rel}: unusable table scroll instructions {cues}"
                                        )
                                if rel == "essays/series-preface.html":
                                    preface = page.evaluate("""() => {
                                        const article = document.querySelector(".article-content");
                                        const lifecycle = article?.querySelector(".preface-lifecycle");
                                        const wrappers = [...article.querySelectorAll(".table-scroll")];
                                        const mobile = [...article.querySelectorAll(".preface-mobile-records")];
                                        const compact = wrappers.filter(w => w.dataset.prefaceAlternative === "mobile");
                                        const linked = wrappers[0]?.querySelectorAll('tbody tr td:nth-child(2) a');
                                        const cues = wrappers.map(w => {
                                            const hint = w.previousElementSibling;
                                            return {
                                                exists: !!hint && hint.classList.contains("preface-scroll-hint") &&
                                                    hint.id === w.getAttribute("aria-describedby"),
                                                visible: !!hint && getComputedStyle(hint).display !== "none" &&
                                                    hint.getBoundingClientRect().height >= 10
                                            };
                                        });
                                        const cards = mobile.reduce((n, e) => n +
                                            e.querySelectorAll(".preface-mobile-record").length, 0);
                                        const mobileDisplayed = mobile.filter(e =>
                                            getComputedStyle(e).display !== "none").length;
                                        const nativeDisplayed = compact.filter(e =>
                                            getComputedStyle(e).display !== "none").length;
                                        const bounds = lifecycle?.getBoundingClientRect();
                                        const dts = [...article.querySelectorAll(".preface-mobile-records dt")];
                                        const accessibleClipped = dts.filter(e => {
                                            const st = getComputedStyle(e);
                                            return st.position === "absolute" &&
                                                st.clipPath === "inset(50%)" &&
                                                st.display !== "none";
                                        }).length;
                                        const mobileBounds = mobile.flatMap(sec =>
                                            [...sec.querySelectorAll(".preface-mobile-record")]
                                            .filter(e => getComputedStyle(sec).display !== "none")
                                            .map(e => e.getBoundingClientRect())
                                        );
                                        return {
                                            sourceTableNumbers: wrappers.map(w =>
                                                Number(w.querySelector("table")?.dataset.sourceTable)),
                                            rowCounts: mobile.map(sec =>
                                                sec.querySelectorAll(".preface-mobile-record").length),
                                            mobileLinks: mobile[0]?.querySelectorAll('a[href]').length,
                                            clippedFieldLabels: accessibleClipped,
                                            outOfBoundsRecords: mobileBounds.filter(b =>
                                                b.left < -1 || b.right > innerWidth + 1).length,
                                            stages: lifecycle?.querySelectorAll("li").length ?? 0,
                                            lifecycleFits: !!bounds && bounds.left >= -1 &&
                                                bounds.right <= innerWidth + 1,
                                            tables: wrappers.length,
                                            linkedDocuments: linked?.length ?? 0,
                                            cards, mobileDisplayed, nativeDisplayed,
                                            cuesValid: cues.every(v => v.exists),
                                            cuesVisible: cues.filter(v => v.visible).length,
                                            expectedCues: innerWidth <= 650 ? 0 :
                                                innerWidth <= 900 ? 7 : 0
                                        };
                                    }""")
                                    if (preface["stages"] != 8 or not preface["lifecycleFits"] or
                                        preface["tables"] != 7 or preface["linkedDocuments"] != 9 or
                                        str(preface["sourceTableNumbers"]) != "[1, 2, 3, 4, 5, 6, 7]" or
                                        str(preface["rowCounts"]) != "[10, 3, 8, 5, 6, 5, 7]" or
                                        preface["mobileLinks"] != 9 or
                                        preface["outOfBoundsRecords"] != 0 or
                                        preface["clippedFieldLabels"] != (78 if width <= 650 else 0) or
                                        preface["cards"] != 44 or not preface["cuesValid"] or
                                        preface["cuesVisible"] != preface["expectedCues"] or
                                        (width <= 650 and
                                         (preface["mobileDisplayed"] != 7 or
                                          preface["nativeDisplayed"] != 0)) or
                                        (width > 650 and
                                         (preface["mobileDisplayed"] != 0 or
                                          preface["nativeDisplayed"] != 7))):
                                        failures.append(f"{width}px {rel}: preface reading regression {preface}")
                                if rel == "essays/semantic-participation.html":
                                    semantic = page.evaluate("""() => {
                                        const article = document.querySelector(".article-content");
                                        const source = [...article.querySelectorAll(
                                            ".table-scroll[data-sp-alternative='mobile']"
                                        )];
                                        const mobile = [...article.querySelectorAll(
                                            ".sp-mobile-records"
                                        )];
                                        const cards = [...article.querySelectorAll(
                                            ".sp-mobile-record"
                                        )];
                                        const fields = [...article.querySelectorAll(
                                            ".sp-record-field"
                                        )];
                                        const visibleMobile = mobile.filter(e =>
                                            getComputedStyle(e).display !== "none").length;
                                        const visibleSource = source.filter(e =>
                                            getComputedStyle(e).display !== "none").length;
                                        const bounds = cards.filter(e =>
                                            getComputedStyle(e.closest(".sp-mobile-records")).display !== "none"
                                        ).map(e => e.getBoundingClientRect());
                                        const hints = [...article.querySelectorAll(".sp-scroll-hint")];
                                        const badHints = hints.filter(h =>
                                            !h.nextElementSibling?.classList.contains("table-scroll") ||
                                            h.nextElementSibling?.getAttribute("aria-describedby") !== h.id
                                        ).length;
                                        const sourceIds = source.map(w =>
                                            Number(w.querySelector("table")?.dataset.sourceTable));
                                        const observedRows = mobile.map(e =>
                                            e.querySelectorAll(".sp-mobile-record").length);
                                        const environment = [...article.querySelectorAll(
                                            ".sp-environment-schema .sp-schema-entry"
                                        )];
                                        const governingLabel = article.querySelector(
                                            ".sp-mobile-table-3 .sp-record-field dt"
                                        );
                                        const labelStyle = governingLabel ?
                                            getComputedStyle(governingLabel) : null;
                                        const compactGoverningLabel = !!labelStyle &&
                                            labelStyle.display !== "none" &&
                                            labelStyle.position === "absolute" &&
                                            labelStyle.clipPath === "inset(50%)";
                                        const table3Caption = source[2]?.querySelector(
                                            "caption"
                                        )?.textContent.trim();
                                        return {
                                            tableCount: source.length,
                                            sourceIds, observedRows,
                                            environmentFields: environment.length,
                                            environmentOverflows: environment.filter(e => {
                                                const rect = e.getBoundingClientRect();
                                                return rect.left < -1 || rect.right > innerWidth + 1;
                                            }).length,
                                            compactGoverningLabel,
                                            table3Caption,
                                            readerPathLinks: source[1]?.querySelectorAll(
                                                'tbody tr td:nth-child(2) a[href^="#"]').length ?? 0,
                                            mobilePathLinks: mobile[1]?.querySelectorAll(
                                                'a[href^="#"]').length ?? 0,
                                            mobileCount: mobile.length,
                                            cards: cards.length,
                                            fields: fields.length,
                                            visibleMobile, visibleSource,
                                            badHints,
                                            outOfBounds: bounds.filter(b =>
                                                b.left < -1 || b.right > innerWidth + 1).length,
                                            sequence: article.querySelectorAll(".sp-sequence li").length,
                                            schemas: article.querySelectorAll(".sp-source-schema").length,
                                            proofExamples: article.querySelectorAll(".sp-proof-example").length,
                                            transitionHeadings: article.querySelectorAll(
                                                ".sp-transition-head").length,
                                            transitionCards: article.querySelectorAll(
                                                ".sp-transition-record").length
                                        };
                                    }""")
                                    if (semantic["tableCount"] != 12 or semantic["mobileCount"] != 12 or
                                        semantic["cards"] != 74 or semantic["fields"] != 190 or
                                        semantic["readerPathLinks"] != 22 or
                                        semantic["mobilePathLinks"] != 22 or
                                        semantic["sourceIds"] != list(range(1, 13)) or
                                        semantic["observedRows"] != [6, 5, 1, 5, 7, 13, 8, 4, 5, 7, 7, 6] or
                                        semantic["badHints"] or semantic["outOfBounds"] or
                                        semantic["sequence"] != 7 or semantic["schemas"] != 4 or
                                        semantic["environmentFields"] != 10 or
                                        semantic["environmentOverflows"] != 0 or
                                        semantic["table3Caption"] != "Table 3. Governing claim for semantic artifact membership." or
                                        (width <= 650 and not semantic["compactGoverningLabel"]) or
                                        semantic["proofExamples"] != 1 or
                                        semantic["transitionHeadings"] != 1 or
                                        semantic["transitionCards"] != 4 or
                                        (width <= 650 and
                                         (semantic["visibleMobile"] != 12 or semantic["visibleSource"] != 0)) or
                                        (width > 650 and
                                         (semantic["visibleMobile"] != 0 or semantic["visibleSource"] != 12))):
                                        failures.append(
                                            f"{width}px {rel}: invalid semantic participation reading layout {semantic}"
                                        )
                                if rel == "essays/typed-generativity.html":
                                    typed = page.evaluate("""() => {
                                        const article = document.querySelector(".article-content");
                                        const source = [...article.querySelectorAll(
                                            ".table-scroll[data-tg-alternative='mobile']"
                                        )];
                                        const mobile = [...article.querySelectorAll(".tg-mobile-records")];
                                        const records = [...article.querySelectorAll(".tg-mobile-record")];
                                        const fields = [...article.querySelectorAll(".tg-record-field")];
                                        const cues = [...article.querySelectorAll(".tg-scroll-hint")];
                                        const bounds = records.filter(r =>
                                            getComputedStyle(r.closest(".tg-mobile-records")).display !== "none"
                                        ).map(r => r.getBoundingClientRect());
                                        const sourceVisible = source.filter(e =>
                                            getComputedStyle(e).display !== "none").length;
                                        const mobileVisible = mobile.filter(e =>
                                            getComputedStyle(e).display !== "none").length;
                                        const scrollHintsVisible = cues.filter(e =>
                                            getComputedStyle(e).display !== "none").length;
                                        const badCues = cues.filter(e =>
                                            !e.nextElementSibling?.classList.contains("table-scroll") ||
                                            e.nextElementSibling?.getAttribute("aria-describedby") !== e.id
                                        ).length;
                                        const originalPaths = source[1]?.querySelectorAll(
                                            'tbody tr td:nth-child(2) a[href^="#"]'
                                        ).length ?? 0;
                                        const mobilePaths = mobile[1]?.querySelectorAll(
                                            'a[href^="#"]'
                                        ).length ?? 0;
                                        const symbolSource = [...(source[2]?.querySelectorAll(
                                            'tbody tr td:first-child math[alttext]') ?? []
                                        )].map(m => m.getAttribute("alttext"));
                                        const symbolMobile = [...(mobile[2]?.querySelectorAll(
                                            '.tg-record-field:first-child dd math[alttext]') ?? []
                                        )].map(m => m.getAttribute("alttext"));
                                        const benchmarkTitle = article.querySelector(
                                            '.tg-type-schema[aria-label="Source record typed_generativity_benchmark_item"] .tg-schema-title code'
                                        );
                                        const textRange = document.createRange();
                                        if (benchmarkTitle) textRange.selectNodeContents(benchmarkTitle);
                                        const titleBounds = benchmarkTitle?.getBoundingClientRect();
                                        const schemaNameWraps = [...article.querySelectorAll(
                                            ".tg-schema-fields dt code"
                                        )].filter(name => {
                                            const range = document.createRange();
                                            range.selectNodeContents(name);
                                            return range.getClientRects().length !== 1;
                                        }).length;
                                        return {
                                            sourceIds: source.map(e =>
                                                Number(e.querySelector("table")?.dataset.sourceTable)),
                                            rows: mobile.map(e =>
                                                e.querySelectorAll(".tg-mobile-record").length),
                                            sourceVisible, mobileVisible,
                                            records: records.length, fields: fields.length,
                                            hints: cues.length, scrollHintsVisible, badCues,
                                            originalPaths, mobilePaths,
                                            symbolSource, symbolMobile,
                                            benchmarkTitleLines: benchmarkTitle ?
                                                textRange.getClientRects().length : 0,
                                            benchmarkTitleOverflow: !!titleBounds &&
                                                (titleBounds.left < -1 ||
                                                 titleBounds.right > innerWidth + 1),
                                            schemaNameWraps,
                                            outOfBounds: bounds.filter(b =>
                                                b.left < -1 || b.right > innerWidth + 1).length,
                                            sequenceCount: article.querySelectorAll(".tg-sequence").length,
                                            sequenceStages: article.querySelectorAll(".tg-sequence li").length,
                                            examples: article.querySelectorAll(".tg-domain-example").length,
                                            exampleFields: article.querySelectorAll(".tg-example-line").length,
                                            recordPairs: article.querySelectorAll(".tg-record-pair").length,
                                            splitRecords: article.querySelectorAll(
                                                ".tg-record-pair .tg-type-schema").length,
                                            typeSchemas: article.querySelectorAll(".tg-type-schema").length,
                                            typeFields: article.querySelectorAll(".tg-schema-field").length,
                                            schemaOverflows: [...article.querySelectorAll(
                                                ".tg-schema-field"
                                            )].filter(e => {
                                                const rect = e.getBoundingClientRect();
                                                return rect.left < -1 || rect.right > innerWidth + 1;
                                            }).length
                                        };
                                    }""")
                                    expected_rows = [6, 5, 5, 5, 3, 4, 5, 5, 5, 9, 3, 6, 7, 8, 5]
                                    if (typed["sourceIds"] != list(range(1, 16)) or
                                        typed["rows"] != expected_rows or
                                        typed["records"] != 81 or typed["fields"] != 227 or
                                        typed["hints"] != 15 or typed["badCues"] != 0 or
                                        typed["originalPaths"] != 22 or typed["mobilePaths"] != 22 or
                                        typed["symbolSource"] != ["Gamma", "A", "t", "theta", "P_theta"] or
                                        typed["symbolMobile"] != ["Gamma", "A", "t", "theta", "P_theta"] or
                                        typed["benchmarkTitleLines"] != 1 or
                                        typed["benchmarkTitleOverflow"] or
                                        typed["schemaNameWraps"] != 0 or
                                        typed["sequenceCount"] != 2 or typed["sequenceStages"] != 9 or
                                        typed["examples"] != 4 or typed["exampleFields"] != 13 or
                                        typed["recordPairs"] != 1 or typed["splitRecords"] != 2 or
                                        typed["typeSchemas"] != 4 or typed["typeFields"] != 45 or
                                        typed["schemaOverflows"] != 0 or
                                        typed["outOfBounds"] != 0 or
                                        (width <= 650 and (
                                            typed["sourceVisible"] != 0 or typed["mobileVisible"] != 15 or
                                            typed["scrollHintsVisible"] != 0)) or
                                        (width > 650 and (
                                            typed["sourceVisible"] != 15 or typed["mobileVisible"] != 0 or
                                            typed["scrollHintsVisible"] != (15 if width <= 1000 else 0)))):
                                        failures.append(
                                            f"{width}px {rel}: typed generation reading regression {typed}"
                                        )
                                if rel == "essays/functorial-consistency.html":
                                    functorial = page.evaluate("""() => {
                                        const article = document.querySelector(".article-content");
                                        const square = article.querySelector(".fc-commuting");
                                        const squareBounds = square?.getBoundingClientRect();
                                        const nodes = [...(square?.querySelectorAll(
                                            ".fc-square-node") ?? [])];
                                        const nodeBounds = nodes.map(n => n.getBoundingClientRect());
                                        const original = [...article.querySelectorAll(
                                            ".table-scroll[data-fc-alternative='mobile']"
                                        )];
                                        const mobile = [...article.querySelectorAll(".fc-mobile-records")];
                                        const records = [...article.querySelectorAll(".fc-mobile-record")];
                                        const fields = [...article.querySelectorAll(".fc-record-field")];
                                        const hints = [...article.querySelectorAll(".fc-scroll-hint")];
                                        const sourceVisible = original.filter(e =>
                                            getComputedStyle(e).display !== "none").length;
                                        const mobileVisible = mobile.filter(e =>
                                            getComputedStyle(e).display !== "none").length;
                                        const shownHints = hints.filter(e =>
                                            getComputedStyle(e).display !== "none").length;
                                        const invalidHints = hints.filter(h =>
                                            !h.nextElementSibling?.classList.contains("table-scroll") ||
                                            h.nextElementSibling?.getAttribute("aria-describedby") !== h.id
                                        ).length;
                                        const visibleRecords = records.filter(r =>
                                            getComputedStyle(r.closest(".fc-mobile-records")).display !== "none"
                                        ).map(r => r.getBoundingClientRect());
                                        const condition = square?.querySelector(
                                            ".fc-condition-formula math[alttext]"
                                        );
                                        const sizes = original.map(e => Number(e.dataset.columns));
                                        return {
                                            tableCount: original.length,
                                            tableIds: original.map(e =>
                                                Number(e.querySelector("table")?.dataset.sourceTable)),
                                            rowCounts: mobile.map(e =>
                                                e.querySelectorAll(".fc-mobile-record").length),
                                            cards: records.length, fields: fields.length,
                                            sourceVisible, mobileVisible,
                                            hints: hints.length, shownHints, invalidHints,
                                            squareNodes: nodes.length,
                                            squareArrows: square?.querySelectorAll(
                                                ".fc-horizontal-arrow, .fc-down-arrow").length ?? 0,
                                            squareFits: !!squareBounds &&
                                                squareBounds.left >= -1 && squareBounds.right <= innerWidth + 1 &&
                                                nodeBounds.every(n => n.left >= -1 && n.right <= innerWidth + 1),
                                            squareStructure: nodeBounds.length === 4 &&
                                                nodeBounds[0].right < nodeBounds[1].left &&
                                                nodeBounds[2].right < nodeBounds[3].left &&
                                                nodeBounds[0].bottom < nodeBounds[2].top &&
                                                nodeBounds[1].bottom < nodeBounds[3].top,
                                            condition: condition?.getAttribute("alttext") ?? null,
                                            overflowCards: visibleRecords.filter(
                                                b => b.left < -1 || b.right > innerWidth + 1).length,
                                            threeAndFourColumnTables: sizes.filter(c => c >= 3).length
                                        };
                                    }""")
                                    expected_rows = [
                                        5, 8, 6, 5, 8, 9, 12, 16, 13, 5,
                                        8, 6, 7, 8, 7, 15, 5, 6, 7
                                    ]
                                    if (functorial["tableCount"] != 19 or
                                        functorial["tableIds"] != list(range(1, 20)) or
                                        functorial["rowCounts"] != expected_rows or
                                        functorial["cards"] != 156 or functorial["fields"] != 419 or
                                        functorial["hints"] != 19 or functorial["invalidHints"] or
                                        functorial["squareNodes"] != 4 or
                                        functorial["squareArrows"] != 4 or
                                        not functorial["squareFits"] or
                                        not functorial["squareStructure"] or
                                        functorial["condition"] != "T(f(x)) ~ g(T(x))" or
                                        functorial["overflowCards"] or
                                        (width <= 650 and (
                                            functorial["sourceVisible"] != 0 or
                                            functorial["mobileVisible"] != 19 or
                                            functorial["shownHints"] != 0)) or
                                        (width > 650 and (
                                            functorial["sourceVisible"] != 19 or
                                            functorial["mobileVisible"] != 0 or
                                            functorial["shownHints"] !=
                                                (functorial["threeAndFourColumnTables"]
                                                 if width <= 1000 else 0)))):
                                        failures.append(
                                            f"{width}px {rel}: functorial source reading regression {functorial}"
                                        )
                                table_structure = page.evaluate("""() => ({
                                    invalid: [...document.querySelectorAll(".article-content .table-scroll")]
                                      .filter(w => {
                                        const t = w.querySelector("table");
                                        const preceding = w.previousElementSibling;
                                        const label = (preceding?.classList.contains("preface-scroll-hint") ||
                                                       preceding?.classList.contains("sp-scroll-hint") ||
                                                       preceding?.classList.contains("tg-scroll-hint") ||
                                                       preceding?.classList.contains("fc-scroll-hint"))
                                          ? preceding.previousElementSibling : preceding;
                                        if (!t || !t.tHead || !t.tBodies.length ||
                                            !t.caption || !t.caption.classList.contains("visually-hidden") ||
                                            !label || !label.classList.contains("table-display-caption") ||
                                            label.id !== w.getAttribute("aria-labelledby")) return true;
                                        const headers = t.tHead.querySelectorAll("th[scope=col]");
                                        const count = Number(w.dataset.columns);
                                        if (!Number.isInteger(count) || count < 1 ||
                                            headers.length < 1 || headers.length > count) return true;
                                        if (t.querySelector("th[ead]")) return true;
                                        if (getComputedStyle(label).display === "none") return true;
                                        const authored = label.classList.contains("source-visible-caption");
                                        const bounds = label.getBoundingClientRect();
                                        if (authored) {
                                            if (bounds.height < 10 ||
                                                bounds.right > innerWidth + 2 ||
                                                !label.textContent.trim().startsWith("Table.")) return true;
                                        } else if (bounds.height > 2 || bounds.width > 2) {
                                            return true;
                                        }
                                        const compactSquare = t.id === "table-5" &&
                                            !!t.closest(".ci-commuting") &&
                                            !!document.querySelector(".ci-commuting-mobile") &&
                                            getComputedStyle(w).display === "none";
                                        const compactPreface = !!w.dataset.prefaceAlternative &&
                                            getComputedStyle(w).display === "none";
                                        const compactSemantic = !!w.dataset.spAlternative &&
                                            getComputedStyle(w).display === "none";
                                        const compactTyped = !!w.dataset.tgAlternative &&
                                            getComputedStyle(w).display === "none";
                                        const compactFunctorial = !!w.dataset.fcAlternative &&
                                            getComputedStyle(w).display === "none";
                                        if (innerWidth <= 375 && count >= 2 &&
                                            t.getBoundingClientRect().width < 550 &&
                                            !compactSquare && !compactPreface &&
                                            !compactSemantic && !compactTyped &&
                                            !compactFunctorial) return true;
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
                                    if rel == "essays/series-preface.html":
                                        for name, selector in (
                                            ("lifecycle", ".preface-lifecycle"),
                                            ("reading-map", '.preface-mobile-records[aria-label="Publication order and reading links"]'),
                                            ("foundations", '.preface-mobile-records[aria-label="Foundational layers and questions"]'),
                                            ("glossary", '.preface-mobile-records[aria-label="Core terms and definitions"]'),
                                            ("claims", '.preface-mobile-records[aria-label="Claim protocol levels and treatment"]'),
                                            ("notation", '.preface-mobile-records[aria-label="Mathematical notation and reading"]'),
                                            ("publication", '.preface-mobile-records[aria-label="Publication steps and gates"]'),
                                            ("schemas", '.preface-mobile-records[aria-label="Canonical schemas and artifacts"]'),
                                        ):
                                            item = page.locator(selector).first
                                            if item.count() and item.is_visible():
                                                item.screenshot(
                                                    path=str(screenshots / f"{width}-{label}-{name}.png")
                                                )
                                    if rel == "essays/semantic-participation.html":
                                        for name, selector in (
                                            ("contributions", ".sp-mobile-table-1"),
                                            ("governing-claim", ".sp-mobile-table-3"),
                                            ("thresholds", ".sp-mobile-table-5"),
                                            ("epistemic-types", ".sp-mobile-table-6"),
                                            ("bench", ".sp-mobile-table-9"),
                                            ("claim-ledger", ".sp-mobile-table-12"),
                                            ("sequence", ".sp-sequence"),
                                            ("membership", ".sp-criterion"),
                                            ("proof-example", ".sp-proof-example"),
                                            ("environment", ".sp-source-schema"),
                                        ):
                                            item = page.locator(selector).first
                                            if item.count() and item.is_visible():
                                                item.screenshot(
                                                    path=str(screenshots / f"{width}-{label}-{name}.png")
                                                )
                                    if rel == "essays/typed-generativity.html":
                                        for name, selector in (
                                            ("contributions", ".tg-mobile-table-1"),
                                            ("reader-map", ".tg-mobile-table-2"),
                                            ("symbols", ".tg-mobile-table-3"),
                                            ("levels", ".tg-mobile-table-5"),
                                            ("metrics", ".tg-mobile-table-10"),
                                            ("objections", ".tg-mobile-table-13"),
                                            ("claims", ".tg-mobile-table-15"),
                                            ("lifecycle", ".tg-sequence"),
                                            ("domain-example", ".tg-domain-example"),
                                            ("record-pair", ".tg-record-pair"),
                                            ("harness-schema", '.tg-type-schema[aria-label="Source record type_first_item"]'),
                                            ("benchmark-schema", '.tg-type-schema[aria-label="Source record typed_generativity_benchmark_item"]'),
                                        ):
                                            item = page.locator(selector).first
                                            if item.count() and item.is_visible():
                                                item.screenshot(
                                                    path=str(screenshots / f"{width}-{label}-{name}.png")
                                                )
                                    if rel == "essays/functorial-consistency.html":
                                        for name, selector in (
                                            ("commuting-square", ".fc-commuting"),
                                            ("contributions", ".fc-mobile-table-1"),
                                            ("evaluation-object", ".fc-mobile-table-2"),
                                            ("metrics", ".fc-mobile-table-6"),
                                            ("failure-taxonomy", ".fc-mobile-table-7"),
                                            ("item-schema", ".fc-mobile-table-8"),
                                            ("output-schema", ".fc-mobile-table-9"),
                                            ("benchmark-card", ".fc-mobile-table-16"),
                                            ("worked-cases", ".fc-mobile-table-17"),
                                            ("editorial-revisions", ".fc-mobile-table-19"),
                                        ):
                                            item = page.locator(selector).first
                                            if item.count() and item.is_visible():
                                                item.screenshot(
                                                    path=str(screenshots / f"{width}-{label}-{name}.png")
                                                )
                                    first_table = page.locator(".table-scroll:visible").first
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
