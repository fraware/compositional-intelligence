#!/usr/bin/env python3
"""Reviewable, source-preserving scientific presentation of V3 HTML essays.

Only the transcriptions listed in FORMULAE are converted to MathML. The exact
source transcription remains in each MathML alttext attribute. Structured
record fields are formatted without changing their content.
"""
from __future__ import annotations

from functools import lru_cache
from html import escape, unescape
import re
import subprocess

FORMULAE: tuple[tuple[str, str], ...] = (
    ("Gamma; M; E; C |- write_memory(m) : M -> M + {m} ! memory_write @ rho",
     r"\Gamma;M;E;C\vdash\operatorname{write\_memory}(m):M\to M+\{m\}\;!\;\operatorname{memory\_write}@\rho"),
    ("Gamma; M; E; C |- pi : Pre_0 -> Post_n ! (eps_1 + ... + eps_n) @ rho",
     r"\Gamma;M;E;C\vdash\pi:\mathrm{Pre}_0\to\mathrm{Post}_n\;!\;(\varepsilon_1+\cdots+\varepsilon_n)@\rho"),
    ("Gamma; M; E; C |- a : Pre -> Post ! epsilon @ rho",
     r"\Gamma;M;E;C\vdash a:\mathrm{Pre}\to\mathrm{Post}\;!\;\varepsilon@\rho"),
    ("Gamma; M; E; C |- a : Pre -> Post ! eps @ rho",
     r"\Gamma;M;E;C\vdash a:\mathrm{Pre}\to\mathrm{Post}\;!\;\varepsilon@\rho"),
    ("Gamma;M;E;C ⊢ a : Pre -> Post ! epsilon @ rho",
     r"\Gamma;M;E;C\vdash a:\mathrm{Pre}\to\mathrm{Post}\;!\;\varepsilon@\rho"),
    ("Gamma ⊢_theta t : A ▷ Q", r"\Gamma\vdash_{\theta} t:A\triangleright Q"),
    ("Gamma |-_theta t : A |> Q", r"\Gamma\vdash_{\theta} t:A\triangleright Q"),
    ("Gamma |-theta t : A |> Q", r"\Gamma\vdash_{\theta} t:A\triangleright Q"),
    ("Gamma |- t : A", r"\Gamma\vdash t:A"),
    ("P_theta(t : A | Gamma)", r"P_{\theta}(t:A\mid\Gamma)"),
    ("P_theta(tactic | proof_state)", r"P_{\theta}(\mathrm{tactic}\mid\mathrm{proof\_state})"),
    ("T(f(x)) ~= g(T(x))", r"T(f(x))\simeq g(T(x))"),
    ("T(f(x)) approx g(T(x))", r"T(f(x))\approx g(T(x))"),
    ("T(f(x)) ≈ g(T(x))", r"T(f(x))\approx g(T(x))"),
    ("w_i -> tau_i -> pi -> [[pi]]", r"w_i\to\tau_i\to\pi\to\llbracket\pi\rrbracket"),
    ("w_i -> tau_i -> pi -> pi", r"w_i\to\tau_i\to\pi\to\pi"),
    ("TaskSpec -> ArchitectureType -> ArchitectureInstance",
     r"\mathrm{TaskSpec}\to\mathrm{ArchitectureType}\to\mathrm{ArchitectureInstance}"),
    ("Member_E(a)", r"\operatorname{Member}_E(a)"),
    ("A |= S", r"A\models S"),
    ("T(f(x))", r"T(f(x))"),
    ("g(T(x))", r"g(T(x))"),
)

_UNIQUE = dict(FORMULAE)
if len(_UNIQUE) != len(FORMULAE):
    raise ValueError("Duplicate source transcriptions")
_TOKEN = re.compile("|".join(
    "(?<![A-Za-z0-9_])" + re.escape(key) + "(?![A-Za-z0-9_])"
    for key in sorted(_UNIQUE, key=len, reverse=True)
))
_TEXT = re.compile(r"(?<=>)([^<]+)(?=<)", re.S)
_HIDDEN_LABEL = re.compile(
    r'<p\b[^>]*class="table-display-caption"[^>]*>[\s\S]*?</p>'
    r'|<caption\b[^>]*class="visually-hidden"[^>]*>[\s\S]*?</caption>'
)
_ONLY_MATH = re.compile(r"<p>\s*(<math\b[^>]*>(?:(?!</p>)[\s\S])*?</math>)([.]?)\s*</p>")
_P = re.compile(r"^<p>([\s\S]*?)</p>$")
_BR = re.compile(r"<br\s*/?>", re.I)
_KEY = re.compile(r"^[a-z][a-z0-9_]*:$")
_FIELD = re.compile(r"^\s*(?:-\s*)?[A-Za-z][\w.-]*\s*:\s*.*$")


