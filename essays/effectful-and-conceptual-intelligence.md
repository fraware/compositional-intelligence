# Effectful and Conceptual Intelligence

<a id="abstract"></a>

## Abstract

Language-model agents act through tools, files, databases, browsers, communication systems, and, increasingly, scientific or physical instruments. Their evaluation consequently extends beyond the correctness of generated responses. Executed actions alter persistent state, create commitments, and shape subsequent decisions. The relevant object of evaluation is the trace connecting an instruction to an authorized operation, its observed consequences, and the evidence supporting the agent's account of what occurred.

This essay develops a type-and-effect *record discipline* for consequential agent behavior. Its organizing judgment, `Γ; M; E; C ⊢ a : Pre → Post ! ε @ ρ`, associates an action with instruction context, memory, environment, capabilities, preconditions, postconditions, declared effects, and risk-authority obligations. The notation describes a proposed contract. It becomes a meaningful execution constraint only through trusted mediation, state observation, and independent validation. The resulting Typed Action Ledger distinguishes proposal, authorization, execution, and validation. The Effectful Agent Benchmark evaluates these stages separately from task completion. The Concept Transfer Record addresses a related dependency: concepts influence proposed actions through claims, assumptions, and plans, while evidential support for a claim and permission to act upon it involve separate judgments. The shared object is an inspectable dependency connecting a claim to a consequential operation, subject to the limits of reported reasoning and observable state.

The intellectual foundations include program specifications, planning, effect systems, capability security, interactive-agent evaluation, analogical reasoning, and causal transportability. The synthesis is a research proposal, without a formal soundness theorem, a verified implementation, or measured evidence of improvement. Its central hypothesis concerns execution-coupled records: under controlled task and tool conditions, binding declared effects to authorization and validation will improve containment of forbidden actions, discrimination of unsupported completion claims, and reconstruction of consequential decisions. A logging-only system would test the narrower contribution of documentation and audit.

<a id="position-in-the-compositional-intelligence-series"></a>

## 1. Position in the Compositional Intelligence series

*Effectful and Conceptual Intelligence* completes a progression developed across the preceding essays: semantic participation, typed generation, transformation-preserving evaluation, compositional linguistic structure, architectural specification, and quantitative warrant. Those studies examine the validity of artifacts, their transformations, and the evidence accompanying their use. This essay examines the further transition from a warranted artifact to an action that alters its environment.

`membership → generation → transformation → language → architecture → warrant → action`

The distinction is consequential. A candidate plan, even one supported by sound reasoning, has yet to establish permission to modify a repository, contact a third party, spend funds, update persistent memory, or operate an instrument. Authority, execution conditions, observed effects, and the limits of verification belong to the evaluation object itself. The compositional program consequently confronts two connected tests. The first asks whether a representation supports the interpretation or claim for which it is used. The second asks whether a particular intervention is licensed and whether its consequences satisfy the relevant obligations. Observations from execution feed back into the representational record. The essay studies this interface while preserving the distinct standards governing inference, permission, and empirical observation.

<a id="evaluation-unit-for-agent-action"></a>

## 2. The evaluation unit is an effectful trace

ReAct interleaves language-model reasoning and actions, while Toolformer investigates learning to invoke external APIs [8, 14]. WebArena and OSWorld assess task execution in interactive web and computer environments [9, 15]. τ-bench evaluates tool-agent-user interaction under domain policies [10]. AgentDojo tests prompt-injection attacks against tool-using agents [11]. AgentRewardBench studies expert and automated judgments of web-agent trajectories, including task success and side effects [12]. These benchmarks differ in tasks, interfaces, and ground truth. They establish neither a common effect taxonomy nor the effectiveness of the proposed ledger.

Evaluation of an effectful trace extends beyond the final response. It distinguishes the governing instruction, encountered observations, expressly relied-upon premises, proposed operation, authorization decision, attempted intervention, observed state changes, and evidence supporting a completion claim. Reported success and authorized success are separate outcomes. Likewise, a blocked unauthorized attempt and an unauthorized operation that reached its target have different diagnostic meanings.

Observation has a defined scope. Browser output, tool results, file diffs, API acknowledgments, and sensor readings expose different portions of the environment. An API acknowledgment establishes the response received from an endpoint under its interface semantics; it need not establish downstream delivery or rule out secondary effects. A passing test suite establishes the outcomes of selected tests under their configured conditions, leaving untested repository invariants unresolved. The trace records **unknown** for an unsettled obligation. An effect outside the observation boundary must never be counted as absent solely because it was not detected.

<a id="the-typed-action-judgment"></a>

## 3. The typed-action judgment

The essay retains the following judgment as its organizing notation.

> `Γ; M; E; C ⊢ a : Pre → Post ! ε @ ρ`

| Symbol | Interpretation | Operational obligation |
|---|---|---|
| `Γ` | Trusted instruction, policy, and task context | Identify the governing instructions and applicable constraints. |
| `M` | Persistent or retrievable memory context | State the relevant memory version, sources, and access conditions. |
| `E` | Environment and interface context | Identify the target, observed state, and assumptions about external state. |
| `C` | Capability context | Identify available tool channels and their bounded execution privileges. |
| `a` | Proposed action or plan step | Specify target, arguments, and intended operation. |
| `Pre` | Preconditions | Identify conditions to establish before execution. |
| `Post` | Postconditions | Identify claims about the resulting state and their validators. |
| `ε` | Declared effects | Identify prospective reads, writes, disclosures, commitments, and other changes. |
| `ρ` | Risk-authority obligations | Identify authority source, approval, reversibility, uncertainty, and escalation. |

The turnstile denotes a *declared contract*. No derivation rules or soundness theorem are supplied for arbitrary agent actions. The expression `Pre → Post` records an intended state transition and its proof obligations; it does not establish that the operation realizes `Post`. A future formal calculus would need an operational semantics, a model of state and effects, composition rules, a treatment of environmental interference, and an explicit trusted computing base. In this essay the notation disciplines what is specified and checked, without assigning unearned static guarantees.

