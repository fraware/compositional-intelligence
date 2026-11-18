"""Source-grounded search and AI retrieval metadata for the essay collection.

These editorial descriptors support discovery without changing any manuscript
body, claiming peer review, or inventing research results or publication dates.
llms.txt is a navigational convention, not a search ranking signal.
"""
from __future__ import annotations

import hashlib
import html
import json
import re
from pathlib import Path

BASE = "https://fraware.github.io/compositional-intelligence/"
AUTHOR_ID = "https://mateopetel.xyz/#person"
AUTHOR = {
    "@type": "Person",
    "@id": AUTHOR_ID,
    "name": "Mateo Petel",
    "url": "https://mateopetel.xyz/",
    "sameAs": [
        "https://github.com/fraware",
        "https://www.linkedin.com/in/mateo-petel/",
    ],
}
HOME_TITLE = "Compositional Intelligence | Typed Artifacts and AI"
HOME_DESCRIPTION = (
    "Research essays on compositional intelligence, typed AI artifacts, semantic "
    "participation, functorial consistency, and evaluating AI in structured worlds."
)

# Every description is an editorial summary supported by the manuscript abstract.
# "Definition" is a navigation aid; the full specification is in the source essay.
CONCEPTS = {
    "compositional-intelligence": {
        "term": "Compositional Intelligence",
        "seo_title": "Compositional Intelligence | A Framework for AI",
        "description": "A research framework for evaluating AI-generated typed artifacts through semantic participation, structural consistency, evidence, and controlled effects.",
        "definition": "A proposed research program for judging AI-generated artifacts by their admissibility, structural relationships, validation, evidence, and authorized use in structured worlds.",
        "topics": ["compositional intelligence", "AI evaluation", "typed artifacts", "structured worlds"],
    },
    "semantic-participation": {
        "term": "Semantic Participation",
        "seo_title": "Semantic Participation | AI Artifact Validation",
        "description": "How generated proofs, programs, and scientific claims participate in structured environments through validation, provenance, epistemic status, and permitted use.",
        "definition": "The conditions for treating a generated candidate as an artifact within a specified environment, with recorded validation, alignment, compositional role, epistemic status, and permitted use.",
        "topics": ["semantic participation", "AI artifact validation", "formal verification", "scientific evidence"],
    },
    "typed-generativity": {
        "term": "Typed Generativity",
        "seo_title": "Typed Generativity | Probabilistic Type Inhabitation",
        "description": "Model AI generation as inference of a target type followed by probabilistic construction of candidate inhabitants, distinguishing typed output and constrained decoding.",
        "definition": "An account of generation as inference of a target type or artifact class followed by probabilistic construction of candidate inhabitants under an available context.",
        "topics": ["typed generativity", "probabilistic type inhabitation", "type-guided generation", "constrained decoding"],
    },
    "functorial-consistency": {
        "term": "Functorial Consistency",
        "seo_title": "Functorial Consistency | Structure-Preserving AI",
        "description": "A proposed AI evaluation benchmark comparing transform-then-translate with translate-then-transform under explicit equivalence relations and validators.",
        "definition": "A proposed benchmark criterion testing whether two transformation paths agree under a declared target equivalence relation and validator.",
        "topics": ["functorial consistency", "commuting diagrams", "structure-preserving AI", "AI benchmarks"],
    },
    "lambek-machines": {
        "term": "Lambek Machines",
        "seo_title": "Lambek Machines | Grammar-as-Logic for Language AI",
        "description": "A research proposal using Lambek categorial types, linguistic derivations, and semantic composition to study language-model generalization and evaluation.",
        "definition": "Language systems that expose enough of a categorial type-and-derivation pipeline for analysis, supervision, constrained generation, repair, or compositional evaluation.",
        "topics": ["Lambek machines", "grammar as logic", "categorial grammar", "compositional language models"],
    },
    "algebraic-architectures": {
        "term": "Algebraic Architectures",
        "seo_title": "Algebraic Architectures | Structured Neural Models",
        "description": "Specify neural model families through task structure, symmetries, interfaces, constraints, validators, and empirically testable architectural commitments.",
        "definition": "A specification-first approach to neural architecture design that relates task requirements to structural model commitments and validation obligations.",
        "topics": ["algebraic architectures", "geometric deep learning", "equivariant neural networks", "architecture specification"],
    },
    "quantitative-curry-howard": {
        "term": "Quantitative Curry-Howard",
        "seo_title": "Quantitative Curry-Howard | Evidence and Proof",
        "description": "Separate soft quantitative evidence, search scores, probabilities, and uncertainty records from validated proofs and checker-established correctness.",
        "definition": "An operational interface attaching quantitative evidence to candidate typed artifacts while preserving the distinction from formally verified proof or empirical validation.",
        "topics": ["quantitative Curry-Howard", "proof search", "probabilistic warrant", "formal validation"],
    },
    "effectful-and-conceptual-intelligence": {
        "term": "Effectful and Conceptual Intelligence",
        "seo_title": "Effectful AI Agents | Typed Actions and Authority",
        "description": "Evaluate AI agent actions using typed preconditions, postconditions, effect records, authority, reversibility, validation, and execution traces.",
        "definition": "An approach to consequential AI-agent behavior that records actions through typed preconditions, postconditions, effects, authority, risk, and validation.",
        "topics": ["effectful AI", "AI agents", "type and effect systems", "runtime validation"],
    },
}


