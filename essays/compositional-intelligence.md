# Compositional Intelligence

*Mateo Petel*

## Abstract

Generative AI is often evaluated through output quality, benchmark performance, and local task performance. Those measures register useful capability, although they leave under-specified the condition that matters for cumulative knowledge and agentic deployment. A generated object has standing when a structured world can check it, align it with an intended source, compose it with existing objects, reuse it under declared conditions, warrant it at an appropriate epistemic level, or authorize action under controlled effects.

This paper introduces Compositional Intelligence, a proposed research program for typed artifacts in structured worlds. The framework has three central components. Semantic participation defines artifact membership through validation, alignment, composability, epistemic status, and permitted use. Typed generativity models generation as target-type inference followed by probabilistic construction of candidate inhabitants. Functorial Consistency evaluates whether transformations commute across source and target representations under explicit equivalence regimes.

The paper then compresses three supporting layers. Architecture specification treats model families as structural commitments about objects, transformations, symmetries, interfaces, and validators. Quantitative Curry-Howard attaches evidence records to candidate typed artifacts and preserves the boundary between soft warrant and proof. Typed action ledgers record preconditions, postconditions, effects, authority, handlers, validators, and audit traces for agentic systems.

The proposal is falsifiable. Its schemas and benchmarks matter only if they improve diagnosis, validation, repair, reuse, architecture choice, calibration, or effect control.

## Introduction

A generated proof sketch, code patch, theorem formalization, scientific protocol, plan, or tool call has value when it can enter an environment that supplies validation, integration, repair, rejection, and permitted use. Benchmark accuracy and task completion remain useful measurement instruments, since they make capability comparable. They remain insufficient for artifacts that must enter cumulative technical systems, where surface plausibility gives limited information about alignment, dependency preservation, future reuse, or action authority.

The output-artifact distinction is clearest in structured environments. A proof assistant checks a formal proof relative to a formal statement, and source-target alignment remains a separate obligation. A code patch can satisfy visible tests and still violate an interface, invariant, or dependency relation. A scientific protocol can appear coherent and omit controls, uncertainty, stopping conditions, or the claim type it can support. An agent can reach a target state through tool calls, web or computer interaction, memory updates, delegated authority, or exposure to untrusted instructions. Compositional Intelligence treats those trajectories as effectful traces requiring authority, memory, validation, and side-effect records.

Compositional Intelligence evaluates generative AI as the construction, transformation, validation, warranting, and execution of typed artifacts inside structured worlds. A typed artifact is an attempted object under constraints, including a proof, program, theorem statement, semantic parse, experimental protocol, plan, explanation, database query, memory write, tool call, or skill. A structured world is an environment in which such objects have dependencies, validators, admissible transformations, review practices, epistemic statuses, and permitted uses.

The framework has different uses across research communities. Evaluation researchers can convert structure-preservation failures into benchmark items. Formal-methods researchers can separate checker validity from source-target alignment and downstream semantic use. Agent researchers can distinguish target state success from acceptable state-changing traces. AI-for-science researchers can treat protocols, claims, and experimental plans as artifacts whose assumptions, warrant, and permitted uses require explicit representation.

The core technical test is structure preservation across transformations. If a source object is transformed before translation, and the translated object is transformed afterward, the two paths must agree under a declared equivalence regime. The commutation test turns the framework into an evaluation unit, drawing on compositional-generalization and transformation-sensitive evaluation and adding a benchmark record centered on source path, target path, validator, and failure label.

The unit of analysis is the typed artifact with a record. The record states the attempted object kind, assumptions, dependencies, validation status, transformation behavior, warrant type, permitted downstream uses, and possible effects. The framework does not impose a single formal machinery across domains; it requires each domain to declare its validation regime and epistemic type.

This paper contributes five objects and principles.

1.  It defines a membership criterion for AI-generated artifacts, called semantic participation.

2.  It introduces a typed-generativity schema for target-type inference and candidate construction.

3.  It proposes Functorial Consistency as a commutation-square evaluation principle and the paper\'s central benchmark object.

4.  It compresses architecture, warrant, and effectful action into a compact record protocol.

5.  It states a falsifiable benchmark agenda for testing whether these records improve diagnosis, validation, repair, reuse, architecture choice, calibration, or effect control.

The paper\'s claim protocol is explicit. The cited literatures support background formalisms, systems, and benchmarks. The schemas and benchmark objects introduced as Compositional Intelligence artifacts are original proposals. Their practical value remains an empirical question.

## From Outputs to Artifacts

Output-centric evaluation asks whether an answer is fluent, persuasive, benchmark-correct, or locally successful. That grammar is adequate when the task boundary is narrow and the output is the final object of interest. It weakens when generated objects must enter cumulative technical environments.

A membership-centric grammar asks whether a generated object can occupy a stable position inside a structured world. The artifact must be expressible in the environment, validated by available checkers or review procedures, aligned with its source intention, composable with existing objects, and usable in later reasoning under stated conditions. Progress is measured by an artifact with a record, dependencies, warrant, permitted uses, and an integration pathway.

Three recurring failures motivate the shift.

Table. Output failures and missing artifact conditions.



<table>
<colgroup>
<col style="width: 29%"/>
<col style="width: 29%"/>
<col style="width: 41%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Domain</strong></th>
<th><strong>Local success</strong></th>
<th><strong>Missing artifact condition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>formalization</td>
<td>proof artifact checks</td>
<td>formal statement checking <span class="citation-group">[<a aria-label="Reference 1 — The Lean Language Reference" class="citation-link" href="#ref-LeanRef">1</a>, <a aria-label="Reference 2 — Theorem Proving in Lean 4" class="citation-link" href="#ref-TPIL4">2</a>]</span>, plus independently assessed source–target alignment</td>
</tr>
<tr class="even">
<td>code</td>
<td>tests pass under the visible test regime</td>
<td>interface and invariant preservation</td>
</tr>
<tr class="odd">
<td>agents</td>
<td>target state reached</td>
<td>benchmark task, policy, and attack outcomes <span class="citation-group">[<a aria-label="Reference 3 — WebArena: A Realistic Web Environment for Building Autonomous Agents" class="citation-link" href="#ref-WebArena2023">3</a>, <a aria-label="Reference 4 — OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments" class="citation-link" href="#ref-OSWorld2024">4</a>, <a aria-label="Reference 5 — τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains" class="citation-link" href="#ref-TauBench2025">5</a>, <a aria-label="Reference 6 — AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents" class="citation-link" href="#ref-AgentDojo2024">6</a>]</span>, plus a separate authority-and-effect trace</td>
</tr>
</tbody>
</table>



These failures differ operationally, but they share a record problem. The evaluator cannot tell what kind of object was produced, what it preserves, what warrants it, and what it is allowed to affect.

**output -\> candidate artifact -\> typed candidate -\> transformed artifact\
**-\> validated artifact -\> warranted artifact -\> reusable artifact -\> effectful action

Figure. From output to artifact. The lifecycle is conceptual instead of strictly linear; its purpose is to expose the status of generated objects as they enter structured worlds.

This lifecycle is neither strictly linear nor universal. Some artifacts never receive formal validation. Some are reviewed. Some remain conjectural. Some are useful as heuristics. Some should be rejected. The relevant condition is that the artifact\'s status should be explicit.

