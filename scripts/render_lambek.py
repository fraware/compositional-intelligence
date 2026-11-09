#!/usr/bin/env python3
"""Source-checked publication presentation of Lambek Machines V3.

The canonical essay file is unchanged. Any deviation in original tables,
diagrams or technical record inventories aborts the publication build.
"""
from __future__ import annotations
from html import escape, unescape
import re
import subprocess

HEADERS = {
  1:("ID","Contribution","Publication claim"),
  2:("Reader","Recommended path"),
  3:("Literature","Supported claim","Boundary for this essay"),
  4:("Level","Name","Description","Evidence required"),
  5:("Transformation family","Source-side operation","Target-side expectation"),
  6:("Condition","Description","Purpose"),
  7:("Failure label","Meaning"),
  8:("Metric","Measures"),
  9:("Track","Recommended size","Purpose"),
  10:("Evidence pattern","Interpretation"),
  11:("Objection","Response"),
  12:("Criterion","Decision rule"),
  13:("Source anchor","Use in Essay 4"),
  14:("Area","Revision"),
}
ROWS = (6,5,7,4,7,8,11,10,5,6,7,7,8,7)
CAPTIONS = {
  1:"Table 1. Contributions and publication claims.",
  2:"Table 2. Recommended reading paths.",
  3:"Table 3. Literature and evidential boundaries.",
  4:"Table 4. Lambek Machine levels and evidence requirements.",
  5:"Table 5. Linguistic transformations and semantic expectations.",
  6:"Table 6. Auxiliary supervision evaluation conditions.",
  7:"Table 7. Failure labels and meanings.",
  8:"Table 8. Evaluation metrics and measures.",
  9:"Table 9. Pilot evaluation tracks and recommended sizes.",
  10:"Table 10. Evidence patterns and interpretation.",
  11:"Table 11. Objections and responses.",
  12:"Table 12. Kill criteria and decision rules.",
  13:"Table 13. Source anchors and their roles.",
  14:"Table 14. Editorial changes from v0.2 to v0.3.",
}
SECTIONS = {
  "1":"position-in-the-compositional-intelligence-series",
  "2":"thesis-and-boundary-conditions",
  "3":"formal-core---the-lambek-machine-schema",
  "4":"literature-landscape-and-source-policy",
  "5":"four-levels-of-lambek-machines",
  "6":"functorial-language-consistency",
  "7":"diagnostic-cases",
  "8":"lambek-auxiliary-supervision-v0.2",
  "9":"benchmark-schemas",
  "10":"metrics-and-pilot-plan",
  "11":"success-and-failure-conditions",
  "12":"strongest-objections",
  "13":"kill-criteria",
  "14":"relation-to-essay-5---algebraic-architectures",
  "15":"conclusion",
}
APPENDICES = {
  "A":"appendix-a.-lambek-machine-record",
  "B":"appendix-b.-functorial-language-consistency-item",
}
SCHEMAS = {
  "lambek-benchmark-item":("lambek_benchmark_item:",18),
  "model-output-record":("lambek_model_output:",12),
  "appendix-a.-lambek-machine-record":("lambek_machine_record:",24),
  "appendix-b.-functorial-language-consistency-item":(
    "functorial_language_consistency_item:",15),
}
TABLE = re.compile(
 r'(?P<start><div aria-labelledby="table-(?P<num>\d+)-caption" '
 r'class="table-scroll" data-columns="\d+" role="group" tabindex="0">)'
 r'(?P<table><table data-source-table="\d+" id="table-\d+">[\s\S]*?</table>)'
 r'(?P<end></div>)'
)
TAG=re.compile(r"<[^>]*>")