def validate_inventory(essays: list[tuple[str, str, str, str]]) -> None:
    """Reject stale metadata whenever the authoritative essay inventory changes."""
    slugs = [row[0] for row in essays]
    if len(slugs) != 8 or set(slugs) != set(CONCEPTS) or len(set(slugs)) != len(slugs):
        raise ValueError("Discovery records must match all eight published essays")
    for _, title, _, _ in essays:
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Every essay must have a nonempty authored title")


def _json_script(graph: dict) -> str:
    """Serialize immutable JSON-LD without executable JavaScript or tag breakouts."""
    payload = json.dumps(graph, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return '<script type="application/ld+json">' + payload.replace("<", "\\u003c") + "</script>"


def _insert_head(source: str, content: str) -> str:
    if source.count("</head>") != 1:
        raise ValueError("Expected exactly one HTML document head")
    return source.replace("</head>", content + "\n</head>", 1)


def _swap_title(source: str, new_title: str) -> str:
    old = "<title>Compositional Intelligence</title>"
    if source.count(old) != 1:
        raise ValueError("Expected a single known legacy publication title")
    return source.replace(old, "<title>" + html.escape(new_title, quote=True) + "</title>", 1)


def _person() -> dict:
    return dict(AUTHOR)


def article_graph(slug: str, title: str, category: str) -> dict:
    """Describe a research essay, never a peer-reviewed or accepted paper."""
    if slug not in CONCEPTS:
        raise ValueError("Unknown essay slug")
    data = CONCEPTS[slug]
    url = BASE + "essays/" + slug + ".html"
    series_id = BASE + "#series"
    return {
        "@context": "https://schema.org",
        "@graph": [
            _person(),
            {
                "@type": "WebSite", "@id": BASE + "#website",
                "url": BASE, "name": "Compositional Intelligence", "inLanguage": "en",
            },
            {
                "@type": "WebPage", "@id": url + "#webpage",
                "url": url, "name": title, "description": data["description"],
                "inLanguage": "en", "isPartOf": {"@id": BASE + "#website"},
                "mainEntity": {"@id": url + "#article"},
            },
            {
                "@type": "Article", "@id": url + "#article",
                "url": url, "headline": title, "description": data["description"],
                "inLanguage": "en", "author": {"@id": AUTHOR_ID},
                "isPartOf": {"@id": series_id},
                "mainEntityOfPage": {"@id": url + "#webpage"},
                "genre": "Research essay",
                "isAccessibleForFree": True,
                "keywords": data["topics"],
                "about": [{"@type": "Thing", "name": topic} for topic in data["topics"]],
            },
            {
                "@type": "BreadcrumbList", "@id": url + "#breadcrumb",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1,
                     "name": "Compositional Intelligence", "item": BASE},
                    {"@type": "ListItem", "position": 2, "name": title, "item": url},
                ],
            },
        ],
    }