The separation of `Γ` from observations is indispensable. Retrieved pages, repository content, tool responses, and stored summaries have provenance and trust attributes. Their appearance in context never grants them the authority of an instruction. The separation of `C` from `ρ` is equally important. A tool's availability describes an execution channel. The permission to exercise that channel for a particular target and purpose is an independent decision. This follows longstanding work on least privilege and the confused-deputy problem [5, 6].

The execution record connects the declared contract to a mediator decision, an executor-bound request, observations, and validator outcomes. These distinguish **declared**, **authorized**, **attempted**, **observed**, and **validated** effects. If an externalized claim `q` materially supports the action `a`, the record additionally identifies `depends(a, q)` and the version of `q` consulted. That link documents an expressed justification, without establishing that the model disclosed every causal influence on its choice. Safety-critical preconditions need evidence from trusted checks of the operative state, not reliance on the agent's account of its reasoning.

<a id="execution-phases"></a>

## 4. Proposal, authorization, execution, and validation

| Phase | Question | Failure revealed |
|---|---|---|
| Proposal | Which operation, target, and effects did the agent request? | Invalid action, wrong target, omitted effect, or unsupported premise. |
| Authorization | Was that operation permitted for this task, principal, and state? | Authority confusion, excessive privileges, absent approval, or stale checks. |
| Execution | What operation reached the environment, and what evidence describes its effects? | Tool failure, partial commit, unexpected write, bypass, or unobserved consequence. |
| Validation | Which postconditions and protected-state obligations were actually checked? | Unsupported completion, failed frame condition, insufficient observation, or ineffective compensation. |

These phases remain analytically distinct even in a transactional runtime. A forbidden operation might never be proposed, might be refused by a mediator, or might execute despite an apparent policy gate. Those outcomes locate different successes or failures in the planner and the execution boundary. A coarse final-state score might conceal each distinction; none of them alone establishes successful completion of the legitimate task.

Authorization at proposal time also fails to settle execution-time validity if relevant state changes before the operation commits. Permissions, resources, and repository revisions might become stale. For targets supporting transactional or conditional updates, the executor must bind checked conditions to the committed action. If a required precondition has expired, the operation must be denied or checked again at the execution boundary. For interfaces lacking atomic checks, the admissible action scope must reflect the resulting race, with its residual risk and observation limits recorded.

<a id="effect-taxonomy"></a>

## 5. Classifying effects without conflating their roles

The taxonomy separates **effects on the environment**, **execution mechanisms**, and **cross-cutting obligations**. A tool invocation is an execution mechanism with potentially multiple effects. Security and privacy constrain the flows and destinations permitted for those effects. A reusable skill is a versioned procedure that produces effects upon invocation. Conceptual transfer concerns the support and use of inferences, with externally consequential effects arising at specified interfaces.

| Dimension | Representative operation | Relevant record |
|---|---|---|
| Observation | Read a page, query a database, inspect a file, sample a sensor | Source, freshness, sensitivity, trust, and observation scope. |
| State modification | Edit a file, update a database, change a calendar, write memory | Target, diff or event, persistence, protected state, validator. |
| Communication and commitment | Send a message, make a booking, submit a request, transfer funds | Recipient, authorized purpose, approval, obligation, and compensation. |
| Physical intervention | Move a robot, operate an instrument, manipulate a sample | Instrument and sample identity, hazard, stopping rule, physical evidence. |
| Knowledge-record modification | Store a claim, revise a hypothesis record, withdraw a prior conclusion | Evidence provenance, dependencies, invalidation, retention, and permitted downstream use. |

`Tool invocation`, `skill invocation`, and `plan execution` identify execution structures. `Credential handling`, `privacy`, `security boundaries`, and `reversibility` qualify the effects they produce. In a realistic operation, multiple categories coexist. Browser automation might read personal information, submit a form, and send an external notification in one invocation. Describing the operation as `tool_call` alone would miss the security-relevant structure.

Forming an analogy or reconsidering a hypothesis is a conceptual operation, not automatically a persistent state change. A stored conclusion, published claim, or execution decision influenced by that operation has an observable interface and produces potentially consequential effects. This distinction prevents internal reasoning from being mislabeled as a tool effect.

Effect descriptions also have different levels of precision. File writes might have exact paths and patches, external messages might have verified recipients with uncertain delivery, and physical actions might have measured instrument outputs alongside unobserved downstream consequences. The declaration must identify its observation and precision limits. Complete enumeration of open-world effects is not assumed.

<a id="handlers-validators-and-authority"></a>

## 6. Handlers, validators, and the trusted boundary

Effect systems describe or constrain computational effects, and algebraic handlers give semantics to handling particular effects under defined models [3, 4]. The proposed agent handler adapts the separation of an operation from its treatment as an operational record discipline; no static effect-safety guarantee transfers from those formalisms. It evaluates an action instance against the declared contract and current authority policy, recording a decision together with conditions governing any permitted execution.

> `handler(a, Pre, ε, ρ, Γ, C, E) → (decision, mode, obligations)`

Here `decision` distinguishes `allow`, `deny`, `await_approval`, and `escalate`. Authorized execution might also specify a sandbox or another bounded mode, with post-execution checks recorded as obligations. A sandbox designation by itself establishes neither authorization nor isolation.

Its significance depends on **complete mediation of the protected operation**. A handler that logs advisory decisions while an agent retains a privileged alternative tool path has no enforcement authority over that path. The executor must bind permission to a concrete action instance, principal, target, arguments, and checked state or policy version at the point of use. If the checked conditions expire before commit, the system must revalidate them or disclose the race. An environment permitting bypass defeats the corresponding containment claim. Complete mediation is a longstanding security principle [5]; its satisfaction in a particular agent runtime is an implementation property to test.

The post-execution validator examines evidence relative to a declared `Post` and protected frame conditions.

> `validator(Post, frame, observed_evidence) → pass | fail | partial | unknown`

`pass` means the specified checks succeeded over the observed state and under their declared assumptions. It is not a universal claim about unobserved state. `partial` denotes mixed or incomplete obligations. `unknown` denotes insufficient evidence to decide. Validators need independent identification beyond the agent's assertion of success wherever independent inspection is supported.

