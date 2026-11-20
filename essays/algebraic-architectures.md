# Algebraic Architectures

## Abstract

A neural architecture encodes judgments about the structure of a task. The same tensor representation might describe a time-ordered sequence or an unordered collection, although the two objects obey incompatible transformation laws. Molecular energies and forces transform differently under changes of spatial coordinates. Scientific agents introduce state, action, and external verification beyond the interface of a predictor. Benchmark accuracy and computational cost remain essential measures, yet neither identifies which structural obligations a system enforces by construction, which it learns imperfectly, or which it leaves to external validators.

*Algebraic Architectures* develops a specification-first account of these judgments within *Compositional Intelligence*. It distinguishes the obligations of a task, the commitments of an architecture class, and the evidence available for a configured instance. The mathematical center is compositional preservation. An equivariant module contributes a system-level guarantee only along a path of compatible transformations, including representation, preprocessing, computation, and output. Analogous boundary questions arise for locality, finite memory, verified transitions, and effectful interfaces, although these properties have distinct mathematical semantics. An *Architecture Specification Catalog* is proposed as a modest decision instrument for recording such obligations and anticipating mismatches. Its usefulness depends on demonstrated improvements over existing design and evaluation practice, not on the descriptive richness of its records.

## 1. The architectural question

The preceding essays in *Compositional Intelligence* examine membership in formal and scientific worlds, generation under target types, and the preservation of structure under transformation. *Lambek Machines* develops typed linguistic composition. This essay addresses a complementary question concerning the systems that generate, transform, or act upon those artifacts. **Which properties of the task are preserved by the construction of the model, and which are contingent on training, integration, and subsequent validation?**

Consider two input arrays containing the same measurements. In one task, their order records time. In another, the order was introduced solely to serialize an unordered collection. Reordering changes the meaning of the first input and preserves the meaning of the second. An architecture that treats all positions as semantically significant introduces a dependence that the second task does not justify. Conversely, imposing permutation invariance on the first task destroys information its target depends upon. Neither tensor shape nor model capacity resolves the distinction.

This problem belongs to an extensive established literature. Group-equivariant networks, Deep Sets, graph networks, geometric deep learning, and categorical accounts of neural architectures already articulate connections from structure to computation [1–4, 11, 12]. Model Cards and the ML Test Score likewise precede the present proposal as instruments for documented assessment [13, 14]. The contribution pursued here is narrower. It is a way of **connecting prospective task obligations to the design of a complete system, then identifying what evidence would justify or defeat an architectural choice**. That proposed utility is open to empirical scrutiny.

An inductive bias has value only relative to the task. Incorporating a true symmetry might eliminate the need to learn it from examples. Enforcing a false symmetry might exclude the desired function altogether. Architecture selection consequently concerns the fit of a particular construction under declared assumptions, resource conditions, and tests of its intended use.

## 2. Task, architecture class, and configured system

The argument distinguishes three objects.

$$
\mathrm{TaskSpec}\;\longrightarrow\;\mathrm{ArchitectureType}\;\longrightarrow\;\mathrm{ArchitectureInstance}.
$$

The arrows represent a sequence of justified choices, not a function that uniquely identifies an optimal model.

**TaskSpec** states the object and output types, the relevant transformations, valid and invalid behavior, applicable constraints, operating domain, resource limits, and acceptance conditions. A task specification is itself a scientific claim. Treating spatial reflections as irrelevant, for example, would be an error for a parity-sensitive observable, regardless of the sophistication of the architecture selected to implement that assumption.

**ArchitectureType** designates a class of constructions with identified components and admissible configurations. Its commitments might include permutation-invariant aggregation, equivariant geometric operators, restricted message-passing neighborhoods, content-based attention, recurrent state, or a proof-checking interface. Class-level guarantees are conditional on the precise construction, its parameters, and the semantics of its components. A generic family name is insufficient to establish them.

**ArchitectureInstance** designates a trained and configured system, including its representations, parameters, inference procedure, numerical implementation, external memory, tools, validators, and deployment setting. A result obtained by one instance on a specified evaluation distribution does not establish a property of the entire architecture class. Conversely, a structural theorem concerning a class does not establish the scientific accuracy of an instance.

