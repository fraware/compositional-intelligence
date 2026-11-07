# Typed Generativity

*Mateo Petel*

## Abstract

Typed Generativity is the generation layer of the Compositional Intelligence series. Semantic Participation asks when generated outputs count as artifacts in structured worlds. Typed Generativity asks how generation should be analyzed once the requested product is treated as a candidate artifact instead of a bare token sequence. The central claim is that many high-value generative tasks are usefully modeled as probabilistic construction of candidate inhabitants of inferred target types.

Typed Generativity proposes an operational decomposition of candidate generation. Under a normalized joint model distribution over declared target labels A and candidate representations t, P_theta(A,t \| c) = P_theta(A \| c) P_theta(t \| A,c), where c denotes generator context. This is the probability chain rule, not a model-specific theorem. Candidate representations include outputs later rejected by a validator. In a formal object language, a separate environment Δ and target type τ govern Δ ⊢ t : τ, with the correspondence from label A to type τ explicitly declared. Schema-governed and semi-formal tasks need independent validators or annotation protocols. Internal type-like representations remain an untested empirical hypothesis. The probabilistic factorization holds for any normalized joint law and supplies no evidence of a literal internal infer-then-generate mechanism. A mechanism claim needs independent intervention or causal evidence. The proposed Type-First Prompting Harness should compare diagnostic and downstream gains against information-, token-, and checker-exposure-matched controls. Pre-generation target commitments and labels reconstructed from outputs are distinct observations.

The essay separates three levels of typed generation. Typed output concerns artifacts checked after generation. Typed decoding concerns generation constrained by a schema, grammar, type, tool interface, or parser. Typed latent cognition names the stronger hypothesis that a system internally represents requested object structure in type-like ways before or during generation. The first two levels support immediate evaluation. The third requires targeted evidence from interventions, probes, ambiguity datasets, and failure clustering.

The companion evaluation object is the Type-First Prompting Harness v0.3. It tests whether explicit target-type articulation improves generation across code, Lean or mathematics, explanation, scientific protocol design, planning, and tool-use tasks. The essay succeeds if it gives researchers a precise way to distinguish target-type failure, invalid inhabitant failure, valid non-participation, and transformation instability. It leads directly to Functorial Consistency, which asks whether generated artifacts preserve structure across representations.

## Contribution summary



<table>
<colgroup>
<col style="width: 6%"/>
<col style="width: 29%"/>
<col style="width: 64%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th><strong>Contribution</strong></th>
<th><strong>Publication claim</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>C1</td>
<td>Generation schema</td>
<td>Where a normalized joint distribution is defined: P_theta(A,t | c) = P_theta(A | c) P_theta(t | A,c). Validation and formal typing are separate.</td>
</tr>
<tr class="even">
<td>C2</td>
<td>Target-type failure diagnosis</td>
<td>Many model errors are more precisely classified as wrong target type, invalid inhabitant, type drift, constraint omission, or valid non-participation.</td>
</tr>
<tr class="odd">
<td>C3</td>
<td>Three-level distinction</td>
<td>Typed output and typed decoding are operational evaluation layers; typed latent cognition remains a testable hypothesis.</td>
</tr>
<tr class="even">
<td>C4</td>
<td>Type-First Prompting Harness</td>
<td>The proposed harness tests whether explicit target-type articulation improves artifact validity, alignment, repair, downstream use, and transformation stability.</td>
</tr>
<tr class="odd">
<td>C5</td>
<td>Bridge to Functorial Consistency</td>
<td>Typed generation supplies the candidate objects whose transformations are evaluated through commutation-square tests.</td>
</tr>
<tr class="even">
<td>C6</td>
<td>Boundary control</td>
<td>The essay uses type-theoretic vocabulary as an operational abstraction and avoids claims that language models instantiate dependent type theory.</td>
</tr>
</tbody>
</table>



## Reader map



<table>
<colgroup>
<col style="width: 29%"/>
<col style="width: 70%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Reader</strong></th>
<th><strong>Recommended path</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AI evaluation researcher</td>
<td>Sections 1, 4, 5, 8, 9, and Appendix B</td>
</tr>
<tr class="even">
<td>Formal-methods researcher</td>
<td>Sections 2, 3, 6.2, 7.2, 8, and Appendix A</td>
</tr>
<tr class="odd">
<td>Program-synthesis researcher</td>
<td>Sections 3, 5, 6.1, 7.1, 8, and 10</td>
</tr>
<tr class="even">
<td>AI-for-science reader</td>
<td>Sections 6.4, 7.4, 8, 9, and 11</td>
</tr>
<tr class="odd">
<td>Series reader</td>
<td>Read after Essay 1 and before Essay 3</td>
</tr>
</tbody>
</table>



## 1. Position in the Compositional Intelligence series {#1-position-in-the-compositional-intelligence-series}