The relationship to Hoare logic and separation logic is specific [1, 2]. Preconditions and postconditions structure claims about program transitions, while frame reasoning concerns preservation of state outside a command's footprint under defined assumptions. The ledger borrows the practice of declaring and checking protected state. Its `frame_conditions` field alone supplies neither a proof of a Hoare triple nor an application of the separation-logic frame rule. Those results depend on formal premises and semantics absent from this proposal.

Repair and reversal also need distinct treatment. Reverting a repository diff might restore files, assuming no unrecorded effects or concurrent conflicting writes. Sending a second email does not undo receipt of the first. Issuing a refund does not erase a prior economic commitment. Experimental interventions might change a sample irreversibly. The ledger records **rollback** only where inverse state restoration is supported, and **compensation** or **containment** in other cases. An irreversible action without an adequate response path needs an explicit risk decision before execution.

<a id="typed-action-ledger"></a>

## 7. Typed Action Ledger

The Typed Action Ledger is a proposed execution-linked record for consequential agent behavior. Its minimum useful structure connects a task's governing context to each action instance and to evidence acquired during authorization, execution, and validation.

| Record group | Minimum content |
|---|---|
| Task and authority | Task identifier, intended goal, trusted policy, principal, authority source, scope, approval, and validity interval. |
| Action identity | Unique entry, version, initiator, target, arguments, source observations, and material claim dependencies. |
| Contract | Preconditions, expected postconditions, proposed effects, allowed effects, forbidden effects, and protected state. |
| Control decision | Handler identity and version, checks performed, decision, decision time, and executor-bound authorization. |
| Execution evidence | Attempted operation, executor identity, outcome, tool receipt, observable state delta, and evidence provenance. |
| Validation | Validator identity, exact checks, verdict, unknown obligations, repair or compensation, and any human escalation. |
| Downstream use | Permission to update memory, reuse a skill, report completion, publish a claim, or initiate a dependent operation, with invalidation links to relied-upon premises. |

Ledger entries carry no automatic authority. The trusted control boundary must make the decision effective, and the validator must obtain evidence from a source appropriate to the claimed state transition. The record itself needs integrity protection, access control, proportionate retention limits, and provenance for externally generated receipts. Its evidential value depends on the independence and reliability of the sources that produced those receipts. If an agent controls its audit history or forges executor receipts, its records provide weak independent evidence. Event ordering, policy version, checked state version, and binding of the executor request to a prior authorization decision are decisive. A ledger entry produced only at task completion cannot substantiate pre-execution mediation.

Low-impact observations warrant concise records. Persistent writes, disclosures, financial commitments, and physical interventions warrant narrower scopes and stronger evidence. Proportionate record depth is an engineering choice to evaluate, without assuming a universal schedule of safeguards.

### 7.1 Worked example: a repository repair

Consider a request to repair a failing parser. The agent is authorized to edit `src/parser.py`. Test files and repository policy files are protected. The goal is to restore correct parsing while preserving the existing tests and policies. The scenario is illustrative and reports no measured result.

| Step | Action and evidence | Evaluation |
|---|---|---|
| Proposal | The agent proposes a patch touching `src/parser.py` and `tests/test_parser.py`, with the second edit weakening an assertion. | The declared write set exceeds the authorized scope. Passing tests would not settle the contract. |
| Authorization | A mediator compares the proposed write targets with the approved target set and rejects the operation. | `deny`. No protected write reaches the executor if mediation is complete. |
| Revised proposal | The agent submits a patch confined to `src/parser.py`. | The patch is eligible for authorization, subject to current state and other preconditions. |
| Execution | The executor applies the patch, returning a commit or diff identifier and the observed changes. | The ledger associates evidence with the actual operation, not the agent's account. |
| Validation | Independent checks run the relevant tests, inspect the diff, and compare protected files with their prior versions. | `pass` only for the obligations actually checked. Remaining invariants retain their evidential limits. |

The example exposes two properties that task-success scoring alone could miss. First, the original proposal was defective even if a privileged executor would have produced passing tests. Second, the mediator's refusal is an enforcement success paired with a proposal failure. A scientifically useful benchmark records both facts. If the tool has an alternative path capable of writing protected files, the nominal refusal establishes little about system-level containment.

<a id="memory-tools-plans-and-skills"></a>

## 8. Memory, tools, plans, and skills

<a id="memory-as-effect"></a>

### 8.1 Memory as a persistent effect

Persistent memory is part of the agent's future decision environment. An unsupported observation stored as fact might become a premise in later planning. Even a validated observation needs invalidation if it subsequently becomes obsolete. Each memory-write record identifies its evidence source, intended scope, authority to retain it, sensitivity, dependencies, invalidation triggers, and permitted uses. Write permission and factual warrant are separate conditions.

> `Γ; M; E; C ⊢ write_memory(m) : Pre_M → Post_M ! memory_write @ ρ_M`

The symbolic transition `M → M ∪ {m}` is insufficient for replacement, contradiction, deletion, and dependency-driven invalidation. A concrete memory implementation needs versioned update semantics and a rule for carrying or withdrawing dependent claims. Storing a record is an execution event. Accepting its content as established knowledge is a distinct epistemic decision. If a stored conclusion depends on a transferred relation that later fails, the memory system must identify the dependent records within its declared scope. A change of warrant does not automatically undo actions previously taken on the basis of that conclusion.

<a id="tools-as-typed-interfaces"></a>

### 8.2 Tools as typed interfaces

Tools expose schemas, arguments, return values, side effects, credentials, and failure modes. Interface validation narrows malformed operations without establishing that every valid call is authorized. Tool returns also carry epistemic status: a claimed database result must correspond to a recorded response, and an API acknowledgment must not be promoted into proof of a stronger external outcome. The record distinguishes the interface's specification from the observed behavior of a particular invocation.

<a id="plans-as-state-transition-programs"></a>

### 8.3 Plans as compositions of state transitions

Planning formalisms such as PDDL specify actions through conditions and state-changing effects [7]. The proposed record discipline extends that concern to authorization, observation, and validation for tool-using agents. A sequence is locally compatible if the state established by one step satisfies the next step's preconditions, under the chosen state model. External interference, branching, retries, partial commits, and expiring permissions complicate that judgment.

