# Semantic Participation

*Mateo Petel*

## Abstract

AI reasoning is commonly evaluated through output quality, benchmark performance, and local task completion. Those measures remain useful, although they understate the condition required for cumulative knowledge. A proof sketch, code patch, theorem formalization, protocol, dataset, model result, or scientific claim receives epistemic status only when it can enter a structured environment with explicit validity, alignment, warrant, compositional behavior, and conditions for future use.

This essay introduces semantic participation as the membership layer for AI-generated artifacts. Semantic participation is the capacity of an AI system to place candidate artifacts inside a semantic environment with recorded validation, source-target alignment, compositional role, epistemic type, and permitted use. The framework treats AI outputs as candidate artifacts whose value depends on their position in a world of definitions, dependencies, checkers, provenance, review procedures, admissible operations, and downstream consumption.

Curry-Howard-Lambek supplies the conceptual architecture. Curry-Howard links propositions, types, proofs, and programs. Lambek's original syntactic calculus formalizes composition through ordered grammatical types <span class="citation-group">[<a class="citation-link" href="#ref-Lambek1958" aria-label="Reference 1 — The Mathematics of Sentence Structure">1</a>]</span>. Lean supplies the operational exemplar <span class="citation-group">[<a class="citation-link" href="#ref-LeanRef" aria-label="Reference 2 — The Lean Language Reference">2</a>, <a class="citation-link" href="#ref-TPIL4" aria-label="Reference 3 — Theorem Proving in Lean 4">3</a>]</span>, since generated proof artifacts can be elaborated, checked by a trusted kernel, inspected through proof states, integrated with Mathlib, and reviewed by maintainers. The target class is broader and includes proof assistants, verified programming languages, scientific workflow systems, laboratory automation protocols, research-object infrastructures, and institutional review environments.

The essay contributes six technical objects. It defines semantic environment, ArtifactRecord, semantic membership, semantic transport, epistemic type, and library improvement delta, then turns those objects into record schemas, lifecycle contracts, benchmark protocols, case studies, and falsification criteria. The research program asks how AI systems can participate in cumulative knowledge worlds beyond the production of impressive local answers.

## Contribution summary



<table>
<colgroup>
<col style="width: 6%"/>
<col style="width: 22%"/>
<col style="width: 70%"/>
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
<td>Semantic participation</td>
<td>A proposed membership relation between AI-generated artifacts and structured semantic environments.</td>
</tr>
<tr class="even">
<td>C2</td>
<td>Seven thresholds</td>
<td>A separation among fluency, task success, formal validity, semantic alignment, composability, epistemic warrant, and reuse.</td>
</tr>
<tr class="odd">
<td>C3</td>
<td>Semantic transport</td>
<td>A record-bearing transformation between source and target environments that exposes preservation, loss, generality shifts, and downstream-use conditions.</td>
</tr>
<tr class="even">
<td>C4</td>
<td>Epistemic types</td>
<td>A warrant grammar for artifacts such as theorems, conjectures, simulations, empirical results, causal claims, approximations, and benchmark-conditioned claims.</td>
</tr>
<tr class="odd">
<td>C5</td>
<td>Library improvement delta</td>
<td>A proposed measure of how AI contributions affect future reasoning through reuse, searchability, maintainability, dependency control, and automation compatibility.</td>
</tr>
<tr class="even">
<td>C6</td>
<td>Membership benchmarks</td>
<td>A proposed evaluation program for source-target alignment, semantic transport, epistemic typing, and library integration.</td>
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
<td>Formal-methods researcher</td>
<td>Sections 1, 3, 4, 5, 8, and Appendix A.</td>
</tr>
<tr class="even">
<td>AI evaluation researcher</td>
<td>Sections 2, 4, 7, 8, 10, and Appendix B.</td>
</tr>
<tr class="odd">
<td>AI-for-science reader</td>
<td>Sections 6, 7, 9, 10, and Appendix C.</td>
</tr>
<tr class="even">
<td>Mathematician</td>
<td>Sections 3, 5, 6.1, 8, and Appendix D.</td>
</tr>
<tr class="odd">
<td>Series reader</td>
<td>Read before Essay 2; return to Section 8 before Essay 3.</td>
</tr>
</tbody>
</table>



## 1. Position in the Compositional Intelligence series {#1-position-in-the-compositional-intelligence-series}

Compositional Intelligence studies AI systems as constructors, transformers, validators, warrant-bearing mechanisms, and executors of typed artifacts inside structured worlds. Essay 1 defines the membership criterion for the series. Essay 2 analyzes target-type inference and candidate construction. Essay 3 tests transformation stability through commutation-square evaluation. Essays 4 through 7 extend the framework to language, architecture, quantitative warrant, and action.

> membership -\> generation -\> transformation -\> language -\> architecture -\> warrant -\> action