Typed Generativity occupies the transition between artifact membership and transformation-preserving evaluation. Essay 1 defines Semantic Participation as the condition under which an AI-generated object can enter a structured environment with validation, alignment, warrant, and permitted use. Essay 2 asks how the object is generated. Essay 3 then tests whether the generated object changes correctly under structured transformations.

semantic membership -\> target-type inference -\> candidate inhabitant -\> transformation preservation

This position determines the essay's scope. A proof, program, protocol, plan, tool call, or explanation needs dependencies, validators, assumptions, epistemic status, and permitted-use conditions in order to participate in a target environment. A generative system should therefore be evaluated by how it identifies the requested object class before it constructs a candidate. Many failures attributed to weak reasoning or weak retrieval are more accurately diagnosed as failures of target-type inference.

Typed Generativity converts the external standard of Semantic Participation into an internal diagnostic for generation. The wrong answer can arise from incorrect target selection, incomplete constraint extraction, invalid inhabitant construction, unstable target maintenance, or local validity without world membership. These cases require different interventions and should be separated at benchmark time.

## 2. Thesis and scope control {#2-thesis-and-scope-control}

The proposal models a class of generative tasks as inference over target-class labels followed by production of candidate representations. A candidate is submitted to independent validation, review, repair, and semantic participation assessment; successful type inhabitation is an outcome of checking, not a premise of sampling.

generator context c → infer target label A → propose candidate t → validate under task rules (Δ ⊢ t : τ where formally applicable) → assess ParticipationStatus for the proposed use

In proof assistants and type-directed program synthesis, a target proposition, type, or refinement specification is explicit under a declared formal environment <span class="citation-group" data-review="unapproved" data-target="TYPED-GENERATIVITY-P014" data-scope-id="TYPED-GENERATIVITY-P014-1" data-source-keys="LeanRef,TPIL4,Polikarpova2016">[<a class="citation-link" href="#ref-LeanRef" aria-label="Provisional reference 1 — The Lean Language Reference">1</a>, <a class="citation-link" href="#ref-TPIL4" aria-label="Provisional reference 2 — Theorem Proving in Lean 4">2</a>, <a class="citation-link" href="#ref-Polikarpova2016" aria-label="Provisional reference 3 — Program Synthesis from Polymorphic Refinement Types">3</a>]</span>. For tool use, interface definitions constrain valid arguments and actions; Toolformer studies model-selected API calls <span class="citation-group" data-review="unapproved" data-target="TYPED-GENERATIVITY-P014" data-scope-id="TYPED-GENERATIVITY-P014-2" data-source-keys="Toolformer2023">[<a class="citation-link" href="#ref-Toolformer2023" aria-label="Provisional reference 4 — Toolformer: Language Models Can Teach Themselves to Use Tools">4</a>]</span>. Structured output may likewise be checked against an application-defined schema. Explanation, planning, scientific protocol design, and structured writing are exploratory domains proposed in this essay. Treating their targets as latent types is a modeling hypothesis that needs domain-specific validation and evaluation.

Typed Generativity is an operational abstraction over the object layer of generation. A code string is judged as a program. A proof script is elaborated as a formal object. A JSON response is consumed through a schema. A scientific protocol encodes controls, measurements, uncertainty, stopping criteria, analysis plans, and permitted claims. A plan encodes a state transformation under constraints. The abstraction is useful to the extent that it improves diagnosis, validation, repair, and downstream artifact use.

## 3. Central schema {#3-central-schema}

The central schema records generation at the level of candidate artifact construction.

P_theta(A,t \| c) = P_theta(A \| c) P_theta(t \| A,c)

Let c denote a generation context and Ω_c a finite or countable tagged candidate space of pairs (A,t), with target-class label A and candidate representation t. A normalized joint probability mass P_theta(A,t | c) satisfies P_theta(A,t | c) = P_theta(A | c) P_theta(t | A,c) for classes with P_theta(A | c) > 0. At zero marginal probability, the joint law leaves the conditional distribution undetermined. Invalid and malformed candidates remain in the sampling space. In formally checkable tasks, a declared partial mapping μ_c(A) = τ associates eligible target classes with object-language types, and a separate parser and checker assess Δ ⊢ parse(t) : τ where defined. Schema-governed and semi-formal tasks use separately declared validation or annotation protocols. The factorization is the probability chain rule; its empirical usefulness and any type-inference mechanism remain independent questions.