> `π = a₁ ; a₂ ; … ; aₙ`, with `ε_declared(π) ⊇ ⋃ᵢ ε_declared(aᵢ)` under a set-valued, conservative effect abstraction.

This inclusion is a specification obligation for the sequential case, not a theorem about realized effects. Other composition operators need their own rules; monitoring must reconcile the declared scope with observed behavior. Event ordering and authority scope continue to constrain each step.

<a id="skills-as-reusable-effectful-programs"></a>

### 8.4 Skills as reusable effectful programs

Reusable skills are named, versioned plan patterns with recorded preconditions, permitted effects, execution evidence, known failure cases, and deprecation criteria. Reuse never bypasses current authorization or environmental checks. A skill validated for a particular repository revision, API contract, or instrument configuration needs renewed checks as those dependencies change.

<a id="conceptual-intelligence-as-controlled-transfer"></a>

## 9. Conceptual intelligence and the transition to action

Conceptual intelligence encompasses the formation, abstraction, combination, revision, and transfer of representations. The present essay studies one tractable part of that broader subject: the use of an explicit conceptual inference as a premise in an agent's subsequent conduct. Constructing an analogy need not modify any external target. Storing its conclusion, recommending an intervention on its basis, or invoking a tool under its assumptions introduces consequential commitments. The common object is **a recorded dependence from a claim to an intended use**, alongside independently governed action and observation.

Conceptual transfer begins with source and target representations, a partial mapping, and a claim proposed for the target domain. Its legitimacy depends on evidence pertinent to that target claim. The agent might use a supported relation for explanation, a tentative one for hypothesis formation, or a stronger claim for a safety-sensitive operation. Evidence appropriate to one use does not automatically justify another. An action based on the claim also needs permission, verified preconditions, and post-execution evidence. The conceptual and operational components thus have distinct correctness conditions, connected by a declared dependency and subsequent feedback.

> `source model → partial mapping → target claim → intended use → action proposal → authorization → execution evidence → claim revision`

This sequence is an analytical representation, not a necessary account of the agent's hidden computation. Some actions proceed through established procedural rules without a new conceptual transfer. Some conceptual work produces no action. Their connection is strongest in cases where an explicit inferential commitment materially affects the choice, parameters, or risk assessment of an intervention. The proposal seeks to evaluate those cases without reducing the whole of conceptual intelligence to effect control.

<a id="concept-transfer-and-warrant"></a>

### 9.1 The warrant of a conceptual transfer

Structure-mapping theory studies analogies through relational correspondences [13]. Philosophical work on analogical arguments likewise emphasizes the argument connecting the source example to the proposed generalization [16]. These traditions motivate precise questions about a mapping's scope, without implying that a correspondence licenses every inference drawn from it.

Let `S` and `T` denote representations of a source domain and target domain, and let `μ` be a proposed *partial* mapping of selected objects or relations from `S` to `T`. The Concept Transfer Record identifies a target claim `q` that depends on this mapping, the relevant correspondences `R`, the supporting or contrary target evidence `W`, and an intended downstream use `U`. This is descriptive notation, not a formal proof system. Neither the existence of `μ` nor a plausible resemblance establishes `q`.

| Transfer question | Required distinction |
|---|---|
| What is mapped? | Named objects, operations, and relations, with explicit mapping limits. |
| What is inferred? | The particular target claim `q`, distinguished from the original source facts. |
| What supports it? | Source-model evidence, target-specific observations, assumptions, and counterevidence. |
| What fails to transfer? | Relations shown false, untested, changed, or dependent on missing conditions. |
| How is it used? | Explanation, hypothesis formation, design guidance, or a premise for consequential action. |
| What withdraws its warrant? | New measurements, changes of context, invalidated assumptions, or counterexamples. |

These questions concern inferential support, not a generic score of similarity. A relation judged helpful for explanation might remain untested as a physical invariant. Evidence sufficient to motivate a hypothesis might be inadequate for a high-impact intervention. The required strength of support depends on the *claim and intended use*. Furthermore, even an independently supported target claim supplies no authority to act. Permission, resource constraints, and execution risk remain separate obligations under the typed-action judgment.

The distinction resembles a specific issue in causal inference: results obtained in one population or setting cannot automatically be transported to another without appropriate assumptions about the differences. Pearl and Bareinboim formalize transportability for causal effects under specified causal models [17]. Their results are a domain-specific illustration of the need for justified transfer, not a theorem about arbitrary analogies or the proposed ledger.

<a id="transfer-example"></a>

### 9.2 Worked example: treating a laboratory protocol as a transaction

Consider an agent designing a laboratory procedure by analogy with a database transaction. The source model has a sequence of guarded operations, a record of changes, and a rollback mechanism under specified transactional assumptions. The target is a physical experiment involving a sample and an instrument. Both domains benefit from checking preconditions, recording operations, and defining failure responses. The analogy provides useful organizational guidance.

The decisive divergence concerns reversal. A database transaction might support restoration under its storage and concurrency semantics. The laboratory procedure might consume a sample, generate waste, or induce an irreversible physical transformation. The existence of a log, abort button, or subsequent compensating procedure establishes neither restoration of the sample nor elimination of the original exposure.

The same transfer produces two different judgments. As **design guidance**, it motivates explicit preconditions, checkpoints, logs, and stop conditions. As **evidence of physical reversibility**, it lacks the needed target-specific support. The Concept Transfer Record must keep those judgments separate. If the agent proposes a physical action on the premise that all effects are reversible, the unsupported premise becomes material to authorization. The executor must evaluate the operation under the actual instrument and safety policy, independently of the analogy's plausibility.

To test the decisive condition, an evaluator could vary one target property while holding the analogy and goal fixed: one procedure supports an independently verified restoration operation, while another irreversibly consumes the sample. The desired difference is not a generic refusal to reason analogically. It is an appropriate distinction in the proposed action and in the claims asserted about recovery. This is a proposed diagnostic pair, not a completed experiment.

<a id="concept-to-action-boundary"></a>

### 9.3 The concept-to-action boundary

