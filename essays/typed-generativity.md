# Typed Generativity

*Mateo Petel*

<!-- AUTHORITATIVE-DOCX SHA256 174be720ce13dfaf0196ad51a5f35c02810fc8bd0a00356399f0ab4baf67e028; source Essay2_Typed_Generativity_V3(1).docx -->
<!-- Publication editorial revision V5 of the DOCX-derived manuscript. The DOCX SHA-256 above identifies only the historical V3 source, not this edited text. Original manuscript tables are preserved; editorial additions are identified in the accompanying audit. -->

<h2 id="abstract">Abstract</h2>
<p>Typed Generativity examines how an AI system selects a specification for an intended artifact, constructs a candidate, and submits that candidate to validation and downstream assessment. The central proposal is an external analysis of target-directed generation, with formal types in proof-oriented settings and explicit operational specifications in broader artifact tasks. The distinction matters for the Compositional Intelligence series. Semantic Participation assesses an artifact's standing in a structured environment; the present essay examines the construction and validation stages that precede such participation.</p>
<p>The expression P_theta(t : A | Gamma) is retained as the essay's mnemonic for target-directed generation. Its probabilistic interpretation depends on an explicit space of target specifications and candidate artifacts. In an instrumented two-stage generator, target selection and candidate construction admit a joint probability law. Validation remains a separate operation. For a formal proof artifact, an inhabitation judgment is justified by the relevant checker; for a protocol, plan, or explanation, acceptance depends on stated operational criteria. This distinction permits a common evaluative analysis without identifying these broader artifact specifications with formal types.</p>
<p>The essay separates three levels of typed generation. Typed output concerns artifacts checked after generation. Typed decoding concerns generation constrained by a schema, grammar, type, tool interface, or parser. Typed latent cognition names the stronger hypothesis that a system internally represents requested object structure in type-like ways before or during generation. The first two levels support immediate evaluation. The third requires targeted evidence from interventions, probes, ambiguity datasets, and failure clustering.</p>
<p>The proposed Type-First Prompting Harness v0.3 examines the effect of explicit target-specification articulation across six domains. Its primary comparison is the assigned type-first intervention against neutral deliberation under matching predeclared limits. A common endpoint means compliance with a domain-specific frozen acceptance contract, not interchangeable evidence across domains. The study separates assigned-trial outcomes from evaluator unavailability, target-selection diagnostics from construction failures, and external intervention effects from claims about internal representations. The companion contract is an unexecuted prototype. Functorial Consistency extends the analysis to structured transformations.</p>
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
<p>Table 1 preserves the source manuscript's proposed contributions. Its failure-taxonomy claims are analytical classifications, not observed prevalence estimates. Any assertion that one diagnosis explains more errors than another belongs to a future empirical comparison.</p>
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
<p>This position determines the essay’s scope. Proofs, programs, protocols, plans, tool calls, and explanations have different acceptance and use conditions. Their evaluation depends on the relevant assumptions, validators, dependencies, and intended environment. A failure apparently attributable to reasoning or retrieval could originate in target selection, constraint extraction, artifact construction, or downstream integration. Distinguishing these explanations is an empirical objective, not an observed prevalence claim.</p>
<p>Typed Generativity links the external standards of Semantic Participation to candidate-generation diagnostics. Incorrect target selection, omitted constraints, invalid construction, unstable specification maintenance, and local validity without permitted downstream use identify different failure sites. A recorded target specification permits analysis of the first two sites; output-only evaluations generally cannot recover a unique earlier selection process. Error labels are assigned only from evidence available for the relevant stage.</p>
<h2 id="thesis-and-scope-control">2. Thesis and scope control</h2>
<p>The thesis is that many high-value AI generations are usefully analyzed through target-specification inference followed by candidate construction. The system receives context, selects or proposes an object class, constructs a candidate for that class, and submits the result to validation, review, repair, and semantic-membership assessment. The notation t : A records an intended typing relation at the generation stage. Verified inhabitation is established separately by a checker or an appropriately specified evaluation procedure.</p>
<p>Gamma -&gt; infer A -&gt; construct t : A -&gt; validate/repair -&gt; semantic participation</p>
<p>The claim has distinct meanings across domains. In a proof assistant, a declared target type and a derivation accepted by the kernel support a formal inhabitation claim. A well-typed program likewise satisfies the language's typing rules, although behavioral correctness remains a separate obligation. In structured outputs and tool use, supplied schemas constrain particular aspects of the artifact or action. Explanation, planning, scientific protocol design, and structured writing rely on task specifications assembled from context, with criteria that are partly interpretive. The essay's use of type in these latter settings describes an evaluation abstraction, not a theorem of type theory.</p>
<p>Typed Generativity is an operational abstraction over the object layer of generation. A code string is judged as a program. A proof script is elaborated as a formal object. A JSON response is consumed through a schema. A scientific protocol encodes controls, measurements, uncertainty, stopping criteria, analysis plans, and permitted claims. A plan encodes a state transformation under constraints. The abstraction is useful to the extent that it improves diagnosis, validation, repair, and downstream artifact use.</p>
<h2 id="central-schema">3. Central schema</h2>
<p>The source manuscript summarizes construction through the following schematic expression.</p>
<p>P_theta(t : A | Gamma)</p>
<p>For an external model, let γ denote the observed task context, a a target specification drawn from a measurable set 𝒜, and t an artifact drawn from a measurable set 𝒯. The specification fixes an object kind, constraints, and a validation regime for environment e. If a staged procedure explicitly records a before candidate construction, q<sub>θ</sub>(a | γ) denotes its target-selection kernel and r<sub>θ</sub>(t | a, γ) its artifact-construction kernel. Their composition defines the joint law below. In a system without that staged interface, the factorization exists abstractly for a joint law, yet the separate factors have no empirically identified interpretation as successive internal computations.</p>
<p class="schema-equation"><code>p_θ(a, t | γ) = q_θ(a | γ) · r_θ(t | a, γ).</code></p>
<p>For an explicitly staged procedure, the factorization follows from its construction; it is not a theory of internal cognition. A staged generator supplies observable target-selection and construction records by design. For an uninstrumented model, alternative unobserved target variables might explain the same final-artifact distribution, leaving internal processing unidentified. The symbols denote probability masses or densities under the stated sampling model; a deterministic procedure is a degenerate case. Scores and rankings receive probabilistic meaning only through a declared sampling policy. Testable content arises from independently specified targets, recorded decisions, and comparisons that distinguish specification information from task genre, format, and additional deliberation.</p>
<p>Generation and verification are distinct. A formal typing assertion Δ ⊢ t : A is warranted only under the declared calculus, environment, and trusted checking procedure. Proposed(γ, a, t) records a candidate and its selected specification without making that assertion. For broader specifications, V(a, t, e) returns accepted, rejected, or indeterminate under a declared review or validation procedure. Acceptance is relative to its frozen criteria and evidence regime. Scientific-protocol acceptance establishes a prospective document-level judgment, not observed experimental success. Formal proof checking establishes a judgment relative to the checker and admitted axioms, not independent fidelity to a natural-language theorem. Semantic Participation additionally assesses alignment, dependencies, authority, warrant, and permitted use. Invalid artifacts, unexecuted validators, validator errors, and missing reviewer judgments occupy distinct failure states.</p>
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
<p>Table 3 retains the source's mnemonic descriptions, including its broader use of P_theta for rankings and search. The probabilistic interpretation is narrower: scores and rankings yield distributions only under a specified stochastic selection rule. Operational evaluation distinguishes the chosen target, the produced candidate, the result of validation, and the artifact's participation in its intended environment. Failure labels describe these separate observations without presupposing the model's internal reasoning process.</p>
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
<p>An underspecified prompt need not determine a unique target. For each task, independent annotators designate an admissible set of target interpretations, with an explicit unresolved-intent status if context lacks enough information even for that judgment. Agreement with one private reference label is an unsuitable success criterion in such cases. The evaluator distinguishes target selection, clarification, justified abstention, and the admissible object set. Clarification is an eligible action only in a separately defined interactive protocol with its own time, turn, and tool budgets. In one-shot evaluation, unresolved intent remains an explicitly reported limitation of the item.</p>
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
<p>These levels are distinct claims, not consecutive stages or a hierarchy of increasingly strong typing guarantees. Output validation and constrained decoding can operate together without revealing the system's internal representations. Internal type-like structure, if present, does not itself establish that generated artifacts satisfy their specifications. The first two levels admit external intervention and validation tests. The third is a hypothesis about representation and causal use: probes or failure clusters supply correlational evidence, whereas controlled interventions and specificity controls are needed to determine whether a putative target representation contributes to generation, repair, or transformation behavior.</p>
<h2 id="domain-examples">6. Domain examples</h2>
<h3 id="code-generation">6.1 Code generation</h3>
<p>Code generation separates ordinary typing from behavioral correctness. Deduplication depends on a defined equality relation. For arbitrary opaque element types, the bare polymorphic signature List α → List α supplies no equality operation and does not specify stable duplicate removal. In a language supporting constrained polymorphism, the example needs an equality assumption; a specification of first-occurrence preservation then constitutes a distinct behavioral obligation.</p>
<p>Prompt: write a function that removes duplicates from a list and preserves the first occurrence order.<br/>
A = for every α equipped with decidable equality, List α -&gt; List α<br/>
constraints = for each input list, return exactly the first representative of each equality class in its original order; pure function<br/>
t = candidate implementation</p>
<p>Passing the function's ordinary type checker establishes its input-output type under the equality assumption. A proof of the behavioral postcondition, or a test-based estimate of compliance with it, supplies additional evidence. Those forms of evidence carry different guarantees. The source's failure categories in Table 6 remain applicable under this corrected specification.</p>
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
<p>The formalization must specify a nonempty interval, for example the closed real interval [a, b] with a ≤ b. A maximum-attainment claim quantifies a witness x in that interval and establishes an inequality for every other point in the interval. Existence of a supremum, or a statement over an empty domain, misses that target. Lean elaboration establishes well-formed declarations in a specific environment. Kernel checking verifies a proof term relative to the resulting statement, definitions, and axioms. A benchmark success decision also needs a dependency and axiom audit that excludes <code>sorry</code>, unauthorized declarations, and unapproved trusted computation; a successful compilation alone does not satisfy this criterion. For instance, Lean's <code>#print axioms</code> reports dependencies for review. A separate expert or semantic reference checks agreement with the intended mathematical proposition. Each result identifies its Lean revision and library snapshot.</p>
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
<p>Scientific protocol design distinguishes document completeness, technical feasibility, and eventual evidential adequacy. A molecular-stability protocol needs an operationalized observable, defined conditions, interval, sampling and uncertainty plan, applicable controls, quality procedures, and a bounded conclusion. Expert review of a proposed protocol establishes at most a judged level of prospective adequacy. It cannot establish that an unexecuted experiment produces reliable measurements or supports a particular scientific conclusion. The evaluation records these evidential levels separately.</p>
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
<p>Planning tasks describe proposed transitions between states under resource, temporal, and authority constraints. A plan is generally a contingent action sequence or policy, not a total function from every current state to a goal state. Its correctness depends on preconditions, environmental assumptions, possible disturbances, and the specified notion of successful completion.</p>
<p>Prompt: plan how to prepare, run, and analyze a small experiment by tomorrow afternoon.<br/>
A = StateTransitionPlan(initial_state, goal_condition, actions, preconditions, resources, contingencies)<br/>
constraints = time, resources, dependencies, authority, risk, recovery path</p>
<p>Tool calls must satisfy interface constraints and independent authorization conditions. A syntactically valid call or executable plan does not establish permission to act. Actual execution introduces side effects, observability limits, postconditions, failure handlers, and audit evidence, connecting the present analysis to the later effect-and-authority framework.</p>
<h2 id="type-first-prompting-harness-v0.3">7. Type-First Prompting Harness v0.3</h2>
<p>The Type-First Prompting Harness is an evaluation proposal, not a completed benchmark. Its principal intervention explicitly requests a target specification before artifact construction. The comparative question is whether that instruction improves externally assessed outcomes beyond a neutral deliberation step under the same task information and resource limits. Source targets, reviewer rubrics, model instructions, and acceptance tests must be fixed independently to prevent the treatment from introducing otherwise unavailable task information.</p>
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
<p>Each outcome needs an item-specific rubric, a declared evidence source, and a defined analysis unit. The primary endpoint is successful artifact acceptance under the item's precommitted task contract, including admissible target interpretation and mandatory validation and alignment checks. This endpoint is deliberately stronger than parse success yet narrower than evidence of real-world scientific effectiveness. Component outcomes remain separate, avoiding an opaque aggregate score. Items with indeterminate intent or ineligible downstream tests are identified before randomization; checker nonexecution and operational failures retain distinct status codes. Human reviewers assess normalized artifacts without access to assignment or model-generated preparatory notes.</p>
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
<p>The proposed feasibility pilot contains 150 curated items, 25 per domain. Each item is assigned to direct generation, neutral deliberation, and type-first generation under a common model revision and declared resource limits. Equal caps constrain the available budget; actual token use, latency, and cost are measured independently. Repeated samples within an item estimate generation variability; they do not enlarge the number of independent items. The pilot tests rubric feasibility, annotation concordance, validator reliability, tool-state capture, missing-data handling, task provenance, and resource cost. Its outcomes are exploratory. Confirmatory items must be held out from the iterative rubric and prompt revisions induced by the pilot.</p>
<p>Failure diagnosis is multi-stage and partly multi-label. Ambiguity is a property of the request; target mismatch describes a selection; constraint omission, invalid construction, and blocked downstream participation describe different later stages. Transformation instability applies only to candidates with a declared transformation test. Multiple failures can coexist. Any single-primary-cause taxonomy needs a separate adjudication policy and an explicit rule for missing or indeterminate evidence.</p>
<h3 id="identification-and-analysis-protocol">7.4 Identification and analysis protocol</h3>
<p><strong>Experimental contrast.</strong> The principal comparison randomizes the assignment of either type-first articulation (T) or neutral deliberation (L). Each condition receives the same task information, model revision, allowed retrieval, tool permissions, preparation opportunity, final-artifact slot, and predeclared resource limits. T directs the preparatory phase toward target-kind identification, constraints, ambiguity, and validation. L permits deliberation without prescribing these components. Spontaneous specification reasoning under L is part of the comparator. The contrast evaluates the two complete instruction packages. Direct generation, oracle specifications, constrained decoding, and checker-assisted repair supply separate exploratory comparisons, since they change information or mechanisms.</p>
<p><strong>Independent acceptance.</strong> Before confirmatory generation, domain experts establish admissible target interpretations, mandatory acceptance criteria, evidence grades, and rules for unresolved judgments. Reviewers assess extracted final artifacts under a treatment-independent protocol. The primary endpoint is satisfaction of the item's declared acceptance contract, including target alignment. Proof checking, test-suite success, prospective protocol review, simulated planning, and authorized tool execution remain distinct forms of evidence. Completed refusals and model-side failures count as unsuccessful under the prespecified one-shot convention; infrastructure failures and inconclusive mandatory assessments produce missing or indeterminate outcomes. Every preassigned trial stays in the analysis ledger.</p>
<p><strong>Estimand.</strong> For task i in a fixed domain-specific corpus I<sub>d</sub>, let μ<sub>i,c</sub> denote expected acceptance under assigned condition c over the declared generation and assessment process. The fixed-corpus treatment contrast is</p>
<p class="schema-equation"><code>Δ<sub>d</sub><sup>fixed</sup> = (1 / |I<sub>d</sub>|) Σ<sub>i∈I_d</sub> (μ<sub>i,T</sub> − μ<sub>i,L</sub>).</code></p>
<p>Estimate the contrast through preallocated repetitions under each condition, averaging trial outcomes within tasks before averaging task-level differences. Repetitions characterize variation for these tasks, not the size or representativeness of the task population. A separate population-level claim needs justified task sampling and allowance for shared source families. Unknown outcomes receive explicit pessimistic and optimistic bounds, not automatic removal. Such bounds differ from statistical confidence intervals.</p>
<p><strong>Reproducibility and interpretation.</strong> Preallocate and randomize trials, isolate generation sessions and mutable tool state, pin model and validator versions, and retain termination, extraction, resource-consumption, and evidence records. Human reviewers initially score independently, with disagreements and adjudications retained. Record task provenance and retrieval-time exposure to hidden answers, including search results containing reference responses. Report outcomes for each domain, resource cost, judgment disagreement, and assignment disposition. An optional equal-weight cross-domain macro-average is a declared reporting convention, not an estimate of a universal task distribution. Any observed contrast measures the effect of assigning the complete T package under the tested conditions. It establishes neither an isolated benefit for a specific target-specification field nor a causal representation mechanism inside the model. The full proposed protocol is retained separately, together with the domain acceptance handbook and record contract.</p>
<h3 id="discriminating-predictions-and-decision-rules">7.5 Discriminating predictions and decision rules</h3>
<p>The framework has three separable claims. The <em>procedural</em> claim predicts incremental task-level acceptance under the type-first treatment relative to neutral deliberation. The <em>diagnostic</em> claim predicts additional held-out predictive or triage value from independently defined target-specification labels. Prospective prediction must use only information available at the stated prediction time; retrospective diagnosis can use observed checker outcomes, provided the proposed label does not restate the outcome it seeks to predict. The <em>representational</em> claim predicts a causal role for target-like internal variables; output-level prompting trials alone do not test it. Each claim retains its own evidence threshold.</p>
<p>The procedural claim is evaluated against a practically important effect threshold and a prespecified resource-cost tradeoff. A small positive difference at substantially greater cost does not establish practical value. The diagnostic claim uses task-family-disjoint holdouts, separately timed prediction tasks, and an appropriate prespecified proper scoring rule for probabilistic forecasts. Criterion-derived labels are prohibited as predictors of their own criterion outcome. Retrospective triage is evaluated separately through adjudicated fault localization and repair utility, without transferring its benefit to a claim of prospective prediction. For the representational claim, probes receive topic, lexical, and formatting controls alongside intervention-based validation.</p>
<p>Follow-up ablations isolate the contribution of object-kind labeling, explicit constraint extraction, validator selection, and extra deliberation. Their design and analysis plan are fixed before confirmatory evaluation, or their findings remain exploratory. Disagreement on admissible target interpretations, unavailable validators, and target descriptions tailored to model outputs count as threats to measurement validity, not evidence of model failure. Strong null findings narrow the scope of an intervention or label scheme; they do not retroactively establish the absence of internal object representations across systems.</p>
<h3 id="domain-specific-acceptance-and-evidence">7.6 Domain-specific acceptance and evidence</h3>
<p>The shared endpoint denotes satisfaction of an independently frozen, domain-specific task contract. Its comparability across domains concerns the intervention's effect on meeting each contract, not the evidential strength of the contracts themselves. A generated code patch might pass tests and still violate an untested behavioral requirement. A Lean proof might be kernel-checked relative to an unapproved axiom, or prove a proposition unlike the source claim. An explanation might satisfy audience constraints while remaining factually unsupported. A scientific protocol might be judged prospective and complete without having been executed. A plan might satisfy simulator constraints without surviving real disturbances. A tool call might match a schema and still lack permission to change state. Appendix F and the companion domain handbook specify the required distinctions and evidence limits.</p>
<p>Admissible target interpretations must be recorded independently of the tested outputs. A task with several reasonable final-artifact types admits a declared set or an interactive clarification pathway; the benchmark cannot silently score a reasonable alternative as mistaken. If the acceptable interpretations cannot be adjudicated in advance, the task enters the ambiguity cohort or is excluded from confirmatory artifact acceptance by a recorded pre-assignment decision. Mandatory criteria must encode target alignment, with additional requirements appropriate to the domain. Missing criteria never become satisfied merely through JSON validity or checker completion.</p>
<h3 id="trial-disposition-and-missing-evidence">7.7 Assigned-trial dispositions and incomplete evidence</h3>
<p>Every planned trial has a preassigned task, condition, and attempt index. Trial disposition is distinct from completion, artifact extraction, criterion assessment, and final acceptance. For the one-shot artifact endpoint, a completed refusal or explicit model-generation failure counts as unsuccessful under a previously fixed rule. An evaluator outage or execution-infrastructure failure produces an unknown potential artifact outcome and is reported as missing, even if a conservative secondary analysis scores it zero. A completed artifact with a rejected mandatory criterion is unsuccessful. All mandatory criteria accepted establishes success; an undecided mandatory criterion otherwise leaves acceptance unresolved.</p>
<p>Report assigned-trial counts, observed-success counts, observed-failure counts, indeterminate counts, and infrastructure-loss counts for every condition. Provide pessimistic and optimistic acceptance bounds, and bounds on the T-minus-L contrast, before complete-case estimates. Repeated trials are nested under tasks and task families. The diagnostic question is whether artifact and target records explain failure patterns independently of the label-generation procedure, not whether a target description restates a failed checker verdict.</p>
<h2 id="target-type-and-candidate-inhabitant-records">8. Target-type and candidate-inhabitant records</h2>
<p>Typed Generativity introduces target_type_record and candidate_inhabitant_record as proposed external reporting objects. The first records a declared specification; it does not expose the system's latent state. The second records the candidate and its validation route. Study records additionally distinguish planned assignments, execution traces, extraction decisions, criterion results, and adjudicated acceptance. The original schemas below remain as historical proposals. Appendix D describes the supplementary machine-readable contract; Appendix E specifies outcome derivation and Appendix F gives domain-specific evidence boundaries. The contract's checkable invariants are a narrow part of the full research protocol.</p>
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
<p>The Curry–Howard correspondence supports the exact interpretation of proof terms as inhabitants within a stated logical calculus. Type-and-example-directed synthesis (Osera and Zdancewic, 2015) and synthesis from polymorphic refinement types (Polikarpova et al., 2016) provide established precedents for specification-driven construction. PICARD (Scholak et al., 2021) and Synchromesh (Poesia et al., 2022) demonstrate constrained generation through different parser and semantic-decoding mechanisms. LeanDojo (Yang et al., 2023) provides infrastructure for retrieval-augmented interaction with Lean. Park et al. (2025) study efficient grammar-constrained decoding, while Mündler et al. (2026) extend grammar constraints to diffusion-model generation. The AlphaProof study, first published online in 2025 and appearing in the 2026 version of record, reports specialist formal mathematical proof search. These works establish relevant technical precedents, not empirical confirmation of the present target-inference model or the latent-representation hypothesis. <strong>The prospective contribution is a cross-domain diagnostic and experimental evaluation design. Its incremental validity, predictive value, and practical usefulness remain untested.</strong></p>
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
<p>The research boundary remains strict. The cited systems establish results within formal synthesis, constrained generation, proof interaction, or specialized mathematical search. They do not verify the target-inference schema, this benchmark, or a latent representation hypothesis. Evaluation methodology is informed by Miller's statistical treatment of model comparisons and NIST AI 800-3's distinction between the evaluand, data-generating process, and statistical model. Those sources guide uncertainty reporting; they do not establish empirical benefits for type-first prompting.</p>
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
<p>These are hypotheses for a planned study, not observed outcomes. Before a confirmatory run, specify the practical effect threshold, cost tradeoff, target-annotation reliability criteria, and predictive baseline. Inconclusive confidence intervals do not license either a positive finding or a universal null conclusion. A weak output-level intervention does not falsify the internal representation hypothesis, whereas unstable annotation or no predictive increment limits the usefulness of the proposed operational target categories.</p>
<h2 id="conclusion-and-transition-to-functorial-consistency">12. Conclusion and transition to Functorial Consistency</h2>
<p>Typed Generativity proposes a framework for target-directed construction and the evaluation of artifacts under explicit specifications. Its central distinction is between an externally observed target declaration, a generated candidate, a validator judgment, and the candidate's permitted use in a structured environment. The probabilistic decomposition alone identifies no internal mechanism. Its explanatory value rests on separating failure sites; any claim of improved generation awaits discriminating experiments, independent artifact assessments, and reproducible records.</p>
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