A generated theorem statement, proof script, function, protocol, semantic parse, plan, or tool call should therefore include enough structure for the target environment to judge it. The record need not be long. It should answer the questions that determine whether the object can participate: what kind of object it is, what environment it targets, what constraints it must satisfy, what validates it, what it preserves, what remains uncertain, and what uses are allowed.

## Semantic Participation

Semantic participation is the capacity of an AI system to place artifacts inside a semantic environment with recorded validation, alignment, compositional role, epistemic status, and permitted use. It is the membership criterion proposed in this paper.

A semantic environment is a structured world with objects, validators, dependencies, admissible operations, memory, review practices, and reuse conditions. Proof assistants, codebases, scientific workflows, laboratory systems, semantic parsers, research-object repositories, design catalogs, and agent runtimes are all possible semantic environments. They differ in validation strength, but they share the membership problem. Lean provides a concrete example of formal validation through dependent type theory and proof checking [\[[1](#ref-LeanRef){.citation-link aria-label="Reference 1 — The Lean Language Reference"}, [2](#ref-TPIL4){.citation-link aria-label="Reference 2 — Theorem Proving in Lean 4"}\]]{.citation-group}. LeanDojo adds programmatic interaction, proof-data extraction, and retrieval-augmented theorem-proving infrastructure around Lean [\[[7](#ref-LeanDojo2023){.citation-link aria-label="Reference 7 — LeanDojo: Theorem Proving with Retrieval-Augmented Language Models"}\]]{.citation-group}.

An artifact semantically participates in an environment when it is expressible there, checkable or reviewable there, aligned with its intended source, composable with relevant objects, and assigned an epistemic type that constrains downstream use.

The central distinction is among thresholds that are often collapsed. Fluency shows that a model can produce acceptable surface form. Task success shows that a system can meet an evaluation condition. Formal validity shows that a proof term is accepted by a formal checker relative to its stated proposition, environment, and axiom dependencies [\[[1](#ref-LeanRef){.citation-link aria-label="Reference 1 — The Lean Language Reference"}, [2](#ref-TPIL4){.citation-link aria-label="Reference 2 — Theorem Proving in Lean 4"}\]]{.citation-group}. Source-target alignment shows that the artifact preserves the intended source meaning. Epistemic utility shows that the artifact can be used responsibly in later reasoning. Semantic participation requires these thresholds to be recorded together.

Table. Semantic participation thresholds.



<table>
<colgroup>
<col style="width: 25%"/>
<col style="width: 24%"/>
<col style="width: 25%"/>
<col style="width: 24%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Threshold</strong></th>
<th><strong>What it establishes</strong></th>
<th><strong>What it leaves open</strong></th>
<th><strong>Record needed</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>fluency</td>
<td>surface plausibility</td>
<td>validity, alignment, warrant</td>
<td>artifact type</td>
</tr>
<tr class="even">
<td>task success</td>
<td>local performance</td>
<td>downstream reuse</td>
<td>evaluation context</td>
</tr>
<tr class="odd">
<td>formal validity</td>
<td>checker acceptance</td>
<td>source-target alignment</td>
<td>formal statement and source map</td>
</tr>
<tr class="even">
<td>semantic alignment</td>
<td>intended meaning preserved</td>
<td>warrant and reuse</td>
<td>transport record</td>
</tr>
<tr class="odd">
<td>composability</td>
<td>fits existing objects</td>
<td>long-term value</td>
<td>dependency and interface record</td>
</tr>
<tr class="even">
<td>epistemic warrant</td>
<td>kind of support known</td>
<td>permitted use</td>
<td>epistemic type</td>
</tr>
<tr class="odd">
<td>reuse</td>
<td>future use possible</td>
<td>maintenance cost</td>
<td>reuse conditions</td>
</tr>
</tbody>
</table>



Semantic participation depends on existing validation machinery without collapsing into it. Proof assistants supply environments where formal derivations can be checked; Semantic Participation adds the membership criterion linking validation, alignment, composability, epistemic type, and permitted use [\[[1](#ref-LeanRef){.citation-link aria-label="Reference 1 — The Lean Language Reference"}, [2](#ref-TPIL4){.citation-link aria-label="Reference 2 — Theorem Proving in Lean 4"}\]]{.citation-group}.

The proposed ArtifactRecord makes this membership question inspectable. A minimal record includes target environment, dependencies, assumptions, validation status, epistemic type, alignment status, permitted use, and repair path. The record is useful only if it changes what reviewers, validators, users, or downstream systems can do. It should expose hidden assumptions, wrong target claims, weak warrant, dependency problems, poor library fit, unsupported reuse, or failure to preserve meaning across transport. If it simply adds documentation without improving diagnosis or reuse, it fails.

Semantic participation is therefore an original proposal in the series. It does not claim to invent proof checking, provenance, formal verification, or research-object packaging. It proposes that AI reasoning should be evaluated by artifact membership in structured semantic environments, where validity, source-target alignment, epistemic status, compositional role, and downstream reuse are recorded together.

## Typed Generativity

Typed generativity models generation as target-type inference followed by candidate-inhabitant construction:

P_theta(A,t \| c) = P_theta(A \| c) P_theta(t \| A,c).

Here c is the generator context, including prompts, retrieved material, examples, tools, memory and environment. A is a declared target-class label, while t is a candidate representation that can later fail validation. The factorization assumes a normalized joint model distribution on a specified tagged candidate space and follows from the probability chain rule. For formal tasks, the independent judgment Δ ⊢ t : τ belongs to an object-language typing environment Δ and a target type τ; mapping A to τ is a domain-specific obligation. Model rankings without a normalized distribution retain ranking semantics. Claims about latent type-like representations remain empirical hypotheses.

Generation tasks admit a target-artifact analysis. In a Lean theorem-proving task, A denotes the elaborated proposition to be proved, while t denotes a candidate core proof term checked against A under the declared environment and axioms. A tactic script supplies source-level instructions for constructing that term; the script itself is distinct from a term inhabiting A [\[[1](#ref-LeanRef){.citation-link aria-label="Reference 1 — The Lean Language Reference"}, [2](#ref-TPIL4){.citation-link aria-label="Reference 2 — Theorem Proving in Lean 4"}, [7](#ref-LeanDojo2023){.citation-link aria-label="Reference 7 — LeanDojo: Theorem Proving with Retrieval-Augmented Language Models"}\]]{.citation-group}. In a tool-use setting, our abstraction treats A as an action schema and t as a candidate call with arguments, with tool-use work providing the motivating context [\[[8](#ref-Toolformer2023){.citation-link aria-label="Reference 8 — Toolformer: Language Models Can Teach Themselves to Use Tools"}\]]{.citation-group}. In a scientific setting, A can be a protocol type and t a candidate procedure. In an explanation setting, A can be an audience-specific explanatory artifact and t a candidate explanation with scope, assumptions, and warrant.

The schema provides an abstraction. It does not claim that current language models literally implement dependent type theory. It distinguishes the object layer from the token substrate. Source code is a string, but it is evaluated as a program. A Lean script is text, but it elaborates into formal objects [\[[1](#ref-LeanRef){.citation-link aria-label="Reference 1 — The Lean Language Reference"}, [2](#ref-TPIL4){.citation-link aria-label="Reference 2 — Theorem Proving in Lean 4"}\]]{.citation-group}. A structured data response is text, but it is consumed as a typed object by downstream software. A scientific protocol is text, but it encodes actions, controls, measurements, stopping conditions, analysis plans, and permitted claims. Typed generativity studies this object layer.

Table. Levels of typed generation.



<table>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Level</strong></th>
<th><strong>Meaning</strong></th>
<th><strong>Status</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>typed output</td>
<td>artifact checked after generation</td>
<td>operational</td>
</tr>
<tr class="even">
<td>typed decoding</td>
<td>generation constrained by schema, grammar, type, or interface</td>
<td>operational</td>
</tr>
<tr class="odd">
<td>typed latent cognition</td>
<td>model internally represents target-object structure</td>
<td>hypothesis</td>
</tr>
</tbody>
</table>



Typed output is visible in proof assistants, and tool-use work shows a related interface layer in which model outputs are consumed as calls to external tools [\[[1](#ref-LeanRef){.citation-link aria-label="Reference 1 — The Lean Language Reference"}, [2](#ref-TPIL4){.citation-link aria-label="Reference 2 — Theorem Proving in Lean 4"}, [8](#ref-Toolformer2023){.citation-link aria-label="Reference 8 — Toolformer: Language Models Can Teach Themselves to Use Tools"}\]]{.citation-group}. Typed latent cognition remains a hypothesis about internal representations. The paper does not require it. The operational framework requires only that outputs and decoding constraints can be evaluated against target types.

Table. Typed-generativity failure taxonomy.



<table>
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Failure</strong></th>
<th><strong>Meaning</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>target-type ambiguity</td>
<td>task admits several object types</td>
</tr>
<tr class="even">
<td>target-type mismatch</td>
<td>system chooses the wrong object class</td>
</tr>
<tr class="odd">
<td>target-type drift</td>
<td>generation changes target midway</td>
</tr>
<tr class="even">
<td>invalid inhabitant</td>
<td>object has right type but fails validation</td>
</tr>
<tr class="odd">
<td>valid non-participation</td>
<td>object validates locally but fails membership</td>
</tr>
</tbody>
</table>



These failures require different interventions. A wrong target type calls for better disambiguation. An invalid inhabitant calls for checking and repair. A valid non-participating artifact calls for source-target alignment, dependency analysis, or permitted-use constraints.

The Type-First Prompting Harness proposed below tests whether explicit target-type articulation improves artifact construction across code, Lean or mathematics, explanation, scientific protocol design, and planning. It is a test of the typed-generativity hypothesis. If explicit target-type articulation merely adds verbosity, the intervention should be rejected. The diagnostic framework can remain useful, but the practical method would need revision.

## Functorial Consistency

Functorial Consistency is the paper\'s central evaluation proposal. It tests whether an AI system preserves task-relevant structure across transformations. The idea is that a source object can be transformed before translation, or translated before the corresponding target-side transformation. A structure-preserving system should make these two paths agree under a specified equivalence regime.

The claim is diagnostic. Local correctness is too weak. A model can produce a plausible theorem, working program, valid semantic parse, or reasonable plan and still fails to preserve the relation that gives the artifact its meaning. A theorem can be valid in isolation although losing generality under formalization. A program can pass tests and still fails under an edge-case strengthening. A semantic parse can look correct before paraphrase and drift afterward. A plan can reach the goal although violating a resource or approval dependency.



<table>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th>source x ∈ X</th>
<th>f : X → X′</th>
<th>transformed source f(x) ∈ X′</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>↓ T_0</td>
<td></td>
<td>↓ T_1</td>
</tr>
<tr class="even">
<td>target T_0(x) ∈ Y</td>
<td>g : Y → Y′</td>
<td>transformed target g(T_0(x)) ∈ Y′</td>
</tr>
</tbody>
</table>



Figure. Typed two-path comparison with separate transports T_0 and T_1. The target results are assessed under a declared relation R, which can be directional and need not be an equivalence.

The evaluation condition is:

T_1(f(x)) R g(T_0(x)), with R and its orientation declared for the target environment.

The diagram illustrates two typed paths, not a proof of mathematical functoriality. Let f : X → X′ be a source-side operation, T_0 : X → Y and T_1 : X′ → Y′ be transports, and g : Y → Y′ be a target-side operation. Both paths must be defined and independently valid in Y′ before their outputs are compared under the declared relation R. The comparison procedure distinguishes relation_pass, relation_fail and relation_unknown from invalid items or unavailable paths. The earlier shorthand T(f(x)) ≈ g(T(x)) is explanatory; the operative comparison is T_1(f(x)) R g(T_0(x)).

For stochastic transports, each evaluation item declares its statistical estimand. Under a pathwise estimand, specify a justified joint coupling of both path outputs and estimate the probability of R under that coupling. Shared nominal random seeds alone do not establish a valid coupling. Under a distributional estimand with a measurable deterministic target map g, compare the law of T_1(f(x)) with g_#Law(T_0(x)) using a prespecified metric or test. For a randomized target operation g, use the law induced by its declared transition kernel in place of a deterministic pushforward. Equal marginal laws do not entail pathwise agreement for arbitrary couplings. Report sampling budgets, seeds, dependence assumptions, invalid outputs, missing paths, validator uncertainty, and sampling uncertainty separately. The deterministic square is the point-mass case. Neither evaluation outcome alone establishes the identity or composition laws of a functor.

Commutation establishes agreement only relative to the supplied relation and validator. Constant transports into a single target object, for example, yield commuting squares despite losing source distinctions. An evaluation item must separately record source-to-target adequacy, freeze source and target operations and acceptance criteria before observing model outputs, and test for degeneracy using independently specified controls. A defective benchmark specification is an invalid_item, and a fixture awaiting a decisive eligibility check is an unresolved_item. A generated object decisively failing a local validator is an invalid_candidate, while an inconclusive local check is unresolved_local_validity. Report locally valid-pair coverage, relation-adjudication coverage, conditional relation agreement, relation-pass yield over eligible attempts, and the stricter joint relation-and-independent-adequacy yield. A commuting pair that fails source adequacy contributes to relation-pass yield and fails the joint adequacy criterion. Invalid benchmark items are separately counted and excluded from model-performance denominators.


The comparison relation R and its validator are declared per task. Formal settings distinguish definitional equality, logical equivalence, directional implication, and refinement through their respective proof obligations [\[[1](#ref-LeanRef){.citation-link aria-label="Reference 1 — The Lean Language Reference"}, [2](#ref-TPIL4){.citation-link aria-label="Reference 2 — Theorem Proving in Lean 4"}\]]{.citation-group}. In executable systems, passing a test suite establishes agreement only under the tested specification and coverage. COGS and SLOG provide semantic-parsing tasks with task-specific logical forms and generalization splits [\[[9](#ref-COGS2020){.citation-link aria-label="Reference 9 — COGS: A Compositional Generalization Challenge Based on Semantic Interpretation"}, [10](#ref-SLOG2023){.citation-link aria-label="Reference 10 — SLOG: A Structural Generalization Benchmark for Semantic Parsing"}\]]{.citation-group}. The proposed cross-representation comparison needs an independently specified relation and acceptance procedure. PDDL specifies planning domains with actions, preconditions, and effects [\[[11](#ref-PDDL1998){.citation-link aria-label="Reference 11 — PDDL—The Planning Domain Definition Language, Version 1.2"}\]]{.citation-group}. Any plan or trace comparison must additionally declare its target relation. Expert-reviewed transport records assumptions, uncertainty, and permitted claims. Validator protocols include known-positive and known-negative controls and distinguish unresolved outcomes from rejection.

A benchmark item records eight fields: source environment E_s, target environment E_t, source object x, source transformation f, transport specification T = (T_0, T_1), target transformation g, target-side acceptance relation R, and validator V. Additional fields include typing assumptions, directionality, reference cases, reviewer protocol, failure labels, repair traces and validator uncertainty. The minimal item is:

I = (E_s, E_t, x, f, T, g, R, V).

Here E_s and E_t name the declared source and target environments. The artifact x belongs to a source class X, and f maps X into the transformed source class X′. The transport record T supplies T_0 : X -\> Y and T_1 : X′ -\> Y′. The corresponding target operation g maps Y into Y′. The relation R compares two artifacts in Y′; the validator V implements its declared acceptance procedure with an explicit undetermined outcome for unresolved cases. The representation I denotes one evaluation item.

Lean elaborates surface syntax into core terms and submits declarations to a trusted kernel [\[[1](#ref-LeanRef){.citation-link aria-label="Reference 1 — The Lean Language Reference"}, [2](#ref-TPIL4){.citation-link aria-label="Reference 2 — Theorem Proving in Lean 4"}\]]{.citation-group}. For an informal theorem, Compositional Intelligence proposes a separate test comparing specialization before formalization with specialization of the formalized theorem. The test uses an explicitly declared relation and independent source–target alignment review.

Functorial Consistency differs from ordinary robustness. Robustness often asks whether an output remains stable under perturbation. Functorial Consistency asks whether the output changes in the right way under a typed transformation. Some transformations should preserve meaning. Others should change meaning in controlled ways. A paraphrase can preserve denotation. A specialization should narrow a claim. An edge-case strengthening should add a behavioral condition. A decomposition should preserve recomposability.

Functorial Consistency also differs from self-consistency. Self-consistency compares repeated samples, reasoning paths, or outputs from the same prompt. Functorial Consistency compares two structured paths involving source-side transformation, target translation, and target-side transformation. Agreement is measured between transformed artifacts, not among repeated answers.

Table. Functorial Consistency against adjacent evaluation types.



<table>
<colgroup>
<col style="width: 49%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Evaluation type</strong></th>
<th><strong>Question</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>accuracy</td>
<td>Is the output correct?</td>
</tr>
<tr class="even">
<td>robustness</td>
<td>Is the output stable under perturbation?</td>
</tr>
<tr class="odd">
<td>self-consistency</td>
<td>Do repeated outputs agree?</td>
</tr>
<tr class="even">
<td>compositional generalization</td>
<td>Can the model recombine familiar structures?</td>
</tr>
<tr class="odd">
<td>Functorial Consistency</td>
<td>Does the output transform in the right way across representations?</td>
</tr>
</tbody>
</table>



SCAN, CFQ, COGS and SLOG evaluate forms of systematic recombination [\[[12](#ref-SCAN2018){.citation-link aria-label="Reference 12 — Generalization without Systematicity: On the Compositional Skills of Sequence-to-Sequence Recurrent Networks"}, [13](#ref-CFQ2020){.citation-link aria-label="Reference 13 — Measuring Compositional Generalization: A Comprehensive Method on Realistic Data"}, [9](#ref-COGS2020){.citation-link aria-label="Reference 9 — COGS: A Compositional Generalization Challenge Based on Semantic Interpretation"}, [10](#ref-SLOG2023){.citation-link aria-label="Reference 10 — SLOG: A Structural Generalization Benchmark for Semantic Parsing"}\]]{.citation-group}. FormalBench evaluates specification inference using deductive success/failure/unknown outcomes, mutation-based completeness proxies, transformation robustness, and repair; ConsistencyChecker computes similarity-based consistency scores over paths through reversible-transformation trees [\[[14](#ref-FormalBench2025){.citation-link aria-label="Reference 14 — Can LLMs Reason About Program Semantics? A Comprehensive Evaluation of LLMs on Formal Specification Inference"}, [15](#ref-ConsistencyChecker2025){.citation-link aria-label="Reference 15 — ConsistencyChecker: Tree-based Evaluation of LLM Generalization Capabilities"}\]]{.citation-group}. Metamorphic testing supplies a broader family of transformed-input output-relation tests. Functorial Consistency proposes a typed two-path source-to-target record specifying its acceptance relation, validator evidence and failure attribution. The incremental diagnostic value of that record remains a hypothesis for task-matched comparison with metamorphic and reversible-transformation baselines under equal information and validator budgets.

Useful metrics include local validity, path agreement, type preservation, assumption preservation, generality preservation, constraint integration, repair cost, reviewer agreement, and diagnostic novelty. The failure taxonomy includes object failure, transformation failure, translation failure, target-transformation failure, non-commutation, type drift, assumption loss, generality collapse, overstrengthening, spurious equivalence, validator mismatch, and constraint mention without integration.

The benchmark succeeds only if it reveals failures that local accuracy, ordinary robustness, or ordinary self-consistency miss. If the categorical framing does not improve benchmark design, failure diagnosis, or structure-preservation analysis, it should be reduced to a plain commutation-test framing. The benchmark fails if commutation squares reveal no diagnostic failures beyond local accuracy, robustness, or self-consistency.

## Extensions as Record Disciplines

The first three layers define the core framework: membership, generation, and transformation. The remaining layers show how the same record protocol extends into language composition, architecture choice, quantitative warrant, and effectful action.

Table. Extension schemas and boundaries.



<table>
<colgroup>
<col style="width: 24%"/>
<col style="width: 24%"/>
<col style="width: 25%"/>
<col style="width: 25%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Extension</strong></th>
<th><strong>Core question</strong></th>
<th><strong>Schema</strong></th>
<th><strong>Boundary</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>language</td>
<td>does typed compositional structure improve downstream semantics?</td>
<td>w_i -&gt; tau_i -&gt; pi -&gt; pi</td>
<td>transformers are not claimed to implement Lambek calculus</td>
</tr>
<tr class="even">
<td>architecture</td>
<td>does task structure constrain model-family choice?</td>
<td>A |= S</td>
<td>ArchitectureSpec is untested</td>
</tr>
<tr class="odd">
<td>warrant</td>
<td>do scores predict validation, repair, or reuse?</td>
<td>Gamma ⊢_theta t : A ▷ Q</td>
<td>soft warrant is not proof</td>
</tr>
<tr class="even">
<td>action</td>
<td>do effect records improve control and audit?</td>
<td>Γ; M; E; C ⊢_spec a : Pre → Post ! ε @ ρ</td>
<td>an action is not an answer</td>
</tr>
</tbody>
</table>



### Language

Lambek calculus and categorial type systems supply formal accounts of typed linguistic composition, and supertagging predicts richly structured lexical categories [\[[16](#ref-Lambek1958){.citation-link aria-label="Reference 16 — The Mathematics of Sentence Structure"}, [17](#ref-BangaloreJoshi1999){.citation-link aria-label="Reference 17 — Supertagging: An Approach to Almost Parsing"}\]]{.citation-group}. DisCoCat studies categorical compositional distributional semantics [\[[18](#ref-DisCoCat2010){.citation-link aria-label="Reference 18 — Mathematical Foundations for a Compositional Distributional Model of Meaning"}\]]{.citation-group}. Zhao and Penn evaluate large language models on CCG and Lambek categorial supertagging and report CCG logical-form parsing and LCG parsability results [\[[19](#ref-LLMSupertagger2024){.citation-link aria-label="Reference 19 — LLM-supertagger: Categorial Grammar Supertagging via Large Language Models"}\]]{.citation-group}. That evaluation addresses lexical-category prediction; semantic transformation stability, source--target alignment, and downstream repair are further outcomes requiring separate tests. Lambek Machines proposes to evaluate those outcomes under controlled comparisons.

A Lambek Machine is proposed here as a language system that exposes enough of this typed compositional pipeline for analysis, supervision, constrained generation, or architectural bias. The definition is operational. It does not assert that Transformers literally implement Lambek calculus, that supertagging is semantic understanding, or that symbolic categorial grammar should replace neural language modeling. The decisive test is downstream compositional behavior.

### Architecture

Architecture design solves a matching problem. A task imposes structure. A model family embodies assumptions. The design problem is to align them well enough that the model can learn efficiently, generalize appropriately, preserve relevant invariants, expose useful interfaces, and submit to validation.

The core schema is:

TaskSpec -\> ArchitectureType -\> ArchitectureInstance. The notation A \|= S is reserved for a specified formal satisfaction judgment. Structural support, empirical performance, reviewed fit, runtime cost and implementation constraints receive distinct fields in ArchitectureSpec.

Geometric Deep Learning, Deep Sets, Graph Networks, Transformers, and Mamba address different structural assumptions and architectural mechanisms [\[[20](#ref-GDL2021){.citation-link aria-label="Reference 20 — Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges"}, [21](#ref-DeepSets2017){.citation-link aria-label="Reference 21 — Deep Sets"}, [22](#ref-GraphNetworks2018){.citation-link aria-label="Reference 22 — Relational Inductive Biases, Deep Learning, and Graph Networks"}, [23](#ref-Transformer2017){.citation-link aria-label="Reference 23 — Attention Is All You Need"}, [24](#ref-Mamba2023){.citation-link aria-label="Reference 24 — Mamba: Linear-Time Sequence Modeling with Selective State Spaces"}\]]{.citation-group}. Categorical Deep Learning already proposes an algebraic bridge between constraints and neural architecture implementations [\[[25](#ref-CategoricalDL2024){.citation-link aria-label="Reference 25 — Position: Categorical Deep Learning is an Algebraic Theory of All Architectures"}\]]{.citation-group}. ArchitectureSpec is a separate proposed decision record connecting task transformations, interfaces, resource assumptions, evidence grades, and validators to architecture selection. Its incremental contribution would be established through prospective, information-matched decisions and demonstrable improvement in mismatch diagnosis or validation.

### Warrant

Modern AI systems often operate around exact judgments without producing exact judgments directly. They propose tactics, retrieve premises, rank lemmas, generate proof scripts, draft formal statements, produce code, optimize differentiable constraints, and construct reasoning traces. These objects can be scored before they are checked.

Quantitative Curry-Howard is proposed here as a study of the candidate layer before and around exact validation:

Gamma ⊢\_theta t : A ▷ Q.

Q is a quantitative evidence record. It can include score, probability, uncertainty, loss, margin, calibration status, validation status, diagnostics, repair distance, epistemic type, and permitted use.

End-to-end differentiable proving and Logical Neural Networks investigate trainable or graded reasoning mechanisms [\[[26](#ref-DiffProving2017){.citation-link aria-label="Reference 26 — End-to-End Differentiable Proving"}, [27](#ref-LNN2020){.citation-link aria-label="Reference 27 — Logical Neural Networks"}\]]{.citation-group}. Quasi-Borel spaces provide semantics for higher-order probability [\[[28](#ref-QBS2017){.citation-link aria-label="Reference 28 — A Convenient Category for Higher-Order Probability Theory"}\]]{.citation-group}. A 2026 preprint formalizes selected differentiable and fuzzy logics in Rocq and studies their analytic, algebraic and proof-theoretic properties [\[[29](#ref-DifferentiableLogicsDTT2026){.citation-link aria-label="Reference 29 — A Foundation for Differentiable Logics using Dependent Type Theory"}\]]{.citation-group}. The cited sources support distinct background claims. Quantitative Curry-Howard proposes an evidence record separating search scores, relaxed satisfaction, probabilistic uncertainty, calibration and exact checker acceptance. Its practical contribution remains subject to comparative evaluation of validation, repair, review and authorized use.

### Action

When AI systems act, output-centric evaluation fails more severely since an action changes state. The state can be internal, computational, social, economic, or physical. The correct unit of analysis is the typed, warranted, effectful trace by which an agent moves from instruction to consequence.

The central judgment is:

Γ; M; E; C ⊢\_spec a : Pre → Post ! ε @ ρ.

Here Gamma is instruction and policy context. M is memory. E is environment or interface state. C is capability context. a is an action or plan step. Pre and Post are preconditions and postconditions. epsilon is an effect row. rho records risk, authority, reversibility, and validation obligations.

The typed-action judgment specifies a record of contextual authority, preconditions, postconditions, effect declarations and validator obligations. Operational enforcement additionally uses decision-time checks, capability boundaries, execution guards and post-execution validation. These mechanisms face separate evaluation under delayed tools, concurrent effects, persistent memory and irreversible operations. Record completeness, runtime enforcement and terminal task completion receive independent measurements.

Hoare logic, PDDL, monads, and algebraic effects supply foundational accounts of preconditions, postconditions, planning effects, and computational effects [\[[30](#ref-Hoare1969){.citation-link aria-label="Reference 30 — An Axiomatic Basis for Computer Programming"}, [11](#ref-PDDL1998){.citation-link aria-label="Reference 11 — PDDL—The Planning Domain Definition Language, Version 1.2"}, [31](#ref-Moggi1989){.citation-link aria-label="Reference 31 — Computational Lambda-Calculus and Monads"}, [32](#ref-PlotkinPretnar2013){.citation-link aria-label="Reference 32 — Handling Algebraic Effects"}\]]{.citation-group}. Contemporary agent benchmarks and tool-use systems motivate the need for trajectory-level evaluation across reasoning-action interleaving, tool use, realistic web and computer environments, policy-constrained interactions, prompt-injection settings, and trajectory evaluation [\[[33](#ref-ReAct2022){.citation-link aria-label="Reference 33 — ReAct: Synergizing Reasoning and Acting in Language Models"}, [8](#ref-Toolformer2023){.citation-link aria-label="Reference 8 — Toolformer: Language Models Can Teach Themselves to Use Tools"}, [3](#ref-WebArena2023){.citation-link aria-label="Reference 3 — WebArena: A Realistic Web Environment for Building Autonomous Agents"}, [4](#ref-OSWorld2024){.citation-link aria-label="Reference 4 — OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments"}, [5](#ref-TauBench2025){.citation-link aria-label="Reference 5 — τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains"}, [6](#ref-AgentDojo2024){.citation-link aria-label="Reference 6 — AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents"}, [34](#ref-AgentRewardBench2025){.citation-link aria-label="Reference 34 — AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories"}\]]{.citation-group}. TypedActionLedger is proposed here as an accounting layer around such systems. It succeeds only if it changes execution, repair, review, or audit.

## Benchmarks and Implementation Agenda

Compositional Intelligence has value only if its records turn into benchmarks, validators, and implementation artifacts. The core technical agenda is summarized below.

Table. Artifacts, tests, and failure conditions.



<table>
<colgroup>
<col style="width: 24%"/>
<col style="width: 25%"/>
<col style="width: 24%"/>
<col style="width: 25%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Layer</strong></th>
<th><strong>Artifact</strong></th>
<th><strong>Test</strong></th>
<th><strong>Failure condition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>membership</td>
<td>ArtifactRecord</td>
<td>Does it improve alignment, review, reuse, or repair?</td>
<td>record adds cost without diagnostic value</td>
</tr>
<tr class="even">
<td>generation</td>
<td>Type-First Prompting Harness</td>
<td>Does target-type articulation improve artifacts?</td>
<td>intervention adds verbosity without improvement</td>
</tr>
<tr class="odd">
<td>transformation</td>
<td>Functorial Consistency Bench</td>
<td>Does path agreement reveal hidden failures?</td>
<td>benchmark collapses into ordinary accuracy</td>
</tr>
<tr class="even">
<td>language</td>
<td>Lambek Auxiliary Supervision</td>
<td>Does categorial structure improve downstream semantics?</td>
<td>only supertagging improves</td>
</tr>
<tr class="odd">
<td>architecture</td>
<td>ArchitectureSpec Catalog</td>
<td>Does structure constrain architecture choice?</td>
<td>same architecture recommended everywhere</td>
</tr>
<tr class="even">
<td>warrant</td>
<td>Quantitative Curry-Howard Bench</td>
<td>Do scores predict validation or repair?</td>
<td>scores fail to improve calibration or repair</td>
</tr>
<tr class="odd">
<td>action</td>
<td>Typed Action Ledger</td>
<td>Do effect records improve control or audit?</td>
<td>ledger turns into inert documentation</td>
</tr>
</tbody>
</table>



A first Type-First Prompting pilot should use 100-150 curated items across code, Lean or mathematics, explanation, scientific protocol design, and planning. It should measure target-type accuracy, constraint recall, inhabitant validity, semantic alignment, repair cost, type stability, downstream usability, and ambiguity handling.

A first Functorial Consistency pilot should use 80-120 commutation-square items across informal mathematics to Lean, requirements to code, language to semantic parse, and goals to plans. The first version should prioritize exact, executable, and denotational equivalence regimes before relying heavily on reviewed alignment. The primary question is whether path agreement reveals failures missed by local validity.

A first Lambek pilot should use two or three dataset families: a categorial resource for supertagging and derivational evaluation, a semantic parsing dataset or controlled semantic examples, and hand-curated transformation squares. The primary question is whether categorial structure improves downstream semantic behavior, not merely category prediction.

A first ArchitectureSpec catalog should contain 20-30 task-family records with candidate architecture families, excluded families, structural commitments, validators, and predicted failure modes. Candidate task families include sets, graphs, molecules, long-context sequences, proof states, scientific protocols, and agent workflows.

A first Quantitative Curry-Howard pilot should collect candidate artifacts with scores, validation outcomes, repair traces, and calibration records. The initial domains can include Lean proof search, code synthesis, soft constraints, probabilistic scientific claims, and reasoning-trace verification where appropriate.

A first Effectful Agent pilot should annotate existing web or tool-use tasks with preconditions, postconditions, effects, authority, side-effect labels, memory updates, rollback requirements, and audit traces. Evaluation should include unauthorized action rate, side-effect control, data isolation, memory pollution, rollback quality, and audit completeness.

The minimum viable repository should contain four components: JSON Schemas for the records, a small seed dataset for each benchmark family, validator interfaces for each equivalence regime, and diagnostic scripts that produce failure labels instead of only aggregate scores. The first repository should prioritize data schemas and diagnostic scripts before model training.

## Related Work and Source Boundaries

Compositional Intelligence is built from existing technical traditions, but its core artifacts are original proposals. Formal verification and proof assistants supply validation mechanisms; they do not by themselves establish source-target alignment or downstream semantic membership [\[[1](#ref-LeanRef){.citation-link aria-label="Reference 1 — The Lean Language Reference"}, [2](#ref-TPIL4){.citation-link aria-label="Reference 2 — Theorem Proving in Lean 4"}, [7](#ref-LeanDojo2023){.citation-link aria-label="Reference 7 — LeanDojo: Theorem Proving with Retrieval-Augmented Language Models"}\]]{.citation-group}. Proof-assistant infrastructure and tool-use systems supply examples of typed or interface-constrained construction; they do not settle target-type inference for open-ended natural-language tasks [\[[1](#ref-LeanRef){.citation-link aria-label="Reference 1 — The Lean Language Reference"}, [2](#ref-TPIL4){.citation-link aria-label="Reference 2 — Theorem Proving in Lean 4"}, [7](#ref-LeanDojo2023){.citation-link aria-label="Reference 7 — LeanDojo: Theorem Proving with Retrieval-Augmented Language Models"}, [8](#ref-Toolformer2023){.citation-link aria-label="Reference 8 — Toolformer: Language Models Can Teach Themselves to Use Tools"}\]]{.citation-group}.

Compositional-generalization benchmarks investigate systematic generalization under constructed task distributions [\[[12](#ref-SCAN2018){.citation-link aria-label="Reference 12 — Generalization without Systematicity: On the Compositional Skills of Sequence-to-Sequence Recurrent Networks"}, [13](#ref-CFQ2020){.citation-link aria-label="Reference 13 — Measuring Compositional Generalization: A Comprehensive Method on Realistic Data"}, [9](#ref-COGS2020){.citation-link aria-label="Reference 9 — COGS: A Compositional Generalization Challenge Based on Semantic Interpretation"}, [10](#ref-SLOG2023){.citation-link aria-label="Reference 10 — SLOG: A Structural Generalization Benchmark for Semantic Parsing"}\]]{.citation-group}. FormalBench evaluates specification consistency, mutation-based completeness proxies, and transformation robustness with an explicit unknown verdict; ConsistencyChecker uses path- and tree-level similarity scores for reversible transformations [\[[14](#ref-FormalBench2025){.citation-link aria-label="Reference 14 — Can LLMs Reason About Program Semantics? A Comprehensive Evaluation of LLMs on Formal Specification Inference"}, [15](#ref-ConsistencyChecker2025){.citation-link aria-label="Reference 15 — ConsistencyChecker: Tree-based Evaluation of LLM Generalization Capabilities"}\]]{.citation-group}. The proposed Functorial Consistency item specifies two typed paths and an acceptance procedure. Its incremental diagnostic advantage is an open empirical question.

Lambek calculus, categorial type systems, and DisCoCat supply prior accounts of typed or compositional linguistic interpretation [\[[16](#ref-Lambek1958){.citation-link aria-label="Reference 16 — The Mathematics of Sentence Structure"}, [17](#ref-BangaloreJoshi1999){.citation-link aria-label="Reference 17 — Supertagging: An Approach to Almost Parsing"}, [18](#ref-DisCoCat2010){.citation-link aria-label="Reference 18 — Mathematical Foundations for a Compositional Distributional Model of Meaning"}\]]{.citation-group}. Zhao and Penn report lexical-category prediction together with CCG logical-form parsing and LCG parsability outcomes; broader tests of semantic transformation stability, source–target alignment, and repair remain separate research objectives [\[[19](#ref-LLMSupertagger2024){.citation-link aria-label="Reference 19 — LLM-supertagger: Categorial Grammar Supertagging via Large Language Models"}\]]{.citation-group}. Lambek Machines proposes that assessment through explicit task and comparator specifications.

Architecture research supplies structural priors across geometric, set, graph, attention-based, and state-space models [\[[20](#ref-GDL2021){.citation-link aria-label="Reference 20 — Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges"}, [21](#ref-DeepSets2017){.citation-link aria-label="Reference 21 — Deep Sets"}, [22](#ref-GraphNetworks2018){.citation-link aria-label="Reference 22 — Relational Inductive Biases, Deep Learning, and Graph Networks"}, [23](#ref-Transformer2017){.citation-link aria-label="Reference 23 — Attention Is All You Need"}, [24](#ref-Mamba2023){.citation-link aria-label="Reference 24 — Mamba: Linear-Time Sequence Modeling with Selective State Spaces"}\]]{.citation-group}. Categorical Deep Learning also connects architectural constraints and implementations [\[[25](#ref-CategoricalDL2024){.citation-link aria-label="Reference 25 — Position: Categorical Deep Learning is an Algebraic Theory of All Architectures"}\]]{.citation-group}. ArchitectureSpec proposes a task-level decision record; its ability to improve architectural choices or failure prediction is an empirical question.

Differentiable proving and Logical Neural Networks provide forms of trainable or graded reasoning [\[[26](#ref-DiffProving2017){.citation-link aria-label="Reference 26 — End-to-End Differentiable Proving"}, [27](#ref-LNN2020){.citation-link aria-label="Reference 27 — Logical Neural Networks"}\]]{.citation-group}. Quasi-Borel spaces supply semantic foundations for higher-order probability [\[[28](#ref-QBS2017){.citation-link aria-label="Reference 28 — A Convenient Category for Higher-Order Probability Theory"}\]]{.citation-group}, and a 2026 Rocq preprint formalizes selected fuzzy and differentiable logics [\[[29](#ref-DifferentiableLogicsDTT2026){.citation-link aria-label="Reference 29 — A Foundation for Differentiable Logics using Dependent Type Theory"}\]]{.citation-group}. Quantitative Curry--Howard proposes evidence records for candidate-artifact scores, uncertainty, validation, and calibration. Calibration of learned-model warrant is a separate empirical obligation.

Hoare logic, PDDL, monadic semantics, and algebraic effects address program assertions, planning action models, and computational effects [\[[30](#ref-Hoare1969){.citation-link aria-label="Reference 30 — An Axiomatic Basis for Computer Programming"}, [11](#ref-PDDL1998){.citation-link aria-label="Reference 11 — PDDL—The Planning Domain Definition Language, Version 1.2"}, [31](#ref-Moggi1989){.citation-link aria-label="Reference 31 — Computational Lambda-Calculus and Monads"}, [32](#ref-PlotkinPretnar2013){.citation-link aria-label="Reference 32 — Handling Algebraic Effects"}\]]{.citation-group}. Agent and tool-use studies evaluate reasoning-action interactions, tool use, web and desktop trajectories, policy-sensitive interaction, prompt-injection defenses, or trajectory judgments [\[[33](#ref-ReAct2022){.citation-link aria-label="Reference 33 — ReAct: Synergizing Reasoning and Acting in Language Models"}, [8](#ref-Toolformer2023){.citation-link aria-label="Reference 8 — Toolformer: Language Models Can Teach Themselves to Use Tools"}, [3](#ref-WebArena2023){.citation-link aria-label="Reference 3 — WebArena: A Realistic Web Environment for Building Autonomous Agents"}, [4](#ref-OSWorld2024){.citation-link aria-label="Reference 4 — OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments"}, [5](#ref-TauBench2025){.citation-link aria-label="Reference 5 — τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains"}, [6](#ref-AgentDojo2024){.citation-link aria-label="Reference 6 — AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents"}, [34](#ref-AgentRewardBench2025){.citation-link aria-label="Reference 34 — AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories"}\]]{.citation-group}. TypedActionLedger proposes separate execution-time control and audit records; its contribution depends on observed improvements in authorization, effect control, repair, or reviewer decisions.

The paper uses citations source-functionally. Each source supports a specific background, system, benchmark, or contrast claim. No cited source is used to validate the original Compositional Intelligence artifacts.

## Limitations and Falsification

Compositional Intelligence has a broad scope, and breadth creates the primary methodological risk. A framework spanning proof assistants, code, science, language, architecture, quantitative warrant, and agent action can degrade into vocabulary absent operational consequences. The response is to require records, validators, benchmarks, and kill criteria.

The main limitations are the following.

6.  The framework can turn into too broad to constrain annotation, evaluation, or design.

7.  Domains differ sharply in formalization level.

8.  Human equivalence judgments can be noisy.

9.  Record schemas can turn into expensive metadata.

10. Type annotations can fail to predict model errors.

11. Functorial Consistency can add little beyond local accuracy.

12. ArchitectureSpec can fail to improve architecture choice.

13. TypedActionLedger can fail to influence execution or repair.

14. The framework can overfit to domains where artifacts are already structured and underperform in open-ended interpretive tasks.

The first empirical phase should therefore focus on domains with explicit validators before expanding to interpretive settings. Proof assistants, code, semantic parsing, planning, and tool-use workflows are better initial domains than open-ended conversation, cultural interpretation, or unconstrained creative tasks. The program can later expand only where its records produce measurable diagnostic value.

Human equivalence judgments should be used carefully. Reviewed alignment should enter where formal, executable, or denotational checks are unavailable or incomplete. It should be recorded as reviewed alignment, not hidden behind mathematical notation. The symbol ≈ is never enough by itself.

Record schemas can turn into expensive metadata. This risk is material. An ArtifactRecord, QuantitativeJudgmentRecord, or TypedActionLedgerEntry matters only when it changes diagnosis, review, repair, reuse, authorization, or audit. If record fields are filled after the fact and never used to guide system behavior or human decisions, they should be simplified or removed.

The framework should be revised if its records do not improve validation, alignment, diagnosis, repair, reuse, architecture choice, calibration, or effect control. It should be narrowed if its schemas fail outside proof assistants, code, semantic parsing, and agent workflows. It should be simplified if its mathematical vocabulary does not improve annotation, evaluation, or system design.

The credible version of the program is empirical.

The kill criteria are explicit and operational.

15. Artifact records do not improve review, repair, or reuse.

16. Target-type annotations do not predict or classify failures.

17. Functorial Consistency adds no diagnostic signal beyond ordinary accuracy.

18. Categorial supervision does not improve downstream compositional behavior.

19. ArchitectureSpec cannot rule out unsuitable architectures.

20. Quantitative records do not predict validation, repair, or calibration.

21. Typed action ledgers do not reduce unauthorized actions, side effects, repair cost, or audit failures.

These criteria expose the proposal to empirical rejection, which is part of the contribution.

## Conclusion

Compositional Intelligence reframes generative AI evaluation around typed artifacts and the structured worlds those artifacts enter. The path from output to knowledge requires target-type inference, candidate construction, transformation preservation, validation, warrant, reuse, and effect control. This paper has presented a compact framework for that path and a set of records and benchmarks that could refute or refine it.

The framework succeeds only if it makes AI artifacts more checkable, composable, repairable, reusable, calibrated, and accountable. Its ambition is matched by a concrete test. If the records do not change validation, repair, review, architecture choice, or action control, they should be revised or removed. If they do, Compositional Intelligence offers a practical route from fluent output to structured participation.

## Appendix materials from the synthesis paper

## Claim Levels and Epistemic Types

### Claim levels



<table>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Level</strong></th>
<th><strong>Meaning</strong></th>
<th><strong>Publication treatment</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>L0</td>
<td>formal or established background</td>
<td>cite where nontrivial</td>
</tr>
<tr class="even">
<td>L1</td>
<td>source-supported empirical or system claim</td>
<td>cite directly</td>
</tr>
<tr class="odd">
<td>L2</td>
<td>interpretive synthesis</td>
<td>anchor in multiple sources</td>
</tr>
<tr class="even">
<td>L3</td>
<td>original proposal</td>
<td>mark as proposed here</td>
</tr>
<tr class="odd">
<td>L4</td>
<td>testable hypothesis</td>
<td>mark as unproven until benchmarked</td>
</tr>
</tbody>
</table>



### Epistemic types



<table>
<colgroup>
<col style="width: 49%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Type</strong></th>
<th><strong>Meaning</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>proved</td>
<td>established by proof in a specified formal or mathematical setting</td>
</tr>
<tr class="even">
<td>formally validated</td>
<td>accepted by checker, type checker, schema validator, or model checker</td>
</tr>
<tr class="odd">
<td>executable validated</td>
<td>validated by execution, tests, simulation checks, or runtime behavior</td>
</tr>
<tr class="even">
<td>empirically supported</td>
<td>supported by measurement or experiment</td>
</tr>
<tr class="odd">
<td>simulation derived</td>
<td>derived from simulation under model assumptions</td>
</tr>
<tr class="even">
<td>probabilistic</td>
<td>supported by posterior, likelihood, calibrated probability, or probabilistic model</td>
</tr>
<tr class="odd">
<td>model relative</td>
<td>true or warranted relative to specified model assumptions</td>
</tr>
<tr class="even">
<td>approximate</td>
<td>valid within stated tolerance or approximation</td>
</tr>
<tr class="odd">
<td>benchmark supported</td>
<td>supported by benchmark performance under conditions</td>
</tr>
<tr class="even">
<td>reviewed</td>
<td>assessed by human, automated, or hybrid review</td>
</tr>
<tr class="odd">
<td>conjectural</td>
<td>plausible but unproved or unvalidated</td>
</tr>
<tr class="even">
<td>unvalidated</td>
<td>generated but unchecked</td>
</tr>
<tr class="odd">
<td>refuted</td>
<td>rejected by proof, checker, counterexample, failed validation, or review</td>
</tr>
</tbody>
</table>



## Minimal Schema Summaries

### ArtifactRecord

artifact_record:

id: string

kind: string

content: string \| object

target_environment: string

dependencies: list\[string\]

assumptions: list\[string\]

validation_status: string

epistemic_type: string

alignment_status: string

permitted_use: list\[string\]

repair_path: string \| null

### TargetTypeRecord

target_type_record:

task_id: string

prompt: string

context: string

candidate_target_types: list\[string\]

selected_target_type: string

constraints: list\[string\]

invalid_target_types: list\[string\]

validation_method: string

### FunctorialConsistencyItem

functorial_consistency_item:

id: string

source_environment: string

target_environment: string

source_object: string

source_transformation: string

translation: string

target_transformation: string

equivalence_regime: string

validator: string

failure_labels: list\[string\]

### ArchitectureSpec

architecture_spec:

id: string

task_family: string

object_types: list\[string\]

transformations: list\[string\]

laws: list\[string\]

operations: list\[string\]

interfaces: list\[string\]

effects: list\[string\]

validators: list\[string\]

candidate_architectures: list\[string\]

excluded_architectures: list\[string\]

predicted_failure_modes: list\[string\]

### QuantitativeJudgmentRecord

quantitative_judgment:

artifact_id: string

context: string

target: string

candidate: string

model: string

score: string \| number \| null

probability: number \| null

uncertainty: string \| null

calibration_status: string

validation_status: string

diagnostics: string

repair_distance: string \| null

epistemic_type: string

permitted_use: list\[string\]

### TypedActionLedgerEntry

typed_action_ledger_entry:

entry_id: string

action_type: string

instruction_sources: list\[string\]

observation_sources: list\[string\]

preconditions: list\[string\]

postconditions: list\[string\]

declared_effects: list\[string\]

authority_source: string

capabilities_required: list\[string\]

handler: string

authorization_result: string

execution_result: string

observed_state_delta: string

frame_conditions:

may_modify: list\[string\]

must_preserve: list\[string\]

validation_result: string

repair_or_rollback: string \| null

permitted_downstream_use: list\[string\]

### ConceptTransferRecord

concept_transfer_record:

id: string

source_domain: string

target_domain: string

preserved_relations: list\[string\]

lost_relations: list\[string\]

counterexamples: list\[string\]

distortion_risk: string

permitted_use: list\[string\]

forbidden_use: list\[string\]

## Source-Use Warnings

-   The Lean Language Reference and Theorem Proving in Lean 4 support Lean and dependent-type-theory claims. They do not establish semantic participation.

-   LeanDojo supports programmatic interaction, proof-data extraction, and theorem-proving infrastructure around Lean. It does not establish semantic participation.

-   SCAN, CFQ, COGS, and SLOG support compositional-generalization context. They do not establish Functorial Consistency.

-   FormalBench and ConsistencyChecker support transformation-sensitive evaluation context. They do not establish the commutation-square benchmark proposed here.

-   Lambek\'s sentence-structure calculus, Bangalore and Joshi\'s supertagging work, DisCoCat, and LLM-Supertagger support language-composition context. They do not establish that Transformers implement Lambek calculus.

-   Geometric Deep Learning, Deep Sets, Graph Networks, Transformers, Mamba, and Categorical Deep Learning support architecture context. They do not validate ArchitectureSpec.

-   End-to-end differentiable proving, Logical Neural Networks, quasi-Borel spaces, and recent differentiable-logics work support quantitative-warrant context. They do not make soft scores into proof.

-   Hoare logic, PDDL, Moggi\'s monadic semantics, and algebraic-effects work support preconditions, planning, monads, and effects. They do not establish TypedActionLedger.

-   ReAct, Toolformer, WebArena, OSWorld, tau-bench, AgentDojo, and AgentRewardBench support tool-use and agent-evaluation context. They do not validate effect-control claims.
