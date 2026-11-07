# Algebraic Architectures

*Mateo Petel*

## Abstract

Neural architectures are frequently characterized through capacity, training procedure, benchmark performance, parameter count, and scaling behavior. Those descriptors omit a structural dimension that matters for Compositional Intelligence. A model family encodes commitments about the objects it represents, the transformations it preserves, the symmetries it exploits, the memory regimes it supports, the interfaces it exposes, and the validators that can be applied to its outputs. These commitments affect sample efficiency, extrapolation, interpretability, runtime cost, validation design, and deployment failure modes.

Algebraic Architectures proposes specification-first assessment of neural architecture choices. TaskSpec -\> ArchitectureType -\> ArchitectureInstance records how a task constrains objects, operations, symmetries, interfaces, memory, resources and validation. The formal relation A \|= S is used only for a specified satisfaction claim with stated semantics and proof obligations. Architectural compatibility, empirical behavior, expert-reviewed fit, implementation cost and residual mismatch occupy separate evidence fields. ArchitectureSpec is proposed as an auditable decision record. Its utility depends on improved exclusions, validation and task-family selection.

The architectural baselines considered here include geometric deep learning, Deep Sets, graph networks, Transformers, selective state-space models, and categorical deep learning <span class="citation-group">[<a class="citation-link" href="#ref-GDL2021" aria-label="Reference 1 — Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges">1</a>, <a class="citation-link" href="#ref-DeepSets2017" aria-label="Reference 2 — Deep Sets">2</a>, <a class="citation-link" href="#ref-GraphNetworks2018" aria-label="Reference 3 — Relational Inductive Biases, Deep Learning, and Graph Networks">3</a>, <a class="citation-link" href="#ref-Transformer2017" aria-label="Reference 4 — Attention Is All You Need">4</a>, <a class="citation-link" href="#ref-Mamba2023" aria-label="Reference 5 — Mamba: Linear-Time Sequence Modeling with Selective State Spaces">5</a>, <a class="citation-link" href="#ref-CategoricalDL2024" aria-label="Reference 6 — Position: Categorical Deep Learning is an Algebraic Theory of All Architectures">6</a>]</span>. Other families identified for an expanded comparison include equivariant neural networks, graph Transformers, equivariant atomistic architectures, neural algorithmic reasoning, and scientific graph systems. These literatures motivate the proposed specification record without validating it. The companion artifact is the Architecture Specification Catalog, which compares architecture families against task specifications through explicit exclusions, tradeoffs, validators, evidence levels, and decision criteria. Scientific value depends on independent tests of whether the record constrains design choice, predicts mismatch, improves validation, or changes an architecture decision.

## Contribution summary



<table>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
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
<td>Specification-first architecture</td>
<td>Architecture selection is framed as a match between a structured task specification, an architecture family, and a trained instance.</td>
</tr>
<tr class="even">
<td>C2</td>
<td>Operational satisfaction relation</td>
<td>ArchitectureSpec records formal satisfaction, structural support, empirical results, reviewed fit and violations in distinct evidence fields.</td>
</tr>
<tr class="odd">
<td>C3</td>
<td>ArchitectureSpec</td>
<td>The proposed schema records object types, transformations, operations, laws, symmetries, resources, interfaces, effects, and validators.</td>
</tr>
<tr class="even">
<td>C4</td>
<td>Mismatch taxonomy</td>
<td>The essay distinguishes underbias, overbias, symmetry mismatch, relational mismatch, memory mismatch, interface mismatch, validation mismatch, and cost-structure mismatch.</td>
</tr>
<tr class="odd">
<td>C5</td>
<td>Architecture Specification Catalog</td>
<td>The catalog functions as an exclusion and validation instrument, not as a taxonomy of model names.</td>
</tr>
<tr class="even">
<td>C6</td>
<td>Bridge to quantitative warrant</td>
<td>The next layer studies how learned systems attach scores, probabilities, uncertainty, validation status, and repair distance to candidate typed artifacts.</td>
</tr>
</tbody>
</table>



## Reader map



<table>
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Reader</strong></th>
<th><strong>Recommended path</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ML architecture researcher</td>
<td>Sections 1, 3, 4, 5, 8, 9, and Appendix A</td>
</tr>
<tr class="even">
<td>Geometric deep learning researcher</td>
<td>Sections 4, 6.1, 7.1, 7.2, 7.3, and 9</td>
</tr>
<tr class="odd">
<td>Formal-methods or category-theory reader</td>
<td>Sections 3, 4, 5, 8, and Appendix C</td>
</tr>
<tr class="even">
<td>AI evaluation researcher</td>
<td>Sections 5, 8, 9, 10, 11, and Appendix B</td>
</tr>
<tr class="odd">
<td>Series reader</td>
<td>Read after Essay 4 and before Essay 6</td>
</tr>
</tbody>
</table>