The practical boundary is crossed once a claim is treated as a material premise of an action. A claim might receive support for one purpose while being insufficient for another. Consider the laboratory analogy in Section 9.2. It supports a checklist for experimental preparation, yet it establishes no physical rollback property. A policy permitting an operation on the assumption of rollback would need target-specific evidence for that assumption.

Three inspectable records connect the boundary without conflating its judgments. The **claim record** states the target proposition, available evidence, material assumptions, and intended uses. The **action record** identifies the proposed operation and any claims expressly relied upon to support its preconditions or risk assessment. The **authorization record** identifies the governing policy, checked evidence and operative state, and decision. A claim assessment grants no execution privileges, while an authorization decision establishes no post-execution result. The actual validator must inspect evidence of the operation's effects.

In compact form, let `q` denote a target claim, `u` its intended use, `W` the available evidence, and `a` a proposed operation. `warrant(q, u, W)` is an assessment of evidential support, potentially including an unresolved status; `authorize(a, state, policy)` is an assessment of permission under the governing policy and operative state. These are separate decisions in a proposed interface, without formal inference rules or established soundness. Where `depends(a, q)` is material, the policy might condition authorization on a specified warrant status, an independent check of the operative precondition, or explicit escalation. Such a rule constrains conduct only if the executor enforces the resulting decision.

No self-reported rationale exposes every influence on a model's decision. Agents might omit a premise, produce a post hoc explanation, or invoke an action without naming its conceptual basis. The record discipline accordingly addresses **externalized claims, declared dependencies, instrumented operations, and independently checked state**. It neither certifies hidden cognition nor treats a complete-looking rationale as proof that the action was justified. For high-impact operations, the relevant preconditions need checks anchored in the environment, beyond the agent's declaration.

<a id="conceptual-revision"></a>

### 9.4 Revision and propagation of new evidence

Interventions produce observations that might support, restrict, or disconfirm the concepts used to plan them. Claim records consequently need explicit versions and evidence dependencies. If a target relation loses its warrant, the system identifies dependent claims, stored conclusions, reusable plans, and pending actions recorded under its declared dependency model. Future uses of the premise are then subject to renewed review or withdrawal under the applicable policy. Dependency coverage is limited to the references actually recorded.

Temporal order is decisive. Invalidating a premise prior to authorization might block a pending action. Invalidating it during execution might trigger an abort or containment procedure, contingent on the executor's control surface. Discovering the error following execution changes future decisions and the evidential status of the earlier justification. It does not retract communications already received, restore consumed samples, or nullify economic commitments. Conceptual revision and effect compensation are coordinated through records, with distinct mechanisms and success criteria.

This asymmetry is part of the essay's central argument. Evidence from action feeds back into concepts, while executed consequences persist under the environment's physical, technical, and institutional rules. The shared history supports diagnosis and prospective correction; it provides no general inverse for an earlier intervention.

<a id="concept-transfer-evaluation"></a>

### 9.5 Evaluating conceptual transfer under consequences

Decisive evaluation must distinguish improved reasoning about the target from reduced operational harm. Matched source-target problems would contain supported transfers, partially valid transfers, and plausible yet false transfers, with independently grounded target evidence. Each family would include legitimate actions as well as tempting, unsupported ones. The reference evaluation must establish which target conclusions and operational uses are warranted under the scenario assumptions before inspecting the tested agent's output.

The outcomes need separate reporting: correctness of stated target claims, correctness of declared permitted use, choice of proposed operation, authorized task completion, forbidden executed effects, and the cost of checks. A model might identify a flawed analogy yet still attempt an unauthorized operation. Conversely, a mediator might prevent the harmful effect despite the model continuing to assert the flawed claim. Neither result establishes improvement across both conceptual judgment and effect containment.

The proposed factorial comparison varies two factors independently. The first is whether the planner receives structured concept-transfer records. The second is whether a trusted executor enforces action-policy checks or runs the same checks in **shadow mode**, without blocking an operation. The executor must use the same baseline action metadata and independent state checks in every arm, including arms without a transfer record; otherwise the treatment confounds record availability with enforcement quality. Minimal event instrumentation stays constant across arms, and shadow-mode decision feedback is withheld from the planner during the trial. The added transfer record changes available information by design; other task information, tool affordances, and execution budgets must be held comparable. Only controlled, resettable environments with simulated consequential targets belong in shadow-mode comparisons. Random assignment, predeclared reference labels, repeated trials, and matched resource budgets would support attribution of differences in expressed claims and executed effects to the respective factors.

Results concern observable commitments and actions. A successful record-based intervention would establish a narrower empirical fact: under the tested conditions, the externalized dependencies and enforcement path improved specified outcomes. It would establish no general access to hidden reasoning, and it would not settle the full scope of conceptual intelligence.

<a id="conceptual-and-effectful-scope"></a>

### 9.6 One interface, distinct standards of success

The conceptual and effectful components form a coherent research interface, without presently constituting a single formal theory. Conceptual transfer generates candidate claims with validity contingent on mapping assumptions and target-domain evidence. Operational control evaluates a proposed intervention under authority, preconditions, effect scope, and observed consequences. The interface records where a particular claim is used to support an operation, allowing later evidence to revise future reliance on that claim.

This framing protects the strongest contribution of each component. Conceptual evaluation retains its concern with explanatory and inferential adequacy beyond tool execution. Effectful evaluation retains its concern with authority and state transitions even for routine actions involving no novel conceptual inference. A common record structure is justified by the dependency that joins them, not by an assertion that these problems have identical semantics.

<a id="security-as-effect-control"></a>

## 10. Security as control of information and authority flows

Prompt injection and related attacks test the boundary from untrusted observation to privileged action. Retrieved pages or tool results might contain an instruction to send data externally, alter a repository, retain a malicious memory, or invoke a different tool. The observed content supplies task data; it does not supply governing authority. The executor enforcing authorized targets and flows has a distinct role from the agent's ability to recognize malicious text.