Semantic Participation is the entry point into the sequence. Later essays ask how artifacts are generated, transformed, architecturally supported, quantitatively warranted, and executed. This essay asks the prior membership question. An AI-generated object counts as an artifact in a serious world of knowledge, software, science, or action only after its target environment, validation status, source alignment, compositional role, epistemic type, and permitted use have been specified.

## 2. Governing claim {#2-governing-claim}



<table>
<colgroup>
<col style="width: 100%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Governing claim</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>An AI output counts as an artifact when it has a recorded position inside a structured semantic environment. It must be expressible there, validated or reviewable there, aligned with its source intention, composable with relevant objects, assigned an epistemic type, and governed by permitted-use conditions.</td>
</tr>
</tbody>
</table>



The claim is membership-centric. A model response can be fluent, useful, and locally successful without satisfying the conditions that support cumulative use. A proof sketch requires definitions, assumptions, proof obligations, and admissible generality. A code patch requires interfaces, tests, dependencies, invariants, security assumptions, and deployment assumptions. A scientific claim requires instruments, models, samples, uncertainty, protocols, evidence, and permitted claim types. A plan requires authority, preconditions, effects, state changes, and validation.

Semantic Participation changes the unit of analysis from the isolated response to the artifact-in-world. The artifact is evaluated together with its representation, dependencies, assumptions, validators, alignment record, epistemic type, and reuse path. Membership is environment-relative. A formal theorem, program, protocol, dataset, or claim can fit one structured setting and fail in another through incompatible definitions, dependencies, review standards, or downstream-use conditions.

## 3. From output quality to semantic membership {#3-from-output-quality-to-semantic-membership}

Output-centric evaluation asks whether a system produces a persuasive answer, passes a benchmark, solves a formal goal, or completes an isolated task. This grammar has advanced AI evaluation through comparable metrics and visible capability demonstrations. It also leaves unresolved the difference between local performance and membership in a structured world.

A membership-centric grammar asks whether a generated artifact can enter an environment that controls expression, validation, alignment, composition, warrant, and reuse. The artifact must be available to the environment in a representation the environment can process; it must satisfy available checkers or review procedures; it must preserve source intention under an explicit relation; it must fit the relevant dependency and interface structure; it must support only claims licensed by its epistemic type.



<table>
<colgroup>
<col style="width: 17%"/>
<col style="width: 28%"/>
<col style="width: 54%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Domain</strong></th>
<th><strong>Local success</strong></th>
<th><strong>Membership condition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Formalization</td>
<td>A proof term or tactic script checks.</td>
<td>The formal target preserves the intended informal claim, uses suitable definitions, and integrates with the library.</td>
</tr>
<tr class="even">
<td>Code</td>
<td>Visible tests pass.</td>
<td>Interfaces, invariants, dependencies, security assumptions, and maintainability conditions are preserved.</td>
</tr>
<tr class="odd">
<td>Science</td>
<td>A protocol or claim sounds plausible.</td>
<td>Controls, uncertainty, measurement context, model assumptions, and permitted claim type are explicit.</td>
</tr>
<tr class="even">
<td>Semantic parsing</td>
<td>The parse is locally accepted.</td>
<td>Meaning remains stable under paraphrase, scope changes, and target-environment transformations.</td>
</tr>
<tr class="odd">
<td>Agents</td>
<td>The final state is achieved.</td>
<td>Authority, side effects, memory writes, rollback obligations, and audit traces are recorded.</td>
</tr>
</tbody>
</table>



These cases differ operationally and expose the same record problem. A reviewer needs to know the object type, environment, dependencies, assumptions, validators, source alignment, warrant, permitted use, and repair route. Without those fields, local success can be mistaken for durable contribution.

## 4. The seven thresholds {#4-the-seven-thresholds}

Semantic Participation separates seven thresholds that current AI evaluation often merges into one judgment. The separation matters as each threshold supports a different downstream inference and fails through a different mechanism.



<table>
<colgroup>
<col style="width: 18%"/>
<col style="width: 38%"/>
<col style="width: 42%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Threshold</strong></th>
<th><strong>What it establishes</strong></th>
<th><strong>Membership question</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Fluency</td>
<td>The artifact has acceptable surface form.</td>
<td>Which object type is being attempted?</td>
</tr>
<tr class="even">
<td>Task success</td>
<td>The system meets a local evaluation condition.</td>
<td>Which downstream environment can use the artifact?</td>
</tr>
<tr class="odd">
<td>Formal validity</td>
<td>A checker accepts a statement, proof, program, schema, or derivation.</td>
<td>Does the checked target preserve the intended source?</td>
</tr>
<tr class="even">
<td>Semantic alignment</td>
<td>The target artifact preserves intended meaning under a stated relation.</td>
<td>What changed, weakened, strengthened, or remained uncertain?</td>
</tr>
<tr class="odd">
<td>Composability</td>
<td>The artifact fits existing objects, interfaces, libraries, or protocols.</td>
<td>Which dependencies, interfaces, and reuse paths matter?</td>
</tr>
<tr class="even">
<td>Epistemic warrant</td>
<td>The support type is declared.</td>
<td>Which claims and actions are permitted from this artifact?</td>
</tr>
<tr class="odd">
<td>Reuse</td>
<td>Future systems or humans can build with the artifact.</td>
<td>Which maintenance, search, automation, and review conditions apply?</td>
</tr>
</tbody>
</table>