## 1. Position in the Compositional Intelligence series {#1-position-in-the-compositional-intelligence-series}

The architecture layer specifies how model-family commitments interact with typed artifacts and structure-preserving evaluation. The first essays define artifact membership, target-type inference, and transformation-sensitive evaluation. The language layer instantiates these ideas in typed linguistic composition. Essay 5 shifts attention to the model families that make certain objects, transformations, validators, and failure modes easier to represent or harder to observe.

Architecture is part of the artifact lifecycle in any setting where the task imposes structure that the model must preserve under transformation. A set-valued task requires invariance to item order; an atomistic prediction task requires rotation, translation, and permutation constraints; an effectful workflow requires explicit state interfaces and validation hooks. A model family either supports the relevant structure directly, learns it indirectly, hides it behind scale, or introduces an incompatible bias. The specification layer records which case is being claimed and what evidence would distinguish it.

ArchitectureSpec inherits the transformation requirement from Functorial Consistency. A structural architecture claim should identify the transformations under which behavior is invariant, equivariant, covariant, specialized, generalized, or deliberately changed. The specification has value only when those commitments produce validators, counterexamples, or exclusions.

> artifact membership -\> target-type inference -\> transformation preservation -\> language structure -\> architecture specification

## 2. Thesis and boundary conditions {#2-thesis-and-boundary-conditions}

The thesis of Algebraic Architectures is that architecture design should be evaluated as a specification-satisfaction problem. A task imposes object structure, transformation structure, operational laws, interface requirements, effects, resources, and validators. A model family encodes assumptions about those structures, and a trained instance realizes those assumptions under data, optimization, scale, inference, and deployment constraints.

The proposed account constrains architecture selection without replacing empirical comparison. Algebraic, geometric, or categorical arguments supply candidate invariants, equivariances, locality assumptions, compositional interfaces, and validation tests. They do not settle performance under finite data, nonideal optimization, distribution shift, resource limits, or hybrid deployment constraints. The architecture record should therefore state the status of each claim, including formal guarantee, architectural support, empirical satisfaction, reviewed alignment, or violation.

Geometric deep learning, Deep Sets, graph networks, and categorical deep learning <span class="citation-group">[<a class="citation-link" href="#ref-GDL2021" aria-label="Reference 1 — Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges">1</a>, <a class="citation-link" href="#ref-DeepSets2017" aria-label="Reference 2 — Deep Sets">2</a>, <a class="citation-link" href="#ref-GraphNetworks2018" aria-label="Reference 3 — Relational Inductive Biases, Deep Learning, and Graph Networks">3</a>, <a class="citation-link" href="#ref-CategoricalDL2024" aria-label="Reference 6 — Position: Categorical Deep Learning is an Algebraic Theory of All Architectures">6</a>]</span> provide documented structural baselines. Transformers, selective state-space models, equivariant atomistic networks, and neural algorithmic reasoning remain additional comparison families requiring individual source review in a final survey. ArchitectureSpec and the Architecture Specification Catalog are proposed Compositional Intelligence records for task-level design audit. Their incremental diagnostic value remains unmeasured.

## 3. Formal core. Architecture as satisfaction of structure {#3-formal-core-architecture-as-satisfaction-of-structure}

The central schema separates task structure, model-family commitment, and trained-system evidence.

$$
\mathrm{TaskSpec}\to\mathrm{ArchitectureType}\to\mathrm{ArchitectureInstance}.
$$

TaskSpec describes the structure the task imposes before candidate architectures are selected. ArchitectureType describes a model family together with its representational commitments, computational primitives, symmetry assumptions, memory mechanisms, interfaces, and validator exposure. ArchitectureInstance denotes a trained system with parameters, data, objective, optimizer, inference procedure, memory subsystem, interface implementation, validation record, and deployment profile. A strong architecture type can produce a weak instance, and a general model family can occasionally learn a structure that another family encodes directly. The record should keep those cases distinct.

For a formal architecture model A and formal specification S, the assertion A \|= S carries the proof or semantic satisfaction obligation specified by the chosen theory. For empirical architecture selection, ArchitectureSpec instead records structural compatibility, trained-instance results, reviewed fit, resource constraints and counterexamples as separately attributed claims. The record must identify the architecture instance and test setting whenever empirical performance is asserted.



