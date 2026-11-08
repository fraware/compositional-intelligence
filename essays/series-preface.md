# Series Preface

*Mateo Petel*

Generative AI produces artifacts that enter increasingly complex intellectual and operational environments. Proof sketches enter formal mathematical systems. Programs enter codebases governed by interfaces and invariants. Scientific protocols enter experimental workflows governed by measurement, controls, and evidential standards. Agents issue tool calls and modify persistent state. Each setting raises a question extending beyond the quality of an isolated response. How does a generated object acquire a defensible status inside the world that will use it?

**Compositional Intelligence** proposes a research program centered on that question. Its objects are typed artifacts in structured worlds. The program studies how such artifacts are constructed, checked, aligned with their sources, transformed, composed, warranted, reused, and executed under appropriate authority. Prediction quality, benchmark accuracy, and local task success retain their roles as evidence. The proposed framework adds evaluation of artifact status, preservation of relevant structure, and consequences of downstream use.

## From output to artifact

Typed artifacts include formal proofs, programs, mathematical statements, semantic parses, experimental protocols, datasets, claims, plans, memory updates, and tool calls. Each artifact is interpreted relative to an environment that specifies admissible representations, dependencies, validators, transformations, epistemic classifications, and permitted uses.

The distinction carries several obligations. Proof checking establishes validity relative to a formal statement and a trusted checking regime. Source–target alignment addresses the relation of that statement to its intended meaning. Scientific evidence supports claims within declared assumptions and uncertainty bounds. Tool execution introduces state transitions whose authority and effects need independent assessment. Compositional Intelligence organizes these obligations around the artifact and its position in the environment.

## Three foundations

The first three essays establish the program's core sequence.

**Semantic Participation** studies the conditions under which a candidate artifact receives a usable status in a structured environment. Validation, source alignment, composability, epistemic classification, and permitted use are recorded as distinct conditions of membership.

**Typed Generativity** analyzes target-class inference and the generation of candidate representations. On a declared normalized joint distribution, the factorization follows the probability chain rule.

$
\begin{aligned}
P_{\theta}(A,t\mid c) &= P_{\theta}(A\mid c)\\
&\quad\cdot P_{\theta}(t\mid A,c).
\end{aligned}
$ The generator context $c$ is distinct from the formal typing environment; $A$ denotes a target-class label and $t$ denotes a candidate that can fail validation. Formal acceptance uses the independent judgment $\Delta\vdash\operatorname{parse}(t):\tau$ under an explicit mapping from the target label to type τ. Semi-formal tasks need declared validators, and claims about latent type-like representations remain empirical hypotheses.

**Functorial Consistency** studies the preservation of relevant relations under transformations. The evaluation pattern compares two well-typed routes through a source-to-target transformation. For source operation $f:X\to X^{\prime}$, transports $T_0:X\to Y$ and $T_1:X^{\prime}\to Y^{\prime}$, and target operation $g:Y\to Y^{\prime}$, a declared relation $R$ compares $T_1(f(x))$ and $g(T_0(x))$. The validator and relation determine the result and its evidentiary status. This is a proposed family of path-agreement tests. Mathematical functoriality introduces additional identity and composition obligations.

Together, these concepts define the destination of generation, the construction problem, and a test of structural preservation.

## Language, architecture, evidence, and action

Four companion essays develop the program across additional domains.

**Lambek Machines** treats categorial linguistic structure as a candidate interface for supervision, interpretation, and evaluation of language systems. Its empirical question concerns downstream semantic behavior under controlled transformations.

**Algebraic Architectures** investigates task specifications as constraints on architectural choice. Object structure, symmetries, interfaces, and validators provide a basis for comparing architectural commitments against domain requirements. Formal satisfaction, structural support and empirical performance receive distinct evidence grades.

**Quantitative Curry–Howard** separates scores used for search, probabilistic support, relaxed satisfaction, and exact validation. Candidate artifacts acquire evidence records whose semantics and calibration determine their appropriate use. A learned score retains its evidential meaning within its specified validation regime.

**Effectful and Conceptual Intelligence** extends artifact evaluation to actions and state changes. Typed action records relate instructions, authority, preconditions, effects, execution, validation, repair, memory, and audit. Their effectiveness as runtime controls depends on independently evaluated authorization gates and state-transition enforcement.

## An empirical research agenda

The proposed schemas and benchmark protocols are research designs. Their scientific value depends on implementation and comparative evaluation. Useful tests would establish whether the records improve failure diagnosis, validation, repair, compositional generalization, architecture selection, calibration, downstream reuse, or control of agent effects. Independent baselines and explicit failure criteria are central to that assessment.

The essays distinguish established mathematical and technical foundations from the program's original proposals. Formal validity is judged by the applicable formal system. Empirical claims are judged by the corresponding evidence and evaluation design. Interpretive claims remain tied to their assumptions. This separation preserves the scientific status of each contribution.

The sequence begins with membership, continues through construction and structural preservation, and extends toward language, architecture, evidence, and action. Read together, the essays propose a common way to study intelligent systems through the objects they place into structured worlds and the relationships those objects sustain.