The distinction prevents three conflations. A task obligation is not evidence that any candidate satisfies it. An architectural guarantee is not a measurement of predictive adequacy. A successful measurement is not automatically a guarantee under every admissible input or system configuration. Architectural judgment is sound only to the extent that these claims retain their individual scopes.

## 3. Preservation under composition

An algebraic formulation becomes informative once the task specifies operations and transformations that its outputs must respect. Let a model implement

$$
f_\theta:X\longrightarrow Y,
$$

and let a group $G$ act on inputs and outputs through $\rho_X$ and $\rho_Y$. On an operating domain $D\subseteq X$ preserved by the relevant transformations, the equivariance obligation is

$$
f_\theta\bigl(\rho_X(g)x\bigr)=\rho_Y(g)f_\theta(x),
\qquad x\in D,\;g\in G. \qquad\text{(1)}
$$

Invariance is the special case with a trivial output action. Equation (1) asserts the agreement of two paths, first transforming the input and computing, or first computing and transforming the output. It presupposes compatible group actions and a justified identification of admissible transformations. If a predictor produces a probability distribution, the corresponding law is equality of the transformed output distribution and the distribution predicted from the transformed input. Independent draws need not coincide.

The compositional argument is direct. Suppose $f:X\to Y$ and $h:Y\to Z$ satisfy compatible equivariance laws. Then

$$
\begin{aligned}
(h\circ f)(\rho_X(g)x)
&=h\bigl(\rho_Y(g)f(x)\bigr)\\
&=\rho_Z(g)(h\circ f)(x).
\end{aligned} \qquad\text{(2)}
$$

Their composition inherits the transformation law. The conclusion depends on the shared transformation semantics at the intermediate interface. An encoder introducing arbitrary order, geometry-dependent preprocessing without the required equivariance, or an output head with incompatible transformation rules breaks the argument. A theorem about one neural module does not automatically extend to the complete pipeline that invokes it.

The same distinction applies to implementation. A construction might satisfy Equation (1) over real numbers while a finite-precision implementation exhibits numerical discrepancies. An implementation-level claim needs specified error tolerances, input regimes, and computational conditions. Tests identify implementation violations, while a finite suite of passing tests leaves the universal claim unproved.

Transformation preservation is not the sole structural obligation. Finite-radius message passing constrains local information flow. Recurrence constrains the manner in which information reaches later computations. A proof-producing system might expose transitions to a kernel that checks the resulting artifact. An instrument controller might mediate state-changing actions through independently checked preconditions. These cases involve graphs, state transitions, resources, or effects. They call for their own formal definitions; they are not instances of group equivariance by terminological extension.

This gives the architectural thesis its specific content. **Composition transports a guarantee only through compatible interfaces under their stated assumptions.** To evaluate a system, one must identify the relevant property, the components intended to preserve it, and the boundary beyond which the claim has no established force. The connection to *Functorial Consistency* is substantive. Both essays examine agreement along transformation paths, with the present essay locating the obligation in the construction and integration of model systems.

## 4. What qualifies as satisfaction

The notation $A\models S$ is useful only with a defined interpretation. Let $A$ denote an architecture class and $S_j$ a particular obligation. A class-level statement of satisfaction asserts, under declared assumptions, that every admissible member of that class meets the obligation.

$$
A\models S_j
\quad\Longleftrightarrow\quad
\forall\theta\in\Theta_A,\;S_j(f_\theta)
\quad\text{under the stated assumptions}. \qquad\text{(3)}
$$

Here $S_j(f_\theta)$ abbreviates a fully specified predicate with its own domain and quantifiers. Equation (3) records an intended interpretation, not a theorem establishing any particular architecture's compliance. The statement might hold for a restricted class despite failing for a wider family sharing its name.