<table>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Regime</strong></th>
<th><strong>Meaning</strong></th>
<th><strong>Required evidence</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>formal guarantee</td>
<td>The architecture enforces the property by construction or proof.</td>
<td>Mathematical proof, type-level guarantee, exact equivariance argument, or verified implementation.</td>
</tr>
<tr class="even">
<td>architectural support</td>
<td>The architecture makes the property low-cost or natural without guaranteeing it.</td>
<td>Mechanistic argument, structural analysis, ablation, or controlled transformation test.</td>
</tr>
<tr class="odd">
<td>empirical satisfaction</td>
<td>A trained instance demonstrates the behavior under stated conditions.</td>
<td>Evaluation results, transformation tests, calibration, and error analysis.</td>
</tr>
<tr class="even">
<td>reviewed alignment</td>
<td>Experts judge the architecture-task match when formal tests are incomplete.</td>
<td>Reviewer protocol, rationale, uncertainty statement, and disagreement record.</td>
</tr>
<tr class="odd">
<td>violation</td>
<td>The architecture ignores, distorts, or conflicts with task structure.</td>
<td>Counterexample, failed validator, cost failure, or mismatch report.</td>
</tr>
</tbody>
</table>



## 4. ArchitectureSpec v0.3 {#4-architecturespec-v0-3}

ArchitectureSpec records the structures that a model family must represent, preserve, expose, or validate. The schema is designed as an exclusion and validation instrument. A record that accepts every architecture for every task has no design value.

> ArchitectureSpec = (O, T, Sigma, L, G, R, Phi, E, V)\
> O object types such as sets, graphs, sequences, fields, molecules, programs, proof states, plans\
> T transformations such as permutations, rotations, translations, rewrites, time shifts, interventions\
> Sigma operations such as aggregation, message passing, attention, recurrence, composition, retrieval, planning\
> L laws such as invariance, equivariance, conservation, causality, monotonicity, locality, typing rules\
> G symmetries and geometry such as groups, gauges, coordinates, manifolds, graph automorphisms\
> R resources such as context length, memory, latency, throughput, compute, data, bandwidth, energy\
> Phi interfaces such as inputs, outputs, tools, validators, explanations, proof obligations, APIs\
> E effects such as state, IO, uncertainty, external tools, interaction, physical action, feedback\
> V validators such as tests, ablations, invariance checks, simulations, proofs, expert review

The specification should force an explicit mismatch diagnosis. If the task is permutation-invariant and the architecture treats arbitrary order as semantically meaningful, the record should require a permutation validator or exclude the architecture for the base design. If the task depends on graph-local interactions and the model flattens the graph without structural encodings, the record should mark a relational underbias. If the task requires long-range selective access under latency constraints, the record should distinguish direct content interaction from compressed state propagation and report the associated resource profile.

A structural guarantee identifies the architecture family, the input domain, the transformation class, and the assumptions under which a property holds for all admissible inputs. Finite transformation tests provide instance-specific empirical evidence over sampled cases; they do not prove a universal invariance claim. Trained-instance checks must additionally account for preprocessing, approximation and runtime interfaces. Extrapolation claims need held-out sizes, geometries or horizons, and effectful interfaces need validated action preconditions, postconditions and authority. ArchitectureSpec records each assertion with its quantifiers, proof or test procedure, evidence grade and unresolved counterexamples.

## 5. Underbias, overbias, and cost structure {#5-underbias-overbias-and-cost-structure}

Inductive bias has diagnostic value only when the specification records both its benefits and its failure modes. Underbias occurs when known task structure is absent from the architecture, forcing the instance to learn the structure from data, scale, or incidental correlations. Overbias occurs when the architecture enforces a law that excludes valid task behavior. A credible architecture analysis must detect both errors and avoid treating structural design as a one-directional improvement.



<table>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Risk</strong></th>
<th><strong>Diagnostic case</strong></th>
<th><strong>Audit question</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>underbias</td>
<td>A sequence model treats set order as informative in a task whose target is exchangeable.</td>
<td>Does output change under irrelevant item permutations?</td>
</tr>
<tr class="even">
<td>underbias</td>
<td>A molecule model omits graph and coordinate structure.</td>
<td>Does prediction fail under atom relabeling, rotation, translation, or physical sanity checks?</td>
</tr>
<tr class="odd">
<td>overbias</td>
<td>A local message-passing model is used for a task dominated by global dependencies.</td>
<td>Does performance degrade under long-range interaction tests or graph-size extrapolation?</td>
</tr>
<tr class="even">
<td>overbias</td>
<td>A rigid grammar constraint is imposed on open-domain generation.</td>
<td>Does the constraint exclude valid outputs or reduce utility without validation gain?</td>
</tr>
<tr class="odd">
<td>cost mismatch</td>
<td>A quadratic attention model is selected for million-token retrieval under strict latency constraints.</td>
<td>Does the architecture meet memory, latency, throughput, and retrieval obligations?</td>
</tr>
<tr class="even">
<td>interface mismatch</td>
<td>A static predictor is used in tool, state, and action workflows.</td>
<td>Can the system expose preconditions, postconditions, effects, rollback, and audit traces?</td>
</tr>
</tbody>
</table>



