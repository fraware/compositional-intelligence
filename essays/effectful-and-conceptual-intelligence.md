# Effectful and Conceptual Intelligence

*Mateo Petel*

## Abstract

Language-model agents now operate through interfaces that alter state, including tools, files, databases, browsers, calendars, code execution, workflow systems, and embodied environments. This shift changes the evaluation target. A text response can often receive review before downstream use. An agent action changes internal, computational, social, economic, or physical state. The relevant object is therefore the typed, warranted, effectful trace connecting instruction, authority, execution, validation, and consequence.

This essay proposes a type-and-effect record for consequential agent behavior. Its judgment, Gamma; M; E; C \|- a : Pre -\> Post ! eps @ rho, records instruction context, memory, environment, capabilities, requested action, preconditions, postconditions, declared effects and risk-authority obligations. It specifies an auditable candidate action and its governing checks. Execution-time enforcement additionally depends on actual permission gates, state observations, handlers and post-execution validation. Record completeness and enforcement effectiveness are independently testable properties.

The framework is grounded in Hoare-style pre/post reasoning, planning formalisms, monadic semantics, algebraic effects and handlers <span class="citation-group" data-review="unapproved" data-target="EFFECTFUL-AND-CONCEPTUAL-INTELLIGENCE-P006" data-scope-id="EFFECTFUL-AND-CONCEPTUAL-INTELLIGENCE-P006-1" data-source-keys="Hoare1969,PDDL1998,Moggi1989,PlotkinPretnar2013">[<a class="citation-link" href="#ref-Hoare1969" aria-label="Provisional reference 1 — An Axiomatic Basis for Computer Programming">1</a>, <a class="citation-link" href="#ref-PDDL1998" aria-label="Provisional reference 2 — PDDL—The Planning Domain Definition Language, Version 1.2">2</a>, <a class="citation-link" href="#ref-Moggi1989" aria-label="Provisional reference 3 — Computational Lambda-Calculus and Monads">3</a>, <a class="citation-link" href="#ref-PlotkinPretnar2013" aria-label="Provisional reference 4 — Handling Algebraic Effects">4</a>]</span>. Agent security and trajectory-judge evaluation supply distinct empirical antecedents <span class="citation-group" data-review="unapproved" data-target="EFFECTFUL-AND-CONCEPTUAL-INTELLIGENCE-P006" data-scope-id="EFFECTFUL-AND-CONCEPTUAL-INTELLIGENCE-P006-2" data-source-keys="AgentDojo2024,AgentRewardBench2025">[<a class="citation-link" href="#ref-AgentDojo2024" aria-label="Provisional reference 5 — AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents">5</a>, <a class="citation-link" href="#ref-AgentRewardBench2025" aria-label="Provisional reference 6 — AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories">6</a>]</span>. AgentDojo studies prompt-injection attack and defense. AgentRewardBench assesses judgments of web-agent trajectories, including task success and side effects. Tool use, memory writes, and authorization controls are separate targets of the proposed ledger. Its contribution is an accounting layer for consequential agent behavior. Actions, tool calls, memory writes, plan steps, skill invocations, and concept transfers are represented with declared effects, authority source, provenance, validators, compensation paths, and permitted downstream use.

The claim is falsifiable. Typed effect records matter only where they improve action selection, authorization, validation, repair, auditability, memory quality, skill reuse, security analysis, or controlled conceptual transfer. A ledger that adds documentation without changing execution-time control has no technical role in the proposed program.



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
<td>Typed-action judgment</td>
<td>Gamma; M; E; C |- a : Pre -&gt; Post ! eps @ rho records action, context, memory, environment, capability, pre/post conditions, effects, risk, authority, and validation obligations.</td>
</tr>
<tr class="even">
<td>C2</td>
<td>Execution-phase separation</td>
<td>The framework separates proposal, authorization, execution, and validation, exposing failures that final task success can obscure.</td>
</tr>
<tr class="odd">
<td>C3</td>
<td>Effect taxonomy</td>
<td>The taxonomy distinguishes read, write, tool, memory, human, social, economic, physical, skill, security, and conceptual-transfer effects.</td>
</tr>
<tr class="even">
<td>C4</td>
<td>Typed Action Ledger</td>
<td>The ledger is proposed as an execution-time accounting layer for action contracts, authority, state change, handlers, validators, rollback, and audit.</td>
</tr>
<tr class="odd">
<td>C5</td>
<td>Effectful Agent Benchmark</td>
<td>The benchmark design evaluates task success together with preconditions, postconditions, side effects, authority, rollback, memory quality, and audit completeness.</td>
</tr>
<tr class="even">
<td>C6</td>
<td>Series closure</td>
<td>The essay connects membership, generation, transformation, language structure, architecture specification, and quantitative warrant to action under consequences.</td>
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
<th><strong>Reader</strong></th>
<th><strong>Recommended path</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Agent researcher</td>
<td>Sections 1, 2, 3, 4, 5, 7, 11, and 13</td>
</tr>
<tr class="even">
<td>Security researcher</td>
<td>Sections 4, 5, 6, 10, 11, and 13</td>
</tr>
<tr class="odd">
<td>Formal-methods researcher</td>
<td>Sections 3, 4, 6, 7, 8, and Appendix A</td>
</tr>
<tr class="even">
<td>AI-for-science reader</td>
<td>Sections 8, 9, 11, 12, and 14</td>
</tr>
<tr class="odd">
<td>Series reader</td>
<td>Read after Essay 6; use Section 14 as the suite synthesis</td>
</tr>
</tbody>
</table>