<table>
<colgroup>
<col style="width: 11%"/>
<col style="width: 33%"/>
<col style="width: 55%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Symbol</strong></th>
<th><strong>Meaning</strong></th>
<th><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Gamma</td>
<td>Context available to the system</td>
<td>Prompt, retrieved lemmas, tool schema, codebase, prior interaction</td>
</tr>
<tr class="even">
<td>A</td>
<td>Inferred target type or object class</td>
<td>ProofSketch, LeanStatement, Program, ExperimentalProtocol, Plan</td>
</tr>
<tr class="odd">
<td>t</td>
<td>Candidate inhabitant</td>
<td>Proof script, function, explanation, protocol, plan, tool call</td>
</tr>
<tr class="even">
<td>theta</td>
<td>Model or system</td>
<td>LLM, theorem prover, code model, agent policy, decoding system</td>
</tr>
<tr class="odd">
<td>P_theta</td>
<td>Distribution, ranking, or search over candidates</td>
<td>Sampling distribution, beam ranking, constrained decoding distribution, search policy</td>
</tr>
</tbody>
</table>



The schema separates failures that ordinary output evaluation tends to collapse. A system can infer the right target type and fail to construct a valid inhabitant. It can construct a locally valid inhabitant of the wrong type. It can construct a valid object whose assumptions, dependencies, or permitted uses block Semantic Participation. This separation is the main diagnostic contribution of the essay.

## 4. Latent target types and underspecified prompts {#4-latent-target-types-and-underspecified-prompts}

Target types are frequently latent under natural-language prompting. The prompt "Explain compactness" can request an expert summary, undergraduate explanation, proof sketch, model-theoretic statement, topology example, historical note, or Lean formalization guide. The prompt "write the function" can request a pure function, API-compatible implementation, vectorized operation, memory-safe patch, or testable reference implementation. The prompt "design an experiment" can request a literature plan, executable protocol, statistical design, lab automation workflow, or claim-warrant record.



<table>
<colgroup>
<col style="width: 18%"/>
<col style="width: 37%"/>
<col style="width: 44%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Prompt family</strong></th>
<th><strong>Candidate target types</strong></th>
<th><strong>Typical target-type failure</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Mathematics</td>
<td>ProofSketch, FormalStatement, LeanProof, Counterexample, Intuition</td>
<td>Provides intuition when a formal statement or proof obligation was requested.</td>
</tr>
<tr class="even">
<td>Code</td>
<td>Function, Patch, APIAdapter, TestSuite, Query, Refactor</td>
<td>Produces syntactically valid code under the wrong behavioral contract.</td>
</tr>
<tr class="odd">
<td>Science</td>
<td>Protocol, Hypothesis, LiteraturePlan, SimulationPlan, EvidenceRecord</td>
<td>Gives general advice when an executable protocol or evidence record was needed.</td>
</tr>
<tr class="even">
<td>Explanation</td>
<td>ExpertSummary, Tutorial, Analogy, FormalDerivation, DebuggingGuide</td>
<td>Selects the wrong audience, precision level, or warrant level.</td>
</tr>
<tr class="odd">
<td>Planning</td>
<td>Checklist, Schedule, StateTransitionPlan, RiskPlan, RecoveryPlan</td>
<td>Lists steps without preconditions, resource dependencies, authority, or recovery path.</td>
</tr>
</tbody>
</table>



A well-calibrated system should sometimes preserve ambiguity instead of forcing a single target. Target-type inference should therefore record candidate target types, selection rationale, unresolved ambiguity, invalid target examples, and validation criteria. This record improves generation only if it changes the candidate artifact or the repair path.

## 5. Three levels of typed generation {#5-three-levels-of-typed-generation}



<table>
<colgroup>
<col style="width: 18%"/>
<col style="width: 28%"/>
<col style="width: 27%"/>
<col style="width: 26%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Level</strong></th>
<th><strong>Definition</strong></th>
<th><strong>Current status</strong></th>
<th><strong>Main test</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Level 1: typed output</td>
<td>The artifact is generated first and checked afterward.</td>
<td>Operational in proof assistants, compilers, schema validators, tests, and review pipelines.</td>
<td>Does validation distinguish valid, invalid, and misaligned artifacts?</td>
</tr>
<tr class="even">
<td>Level 2: typed decoding</td>
<td>Generation is constrained by a schema, grammar, type, parser, or tool interface.</td>
<td>Operational in structured-output systems, grammar-constrained decoding, tool interfaces, APIs, and formal languages.</td>
<td>Does the constraint improve validity and downstream use?</td>
</tr>
<tr class="odd">
<td>Level 3: typed latent cognition</td>
<td>The system internally represents requested object structure in type-like ways before or during generation.</td>
<td>Research hypothesis.</td>
<td>Do interventions, probes, ambiguity tests, and failure clusters reveal target-object representations?</td>
</tr>
</tbody>
</table>



The publication version should keep these levels distinct. Level 1 and Level 2 already support practical measurement. Level 3 is the scientific frontier. Evidence for Level 3 requires more than improved formatting. It requires showing that internal representations, decoding behavior, or failure patterns track target-object structure in ways that predict validity, repair, or transformation stability.

## 6. Domain examples {#6-domain-examples}

### 6.1 Code generation {#6-1-code-generation}