Cost belongs inside the architecture specification. Latency, memory, bandwidth, deployment hardware, context length, retraining cost, data availability, and validator cost determine whether a structural commitment is usable in the intended environment. A specification that ignores resource and interface constraints is incomplete for deployed systems, even when the architecture has favorable local accuracy.

## 6. State-of-the-art landscape and source use {#6-state-of-the-art-landscape-and-source-use}

The state-of-the-art landscape supplies structural lessons for ArchitectureSpec. Each source tradition supports a specific design claim, and none validates the proposed record schema by itself. The architecture layer should therefore cite these literatures for their demonstrated commitments and then state the additional specification claim introduced here.



<table>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Area</strong></th>
<th><strong>Structural lesson</strong></th>
<th><strong>ArchitectureSpec implication</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>geometric deep learning</td>
<td>Many tasks contain symmetries, locality, gauges, graphs, manifolds, or geometric priors.</td>
<td>Record transformations, symmetry groups, and invariance or equivariance validators.</td>
</tr>
<tr class="even">
<td>Deep Sets</td>
<td>Permutation-invariant set functions require architectures that respect exchangeability.</td>
<td>Record whether ordering is meaningful or spurious.</td>
</tr>
<tr class="odd">
<td>graph networks</td>
<td>Relational inductive bias is appropriate when entities and interactions define the task objects.</td>
<td>Record nodes, edges, global state, message-passing structure, and graph-size obligations.</td>
</tr>
<tr class="even">
<td>Transformers</td>
<td>Attention supports content-addressed interaction over token sequences.</td>
<td>Record sequence structure, context length, retrieval demands, and quadratic-cost tradeoffs.</td>
</tr>
<tr class="odd">
<td>selective state-space models</td>
<td>Input-dependent recurrence supports efficient propagation over long sequences.</td>
<td>Record content selectivity, state compression, retrieval behavior, and latency.</td>
</tr>
<tr class="even">
<td>equivariant atomistic models</td>
<td>3D scientific tasks often require rotation, translation, and permutation structure.</td>
<td>Record geometry, frame conventions, physical sanity checks, and energy-force consistency.</td>
</tr>
<tr class="odd">
<td>neural algorithmic reasoning</td>
<td>Algorithmic tasks require invariants, step structure, and size extrapolation.</td>
<td>Record execution traces, loop invariants, and extrapolation validators.</td>
</tr>
<tr class="even">
<td>categorical deep learning</td>
<td>Categorical language can relate constraints, morphisms, and implementations.</td>
<td>Use categorical notation only when it improves specification, comparison, or diagnosis.</td>
</tr>
</tbody>
</table>



The source anchors for this essay include geometric deep learning, Deep Sets, graph networks, attention-based sequence modeling, selective state-space models, equivariant atomistic architectures, scientific graph systems, neural algorithmic reasoning, and categorical deep learning. These sources motivate the architecture layer as background and do not provide evidence for ArchitectureSpec as an evaluated artifact.

## 7. Worked examples {#7-worked-examples}

### 7.1 Sets {#7-1-sets}

Set-valued tasks expose the distinction between representational convenience and semantic structure. If the target is a function of an unordered finite collection, item permutation should not affect the output. The specification should identify the object type as a set, the transformation as item permutation, the law as invariance, the operation as aggregation or exchangeable attention, and the validator as a permutation stress test.

> TaskSpec: finite set -\> label or statistic\
> Required law: F({x_1,\...,x_n}) = F({x_perm(1),\...,x_perm(n)})\
> Candidate families: Deep Sets, invariant pooling, attention with validated positional treatment\
> Mismatch: sequence model with arbitrary position encodings and no permutation validator

The specification should exclude architectures that assign semantic significance to arbitrary input order unless instance-level validation shows invariance under permutations. The catalog entry earns value by making that exclusion explicit.

### 7.2 Molecules and 3D atomistic systems {#7-2-molecules-and-3d-atomistic-systems}

Atomistic prediction tasks require simultaneous relational and geometric commitments. Atom indexing should be irrelevant, scalar energies should be invariant to rigid frame changes, and vector forces should transform equivariantly. An architecture family can support those laws directly, or an instance can demonstrate them empirically through targeted validators.

> Objects: atoms, bonds, coordinates, scalar energy, vector forces\
> Transformations: atom permutation, rigid rotation, translation\
> Laws: energy invariance, force equivariance, physical sanity constraints\
> Validators: relabeling tests, rotation and translation checks, energy-force consistency, OOD geometry tests

A flat descriptor model can succeed on local benchmarks and still fail under geometric transformations. An equivariant graph architecture provides a stronger structural match, but ArchitectureSpec still requires data-coverage evidence, instance-level checks, and task-specific physical validation before the satisfaction relation is upgraded from architectural support to empirical satisfaction.