@lru_cache(maxsize=None)
def _mathml(source: str) -> str:
    """Convert reviewed TeX to annotated, semantic MathML with fixed Pandoc."""
    run = subprocess.run(
        ["pandoc", "--from=markdown", "--to=html5", "--mathml", "--wrap=none"],
        input="$" + _UNIQUE[source] + "$",
        capture_output=True, text=True, check=True,
    )
    match = re.search(r"<math\b[\s\S]*?</math>", run.stdout)
    if match is None or 'encoding="application/x-tex"' not in match.group():
        raise RuntimeError("Missing annotated MathML for " + source)
    return match.group().replace(
        "<math ", '<math tabindex="0" alttext="' + escape(source, quote=True) + '" ', 1
    )


def render_source_math(body: str) -> str:
    """Replace only exact source mathematics in text nodes; never edit tags."""
    def replace_node(match: re.Match[str]) -> str:
        original = match.group(1)
        plain = unescape(original)
        matches = list(_TOKEN.finditer(plain))
        if not matches:
            return original
        chunks: list[str] = []
        start = 0
        for item in matches:
            chunks.append(escape(plain[start:item.start()], quote=False))
            chunks.append(_mathml(item.group()))
            start = item.end()
        chunks.append(escape(plain[start:], quote=False))
        return "".join(chunks)

    # The manuscript-derived accessible table labels are not rendered prose.
    # Keep them unmodified; putting MathML inside visually hidden captions can
    # create zero-size formula elements and duplicate speech output.
    hidden: list[str] = []

    def conceal(match: re.Match[str]) -> str:
        index = len(hidden)
        hidden.append(match.group())
        return '<source-caption-slot data-index="' + str(index) + '"></source-caption-slot>'

    body = _HIDDEN_LABEL.sub(conceal, body)
    body = _TEXT.sub(replace_node, body)

    def display(match: re.Match[str]) -> str:
        math = (match.group(1)
                .replace('tabindex="0" ', "", 1)
                .replace('display="inline"', 'display="block"', 1))
        return (
            '<div class="math-scroll" role="group" tabindex="0" '
            'aria-label="Displayed mathematical expression">' +
            math + match.group(2) + "</div>"
        )

    body = _ONLY_MATH.sub(display, body)
    for index, text in enumerate(hidden):
        slot = '<source-caption-slot data-index="' + str(index) + '"></source-caption-slot>'
        body = body.replace(slot, text)
    return body


def _schema(lines: list[str]) -> str:
    """Render source record fields together without changing their content."""
    return (
        '<div class="record-schema" role="group" tabindex="0" aria-label="Source record ' +
        escape(lines[0][:-1], quote=True) + '"><pre><code>' +
        escape("\n".join(lines)) + "</code></pre></div>"
    )


def render_source_records(body: str) -> str:
    """Recover Word paragraph or line-break conventions for field records."""
    parts = re.split(r"(<p>[\s\S]*?</p>)", body)
    output: list[str] = []
    i = 0
    while i < len(parts):
        para = _P.fullmatch(parts[i])
        if para:
            contents = para.group(1)
            if _BR.search(contents) and not re.search(r"<(?!br\s*/?>)", contents, re.I):
                lines = [unescape(value).strip() for value in _BR.split(contents)]
                if (len(lines) >= 5 and _KEY.fullmatch(lines[0]) and
                        "_" in lines[0] and
                        sum(bool(_FIELD.fullmatch(v)) for v in lines[1:]) >= 4):
                    output.append(_schema(lines))
                    i += 1
                    continue
            name = unescape(contents).strip()
            if _KEY.fullmatch(name) and "_" in name:
                lines = [name]
                j = i + 1
                while j + 1 < len(parts):
                    if parts[j].strip():
                        break
                    next_para = _P.fullmatch(parts[j + 1])
                    if next_para is None or "<" in next_para.group(1):
                        break
                    value = unescape(next_para.group(1)).strip()
                    if not _FIELD.fullmatch(value):
                        break
                    lines.append(value)
                    j += 2
                if len(lines) >= 5:
                    output.append(_schema(lines))
                    i = j
                    continue
        output.append(parts[i])
        i += 1
    return "".join(output)


def enhance_scientific_presentation(body: str) -> str:
    """Improve typography without modifying the canonical manuscript source."""
    return render_source_math(render_source_records(body))