Code generation makes target-type failures visible as soon as syntax and local tests are separated from behavioral contracts and codebase membership.

Prompt: write a function that removes duplicates from a list and preserves the first occurrence order.\
A = forall alpha. List alpha -\> List alpha\
constraints = preserves order, preserves first occurrence, removes later duplicates, pure function, stable equality semantics\
t = candidate implementation



<table>
<colgroup>
<col style="width: 27%"/>
<col style="width: 72%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Failure</strong></th>
<th><strong>Meaning</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Target-type mismatch</td>
<td>Returns a set or sorted list when an order-preserving list function was requested.</td>
</tr>
<tr class="even">
<td>Constraint loss</td>
<td>Removes duplicates and loses first-occurrence order.</td>
</tr>
<tr class="odd">
<td>Invalid inhabitant</td>
<td>Has the apparent function type and fails edge cases.</td>
</tr>
<tr class="even">
<td>Valid non-participation</td>
<td>Passes local tests and violates project interface, dependency, or maintainability constraints.</td>
</tr>
</tbody>
</table>



### 6.2 Lean and mathematical formalization {#6-2-lean-and-mathematical-formalization}

Mathematical formalization shows why target-type inference cannot be reduced to checker acceptance. A formal statement can validate and still encode the wrong mathematical target.

Prompt: formalize a theorem stating that a continuous real-valued function on a compact interval attains a maximum.\
A = FormalTheoremStatement + optional proof obligation\
constraints = continuity, compact interval or compact set, point in domain, maximum attained, source-target alignment\
t = Lean theorem statement, definitions, proof sketch, or proof script

The target distinction is substantive. A statement about supremum existence differs from an attainment claim by the witness point in the domain. Typed Generativity identifies the requested object before Functorial Consistency tests whether specialization, translation, and formalization preserve the relevant structure.

### 6.3 Explanation {#6-3-explanation}

Explanation tasks are often misdiagnosed as failures of clarity when the deeper failure is wrong target-type selection. The requested object depends on audience, allowed simplification, notation, proof status, and permitted use.



<table>
<colgroup>
<col style="width: 32%"/>
<col style="width: 67%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Candidate target type</strong></th>
<th><strong>Validation criterion</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ExpertSummary</td>
<td>Precise statement, assumptions, consequences, and relation to adjacent results.</td>
</tr>
<tr class="even">
<td>UndergraduateExplanation</td>
<td>Accessible intuition, examples, and minimal formal prerequisites.</td>
</tr>
<tr class="odd">
<td>FormalProofSketch</td>
<td>Definitions, proof obligations, and logical dependencies.</td>
</tr>
<tr class="even">
<td>HistoricalContext</td>
<td>Origin, motivation, development, and influence.</td>
</tr>
<tr class="odd">
<td>LeanFormalizationGuide</td>
<td>Definitions, library names, theorem statement shape, and proof obligations.</td>
</tr>
</tbody>
</table>



### 6.4 Scientific protocol design {#6-4-scientific-protocol-design}

Scientific protocol design exposes the relation between target type and permitted claim. A surface-level answer can be fluent and still fail as a protocol if it omits controls, uncertainty, stopping criteria, or the evidential claim the protocol can support.

Prompt: design an experiment to test whether molecule X is stable under condition Y.\
A = ExperimentalProtocol(hypothesis, materials, controls, measurement, uncertainty, QC, stopping_conditions, analysis_plan, permitted_claim)



<table>
<colgroup>
<col style="width: 27%"/>
<col style="width: 72%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Failure</strong></th>
<th><strong>Meaning</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Protocol-type collapse</td>
<td>Gives general scientific advice instead of an executable protocol.</td>
</tr>
<tr class="even">
<td>Evidence-type mismatch</td>
<td>Treats simulation-derived support as empirical evidence.</td>
</tr>
<tr class="odd">
<td>Missing controls</td>
<td>Omits positive control, negative control, calibration control, or protocol-specific control.</td>
</tr>
<tr class="even">
<td>Missing uncertainty</td>
<td>Omits measurement uncertainty, replicate design, or statistical analysis plan.</td>
</tr>
<tr class="odd">
<td>Missing permitted claim</td>
<td>Fails to state which conclusion the protocol can support.</td>
</tr>
</tbody>
</table>



### 6.5 Planning and tool use {#6-5-planning-and-tool-use}

Planning and tool-use tasks treat generated objects as candidate state transformations. A plan is not merely a list of steps. It is a proposed transition from current state to goal state under time, resource, authority, and recovery constraints.

Prompt: plan how to prepare, run, and analyze a small experiment by tomorrow afternoon.\
A = Plan : CurrentState -\> GoalState\
constraints = time, resources, dependencies, authority, risk, recovery path

Tool calls are candidate inhabitants of action schemas. Once execution changes state, the effect and authority layer developed later in the series adds preconditions, postconditions, handlers, rollback paths, and audit traces.