### 7.3 Long-context sequence modeling {#7-3-long-context-sequence-modeling}

Long-context tasks differ in the memory operation they require. Some demand exact retrieval from distant context, others require streaming compression, temporal forecasting, or summarization under resource constraints. A generic long-context label therefore hides the architecture question that matters for validation.

> Objects: tokens, spans, events, memory states, retrieved facts\
> Transformations: context extension, truncation, time shift, irrelevant-prefix insertion, distractor insertion\
> Resources: context length, throughput, memory footprint, latency\
> Validators: needle retrieval, degradation curves, distractor robustness, streaming consistency

A selective state-space model and a full-attention Transformer encode different tradeoffs. The former offers efficient recurrent propagation with compressed state; the latter provides direct token-token interaction with higher computational cost. ArchitectureSpec should record the tradeoff and assign validators to the intended memory behavior instead of declaring a universal architecture winner.

### 7.4 Graph-structured scientific systems {#7-4-graph-structured-scientific-systems}

Scientific forecasting systems often combine spatial structure, temporal dynamics, boundary conditions, and interaction graphs. The architecture specification should state whether the task is a mesh problem, graph problem, field problem, sequence problem, or hybrid dynamical system. The lesson from scientific graph systems is that object structure, learned dynamics, and validation target must be specified together.

> Objects: nodes, edges, fields, time steps, forcings, boundary conditions\
> Transformations: spatial shifts, time shifts, grid refinements, perturbations, extreme-event cases\
> Validators: rollout stability, conservation diagnostics, resolution transfer, event-specific error analysis

### 7.5 Algorithms and proof states {#7-5-algorithms-and-proof-states}

Algorithmic and theorem-proving tasks require state representation, invariant preservation, transition structure, and extrapolation beyond seen sizes or seen lemmas. A model can solve small instances and still fail the invariant that defines the algorithm. ArchitectureSpec should therefore record proof-state interfaces, retrieval mechanisms, step validators, and repair behavior.

> Objects: states, goals, subgoals, proof contexts, lemmas, traces\
> Operations: rewrite, split, search, retrieve, backtrack, verify\
> Validators: invariant checks, proof checking, replay, larger-instance generalization, repair cost

### 7.6 Scientific protocols and effectful architectures {#7-6-scientific-protocols-and-effectful-architectures}

Protocol generation and laboratory automation require architecture support for action, state, tool interfaces, uncertainty, external feedback, and audit evidence. A static predictor can draft plausible protocol text and still lack the architectural interfaces needed for execution. This case links the architecture layer to the later effectful-action layer.

> Objects: samples, instruments, measurements, protocols, claims, actions\
> Effects: state changes, physical operations, tool calls, human approval, memory writes\
> Validators: precondition checks, postcondition validation, rollback, audit trace, evidence status

## 8. Architecture Specification Catalog v0.3 {#8-architecture-specification-catalog-v0-3}

The Architecture Specification Catalog is a proposed companion artifact for comparing architecture families against task specifications. The catalog should classify structural commitments, validators, tradeoffs, and exclusions. It should not function as a list of model names.



<table>
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Purpose</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>task family</td>
<td>Name the task family and target artifacts.</td>
</tr>
<tr class="even">
<td>object structure</td>
<td>State whether objects are sets, sequences, graphs, fields, programs, plans, proof states, or hybrids.</td>
</tr>
<tr class="odd">
<td>transformations</td>
<td>List transformations under which behavior should be invariant, equivariant, covariant, or controlled.</td>
</tr>
<tr class="even">
<td>laws and constraints</td>
<td>Record conservation, causality, typing, symmetry, locality, monotonicity, resource, or authority constraints.</td>
</tr>
<tr class="odd">
<td>candidate architectures</td>
<td>List architecture families that support the specification and state the support regime.</td>
</tr>
<tr class="even">
<td>excluded architectures</td>
<td>List model families that are structurally mismatched unless special validation succeeds.</td>
</tr>
<tr class="odd">
<td>validators</td>
<td>Define tests, ablations, proofs, simulations, reviews, and deployment checks.</td>
</tr>
<tr class="even">
<td>tradeoffs</td>
<td>Record compute, latency, memory, data, interpretability, maintenance, and deployment constraints.</td>
</tr>
<tr class="odd">
<td>evidence level</td>
<td>Mark formal guarantee, architectural support, empirical satisfaction, reviewed alignment, or violation.</td>
</tr>
<tr class="even">
<td>predicted failures</td>
<td>State the expected failure if the mismatch hypothesis is correct.</td>
</tr>
</tbody>
</table>