Outside such a claim, evidence needs more careful language. **Architectural support** identifies a mechanism plausibly favorable to an obligation without proof for the entire class. **Empirical conformance** records that a particular instance met a test criterion under stated conditions. **Reviewed alignment** records an expert judgment and its unresolved assumptions. **Violation** identifies a counterexample, failed acceptance test, or demonstrated incompatibility. **Unassessed** indicates that the available evidence does not settle the obligation. These descriptions are not points on a common numerical scale. A mathematical proof and an empirical measurement might support the same obligation at different boundaries, and a discrepancy might reveal that the assumed boundary was wrong.

Architectural exclusion needs equally precise grounds. A candidate is *provably incompatible* if its specified construction cannot represent necessary task behavior under the relevant assumptions. A candidate might instead lack a mandatory class-level guarantee without being mathematically incapable of the task. A trained instance might fail a prespecified empirical threshold, while an untested family presents only a predicted risk. Conflating those cases converts a preference for structural design into a claim unsupported by the evidence.

Two familiar errors follow. **Underbias** leaves relevant task structure to be learned despite an available construction that preserves it. **Overbias** enforces a constraint incompatible with valid target behavior. Their diagnosis is task-relative. A network invariant to atom ordering might be suitable for molecular energy, while indiscriminate invariance to mirror reflection would be wrong for an observable that distinguishes handedness. The goal is justified structure, not maximal structure.

## 5. Worked architectural judgments

### 5.1 Unordered collections

Suppose $x=(x_1,\ldots,x_n)$ serializes a finite unordered collection, with repetitions retained if the task concerns a multiset. Reindexing by any $\pi\in S_n$ leaves the semantic object unchanged. For a scalar target the obligation is

$$
f_\theta(\pi x)=f_\theta(x). \qquad\text{(4)}
$$

The Deep Sets construction

$$
f_\theta(x)=\rho_\theta\!\left(\sum_{i=1}^n\phi_\theta(x_i)\right) \qquad\text{(5)}
$$

satisfies this invariance for every admissible parameter setting of its mathematical form [2]. The guarantee is limited to permutation invariance. It says nothing by itself about the approximation of every relevant invariant target, about the latent dimension needed for a specified collection size, or about generalization to larger collections. Work on the limitations of set-function representations makes these expressive qualifications explicit [3].

A sequence model with absolute positional embeddings lacks the corresponding class-level guarantee unless additional constraints enforce it. Such a model might nevertheless learn adequate invariance under a particular data distribution. The appropriate experiment permutes the same semantic inputs, measures prediction variation, and separately tests task accuracy and cardinality transfer. Attention without position-dependent information, with an invariant readout and compatible masking, belongs to a different architectural case. A comparison based only on the label *Transformer* would conceal the distinction.

If the application imposes a hard construction-level invariance rule, a candidate lacking that guarantee fails the specified selection condition pending an enforcing mechanism or proof. If the obligation is empirical invariance to a declared tolerance, both candidates are eligible for evaluation. Neither decision asserts expressive impossibility in the absence of a supporting argument.

### 5.2 Molecular energy and forces

Let $z$ contain atom identities and $R\in\mathbb{R}^{n\times3}$ coordinates arranged by rows. Let $P$ be a permutation matrix, $Q\in SO(3)$ a proper rotation, $b\in\mathbb{R}^3$ a translation, and $\mathbf{1}$ the all-ones column vector. For a scalar energy model $U$, a representative task law is

$$
U(Pz,\,PRQ+\mathbf{1}b^\top)=U(z,R). \qquad\text{(6)}
$$

For a vector force model $F\in\mathbb{R}^{n\times3}$, the corresponding transformation law is

$$
F(Pz,\,PRQ+\mathbf{1}b^\top)=PF(z,R)Q. \qquad\text{(7)}
$$

For conservative forces derived from the same differentiable energy, the specification also includes

$$
F(z,R)=-\nabla_R U(z,R). \qquad\text{(8)}
$$

The transformation laws and gradient relation are distinct obligations. A force model might satisfy Equation (7) while failing Equation (8). There is, however, a useful implication. If $U$ satisfies Equation (6) on a domain supporting the transformations and $F$ is *defined* by the negative gradient of $U$, orthogonality of $P$ and $Q$ and the chain rule yield Equation (7). An independently parameterized force head needs its own evidence for both claims. Even a construction satisfying all three equations has no general guarantee of chemical accuracy, numerical stability, or extrapolation to unfamiliar molecular configurations.