def homepage_graph(essays: list[tuple[str, str, str, str]]) -> dict:
    """Identify the canonical collection, its author, and its eight essays."""
    validate_inventory(essays)
    series_id = BASE + "#series"
    return {
        "@context": "https://schema.org",
        "@graph": [
            _person(),
            {
                "@type": "WebSite", "@id": BASE + "#website",
                "url": BASE, "name": "Compositional Intelligence",
                "description": HOME_DESCRIPTION, "inLanguage": "en",
                "publisher": {"@id": AUTHOR_ID},
            },
            {
                "@type": "CreativeWorkSeries", "@id": series_id,
                "url": BASE, "name": "Compositional Intelligence",
                "description": HOME_DESCRIPTION,
                "creator": {"@id": AUTHOR_ID}, "inLanguage": "en",
                "hasPart": [
                    {"@id": BASE + "essays/" + slug + ".html#article"}
                    for slug, _, _, _ in essays
                ],
            },
            {
                "@type": "CollectionPage", "@id": BASE + "#webpage",
                "url": BASE, "name": "Compositional Intelligence",
                "description": HOME_DESCRIPTION, "inLanguage": "en",
                "isPartOf": {"@id": BASE + "#website"},
                "mainEntity": {"@id": series_id},
            },
            {
                "@type": "ItemList", "@id": BASE + "#contents",
                "name": "Compositional Intelligence essays",
                "itemListElement": [
                    {
                        "@type": "ListItem", "position": i,
                        "item": {
                            "@type": "Article",
                            "@id": BASE + "essays/" + slug + ".html#article",
                            "name": title,
                            "url": BASE + "essays/" + slug + ".html",
                        },
                    }
                    for i, (slug, title, _, _) in enumerate(essays, start=1)
                ],
            },
        ],
    }


def concept_graph(essays: list[tuple[str, str, str, str]]) -> dict:
    """Publish glossary terms as descriptions linked to their source essays."""
    validate_inventory(essays)
    url = BASE + "concepts.html"
    terms = [
        {
            "@type": "DefinedTerm",
            "@id": url + "#" + slug,
            "name": data["term"], "description": data["definition"],
            "url": url + "#" + slug,
            "inDefinedTermSet": {"@id": url + "#terms"},
            "subjectOf": {
                "@id": BASE + "essays/" + slug + ".html#article"
            },
        }
        for slug, data in CONCEPTS.items()
    ]
    return {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "CollectionPage", "@id": url + "#webpage",
                "url": url, "name": "Concepts in Compositional Intelligence",
                "description": "An editorial guide linking eight research concepts to their original essays.",
                "inLanguage": "en", "isPartOf": {"@id": BASE + "#website"},
                "mainEntity": {"@id": url + "#terms"},
            },
            {
                "@type": "DefinedTermSet", "@id": url + "#terms",
                "url": url, "name": "Compositional Intelligence concepts",
                "hasDefinedTerm": [{"@id": term["@id"]} for term in terms],
            },
            *terms,
        ],
    }


def decorate_article(source: str, slug: str, title: str, category: str) -> str:
    """Improve machine-readable retrieval without editing the rendered manuscript."""
    if slug not in CONCEPTS:
        raise ValueError("Unknown article")
    data = CONCEPTS[slug]
    source = _swap_title(source, data["seo_title"])
    # Each generated essay has exactly one source subtitle as description.
    old = '<meta name="description" content="'
    if source.count(old) != 1:
        raise ValueError("Unexpected article description metadata")
    source = re.sub(
        r'<meta name="description" content="[^"]*">',
        '<meta name="description" content="' +
        html.escape(data["description"], quote=True) + '">',
        source, count=1,
    )
    extra = (
        '<meta name="twitter:card" content="summary">\n'
        '<meta name="twitter:title" content="' + html.escape(title, quote=True) + '">\n'
        '<meta name="twitter:description" content="' +
        html.escape(data["description"], quote=True) + '">\n'
        '<link rel="alternate" type="application/json" title="Research corpus index" href="../corpus.json">\n'
        '<link rel="help" type="text/plain" title="AI retrieval guide" href="../llms.txt">\n'
        + _json_script(article_graph(slug, title, category))
    )
    return _insert_head(source, extra)