## 1. Position in the Compositional Intelligence series {#1-position-in-the-compositional-intelligence-series}

Effectful and Conceptual Intelligence supplies the action layer of Compositional Intelligence. Earlier essays define artifact membership, target-type inference, transformation-preserving evaluation, typed linguistic composition, architecture specification, and quantitative warrant. The present essay asks how those artifacts enter execution contexts in which an agent can change memory, call tools, edit state, create commitments, or operate physical systems.

membership -\> generation -\> transformation -\> language -\> architecture -\> warrant -\> action

The transition from warrant to action introduces a new evaluation unit. Scores, validators, and epistemic types guide action only through an authorization surface that tests preconditions, permitted effects, validation obligations, and compensation paths. A system that generates a plausible plan has produced a candidate artifact; it has not thereby justified the state transitions needed to execute that plan.

## 2. Evaluation unit for agent action {#2-evaluation-unit-for-agent-action}

Agent action requires state-transition evaluation instead of response-level evaluation. A response can be inspected as a representational artifact; an action modifies a state that can influence later reasoning, external systems, social commitments, financial records, or physical processes. The evaluation target is therefore the trace by which the agent moves from instruction to consequence under a specified authority envelope.

A failure in an agent trace differs from an error in a generated answer. A false tool result can enter the workflow as an observation, a false memory can contaminate later decisions, and an unauthorized message can create an obligation outside the user intent that licensed the interaction. These cases share a structural feature: the defect is located in the relation among context, authority, state change, and validation, not only in the linguistic surface of an answer.

## 3. The typed-action judgment {#3-the-typed-action-judgment}

The core judgment records an action as a constrained state transition. It exposes the context available to the agent, the persistent memory state, the target environment, the capabilities under which execution occurs, the action contract, the declared effects, and the risk-authority record governing authorization and validation.

Γ; M; E; C ⊢\_spec a : Pre → Post ! ε @ ρ



<table>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Symbol</strong></th>
<th><strong>Meaning</strong></th>
<th><strong>Operational role</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Gamma</td>
<td>instruction, policy, and task context</td>
<td>States goals, constraints, user intent, and system-level rules.</td>
</tr>
<tr class="even">
<td>M</td>
<td>memory context</td>
<td>Records persistent facts, episodic traces, preference records, skill history, and memory-access limits.</td>
</tr>
<tr class="odd">
<td>E</td>
<td>environment or interface state</td>
<td>Records files, pages, applications, APIs, databases, instruments, or physical setup.</td>
</tr>
<tr class="even">
<td>C</td>
<td>capability context</td>
<td>Records tools, permissions, credentials, authority limits, rate limits, and action channels.</td>
</tr>
<tr class="odd">
<td>a</td>
<td>action or plan step</td>
<td>Specifies the proposed operation, tool call, write, message, memory update, skill invocation, or physical act.</td>
</tr>
<tr class="even">
<td>Pre</td>
<td>preconditions</td>
<td>Defines state, resource, approval, policy, and safety conditions required before execution.</td>
</tr>
<tr class="odd">
<td>Post</td>
<td>postconditions</td>
<td>Defines the expected state after execution and the evidence needed to assert completion.</td>
</tr>
<tr class="even">
<td>eps</td>
<td>effect row</td>
<td>Declares state changes and side effects.</td>
</tr>
<tr class="odd">
<td>rho</td>
<td>risk-authority record</td>
<td>Records risk level, authority source, reversibility, validation type, and escalation policy.</td>
</tr>
</tbody>
</table>



The judgment is an execution-accounting proposal. An operational system would use its fields to evaluate authorization before a consequential action, constrain the available capabilities, observe state changes, validate postconditions and trigger compensation where supported. Ledger completeness and enforcement effectiveness are independent evaluation dimensions. The proposed evaluation separates record coverage, decision-time authorization, execution-time violations, postcondition evidence and terminal task completion.

## 4. Execution phases {#4-execution-phases}

Effectful evaluation separates proposal, authorization, execution, and validation. Final task success erases these phases and therefore hides the failure mode most relevant to audit. An agent can choose the wrong operation, possess a tool without authority, execute only a partial state transition, or report completion without verifying the resulting state.



<table>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Phase</strong></th>
<th><strong>Question</strong></th>
<th><strong>Failure exposed</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Propose</td>
<td>Which action is the agent requesting?</td>
<td>Wrong action type, wrong target, missing context, or invalid plan step.</td>
</tr>
<tr class="even">
<td>Authorize</td>
<td>Is the action permitted under current authority and risk constraints?</td>
<td>Permission violation, policy conflict, missing approval, or capability overreach.</td>
</tr>
<tr class="odd">
<td>Execute</td>
<td>Which state transition occurred?</td>
<td>Tool error, unintended write, hidden side effect, partial execution, or external-system drift.</td>
</tr>
<tr class="even">
<td>Validate</td>
<td>Did postconditions hold and frame conditions remain intact?</td>
<td>Unverified completion, state drift, failed rollback, missing evidence, or audit gap.</td>
</tr>
</tbody>
</table>



This phase separation connects directly to transformation-sensitive evaluation. A plan or tool call can look locally plausible and still fail to preserve the relation between intended state transition and observed state delta. The ledger therefore compares declared preconditions, declared effects, observed changes, validated postconditions, and protected frame conditions.

## 5. Effect taxonomy {#5-effect-taxonomy}

Agent systems require an effect taxonomy that distinguishes operations by state impact and review obligation. A generic tool-call label erases the difference between reading a page, writing a file, committing to a social action, storing memory, or touching a physical instrument. Those effects require different authority sources, validators, rollback paths, and audit evidence.