The choice of symmetry must reflect the observable. Proper rotation and translation laws are relevant to many atomistic prediction tasks. A parity-sensitive observable needs transformation rules that preserve its handedness dependence. Moreover, the E(n)-equivariant construction of Satorras and collaborators explicitly includes reflections [7]. That feature is appropriate for suitable targets and potentially excessive for others. The class-level symmetry of a named architecture must be examined against the actual output representation and scientific question. EquiformerV2 supplies another established architecture family for equivariant atomistic prediction [8], without resolving this task-specific comparison on its own.

The complete model boundary matters. Atom representations, coordinate conventions, neighborhood construction, feature preprocessing, energy and force heads, and numerical evaluation each enter the claim. A descriptor model with properly invariant features is not ruled out solely for lacking an equivariant neural backbone. What distinguishes the candidates is the guarantee of the complete construction, its empirical accuracy, its physical diagnostics, and the resources needed to establish those properties.

### 5.3 Long-context memory

Long-context tasks differ in the information that a system must preserve. Recovering an arbitrary distant identifier differs from computing an aggregate statistic, forecasting a temporal process, or maintaining a running summary. Their specifications must distinguish exact retrieval, approximate retrieval, selective updating, and latency under an intended sequence-length distribution.

Dense self-attention permits content-dependent interactions over accessible token representations, subject to the attention pattern and implementation. Selective state-space models such as Mamba propagate information through input-dependent state updates [5, 6]. Neither family description implies exact retrieval across arbitrary unbounded contexts. Evaluations need to vary target distance, distractor content, context length, query structure, and computational cost.

There is a precise limitation for a finite-memory regime. Suppose a sequential system must receive $n$ independent bits, retain no external storage, and subsequently answer a query for *any* one of those bits with certainty. Its internal state must distinguish all $2^n$ possible input strings. A state bounded to $b<n$ bits has fewer than $2^n$ possible values, hence cannot satisfy that requirement. The conclusion concerns exact universal retrieval under the stated state bound. It does not imply poor empirical performance on a particular distribution, or an identical impossibility for an idealized model with unbounded-precision states. Streaming tasks admitting compact sufficient statistics present a different architectural problem.

The relevant comparison is thus indexed by the memory operation and resource budget, not by a generic notion of long-range intelligence. Hardware, caching, state precision, external memory, and permitted error belong in the system description.

### 5.4 Scientific graphs and algorithmic processes

Scientific forecasting might represent spatial dynamics on a mesh, graph, field, or hybrid discretization. Edges might denote physical interactions, geometric proximity, numerical adjacency, or learned connections. This distinction affects the validity of a claimed relational inductive bias. The GraphCast system illustrates the empirical value of graph-based computation for medium-range global weather forecasting [9]. Its evaluated forecast skill does not establish an unconditional conservation law or guaranteed transfer to arbitrary discretizations.

An architectural judgment must connect the intended representation to the scientific tests it motivates. Depending on the task, these include extended rollout error, conservation diagnostics, behavior under changed mesh resolution, and performance under defined distribution shifts. The existence of graph structure does not settle any of those outcomes. A finite-depth local message-passing construction also has a bounded communication radius unless augmented with longer-range connections, global features, additional depth, or other communication mechanisms.

Neural algorithmic reasoning brings a related distinction into view [10]. Training-size success is separate from correctness of transitions, preservation of invariants, and extrapolation to larger problems. In proof-oriented systems, a model proposing a proof step and a trusted kernel validating it have different roles. A completed kernel check warrants a claim relative to the kernel's rules and trusted base. It does not establish that the learned proposal mechanism is correct in general.

### 5.5 Scientific agents and effects

An experimental agent moves beyond the semantics of a static input-output predictor. Its behavior interacts with instrument state, permissions, tool responses, and observations of a changing physical process. A plausible protocol description is insufficient evidence of permitted or correct execution. The relevant design includes state representation, action preconditions, effect tracking, independently mediated operations, and post-action reconciliation.