def captions(body:str)->str:
    """Replace conversion metadata, including the erroneous long Table 9 caption."""
    for n,caption in CAPTIONS.items():
        pat=re.compile(rf'(<p class="table-display-caption" id="table-{n}-caption">)[^<]*(</p>)')
        m=list(pat.finditer(body))
        if len(m)!=1: raise ValueError(f"Missing visible table {n} caption")
        if n==9 and (len(m[0].group())<700 or "Table 8. Metric" not in m[0].group()):
            raise ValueError("Original Table 9 caption anomaly has changed")
        body=pat.sub(lambda x:x.group(1)+escape(caption)+x.group(2),body,count=1)
        native=re.compile(
           rf'(<table data-source-table="{n}" id="table-{n}">'
           r'<caption class="visually-hidden">)[^<]*(</caption>)')
        if len(native.findall(body))!=1: raise ValueError(f"Missing native caption {n}")
        body=native.sub(lambda x:x.group(1)+escape(caption)+x.group(2),body,count=1)
    return body


def reader_map(body:str)->str:
    """Link targets that exist, leaving the authored nonexistent 8.4 unlinked."""
    pat=re.compile(r'(<table data-source-table="2" id="table-2">)([\s\S]*?)(</table>)')
    m=list(pat.finditer(body))
    if len(m)!=1: raise ValueError("Reader map missing")
    content=m[0].group(2)
    row=re.compile(r'(<tr\b[^>]*>\s*<td>[^<]+</td>\s*<td>)([^<]+)(</td>\s*</tr>)')
    matches=list(row.finditer(content))
    if len(matches)!=5: raise ValueError("Reader map row count changed")
    for x in reversed(matches):
        raw=x.group(2)
        if "Read after Essay 3 and before Essay 5" in raw:
            linked=raw.replace("Essay 3",'<a href="functorial-consistency.html">Essay 3</a>',1)
            linked=linked.replace("Essay 5",'<a href="algebraic-architectures.html">Essay 5</a>',1)
        else:
            linked=re.sub(r'\b\d+(?:\.\d+)?\b',lambda y:
              ('<a href="#'+SECTIONS[y.group()]+'">'+y.group()+'</a>')
              if y.group() in SECTIONS else y.group(),raw)
            for letter,fragment in APPENDICES.items():
                linked=linked.replace("Appendix "+letter,
                  'Appendix <a href="#'+fragment+'">'+letter+'</a>',1)
        content=content[:x.start(2)]+linked+content[x.end(2):]
    if "8.4" not in content or ">8.4</a>" in content:
        raise ValueError("Unresolved authored Section 8.4 incorrectly linked")
    x=m[0]
    return body[:x.start()]+x.group(1)+content+x.group(3)+body[x.end():]


def sequence(body:str)->str:
    original=("<p>artifact membership -&gt; target-type inference -&gt; "
              "transformation preservation -&gt; typed linguistic composition</p>")
    if body.count(original)!=1: raise ValueError("Source sequence changed")
    parts=("artifact membership","target-type inference",
           "transformation preservation","typed linguistic composition")
    return body.replace(original,
      '<div class="lm-sequence" aria-label="Authored composition sequence">'
      '<ol>'+''.join('<li>'+escape(x)+'</li>' for x in parts)+'</ol></div>',1)


PIPELINE=(
 ("w_1, ..., w_n",r"w_1,\ldots,w_n"),
 ("-> tau_1, ..., tau_n",r"\tau_1,\ldots,\tau_n"),
 ("-> pi : tau_1 tensor ... tensor tau_n => S",
  r"\pi:\tau_1\otimes\cdots\otimes\tau_n\Rightarrow S"),
 ("-> [[pi]](v_1, ..., v_n)",r"\llbracket\pi\rrbracket(v_1,\ldots,v_n)"),
)


def mathml(text:str,tex:str)->str:
    """Render pinned-Pandoc MathML; keep the author's source in alttext."""
    run=subprocess.run(
      ["pandoc","--from=markdown","--to=html5","--mathml","--wrap=none"],
      input="$"+tex+"$",capture_output=True,text=True,check=True)
    match=re.search(r"<math\b[\s\S]*?</math>",run.stdout)
    if not match or 'encoding="application/x-tex"' not in match.group():
        raise ValueError("Mathematics not annotated by Pandoc")
    return match.group().replace(
      "<math ",'<math alttext="'+escape(text,quote=True)+'" ',1)