<table>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Effect class</strong></th>
<th><strong>Typical operation</strong></th>
<th><strong>Required record field</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Read</td>
<td>Read webpage, file, database row, repository state, or sensor value.</td>
<td>Source, trust level, freshness, sensitivity, and observation channel.</td>
</tr>
<tr class="even">
<td>Write</td>
<td>Edit file, database row, repository, document, calendar, or form.</td>
<td>Target, diff, reversibility, postcondition, and frame condition.</td>
</tr>
<tr class="odd">
<td>Tool call</td>
<td>Invoke API, shell command, browser operation, or code execution.</td>
<td>Tool schema, arguments, return value, failure mode, and isolation status.</td>
</tr>
<tr class="even">
<td>Memory</td>
<td>Store or retrieve persistent fact, summary, preference, or skill trace.</td>
<td>Scope, retention, source, confidence, invalidation condition, and privacy class.</td>
</tr>
<tr class="odd">
<td>Human or social</td>
<td>Send message, make request, create commitment, or escalate.</td>
<td>Recipient, authority, obligation, approval status, and cancellation path.</td>
</tr>
<tr class="even">
<td>Economic</td>
<td>Purchase, booking, subscription, or financial transaction.</td>
<td>Approval, budget, cancellation path, receipt, and legal or institutional scope.</td>
</tr>
<tr class="odd">
<td>Physical</td>
<td>Robotic, laboratory, sensorimotor, or instrument action.</td>
<td>Instrument state, sample, hazard, operator approval, abort condition, and evidence record.</td>
</tr>
<tr class="even">
<td>Skill</td>
<td>Invoke or store reusable action pattern.</td>
<td>Version, pre/post contract, validation history, owner, and deprecation rule.</td>
</tr>
<tr class="odd">
<td>Security</td>
<td>Handle credential, untrusted content, prompt-injection surface, or data boundary.</td>
<td>Isolation status, sanitization rule, allowed channel, and audit trail.</td>
</tr>
<tr class="even">
<td>Concept transfer</td>
<td>Apply analogy, abstraction, or schema across domains.</td>
<td>Preserved relations, lost relations, counterexamples, distortion risk, and permitted use.</td>
</tr>
</tbody>
</table>



The taxonomy is extensible, but its first use is diagnostic. It blocks the common error in which a system treats tool availability as authorization or treats a read observation as an instruction. The relevant evaluation question is whether the declared effect class matches the actual state transition and the authority relation that licensed it.

## 6. Handlers, validators, and authority {#6-handlers-validators-and-authority}

Effect records become execution controls only if a trusted component mediates each consequential operation at its execution boundary. That component checks the actual capability, policy and user authorization against the pending action and current state, then permits, denies or escalates the operation. A logged decision by an untrusted agent is audit evidence, not enforcement. The ledger records the enforcement identity and policy version, capability scope, precondition evidence, observed poststate and protected frame conditions. External writes and asynchronous actions require explicit race, partial-failure and irreversibility handling; denial or human escalation is appropriate where authorization cannot be established.

handler(eps, rho, Pre, C, E) -\> authorize \| deny \| ask \| sandbox \| escalate

Validators supply the post-execution counterpart to handlers. They compare postconditions with observed state, check frame conditions, record diagnostics, and decide whether repair, rollback, escalation, or human review is required. Their output is part of the artifact record for the trace, so a claimed completion without validation remains an unverified state-transition claim.

validator(Post, observed_state_delta, frame_conditions) -\> pass \| fail \| partial \| unknown

Authority is a typed resource distinct from interface access. A callable tool supplies a capability channel; policy, user intent, risk class, and institutional procedure determine whether the action is permitted. The ledger therefore records authority source, capability scope, approval status, and escalation criteria as separate fields, giving reviewers a path from instruction to authorization decision.

## 7. Typed Action Ledger {#7-typed-action-ledger}

The Typed Action Ledger is a proposed record of consequential agent steps. Its fields distinguish a proposed action contract, the policy decision, authorized dispatch, observed effects, and subsequent validation or compensation. The ledger itself records evidence; an enforcement claim depends on a trusted mediator covering all consequential dispatch routes, current authority and capabilities, revocation or freshness checks, concurrent operations, asynchronous effects, and irreversible external actions. Recording an unauthorized dispatch supports retrospective diagnosis, while preventing that dispatch is a separate operational property. The proposal identifies these trust-boundary obligations; enforcement effectiveness and side-effect reduction remain empirical questions.



<table>
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Ledger field group</strong></th>
<th><strong>Purpose</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Task context</td>
<td>Record user goal, policy context, risk level, initial memory snapshot, environment snapshot, and capability context.</td>
</tr>
<tr class="even">
<td>Entry identity</td>
<td>Record entry id, timestamp, proposed-by field, instruction sources, and observation sources.</td>
</tr>
<tr class="odd">
<td>Action contract</td>
<td>Record action type, preconditions, postconditions, declared effects, and frame conditions.</td>
</tr>
<tr class="even">
<td>Authority record</td>
<td>Record authority source, capabilities required, capabilities granted, and approval result.</td>
</tr>
<tr class="odd">
<td>Execution record</td>
<td>Record handler, tool or environment call, execution result, and observed state delta.</td>
</tr>
<tr class="even">
<td>Validation record</td>
<td>Record validator, validation result, diagnostics, repair, rollback, or escalation.</td>
</tr>
<tr class="odd">
<td>Reuse record</td>
<td>Record permitted downstream use, memory-update policy, skill-library update policy, and audit status.</td>
</tr>
</tbody>
</table>