The distinction between formal validity and semantic alignment is central. A proof assistant can check that a term inhabits a formal statement under a specified environment <span class="citation-group">[<a class="citation-link" href="#ref-LeanRef" aria-label="Reference 2 — The Lean Language Reference">2</a>, <a class="citation-link" href="#ref-TPIL4" aria-label="Reference 3 — Theorem Proving in Lean 4">3</a>]</span>. The alignment relation asks whether that formal statement preserves the intended informal claim. In mathematical formalization, this separates proving a valid theorem from proving the theorem the source intended. In science, it separates a model-relative result from an empirical claim. In code, it separates passing tests from preserving the intended interface contract.

## 5. Formal core {#5-formal-core}

### 5.1 Semantic environment {#5-1-semantic-environment}

A semantic environment is a structured world in which artifacts can be expressed, transformed, checked, stored, diagnosed, reviewed, and reused. The definition is operational. It identifies the components that an implementation, benchmark, or review interface should expose.

> SemanticEnvironment E = {\
> Obj_E recognized objects\
> Art_E admissible artifacts\
> State_E structured environment state\
> Act_E admissible actions or transformations\
> Step_E State_E x Act_E -\> State_E + Diag_E\
> Check_E Art_E -\> CheckResult x Diag_E\
> Align_E Art_E x Source -\> AlignmentResult\
> Compose_E Art_E x Context_E -\> CompositionResult\
> Mem_E persistent environment memory\
> Review_E human, automated, or hybrid review procedure\
> }

Proof assistants, codebases, workflow systems, semantic parsers, data repositories, and laboratory protocols instantiate these components differently. The schema requires environment-relative membership in place of a universal validation rule.

### 5.2 ArtifactRecord {#5-2-artifactrecord}

An ArtifactRecord packages a generated object with the fields required for membership assessment. The record is a minimal audit surface for the object, its environment, its warrant, and its permitted use.

> ArtifactRecord a = {\
> id\
> content\
> representation\
> target_environment\
> dependencies\
> assumptions\
> source_intention\
> validation_path\
> validation_status\
> alignment_status\
> epistemic_type\
> compositional_role\
> permitted_use\
> prohibited_use\
> repair_path\
> review_status\
> }

The record should remain compact in low-risk settings and richer in high-stakes settings. Its value lies in changing review, repair, reuse, and downstream consumption. A record filled after the fact for cosmetic completeness has little scientific value.

### 5.3 Semantic membership {#5-3-semantic-membership}

Semantic membership is represented as an operational criterion over a target artifact, source intention, and preservation record.

> ParticipationStatus_E(a,b,rho,u) records the outcome of the declared environment\'s admission policy for artifact a, source intention b, preservation record rho, and proposed use u. It is accepted only if expression, successful validation or an accepted expert review, source alignment, compositional interface fit, warrant appropriate to the epistemic type, reuse eligibility where the requested use entails reuse, and permitted use all receive affirmative decisions. It is rejected on a decisive failed obligation and unresolved where required evidence remains missing or inconclusive. Reviewability alone establishes eligibility for review, not admission. This three-valued aggregate is an operational protocol whose outcomes depend on the specified environment and review policy.

Here a is the target artifact, b is the source intention or source artifact, and rho is the preservation record. The criterion is environment-relative. A theorem can fit one formal development and fail in another through imports, definitions, naming conventions, abstraction choices, and maintainability norms. A dataset can fit one scientific workflow and fail in another through consent conditions, preprocessing, instrument differences, and statistical assumptions.

### 5.4 Semantic transport {#5-4-semantic-transport}

Semantic transport is the movement of an artifact between environments with a preservation record. It records the semantic cost of translation, specialization, generalization, encoding, formalization, or institutional migration.

> T : (a, E_s) -\> (b, E_t, rho_T)\
> \
> TransportRecord rho_T = {\
> source_artifact\
> target_artifact\
> source_environment\
> target_environment\
> objects_preserved\
> transformations_preserved\
> assumptions_added\
> assumptions_removed_or_weakened\
> generality_change\
> definitions_selected\
> examples_preserved\
> counterexamples_excluded\
> validation_path\
> alignment_status\
> epistemic_type\
> permitted_use\
> reviewer_notes\
> }

Transport records prepare the ground for Functorial Consistency. Essay 3 asks whether source-side transformations and target-side transformations agree under an explicit equivalence regime. Essay 1 supplies the membership record that makes those transformations reviewable.

## 6. Lean as operational exemplar {#6-lean-as-operational-exemplar}