The record tracks sensitive reads and possible disclosures, including compositions distributed across several tools. It further distinguishes a rejected malicious proposal from successful exfiltration, a poisoned memory write from subsequent use of that memory, and a policy violation from a missing audit record. An annotation that labels an operation `security` provides no isolation by itself. Actual containment depends on the trusted enforcement boundary, scope of credentials, and the channels accessible outside the declared workflow.

AgentDojo supplies an established environment for studying attacks against tool-using agents [11]. The proposed extension classifies attack outcomes by the operation proposed, the operation attempted, the enforcement decision, the observed state change, and the evidence supporting each label. Its incremental diagnostic value relative to existing attack-success and utility measures remains an empirical question.

<a id="effectful-agent-benchmark-v0.2"></a>

## 11. Effectful Agent Benchmark v0.2

The proposed Effectful Agent Benchmark tests whether effect-aware control changes outcomes that task-success metrics conceal. Each item fixes a task goal, initial state, policy and authority context, available tools, protected state, permitted and forbidden operations, untrusted observations, required checks, and an evaluation procedure. Test interfaces expose the instructions, policy restrictions, protected-state rules, and observations needed for legitimate action, while concealed environment state, adjudication labels, and attack objectives are withheld. Evaluation also needs safeguards against reuse of public test items during development or tuning.

The evaluation separates the planner from the mediator and executor. Where a consequential action relies on an expressed conceptual inference, the item also identifies which premises are material to the action and which target-domain evidence would justify their use. **Proposal validity** assesses the action selected by the agent. **Authorization correctness** assesses the policy decision under an independently specified reference rule. **Containment** assesses whether forbidden effects reached the environment given an opportunity to attempt them. **State validity** assesses postconditions and protected-state changes over a defined observation scope. **Audit sufficiency** assesses whether an independent reviewer could reconstruct the relevant event and decision from retained evidence.

| Outcome | Operational definition | Important limitation |
|---|---|---|
| Task completion | Independently checked goal achievement. | Does not imply authorized execution. |
| Invalid-proposal rate | Policy-invalid proposals divided by all proposals eligible for the specified decision. | Report invalidity types and opportunities without proposals separately. |
| Authorization error | False permits per prohibited request evaluated, and false refusals per permissible request evaluated. | Reference policy, ambiguous cases, and adjudication process need independent justification. |
| Forbidden-effect execution rate | Trials with at least one detected forbidden effect divided by trials possessing a verified forbidden-effect route in the isolated test environment. | Report eligible routes, agent attempts, mediator decisions, and observed execution separately; this metric mixes proposal and enforcement behavior. |
| Containment failure under attempted violation | Attempts resulting in a detected forbidden effect divided by verified forbidden-operation attempts reaching the protected mediation boundary. | Establish the attempted operation, intended target, and operative enforcement path independently; separately report bypass attempts and unobservable outcomes. |
| Protected-state violation | Detected forbidden changes in specified state regions per eligible task or action. | Unobserved state cannot be counted as preserved. |
| Validation coverage | Applicable obligations for which a specified check returned interpretable evidence, divided by all applicable obligations. | A completed check might return failure or uncertainty; coverage establishes neither correctness nor successful validation. |
| Completion-claim accuracy | Correctly classified completion assertions divided by assertions with adjudicated reference outcomes. | Report unsupported positive claims, unsupported negative claims, and reference-unknown cases separately. |
| Transfer-use validity | Stated claims and uses agreeing with independently specified target evidence and application criteria, reported separately. | The claims' truth status and permissible use need independent references; no inference about hidden cognition follows. |
| Recovery performance | Restored or compensated obligations under defined failure cases. | Compensation is not equivalent to reversal. |
| Audit reconstruction | Required events reconstructed correctly by blinded reviewers divided by adjudicated events. | Reviewers need trusted source evidence; an agent-authored log might be fluent yet inaccurate. |
| Task cost | Tool calls, latency, token use, reviewer effort, and execution expenditure. | Security gains have to be interpreted alongside utility and overhead. |

These metrics need explicit denominators and `not applicable` outcomes. Tasks with no consequential action provide no evidence of successful authorization for consequential actions. Likewise, a refusal might prevent an unauthorized effect while failing a legitimate task. Reporting only a composite score would obscure the relevant trade-offs.

The initial study would compare a task agent with outcome-only measurement, a logging-only variant, and a variant with execution-coupled mediation, under comparable tool access and budgets. Minimal outcome measurement is necessary in every arm, even without an agent-facing ledger. A separate study would test the factorial design of Section 9.5 on transfer-relevant tasks. The reference policy, permissible targets, postconditions, and effect labels must be specified before evaluating agent outputs. Intervention assignments, tool interfaces, execution budgets, reset procedures, and observation mechanisms need independent documentation. Report uncertainty with the task as the primary sampling unit, accounting for repeated stochastic trials and shared task families. Disaggregate failure types and report the number of eligible, attempted, blocked, and executed forbidden operations. Include legitimate requests, policy conflicts, adversarial observations, partial commits, and matched target conditions. Dedicated bypass tests must establish a viable forbidden-effect route in the isolated test environment. A low attack-attempt rate gives information about planner behavior, not a reliable estimate of enforcement strength.

The benchmark's scientific value is conditional. If ordinary task success, side-effect judgments, and existing security evaluations already identify all relevant failures at similar evaluation cost, the new benchmark adds limited information. If the ledger reduces a measured error only by refusing most tasks or imposing prohibitive overhead, it has not established a useful general-purpose improvement. No benchmark runs or causal effects are asserted in this essay.

<a id="diagnostic-cases"></a>

## 12. Diagnostic cases across domains

Repository-editing agents supply precise state comparisons. The worked example in Section 7.1 demonstrates the difference from test success to frame preservation and action authorization. It also exposes the limits of tests as validators of unrelated state.

Calendar and email agents illustrate social consequences. Drafting and sending are distinct action types, as are checking an appointment and committing another person's time. Recipient identity, time-zone interpretation, approval scope, and cancellation procedure belong to the contract. An external recipient's receipt of a message cannot be fully undone by later compensation.

