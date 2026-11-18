#!/usr/bin/env python3
"""Render source-mapped synthesis citations and an accessible bibliography.

The catalogue is a checked-in publication resource, distinct from the original
DOCX provenance. Every cited manuscript key must resolve to exactly one entry.
Authorial prose and the source manuscript remain unchanged by this renderer.
"""
from __future__ import annotations

from html import escape
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

_TEXT = re.compile(r"(?<=>)([^<]+)(?=<)", re.S)
_PAREN = re.compile(r"\(([A-Za-z][A-Za-z0-9]*(?:,[A-Za-z][A-Za-z0-9]*)*)\)")
_KEY = re.compile(r"^[A-Za-z][A-Za-z0-9]*$")


def render_synthesis_references(body: str, catalogue_path: Path) -> str:
    """Link every cited key and append a source-checked reference list.

    The reference inventory is exact. A missing, unused, duplicate, or unsafe
    reference fails the build instead of silently displaying an incomplete list.
    """
    catalogue = json.loads(catalogue_path.read_text(encoding="utf-8"))
    if catalogue.get("schema_version") != 1:
        raise ValueError("Unexpected synthesis bibliography schema")
    entries = catalogue.get("references")
    if not isinstance(entries, list) or len(entries) != 34:
        raise ValueError("Synthesis bibliography must have 34 references")
    by_key: dict[str, dict[str, str]] = {}
    for entry in entries:
        if not isinstance(entry, dict) or set(entry) != {
            "key", "authors", "year", "title", "venue", "url"
        }:
            raise ValueError("Malformed bibliography record")
        if any(not isinstance(value, str) or not value.strip()
               for value in entry.values()):
            raise ValueError("Empty bibliography field")
        key = entry["key"]
        if not _KEY.fullmatch(key) or key in by_key:
            raise ValueError("Invalid or duplicated citation key: " + key)
        url = urlsplit(entry["url"])
        if url.scheme != "https" or not url.netloc or url.username or url.password:
            raise ValueError("Unsafe bibliography URL for " + key)
        by_key[key] = entry

    if '<h2 id="references">' in body or 'class="bibliography"' in body:
        raise ValueError("Synthesis bibliography is already rendered")
    cited: set[str] = set()

    def replace_node(match: re.Match[str]) -> str:
        def link_citation(found: re.Match[str]) -> str:
            keys = found.group(1).split(",")
            if not all(key in by_key for key in keys):
                return found.group()
            cited.update(keys)
            linked = "; ".join(
                '<a class="citation-link" href="#ref-' + key + '">' +
                escape(by_key[key]["authors"] + ", " + by_key[key]["year"]) +
                "</a>"
                for key in keys
            )
            return "(" + linked + ")"
        return _PAREN.sub(link_citation, match.group(1))

    linked_body = _TEXT.sub(replace_node, body)
    if cited != set(by_key):
        raise ValueError(
            "Bibliography does not match cited keys: missing=" +
            repr(sorted(set(by_key) - cited)) +
            "; unknown=" + repr(sorted(cited - set(by_key)))
        )

    items = []
    for entry in sorted(entries, key=lambda e: (
        e["authors"].casefold(), e["year"], e["title"].casefold()
    )):
        key = entry["key"]
        items.append(
            '<li id="ref-' + key + '" class="bibliography-entry">' +
            '<span class="ref-details">' +
            escape(entry["authors"]) + " (" + escape(entry["year"]) + "). " +
            "<cite>" + escape(entry["title"]) + "</cite>. " +
            escape(entry["venue"]) + ".</span> " +
            '<a href="' + escape(entry["url"], quote=True) +
            '" rel="noopener noreferrer">Publication</a></li>'
        )
    return (
        linked_body +
        '\n<section class="bibliography" aria-labelledby="references">' +
        '<h2 id="references">References</h2>' +
        '<p class="bibliography-note">Primary publications and documentation corresponding to the citation keys in this essay. Years identify the linked editions; some works first appeared as earlier preprints.</p>' +
        '<ol class="references-list">' + "".join(items) +
        "</ol></section>\n"
    )