Lean is the privileged example for this essay as it makes several membership dimensions visible at once. A generated proof artifact can be elaborated, type checked, inspected through proof states, connected to library dependencies, repaired through diagnostics, and reviewed by maintainers. Lean therefore illustrates the separation among fluent proof sketch, formal target, proof term, checker acceptance, library integration, source-target alignment, and future reuse.

The trusted kernel establishes a strong form of formal validity for accepted artifacts relative to the formal statement and environment. The membership question extends that result by asking whether the formal statement captured the intended source claim, whether the selected definitions fit the intended mathematics, whether the artifact composes with library conventions, and whether future users can find, maintain, and reuse it.

Lean is one example in a broader family. Rocq and Isabelle/HOL provide distinct theorem-proving environments <span class="citation-group">[<a class="citation-link" href="#ref-RocqDocs" aria-label="Reference 4 — Rocq Prover documentation">4</a>, <a class="citation-link" href="#ref-IsabelleDocs" aria-label="Reference 5 — Isabelle documentation (Isabelle2025-1)">5</a>]</span>. Dafny and F* provide program-verification environments with different specification and trust models <span class="citation-group">[<a class="citation-link" href="#ref-DafnyDocs" aria-label="Reference 6 — Dafny Reference Manual">6</a>, <a class="citation-link" href="#ref-FStarDocs" aria-label="Reference 7 — Proof-Oriented Programming in F*">7</a>]</span>. Alloy supports relational software modeling <span class="citation-group">[<a class="citation-link" href="#ref-AlloyDocs" aria-label="Reference 8 — Alloy language specification">8</a>]</span>; PRISM and Storm support probabilistic model checking <span class="citation-group">[<a class="citation-link" href="#ref-PrismDocs" aria-label="Reference 9 — PRISM Manual: Introduction">9</a>, <a class="citation-link" href="#ref-StormDocs" aria-label="Reference 10 — Storm: A Modern Probabilistic Model Checker">10</a>]</span>. RO-Crate 1.1 specifies research-object metadata and provenance conventions <span class="citation-group">[<a class="citation-link" href="#ref-ROCrate11" aria-label="Reference 11 — RO-Crate Metadata Specification 1.1">11</a>]</span>. Scientific workflows and laboratory automation remain proposed extensions to the Semantic Participation framework. Each proposed extension needs its own object language, validators, review criteria, authority model, and permitted-use semantics.

## 7. Epistemic types {#7-epistemic-types}

AI systems need an explicit grammar of warrant. Current interfaces often present theorem, conjecture, proof sketch, simulation, empirical result, causal claim, approximation, benchmark result, and reviewed claim in the same confident register. Semantic Participation treats this as an epistemic-typing problem.



<table>
<colgroup>
<col style="width: 22%"/>
<col style="width: 12%"/>
<col style="width: 25%"/>
<col style="width: 39%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Epistemic type</strong></th>
<th colspan="2"><strong>Meaning</strong></th>
<th><strong>Permitted use</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Proved</td>
<td colspan="2">Established by mathematical or formal proof in a specified setting.</td>
<td>Supports theorem-level reasoning in that setting.</td>
</tr>
<tr class="even">
<td>FormallyValidated</td>
<td colspan="2">Accepted by a checker, compiler, verifier, or schema validator.</td>
<td>Supports target-environment operations under the stated validator.</td>
</tr>
<tr class="odd">
<td>Conjectural</td>
<td colspan="2">Plausible and unproved.</td>
<td>Guides exploration, search, or hypothesis generation.</td>
</tr>
<tr class="even">
<td>SimulationDerived</td>
<td colspan="2">Derived from simulation under model assumptions.</td>
<td>Supports model-relative claims and experimental design.</td>
</tr>
<tr class="odd">
<td>Empirical</td>
<td colspan="2">Supported by measurement or experiment.</td>
<td>Supports claims under protocol, sample, and uncertainty conditions.</td>
</tr>
<tr class="even">
<td>Causal</td>
<td colspan="2">Supported by intervention, identification, or causal model.</td>
<td>Supports causal claims under stated assumptions.</td>
</tr>
<tr class="odd">
<td>BenchmarkSupported</td>
<td colspan="2">Supported by benchmark performance.</td>
<td>Supports distribution-specific performance claims.</td>
</tr>
<tr class="even">
<td>AlignmentUncertain</td>
<td colspan="2">Target-source preservation remains unresolved.</td>
<td>Requires review before downstream promotion.</td>
</tr>
<tr class="odd">
<td>LibraryIntegrated</td>
<td colspan="2">Accepted into a maintained environment with a reuse path.</td>
<td>Supports future reasoning and automation.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Type transition</strong></td>
<td colspan="2"><strong>Required control</strong></td>
</tr>
<tr class="odd">
<td colspan="2">Conjectural -&gt; theorem-level use</td>
<td colspan="2">Proof or formal validation.</td>
</tr>
<tr class="even">
<td colspan="2">SimulationDerived -&gt; empirical use</td>
<td colspan="2">Empirical protocol with instruments, samples, controls, uncertainty, and review.</td>
</tr>
<tr class="odd">
<td colspan="2">BenchmarkSupported -&gt; general competence</td>
<td colspan="2">Additional evidence outside the benchmark distribution.</td>
</tr>
<tr class="even">
<td colspan="2">AlignmentUncertain -&gt; promoted use</td>
<td colspan="2">Transport or alignment resolution with reviewer notes.</td>
</tr>
</tbody>
</table>