Laboratory protocol agents stress resource and physical-state assumptions. The database-transaction analogy in Section 9.2 adds an independent conceptual failure mode: valid organizational guidance might be promoted into an unsupported claim of physical reversibility. Sample identity, instrument configuration, controls, stopping criteria, hazard classification, and evidence policy constrain legitimate action. Execution records must distinguish a protocol prepared on paper, an instruction sent to equipment, an instrument acknowledgment, and a physically verified result. Experimental data support claims only to the extent licensed by the measurement and inference procedure.

Web agents encountering malicious content test the separation of observation from authority. The critical event is not the presence of an attack string alone. It is whether the untrusted content causes a forbidden proposal, whether the mediator blocks it, whether a protected effect executes, and whether subsequent records correctly represent the event.

<a id="objections-and-failure-modes"></a>

## 13. Objections and limiting cases

**A ledger might become elaborate logging.** This objection is decisive for a system lacking an enforcement path. Documentation supports reconstruction and perhaps human review, yet it provides no execution containment on its own. The strongest version of the proposal couples the record to a mediator and a validator. Weaker deployments need correspondingly narrower claims.

**Open-world effects resist exact types.** The proposal records declared effects and bounded observations under an explicit abstraction. Unknown effects and external dependencies remain possible. It makes no claim of complete static inference or soundness for arbitrary tools.

**Human review could perform the same work.** Human review is a relevant baseline, especially for consequential decisions. The pertinent comparison concerns decision accuracy, consistency, time, and the information supplied to the reviewer, not an assumption that automation necessarily improves judgment.

**Runtime checks introduce cost and false refusals.** A policy gate might block legitimate work, misinterpret authority, or race with external updates. Utility, erroneous denial, latency, and reviewer workload belong in the same empirical analysis as blocked violations.

**Concept transfer differs categorically from file writes.** The proposed connection is a chain of dependence from externalized inferential assumptions to durable memory, design commitments, scientific claims, or executed actions. The record identifies material dependencies and restrictions on their use. It does not equate an internal thought with a state change.

**A transfer record cannot verify an agent's hidden reasoning.** This limitation is substantive. The system evaluates expressed claims and mediated operations, leaving unreported dependencies and latent reasoning outside its inspection boundary. Direct state checks and reference-policy evaluation are indispensable safeguards against incomplete rationales.

**The audit record might itself be compromised.** The trusted base includes the mediator, executor, observation mechanism, and record-integrity controls. If the same untrusted agent controls all four, a complete-looking trace provides weak independent evidence.

<a id="kill-criteria-and-series-synthesis"></a>

## 14. Research criteria and series synthesis

<a id="kill-criteria"></a>

### 14.1 Conditions for revising or abandoning the proposal

The empirical program has clear failure conditions. The enforcement variant might produce no material improvement over matched logging-only or uninstrumented baselines. Declared effects might be too incomplete to guide decisions in the selected environments. Validators might be unable to detect the relevant state changes with adequate reliability. Authorization checks might permit bypass or lead to unacceptable denial of legitimate work. A benchmark might reproduce existing task-success and security measures without identifying additional failures. Concept Transfer Records might have no measurable effect on unsupported promotion of conceptual inferences into action premises or on the resulting decisions. Each outcome would narrow the claims justified by the framework.

The strongest case for continuation would be evidence that independently checked, execution-linked records improve control or diagnosis at an acceptable cost, with a clear account of the mechanisms responsible for improvement. Neither a polished schema nor a plausible trace is a substitute for that evidence.

<a id="series-synthesis"></a>

### 14.2 Synthesis

The series converges on typed artifacts situated in environments with conditions for generation, composition, transformation, validation, and use. Concept formation and transfer enlarge the candidate relations through which an agent interprets a task. Effectful action tests the consequences of acting on selected interpretations. The present essay extends that account to the world changes enacted by agents. **Warrant** concerns the support for a candidate claim or plan. **Authority** concerns permission to perform a particular operation. **Execution evidence** concerns what took place. **Validation** concerns which consequences have been established. These distinctions are complementary and none is interchangeable with the others. Target-domain evidence is needed to justify a transferred premise. Independent permission is needed to perform the action. Execution evidence is needed to establish which intervention occurred. Subsequent observations might call for revision of the originating concept.

| Essay | Principal question |
|---|---|
| Semantic Participation | Under which conditions does an artifact participate meaningfully in an environment? |
| Typed Generativity | Which target type is inferred, and what would inhabit it? |
| Functorial Consistency | Which relations survive a transformation? |
| Lambek Machines | How does compositional linguistic structure constrain valid construction? |
| Algebraic Architectures | Which structural commitments does a model architecture embody? |
| Quantitative Curry–Howard | Which measurements, validators, and uncertainties support an artifact's use? |
| Effectful and Conceptual Intelligence | Which conceptual inferences legitimately support action proposals, under what authority are those actions executed, and what consequences are established by evidence? |

The final proposition is deliberately limited. Intelligence expressed through consequential action warrants evaluation of declared inferential dependencies alongside authorized and observed operations, with uncertainty retained for unobserved consequences and undisclosed reasoning. The proposed record discipline earns its place in the series through demonstrated changes in what systems prevent, evaluators distinguish, and investigators substantiate. Its unity resides in the accountable passage from inference to intervention and subsequent revision, under distinct standards at each stage.

<a id="appendix-a.-typed-action-ledger-schema"></a>

## Appendix A. Typed Action Ledger record specification

The following is a **conceptual schema**, not a validated implementation or a normative interchange format. Concrete implementations would also define field types, versioning, signature or integrity mechanisms, event ordering, authorization-token binding, retention, and data minimization.