## 7. Type-First Prompting Harness v0.3 {#7-type-first-prompting-harness-v0-3}

The Type-First Prompting Harness is an evaluation design. It tests whether explicit target-type articulation improves generation. It should be reported as a scientific probe of Typed Generativity, not as a prompting style.



<table>
<colgroup>
<col style="width: 20%"/>
<col style="width: 43%"/>
<col style="width: 35%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Condition</strong></th>
<th><strong>Instruction pattern</strong></th>
<th><strong>Purpose</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Direct generation</td>
<td>Answer the task immediately.</td>
<td>Baseline for ordinary generation.</td>
</tr>
<tr class="even">
<td>Type-first generation</td>
<td>Identify target type, constraints, ambiguity, invalid targets, and validator before generating.</td>
<td>Tests whether target-type articulation improves artifact quality.</td>
</tr>
<tr class="odd">
<td>Type-constrained generation</td>
<td>Generate under an explicit schema, grammar, type, or tool interface.</td>
<td>Tests typed decoding.</td>
</tr>
<tr class="even">
<td>Type-first plus checker</td>
<td>Receive validation feedback and repair.</td>
<td>Tests diagnosis and repair loops.</td>
</tr>
<tr class="odd">
<td>Ambiguity-aware generation</td>
<td>List candidate target types and resolve or preserve ambiguity.</td>
<td>Tests underspecified prompts.</td>
</tr>
</tbody>
</table>



### 7.1 Dataset schema {#7-1-dataset-schema}

type_first_item:\
task_id: string\
domain: code \| lean_math \| explanation \| scientific_protocol \| planning \| tool_use\
prompt: string\
intended_target_type: string\
candidate_target_types: list\[string\]\
constraints: list\[string\]\
invalid_target_type_examples: list\[string\]\
valid_inhabitant_criteria: list\[string\]\
checker_or_validator: string\
human_review_fields: list\[string\]\
ambiguity_status: explicit \| latent \| unresolved\
semantic_participation_target: string

### 7.2 Metrics {#7-2-metrics}



<table>
<colgroup>
<col style="width: 20%"/>
<col style="width: 46%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Metric</strong></th>
<th><strong>Definition</strong></th>
<th><strong>Interpretation</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Target-type accuracy</td>
<td>Agreement between inferred and intended object type.</td>
<td>Tests target-object inference.</td>
</tr>
<tr class="even">
<td>Constraint recall</td>
<td>Fraction of required constraints surfaced before generation.</td>
<td>Tests object specification.</td>
</tr>
<tr class="odd">
<td>Inhabitant validity</td>
<td>Whether the candidate passes relevant checks or review.</td>
<td>Tests construction quality.</td>
</tr>
<tr class="even">
<td>Semantic alignment</td>
<td>Whether the candidate preserves intended meaning.</td>
<td>Connects to Essay 1.</td>
</tr>
<tr class="odd">
<td>Repair cost</td>
<td>Number and complexity of repair steps after diagnostics.</td>
<td>Tests usefulness for iteration.</td>
</tr>
<tr class="even">
<td>Type stability</td>
<td>Whether generation remains within the inferred target type.</td>
<td>Detects type drift.</td>
</tr>
<tr class="odd">
<td>Downstream usability</td>
<td>Whether the artifact can be used in the target environment.</td>
<td>Tests Semantic Participation.</td>
</tr>
<tr class="even">
<td>Transformation stability</td>
<td>Whether the artifact behaves correctly under source or target transformations.</td>
<td>Connects to Essay 3.</td>
</tr>
<tr class="odd">
<td>Ambiguity handling</td>
<td>Whether unresolved target-type ambiguity is surfaced.</td>
<td>Rewards calibrated uncertainty.</td>
</tr>
</tbody>
</table>



### 7.3 Initial pilot {#7-3-initial-pilot}

A first curated pilot should contain 150 items distributed evenly across code, Lean or mathematical formalization, explanation, scientific protocol design, planning, and tool use. This size supports expert annotation and still exposes initial diagnostic signal. The first pilot should prioritize label quality over scale.

The primary analysis should classify every failure into at least three classes: wrong target type, right target type with invalid inhabitant, and valid inhabitant with failed semantic participation. A fourth class, transformation instability, should be added when the artifact fails a Functorial Consistency test.

## 8. Target-type and candidate-inhabitant records {#8-target-type-and-candidate-inhabitant-records}

Typed Generativity requires two lightweight records. The target_type_record records the object inferred before generation. The candidate_inhabitant_record records the generated candidate and its validation path. Together they connect generation to membership and transformation.