The catalog succeeds only when it changes an architecture decision or a validation plan. An entry that recommends every candidate family, avoids exclusions, or fails to predict a mismatch should be rejected as descriptive taxonomy.

## 9. Architecture comparison protocol {#9-architecture-comparison-protocol}

The comparison protocol converts ArchitectureSpec into an auditable workflow. The protocol is intended for small, high-quality pilots before any large catalog is attempted.



<table>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
<th><strong>Output</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Write the task specification before naming architectures.</td>
<td>TaskSpec with objects, transformations, laws, interfaces, resources, effects, and validators.</td>
</tr>
<tr class="even">
<td>2</td>
<td>List candidate architecture types and their structural commitments.</td>
<td>ArchitectureType comparison table.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>List excluded or high-risk architecture types.</td>
<td>Mismatch hypotheses and expected failure modes.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Define validators for each structural claim.</td>
<td>Transformation tests, ablations, proofs, simulations, or review protocol.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Train or evaluate concrete instances.</td>
<td>Instance-level evidence with cost and deployment metrics.</td>
</tr>
<tr class="even">
<td>6</td>
<td>Run mismatch analysis.</td>
<td>Architecture mismatch report with underbias, overbias, cost, and validation labels.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>Update the catalog entry.</td>
<td>Evidence level and revised decision rule.</td>
</tr>
</tbody>
</table>



## 10. Benchmark obligations {#10-benchmark-obligations}

The first pilot tests whether the specification record improves actual architecture decisions or validation plans beyond established descriptive and expert-led selection practices. Prespecify candidate families, task constraints, exclusion criteria, utility outcomes and reviewer decisions. Hold training data, tuning budgets, compute, evaluation information and reviewer effort comparable across conditions, and assess held-out structural failures and counterexamples. A catalog of 20--30 entries across several task families is a possible pilot scope, not an evidential claim about statistical power. Report selection regret, missed failure modes, resource use and annotation cost.



<table>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Pilot family</strong></th>
<th><strong>Core validator</strong></th>
<th><strong>Failure signal</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>sets</td>
<td>Permutation invariance and item-order stress tests.</td>
<td>Order-sensitive architecture changes predictions under irrelevant permutations.</td>
</tr>
<tr class="even">
<td>graphs</td>
<td>Node relabeling, structural perturbation, and graph-size extrapolation.</td>
<td>Flattened or weakly relational model fails under relabeling or size changes.</td>
</tr>
<tr class="odd">
<td>3D molecules</td>
<td>Permutation, rotation, translation, and physical sanity checks.</td>
<td>Energy or force predictions violate geometry or physical consistency.</td>
</tr>
<tr class="even">
<td>long context</td>
<td>Retrieval, distractor insertion, degradation curves, and latency.</td>
<td>Architecture meets local accuracy but fails resource or retrieval obligations.</td>
</tr>
<tr class="odd">
<td>algorithmic tasks</td>
<td>Invariant checks and size extrapolation.</td>
<td>Model solves training-size cases without preserving algorithmic structure.</td>
</tr>
<tr class="even">
<td>effectful workflows</td>
<td>Precondition, postcondition, effect, rollback, and audit checks.</td>
<td>Static or underinstrumented system cannot expose state-change guarantees.</td>
</tr>
</tbody>
</table>



The benchmark should include cases where several architectures obtain similar local accuracy but diverge under structural transformations, extrapolation, interface validation, or resource constraints. That divergence is the architecture-specific analogue of Functorial Consistency.

## 11. Strongest objections {#11-strongest-objections}



<table>
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Objection</strong></th>
<th><strong>Answer</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This is only inductive bias under another name.</td>
<td>Inductive bias is the background concept. The proposed record links task structure, exclusions, validators, tradeoffs, and evidence levels.</td>
</tr>
<tr class="even">
<td>Architecture choice is empirical.</td>
<td>The framework shapes the hypothesis space and validation plan; experiments remain decisive.</td>
</tr>
<tr class="odd">
<td>Scale often dominates hand-designed structure.</td>
<td>ArchitectureSpec should record when generic scale learns the relevant structure and what compute, data, and validation costs were incurred.</td>
</tr>
<tr class="even">
<td>Strong inductive bias can harm performance.</td>
<td>Overbias is a first-class failure mode, and the catalog must record valid behaviors excluded by the architecture.</td>
</tr>
<tr class="odd">
<td>Category theory is unnecessary.</td>
<td>The categorical layer should be retained only where it improves specification, comparison, or diagnosis.</td>
</tr>
<tr class="even">
<td>Existing frameworks cover much of this.</td>
<td>The essay integrates those frameworks into the Compositional Intelligence chain linking membership, generation, transformation, language, architecture, warrant, and action.</td>
</tr>
<tr class="odd">
<td>The catalog can lose currency.</td>
<td>The catalog should classify structural commitments, validators, and tradeoffs instead of brand-name model families.</td>
</tr>
</tbody>
</table>



