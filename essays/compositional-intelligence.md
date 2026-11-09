# Compositional Intelligence

*Mateo Petel*

<!-- AUTHORITATIVE-DOCX SHA256 0c64bcec2fc3127d1b0f5dcd45509b512e8ec5de77438c5cd780d3daa7fe176b; source Compositional_Intelligence_Book_Manuscript_V3(1).docx -->

<h2 id="abstract">Abstract</h2>
<p>Generative AI is often evaluated through output quality, benchmark performance, and local task performance. Those measures register useful capability, although they leave under-specified the condition that matters for cumulative knowledge and agentic deployment. A generated object has standing when a structured world can check it, align it with an intended source, compose it with existing objects, reuse it under declared conditions, warrant it at an appropriate epistemic level, or authorize action under controlled effects.</p>
<p>This paper introduces Compositional Intelligence, a proposed research program for typed artifacts in structured worlds. The framework has three central components. Semantic participation defines artifact membership through validation, alignment, composability, epistemic status, and permitted use. Typed generativity models generation as target-type inference followed by probabilistic construction of candidate inhabitants. Functorial Consistency evaluates whether transformations commute across source and target representations under explicit equivalence regimes.</p>
<p>The paper then compresses three supporting layers. Architecture specification treats model families as structural commitments about objects, transformations, symmetries, interfaces, and validators. Quantitative Curry-Howard attaches evidence records to candidate typed artifacts and preserves the boundary between soft warrant and proof. Typed action ledgers record preconditions, postconditions, effects, authority, handlers, validators, and audit traces for agentic systems.</p>
<p>The proposal is falsifiable. Its schemas and benchmarks matter only if they improve diagnosis, validation, repair, reuse, architecture choice, calibration, or effect control.</p>
<h2 id="introduction">Introduction</h2>
<p>A generated proof sketch, code patch, theorem formalization, scientific protocol, plan, or tool call has value when it can enter an environment that supplies validation, integration, repair, rejection, and permitted use. Benchmark accuracy and task completion remain useful measurement instruments, since they make capability comparable. They remain insufficient for artifacts that must enter cumulative technical systems, where surface plausibility gives limited information about alignment, dependency preservation, future reuse, or action authority.</p>
<p>The output-artifact distinction is clearest in structured environments. A proof assistant checks a formal proof relative to a formal statement, and source-target alignment remains a separate obligation. A code patch can satisfy visible tests and still violate an interface, invariant, or dependency relation. A scientific protocol can appear coherent and omit controls, uncertainty, stopping conditions, or the claim type it can support. An agent can reach a target state through tool calls, web or computer interaction, memory updates, delegated authority, or exposure to untrusted instructions. Compositional Intelligence treats those trajectories as effectful traces requiring authority, memory, validation, and side-effect records.</p>
<p>Compositional Intelligence evaluates generative AI as the construction, transformation, validation, warranting, and execution of typed artifacts inside structured worlds. A typed artifact is an attempted object under constraints, including a proof, program, theorem statement, semantic parse, experimental protocol, plan, explanation, database query, memory write, tool call, or skill. A structured world is an environment in which such objects have dependencies, validators, admissible transformations, review practices, epistemic statuses, and permitted uses.</p>
<p>The framework has different uses across research communities. Evaluation researchers can convert structure-preservation failures into benchmark items. Formal-methods researchers can separate checker validity from source-target alignment and downstream semantic use. Agent researchers can distinguish target state success from acceptable state-changing traces. AI-for-science researchers can treat protocols, claims, and experimental plans as artifacts whose assumptions, warrant, and permitted uses require explicit representation.</p>
<p>The core technical test is structure preservation across transformations. If a source object is transformed before translation, and the translated object is transformed afterward, the two paths must agree under a declared equivalence regime. The commutation test turns the framework into an evaluation unit, drawing on compositional-generalization and transformation-sensitive evaluation and adding a benchmark record centered on source path, target path, validator, and failure label.</p>
<p>The unit of analysis is the typed artifact with a record. The record states the attempted object kind, assumptions, dependencies, validation status, transformation behavior, warrant type, permitted downstream uses, and possible effects. The framework does not impose a single formal machinery across domains; it requires each domain to declare its validation regime and epistemic type.</p>
<p>This paper contributes five objects and principles.</p>
<ol type="1">
<li><p>It defines a membership criterion for AI-generated artifacts, called semantic participation.</p></li>
<li><p>It introduces a typed-generativity schema for target-type inference and candidate construction.</p></li>
<li><p>It proposes Functorial Consistency as a commutation-square evaluation principle and the paper's central benchmark object.</p></li>
<li><p>It compresses architecture, warrant, and effectful action into a compact record protocol.</p></li>
<li><p>It states a falsifiable benchmark agenda for testing whether these records improve diagnosis, validation, repair, reuse, architecture choice, calibration, or effect control.</p></li>
</ol>
<p>The paper's claim protocol is explicit. The cited literatures support background formalisms, systems, and benchmarks. The schemas and benchmark objects introduced as Compositional Intelligence artifacts are original proposals. Their practical value remains an empirical question.</p>
<h2 id="from-outputs-to-artifacts">From Outputs to Artifacts</h2>
<p>Output-centric evaluation asks whether an answer is fluent, persuasive, benchmark-correct, or locally successful. That grammar is adequate when the task boundary is narrow and the output is the final object of interest. It weakens when generated objects must enter cumulative technical environments.</p>
<p>A membership-centric grammar asks whether a generated object can occupy a stable position inside a structured world. The artifact must be expressible in the environment, validated by available checkers or review procedures, aligned with its source intention, composable with existing objects, and usable in later reasoning under stated conditions. Progress is measured by an artifact with a record, dependencies, warrant, permitted uses, and an integration pathway.</p>
<p>Three recurring failures motivate the shift.</p>
<p>Table. Output failures and missing artifact conditions.</p>
<p class="table-display-caption" id="table-1-caption">Table. Output failures and missing artifact conditions.</p>
<div aria-labelledby="table-1-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="1" id="table-1"><caption class="visually-hidden">Table. Output failures and missing artifact conditions.</caption>
<colgroup>
<col style="width: 29%"/>
<col style="width: 29%"/>
<col style="width: 41%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Domain</strong></th>
<th scope="col"><strong>Local success</strong></th>
<th scope="col"><strong>Missing artifact condition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>formalization</td>
<td>proof artifact checks</td>
<td>source-target alignment (LeanRef,TPIL4)</td>
</tr>
<tr class="even">
<td>code</td>
<td>tests pass under the visible test regime</td>
<td>interface and invariant preservation</td>
</tr>
<tr class="odd">
<td>agents</td>
<td>target state reached</td>
<td>authority and effect trace (WebArena2023,OSWorld2024,TauBench2025,AgentDojo2024)</td>
</tr>
</tbody>
</table></div>
<p>These failures differ operationally, but they share a record problem. The evaluator cannot tell what kind of object was produced, what it preserves, what warrants it, and what it is allowed to affect.</p>
<p><strong>output -&gt; candidate artifact -&gt; typed candidate -&gt; transformed artifact<br/>
</strong>-&gt; validated artifact -&gt; warranted artifact -&gt; reusable artifact -&gt; effectful action</p>
<p>Figure. From output to artifact. The lifecycle is conceptual instead of strictly linear; its purpose is to expose the status of generated objects as they enter structured worlds.</p>
<p>This lifecycle is neither strictly linear nor universal. Some artifacts never receive formal validation. Some are reviewed. Some remain conjectural. Some are useful as heuristics. Some should be rejected. The relevant condition is that the artifact's status should be explicit.</p>
<p>A generated theorem statement, proof script, function, protocol, semantic parse, plan, or tool call should therefore include enough structure for the target environment to judge it. The record need not be long. It should answer the questions that determine whether the object can participate: what kind of object it is, what environment it targets, what constraints it must satisfy, what validates it, what it preserves, what remains uncertain, and what uses are allowed.</p>
<h2 id="semantic-participation">Semantic Participation</h2>
<p>Semantic participation is the capacity of an AI system to place artifacts inside a semantic environment with recorded validation, alignment, compositional role, epistemic status, and permitted use. It is the membership criterion proposed in this paper.</p>
<p>A semantic environment is a structured world with objects, validators, dependencies, admissible operations, memory, review practices, and reuse conditions. Proof assistants, codebases, scientific workflows, laboratory systems, semantic parsers, research-object repositories, design catalogs, and agent runtimes are all possible semantic environments. They differ in validation strength, but they share the membership problem. Lean provides a concrete example of formal validation through dependent type theory and proof checking (LeanRef,TPIL4). LeanDojo adds programmatic interaction, proof-data extraction, and retrieval-augmented theorem-proving infrastructure around Lean (LeanDojo2023).</p>
<p>An artifact semantically participates in an environment when it is expressible there, checkable or reviewable there, aligned with its intended source, composable with relevant objects, and assigned an epistemic type that constrains downstream use.</p>
<p>The central distinction is among thresholds that are often collapsed. Fluency shows that a model can produce acceptable surface form. Task success shows that a system can meet an evaluation condition. Formal validity shows that a formal checker accepts a statement or derivation (LeanRef,TPIL4). Source-target alignment shows that the artifact preserves the intended source meaning. Epistemic utility shows that the artifact can be used responsibly in later reasoning. Semantic participation requires these thresholds to be recorded together.</p>
<p>Table. Semantic participation thresholds.</p>
<p class="table-display-caption" id="table-2-caption">Table. Semantic participation thresholds.</p>
<div aria-labelledby="table-2-caption" class="table-scroll" data-columns="4" role="group" tabindex="0"><table data-source-table="2" id="table-2"><caption class="visually-hidden">Table. Semantic participation thresholds.</caption>
<colgroup>
<col style="width: 25%"/>
<col style="width: 24%"/>
<col style="width: 25%"/>
<col style="width: 24%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Threshold</strong></th>
<th scope="col"><strong>What it establishes</strong></th>
<th scope="col"><strong>What it leaves open</strong></th>
<th scope="col"><strong>Record needed</strong></th>
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
</table></div>
<p>Semantic participation depends on existing validation machinery without collapsing into it. Proof assistants supply environments where formal derivations can be checked; Semantic Participation adds the membership criterion linking validation, alignment, composability, epistemic type, and permitted use (LeanRef,TPIL4).</p>
<p>The proposed ArtifactRecord makes this membership question inspectable. A minimal record includes target environment, dependencies, assumptions, validation status, epistemic type, alignment status, permitted use, and repair path. The record is useful only if it changes what reviewers, validators, users, or downstream systems can do. It should expose hidden assumptions, wrong target claims, weak warrant, dependency problems, poor library fit, unsupported reuse, or failure to preserve meaning across transport. If it simply adds documentation without improving diagnosis or reuse, it fails.</p>
<p>Semantic participation is therefore an original proposal in the series. It does not claim to invent proof checking, provenance, formal verification, or research-object packaging. It proposes that AI reasoning should be evaluated by artifact membership in structured semantic environments, where validity, source-target alignment, epistemic status, compositional role, and downstream reuse are recorded together.</p>
<h2 id="typed-generativity">Typed Generativity</h2>
<p>Typed generativity models generation as target-type inference followed by candidate-inhabitant construction:</p>
<p>P_theta(t : A | Gamma).</p>
<p>Here Gamma is the context available to the model: prompt, prior conversation, retrieved material, examples, tool state, memory, assumptions, and environment. A is the inferred target type or target object class. t is the candidate inhabitant, which can be a proof, program, plan, explanation, protocol, semantic parse, or other artifact. P_theta is the model's distribution over candidate inhabitants under context.</p>
<p>A prompt rarely requests tokens alone. It induces a target object. In a proof-assistant setting, A can be a theorem statement and t a proof term or tactic script (LeanRef,TPIL4,LeanDojo2023). In a tool-use setting, our abstraction treats A as an action schema and t as a candidate call with arguments, with tool-use work providing the motivating context (Toolformer2023). In a scientific setting, A can be a protocol type and t a candidate procedure. In an explanation setting, A can be an audience-specific explanatory artifact and t a candidate explanation with scope, assumptions, and warrant.</p>
<p>The schema provides an abstraction. It does not claim that current language models literally implement dependent type theory. It distinguishes the object layer from the token substrate. Source code is a string, but it is evaluated as a program. A Lean script is text, but it elaborates into formal objects (LeanRef,TPIL4). A structured data response is text, but it is consumed as a typed object by downstream software. A scientific protocol is text, but it encodes actions, controls, measurements, stopping conditions, analysis plans, and permitted claims. Typed generativity studies this object layer.</p>
<p>Table. Levels of typed generation.</p>
<p class="table-display-caption" id="table-3-caption">Table. Levels of typed generation.</p>
<div aria-labelledby="table-3-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="3" id="table-3"><caption class="visually-hidden">Table. Levels of typed generation.</caption>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Level</strong></th>
<th scope="col"><strong>Meaning</strong></th>
<th scope="col"><strong>Status</strong></th>
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
</table></div>
<p>Typed output is visible in proof assistants, and tool-use work shows a related interface layer in which model outputs are consumed as calls to external tools (LeanRef,TPIL4,Toolformer2023). Typed latent cognition remains a hypothesis about internal representations. The paper does not require it. The operational framework requires only that outputs and decoding constraints can be evaluated against target types.</p>
<p>Table. Typed-generativity failure taxonomy.</p>
<p class="table-display-caption" id="table-4-caption">Table. Typed-generativity failure taxonomy.</p>
<div aria-labelledby="table-4-caption" class="table-scroll" data-columns="2" role="group" tabindex="0"><table data-source-table="4" id="table-4"><caption class="visually-hidden">Table. Typed-generativity failure taxonomy.</caption>
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Failure</strong></th>
<th scope="col"><strong>Meaning</strong></th>
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
</table></div>
<p>These failures require different interventions. A wrong target type calls for better disambiguation. An invalid inhabitant calls for checking and repair. A valid non-participating artifact calls for source-target alignment, dependency analysis, or permitted-use constraints.</p>
<p>The Type-First Prompting Harness proposed below tests whether explicit target-type articulation improves artifact construction across code, Lean or mathematics, explanation, scientific protocol design, and planning. It is a test of the typed-generativity hypothesis. If explicit target-type articulation merely adds verbosity, the intervention should be rejected. The diagnostic framework can remain useful, but the practical method would need revision.</p>
<h2 id="functorial-consistency">Functorial Consistency</h2>
<p>Functorial Consistency is the paper's central evaluation proposal. It tests whether an AI system preserves task-relevant structure across transformations. The idea is that a source object can be transformed before translation, or translated before the corresponding target-side transformation. A structure-preserving system should make these two paths agree under a specified equivalence regime.</p>
<p>The claim is diagnostic. Local correctness is too weak. A model can produce a plausible theorem, working program, valid semantic parse, or reasonable plan and still fails to preserve the relation that gives the artifact its meaning. A theorem can be valid in isolation although losing generality under formalization. A program can pass tests and still fails under an edge-case strengthening. A semantic parse can look correct before paraphrase and drift afterward. A plan can reach the goal although violating a resource or approval dependency.</p>
<p class="table-display-caption" id="table-5-caption">Table 5. source object x, -- f --&gt;, transformed source f(x)</p>
<div aria-labelledby="table-5-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="5" id="table-5"><caption class="visually-hidden">Table 5. source object x, -- f --&gt;, transformed source f(x)</caption>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>source object x</strong></th>
<th scope="col"><strong>-- f --&gt;</strong></th>
<th scope="col"><strong>transformed source f(x)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>| T</td>
<td></td>
<td>| T</td>
</tr>
<tr class="even">
<td>target object T(x)</td>
<td>-- g --&gt;</td>
<td>transformed target g(T(x))</td>
</tr>
</tbody>
</table></div>
<p>Figure. Functorial Consistency square. The benchmark compares transform-then-translate with translate-then-transform under a stated equivalence regime.</p>
<p>The evaluation condition is:</p>
<p>T(f(x)) ≈ g(T(x)).</p>
<p>The categorical language is useful only insofar as it clarifies the benchmark object: two paths, a source-side transformation, a target-side transformation, and an equivalence regime.</p>
<p>The symbol ≈ is a placeholder that must be instantiated in each domain. In a proof assistant, the equivalence regime can use formal relations available in the target environment, such as definitional equality, theorem equivalence, or implication (LeanRef,TPIL4). When the source object is informal, an additional reviewed-alignment layer can be required. In code, the equivalence regime can use behavioral equivalence under tests or specifications. In semantic parsing, depending on the task representation, it can mean logical equivalence, denotational equivalence, graph isomorphism, or query-result equivalence (COGS2020,SLOG2023). In planning, it can mean satisfying the same goal, precondition, and effect constraints (PDDL1998). In scientific evidence transport, it can require expert review of assumptions, uncertainty, evidential status, and permitted use.</p>
<p>A benchmark item records at least eight fields: source environment, target environment, source object, source transformation, translation, target transformation, equivalence regime, and validator. A richer item also records failure labels, reviewer protocol, repair trace, and diagnostics. The benchmark item can be summarized as:</p>
<p>S = (E_s, E_t, x, f, T, g, epsilon).</p>
<p>Here E_s is the source environment. E_t is the target environment. x is the source object. f is the source-side transformation. T is the translation or semantic transport from source to target. g is the target-side transformation corresponding to f. epsilon is the equivalence, alignment, or acceptance criterion.</p>
<p>A simple example comes from informal mathematics to Lean. If a natural-language theorem is first specialized and then formalized in Lean, the result should align with formalizing the original theorem and then specializing the formal statement. The two paths need not produce identical syntax. They should agree under a stated formal or reviewed equivalence regime (LeanRef,TPIL4).</p>
<p>Functorial Consistency differs from ordinary robustness. Robustness often asks whether an output remains stable under perturbation. Functorial Consistency asks whether the output changes in the right way under a typed transformation. Some transformations should preserve meaning. Others should change meaning in controlled ways. A paraphrase can preserve denotation. A specialization should narrow a claim. An edge-case strengthening should add a behavioral condition. A decomposition should preserve recomposability.</p>
<p>Functorial Consistency also differs from self-consistency. Self-consistency compares repeated samples, reasoning paths, or outputs from the same prompt. Functorial Consistency compares two structured paths involving source-side transformation, target translation, and target-side transformation. Agreement is measured between transformed artifacts, not among repeated answers.</p>
<p>Table. Functorial Consistency against adjacent evaluation types.</p>
<p class="table-display-caption" id="table-6-caption">Table. Functorial Consistency against adjacent evaluation types.</p>
<div aria-labelledby="table-6-caption" class="table-scroll" data-columns="2" role="group" tabindex="0"><table data-source-table="6" id="table-6"><caption class="visually-hidden">Table. Functorial Consistency against adjacent evaluation types.</caption>
<colgroup>
<col style="width: 49%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Evaluation type</strong></th>
<th scope="col"><strong>Question</strong></th>
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
</table></div>
<p>Existing compositional-generalization benchmarks test systematic recombination (SCAN2018,CFQ2020,COGS2020,SLOG2023). Recent transformation-sensitive benchmarks test formal-specification or semantic consistency under transformations (FormalBench2025,ConsistencyChecker2025). Functorial Consistency adds a proposed standardized commutation-square item that records both paths and labels failures by the component that breaks.</p>
<p>Useful metrics include local validity, path agreement, type preservation, assumption preservation, generality preservation, constraint integration, repair cost, reviewer agreement, and diagnostic novelty. The failure taxonomy includes object failure, transformation failure, translation failure, target-transformation failure, non-commutation, type drift, assumption loss, generality collapse, overstrengthening, spurious equivalence, validator mismatch, and constraint mention without integration.</p>
<p>The benchmark succeeds only if it reveals failures that local accuracy, ordinary robustness, or ordinary self-consistency miss. If the categorical framing does not improve benchmark design, failure diagnosis, or structure-preservation analysis, it should be reduced to a plain commutation-test framing. The benchmark fails if commutation squares reveal no diagnostic failures beyond local accuracy, robustness, or self-consistency.</p>
<h2 id="extensions-as-record-disciplines">Extensions as Record Disciplines</h2>
<p>The first three layers define the core framework: membership, generation, and transformation. The remaining layers show how the same record protocol extends into language composition, architecture choice, quantitative warrant, and effectful action.</p>
<p>Table. Extension schemas and boundaries.</p>
<p class="table-display-caption" id="table-7-caption">Table. Extension schemas and boundaries.</p>
<div aria-labelledby="table-7-caption" class="table-scroll" data-columns="4" role="group" tabindex="0"><table data-source-table="7" id="table-7"><caption class="visually-hidden">Table. Extension schemas and boundaries.</caption>
<colgroup>
<col style="width: 24%"/>
<col style="width: 24%"/>
<col style="width: 25%"/>
<col style="width: 25%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Extension</strong></th>
<th scope="col"><strong>Core question</strong></th>
<th scope="col"><strong>Schema</strong></th>
<th scope="col"><strong>Boundary</strong></th>
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
<td>Gamma;M;E;C ⊢ a : Pre -&gt; Post ! epsilon @ rho</td>
<td>an action is not an answer</td>
</tr>
</tbody>
</table></div>
<h3 id="language">Language</h3>
<p>Grammar-as-logic supplies a precise layer for asking whether language models expose, predict, or benefit from typed compositional structure. Lambek calculus and categorial grammar make linguistic composition type-like, and supertagging provides a practical entry point through rich lexical category assignment (Lambek1958,BangaloreJoshi1999). DisCoCat supplies a categorical framework for compositional distributional semantics, and recent LLM-supertagging work shows that large language models can be applied to categorial supertagging tasks (DisCoCat2010,LLMSupertagger2024).</p>
<p>A Lambek Machine is proposed here as a language system that exposes enough of this typed compositional pipeline for analysis, supervision, constrained generation, or architectural bias. The definition is operational. It does not assert that Transformers literally implement Lambek calculus, that supertagging is semantic understanding, or that symbolic categorial grammar should replace neural language modeling. The decisive test is downstream compositional behavior.</p>
<h3 id="architecture">Architecture</h3>
<p>Architecture design solves a matching problem. A task imposes structure. A model family embodies assumptions. The design problem is to align them well enough that the model can learn efficiently, generalize appropriately, preserve relevant invariants, expose useful interfaces, and submit to validation.</p>
<p>The core schema is:</p>
<p>TaskSpec -&gt; ArchitectureType -&gt; ArchitectureInstance, A |= S.</p>
<p>Existing architecture literatures support the importance of structure and inductive bias. Geometric Deep Learning studies geometric priors; Deep Sets characterizes permutation-invariant functions; Graph Networks support relational inductive bias; Transformers introduced attention-based sequence modeling; Mamba introduced selective state-space sequence modeling; and Categorical Deep Learning argues for a category-theoretic bridge between constraints and implementations (GDL2021,DeepSets2017,GraphNetworks2018,Transformer2017,Mamba2023,CategoricalDL2024). ArchitectureSpec is a proposed design and evaluation schema. It asks whether a task specification can rule out unsuitable architecture families, expose structural tradeoffs, predict mismatch failures, and define validators.</p>
<h3 id="warrant">Warrant</h3>
<p>Modern AI systems often operate around exact judgments without producing exact judgments directly. They propose tactics, retrieve premises, rank lemmas, generate proof scripts, draft formal statements, produce code, optimize differentiable constraints, and construct reasoning traces. These objects can be scored before they are checked.</p>
<p>Quantitative Curry-Howard is proposed here as a study of the candidate layer before and around exact validation:</p>
<p>Gamma ⊢_theta t : A ▷ Q.</p>
<p>Q is a quantitative evidence record. It can include score, probability, uncertainty, loss, margin, calibration status, validation status, diagnostics, repair distance, epistemic type, and permitted use.</p>
<p>Soft warrant is not proof. End-to-end differentiable proving, Logical Neural Networks, quasi-Borel spaces, and proof-assistant work on differentiable and fuzzy logics support the study of quantitative or differentiable warrant (DiffProving2017,LNN2020,QBS2017,DifferentiableLogicsDTT2026). They do not make scores, probabilities, or differentiable satisfaction into proof. Quantitative Curry-Howard Bench succeeds only if quantitative records improve search, review, repair, reuse, calibration, or admissibility.</p>
<h3 id="action">Action</h3>
<p>When AI systems act, output-centric evaluation fails more severely since an action changes state. The state can be internal, computational, social, economic, or physical. The correct unit of analysis is the typed, warranted, effectful trace by which an agent moves from instruction to consequence.</p>
<p>The central judgment is:</p>
<p>Gamma; M; E; C ⊢ a : Pre -&gt; Post ! epsilon @ rho.</p>
<p>Here Gamma is instruction and policy context. M is memory. E is environment or interface state. C is capability context. a is an action or plan step. Pre and Post are preconditions and postconditions. epsilon is an effect row. rho records risk, authority, reversibility, and validation obligations.</p>
<p>The notation is operational. It does not claim that current agents possess a full static type system. It specifies the records, handlers, validators, and audit traces required when an AI system performs computations with consequences. An action is not an answer.</p>
<p>Hoare logic, PDDL, monads, and algebraic effects supply foundational accounts of preconditions, postconditions, planning effects, and computational effects (Hoare1969,PDDL1998,Moggi1989,PlotkinPretnar2013). Contemporary agent benchmarks and tool-use systems motivate the need for trajectory-level evaluation across reasoning-action interleaving, tool use, realistic web and computer environments, policy-constrained interactions, prompt-injection settings, and trajectory evaluation (ReAct2022,Toolformer2023,WebArena2023,OSWorld2024,TauBench2025,AgentDojo2024,AgentRewardBench2025). TypedActionLedger is proposed here as an accounting layer around such systems. It succeeds only if it changes execution, repair, review, or audit.</p>
<h2 id="benchmarks-and-implementation-agenda">Benchmarks and Implementation Agenda</h2>
<p>Compositional Intelligence has value only if its records turn into benchmarks, validators, and implementation artifacts. The core technical agenda is summarized below.</p>
<p>Table. Artifacts, tests, and failure conditions.</p>
<p class="table-display-caption" id="table-8-caption">Table. Artifacts, tests, and failure conditions.</p>
<div aria-labelledby="table-8-caption" class="table-scroll" data-columns="4" role="group" tabindex="0"><table data-source-table="8" id="table-8"><caption class="visually-hidden">Table. Artifacts, tests, and failure conditions.</caption>
<colgroup>
<col style="width: 24%"/>
<col style="width: 25%"/>
<col style="width: 24%"/>
<col style="width: 25%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Layer</strong></th>
<th scope="col"><strong>Artifact</strong></th>
<th scope="col"><strong>Test</strong></th>
<th scope="col"><strong>Failure condition</strong></th>
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
</table></div>
<p>A first Type-First Prompting pilot should use 100-150 curated items across code, Lean or mathematics, explanation, scientific protocol design, and planning. It should measure target-type accuracy, constraint recall, inhabitant validity, semantic alignment, repair cost, type stability, downstream usability, and ambiguity handling.</p>
<p>A first Functorial Consistency pilot should use 80-120 commutation-square items across informal mathematics to Lean, requirements to code, language to semantic parse, and goals to plans. The first version should prioritize exact, executable, and denotational equivalence regimes before relying heavily on reviewed alignment. The primary question is whether path agreement reveals failures missed by local validity.</p>
<p>A first Lambek pilot should use two or three dataset families: a categorial resource for supertagging and derivational evaluation, a semantic parsing dataset or controlled semantic examples, and hand-curated transformation squares. The primary question is whether categorial structure improves downstream semantic behavior, not merely category prediction.</p>
<p>A first ArchitectureSpec catalog should contain 20-30 task-family records with candidate architecture families, excluded families, structural commitments, validators, and predicted failure modes. Candidate task families include sets, graphs, molecules, long-context sequences, proof states, scientific protocols, and agent workflows.</p>
<p>A first Quantitative Curry-Howard pilot should collect candidate artifacts with scores, validation outcomes, repair traces, and calibration records. The initial domains can include Lean proof search, code synthesis, soft constraints, probabilistic scientific claims, and reasoning-trace verification where appropriate.</p>
<p>A first Effectful Agent pilot should annotate existing web or tool-use tasks with preconditions, postconditions, effects, authority, side-effect labels, memory updates, rollback requirements, and audit traces. Evaluation should include unauthorized action rate, side-effect control, data isolation, memory pollution, rollback quality, and audit completeness.</p>
<p>The minimum viable repository should contain four components: JSON Schemas for the records, a small seed dataset for each benchmark family, validator interfaces for each equivalence regime, and diagnostic scripts that produce failure labels instead of only aggregate scores. The first repository should prioritize data schemas and diagnostic scripts before model training.</p>
<h2 id="related-work-and-source-boundaries">Related Work and Source Boundaries</h2>
<p>Compositional Intelligence is built from existing technical traditions, but its core artifacts are original proposals. Formal verification and proof assistants supply validation mechanisms; they do not by themselves establish source-target alignment or downstream semantic membership (LeanRef,TPIL4,LeanDojo2023). Proof-assistant infrastructure and tool-use systems supply examples of typed or interface-constrained construction; they do not settle target-type inference for open-ended natural-language tasks (LeanRef,TPIL4,LeanDojo2023,Toolformer2023).</p>
<p>Compositional-generalization and transformation-sensitive benchmarks motivate the evaluation space; Functorial Consistency proposes a path-agreement record for transformations across source and target environments (SCAN2018,CFQ2020,COGS2020,SLOG2023,FormalBench2025,ConsistencyChecker2025). Categorial grammar supplies typed linguistic composition; Lambek Machines ask whether exposed categorial structure improves downstream model behavior (Lambek1958,BangaloreJoshi1999,DisCoCat2010,LLMSupertagger2024). Architecture research supplies structural priors; ArchitectureSpec asks whether task records improve model-family choice (GDL2021,DeepSets2017,GraphNetworks2018,Transformer2017,Mamba2023,CategoricalDL2024). Differentiable proving and neuro-symbolic methods supply soft reasoning mechanisms; Quantitative Curry-Howard records their warrant and preserves the boundary between score and proof (DiffProving2017,LNN2020,QBS2017,DifferentiableLogicsDTT2026). Agent benchmarks and tool-use frameworks supply realistic task contexts; TypedActionLedger asks whether preconditions, postconditions, authority, handlers, effects, and audit records improve action control (Hoare1969,PDDL1998,Moggi1989,PlotkinPretnar2013,ReAct2022,Toolformer2023,WebArena2023,OSWorld2024,TauBench2025,AgentDojo2024,AgentRewardBench2025).</p>
<p>The paper uses citations source-functionally. Each source supports a specific background, system, benchmark, or contrast claim. No cited source is used to validate the original Compositional Intelligence artifacts.</p>
<h2 id="limitations-and-falsification">Limitations and Falsification</h2>
<p>Compositional Intelligence has a broad scope, and breadth creates the primary methodological risk. A framework spanning proof assistants, code, science, language, architecture, quantitative warrant, and agent action can degrade into vocabulary absent operational consequences. The response is to require records, validators, benchmarks, and kill criteria.</p>
<p>The main limitations are the following.</p>
<ol start="6" type="1">
<li><p>The framework can turn into too broad to constrain annotation, evaluation, or design.</p></li>
<li><p>Domains differ sharply in formalization level.</p></li>
<li><p>Human equivalence judgments can be noisy.</p></li>
<li><p>Record schemas can turn into expensive metadata.</p></li>
<li><p>Type annotations can fail to predict model errors.</p></li>
<li><p>Functorial Consistency can add little beyond local accuracy.</p></li>
<li><p>ArchitectureSpec can fail to improve architecture choice.</p></li>
<li><p>TypedActionLedger can fail to influence execution or repair.</p></li>
<li><p>The framework can overfit to domains where artifacts are already structured and underperform in open-ended interpretive tasks.</p></li>
</ol>
<p>The first empirical phase should therefore focus on domains with explicit validators before expanding to interpretive settings. Proof assistants, code, semantic parsing, planning, and tool-use workflows are better initial domains than open-ended conversation, cultural interpretation, or unconstrained creative tasks. The program can later expand only where its records produce measurable diagnostic value.</p>
<p>Human equivalence judgments should be used carefully. Reviewed alignment should enter where formal, executable, or denotational checks are unavailable or incomplete. It should be recorded as reviewed alignment, not hidden behind mathematical notation. The symbol ≈ is never enough by itself.</p>
<p>Record schemas can turn into expensive metadata. This risk is material. An ArtifactRecord, QuantitativeJudgmentRecord, or TypedActionLedgerEntry matters only when it changes diagnosis, review, repair, reuse, authorization, or audit. If record fields are filled after the fact and never used to guide system behavior or human decisions, they should be simplified or removed.</p>
<p>The framework should be revised if its records do not improve validation, alignment, diagnosis, repair, reuse, architecture choice, calibration, or effect control. It should be narrowed if its schemas fail outside proof assistants, code, semantic parsing, and agent workflows. It should be simplified if its mathematical vocabulary does not improve annotation, evaluation, or system design.</p>
<p>The credible version of the program is empirical.</p>
<p>The kill criteria are explicit and operational.</p>
<ol start="15" type="1">
<li><p>Artifact records do not improve review, repair, or reuse.</p></li>
<li><p>Target-type annotations do not predict or classify failures.</p></li>
<li><p>Functorial Consistency adds no diagnostic signal beyond ordinary accuracy.</p></li>
<li><p>Categorial supervision does not improve downstream compositional behavior.</p></li>
<li><p>ArchitectureSpec cannot rule out unsuitable architectures.</p></li>
<li><p>Quantitative records do not predict validation, repair, or calibration.</p></li>
<li><p>Typed action ledgers do not reduce unauthorized actions, side effects, repair cost, or audit failures.</p></li>
</ol>
<p>These criteria expose the proposal to empirical rejection, which is part of the contribution.</p>
<h2 id="conclusion">Conclusion</h2>
<p>Compositional Intelligence reframes generative AI evaluation around typed artifacts and the structured worlds those artifacts enter. The path from output to knowledge requires target-type inference, candidate construction, transformation preservation, validation, warrant, reuse, and effect control. This paper has presented a compact framework for that path and a set of records and benchmarks that could refute or refine it.</p>
<p>The framework succeeds only if it makes AI artifacts more checkable, composable, repairable, reusable, calibrated, and accountable. Its ambition is matched by a concrete test. If the records do not change validation, repair, review, architecture choice, or action control, they should be revised or removed. If they do, Compositional Intelligence offers a practical route from fluent output to structured participation.</p>
<h2 id="appendix-materials-from-the-synthesis-paper">Appendix</h2>
<h2 id="claim-levels-and-epistemic-types">Claim Levels and Epistemic Types</h2>
<h3 id="claim-levels">Claim levels</h3>
<p class="table-display-caption" id="table-9-caption">Table 9. Level, Meaning, Publication treatment</p>
<div aria-labelledby="table-9-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="9" id="table-9"><caption class="visually-hidden">Table 9. Level, Meaning, Publication treatment</caption>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Level</strong></th>
<th scope="col"><strong>Meaning</strong></th>
<th scope="col"><strong>Publication treatment</strong></th>
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
</table></div>
<h3 id="epistemic-types">Epistemic types</h3>
<p class="table-display-caption" id="table-10-caption">Table 10. Type, Meaning — Type, Meaning</p>
<div aria-labelledby="table-10-caption" class="table-scroll" data-columns="2" role="group" tabindex="0"><table data-source-table="10" id="table-10"><caption class="visually-hidden">Table 10. Type, Meaning — Type, Meaning</caption>
<colgroup>
<col style="width: 49%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Type</strong></th>
<th scope="col"><strong>Meaning</strong></th>
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
</table></div>
<h2 id="minimal-schema-summaries">Minimal Schema Summaries</h2>
<h3 id="artifactrecord">ArtifactRecord</h3>
<p>artifact_record:</p>
<p>id: string</p>
<p>kind: string</p>
<p>content: string | object</p>
<p>target_environment: string</p>
<p>dependencies: list[string]</p>
<p>assumptions: list[string]</p>
<p>validation_status: string</p>
<p>epistemic_type: string</p>
<p>alignment_status: string</p>
<p>permitted_use: list[string]</p>
<p>repair_path: string | null</p>
<h3 id="targettyperecord">TargetTypeRecord</h3>
<p>target_type_record:</p>
<p>task_id: string</p>
<p>prompt: string</p>
<p>context: string</p>
<p>candidate_target_types: list[string]</p>
<p>selected_target_type: string</p>
<p>constraints: list[string]</p>
<p>invalid_target_types: list[string]</p>
<p>validation_method: string</p>
<h3 id="functorialconsistencyitem">FunctorialConsistencyItem</h3>
<p>functorial_consistency_item:</p>
<p>id: string</p>
<p>source_environment: string</p>
<p>target_environment: string</p>
<p>source_object: string</p>
<p>source_transformation: string</p>
<p>translation: string</p>
<p>target_transformation: string</p>
<p>equivalence_regime: string</p>
<p>validator: string</p>
<p>failure_labels: list[string]</p>
<h3 id="architecturespec">ArchitectureSpec</h3>
<p>architecture_spec:</p>
<p>id: string</p>
<p>task_family: string</p>
<p>object_types: list[string]</p>
<p>transformations: list[string]</p>
<p>laws: list[string]</p>
<p>operations: list[string]</p>
<p>interfaces: list[string]</p>
<p>effects: list[string]</p>
<p>validators: list[string]</p>
<p>candidate_architectures: list[string]</p>
<p>excluded_architectures: list[string]</p>
<p>predicted_failure_modes: list[string]</p>
<h3 id="quantitativejudgmentrecord">QuantitativeJudgmentRecord</h3>
<p>quantitative_judgment:</p>
<p>artifact_id: string</p>
<p>context: string</p>
<p>target: string</p>
<p>candidate: string</p>
<p>model: string</p>
<p>score: string | number | null</p>
<p>probability: number | null</p>
<p>uncertainty: string | null</p>
<p>calibration_status: string</p>
<p>validation_status: string</p>
<p>diagnostics: string</p>
<p>repair_distance: string | null</p>
<p>epistemic_type: string</p>
<p>permitted_use: list[string]</p>
<h3 id="typedactionledgerentry">TypedActionLedgerEntry</h3>
<p>typed_action_ledger_entry:</p>
<p>entry_id: string</p>
<p>action_type: string</p>
<p>instruction_sources: list[string]</p>
<p>observation_sources: list[string]</p>
<p>preconditions: list[string]</p>
<p>postconditions: list[string]</p>
<p>declared_effects: list[string]</p>
<p>authority_source: string</p>
<p>capabilities_required: list[string]</p>
<p>handler: string</p>
<p>authorization_result: string</p>
<p>execution_result: string</p>
<p>observed_state_delta: string</p>
<p>frame_conditions:</p>
<p>may_modify: list[string]</p>
<p>must_preserve: list[string]</p>
<p>validation_result: string</p>
<p>repair_or_rollback: string | null</p>
<p>permitted_downstream_use: list[string]</p>
<h3 id="concepttransferrecord">ConceptTransferRecord</h3>
<p>concept_transfer_record:</p>
<p>id: string</p>
<p>source_domain: string</p>
<p>target_domain: string</p>
<p>preserved_relations: list[string]</p>
<p>lost_relations: list[string]</p>
<p>counterexamples: list[string]</p>
<p>distortion_risk: string</p>
<p>permitted_use: list[string]</p>
<p>forbidden_use: list[string]</p>
