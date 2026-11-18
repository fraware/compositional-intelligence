# Typed Generativity — final editorial audit (V5)

## Summary

The final manuscript is an edited publication candidate derived from scientific revision V4. Changes are deliberately concentrated: the essay's central mathematical distinctions and the independent status of its empirical hypotheses are retained, while implementation-heavy protocol language is moved from Section 7.4 into an explicit companion document. The entire original 15-table inventory is byte-identical to the uploaded Markdown, including all 81 rows and 227 data cells. No results of actual model experiments are claimed.

## Specific editorial decisions

1. Preserved the probabilistic target-selection/construction schema and its non-identifiability boundary; shortened the optional measure-theoretic discussion without equating a postulated latent variable with an observed mechanism.
2. Replaced the 984-word Section 7.4 narrative with a compact, complete outline of the randomized comparison, domain-specific endpoint, fixed-corpus estimand, missing outcomes, provenance controls, inference limits, and independent adjudication. The full earlier text was exported unaltered into `typed_generativity_full_evaluation_protocol_v4.md`.
3. Corrected the benchmark-contract appendix reference to the actual `v0.2` schema filename.
4. Expanded the reference for *Search-Time Data Contamination* to include the four authors (Han, Mankikar, Michael, Wang), verified against the arXiv record.
5. Tightened the proposed 150-item pilot description to distinguish declared maximum resources from realized token and time usage.
6. Clarified that the literature review supports a proposed evaluation design, rather than measured incremental validity or usability.
7. Made the closing statement conditional on discriminating experiments and independent assessments.

## Source and structure checks

| Check | Result |
|---|---|
| Original source Markdown SHA-256 | `be0e735525199bbd17355895956f78b23e96e6efdc1843eb13ded2ac7969c98e` |
| Final publication draft SHA-256 | `72077f9d10402667c96b1838daef6a7c130214d739b64bdd29dea57c649e2776` |
| Original HTML table equality | **15/15**, complete fragments identical |
| Original table body rows | **81/81** |
| Original table data cells | **227/227** |
| Original heading IDs retained | **Yes** |
| Final heading count | **34** |
| Duplicate HTML IDs in final source | **0** |
| Converted HTML tables/rows/cells | **15 / 81 / 227** |
| Browser / print / deployed website review | **Not performed** |
| Validator regression tests | **32/32 passed** |
| Synthetic validation CLI and reference JSON | **Matched** |
| Final body text word count | **6986** (V4: **7524**) |

## External source checks

Publication records inspected during this pass include Osera and Zdancewic (PLDI 2015), Polikarpova et al. (PLDI 2016), Scholak et al. (EMNLP 2021), Synchromesh (ICLR 2022), LeanDojo (NeurIPS 2023), Park et al. (ICML 2025), Mündler et al. (ICLR 2026), Hubert et al. (*Nature* 2026), NIST AI 800-3 (2026), the Lean language reference, Evan Miller (arXiv 2024), and Han et al. (arXiv 2025). The published *Nature* article lists first online publication as 12 November 2025 and version of record as 13 March 2026. The manuscript cites the 2026 journal version. These checks concern metadata and the suitability of the cited work; they do not independently reproduce the cited experiments.

## Remaining claims and trust boundaries

- The Type-First Prompting Harness is a protocol proposal without completed model runs.
- Six domain acceptance rubrics remain uncalibrated; no domain expert has independently validated the proposed thresholds or error sensitivity.
- No frozen trial manifest, runner, authenticated logs, or randomized confirmatory experiment exists within the package.
- The validator ensures selected structural properties of user-supplied JSON; it does not certify scientific meaning, experimental allocation, trustworthy tool effects, or actual assessor independence.
- The source DOCX identified by the original comment is not used as a byte comparison in this pass; the uploaded Markdown is the authoritative comparator.
- Production website integration is pending. The site's Pandoc 3.1.13, dedicated essay renderer, test suite, styling, mobile and print checks must be run before making publication claims.

## Publication decision

**Recommended as an editorial manuscript for expert review, not as a validated empirical paper.** Future publication requires at least the production-site build and browser QA. The empirical contribution requires independently calibrated rubrics, held-out tasks, and actual randomized trials before stronger claims.