The ledger succeeds only when it alters system behavior or human review. If entries are produced after execution and have no influence on authorization, validation, repair, memory quality, or skill reuse, the record layer should be simplified. A useful ledger is a control surface that constrains execution and makes later reconstruction possible.

## 8. Memory, tools, plans, and skills {#8-memory-tools-plans-and-skills}

### 8.1 Memory as effect {#8-1-memory-as-effect}

Memory writes are consequential effects. A persistent memory record can preserve validated facts and successful plans, but it can also propagate false premises into future decisions. The required record fields include source, confidence, scope, retention, privacy class, invalidation condition, and permitted use.

Gamma; M; E; C \|- write_memory(m) : M -\> M + {m} ! memory_write @ rho

### 8.2 Tools as typed interfaces {#8-2-tools-as-typed-interfaces}

Toolformer studies language-model selection and use of external APIs <span class="citation-group" data-review="unapproved" data-target="EFFECTFUL-AND-CONCEPTUAL-INTELLIGENCE-P029" data-scope-id="EFFECTFUL-AND-CONCEPTUAL-INTELLIGENCE-P029-1" data-source-keys="Toolformer2023">[<a class="citation-link" href="#ref-Toolformer2023" aria-label="Provisional reference 7 — Toolformer: Language Models Can Teach Themselves to Use Tools">7</a>]</span>. AgentDojo evaluates prompt-injection attacks against tool-using agents <span class="citation-group" data-review="unapproved" data-target="EFFECTFUL-AND-CONCEPTUAL-INTELLIGENCE-P029" data-scope-id="EFFECTFUL-AND-CONCEPTUAL-INTELLIGENCE-P029-2" data-source-keys="AgentDojo2024">[<a class="citation-link" href="#ref-AgentDojo2024" aria-label="Provisional reference 5 — AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents">5</a>]</span>. AgentRewardBench evaluates unintended side effects of agent trajectories <span class="citation-group" data-review="unapproved" data-target="EFFECTFUL-AND-CONCEPTUAL-INTELLIGENCE-P029" data-scope-id="EFFECTFUL-AND-CONCEPTUAL-INTELLIGENCE-P029-3" data-source-keys="AgentRewardBench2025">[<a class="citation-link" href="#ref-AgentRewardBench2025" aria-label="Provisional reference 6 — AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories">6</a>]</span>. Tool calls are treated here as interface actions with schemas, arguments, authority requirements, failure modes, side effects, return values, and trust conditions. Under the proposed ledger specification, a tool-result hallucination occurs if the agent claims an observation absent from the recorded tool output or attributes authority exceeding the recorded interface contract.

### 8.3 Plans as state-transition programs {#8-3-plans-as-state-transition-programs}

Plans are state-transition programs with dependency, contingency, and validation structure. A mature plan records initial state, resources, temporal constraints, cumulative effects, precondition checks, postcondition checks, abort conditions, rollback strategy, human approval points, and evidence ledger. Narrative plans lack the execution contract needed for high-impact settings.

Gamma; M; E; C \|- pi : Pre_0 -\> Post_n ! (eps_1 + \... + eps_n) @ rho



<table>
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Level</strong></th>
<th><strong>Plan maturity</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0</td>
<td>Narrative plan.</td>
</tr>
<tr class="even">
<td>1</td>
<td>Ordered checklist.</td>
</tr>
<tr class="odd">
<td>2</td>
<td>Plan annotated with preconditions and postconditions.</td>
</tr>
<tr class="even">
<td>3</td>
<td>Executable plan annotated with effects.</td>
</tr>
<tr class="odd">
<td>4</td>
<td>Validated and monitored plan with abort and rollback.</td>
</tr>
<tr class="even">
<td>5</td>
<td>Reusable plan pattern supported by execution evidence.</td>
</tr>
</tbody>
</table>



### 8.4 Skills as reusable effectful programs {#8-4-skills-as-reusable-effectful-programs}

Skills are reusable action patterns with contracts. A skill library can reduce repeated planning cost, but a weak skill can amplify an original failure across tasks. Reuse should require validated postconditions, scoped effects, stable dependencies, known failure cases, version ownership, and deprecation conditions.

skill s : Pre -\> Post ! eps

## 9. Conceptual intelligence as controlled transfer {#9-conceptual-intelligence-as-controlled-transfer}

Conceptual transfer is first a proposed transformation of a reasoning artifact: an analogy or abstraction maps selected source relations into a target domain under stated assumptions. The record names the source and target domains, mapping, intended relation, known losses, counterexamples, reviewer or validator, and permitted uses. Source-domain validity does not certify target-domain correctness. The transfer becomes consequential for effect control if it changes persistent memory, guides a tool operation or authorizes an external decision. At that boundary, the target claim needs independent warrant and the action needs the authority and effect checks specified elsewhere in the series.

concept_transfer : SourceDomain -\> TargetDomain



<table>
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Transfer field</strong></th>
<th><strong>Question</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Source domain</td>
<td>Which conceptual structure is being imported?</td>
</tr>
<tr class="even">
<td>Target domain</td>
<td>Where is the structure applied?</td>
</tr>
<tr class="odd">
<td>Preserved relations</td>
<td>Which objects, relations, operations, or transformations remain valid?</td>
</tr>
<tr class="even">
<td>Lost relations</td>
<td>Which source-domain relations fail in the target?</td>
</tr>
<tr class="odd">
<td>Counterexamples</td>
<td>Which cases reveal overtransfer or distortion?</td>
</tr>
<tr class="even">
<td>Distortion risk</td>
<td>How can the analogy mislead reasoning or action?</td>
</tr>
<tr class="odd">
<td>Permitted use</td>
<td>Can the transfer support explanation, hypothesis generation, design, or execution?</td>
</tr>
</tbody>
</table>