<table>
<colgroup>
<col style="width: 28%"/>
<col style="width: 35%"/>
<col style="width: 35%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Record</strong></th>
<th><strong>Core question</strong></th>
<th><strong>Primary downstream use</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>target_type_record</td>
<td>What object type did the system infer?</td>
<td>Disambiguation, constraint recall, validator selection.</td>
</tr>
<tr class="even">
<td>candidate_inhabitant_record</td>
<td>What object did the system construct?</td>
<td>Validation, repair, alignment, Semantic Participation.</td>
</tr>
<tr class="odd">
<td>type_failure_record</td>
<td>Where did the typed-generation pipeline fail?</td>
<td>Diagnostics, model comparison, benchmark reporting.</td>
</tr>
</tbody>
</table>



target_type_record:\
task_id: string\
context_summary: string\
candidate_target_types: list\[string\]\
selected_target_type: string\
selection_rationale: string\
constraints: list\[string\]\
invalid_target_examples: list\[string\]\
validator_or_review_method: string\
ambiguity_status: explicit \| latent \| unresolved\
downstream_environment: string\
\
candidate_inhabitant_record:\
task_id: string\
selected_target_type: string\
candidate: string \| object\
validation_status: unchecked \| checked \| failed \| partial \| reviewed\
validator: string\
alignment_status: aligned \| uncertain \| misaligned\
repair_trace: string \| null\
epistemic_type: string\
permitted_use: list\[string\]\
transformation_tests: list\[string\]

## 9. Relation to the state of the art {#9-relation-to-the-state-of-the-art}

Typed Generativity draws on established areas, each with a bounded source function. Curry-Howard supplies the proof-as-inhabitant analogy. Polymorphic refinement-type-directed synthesis uses declared refinement specifications to constrain recursive program construction <span class="citation-group" data-review="unapproved" data-target="TYPED-GENERATIVITY-P040" data-scope-id="TYPED-GENERATIVITY-P040-1" data-source-keys="Polikarpova2016">[<a class="citation-link" href="#ref-Polikarpova2016" aria-label="Provisional reference 3 — Program Synthesis from Polymorphic Refinement Types">3</a>]</span>. Lean and LeanDojo provide environments <span class="citation-group" data-review="unapproved" data-target="TYPED-GENERATIVITY-P040" data-scope-id="TYPED-GENERATIVITY-P040-2" data-source-keys="LeanRef,TPIL4,LeanDojo2023">[<a class="citation-link" href="#ref-LeanRef" aria-label="Provisional reference 1 — The Lean Language Reference">1</a>, <a class="citation-link" href="#ref-TPIL4" aria-label="Provisional reference 2 — Theorem Proving in Lean 4">2</a>, <a class="citation-link" href="#ref-LeanDojo2023" aria-label="Provisional reference 5 — LeanDojo: Theorem Proving with Retrieval-Augmented Language Models">5</a>]</span> in which generated proof artifacts can be checked and proof states can be extracted or manipulated programmatically. Structured-output and schema-constrained systems supply operational typed decoding for model interfaces. Tool-use systems show that generated text can encode calls <span class="citation-group" data-review="unapproved" data-target="TYPED-GENERATIVITY-P040" data-scope-id="TYPED-GENERATIVITY-P040-3" data-source-keys="Toolformer2023">[<a class="citation-link" href="#ref-Toolformer2023" aria-label="Provisional reference 4 — Toolformer: Language Models Can Teach Themselves to Use Tools">4</a>]</span> whose validity depends on interface schemas and arguments.



<table>
<colgroup>
<col style="width: 25%"/>
<col style="width: 39%"/>
<col style="width: 35%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Source area</strong></th>
<th><strong>What it supports</strong></th>
<th><strong>Boundary</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Curry-Howard and typed programming</td>
<td>Exact relations among propositions, types, proofs, and programs in formal settings.</td>
<td>The essay uses this as conceptual architecture for AI generation.</td>
</tr>
<tr class="even">
<td>Type-directed and example-directed synthesis</td>
<td>Search for inhabitants under explicit or example-refined specifications.</td>
<td>Typed Generativity adds latent target-type inference in LLM-era tasks.</td>
</tr>
<tr class="odd">
<td>Lean and LeanDojo</td>
<td>Formal checking, proof-state interaction, proof data, and learned theorem-proving infrastructure.</td>
<td>Formal validity remains separate from source-target alignment and Semantic Participation.</td>
</tr>
<tr class="even">
<td>Structured outputs and constrained decoding</td>
<td>Operational enforcement of schemas or grammars during generation.</td>
<td>Schema conformance alone does not establish semantic alignment or warrant.</td>
</tr>
<tr class="odd">
<td>Tool use</td>
<td>Generated artifacts can encode calls to external tools under interface constraints.</td>
<td>Action consequences require the later effect-record layer.</td>
</tr>
<tr class="even">
<td>Mathematical reasoning systems such as AlphaProof</td>
<td>Learned search can interact with formal reasoning in high-value mathematical tasks.</td>
<td>Contest performance does not establish the general Typed Generativity hypothesis.</td>
</tr>
</tbody>
</table>