Epistemic typing is stronger than provenance and weaker than proof. Provenance records origin. Proof records exact derivation in a formal or mathematical setting. Epistemic typing records the kind of warrant an artifact has and the operations it can responsibly support.

## 8. Library improvement delta {#8-library-improvement-delta}

A system that proves local goals can still make a weak contribution to a formal world. Formal libraries are memory systems whose value depends on theorem reuse, searchability, naming, abstraction, dependency control, automation compatibility, proof robustness, and maintainer acceptance.

$$
\Delta_L(c)=F(L+c)-F(L).
$$

This expression should be interpreted as a vector-valued diagnostic. A contribution can improve one dimension and degrade another.



<table>
<colgroup>
<col style="width: 32%"/>
<col style="width: 67%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Dimension</strong></th>
<th><strong>Diagnostic question</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Downstream proof cost</td>
<td>Does the contribution reduce future formalization effort?</td>
</tr>
<tr class="even">
<td>Theorem reuse</td>
<td>Does it support future statements beyond the local task?</td>
</tr>
<tr class="odd">
<td>Premise retrieval quality</td>
<td>Does it improve search and relevance for proof agents?</td>
</tr>
<tr class="even">
<td>Automation success</td>
<td>Does it improve tactic or automation performance?</td>
</tr>
<tr class="odd">
<td>Dependency control</td>
<td>Does it avoid unnecessary imports and fragile dependencies?</td>
</tr>
<tr class="even">
<td>Naming quality</td>
<td>Can humans and tools find the object?</td>
</tr>
<tr class="odd">
<td>Maintainer acceptance</td>
<td>Does it match library norms and review expectations?</td>
</tr>
<tr class="even">
<td>Duplicate rate</td>
<td>Does it avoid unnecessary redundancy?</td>
</tr>
</tbody>
</table>



The purpose is to evaluate candidate contributions across dimensions that matter for future reasoning. A theorem that checks and remains unfindable, overly specialized, duplicative, or difficult to maintain is a weak library contribution.

## 9. Worked case studies {#9-worked-case-studies}

### 9.1 Extreme Value Theorem and the gap between supremum and attainment {#9-1-extreme-value-theorem-and-the-gap-between-supremum-and-attain}

Semantic transport is visible when an informal theorem moves into a formal environment. Consider the source claim.

> Every continuous real-valued function on a compact interval attains a maximum.

The statement includes several semantic commitments. It specifies a real-valued function, a compact interval, continuity on that interval, a witness point in the interval, and a universal comparison showing that the function value at that point is maximal.

A plausible misformalization proves that the image of the interval is bounded above or has a supremum. That target is mathematically related to the source claim and loses the intended conclusion. Supremum existence is an upper-bound property. Attainment requires a witness point.

> supremum existence is weaker than the existence of x such that f x is maximal on the interval\
> \
> expected shape\
> exists x in Icc a b, forall y in Icc a b, f y \<= f x

The transport record should expose the interval representation, compactness theorem, continuity assumption, codomain, order structure, theorem generality, and reuse path. The proof assistant can certify the formal target. The transport record assesses whether the target captures the source claim.

### 9.2 From simulation-derived stability to empirical scientific claim {#9-2-from-simulation-derived-stability-to-empirical-scientific-cla}

Scientific semantic transport is harder since the target environment combines literature, models, simulations, instruments, protocols, samples, measurements, statistics, uncertainty, and review. Consider the sentence.

> Molecule X is likely stable.

The sentence can describe a literature-supported conjecture, a model-relative prediction, a simulation-derived result, an empirical measurement, or a causal claim about stability under specified interventions. The surface sentence therefore admits several epistemic types.



<table>
<colgroup>
<col style="width: 31%"/>
<col style="width: 68%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Status</strong></th>
<th><strong>Required record</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Model-relative prediction</td>
<td>Model class, training domain, assumptions, calibration, uncertainty, and out-of-distribution indicators.</td>
</tr>
<tr class="even">
<td>Simulation-derived result</td>
<td>Simulation method, force field or quantum method, temperature, timescale, convergence, and sensitivity checks.</td>
</tr>
<tr class="odd">
<td>Empirical measurement</td>
<td>Instrument, protocol, sample conditions, replicates, statistics, controls, and uncertainty.</td>
</tr>
<tr class="even">
<td>Causal claim</td>
<td>Intervention, identification assumptions, mechanism, counterfactual scope, and review procedure.</td>
</tr>
</tbody>
</table>



