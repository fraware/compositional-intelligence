# Compositional Intelligence

*Typed Artifacts, Structured Worlds, and Effectful AI*

**Mateo Petel**

**Read the essays:** https://fraware.github.io/compositional-intelligence/

Compositional Intelligence is a series of research essays on the creation, interpretation, and use of AI-generated artifacts within structured worlds. The collection examines semantic validity, typed generation, structural transformations, linguistic composition, neural architectures, quantitative evidence, and consequential action.

## Essays

1. [Compositional Intelligence](essays/compositional-intelligence.md)
2. [Semantic Participation](essays/semantic-participation.md)
3. [Typed Generativity](essays/typed-generativity.md)
4. [Functorial Consistency](essays/functorial-consistency.md)
5. [Lambek Machines](essays/lambek-machines.md)
6. [Algebraic Architectures](essays/algebraic-architectures.md)
7. [Quantitative Curry–Howard](essays/quantitative-curry-howard.md)
8. [Effectful and Conceptual Intelligence](essays/effectful-and-conceptual-intelligence.md)

The essays advance a research program and identify questions that remain open. The scope of each mathematical and empirical claim is stated in the corresponding essay.

The eight manuscripts in `essays/` are the authoritative website sources. The collection includes four manuscripts retaining their V3 DOCX-derived publication fragments and four scientific or editorial revisions: Compositional Intelligence, [Typed Generativity](essays/typed-generativity.md), [Functorial Consistency](essays/functorial-consistency.md), and [Lambek Machines](essays/lambek-machines.md). The revised Functorial Consistency essay contains eight tables; the V3 DOCX fingerprint and original 19-table inventory remain recorded for historical provenance. The Typed Generativity [research supplement](research/typed-generativity/README.md) records its evaluation protocol and evidence boundaries. The build provides reviewed MathML typesetting and readable schema formatting, and produces a deterministic static site using Pandoc 3.1.13.

The original DOCX file fingerprints and current published source checksums are recorded in `sources/originals.json`. For revised manuscripts, the DOCX fingerprints identify the historical originals and the Markdown checksums identify their current editorial publication sources. GitHub Actions checks the committed source hashes, HTML structure, scientific markup, links, responsive presentation, and deployment. The original Word files are deliberately absent from the public repository. Consequently, CI alone does not establish byte-for-byte correspondence with those files.

An independent local source comparison is available with the original Word documents in a private directory:

```sh
python3 scripts/check_originals.py --original-dir /path/to/originals
```

This verifies the supplied DOCX hashes and reports paragraph overlap and table-count discrepancies for inspection. The comparison is diagnostic, not a proof of complete mathematical or textual equivalence.

© 2026 Mateo Petel. All rights reserved.
