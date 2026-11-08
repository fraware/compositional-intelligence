# Typed Generativity

*Mateo Petel*

<!-- AUTHORITATIVE-DOCX SHA256 174be720ce13dfaf0196ad51a5f35c02810fc8bd0a00356399f0ab4baf67e028; source Essay2_Typed_Generativity_V3(1).docx -->

<h2 id="abstract">Abstract</h2>
<p>Typed Generativity is the generation layer of the Compositional Intelligence series. Semantic Participation asks when generated outputs count as artifacts in structured worlds. Typed Generativity asks how generation should be analyzed once the requested product is treated as a candidate artifact instead of a bare token sequence. The central claim is that many high-value generative tasks are usefully modeled as probabilistic construction of candidate inhabitants of inferred target types.</p>
<p>The core schema is P_theta(t : A | Gamma). Gamma denotes the context available to the system, including prompt, retrieved material, examples, library state, tool state, memory, system instructions, and target environment. A denotes the inferred target type or target object class. t denotes the candidate inhabitant. P_theta denotes the model distribution, ranking, or search policy over candidate inhabitants under the available context. The schema is exact in proof-assistant and typed-programming settings, operational in schema-constrained generation, and semi-formal in explanation, planning, scientific protocol design, and other structured artifact tasks.</p>
<p>The essay separates three levels of typed generation. Typed output concerns artifacts checked after generation. Typed decoding concerns generation constrained by a schema, grammar, type, tool interface, or parser. Typed latent cognition names the stronger hypothesis that a system internally represents requested object structure in type-like ways before or during generation. The first two levels support immediate evaluation. The third requires targeted evidence from interventions, probes, ambiguity datasets, and failure clustering.</p>
<p>The companion evaluation object is the Type-First Prompting Harness v0.3. It tests whether explicit target-type articulation improves generation across code, Lean or mathematics, explanation, scientific protocol design, planning, and tool-use tasks. The essay succeeds if it gives researchers a precise way to distinguish target-type failure, invalid inhabitant failure, valid non-participation, and transformation instability. It leads directly to Functorial Consistency, which asks whether generated artifacts preserve structure across representations.</p>
<h2 id="contribution-summary">Contribution summary</h2>
<p class="table-display-caption" id="table-1-caption">Table 1. ID, Contribution, Publication claim</p>
<div aria-labelledby="table-1-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="1" id="table-1"><caption class="visually-hidden">Table 1. ID, Contribution, Publication claim</caption>
<colgroup>
<col style="width: 6%"/>
<col style="width: 29%"/>
<col style="width: 64%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>ID</strong></th>
<th scope="col"><strong>Contribution</strong></th>
<th scope="col"><strong>Publication claim</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>C1</td>
<td>Generation schema</td>
<td>P_theta(t : A | Gamma) models generation as target-type inference followed by candidate-inhabitant construction.</td>
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
</table></div>
<h2 id="reader-map">Reader map</h2>
<p class="table-display-caption" id="table-2-caption">Table 2. Reader, Recommended path</p>
<div aria-labelledby="table-2-caption" class="table-scroll" data-columns="2" role="group" tabindex="0"><table data-source-table="2" id="table-2"><caption class="visually-hidden">Table 2. Reader, Recommended path</caption>
<colgroup>
<col style="width: 29%"/>
<col style="width: 70%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Reader</strong></th>
<th scope="col"><strong>Recommended path</strong></th>
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
</table></div>
<h2 id="position-in-the-compositional-intelligence-series">1. Position in the Compositional Intelligence series</h2>
<p>Typed Generativity occupies the transition between artifact membership and transformation-preserving evaluation. Essay 1 defines Semantic Participation as the condition under which an AI-generated object can enter a structured environment with validation, alignment, warrant, and permitted use. Essay 2 asks how the object is generated. Essay 3 then tests whether the generated object changes correctly under structured transformations.</p>
<p>semantic membership -&gt; target-type inference -&gt; candidate inhabitant -&gt; transformation preservation</p>
<p>This position determines the essay’s scope. A proof, program, protocol, plan, tool call, or explanation needs dependencies, validators, assumptions, epistemic status, and permitted-use conditions in order to participate in a target environment. A generative system should therefore be evaluated by how it identifies the requested object class before it constructs a candidate. Many failures attributed to weak reasoning or weak retrieval are more accurately diagnosed as failures of target-type inference.</p>
<p>Typed Generativity converts the external standard of Semantic Participation into an internal diagnostic for generation. The wrong answer can arise from incorrect target selection, incomplete constraint extraction, invalid inhabitant construction, unstable target maintenance, or local validity without world membership. These cases require different interventions and should be separated at benchmark time.</p>
<h2 id="thesis-and-scope-control">2. Thesis and scope control</h2>
<p>The thesis is that many high-value AI generations can be analyzed as probabilistic construction of candidate inhabitants of inferred target types. A system receives context, infers an object class, constructs a candidate, and submits that candidate to validation, review, repair, and semantic-membership assessment.</p>
<p>Gamma -&gt; infer A -&gt; construct t : A -&gt; validate/repair -&gt; semantic participation</p>
<p>The claim has different status across domains. In proof assistants and typed programming languages, the target type can be explicit. In structured outputs, the schema can be supplied. In tool-use settings, the target action schema can be given by an interface. In explanation, planning, scientific protocol design, and structured writing, the target type is often latent, underspecified, and partly negotiated by context. The notation is valid only when the validation regime and claim level are stated.</p>
<p>Typed Generativity is an operational abstraction over the object layer of generation. A code string is judged as a program. A proof script is elaborated as a formal object. A JSON response is consumed through a schema. A scientific protocol encodes controls, measurements, uncertainty, stopping criteria, analysis plans, and permitted claims. A plan encodes a state transformation under constraints. The abstraction is useful to the extent that it improves diagnosis, validation, repair, and downstream artifact use.</p>
<h2 id="central-schema">3. Central schema</h2>
<p>The central schema records generation at the level of candidate artifact construction.</p>
<p>P_theta(t : A | Gamma)</p>
<p>Gamma is the available context. It can include prompt, interaction history, retrieved material, examples, system instructions, tool state, memory, library state, source artifact, and target environment. A is the inferred target type or target object class. t is the candidate inhabitant. theta denotes the model or system. P_theta denotes a distribution, ranking, search policy, or constrained decoding process over candidate inhabitants.</p>
<p class="table-display-caption" id="table-3-caption">Table 3. Symbol, Meaning, Example</p>
<div aria-labelledby="table-3-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="3" id="table-3"><caption class="visually-hidden">Table 3. Symbol, Meaning, Example</caption>
<colgroup>
<col style="width: 11%"/>
<col style="width: 33%"/>
<col style="width: 55%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Symbol</strong></th>
<th scope="col"><strong>Meaning</strong></th>
<th scope="col"><strong>Example</strong></th>
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
</table></div>
<p>The schema separates failures that ordinary output evaluation tends to collapse. A system can infer the right target type and fail to construct a valid inhabitant. It can construct a locally valid inhabitant of the wrong type. It can construct a valid object whose assumptions, dependencies, or permitted uses block Semantic Participation. This separation is the main diagnostic contribution of the essay.</p>
<h2 id="latent-target-types-and-underspecified-prompts">4. Latent target types and underspecified prompts</h2>
<p>Target types are frequently latent under natural-language prompting. The prompt “Explain compactness” can request an expert summary, undergraduate explanation, proof sketch, model-theoretic statement, topology example, historical note, or Lean formalization guide. The prompt “write the function” can request a pure function, API-compatible implementation, vectorized operation, memory-safe patch, or testable reference implementation. The prompt “design an experiment” can request a literature plan, executable protocol, statistical design, lab automation workflow, or claim-warrant record.</p>
<p class="table-display-caption" id="table-4-caption">Table 4. Prompt family, Candidate target types, Typical target-type failure</p>
<div aria-labelledby="table-4-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="4" id="table-4"><caption class="visually-hidden">Table 4. Prompt family, Candidate target types, Typical target-type failure</caption>
<colgroup>
<col style="width: 18%"/>
<col style="width: 37%"/>
<col style="width: 44%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Prompt family</strong></th>
<th scope="col"><strong>Candidate target types</strong></th>
<th scope="col"><strong>Typical target-type failure</strong></th>
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
</table></div>
<p>A well-calibrated system should sometimes preserve ambiguity instead of forcing a single target. Target-type inference should therefore record candidate target types, selection rationale, unresolved ambiguity, invalid target examples, and validation criteria. This record improves generation only if it changes the candidate artifact or the repair path.</p>
<h2 id="three-levels-of-typed-generation">5. Three levels of typed generation</h2>
<p class="table-display-caption" id="table-5-caption">Table 5. Level, Definition, Current status, Main test</p>
<div aria-labelledby="table-5-caption" class="table-scroll" data-columns="4" role="group" tabindex="0"><table data-source-table="5" id="table-5"><caption class="visually-hidden">Table 5. Level, Definition, Current status, Main test</caption>
<colgroup>
<col style="width: 18%"/>
<col style="width: 28%"/>
<col style="width: 27%"/>
<col style="width: 26%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Level</strong></th>
<th scope="col"><strong>Definition</strong></th>
<th scope="col"><strong>Current status</strong></th>
<th scope="col"><strong>Main test</strong></th>
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
</table></div>
<p>The publication version should keep these levels distinct. Level 1 and Level 2 already support practical measurement. Level 3 is the scientific frontier. Evidence for Level 3 requires more than improved formatting. It requires showing that internal representations, decoding behavior, or failure patterns track target-object structure in ways that predict validity, repair, or transformation stability.</p>
<h2 id="domain-examples">6. Domain examples</h2>
<h3 id="code-generation">6.1 Code generation</h3>
<p>Code generation makes target-type failures visible as soon as syntax and local tests are separated from behavioral contracts and codebase membership.</p>
<p>Prompt: write a function that removes duplicates from a list and preserves the first occurrence order.<br/>
A = forall alpha. List alpha -&gt; List alpha<br/>
constraints = preserves order, preserves first occurrence, removes later duplicates, pure function, stable equality semantics<br/>
t = candidate implementation</p>
<p class="table-display-caption" id="table-6-caption">Table 6. Failure, Meaning — Failure, Meaning</p>
<div aria-labelledby="table-6-caption" class="table-scroll" data-columns="2" role="group" tabindex="0"><table data-source-table="6" id="table-6"><caption class="visually-hidden">Table 6. Failure, Meaning — Failure, Meaning</caption>
<colgroup>
<col style="width: 27%"/>
<col style="width: 72%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Failure</strong></th>
<th scope="col"><strong>Meaning</strong></th>
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
</table></div>
<h3 id="lean-and-mathematical-formalization">6.2 Lean and mathematical formalization</h3>
<p>Mathematical formalization shows why target-type inference cannot be reduced to checker acceptance. A formal statement can validate and still encode the wrong mathematical target.</p>
<p>Prompt: formalize a theorem stating that a continuous real-valued function on a compact interval attains a maximum.<br/>
A = FormalTheoremStatement + optional proof obligation<br/>
constraints = continuity, compact interval or compact set, point in domain, maximum attained, source-target alignment<br/>
t = Lean theorem statement, definitions, proof sketch, or proof script</p>
<p>The target distinction is substantive. A statement about supremum existence differs from an attainment claim by the witness point in the domain. Typed Generativity identifies the requested object before Functorial Consistency tests whether specialization, translation, and formalization preserve the relevant structure.</p>
<h3 id="explanation">6.3 Explanation</h3>
<p>Explanation tasks are often misdiagnosed as failures of clarity when the deeper failure is wrong target-type selection. The requested object depends on audience, allowed simplification, notation, proof status, and permitted use.</p>
<p class="table-display-caption" id="table-7-caption">Table 7. Candidate target type, Validation criterion</p>
<div aria-labelledby="table-7-caption" class="table-scroll" data-columns="2" role="group" tabindex="0"><table data-source-table="7" id="table-7"><caption class="visually-hidden">Table 7. Candidate target type, Validation criterion</caption>
<colgroup>
<col style="width: 32%"/>
<col style="width: 67%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Candidate target type</strong></th>
<th scope="col"><strong>Validation criterion</strong></th>
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
</table></div>
<h3 id="scientific-protocol-design">6.4 Scientific protocol design</h3>
<p>Scientific protocol design exposes the relation between target type and permitted claim. A surface-level answer can be fluent and still fail as a protocol if it omits controls, uncertainty, stopping criteria, or the evidential claim the protocol can support.</p>
<p>Prompt: design an experiment to test whether molecule X is stable under condition Y.<br/>
A = ExperimentalProtocol(hypothesis, materials, controls, measurement, uncertainty, QC, stopping_conditions, analysis_plan, permitted_claim)</p>
<p class="table-display-caption" id="table-8-caption">Table 8. Failure, Meaning — Failure, Meaning</p>
<div aria-labelledby="table-8-caption" class="table-scroll" data-columns="2" role="group" tabindex="0"><table data-source-table="8" id="table-8"><caption class="visually-hidden">Table 8. Failure, Meaning — Failure, Meaning</caption>
<colgroup>
<col style="width: 27%"/>
<col style="width: 72%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Failure</strong></th>
<th scope="col"><strong>Meaning</strong></th>
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
</table></div>
<h3 id="planning-and-tool-use">6.5 Planning and tool use</h3>
<p>Planning and tool-use tasks treat generated objects as candidate state transformations. A plan is not merely a list of steps. It is a proposed transition from current state to goal state under time, resource, authority, and recovery constraints.</p>
<p>Prompt: plan how to prepare, run, and analyze a small experiment by tomorrow afternoon.<br/>
A = Plan : CurrentState -&gt; GoalState<br/>
constraints = time, resources, dependencies, authority, risk, recovery path</p>
<p>Tool calls are candidate inhabitants of action schemas. Once execution changes state, the effect and authority layer developed later in the series adds preconditions, postconditions, handlers, rollback paths, and audit traces.</p>
<h2 id="type-first-prompting-harness-v0.3">7. Type-First Prompting Harness v0.3</h2>
<p>The Type-First Prompting Harness is an evaluation design. It tests whether explicit target-type articulation improves generation. It should be reported as a scientific probe of Typed Generativity, not as a prompting style.</p>
<p class="table-display-caption" id="table-9-caption">Table 9. Condition, Instruction pattern, Purpose</p>
<div aria-labelledby="table-9-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="9" id="table-9"><caption class="visually-hidden">Table 9. Condition, Instruction pattern, Purpose</caption>
<colgroup>
<col style="width: 20%"/>
<col style="width: 43%"/>
<col style="width: 35%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Condition</strong></th>
<th scope="col"><strong>Instruction pattern</strong></th>
<th scope="col"><strong>Purpose</strong></th>
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
</table></div>
<h3 id="dataset-schema">7.1 Dataset schema</h3>
<p>type_first_item:<br/>
task_id: string<br/>
domain: code | lean_math | explanation | scientific_protocol | planning | tool_use<br/>
prompt: string<br/>
intended_target_type: string<br/>
candidate_target_types: list[string]<br/>
constraints: list[string]<br/>
invalid_target_type_examples: list[string]<br/>
valid_inhabitant_criteria: list[string]<br/>
checker_or_validator: string<br/>
human_review_fields: list[string]<br/>
ambiguity_status: explicit | latent | unresolved<br/>
semantic_participation_target: string</p>
<h3 id="metrics">7.2 Metrics</h3>
<p class="table-display-caption" id="table-10-caption">Table 10. Metric, Definition, Interpretation</p>
<div aria-labelledby="table-10-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="10" id="table-10"><caption class="visually-hidden">Table 10. Metric, Definition, Interpretation</caption>
<colgroup>
<col style="width: 20%"/>
<col style="width: 46%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Metric</strong></th>
<th scope="col"><strong>Definition</strong></th>
<th scope="col"><strong>Interpretation</strong></th>
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
</table></div>
<h3 id="initial-pilot">7.3 Initial pilot</h3>
<p>A first curated pilot should contain 150 items distributed evenly across code, Lean or mathematical formalization, explanation, scientific protocol design, planning, and tool use. This size supports expert annotation and still exposes initial diagnostic signal. The first pilot should prioritize label quality over scale.</p>
<p>The primary analysis should classify every failure into at least three classes: wrong target type, right target type with invalid inhabitant, and valid inhabitant with failed semantic participation. A fourth class, transformation instability, should be added when the artifact fails a Functorial Consistency test.</p>
<h2 id="target-type-and-candidate-inhabitant-records">8. Target-type and candidate-inhabitant records</h2>
<p>Typed Generativity requires two lightweight records. The target_type_record records the object inferred before generation. The candidate_inhabitant_record records the generated candidate and its validation path. Together they connect generation to membership and transformation.</p>
<p class="table-display-caption" id="table-11-caption">Table 11. Record, Core question, Primary downstream use</p>
<div aria-labelledby="table-11-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="11" id="table-11"><caption class="visually-hidden">Table 11. Record, Core question, Primary downstream use</caption>
<colgroup>
<col style="width: 28%"/>
<col style="width: 35%"/>
<col style="width: 35%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Record</strong></th>
<th scope="col"><strong>Core question</strong></th>
<th scope="col"><strong>Primary downstream use</strong></th>
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
</table></div>
<p>target_type_record:<br/>
task_id: string<br/>
context_summary: string<br/>
candidate_target_types: list[string]<br/>
selected_target_type: string<br/>
selection_rationale: string<br/>
constraints: list[string]<br/>
invalid_target_examples: list[string]<br/>
validator_or_review_method: string<br/>
ambiguity_status: explicit | latent | unresolved<br/>
downstream_environment: string<br/>
<br/>
candidate_inhabitant_record:<br/>
task_id: string<br/>
selected_target_type: string<br/>
candidate: string | object<br/>
validation_status: unchecked | checked | failed | partial | reviewed<br/>
validator: string<br/>
alignment_status: aligned | uncertain | misaligned<br/>
repair_trace: string | null<br/>
epistemic_type: string<br/>
permitted_use: list[string]<br/>
transformation_tests: list[string]</p>
<h2 id="relation-to-the-state-of-the-art">9. Relation to the state of the art</h2>
<p>Typed Generativity draws on established areas, each with a bounded source function. Curry-Howard supplies the proof-as-inhabitant analogy. Type-directed and example-directed synthesis show how explicit types, examples, and refinements constrain program construction. Lean and LeanDojo provide environments in which generated proof artifacts can be checked and proof states can be extracted or manipulated programmatically. Structured-output and schema-constrained systems supply operational typed decoding for model interfaces. Tool-use systems show that generated text can encode calls whose validity depends on interface schemas and arguments.</p>
<p class="table-display-caption" id="table-12-caption">Table 12. Source area, What it supports, Boundary</p>
<div aria-labelledby="table-12-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="12" id="table-12"><caption class="visually-hidden">Table 12. Source area, What it supports, Boundary</caption>
<colgroup>
<col style="width: 25%"/>
<col style="width: 39%"/>
<col style="width: 35%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Source area</strong></th>
<th scope="col"><strong>What it supports</strong></th>
<th scope="col"><strong>Boundary</strong></th>
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
</table></div>
<p>The source boundary is strict. These literatures motivate the generation layer. They do not validate the original Type-First Prompting Harness, target_type_record, candidate_inhabitant_record, or Typed Generativity Bench.</p>
<h2 id="strongest-objections">10. Strongest objections</h2>
<p class="table-display-caption" id="table-13-caption">Table 13. Objection, Response standard, Operational test</p>
<div aria-labelledby="table-13-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="13" id="table-13"><caption class="visually-hidden">Table 13. Objection, Response standard, Operational test</caption>
<colgroup>
<col style="width: 24%"/>
<col style="width: 42%"/>
<col style="width: 32%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Objection</strong></th>
<th scope="col"><strong>Response standard</strong></th>
<th scope="col"><strong>Operational test</strong></th>
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
</table></div>
<h2 id="failure-taxonomy-and-kill-criteria">11. Failure taxonomy and kill criteria</h2>
<p class="table-display-caption" id="table-14-caption">Table 14. Failure, Meaning, Repair path</p>
<div aria-labelledby="table-14-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="14" id="table-14"><caption class="visually-hidden">Table 14. Failure, Meaning, Repair path</caption>
<colgroup>
<col style="width: 22%"/>
<col style="width: 41%"/>
<col style="width: 36%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Failure</strong></th>
<th scope="col"><strong>Meaning</strong></th>
<th scope="col"><strong>Repair path</strong></th>
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
</table></div>
<p>The proposal should be revised under the following conditions.</p>
<ul>
<li><p>K1. Type-first interventions do not improve validity, alignment, repair cost, ambiguity handling, downstream usability, or transformation stability.</p></li>
<li><p>K2. Target-type labels fail to predict errors beyond ordinary task labels or genre labels.</p></li>
<li><p>K3. Human annotators cannot agree on target types after task-specific guidelines.</p></li>
<li><p>K4. Structured-output constraints dominate all gains, leaving no additional value for target-type inference.</p></li>
<li><p>K5. The harness adds annotation cost without diagnostic signal.</p></li>
<li><p>K6. Latent-cognition probes fail to distinguish target-object structure from surface format or topic.</p></li>
<li><p>K7. The framework cannot connect generated candidates to Semantic Participation or Functorial Consistency.</p></li>
</ul>
<h2 id="conclusion-and-transition-to-functorial-consistency">12. Conclusion and transition to Functorial Consistency</h2>
<p>Typed Generativity supplies the generation layer of Compositional Intelligence. It reframes generation as construction of candidate inhabitants of inferred target types, with separate failure modes for target-type inference, candidate construction, validation, repair, Semantic Participation, and transformation stability.</p>
<p>The next essay asks whether those generated objects preserve structure. Once a model constructs a candidate proof, program, semantic parse, protocol, or plan, the central test is path agreement across source and target representations under an explicit equivalence regime. Typed Generativity supplies the candidate object. Functorial Consistency supplies the evaluation square.</p>
<p>Typed Generativity: P_theta(t : A | Gamma)<br/>
Functorial Consistency: T(f(x)) approx g(T(x))</p>
<h2 id="appendix-a.-claim-levels">Appendix A. Claim levels</h2>
<p class="table-display-caption" id="table-15-caption">Table 15. Level, Meaning, Example</p>
<div aria-labelledby="table-15-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="15" id="table-15"><caption class="visually-hidden">Table 15. Level, Meaning, Example</caption>
<colgroup>
<col style="width: 9%"/>
<col style="width: 33%"/>
<col style="width: 56%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Level</strong></th>
<th scope="col"><strong>Meaning</strong></th>
<th scope="col"><strong>Example</strong></th>
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
</table></div>
<h2 id="appendix-b.-benchmark-item-schema">Appendix B. Benchmark item schema</h2>
<p>typed_generativity_benchmark_item:<br/>
id: string<br/>
domain: string<br/>
prompt: string<br/>
intended_target_type: string<br/>
candidate_target_types: list[string]<br/>
constraints: list[string]<br/>
invalid_target_examples: list[string]<br/>
valid_inhabitant_criteria: list[string]<br/>
validator: string<br/>
semantic_participation_target: string<br/>
transformation_tests: list[string]<br/>
reviewer_guidelines: string<br/>
failure_labels: list[string]</p>
<h2 id="appendix-c.-source-use-warnings">Appendix C. Source-use warnings</h2>
<ul>
<li><p>Curry-Howard supports the proof-as-inhabitant analogy in formal systems; it does not establish that language models implement type theory.</p></li>
<li><p>Type-directed and example-directed synthesis support explicit specification-guided construction; Typed Generativity adds latent target-type inference under natural-language context.</p></li>
<li><p>Lean and LeanDojo support formal validation and proof-state interaction; they do not establish semantic alignment or downstream reuse on their own.</p></li>
<li><p>Structured-output systems support typed decoding and schema conformance; schema conformance should be distinguished from artifact membership.</p></li>
<li><p>Tool-use systems support interface-constrained generation; executed actions require the effect and authority controls developed later in the series.</p></li>
<li><p>AlphaProof and related mathematical-reasoning systems motivate high-value typed construction; contest results should be cited only for their documented scope.</p></li>
</ul>