## 12. Failure modes and kill criteria {#12-failure-modes-and-kill-criteria}



<table>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Failure mode</strong></th>
<th><strong>Meaning</strong></th>
<th><strong>Required response</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>descriptive collapse</td>
<td>The schema describes every architecture without excluding any.</td>
<td>Strengthen exclusion rules or narrow the task class.</td>
</tr>
<tr class="even">
<td>generic recommendation</td>
<td>The same architecture is recommended across nearly all tasks.</td>
<td>Revise task fields, validators, and mismatch labels.</td>
</tr>
<tr class="odd">
<td>no predictive value</td>
<td>Mismatch hypotheses do not predict failures.</td>
<td>Narrow the theory to domains where structural commitments matter.</td>
</tr>
<tr class="even">
<td>cost omission</td>
<td>The specification ignores latency, memory, compute, or deployment constraints.</td>
<td>Add resource fields and deployment validators.</td>
</tr>
<tr class="odd">
<td>overbias blindness</td>
<td>The framework praises structure without measuring the harm of excessive constraint.</td>
<td>Add counterexamples and overbias tests.</td>
</tr>
<tr class="even">
<td>validator weakness</td>
<td>Structural claims lack tests or ablations.</td>
<td>Remove unsupported claims or define validators.</td>
</tr>
<tr class="odd">
<td>maintenance failure</td>
<td>The catalog cannot track hybrid systems.</td>
<td>Classify by structure instead of model label.</td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Criterion</strong></th>
<th><strong>Decision rule</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>K1</td>
<td>The Architecture Specification Catalog does not improve architecture selection beyond ordinary expert intuition.</td>
</tr>
<tr class="even">
<td>K2</td>
<td>The schema describes architecture families without ruling out unsuitable choices.</td>
</tr>
<tr class="odd">
<td>K3</td>
<td>Architecture specifications fail to predict robustness, sample-efficiency, extrapolation, interpretability, validation, or cost differences.</td>
</tr>
<tr class="even">
<td>K4</td>
<td>The framework cannot distinguish underbias from overbias.</td>
</tr>
<tr class="odd">
<td>K5</td>
<td>The same architecture family is recommended for almost every task.</td>
</tr>
<tr class="even">
<td>K6</td>
<td>The framework cannot produce benchmarkable structural claims.</td>
</tr>
<tr class="odd">
<td>K7</td>
<td>The algebraic or categorical framing adds terminology without improving design.</td>
</tr>
<tr class="even">
<td>K8</td>
<td>Specifications omit deployment-relevant cost, latency, memory, or interface constraints.</td>
</tr>
<tr class="odd">
<td>K9</td>
<td>The catalog cannot be maintained as architecture families evolve.</td>
</tr>
</tbody>
</table>



These criteria keep the proposal accountable to design constraint, failure prediction, and validation. If the catalog does not exclude architectures, predict mismatch, or change validation practice, the architecture layer should be narrowed or retired.

## 13. Relationship to Essay 6. Quantitative Curry-Howard {#13-relationship-to-essay-6-quantitative-curry-howard}

Essay 5 specifies model-family commitments, and Essay 6 specifies the evidentiary layer around candidate typed artifacts. The connection is direct. Architecture determines which structures a model represents and which validators it exposes; quantitative warrant records how candidate outputs are scored, calibrated, checked, repaired, and promoted across epistemic statuses.

The transition is visible across formal, scientific, and agentic systems. A proof-search architecture, molecule model, planning system, or long-context model can be assessed through ArchitectureSpec, but its outputs still require probability, margin, uncertainty, validation status, repair distance, and permitted-use records. The next essay therefore moves from structural commitment to quantitative evidence.

## 14. Conclusion {#14-conclusion}

Algebraic Architectures places model-family selection inside the Compositional Intelligence framework. A generated artifact is shaped by the architecture that produced it, and a structure-preserving transformation is easier to validate when the relevant structure is represented or exposed by design. Architecture claims should therefore identify the task structure, candidate families, excluded families, expected mismatch failures, validators, evidence level, and cost profile.

The proposal remains operational only if it changes design decisions. ArchitectureSpec is useful when it rules out unsuitable model families, predicts mismatch, improves validators, clarifies tradeoffs, or documents the evidentiary status of a structural claim. If it merely relabels inductive bias, the schema should be simplified. The next layer, Quantitative Curry-Howard, applies the same standard to scores, probabilities, uncertainty, validation, and repair around candidate typed artifacts.

## Appendix A. ArchitectureSpec record {#appendix-a-architecturespec-record}