def decorate_homepage(source: str, essays: list[tuple[str, str, str, str]]) -> str:
    """Enrich the generated homepage and link to its editorial concept guide."""
    source = _swap_title(source, HOME_TITLE)
    if source.count('<meta name="description" content=') != 1:
        raise ValueError("Missing canonical homepage description")
    source = re.sub(
        r'<meta name="description" content="[^"]*">',
        '<meta name="description" content="' +
        html.escape(HOME_DESCRIPTION, quote=True) + '">',
        source, count=1,
    )
    marker = '<div id="essays">'
    if source.count(marker) != 1:
        raise ValueError("Missing essay section on publication homepage")
    source = source.replace(
        marker,
        '<p class="reading-guide-link">Explore the '
        '<a href="./concepts.html">research concepts</a> and their original essays.</p>\n'
        + marker,
        1,
    )
    extra = (
        '<meta name="twitter:card" content="summary">\n'
        '<meta name="twitter:title" content="' + html.escape(HOME_TITLE) + '">\n'
        '<link rel="alternate" type="application/json" title="Research corpus index" href="./corpus.json">\n'
        '<link rel="help" type="text/plain" title="AI retrieval guide" href="./llms.txt">\n'
        + _json_script(homepage_graph(essays))
    )
    return _insert_head(source, extra)


def render_concepts(essays: list[tuple[str, str, str, str]]) -> str:
    """Build a readable, source-attributed guide without revising the manuscripts."""
    validate_inventory(essays)
    by_slug = {row[0]: row[1] for row in essays}
    nodes = []
    for slug, data in CONCEPTS.items():
        nodes.append(
            '<section class="concept-entry" aria-labelledby="' + slug + '">'
            '<h2 id="' + slug + '">' + html.escape(data["term"]) + '</h2>'
            '<p>' + html.escape(data["definition"]) + '</p>'
            '<p>Read the original essay <a href="./essays/' + slug + '.html">'
            + html.escape(by_slug[slug]) + '</a>.</p></section>'
        )
    canonical = BASE + "concepts.html"
    return f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#ffffff">