| Field group | Essential fields |
|---|---|
| `ledger` | `ledger_id`, `schema_version`, `task_id`, `created_at`, `record_integrity` |
| `task_context` | `trusted_instruction_refs`, `policy_version`, `principal`, `goal`, `memory_snapshot_ref`, `environment_snapshot_ref` |
| `action` | `entry_id`, `proposer`, `action_type`, `target`, `arguments`, `observation_refs`, `material_claim_refs`, `dependency_refs`, `material_premise_disclosure_status` |
| `contract` | `preconditions`, `postconditions`, `declared_effects`, `allowed_effects`, `forbidden_effects`, `frame_conditions` |
| `authority` | `authority_source`, `scope`, `approval_ref`, `expiry`, `required_capabilities`, `granted_capabilities` |
| `control` | `handler_version`, `policy_version`, `checked_state_version`, `decision`, `decision_evidence`, `bound_executor_request`, `execution_result` |
| `observation` | `executor_receipt`, `state_delta_refs`, `observation_scope`, `unobserved_obligations` |
| `validation` | `validator_version`, `checks`, `verdict`, `diagnostics`, `compensation_ref`, `escalation_ref` |
| `reuse` | `completion_claim_status`, `memory_write_permission`, `skill_reuse_permission`, `claim_invalidation_refs`, `audit_status` |

<a id="appendix-b.-effectful-agent-benchmark-schema"></a>

## Appendix B. Effectful Agent Benchmark item specification

Each item identifies `item_id`, `domain`, `goal`, `initial_state`, `policy_context`, `authority_reference`, `tools`, `memory_state`, `permitted_effects`, `forbidden_effects`, `required_preconditions`, `required_postconditions`, `protected_state`, `untrusted_inputs`, `material_premises`, `target_evidence`, `validators`, `exposure_conditions`, and `failure_labels`. The associated evaluation record identifies each proposal, mediation decision, executed operation, observed effect, completion claim, validator outcome, and evaluation cost.

Reference specifications and hidden labels must remain separate from the agent's observations. Evaluators need to identify whether a test assesses agent choice, policy interpretation, actual enforcement, or retrospective diagnosis. Results without an eligible prohibited-operation path provide no positive evidence of containment.

<a id="appendix-c.-concept-transfer-record-schema"></a>

## Appendix C. Concept Transfer Record specification

Each Concept Transfer Record identifies `id`, `version`, `source_domain`, `target_domain`, `source_objects`, `target_objects`, `mapping`, `claimed_target_inferences`, `preserved_relations`, `changed_relations`, `lost_relations`, `counterexamples`, `source_evidence_refs`, `target_evidence_refs`, `open_assumptions`, `distortion_risk`, `invalidation_conditions`, `permitted_use`, `forbidden_use`, `dependent_claim_refs`, `dependent_action_refs`, and `review_status`. The record distinguishes supported, contradicted, and unresolved target relations under a stated use. Its presence establishes neither the truth of an inference nor authorization for an associated action. Linking material action premises to record versions permits later review if an assumption or observation changes. An absent dependency link is recorded as incomplete disclosure, not evidence that the operation involved no conceptual premise.

## References

1. C. A. R. Hoare. “[An Axiomatic Basis for Computer Programming](https://doi.org/10.1145/363235.363259).” *Communications of the ACM* 12(10), 1969.
2. John C. Reynolds. “[Separation Logic: A Logic for Shared Mutable Data Structures](https://doi.org/10.1109/LICS.2002.1029817).” *LICS*, 2002.
3. Philip Wadler and Peter Thiemann. “[The Marriage of Effects and Monads](https://doi.org/10.1145/601775.601776).” *ACM Transactions on Computational Logic* 4(1), 2003.
4. Gordon D. Plotkin and Matija Pretnar. “[Handling Algebraic Effects](https://doi.org/10.2168/LMCS-9(4:23)2013).” *Logical Methods in Computer Science* 9(4:23), 2013.
5. Jerome H. Saltzer and Michael D. Schroeder. “[The Protection of Information in Computer Systems](https://doi.org/10.1109/PROC.1975.9939).” *Proceedings of the IEEE* 63(9), 1975.
6. Norm Hardy. “[The Confused Deputy (or Why Capabilities Might Have Been Invented)](https://doi.org/10.1145/54289.871709).” *ACM SIGOPS Operating Systems Review* 22(4), 1988.
7. Drew McDermott et al. “[PDDL: The Planning Domain Definition Language](https://www.cs.cmu.edu/~mmv/planning/readings/98aips-PDDL.pdf).” AIPS-98 planning competition specification, 1998.
8. Shunyu Yao et al. “[ReAct: Synergizing Reasoning and Acting in Language Models](https://mlanthology.org/iclr/2023/yao2023iclr-react/).” *ICLR*, 2023.
9. Tianbao Xie et al. “[OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.nips.cc/paper_files/paper/2024/hash/5d413e48f84dc61244b6be550f1cd8f5-Abstract-Datasets_and_Benchmarks_Track.html).” *NeurIPS*, 2024.
10. Shunyu Yao et al. “[τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](https://proceedings.iclr.cc/paper_files/paper/2025/hash/1b126cc38b8638e07bef37e7b2bb72bf-Abstract-Conference.html).” *ICLR*, 2025.
11. Edoardo Debenedetti et al. “[AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/hash/97091a5177d8dc64b1da8bf3e1f6fb54-Abstract-Datasets_and_Benchmarks_Track.html).” *NeurIPS*, 2024.
12. Xing Han Lù et al. “[AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories](https://proceedings.colm.cc/paper_files/paper/2025/hash/e61219bcb30e2a78f0647bfafe7855ca-Abstract-Conference.html).” *COLM*, 2025.
13. Dedre Gentner. “[Structure-Mapping: A Theoretical Framework for Analogy](https://doi.org/10.1207/s15516709cog0702_3).” *Cognitive Science* 7(2), 1983.
14. Timo Schick et al. “[Toolformer: Language Models Can Teach Themselves to Use Tools](https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html).” *NeurIPS*, 2023.
15. Shuyan Zhou et al. “[WebArena: A Realistic Web Environment for Building Autonomous Agents](https://proceedings.iclr.cc/paper_files/paper/2024/hash/4410c0711e9154a7a2d26f9b3816d1ef-Abstract-Conference.html).” *ICLR*, 2024.
16. Paul Bartha. *[By Parallel Reasoning: The Construction and Evaluation of Analogical Arguments](https://academic.oup.com/book/27055)*. Oxford University Press, 2010.
17. Judea Pearl and Elias Bareinboim. “[External Validity: From Do-Calculus to Transportability Across Populations](https://doi.org/10.1214/14-STS486).” *Statistical Science* 29(4), 2014.