> architecture_spec:\
> id: string\
> task_family: string\
> target_artifacts: list\[string\]\
> object_types: list\[string\]\
> transformations:\
> invariant: list\[string\]\
> equivariant: list\[string\]\
> covariant_or_controlled: list\[string\]\
> operations: list\[string\]\
> laws: list\[string\]\
> symmetries_and_geometry: list\[string\]\
> resources:\
> context_length: string\
> latency: string\
> memory: string\
> throughput: string\
> compute_budget: string\
> data_requirements: string\
> interfaces: list\[string\]\
> effects: list\[string\]\
> validators: list\[string\]\
> candidate_architecture_types: list\[string\]\
> excluded_architecture_types: list\[string\]\
> expected_failure_modes: list\[string\]\
> evidence_level: enum\[formal_guarantee, architectural_support, empirical_satisfaction, reviewed_alignment, violation\]\
> revision_status: string

## Appendix B. Architecture mismatch report {#appendix-b-architecture-mismatch-report}

> architecture_mismatch_report:\
> report_id: string\
> architecture_type: string\
> architecture_instance: string \| null\
> task_spec_id: string\
> mismatch_labels:\
> - symmetry_mismatch\
> - relational_mismatch\
> - memory_mismatch\
> - locality_mismatch\
> - globality_mismatch\
> - modality_mismatch\
> - effect_mismatch\
> - interface_mismatch\
> - invariant_loss\
> - underbias\
> - overbias\
> - validation_mismatch\
> - cost_structure_mismatch\
> failed_validators: list\[string\]\
> counterexamples: list\[string\]\
> observed_cost_profile: string\
> repair_options: list\[string\]\
> decision: enum\[retain, modify_instance, add_module, change_architecture_type, reject_for_task\]\
> rationale: string

## Appendix C. Catalog item example {#appendix-c-catalog-item-example}

> catalog_item:\
> task_family: 3D atomistic energy and force prediction\
> object_types: \[molecule_graph, atom_coordinates, scalar_energy, vector_forces\]\
> transformations:\
> invariant: \[atom_relabeling, global_translation, global_rotation_for_energy\]\
> equivariant: \[global_rotation_for_forces\]\
> candidate_architecture_types:\
> - equivariant graph neural network\
> - equivariant graph transformer\
> high_risk_architecture_types:\
> - flat descriptor model without geometry validators\
> - sequence model without relabeling and frame checks\
> validators:\
> - atom_permutation_test\
> - rotation_translation_test\
> - energy_force_consistency_check\
> - out_of_distribution_geometry_test\
> predicted_failures:\
> - geometry_violation\
> - poor_force_consistency\
> - instability_under_atom_relabeling\
> evidence_level: architectural_support until empirical validation is supplied


<section class="bibliography" aria-labelledby="references-heading">
<h2 id="references-heading">References</h2>

<ol class="references-list">
<li id="ref-GDL2021"><span class="ref-key">[1]</span> <a href="https://arxiv.org/abs/2104.13478" rel="noopener noreferrer">Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges</a>. <span class="ref-details">Bronstein et al. · arXiv preprint 2021.</span></li>
<li id="ref-DeepSets2017"><span class="ref-key">[2]</span> <a href="https://papers.neurips.cc/paper_files/paper/2017/hash/f22e4747da1aa27e363d86d40ff442fe-Abstract.html" rel="noopener noreferrer">Deep Sets</a>. <span class="ref-details">Zaheer et al. · NeurIPS 2017.</span></li>
<li id="ref-GraphNetworks2018"><span class="ref-key">[3]</span> <a href="https://arxiv.org/abs/1806.01261" rel="noopener noreferrer">Relational Inductive Biases, Deep Learning, and Graph Networks</a>. <span class="ref-details">Battaglia et al. · arXiv preprint 2018.</span></li>
<li id="ref-Transformer2017"><span class="ref-key">[4]</span> <a href="https://research.google/pubs/attention-is-all-you-need/" rel="noopener noreferrer">Attention Is All You Need</a>. <span class="ref-details">Vaswani et al. · NeurIPS 2017.</span></li>
<li id="ref-Mamba2023"><span class="ref-key">[5]</span> <a href="https://arxiv.org/abs/2312.00752" rel="noopener noreferrer">Mamba: Linear-Time Sequence Modeling with Selective State Spaces</a>. <span class="ref-details">Gu and Dao · arXiv preprint 2023.</span></li>
<li id="ref-CategoricalDL2024"><span class="ref-key">[6]</span> <a href="https://proceedings.mlr.press/v235/gavranovic24a.html" rel="noopener noreferrer">Position: Categorical Deep Learning is an Algebraic Theory of All Architectures</a>. <span class="ref-details">Gavranović et al. · ICML 2024.</span></li>
</ol>
</section>