Concept transfer belongs in the effect layer when it influences plans, memory, scientific hypotheses, system design, or policy recommendations. Its warrant must therefore be recorded together with permitted use. An analogy used as a mnemonic has a different evidence requirement from an analogy used to authorize an action.

## 10. Security as effect control {#10-security-as-effect-control}

Agent security can be analyzed as effect control under adversarial observation and authority pressure. Prompt injection, untrusted tool output, malicious webpages, credential exposure, memory poisoning, and data exfiltration all exploit confusion among observation, instruction, authority, and external write effects.



<table>
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Security failure</strong></th>
<th><strong>Effect-control diagnosis</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Prompt injection</td>
<td>Untrusted observation attempts to authorize a forbidden action.</td>
</tr>
<tr class="even">
<td>Tool-result hallucination</td>
<td>Claimed observation differs from the recorded tool result.</td>
</tr>
<tr class="odd">
<td>Credential leakage</td>
<td>Sensitive read effect composes with unauthorized social or external-write effect.</td>
</tr>
<tr class="even">
<td>Memory poisoning</td>
<td>Untrusted or low-confidence observation is written as persistent memory.</td>
</tr>
<tr class="odd">
<td>Data exfiltration</td>
<td>Sensitive read effect is paired with unauthorized external write.</td>
</tr>
<tr class="even">
<td>Rollback failure</td>
<td>Irreversible action executes without compensation path.</td>
</tr>
<tr class="odd">
<td>Audit failure</td>
<td>Reviewer cannot reconstruct context, authority, action, state delta, and validation.</td>
</tr>
</tbody>
</table>



The ledger turns attacks into effect-level failure labels. The important invariant is not the surface form of the attack, but the unauthorized transition from untrusted observation to action, memory, or external disclosure. This view complements dynamic agent-security benchmarks by attaching each adversarial success to a specific failure in authority, isolation, validation, or audit.

## 11. Effectful Agent Benchmark v0.2 {#11-effectful-agent-benchmark-v0-2}

The Effectful Agent Benchmark evaluates task completion together with effect control. Its items specify the goal, initial state, policy context, tool set, memory state, allowed effects, forbidden effects, required checks, frame conditions, required authority, rollback obligations, untrusted inputs, validators, and audit requirements.



<table>
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Component</strong></th>
<th><strong>Benchmark obligation</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Task scenario</td>
<td>Goal, initial state, policy context, tools, memory state, and environment snapshot.</td>
</tr>
<tr class="even">
<td>Allowed effects</td>
<td>Effects authorized under the stated authority envelope.</td>
</tr>
<tr class="odd">
<td>Forbidden effects</td>
<td>Effects that violate policy, privacy, state scope, or risk limits.</td>
</tr>
<tr class="even">
<td>Required checks</td>
<td>Precondition checks, approval gates, validation tests, and frame conditions.</td>
</tr>
<tr class="odd">
<td>Trajectory record</td>
<td>Observations, proposed actions, authorizations, executions, state deltas, and validations.</td>
</tr>
<tr class="even">
<td>Scoring</td>
<td>Task success, effect precision, authority compliance, side-effect rate, rollback quality, and audit completeness.</td>
</tr>
<tr class="odd">
<td>Failure labels</td>
<td>Unauthorized action, missing precondition, wrong postcondition, memory pollution, exfiltration, rollback failure, and audit failure.</td>
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
<th><strong>Metric</strong></th>
<th><strong>Definition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Task success</td>
<td>Goal achievement under the task specification.</td>
</tr>
<tr class="even">
<td>Effect precision</td>
<td>Fraction of executed effects that are authorized and necessary.</td>
</tr>
<tr class="odd">
<td>Authority compliance</td>
<td>Fraction of consequential actions with valid authority records.</td>
</tr>
<tr class="even">
<td>Precondition coverage</td>
<td>Fraction of required preconditions checked before execution.</td>
</tr>
<tr class="odd">
<td>Postcondition validation</td>
<td>Fraction of claimed completions with successful validation.</td>
</tr>
<tr class="even">
<td>Side-effect control</td>
<td>Unintended state changes per task or per action.</td>
</tr>
<tr class="odd">
<td>Memory quality</td>
<td>Rate of valid persistent memory writes and correct invalidation handling.</td>
</tr>
<tr class="even">
<td>Rollback quality</td>
<td>Availability and effectiveness of repair or compensation path.</td>
</tr>
<tr class="odd">
<td>Audit completeness</td>
<td>Reconstructability of action, context, authority, state delta, and validation.</td>
</tr>
</tbody>
</table>



The benchmark has value only if these metrics diverge from ordinary task success. A trajectory that completes the goal and violates authority, contaminates memory, changes forbidden state, skips checks, or leaves no reconstructable record should score differently from a trajectory that satisfies the same goal under admissible effects.

## 12. Diagnostic cases {#12-diagnostic-cases}

A repository-editing agent provides the most direct diagnostic case for the ledger. The task is locally simple, but the action surface is consequential. The agent should record issue context, modifiable files, tests to preserve, expected postconditions, and forbidden effects. A patch that resolves the visible error and changes an unrelated interface is a task-success artifact with failed frame preservation.