The source boundary is strict. These literatures motivate the generation layer. They do not validate the original Type-First Prompting Harness, target_type_record, candidate_inhabitant_record, or Typed Generativity Bench.

## 10. Strongest objections {#10-strongest-objections}



<table>
<colgroup>
<col style="width: 24%"/>
<col style="width: 42%"/>
<col style="width: 32%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Objection</strong></th>
<th><strong>Response standard</strong></th>
<th><strong>Operational test</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This is type-directed synthesis under a new label.</td>
<td>Typed Generativity includes type-directed synthesis as a source tradition and extends the analysis to latent, probabilistic, underspecified, and non-programmatic generation.</td>
<td>Test open-ended prompts where the target type must be inferred before construction.</td>
</tr>
<tr class="even">
<td>Language models generate strings.</td>
<td>The essay studies the object that the string attempts to encode, such as a program, proof, protocol, plan, explanation, or tool call.</td>
<td>Compare token-level validity with object-level validation.</td>
</tr>
<tr class="odd">
<td>Prompt types are only genres.</td>
<td>Some target types are genres; others specify validators, constraints, interfaces, and permitted uses.</td>
<td>Measure whether target-type labels predict validation and repair beyond genre labels.</td>
</tr>
<tr class="even">
<td>Structured outputs already solve this.</td>
<td>Structured outputs solve part of typed decoding; they do not settle target-type inference, semantic alignment, epistemic status, or transformation stability.</td>
<td>Compare schema conformance with downstream participation.</td>
</tr>
<tr class="odd">
<td>Type-first prompting adds verbosity.</td>
<td>The harness treats this as a possible failure outcome.</td>
<td>Measure validity, repair cost, and transformation stability after controlling for output length.</td>
</tr>
<tr class="even">
<td>Many tasks have unstable target types.</td>
<td>Ambiguity-aware generation records candidate target types and unresolved ambiguity.</td>
<td>Evaluate ambiguity surfacing and user-clarification quality.</td>
</tr>
<tr class="odd">
<td>Latent cognition is unobservable.</td>
<td>The essay labels it as a hypothesis and requires interventions, probes, ambiguity datasets, and failure clustering.</td>
<td>Require evidence beyond output-format improvement.</td>
</tr>
</tbody>
</table>



## 11. Failure taxonomy and kill criteria {#11-failure-taxonomy-and-kill-criteria}



<table>
<colgroup>
<col style="width: 22%"/>
<col style="width: 41%"/>
<col style="width: 36%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Failure</strong></th>
<th><strong>Meaning</strong></th>
<th><strong>Repair path</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Target-type ambiguity</td>
<td>Several plausible object types fit the prompt.</td>
<td>Surface alternatives, ask for clarification, or preserve ambiguity.</td>
</tr>
<tr class="even">
<td>Target-type mismatch</td>
<td>The system selects the wrong object class.</td>
<td>Re-infer target type and validators.</td>
</tr>
<tr class="odd">
<td>Target-type drift</td>
<td>Generation starts under one target type and ends under another.</td>
<td>Add type-stability checks.</td>
</tr>
<tr class="even">
<td>Constraint omission</td>
<td>Required constraints are absent before construction.</td>
<td>Extract constraints before generation.</td>
</tr>
<tr class="odd">
<td>Invalid inhabitant</td>
<td>Right target type and failed validation.</td>
<td>Use checker or reviewer diagnostics for repair.</td>
</tr>
<tr class="even">
<td>Valid non-participation</td>
<td>Local validity with failed semantic membership.</td>
<td>Add alignment, dependency, and permitted-use records.</td>
</tr>
<tr class="odd">
<td>Transformation instability</td>
<td>Artifact fails under a structured transformation.</td>
<td>Move to Functorial Consistency diagnostics.</td>
</tr>
<tr class="even">
<td>Verbosity artifact</td>
<td>Type-first condition improves apparent rigor without improving outcomes.</td>
<td>Ablate length and record fields.</td>
</tr>
</tbody>
</table>



The proposal should be revised under the following conditions.

-   K1. Type-first interventions do not improve validity, alignment, repair cost, ambiguity handling, downstream usability, or transformation stability.

-   K2. Target-type labels fail to predict errors beyond ordinary task labels or genre labels.

-   K3. Human annotators cannot agree on target types after task-specific guidelines.

-   K4. Structured-output constraints dominate all gains, leaving no additional value for target-type inference.

-   K5. The harness adds annotation cost without diagnostic signal.

-   K6. Latent-cognition probes fail to distinguish target-object structure from surface format or topic.

-   K7. The framework cannot connect generated candidates to Semantic Participation or Functorial Consistency.

## 12. Conclusion and transition to Functorial Consistency {#12-conclusion-and-transition-to-functorial-consistency}