For example, a transfer instruction might refer to a sample identity, a permitted instrument state, a target volume, and a subsequent measurement. A tool gateway might reject an unauthorized command, while an observation record might establish whether the intended transfer occurred. The first check concerns authorization; the second concerns physical state. Neither alone establishes the validity of a downstream scientific conclusion. These distinct predicates belong to the architecture of the full system, not to its language-model backbone in isolation.

This is the limit of the symmetry example and an extension of its central discipline. A model's mathematical property, an external controller's enforcement rule, and an observation's evidentiary status occupy different interfaces. Their composition needs explicit semantics and verification appropriate to each obligation. The presence of a validator alone establishes no universal architectural guarantee.

## 6. The place of algebra and prior work

Established architectural traditions explain much of the structural reasoning developed above. Deep Sets supplies an invariant construction [2], with important representational limitations examined by Wagstaff and collaborators [3]. Group-equivariant convolutional networks and geometric deep learning develop symmetry-guided model design [1, 12]. Graph networks articulate relational inductive bias [4]. Attention-based Transformers, selective state-space models, equivariant atomistic networks, graph-based scientific forecasting, and neural algorithmic reasoning each provide further evidence of task-dependent architectural commitments [5–10].

Categorical deep learning is especially important prior work for the present title. Gavranović and collaborators develop a broader algebraic theory linking architectural constraints and implementations [11]. This essay neither replaces that program nor proves a new universal characterization of neural architectures. Its mathematical result about compatible equivariant maps is elementary, and its wider discussion of state and effects is not given a common categorical semantics here.

The proposed distinction concerns the **epistemic use of architectural structure**. A construction identifies a conditional property, a system integration establishes whether the conditions continue to hold, and evidence about an instance establishes further task-specific judgments. Model Cards and ML testing methodologies already provide reporting and assessment practices [13, 14]. The proposed extension is prospective and task-indexed. It puts obligations, predicted counterexamples, and exclusion grounds before candidate evaluation, preserving the assumptions connecting each decision to the evidence. The existence of the proposed record alone establishes neither originality in model documentation nor improved decisions in practice.

## 7. A specification as a decision instrument

The proposed *Architecture Specification Catalog* is a compact record of **task–candidate–obligation judgments**. Its purpose is to distinguish four outcomes that ordinary architectural descriptions might obscure. A design might satisfy a construction-level law, support it without a guarantee, fail an empirical acceptance test, or remain unassessed. The same family might occupy different categories for different obligations, and one assembled system might lose a property certified for a constituent module.

For practical use, a record needs only the task domain, system boundary, explicit obligation, candidate construction, acceptance rule, predicted mismatch, validator, resource constraint, and evidence provenance. The optional notation

$$
\mathrm{ArchitectureSpec}=(O,T,\Sigma,L,G,R,\Phi,E,V) \qquad\text{(9)}
$$

indexes object types, transformations, operations, laws, geometry, resources, interfaces, effects, and validators. It is a descriptive schema, **not** a mathematical signature with demonstrated completeness or uniform semantics. Each obligation must be formulated individually. Inflating the notation beyond the distinctions actually used in a decision would weaken the essay.

Consider the unordered-collection example. Under an explicit requirement for a class-level permutation-invariance guarantee, a model built from invariant aggregation qualifies on that dimension, subject to the full implementation boundary. An unconstrained position-dependent sequence model does not qualify on that dimension until an enforcing mechanism or proof is supplied. Under an empirical tolerance requirement, the second candidate remains eligible for permutation stress testing. The specification changes the *grounds of selection*, without claiming that all invariant models are accurate or that unconstrained models lack the ability to learn the target.

A worthwhile record makes a falsifiable prediction prior to evaluation. It might identify sensitivity to irrelevant permutations, inconsistency of an independent force head, inaccessible information under a constrained memory budget, or absence of independently checked effects. Its failure prediction must be specific enough to test. A record describing every model as broadly suitable, or repeating an already observed failure, contributes no prospective architectural judgment.

## 8. How the proposal would be tested