The semantic-participation failure is promotion across epistemic types without additional warrant. A simulation-derived artifact can guide experimental design. It should retain model-relative status until empirical evidence supports a stronger claim.

## 10. Semantic Participation Bench v0.3 {#10-semantic-participation-bench-v0-3}

The benchmark agenda tests whether membership records improve diagnosis, review, repair, reuse, and permitted-use control. The first phase should use domains where validators and review procedures already exist, then expand to scientific and institutional settings where alignment and epistemic typing exert greater influence.



<table>
<colgroup>
<col style="width: 18%"/>
<col style="width: 22%"/>
<col style="width: 28%"/>
<col style="width: 29%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Track</strong></th>
<th><strong>Input</strong></th>
<th><strong>Primary metric</strong></th>
<th><strong>Diagnostic value</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Mathematics transport</td>
<td>Informal theorem plus candidate formal target.</td>
<td>Source-target alignment, formal validity, generality preservation.</td>
<td>Separates checked proof from intended-theorem preservation.</td>
</tr>
<tr class="even">
<td>Code membership</td>
<td>Natural-language requirement plus patch.</td>
<td>Interface preservation, invariant preservation, test coverage, dependency impact.</td>
<td>Separates passing tests from codebase membership.</td>
</tr>
<tr class="odd">
<td>Science epistemic typing</td>
<td>Model result, simulation, protocol, or claim.</td>
<td>Epistemic-type accuracy and permitted-use correctness.</td>
<td>Prevents promotion across warrant types.</td>
</tr>
<tr class="even">
<td>Library delta</td>
<td>Formal contribution candidate.</td>
<td>Reuse, search, dependency control, automation compatibility, maintainer fit.</td>
<td>Measures contribution to future reasoning.</td>
</tr>
<tr class="odd">
<td>Semantic transport</td>
<td>Artifact moved across representation or environment.</td>
<td>Preservation, loss, assumption changes, repair cost.</td>
<td>Records what changed during transport.</td>
</tr>
</tbody>
</table>



> semantic_participation_item:\
> item_id\
> domain\
> source_artifact\
> source_environment\
> target_environment\
> candidate_artifact\
> expected_membership_conditions\
> validators\
> alignment_questions\
> epistemic_type_options\
> permitted_use_options\
> failure_labels\
> reviewer_protocol

The first pilot should use 100 to 150 items distributed across mathematics transport, code membership, science epistemic typing, and library delta. The pilot should report local validity, alignment accuracy, epistemic-type accuracy, assumption preservation, repair cost, reviewer agreement, and diagnostic novelty.

## 11. Relationship to Functorial Consistency {#11-relationship-to-functorial-consistency}

Semantic Participation supplies the membership criterion. Functorial Consistency supplies the transformation test. A semantic environment specifies what counts as an artifact, which validators apply, which epistemic type is warranted, and which uses are permitted. A commutation-square benchmark then asks whether transformations preserve structure across source and target representations.

> Under environment version E_v and admission-policy version π, Adm_{E_v,π}(a,b,ρ,u) records accepted, rejected, or unresolved admission of artifact a for proposed use u, source intention b, and preservation evidence ρ. The policy identifies mandatory obligations, judgment authorities, evidence freshness, and the precedence of decisive failures. Acceptance records affirmative discharge of all mandatory obligations, including expression, validation or approved expert review, source alignment, compositional interface fit, epistemic warrant, and permitted use; reuse eligibility is a mandatory obligation only for proposed uses involving reuse. A decisive mandatory failure yields rejection; missing, stale, conflicting, or inconclusive evidence yields an unresolved outcome under the declared precedence rule. An empty obligation set yields unresolved status except where π explicitly authorizes vacuous admission. Review eligibility is recorded independently. The earlier Boolean Member_E(a) denotes accepted status only relative to specified environment, policy, and use versions.

The transport record rho_T is the bridge. It records source artifact, target artifact, environments, transformations preserved, assumptions changed, generality changes, validators, alignment status, epistemic type, and permitted use. Functorial Consistency can use that record to classify non-commutation, type drift, assumption loss, generality collapse, overstrengthening, spurious equivalence, and validator mismatch.

## 12. Strongest objections and response protocol {#12-strongest-objections-and-response-protocol}



