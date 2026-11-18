#!/usr/bin/env python3
"""Validate Typed Generativity v0.2 assigned-trial records.

This module checks schema conformance, identifiers, assignment coverage,
criterion-review structure, and deterministic outcome dispositions. It neither
executes an LLM nor independently verifies validators, artifacts, or reviewer
independence. Summaries are descriptive; no confidence interval is computed.

Usage:
  python validate_typed_generativity_contract_v02.py BUNDLE.json \
      --schema typed_generativity_benchmark_contract_v0.2.schema.json \
      --summary summary.json --runner-view tasks_only.json

Python >=3.11; jsonschema>=4.18,<5.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from hashlib import sha256
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker


Outcome = tuple[int, int, str]  # lower, upper, disposition


def load_json(path: Path) -> dict[str, Any]:
    """Load one UTF-8 JSON object, rejecting duplicate keys and non-finite numbers."""
    def unique_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        obj: dict[str, Any] = {}
        for key, value in pairs:
            if key in obj:
                raise ValueError(f"Duplicate JSON object key: {key!r}")
            obj[key] = value
        return obj

    def reject_nonfinite(token: str) -> None:
        raise ValueError(f"Non-finite JSON numeric literal: {token}")

    with path.open(encoding="utf-8") as stream:
        obj = json.load(stream, object_pairs_hook=unique_pairs,
                        parse_constant=reject_nonfinite)
    if not isinstance(obj, dict):
        raise ValueError(f"Root must be a JSON object: {path}")
    return obj


def check_records(bundle: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    """Return structural and cross-record issues, never asserting empirical validity.

    Schema errors short-circuit cross-record checks because subsequent code
    relies on required typed fields; independent issues are accumulated once
    those prerequisites are satisfied.
    """
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = [
        f"Schema/{'/'.join(map(str, error.absolute_path))}: {error.message}"
        for error in validator.iter_errors(bundle)
    ]
    if errors:
        return sorted(set(errors))

    tasks: dict[str, dict[str, Any]] = {}
    runs: dict[str, dict[str, Any]] = {}
    criteria_by_task: dict[str, dict[str, dict[str, Any]]] = {}
    judgments_by_pair: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    seen_assignments: set[tuple[str, str, int]] = set()
    orders: set[int] = set()
    sessions: set[str] = set()

    for task in bundle["tasks"]:
        tid = task["task_id"]
        if tid in tasks:
            errors.append(f"Duplicate task_id {tid}")
            continue
        tasks[tid] = task
        if sha256(task["prompt"].encode("utf-8")).hexdigest() != task["prompt_sha256"]:
            errors.append(f"Prompt digest mismatch for {tid}")
        ids = [c["criterion_id"] for c in task["criteria"]]
        if len(set(ids)) != len(ids):
            errors.append(f"Duplicate criterion_id for {tid}")
        criteria_by_task[tid] = {c["criterion_id"]: c for c in task["criteria"]}
        if not any(c["mandatory"] for c in task["criteria"]):
            errors.append(f"Task {tid} lacks mandatory criteria")
        if not any(c["mandatory"] and c["role"] == "target_alignment" for c in task["criteria"]):
            errors.append(f"Task {tid} lacks a mandatory target-alignment criterion")
        for criterion in task["criteria"]:
            mode, grade = criterion["assessment_mode"], criterion["evidence_grade"]
            if grade == "expert_review" and mode == "automatic":
                errors.append(f"Criterion {tid}/{criterion['criterion_id']} labels expert judgment as automatic")
            if grade == "formal_kernel_check" and mode == "human":
                errors.append(f"Criterion {tid}/{criterion['criterion_id']} lacks a machine formal checker")
        if task["intent_status"] in ("determinate", "admissibly_ambiguous") and not task["admissible_target_ids"]:
            errors.append(f"Adjudicated task {tid} has no admissible targets")
        if (task["split"] == "confirmatory" and task["analysis_cohort"] == "one_shot"
                and task["intent_status"] == "unresolved"):
            errors.append(f"Unresolved task {tid} entered confirmatory one-shot cohort")
        intended_cohort = ("interactive" if task["clarification_policy"] ==
                           "interactive_separate_cohort" else "one_shot")
        if task["analysis_cohort"] != intended_cohort:
            errors.append(f"Task {tid} clarification policy contradicts its cohort")
        if task["split"] == "confirmatory" and task["analysis_cohort"] == "one_shot":
            required = set(bundle["design"]["primary_conditions"])
            if not required <= set(task["eligible_conditions"]):
                errors.append(f"Confirmatory one-shot task {tid} lacks both primary conditions")

    for run in bundle["runs"]:
        rid, tid = run["run_id"], run["task_id"]
        if rid in runs:
            errors.append(f"Duplicate run_id {rid}")
            continue
        runs[rid] = run
        if tid not in tasks:
            errors.append(f"Run {rid} references unknown task {tid}")
        else:
            task = tasks[tid]
            if run["assigned_condition"] not in task["eligible_conditions"]:
                errors.append(f"Run {rid} is ineligible for its assigned condition")
            is_primary = (task["split"] == bundle["design"]["primary_split"]
                          and task["analysis_cohort"] == bundle["design"]["primary_cohort"]
                          and run["assigned_condition"] in bundle["design"]["primary_conditions"])
            if run["analysis_population"] == "primary" and not is_primary:
                errors.append(f"Run {rid} is labeled primary outside the primary design")
            if is_primary and run["analysis_population"] != "primary":
                errors.append(f"Preassigned primary slot {rid} was excluded or reassigned")
        key = (tid, run["assigned_condition"], run["trial_index"])
        if key in seen_assignments:
            errors.append(f"Duplicate task-condition-trial assignment {key}")
        seen_assignments.add(key)
        if run["order_index"] in orders:
            errors.append(f"Duplicate order_index {run['order_index']}")
        orders.add(run["order_index"])
        if run["session_id"] in sessions:
            errors.append(f"Reused session_id {run['session_id']} (isolation not evidenced)")
        sessions.add(run["session_id"])
        if run["observed_output_tokens"] > run["max_output_tokens"]:
            errors.append(f"Run {rid} exceeded its output-token limit")
        if run["termination"] == "completed" and run["artifact_extraction_status"] == "extracted" and not run["artifact"]:
            errors.append(f"Run {rid} has empty extracted artifact")
        if run["termination"] != "completed" and run["declared_target_text"] is not None:
            # A partial target trace is possible. It is allowed, but does not supply a final artifact.
            pass

    # Explicit coverage is essential: absent rows cannot be silently dropped.
    R = bundle["design"]["repetitions_per_task"]
    for tid, task in tasks.items():
        if task["split"] != "confirmatory" or task["analysis_cohort"] != "one_shot":
            continue
        for condition in bundle["design"]["primary_conditions"]:
            for trial_index in range(R):
                if (tid, condition, trial_index) not in seen_assignments:
                    errors.append(f"Missing preallocated trial {tid}/{condition}/{trial_index}")
            extras = [x for x in seen_assignments if x[0] == tid and x[1] == condition and x[2] >= R]
            for extra in extras:
                errors.append(f"Unplanned primary trial {extra}")

    for judgment in bundle["judgments"]:
        rid, cid = judgment["run_id"], judgment["criterion_id"]
        if rid not in runs:
            errors.append(f"Judgment references unknown run {rid}")
            continue
        tid = runs[rid]["task_id"]
        if tid not in criteria_by_task:
            continue
        if cid not in criteria_by_task[tid]:
            errors.append(f"Judgment for {rid} references unknown criterion {cid}")
            continue
        judgments_by_pair[(rid, cid)].append(judgment)
        if runs[rid]["termination"] != "completed" or runs[rid]["artifact_extraction_status"] != "extracted":
            errors.append(f"Judgment attached to nonassessable run {rid}/{cid}")
        if judgment["execution_status"] != "executed" and judgment["verdict"] != "indeterminate":
            errors.append(f"Nonexecuted assessment {rid}/{cid} has definitive verdict")
        if judgment["execution_status"] == "executed" and not judgment["evidence_reference"]:
            errors.append(f"Executed assessment {rid}/{cid} lacks evidence reference")

    for rid, run in runs.items():
        task = tasks.get(run["task_id"])
        if not task:
            continue
        # Nonproduced artifacts do not need fabricated reviewer judgments.
        assessable = (run["termination"] == "completed" and
                      run["artifact_extraction_status"] == "extracted")
        for criterion in task["criteria"]:
            cid = criterion["criterion_id"]
            group = judgments_by_pair[(rid, cid)]
            finals = [j for j in group if j["phase"] == "final"]
            if len(finals) > 1:
                errors.append(f"Duplicate final judgments for {rid}/{cid}")
            if not (criterion["mandatory"] and assessable):
                continue
            if len(finals) != 1:
                errors.append(f"Missing single final mandatory judgment for {rid}/{cid}")
                continue
            final = finals[0]
            mode = criterion["assessment_mode"]
            if mode == "automatic" and final["assessor_kind"] != "machine":
                errors.append(f"Automatic final {rid}/{cid} lacks machine assessor")
            if mode in ("human", "hybrid"):
                humans = [j for j in group if j["phase"] == "initial" and j["assessor_kind"] == "human"]
                distinct = {j["assessor_id"] for j in humans}
                if len(distinct) < 2:
                    errors.append(f"Human criterion {rid}/{cid} lacks two distinct initial reviewers")
                if final["assessor_kind"] != "adjudicator":
                    errors.append(f"Human criterion {rid}/{cid} lacks final adjudicator")
                if final["assessor_id"] in distinct:
                    errors.append(f"Adjudicator for {rid}/{cid} also supplied initial human review")
            if mode == "hybrid" and not any(
                j["phase"] == "initial" and j["assessor_kind"] == "machine"
                for j in group
            ):
                errors.append(f"Hybrid criterion {rid}/{cid} lacks machine assessment")
    return sorted(set(errors))


def runner_view(bundle: dict[str, Any]) -> dict[str, Any]:
    """Export an explicit allowlist with no gold targets, rubrics, or judgments."""
    return {
        "protocol_version": bundle["protocol_version"],
        "dataset_id": bundle["dataset_id"],
        "tasks": [{
            "task_id": task["task_id"], "domain": task["domain"],
            "prompt": task["prompt"], "prompt_sha256": task["prompt_sha256"],
        } for task in bundle["tasks"]],
    }


def trial_outcome(run: dict[str, Any], finals: dict[str, dict[str, Any]],
                  mandatory: list[str]) -> Outcome:
    """Return deterministic artifact-acceptance bounds for one preassigned run."""
    term = run["termination"]
    if term in ("refused", "generation_error", "budget_timeout"):
        return (0, 0, "model_noncompletion")
    if term in ("infrastructure_error", "infrastructure_timeout", "not_started"):
        return (0, 1, "infrastructure_missing")
    extraction = run["artifact_extraction_status"]
    if extraction == "empty":
        return (0, 0, "no_artifact")
    if extraction == "ambiguous":
        return (0, 1, "extraction_indeterminate")
    if extraction != "extracted":
        return (0, 1, "extraction_inconsistent")
    decisions = [finals.get(cid) for cid in mandatory]
    if any(j is not None and j["verdict"] == "rejected" for j in decisions):
        return (0, 0, "criterion_rejected")
    if decisions and all(j is not None and j["verdict"] == "accepted" for j in decisions):
        return (1, 1, "accepted")
    return (0, 1, "assessment_indeterminate")


def descriptive_summary(bundle: dict[str, Any]) -> dict[str, Any]:
    """Calculate assigned-trial bounds, never treating missing runs as successes.

    Call check_records() first. This is a fixed-corpus descriptive summary,
    not a confidence interval or population-level treatment estimate.
    """
    tasks = {t["task_id"]: t for t in bundle["tasks"]}
    finals = defaultdict(dict)
    for judgment in bundle["judgments"]:
        if judgment["phase"] == "final":
            finals[judgment["run_id"]][judgment["criterion_id"]] = judgment
    per_task = defaultdict(lambda: defaultdict(list))
    status_counts = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    for run in bundle["runs"]:
        if run["analysis_population"] != "primary":
            continue
        task = tasks[run["task_id"]]
        mandatory = [c["criterion_id"] for c in task["criteria"] if c["mandatory"]]
        lower, upper, disposition = trial_outcome(run, finals[run["run_id"]], mandatory)
        per_task[run["task_id"]][run["assigned_condition"]].append((lower, upper))
        status_counts[task["domain"]][run["assigned_condition"]][disposition] += 1
    by_domain = defaultdict(list)
    L, T = bundle["design"]["primary_conditions"]
    for tid, conditions in per_task.items():
        task = tasks[tid]
        def avg(cond: str, side: int) -> float:
            data = conditions[cond]
            return sum(x[side] for x in data) / len(data)
        by_domain[task["domain"]].append({
            "task_id": tid,
            "effect_lower": avg(T,0) - avg(L,1),
            "effect_upper": avg(T,1) - avg(L,0),
        })
    domains={}
    for domain, rows in sorted(by_domain.items()):
        domains[domain] = {
            "task_count": len(rows),
            "assigned_trial_count": sum(sum(v.values()) for v in status_counts[domain].values()),
            "effect_bound_lower": sum(r["effect_lower"] for r in rows)/len(rows),
            "effect_bound_upper": sum(r["effect_upper"] for r in rows)/len(rows),
            "dispositions_by_condition": {
                c: dict(sorted(status_counts[domain][c].items())) for c in (L,T)
            },
        }
    expected={"code","lean_math","explanation","scientific_protocol","planning","tool_use"}
    macro=None
    if set(domains)==expected:
        macro={
            "effect_bound_lower":sum(v["effect_bound_lower"] for v in domains.values())/len(expected),
            "effect_bound_upper":sum(v["effect_bound_upper"] for v in domains.values())/len(expected),
            "weighting":"equal_domain_macro_average",
        }
    return {
        "dataset_id":bundle["dataset_id"],
        "record_kind":bundle["record_kind"],
        "interpretation":"synthetic checker demonstration; NOT empirical evidence" if bundle["record_kind"]=="synthetic_example" else "descriptive; independent scientific audit still needed",
        "primary_conditions":[L,T],
        "domains":domains,
        "six_domain_macro_average":macro,
        "statistical_confidence_interval_computed":False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("records", type=Path)
    parser.add_argument("--schema", type=Path, required=True)
    parser.add_argument("--runner-view", type=Path)
    parser.add_argument("--summary", type=Path)
    args = parser.parse_args()
    try:
        schema = load_json(args.schema)
        bundle = load_json(args.records)
        Draft202012Validator.check_schema(schema)
        errors = check_records(bundle, schema)
        if errors:
            for error in errors:
                print("ERROR:",error)
            return 1
        outputs = [(args.runner_view, runner_view(bundle)),
                   (args.summary, descriptive_summary(bundle))]
        for target, payload in outputs:
            if target is None:
                continue
            if target.resolve() in (args.records.resolve(), args.schema.resolve()):
                raise ValueError("Output would overwrite a source input")
            target.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
        print(f"PASS: {len(bundle['tasks'])} tasks; {len(bundle['runs'])} assigned runs; "
              f"{len(bundle['judgments'])} judgments. Structural checks only.")
        return 0
    except (OSError,ValueError,json.JSONDecodeError) as exc:
        print("ERROR:",exc)
        return 1

if __name__=="__main__":
    raise SystemExit(main())