The principal empirical question is whether such records improve decisions beyond informed architecture selection and established assessment methods. Persuasive examples do not answer it.

A credible study would specify tasks, candidate constructions, mandatory and optional obligations, and anticipated failures before inspecting the held-out evaluations. It would compare selection using ArchitectureSpec against expert judgment supplied with the same information and budget, selection based on development-set performance, and a conventional structured checklist. Training budgets, evaluator access, model availability, and computational constraints would need to be comparable for the relevant causal claims. Where equalization is impossible, the evaluation would report the resulting limitation.

Meaningful outcomes include correctness of prospective mismatch predictions, detection of violated assumptions, quality of the chosen system under predetermined acceptance criteria, and the cost of producing and maintaining the records. Structural theorems and empirical observations require distinct adjudication protocols. A mathematically established invariance law is assessed through its proof and implementation assumptions, while generalization and runtime cost remain empirical questions. Reusing the same examples to devise and then validate a checklist would inflate its apparent value.

The proposal loses its broad rationale if it fails to distinguish unsuitable candidates, repeatedly recommends the same construction without task-specific justification, provides no predictive advantage over expert assessment, or incurs record-keeping cost exceeding its decision value. It might still be useful in a narrower domain with unusually precise task laws. The present essay reports no experiment demonstrating an improvement and makes no universal architecture-ranking claim.

Two objections delimit the contribution. First, large general-purpose models might outperform specialized architectures despite lacking their explicit guarantees. Empirical superiority is compatible with the framework; a hard construction-level requirement and an optional preference for efficiency lead to different selection decisions. Second, many tasks have contested or incomplete specifications. In those cases, the specification must record disagreement without promoting an uncertain task assumption into a theorem. No record resolves a task that lacks adequate definition.

## 9. Conclusion. From structure to warrant

The architectural question has a compositional form. Task semantics establish relevant obligations. A model construction secures some conditional properties and leaves others to training or observation. Integration preserves a property only across compatible interfaces. Evaluation then supplies evidence about a particular configured system under declared conditions. Confusing any two of these stages produces an unjustified architectural claim.

This account fits the trajectory of *Compositional Intelligence*. Earlier essays examine the membership, generation, and transformation of artifacts. *Algebraic Architectures* asks what a system's design establishes about the processing of those artifacts. *Quantitative Curry–Howard* turns to the warrant associated with particular outputs, including scores, uncertainty, validation status, and repair. Architecture-level guarantees and output-level evidence remain different obligations, especially in systems that act upon the world they are meant to describe.

The proposed catalog has a limited, testable role. If it changes an architecture decision, anticipates a consequential failure, or selects a better validator under a fair comparison, it earns its place. If it relabels existing engineering judgment without improving that judgment, the appropriate conclusion is to retain the underlying structural reasoning and discard the additional apparatus. The durable claim of this essay is the need to track **what architecture preserves, under which assumptions, across which system boundaries, and with what evidence**.

## Appendix. Illustrative obligation record

The following example illustrates the separation of a task obligation from an evidence claim. Its empty evidence fields signify an unevaluated construction, not favorable results.

```yaml
specification_id: atomistic_energy_force_v1
system_boundary:
  components:
    - coordinate_preprocessing
    - model
    - energy_head
    - force_head
  inference_configuration: to_be_declared

task:
  inputs: [atom_identities, coordinates]
  outputs: [scalar_energy, vector_forces]
  domain: to_be_declared
  resources: [latency_budget, memory_budget, hardware_profile]

candidate:
  architecture_type: equivariant_graph_model
  instance_id: null

obligations:
  - id: scalar_energy_symmetry
    predicate: energy_invariant_under_joint_relabeling_and_SE3
    evidence_claims: []
    assessment: unassessed
  - id: force_equivariance
    predicate: force_equivariant_under_joint_relabeling_and_SE3
    evidence_claims: []
    assessment: unassessed
  - id: conservative_force_consistency
    predicate: force_equals_negative_energy_gradient
    evidence_claims: []
    assessment: unassessed
  - id: predictive_accuracy
    predicate: prespecified_error_on_held_out_geometries
    evidence_claims: []
    assessment: unassessed

prospective_tests:
  - atom_permutation_test
  - proper_rotation_and_translation_test
  - energy_force_gradient_consistency_test
  - held_out_geometry_evaluation
  - latency_and_memory_measurement

anticipated_risks:
  - non_equivariant_preprocessing
  - inconsistent_independent_force_head
  - unfamiliar_geometry_distribution

decision: evaluation_pending
```