A laboratory protocol agent shows the higher-stakes version of the same structure. Sample identity, instrument availability, permissions, controls, stopping rules, uncertainty, hazard class, and permitted claim are preconditions for action and evidence. A plausible protocol that assumes unavailable equipment, omits controls, or licenses a stronger claim than the evidence supports fails as an effectful trace even if its surface text is coherent.

Calendar and email agents require separation between draft, send, schedule, and commit operations. The ledger should record recipient, authority, time-zone assumptions, conflict checks, cancellation path, and the social commitment created by the action. This case is useful precisely where low linguistic complexity coexists with consequential external effects.

A web agent operating over untrusted content tests authority isolation. The system should separate observations from instructions, block untrusted content from granting authority, and label any external write effect. Prompt injection appears as a transition from read effect to unauthorized write, memory, or social effect.

## 13. Objections and failure modes {#13-objections-and-failure-modes}



<table>
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Objection</strong></th>
<th><strong>Response</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>The ledger is only logging.</td>
<td>The ledger has value only when it affects authorization, execution, validation, repair, or audit.</td>
</tr>
<tr class="even">
<td>Static effect systems do not fit open-world agents.</td>
<td>The proposal uses operational records, handlers, and validators, with approximate checks in domains lacking static guarantees.</td>
</tr>
<tr class="odd">
<td>Human review already handles authority.</td>
<td>Human review improves when context, authority, state delta, validation, and failure labels are explicit.</td>
</tr>
<tr class="even">
<td>The ledger slows agents down.</td>
<td>Record depth should scale with risk; low-risk reads need lighter records than persistent writes, commitments, transactions, or physical actions.</td>
</tr>
<tr class="odd">
<td>Effects are hard to enumerate.</td>
<td>The taxonomy is extensible; the required invariant is explicit state change and authority obligation.</td>
</tr>
<tr class="even">
<td>Benchmarks reward overcautious agents.</td>
<td>Metrics include task success, effect precision, and repair quality, so refusal alone cannot dominate.</td>
</tr>
<tr class="odd">
<td>Concept transfer is too interpretive.</td>
<td>Concept Transfer Records should be used only where transfer affects explanation, memory, planning, scientific claims, or decisions.</td>
</tr>
<tr class="even">
<td>Security attacks change quickly.</td>
<td>Effect-level invariants remain stable across attack forms, including authority confusion, untrusted observation, forbidden composition, and missing validation.</td>
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
<th><strong>Failure mode</strong></th>
<th><strong>Meaning</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Effect conflation</td>
<td>Read, write, memory, social, and physical effects receive the same operational treatment.</td>
</tr>
<tr class="even">
<td>Authority confusion</td>
<td>Tool availability is treated as permission.</td>
</tr>
<tr class="odd">
<td>Unchecked precondition</td>
<td>The agent acts before required state, resource, approval, or policy conditions hold.</td>
</tr>
<tr class="even">
<td>Unvalidated postcondition</td>
<td>The agent reports success without checking resulting state.</td>
</tr>
<tr class="odd">
<td>Frame violation</td>
<td>The agent changes state that should have remained protected.</td>
</tr>
<tr class="even">
<td>Memory pollution</td>
<td>False or low-confidence observation enters persistent memory.</td>
</tr>
<tr class="odd">
<td>Skill pollution</td>
<td>Unvalidated action pattern enters a reusable skill library.</td>
</tr>
<tr class="even">
<td>Conceptual overtransfer</td>
<td>Analogy imports invalid source relations into the target domain.</td>
</tr>
<tr class="odd">
<td>Rollback failure</td>
<td>An action needing repair or compensation proceeds without a path.</td>
</tr>
<tr class="even">
<td>Audit failure</td>
<td>A reviewer cannot reconstruct why an action occurred or what changed.</td>
</tr>
</tbody>
</table>



## 14. Kill criteria and series synthesis {#14-kill-criteria-and-series-synthesis}

### 14.1 Kill criteria {#14-1-kill-criteria}



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
<td>Typed action ledgers fail to reduce unauthorized actions, side effects, repair cost, or audit failures.</td>
</tr>
<tr class="even">
<td>K2</td>
<td>Effect annotations have no influence on action selection, authorization, validation, or repair.</td>
</tr>
<tr class="odd">
<td>K3</td>
<td>Runtime handlers cannot be implemented for real tools, memory stores, repositories, workflows, or environments.</td>
</tr>
<tr class="even">
<td>K4</td>
<td>The framework fails to distinguish read, write, memory, social, physical, and conceptual effects.</td>
</tr>
<tr class="odd">
<td>K5</td>
<td>Precondition and postcondition records cannot be checked even approximately in target domains.</td>
</tr>
<tr class="even">
<td>K6</td>
<td>The benchmark reveals no failures missed by ordinary task-success metrics.</td>
</tr>
<tr class="odd">
<td>K7</td>
<td>Analogy records fail to reduce conceptual overtransfer or improve explanation quality.</td>
</tr>
<tr class="even">
<td>K8</td>
<td>Human reviewers cannot use the ledger to make better approval, repair, or audit decisions.</td>
</tr>
<tr class="odd">
<td>K9</td>
<td>The framework fails under prompt injection, memory poisoning, or untrusted tool results.</td>
</tr>
<tr class="even">
<td>K10</td>
<td>The ledger remains documentation with no execution-time control function.</td>
</tr>
</tbody>
</table>



### 14.2 Series synthesis {#14-2-series-synthesis}

The suite converges on a single evaluation object: typed artifacts in structured environments, with validation, transformation stability, warrant, and effect control. Each essay supplies one layer of that object, and each layer has an associated failure mode and benchmark obligation.