def pipeline(body:str)->str:
    source="\n".join('<p>'+escape(s,quote=False)+'</p>' for s,_ in PIPELINE)
    if body.count(source)!=1: raise ValueError("Original four-stage pipeline changed")
    items=''.join('<li>'+mathml(s,t)+'</li>' for s,t in PIPELINE)
    fig=('<div class="lm-pipeline" role="group" aria-label="Source typed composition pipeline">'
         '<ol>'+items+'</ol></div>')
    return body.replace(source,fig,1)


def square(body:str)->str:
    source="\n".join([
     '<p>sentence x --f--&gt; transformed sentence f(x)</p>',
     '<p>| |</p>','<p>T T</p>','<p>v v</p>',
     '<p>semantic artifact T(x) --g--&gt; transformed artifact g(T(x))</p>',
     '<p>Evaluation condition</p>',
     '<p>T(f(x)) approx g(T(x))</p>'])
    if body.count(source)!=1: raise ValueError("Original language square changed")
    fig=(
      '<figure class="lm-square-figure" aria-label="Source Functorial Language Consistency square">'
      '<div class="lm-square">'
      '<div class="lm-node lm-tl">sentence x</div>'
      '<div class="lm-arrow lm-ta">f →</div>'
      '<div class="lm-node lm-tr">transformed sentence f(x)</div>'
      '<div class="lm-arrow lm-la">T ↓</div>'
      '<div class="lm-arrow lm-ra">T ↓</div>'
      '<div class="lm-node lm-bl">semantic artifact T(x)</div>'
      '<div class="lm-arrow lm-ba">g →</div>'
      '<div class="lm-node lm-br">transformed artifact g(T(x))</div>'
      '</div><figcaption><span>Evaluation condition</span> '
      '<span>T(f(x)) approx g(T(x))</span></figcaption></figure>')
    return body.replace(source,fig,1)


def _code(text: str) -> str:
    """Allow line breaks at source underscores without changing text content."""
    return "<code>" + escape(text).replace("_", "_<wbr>") + "</code>"


_FIELD_DECLARATION = re.compile(r"^([A-Za-z][A-Za-z0-9_.-]*:)(?: (.*))?$")


def _format_source_lines(lines: list[str]) -> str:
    """Typeset each authored line in order without inferring unmarked nesting."""
    title = '<p class="lm-schema-heading">' + _code(lines[0]) + "</p>"
    entries: list[str] = []
    for line in lines[1:]:
        field = _FIELD_DECLARATION.fullmatch(line)
        if field:
            name, type_text = field.groups()
            label = '<span class="lm-schema-name">' + _code(name) + "</span>"
            value = (
                '<span class="lm-schema-type">' + _code(type_text) + "</span>"
                if type_text is not None else ""
            )
            entries.append(
                '<li class="lm-schema-line lm-schema-field">' +
                label + (" " if value else "") + value + "</li>"
            )
        else:
            entries.append(
                '<li class="lm-schema-line lm-schema-literal">' +
                _code(line) + "</li>"
            )
    return title + '<ol class="lm-schema-lines">' + "".join(entries) + "</ol>"


def records(body: str) -> str:
    """Render four source records without changing any field or literal line."""
    for anchor, (first, count) in SCHEMAS.items():
        pattern = re.compile(
            rf'(<h[23] id="{re.escape(anchor)}">[^<]+</h[23]>)'
            r'\s*((?:<p>[^<]*</p>\s*)+)'
        )
        matches = list(pattern.finditer(body))
        if len(matches) != 1:
            raise ValueError(f"Missing technical source record {anchor}")
        match = matches[0]
        lines = [
            unescape(value)
            for value in re.findall(r'<p>([^<]*)</p>', match.group(2))
        ]
        if len(lines) != count or lines[0] != first:
            raise ValueError(f"Unexpected technical field inventory in {anchor}")
        schema = (
            '<div class="lm-schema" role="group" '
            'aria-label="Source record ' + escape(first[:-1], quote=True) + '">'
            + _format_source_lines(lines) + "</div>"
        )
        body = (
            body[:match.start()] + match.group(1) + "\n" +
            schema + body[match.end():]
        )
    return body