Evidence subsequently associated with an obligation would identify the claim, scope, assumptions, evaluator, source, and proof or test protocol. Changes in preprocessing, outputs, numerical configuration, or deployment would trigger reassessment of affected claims.

## References

1. Bronstein, M. M., Bruna, J., Cohen, T., & Veličković, P. (2021). [*Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges*](https://arxiv.org/abs/2104.13478). arXiv:2104.13478.
2. Zaheer, M., et al. (2017). [*Deep Sets*](https://proceedings.neurips.cc/paper_files/paper/2017/hash/f22e4747da1aa27e363d86d40ff442fe-Abstract.html). *Advances in Neural Information Processing Systems*, 30.
3. Wagstaff, E., Fuchs, F., Engelcke, M., Posner, I., & Osborne, M. A. (2019). [*On the Limitations of Representing Functions on Sets*](https://proceedings.mlr.press/v97/wagstaff19a.html). *Proceedings of Machine Learning Research*, 97, 6487–6494.
4. Battaglia, P. W., et al. (2018). [*Relational Inductive Biases, Deep Learning, and Graph Networks*](https://arxiv.org/abs/1806.01261). arXiv:1806.01261.
5. Vaswani, A., et al. (2017). [*Attention Is All You Need*](https://proceedings.neurips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html). *Advances in Neural Information Processing Systems*, 30.
6. Gu, A., & Dao, T. (2024). [*Mamba: Linear-Time Sequence Modeling with Selective State Spaces*](https://proceedings.colm.cc/paper_files/paper/2024/hash/12564fe3900e4e2cefb52d4b4ad40625-Abstract-Conference.html). *Conference on Language Modeling*.
7. Satorras, V. G., Hoogeboom, E., & Welling, M. (2021). [*E(n) Equivariant Graph Neural Networks*](https://proceedings.mlr.press/v139/satorras21a.html). *Proceedings of Machine Learning Research*, 139, 9323–9332.
8. Liao, Y.-L., Wood, B., Das, A., & Smidt, T. (2024). [*EquiformerV2: Improved Equivariant Transformer for Scaling to Higher-Degree Representations*](https://proceedings.iclr.cc/paper_files/paper/2024/hash/ab12e8f3443c1a789f595b18d8c597b4-Abstract-Conference.html). *International Conference on Learning Representations*.
9. Lam, R., et al. (2023). [*Learning Skillful Medium-Range Global Weather Forecasting*](https://doi.org/10.1126/science.adi2336). *Science*, 382(6677), 1416–1421.
10. Veličković, P., & Blundell, C. (2021). [*Neural Algorithmic Reasoning*](https://pmc.ncbi.nlm.nih.gov/articles/PMC8276006/). *Patterns*, 2(7), 100273.
11. Gavranović, B., et al. (2024). [*Position: Categorical Deep Learning Is an Algebraic Theory of All Architectures*](https://proceedings.mlr.press/v235/gavranovic24a.html). *Proceedings of Machine Learning Research*, 235, 15209–15241.
12. Cohen, T., & Welling, M. (2016). [*Group Equivariant Convolutional Networks*](https://proceedings.mlr.press/v48/cohenc16.html). *Proceedings of Machine Learning Research*, 48, 2990–2999.
13. Mitchell, M., et al. (2019). [*Model Cards for Model Reporting*](https://doi.org/10.1145/3287560.3287596). *Proceedings of the Conference on Fairness, Accountability, and Transparency*, 220–229.
14. Breck, E., Cai, S., Nielsen, E., Salib, M., & Sculley, D. (2017). [*The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction*](https://doi.org/10.1109/BigData.2017.8258038). *IEEE International Conference on Big Data*.