<table>
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Essay</strong></th>
<th><strong>Core contribution</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Semantic Participation</td>
<td>Generated artifacts enter environments through validity conditions, alignment constraints, composition rules, reuse paths, and review procedures.</td>
</tr>
<tr class="even">
<td>Typed Generativity</td>
<td>Generation is target-type inference followed by candidate-inhabitant construction.</td>
</tr>
<tr class="odd">
<td>Functorial Consistency</td>
<td>Systems should preserve relevant transformations across source and target representations.</td>
</tr>
<tr class="even">
<td>Lambek Machines</td>
<td>Grammar-as-logic supplies a testable interface for typed compositional behavior in language models.</td>
</tr>
<tr class="odd">
<td>Algebraic Architectures</td>
<td>Model families encode structural commitments about objects, symmetries, operations, memory, modality, interfaces, and validation.</td>
</tr>
<tr class="even">
<td>Quantitative Curry-Howard</td>
<td>Scores, uncertainty, losses, calibration, validators, repair, and epistemic type form a warrant layer around typed artifacts.</td>
</tr>
<tr class="odd">
<td>Effectful and Conceptual Intelligence</td>
<td>Agent action requires authority, effects, state changes, handlers, validators, rollback, audit, and controlled transfer.</td>
</tr>
</tbody>
</table>



The resulting program is world-centric in a technical sense. Intelligence is evaluated through the construction, transformation, validation, warranting, and execution of typed artifacts inside structured environments under declared effects and calibrated warrant. The program earns rigor only when records improve diagnosis, validators improve review, benchmarks reveal hidden failures, scores predict useful outcomes, and ledgers change action control.

## Appendix A. Typed Action Ledger schema {#appendix-a-typed-action-ledger-schema}

**typed_action_ledger**



<table>
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Specification</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ledger_id</td>
<td>Unique ledger identifier.</td>
</tr>
<tr class="even">
<td>task</td>
<td>Task id, user goal, policy context, risk level, initial memory snapshot, environment snapshot, and capability context.</td>
</tr>
<tr class="odd">
<td>entries</td>
<td>Entry id, timestamp, proposed-by field, instruction sources, observation sources, action text, and action type.</td>
</tr>
<tr class="even">
<td>action contract</td>
<td>Preconditions, postconditions, declared effects, and frame conditions.</td>
</tr>
<tr class="odd">
<td>effect attributes</td>
<td>Reversibility, persistence, authority, trust source, impact, and validation type.</td>
</tr>
<tr class="even">
<td>capabilities</td>
<td>Capabilities required and capabilities granted.</td>
</tr>
<tr class="odd">
<td>control records</td>
<td>Handler, authorization result, execution result, observed state delta, validator, validation result, diagnostics, repair or rollback, permitted downstream use, and audit status.</td>
</tr>
<tr class="even">
<td>frame conditions</td>
<td>Modifiable state and state that must remain preserved.</td>
</tr>
</tbody>
</table>



## Appendix B. Effectful Agent Benchmark schema {#appendix-b-effectful-agent-benchmark-schema}

**effectful_agent_benchmark_item**



<table>
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Specification</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>item_id</td>
<td>Unique item identifier.</td>
</tr>
<tr class="even">
<td>domain</td>
<td>Task domain and interface class.</td>
</tr>
<tr class="odd">
<td>goal</td>
<td>Target state or operational objective.</td>
</tr>
<tr class="even">
<td>initial_state</td>
<td>Environment, files, memory, tools, accounts, policies, and other relevant state.</td>
</tr>
<tr class="odd">
<td>policy_context</td>
<td>Rules, risk class, approvals, and constraints.</td>
</tr>
<tr class="even">
<td>allowed_effects</td>
<td>Effects authorized for the item.</td>
</tr>
<tr class="odd">
<td>forbidden_effects</td>
<td>Effects that violate state scope, policy, privacy, risk, or authority.</td>
</tr>
<tr class="even">
<td>required_preconditions</td>
<td>Checks required before execution.</td>
</tr>
<tr class="odd">
<td>required_postconditions</td>
<td>Checks required before completion can be asserted.</td>
</tr>
<tr class="even">
<td>frame_conditions</td>
<td>State regions protected from modification.</td>
</tr>
<tr class="odd">
<td>required_authority</td>
<td>Authority source and approval rule.</td>
</tr>
<tr class="even">
<td>rollback_requirements</td>
<td>Repair or compensation path.</td>
</tr>
<tr class="odd">
<td>untrusted_inputs</td>
<td>Pages, tool results, files, or observations treated as untrusted.</td>
</tr>
<tr class="even">
<td>validators</td>
<td>Success validator, side-effect validator, and audit requirements.</td>
</tr>
<tr class="odd">
<td>failure_labels</td>
<td>Unauthorized action, missing precondition, wrong postcondition, memory pollution, exfiltration, rollback failure, audit failure, and related labels.</td>
</tr>
</tbody>
</table>



## Appendix C. Concept Transfer Record schema {#appendix-c-concept-transfer-record-schema}

**concept_transfer_record**