<h2 id="appendix-d.-operational-evaluation-contract">Appendix D. Operational evaluation contract</h2>
<p>The accompanying JSON Schema, <code>typed_generativity_benchmark_contract_v0.2.schema.json</code>, specifies a proposed minimum machine-readable record. It defines benchmark tasks, assigned generation runs, and independent judgments. The schema validates structure; substantive correctness depends on independently authored rubrics and trusted execution of domain-specific checks. Cross-record references and restrictions on leakage or treatment assignment need an additional consistency audit.</p>
<p><strong>Task record.</strong> Each item has a stable task identifier and a task-family identifier for clustered sampling. It records a domain, exact prompt, development or confirmatory split, admissible target identifiers, ambiguity policy, mandatory acceptance criteria, provenance, and a declaration of which criteria have runnable checkers. The benchmark author freezes the item contract before any confirmatory artifact is generated.</p>
<p><strong>Run record.</strong> Each run records its assigned condition, declared model revision, randomization index, trial identifier, generation settings, resource limits, observed token and tool usage, produced artifact, declared target specification if elicited, execution termination status, and relevant environment fingerprints. Target declarations are preparatory artifacts and must remain separate from reviewer-facing final artifacts.</p>
<p><strong>Judgment record.</strong> Each criterion has an assessor identifier, assessment source, accepted/rejected/indeterminate result, evidence reference, and evaluation status. Checker execution status is recorded separately. The final task-level acceptance rule refers only to criteria frozen in the task contract. Each human disagreement is preserved alongside its adjudicated decision; the primary analysis never silently converts missing assessments to passing labels.</p>
<p><strong>Validation boundary.</strong> Structural schema validation does not detect contaminated examples, false scientific conclusions, unauthorized tool execution, or inadequate reference specifications. An illustrative fixture and consistency checker demonstrate record-level constraints without constituting any model result. The confirmatory analysis additionally needs a frozen statistical analysis plan and artifact-level adjudication logs. No experimental results are supplied in this appendix.</p>