<meta name="description" content="Definitions of compositional intelligence, semantic participation, typed generativity, functorial consistency, Lambek machines, and related AI concepts.">
<meta name="author" content="Mateo Petel">
<meta property="og:type" content="website">
<meta property="og:title" content="Concepts in Compositional Intelligence">
<meta property="og:description" content="Eight research concepts with links to their original essays.">
<meta property="og:url" content="{canonical}">
<link rel="canonical" href="{canonical}">
<meta name="twitter:card" content="summary">
<link rel="icon" href="./favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="./style.css">
<link rel="alternate" type="application/json" title="Research corpus index" href="./corpus.json">
<link rel="help" type="text/plain" title="AI retrieval guide" href="./llms.txt">
<title>Compositional Intelligence Concepts | Research Guide</title>
{_json_script(concept_graph(essays))}
</head><body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><div class="container header-inner">
<a class="brand" href="./index.html">Compositional Intelligence</a>
<nav class="header-nav" aria-label="Primary navigation"><a href="./index.html#essays">Essays</a><a href="./essays/compositional-intelligence.html">The thesis</a></nav>
</div></header>
<main class="container" id="main">
<article><header class="article-header">
<p class="breadcrumb"><a href="./index.html">Essays</a> / Concept guide</p>
<h1>Concepts in Compositional Intelligence</h1>
<p class="deck">A guide to eight connected research essays</p></header>
<div class="article-content">
<p>These concise descriptions orient readers to the arguments developed in the essays. They are editorial summaries of a research program, and do not replace the full definitions, qualifications, or evidence in the primary texts.</p>
{''.join(nodes)}
</div></article></main>
<footer class="site-footer"><div class="container"><span>Compositional Intelligence · Mateo Petel</span><span>© 2026 Mateo Petel</span></div></footer>
</body></html>
"""


def _headings(essay_page: str, canonical: str) -> list[dict]:
    """Extract actual h2 section anchors from the published HTML, never invent them."""
    sections: list[dict] = []
    for anchor, raw in re.findall(
        r'<h2\b[^>]*\bid="([^"]+)"[^>]*>(.*?)</h2>', essay_page, re.I | re.S
    ):
        label = html.unescape(re.sub(r"<[^>]+>", "", raw)).strip()
        if label:
            sections.append({"title": label, "url": canonical + "#" + anchor})
    return sections


def build_assets(output: Path, root: Path, essays: list[tuple[str, str, str, str]]) -> None:
    """Emit deterministic crawl guidance, a text guide, and structured corpus index."""
    validate_inventory(essays)
    (output / "concepts.html").write_text(render_concepts(essays), encoding="utf-8")
    corpus = {
        "schema_version": 1,
        "name": "Compositional Intelligence",
        "url": BASE,
        "language": "en",
        "description": HOME_DESCRIPTION,
        "author": {
            "name": "Mateo Petel",
            "url": "https://mateopetel.xyz/",
            "github": "https://github.com/fraware",
        },
        "concept_guide": BASE + "concepts.html",
        "source_repository": "https://github.com/fraware/compositional-intelligence",
        "source_note": (
            "The original DOCX fingerprints are recorded in sources/originals.json. "
            "Published essays are DOCX-derived, source-verified research writing; "
            "a source checksum establishes file identity, not scientific correctness. "
            "The collection includes proposals and untested hypotheses."
        ),
        "essays": [],
    }
    for position, (slug, title, category, subtitle) in enumerate(essays, start=1):
        canonical = BASE + "essays/" + slug + ".html"
        data = CONCEPTS[slug]
        markdown = root / "essays" / (slug + ".md")
        page = (output / "essays" / (slug + ".html")).read_text(encoding="utf-8")
        corpus["essays"].append({
            "position": position,
            "title": title,
            "category": category,
            "subtitle": subtitle,
            "description": data["description"],
            "url": canonical,
            "subjects": data["topics"],
            "concept": {"term": data["term"], "url": BASE + "concepts.html#" + slug},
            "manuscript_sha256": hashlib.sha256(markdown.read_bytes()).hexdigest(),
            "sections": _headings(page, canonical),
        })
    (output / "corpus.json").write_text(
        json.dumps(corpus, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    guide = [
        "# Compositional Intelligence",
        "",
        "> Eight research essays by Mateo Petel on typed AI artifacts, compositional "
        "validity, formal structures, neural architectures, and consequential AI agents.",
        "",
        "Canonical collection: " + BASE,
        "Concept definitions: " + BASE + "concepts.html",
        "Machine-readable corpus: " + BASE + "corpus.json",
        "Canonical sitemap: " + BASE + "sitemap.xml",
        "",
        "## Essays",
        "",
    ]
    for row in corpus["essays"]:
        guide.extend([
            "### " + str(row["position"]) + ". " + row["title"],
            "",
            "- URL: " + row["url"],
            "- Description: " + row["description"],
            "- Topics: " + ", ".join(row["subjects"]),
            "",
        ])
    guide.extend([
        "## Interpretation and provenance",
        "",
        "These manuscripts advance a research program. A proposed definition, benchmark, "
        "or method does not establish an empirical result or a formal proof. Consult "
        "the complete primary essays for conditions and limitations.",
        "The original DOCX fingerprints are recorded in the public source repository. "
        "The corpus index preserves publication source checksums and actual section anchors.",
        "The author and site are one source, not independent corroboration.",
        "",
        "Author: https://mateopetel.xyz/",
        "Source: https://github.com/fraware/compositional-intelligence",
        "",
    ])
    (output / "llms.txt").write_text("\n".join(guide), encoding="utf-8")
    (output / "robots.txt").write_text(
        "User-agent: *\nAllow: /\nSitemap: " + BASE + "sitemap.xml\n",
        encoding="utf-8",
    )