<table>
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Specification</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>id</td>
<td>Unique transfer identifier.</td>
</tr>
<tr class="even">
<td>source_domain</td>
<td>Domain from which the concept, analogy, or schema is imported.</td>
</tr>
<tr class="odd">
<td>target_domain</td>
<td>Domain receiving the transfer.</td>
</tr>
<tr class="even">
<td>source_objects</td>
<td>Objects, roles, mechanisms, or relations in the source domain.</td>
</tr>
<tr class="odd">
<td>target_objects</td>
<td>Objects, roles, mechanisms, or relations in the target domain.</td>
</tr>
<tr class="even">
<td>preserved_relations</td>
<td>Relations that remain valid after transfer.</td>
</tr>
<tr class="odd">
<td>lost_relations</td>
<td>Relations that fail in the target setting.</td>
</tr>
<tr class="even">
<td>changed_relations</td>
<td>Relations requiring modification.</td>
</tr>
<tr class="odd">
<td>counterexamples</td>
<td>Cases that expose overtransfer or distortion.</td>
</tr>
<tr class="even">
<td>distortion_risk</td>
<td>How the transfer can mislead reasoning or action.</td>
</tr>
<tr class="odd">
<td>warrant</td>
<td>Evidence type supporting the transfer.</td>
</tr>
<tr class="even">
<td>permitted_use</td>
<td>Allowed use in explanation, hypothesis generation, design, or execution.</td>
</tr>
<tr class="odd">
<td>forbidden_use</td>
<td>Uses outside the evidence basis.</td>
</tr>
<tr class="even">
<td>review_status</td>
<td>Human, automated, or hybrid review result.</td>
</tr>
</tbody>
</table>



## Appendix D. Claim ledger {#appendix-d-claim-ledger}



<table>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
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
<td>Hoare logic, PDDL, monads, algebraic effects, and effect systems provide background formalisms for pre/post reasoning, planning, and computational effects.</td>
<td>L0</td>
<td>Cite source-functionally in the final bibliography.</td>
</tr>
<tr class="even">
<td>ReAct, Toolformer, OSWorld, tau-bench, AgentDojo, and AgentRewardBench motivate trajectory-level agent evaluation, tool use, user interaction, prompt-injection robustness, and trajectory judging.</td>
<td>L1</td>
<td>Support exact system and benchmark claims only.</td>
</tr>
<tr class="odd">
<td>Agent action should be evaluated as a typed, warranted, effectful trace.</td>
<td>L3</td>
<td>Original proposal in this essay.</td>
</tr>
<tr class="even">
<td>Typed Action Ledger and Effectful Agent Benchmark improve authorization, validation, repair, audit, memory quality, and skill reuse.</td>
<td>L4</td>
<td>Hypothesis to be tested.</td>
</tr>
<tr class="odd">
<td>Concept Transfer Records reduce conceptual overtransfer.</td>
<td>L4</td>
<td>Hypothesis to be tested.</td>
</tr>
</tbody>
</table>




<section class="bibliography" aria-labelledby="references-heading" data-review="unapproved">
<h2 id="references-heading">References (provisional)</h2>
<p class="bibliography-note">Source-scoped working citations. Text and references await specialist and author review.</p>
<ol class="references-list">
<li id="ref-Hoare1969" data-source-key="Hoare1969" data-provisional="true"><span class="ref-key">[1]</span>. <a href="https://doi.org/10.1145/363235.363259" rel="noopener noreferrer">An Axiomatic Basis for Computer Programming</a>. <span class="ref-details">C. A. R. Hoare · Communications of the ACM 12(10), 1969.</span></li>
<li id="ref-PDDL1998" data-source-key="PDDL1998" data-provisional="true"><span class="ref-key">[2]</span>. <a href="https://homepages.inf.ed.ac.uk/mfourman/tools/propplan/pddl.pdf" rel="noopener noreferrer">PDDL—The Planning Domain Definition Language, Version 1.2</a>. <span class="ref-details">McDermott et al. · AIPS-98 technical report.</span></li>
<li id="ref-Moggi1989" data-source-key="Moggi1989" data-provisional="true"><span class="ref-key">[3]</span>. <a href="https://lics.siglog.org/1989/Moggi-Computationallambda.html" rel="noopener noreferrer">Computational Lambda-Calculus and Monads</a>. <span class="ref-details">Eugenio Moggi · LICS 1989.</span></li>
<li id="ref-PlotkinPretnar2013" data-source-key="PlotkinPretnar2013" data-provisional="true"><span class="ref-key">[4]</span>. <a href="https://lmcs.episciences.org/705" rel="noopener noreferrer">Handling Algebraic Effects</a>. <span class="ref-details">Plotkin and Pretnar · Logical Methods in Computer Science 9(4), 2013.</span></li>
<li id="ref-AgentDojo2024" data-source-key="AgentDojo2024" data-provisional="true"><span class="ref-key">[5]</span>. <a href="https://proceedings.nips.cc/paper_files/paper/2024/hash/97091a5177d8dc64b1da8bf3e1f6fb54-Abstract-Datasets_and_Benchmarks_Track.html" rel="noopener noreferrer">AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents</a>. <span class="ref-details">Debenedetti et al. · NeurIPS 2024.</span></li>
<li id="ref-AgentRewardBench2025" data-source-key="AgentRewardBench2025" data-provisional="true"><span class="ref-key">[6]</span>. <a href="https://arxiv.org/abs/2504.08942" rel="noopener noreferrer">AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories</a>. <span class="ref-details">Lù et al. · arXiv preprint 2025.</span></li>
<li id="ref-Toolformer2023" data-source-key="Toolformer2023" data-provisional="true"><span class="ref-key">[7]</span>. <a href="https://proceedings.neurips.cc/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html" rel="noopener noreferrer">Toolformer: Language Models Can Teach Themselves to Use Tools</a>. <span class="ref-details">Schick et al. · NeurIPS 2023.</span></li>
</ol>
</section>