<h2 id="appendix-e.-primary-outcome-derivation">Appendix E. Primary outcome derivation and bounds</h2>
<p>For each preassigned one-shot trial, retain its condition and task even if the model refuses, the generator fails, or the evaluation infrastructure is unavailable. Let the final mandatory-criterion verdicts take values in {accepted, rejected, indeterminate}. Under the frozen decision rule, a valid final artifact succeeds exactly when every mandatory criterion is accepted; any mandatory rejection establishes failure; absent or indeterminate mandatory evidence leaves outcome unknown. A refusal or declared model-generation error is unsuccessful for this artifact-production endpoint. Infrastructure loss is unknown rather than a model error. In interactive tasks, clarification quality belongs to a separately defined endpoint.</p>
<p>Encode each trial as an interval [l, u]. Success gives [1, 1], failure gives [0, 0], and unknown gives [0, 1]. For task i and condition c, let L<sub>ic</sub> and U<sub>ic</sub> be the means of the lower and upper trial endpoints over preallocated trials. The fixed-corpus treatment effect must then lie within</p>
<p class="schema-equation"><code>Δ<sub>lower</sub> = mean<sub>i</sub> (L<sub>iT</sub> − U<sub>iL</sub>),   Δ<sub>upper</sub> = mean<sub>i</sub> (U<sub>iT</sub> − L<sub>iL</sub>).</code></p>
<p>These are deterministic missing-outcome bounds given the recorded assignments, not statistical confidence intervals. An entirely observed corpus collapses the interval to the descriptive paired contrast. Family-based uncertainty intervals, randomization inference, and population generalization require additional, explicitly justified assumptions. Published reports separately identify structural missingness, model-side failure, and criterion-level nonexecution.</p>
<h2 id="appendix-f.-domain-evidence-boundaries">Appendix F. Domain evidence boundaries</h2>
<p>The companion <em>Domain Acceptance Handbook</em> specifies contract profiles for code generation, Lean formalization, explanations, scientific protocols, planning, and tool use. Each profile states the candidate artifact, independent target-admissibility standard, mandatory checks, permitted evidence grade, disqualifying failures, and independent review needs. One label, “accepted,” thus refers to a declared contractual assessment, not a domain-independent truth guarantee. Formal validation, automated testing, expert assessment, simulated execution, and real state changes must be reported under distinct evidence labels. These profiles are proposed adjudication standards, subject to domain-expert review before use in a confirmatory study.</p>
<h2 id="selected-references">Selected references</h2>
<ul>
<li><p>Osera, P.-M., and Zdancewic, S. (2015). <a href="https://pldi15.sigplan.org/details/pldi2015-papers/64/Type-and-Example-Directed-Program-Synthesis">Type-and-Example-Directed Program Synthesis</a>. PLDI, 619–630.</p></li>
<li><p>Polikarpova, N., Kuraj, I., and Solar-Lezama, A. (2016). <a href="https://dspace.mit.edu/entities/publication/c3dcde41-ff5d-442d-b1c1-4f269c8896ef">Program Synthesis from Polymorphic Refinement Types</a>. PLDI, 522–538.</p></li>
<li><p>Scholak, T., Schucher, N., and Bahdanau, D. (2021). <a href="https://aclanthology.org/2021.emnlp-main.779/">PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models</a>. EMNLP, 9895–9901.</p></li>
<li><p>Poesia, G., Polozov, A., Le, V., Tiwari, A., Soares, G., Meek, C., and Gulwani, S. (2022). <a href="https://www.microsoft.com/en-us/research/publication/synchromesh-reliable-code-generation-from-pre-trained-language-models/">Synchromesh: Reliable Code Generation from Pre-Trained Language Models</a>. ICLR.</p></li>
<li><p>Yang, K., et al. (2023). <a href="https://proceedings.neurips.cc/paper_files/paper/2023/hash/4441469427094f8873d0fecb0c4e1cee-Abstract-Datasets_and_Benchmarks.html">LeanDojo: Theorem Proving with Retrieval-Augmented Language Models</a>. Advances in Neural Information Processing Systems 36.</p></li>
<li><p>Park, K., Zhou, T., and D’Antoni, L. (2025). <a href="https://proceedings.mlr.press/v267/park25l.html">Flexible and Efficient Grammar-Constrained Decoding</a>. ICML, Proceedings of Machine Learning Research 267, 48262–48275.</p></li>
<li><p>Mündler, N., Dekoninck, J., and Vechev, M. (2026). <a href="https://proceedings.iclr.cc/paper_files/paper/2026/hash/a1622fc2f8e37ea5fc696d1c13861c36-Abstract-Conference.html">Constrained Decoding of Diffusion LLMs with Context-Free Grammars</a>. ICLR.</p></li>
<li><p>Hubert, T., Mehta, R., Sartran, L., et al. (2026). <a href="https://www.nature.com/articles/s41586-025-09833-y">Olympiad-level formal mathematical reasoning with reinforcement learning</a>. Nature 651, 607–613. First published online 12 November 2025; version of record 13 March 2026.</p></li>
<li><p>Miller, E. (2024). <a href="https://arxiv.org/abs/2411.00640">Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations</a>. arXiv:2411.00640.</p></li>
<li><p>National Institute of Standards and Technology (2026). <a href="https://www.nist.gov/publications/expanding-ai-evaluation-toolbox-statistical-models">Expanding the AI Evaluation Toolbox with Statistical Models</a>. NIST AI 800-3. DOI: 10.6028/NIST.AI.800-3.</p></li>
<li><p>Lean language reference. <a href="https://lean-lang.org/doc/reference/latest/ValidatingProofs/">Validating a Lean Proof</a> and <a href="https://lean-lang.org/doc/reference/latest/Axioms/">Axioms</a>. Version-sensitive reference documentation, consulted 18 November 2026.</p></li>
<li><p>Han, Z., Mankikar, M., Michael, J., and Wang, Z. (2025). <a href="https://arxiv.org/abs/2508.13180">Search-Time Data Contamination</a>. arXiv:2508.13180. Evidence of benchmark-answer exposure during retrieval.</p></li>
</ul>