Typed Generativity supplies the candidate-production component of Compositional Intelligence. The framework separates target-class inference, candidate construction, independent validation, repair, semantic participation, and transformation stability, while reserving formal inhabitant status for candidates accepted under the stated type system.

The next essay asks whether those generated objects preserve structure. Once a model constructs a candidate proof, program, semantic parse, protocol, or plan, the central test is path agreement across source and target representations under an explicit equivalence regime. Typed Generativity supplies the candidate object. Functorial Consistency supplies the evaluation square.

Typed Generativity: P_theta(A,t \| c) = P_theta(A \| c) P_theta(t \| A,c), for a declared normalized joint model. Formal typing, where applicable, uses Δ ⊢ t : τ. Functorial Consistency: T_1(f(x)) R g(T_0(x)), under a declared relation, orientation, and comparison procedure.

## Appendix A. Claim levels {#appendix-a-claim-levels}



<table>
<colgroup>
<col style="width: 9%"/>
<col style="width: 33%"/>
<col style="width: 56%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Level</strong></th>
<th><strong>Meaning</strong></th>
<th><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>L0</td>
<td>Established technical background</td>
<td>Proof assistants can check formal proof artifacts.</td>
</tr>
<tr class="even">
<td>L1</td>
<td>Documented system capability or empirical result</td>
<td>LeanDojo extracts proof states and enables programmatic Lean interaction; structured-output systems enforce supplied schemas.</td>
</tr>
<tr class="odd">
<td>L2</td>
<td>Interpretive synthesis</td>
<td>Code, theorem proving, structured outputs, and tool calls expose typed-output and typed-decoding layers.</td>
</tr>
<tr class="even">
<td>L3</td>
<td>Original proposal</td>
<td>Typed Generativity as target-type inference plus candidate-inhabitant construction.</td>
</tr>
<tr class="odd">
<td>L4</td>
<td>Testable hypothesis</td>
<td>Some systems can encode target-object structure internally beyond surface genre cues.</td>
</tr>
</tbody>
</table>



## Appendix B. Benchmark item schema {#appendix-b-benchmark-item-schema}

typed_generativity_benchmark_item:\
id: string\
domain: string\
prompt: string\
intended_target_type: string\
candidate_target_types: list\[string\]\
constraints: list\[string\]\
invalid_target_examples: list\[string\]\
valid_inhabitant_criteria: list\[string\]\
validator: string\
semantic_participation_target: string\
transformation_tests: list\[string\]\
reviewer_guidelines: string\
failure_labels: list\[string\]


<section class="bibliography" aria-labelledby="references-heading" data-review="unapproved">
<h2 id="references-heading">References (provisional)</h2>
<p class="bibliography-note">Source-scoped working citations. Text and references await specialist and author review.</p>
<ol class="references-list">
<li id="ref-LeanRef" data-source-key="LeanRef" data-provisional="true"><span class="ref-key">[1]</span>. <a href="https://lean-lang.org/doc/reference/latest/" rel="noopener noreferrer">The Lean Language Reference</a>. <span class="ref-details">Lean Community · online reference.</span></li>
<li id="ref-TPIL4" data-source-key="TPIL4" data-provisional="true"><span class="ref-key">[2]</span>. <a href="https://docs.lean-lang.org/theorem_proving_in_lean4/" rel="noopener noreferrer">Theorem Proving in Lean 4</a>. <span class="ref-details">Avigad, de Moura, Kong, and Ullrich · online textbook.</span></li>
<li id="ref-Polikarpova2016" data-source-key="Polikarpova2016" data-provisional="true"><span class="ref-key">[3]</span>. <a href="https://dspace.mit.edu/entities/publication/c3dcde41-ff5d-442d-b1c1-4f269c8896ef" rel="noopener noreferrer">Program Synthesis from Polymorphic Refinement Types</a>. <span class="ref-details">Polikarpova, Kuraj, and Solar-Lezama · PLDI 2016, pp. 522–538.</span></li>
<li id="ref-Toolformer2023" data-source-key="Toolformer2023" data-provisional="true"><span class="ref-key">[4]</span>. <a href="https://proceedings.neurips.cc/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html" rel="noopener noreferrer">Toolformer: Language Models Can Teach Themselves to Use Tools</a>. <span class="ref-details">Schick et al. · NeurIPS 2023.</span></li>
<li id="ref-LeanDojo2023" data-source-key="LeanDojo2023" data-provisional="true"><span class="ref-key">[5]</span>. <a href="https://proceedings.neurips.cc/paper_files/paper/2023/hash/4441469427094f8873d0fecb0c4e1cee-Abstract-Datasets_and_Benchmarks.html" rel="noopener noreferrer">LeanDojo: Theorem Proving with Retrieval-Augmented Language Models</a>. <span class="ref-details">Yang et al. · NeurIPS 2023.</span></li>
</ol>
</section>