_DIAGNOSTIC_PAIRS = (
    (
        "Authored quantifier-scope alternatives",
        "forall student, exists book, read(student, book)",
        "exists book, forall student, read(student, book)",
    ),
    (
        "Authored prepositional-attachment alternatives",
        "instrument(observe, microscope)",
        "modifier(cell, microscope)",
    ),
)


def diagnostic_pairs(body: str) -> str:
    """Present original formal comparisons without normalizing their syntax."""
    for label, first, second in _DIAGNOSTIC_PAIRS:
        original = (
            "<p>" + escape(first) + "</p>\n<p>" + escape(second) + "</p>"
        )
        if body.count(original) != 1:
            raise ValueError(f"Original diagnostic comparison changed: {label}")
        markup = (
            '<div class="lm-diagnostic-pair" role="group" '
            'aria-label="' + escape(label, quote=True) + '">'
            '<div class="lm-diagnostic-line">' + _code(first) + "</div>"
            '<div class="lm-diagnostic-line">' + _code(second) + "</div>"
            "</div>"
        )
        body = body.replace(original, markup, 1)
    return body


def tables(body:str)->str:
    """Derive all 98 mobile records from all 237 unchanged table cells."""
    found=list(TABLE.finditer(body))
    if [int(x.group("num")) for x in found]!=list(range(1,15)):
        raise ValueError("Original fourteen-table inventory changed")
    cell_count=0
    for x in reversed(found):
        n=int(x.group("num"))
        html=x.group("table")
        head=re.search(r'<thead>([\s\S]*?)</thead>',html)
        main=re.search(r'<tbody>([\s\S]*?)</tbody>',html)
        if not head or not main: raise ValueError(f"Malformed table {n}")
        headers=tuple(unescape(TAG.sub("",p)).strip()
          for p in re.findall(r'<th\b[^>]*>([\s\S]*?)</th>',head.group(1)))
        if headers!=HEADERS[n]: raise ValueError(f"Source headings changed at {n}")
        rows=re.findall(r'<tr\b[^>]*>([\s\S]*?)</tr>',main.group(1))
        if len(rows)!=ROWS[n-1]: raise ValueError(f"Source rows changed at {n}")
        cards=[]
        for row in rows:
            cells=re.findall(r'<td(?:\s[^>]*)?>([\s\S]*?)</td>',row)
            if len(cells)!=len(headers): raise ValueError(f"Source cells changed at {n}")
            cell_count+=len(cells)
            record=''.join(
              '<div class="lm-field"><dt>'+escape(label)+'</dt><dd>'+value+'</dd></div>'
              for label,value in zip(headers,cells,strict=True))
            cards.append('<dl class="lm-card">'+record+'</dl>')
        hint=(f'<p class="lm-hint" id="lm-hint-{n}">'
              'Scroll horizontally to see all table columns.</p>')
        start=x.group("start").replace('class="table-scroll"',
           'class="table-scroll" data-lm-alternative="mobile"',1)
        start=start[:-1]+f' aria-describedby="lm-hint-{n}">'
        mobile=(f'<section class="lm-mobile lm-mobile-{n}" '
                f'aria-labelledby="table-{n}-caption">'
                +''.join(cards)+'</section>')
        body=body[:x.start()]+hint+start+html+x.group("end")+mobile+body[x.end():]
    if cell_count!=237: raise ValueError("Source cell inventory changed")
    return body


def render_lambek_machines(body:str)->str:
    """Convert only source-derived presentation structures."""
    for step in (captions,reader_map,sequence,pipeline,square,records,diagnostic_pairs,tables):
        body=step(body)
    if (body.count('data-lm-alternative="mobile"')!=14 or
        body.count('class="lm-card"')!=98 or
        body.count('class="lm-field"')!=237):
        raise ValueError("Incomplete Lambek mobile presentation")
    return body