<table>
<colgroup>
<col style="width: 37%"/>
<col style="width: 62%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Objection</strong></th>
<th><strong>Response protocol</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This is only formal verification with new vocabulary.</td>
<td>The proposal uses formal verification as one validation regime and adds source-target alignment, epistemic type, composability, reuse, and permitted use.</td>
</tr>
<tr class="even">
<td>This is only provenance.</td>
<td>Provenance records origin. Semantic participation records membership, warrant, composition, validation, and use conditions.</td>
</tr>
<tr class="odd">
<td>The framework is too broad.</td>
<td>Breadth must be earned through domain-specific validators, benchmarks, and kill criteria.</td>
</tr>
<tr class="even">
<td>Human review does the real work.</td>
<td>Human review gains reliability when artifacts expose dependencies, assumptions, transport records, and epistemic types.</td>
</tr>
<tr class="odd">
<td>Records will turn into bureaucracy.</td>
<td>Records should be minimized and retained only when they improve diagnosis, repair, review, reuse, or permitted-use control.</td>
</tr>
<tr class="even">
<td>Formal-environment lessons can transfer poorly to science.</td>
<td>The first empirical phase should test transfer through science-specific epistemic typing and protocol records.</td>
</tr>
<tr class="odd">
<td>Library delta cannot be reduced to a scalar.</td>
<td>The delta is vector-valued and review-assisted. Scalar aggregation is an optional reporting layer, not the core object.</td>
</tr>
</tbody>
</table>



## 13. Failure modes and kill criteria {#13-failure-modes-and-kill-criteria}



<table>
<colgroup>
<col style="width: 32%"/>
<col style="width: 67%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Failure mode</strong></th>
<th><strong>Meaning</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Record inertia</td>
<td>ArtifactRecords are filled out and do not affect review, repair, or reuse.</td>
</tr>
<tr class="even">
<td>Alignment opacity</td>
<td>Formal validity is reported and source-target preservation remains unclear.</td>
</tr>
<tr class="odd">
<td>Epistemic promotion</td>
<td>Conjectures, simulations, benchmark results, or model-relative claims are consumed as stronger claim types.</td>
</tr>
<tr class="even">
<td>Environment mismatch</td>
<td>An artifact is valid in one environment and presented as a member of another without a transport record.</td>
</tr>
<tr class="odd">
<td>Library drag</td>
<td>Candidate contributions increase maintenance, dependency complexity, or duplication.</td>
</tr>
<tr class="even">
<td>Review collapse</td>
<td>Human review remains unstructured after the record is introduced.</td>
</tr>
<tr class="odd">
<td>Benchmark collapse</td>
<td>Membership benchmarks measure ordinary accuracy instead of artifact integration.</td>
</tr>
</tbody>
</table>



-   K1. ArtifactRecords do not improve reviewer agreement, diagnosis, repair, or reuse.

-   K2. Transport records do not reduce source-target alignment errors.

-   K3. Epistemic typing does not reduce warrant-promotion errors.

-   K4. Library delta fails to predict maintainer value, reuse, searchability, or automation compatibility.

-   K5. Human reviewers cannot use membership records to make better decisions.

-   K6. Semantic Participation Bench collapses into ordinary accuracy or benchmark score.

-   K7. Record creation costs exceed measured diagnostic or reuse gains.

-   K8. Formal-environment insights fail to transfer to scientific protocol and evidence settings.

## 14. Conclusion {#14-conclusion}

Semantic Participation is the membership core of Compositional Intelligence. It states that AI-generated objects count as serious artifacts only when they enter structured worlds with recorded validation, source-target alignment, compositional role, epistemic status, and permitted use. The framework is strongest where it changes practice through earlier failure detection, clearer validation, targeted repair, stronger library contribution, appropriate scientific warrant, and controlled downstream consumption.

The essay prepares the rest of the series. Typed Generativity explains how models infer target types and construct candidate inhabitants. Functorial Consistency tests whether artifacts preserve structure under transformations. Later essays extend membership to language, architecture, warrant, and action. The result is a world-centric account of AI reasoning as construction, transformation, validation, warranting, and execution of typed artifacts inside structured environments.

## Appendix A. Minimal ArtifactRecord schema {#appendix-a-minimal-artifactrecord-schema}

> artifact_record:\
> id: string\
> kind: string\
> content: string \| object\
> representation: string\
> target_environment: string\
> dependencies: list\[string\]\
> assumptions: list\[string\]\
> source_intention: string\
> validation_path: string\
> validation_status: string\
> alignment_status: string\
> epistemic_type: string\
> compositional_role: string\
> permitted_use: list\[string\]\
> prohibited_use: list\[string\]\
> repair_path: string \| null\
> review_status: string

## Appendix B. Minimal TransportRecord schema {#appendix-b-minimal-transportrecord-schema}

> transport_record:\
> source_artifact: string \| object\
> target_artifact: string \| object\
> source_environment: string\
> target_environment: string\
> transformation_type: string\
> objects_preserved: list\[string\]\
> transformations_preserved: list\[string\]\
> assumptions_added: list\[string\]\
> assumptions_removed_or_weakened: list\[string\]\
> generality_change: string\
> definitions_selected: list\[string\]\
> examples_preserved: list\[string\]\
> counterexamples_excluded: list\[string\]\
> validation_path: string\
> alignment_status: string\
> epistemic_type: string\
> permitted_use: list\[string\]\
> reviewer_notes: string

## Appendix C. Claim ledger {#appendix-c-claim-ledger}



<table>
<colgroup>
<col style="width: 48%"/>
<col style="width: 11%"/>
<col style="width: 39%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Claim</strong></th>
<th><strong>Level</strong></th>
<th><strong>Treatment</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Proof assistants and formal methods provide validation machinery for formal artifacts.</td>
<td>L0/L1</td>
<td>Cite system and documentation sources directly.</td>
</tr>
<tr class="even">
<td>Lean is a concrete exemplar for semantic environments as it exposes formal statements, proof checking, diagnostics, libraries, and review.</td>
<td>L1/L2</td>
<td>Support with Lean documentation, Theorem Proving in Lean 4, Mathlib, and LeanDojo where relevant.</td>
</tr>
<tr class="odd">
<td>Semantic Participation is a membership framework for AI-generated artifacts.</td>
<td>L3</td>
<td>Mark as an original proposal.</td>
</tr>
<tr class="even">
<td>ArtifactRecords improve alignment, review, repair, and reuse.</td>
<td>L4</td>
<td>Test through benchmark pilots.</td>
</tr>
<tr class="odd">
<td>Epistemic typing reduces warrant-promotion errors in science and formalization.</td>
<td>L4</td>
<td>Test through controlled annotation and review tasks.</td>
</tr>
<tr class="even">
<td>Library improvement delta predicts future reasoning value.</td>
<td>L4</td>
<td>Test against maintainer judgment and reuse traces.</td>
</tr>
</tbody>
</table>




<section class="bibliography" aria-labelledby="references-heading">
<h2 id="references-heading">References</h2>

<ol class="references-list">
<li id="ref-Lambek1958"><span class="ref-key">[1]</span> <a href="https://doi.org/10.1080/00029890.1958.11989160" rel="noopener noreferrer">The Mathematics of Sentence Structure</a>. <span class="ref-details">Joachim Lambek · American Mathematical Monthly 65(3), 1958.</span></li>
<li id="ref-LeanRef"><span class="ref-key">[2]</span> <a href="https://lean-lang.org/doc/reference/latest/" rel="noopener noreferrer">The Lean Language Reference</a>. <span class="ref-details">Lean Community · online reference.</span></li>
<li id="ref-TPIL4"><span class="ref-key">[3]</span> <a href="https://docs.lean-lang.org/theorem_proving_in_lean4/" rel="noopener noreferrer">Theorem Proving in Lean 4</a>. <span class="ref-details">Avigad, de Moura, Kong, and Ullrich · online textbook.</span></li>
<li id="ref-RocqDocs"><span class="ref-key">[4]</span> <a href="https://rocq-prover.org/docs" rel="noopener noreferrer">Rocq Prover documentation</a>. <span class="ref-details">Rocq Prover project · official documentation portal; evolving edition, accessed November 2026.</span></li>
<li id="ref-IsabelleDocs"><span class="ref-key">[5]</span> <a href="https://isabelle.in.tum.de/website-Isabelle2025-1/documentation.html" rel="noopener noreferrer">Isabelle documentation (Isabelle2025-1)</a>. <span class="ref-details">Isabelle project · official versioned Isabelle/HOL documentation.</span></li>
<li id="ref-DafnyDocs"><span class="ref-key">[6]</span> <a href="https://dafny.org/dafny/DafnyRef/DafnyRef.html" rel="noopener noreferrer">Dafny Reference Manual</a>. <span class="ref-details">Dafny project · official reference manual; evolving edition, accessed November 2026.</span></li>
<li id="ref-FStarDocs"><span class="ref-key">[7]</span> <a href="https://fstar-lang.org/tutorial/book/" rel="noopener noreferrer">Proof-Oriented Programming in F*</a>. <span class="ref-details">F* project · official proof-oriented programming textbook; evolving edition.</span></li>
<li id="ref-AlloyDocs"><span class="ref-key">[8]</span> <a href="https://alloytools.org/spec.html" rel="noopener noreferrer">Alloy language specification</a>. <span class="ref-details">Alloy Tools · official language specification; evolving edition.</span></li>
<li id="ref-PrismDocs"><span class="ref-key">[9]</span> <a href="https://prismmodelchecker.org/manual/Main/Introduction" rel="noopener noreferrer">PRISM Manual: Introduction</a>. <span class="ref-details">PRISM project · official probabilistic model-checking manual; evolving edition.</span></li>
<li id="ref-StormDocs"><span class="ref-key">[10]</span> <a href="https://www.stormchecker.org/" rel="noopener noreferrer">Storm: A Modern Probabilistic Model Checker</a>. <span class="ref-details">Storm project · official documentation and scope statement; evolving edition.</span></li>
<li id="ref-ROCrate11"><span class="ref-key">[11]</span> <a href="https://www.researchobject.org/ro-crate/specification/1.1/" rel="noopener noreferrer">RO-Crate Metadata Specification 1.1</a>. <span class="ref-details">Research Object Crate community · Recommendation, 26 April 2023 · DOI:10.5281/zenodo.7867028.</span></li>
</ol>
</section>
