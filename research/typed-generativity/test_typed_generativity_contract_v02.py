#!/usr/bin/env python3
"""Adversarial checks for the Typed Generativity V5 publication and benchmark.

Tests operate exclusively on synthetic fixtures; they validate implementation
invariants and text conservation, never scientific or benchmark effectiveness.
"""
from __future__ import annotations

import copy
import hashlib
import json
import re
import tempfile
import unittest
from pathlib import Path

from validate_typed_generativity_contract_v02 import (
    check_records, descriptive_summary, load_json, runner_view, trial_outcome,
)

ROOT = Path(__file__).resolve().parent


class ContractV02Tests(unittest.TestCase):
    """Structural, data-leak, annotation, and assignment checks."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = load_json(ROOT / "typed_generativity_benchmark_contract_v0.2.schema.json")
        cls.fixture = load_json(ROOT / "typed_generativity_synthetic_fixture_v0.2.json")

    def bundle(self):
        return copy.deepcopy(self.fixture)

    def errors(self, bundle):
        return check_records(bundle, self.schema)

    def assert_issue(self, bundle, substring):
        errors = self.errors(bundle)
        self.assertTrue(any(substring in e for e in errors), errors)

    def test_nominal_synthetic_fixture_passes(self):
        self.assertEqual(self.errors(self.bundle()), [])

    def test_runner_projection_excludes_gold_scoring_and_model_artifacts(self):
        view = runner_view(self.bundle())
        self.assertEqual(set(view), {"protocol_version", "dataset_id", "tasks"})
        self.assertEqual(set(view["tasks"][0]), {"task_id", "domain", "prompt", "prompt_sha256"})
        raw = json.dumps(view)
        for forbidden in ("stable-dedup-int", "SYNTHETIC_ARTIFACT", "criteria", "judgments",
                          "assignment_manifest_sha256", "declared_target_text"):
            self.assertNotIn(forbidden, raw)

    def test_prompt_digest_tamper(self):
        bundle = self.bundle()
        bundle["tasks"][0]["prompt_sha256"] = "f"*64
        self.assert_issue(bundle, "Prompt digest mismatch")

    def test_missing_assigned_run_is_detected(self):
        bundle = self.bundle()
        bundle["runs"] = bundle["runs"][:1]
        self.assert_issue(bundle, "Missing preallocated trial")

    def test_missing_assignments_not_solved_by_exclusion_label(self):
        bundle = self.bundle()
        bundle["runs"][1]["analysis_population"] = "excluded_preassignment"
        self.assert_issue(bundle, "was excluded or reassigned")

    def test_unplanned_extra_trial_is_detected(self):
        bundle = self.bundle()
        extra = copy.deepcopy(bundle["runs"][1])
        extra.update(run_id="extra-run", trial_index=1, order_index=2, session_id="third-session")
        bundle["runs"].append(extra)
        self.assert_issue(bundle, "Unplanned primary trial")

    def test_duplicate_task_trial_is_detected(self):
        bundle = self.bundle()
        extra = copy.deepcopy(bundle["runs"][1])
        extra.update(run_id="duplicate-run", order_index=2, session_id="third-session")
        bundle["runs"].append(extra)
        self.assert_issue(bundle, "Duplicate task-condition-trial")

    def test_unknown_task_reference_reports_and_does_not_crash(self):
        bundle = self.bundle()
        bundle["runs"][0]["task_id"] = "unknown-task"
        self.assert_issue(bundle, "unknown task")

    def test_duplicated_session_is_rejected(self):
        bundle = self.bundle()
        bundle["runs"][1]["session_id"] = bundle["runs"][0]["session_id"]
        self.assert_issue(bundle, "Reused session_id")

    def test_artifact_for_refused_run_is_rejected(self):
        bundle = self.bundle()
        bundle["runs"][0]["termination"] = "refused"
        self.assert_issue(bundle, "Schema/")

    def test_refusal_is_counted_as_failure_under_assignment(self):
        bundle = self.bundle()
        run = bundle["runs"][0]
        run.update(termination="refused", artifact=None,
                   artifact_extraction_status="not_applicable",declared_target_text=None)
        bundle["judgments"] = [j for j in bundle["judgments"] if j["run_id"] != run["run_id"]]
        self.assertEqual(self.errors(bundle), [])
        summary = descriptive_summary(bundle)
        self.assertEqual(summary["domains"]["code"]["dispositions_by_condition"]["deliberation"],
                         {"model_noncompletion": 1})
        self.assertEqual(summary["domains"]["code"]["effect_bound_lower"], 0)

    def test_infrastructure_failure_is_unknown_not_model_failure(self):
        bundle = self.bundle()
        run = bundle["runs"][0]
        run.update(termination="infrastructure_error", artifact=None,
                   artifact_extraction_status="not_applicable",declared_target_text=None)
        bundle["judgments"] = [j for j in bundle["judgments"] if j["run_id"] != run["run_id"]]
        self.assertEqual(self.errors(bundle), [])
        summary = descriptive_summary(bundle)
        row = summary["domains"]["code"]
        self.assertEqual((row["effect_bound_lower"],row["effect_bound_upper"]),(-1.0,0.0))
        self.assertEqual(row["dispositions_by_condition"]["deliberation"],
                         {"infrastructure_missing":1})

    def test_indeterminate_mandatory_criterion_produces_bounds(self):
        bundle = self.bundle()
        final = next(j for j in bundle["judgments"] if j["run_id"]=="synthetic-run-1"
                     and j["criterion_id"]=="target-alignment" and j["phase"]=="final")
        final.update(execution_status="unavailable",verdict="indeterminate",evidence_reference=None)
        self.assertEqual(self.errors(bundle), [])
        row=descriptive_summary(bundle)["domains"]["code"]
        self.assertEqual((row["effect_bound_lower"],row["effect_bound_upper"]),(-1.0,0.0))

    def test_any_rejected_mandatory_criterion_is_failure(self):
        bundle = self.bundle()
        for j in bundle["judgments"]:
            if j["run_id"] == "synthetic-run-2" and j["criterion_id"] == "test-fixture" and j["phase"] == "final":
                j.update(execution_status="unavailable",verdict="indeterminate",evidence_reference=None)
        row=descriptive_summary(bundle)["domains"]["code"]
        self.assertEqual((row["effect_bound_lower"],row["effect_bound_upper"]),(-1.0,-1.0))

    def test_missing_final_mandatory_assessment_is_detected(self):
        bundle = self.bundle()
        bundle["judgments"] = [j for j in bundle["judgments"] if not (
            j["run_id"]=="synthetic-run-1" and j["criterion_id"]=="test-fixture" and j["phase"]=="final")]
        self.assert_issue(bundle, "Missing single final mandatory judgment")

    def test_nonexecuted_judgment_cannot_be_accepted(self):
        bundle = self.bundle()
        bundle["judgments"][0]["execution_status"] = "not_run"
        self.assert_issue(bundle, "Nonexecuted assessment")

    def test_duplicate_final_is_detected(self):
        bundle = self.bundle()
        j=next(j for j in bundle["judgments"] if j["phase"]=="final")
        bundle["judgments"].append(copy.deepcopy(j))
        self.assert_issue(bundle, "Duplicate final")

    def test_same_initial_and_final_assessor_is_detected(self):
        bundle = self.bundle()
        final=next(j for j in bundle["judgments"] if j["run_id"]=="synthetic-run-1"
                   and j["criterion_id"]=="target-alignment" and j["phase"]=="final")
        final["assessor_id"]="synthetic-human-1"
        self.assert_issue(bundle, "also supplied initial")

    def test_human_criterion_needs_two_distinct_initial_reviewers(self):
        bundle = self.bundle()
        for j in bundle["judgments"]:
            if j["assessor_id"]=="synthetic-human-2":
                j["assessor_id"]="synthetic-human-1"
        self.assert_issue(bundle, "two distinct initial reviewers")

    def test_target_alignment_is_mandatory(self):
        bundle = self.bundle()
        bundle["tasks"][0]["criteria"][0]["mandatory"] = False
        self.assert_issue(bundle, "lacks a mandatory target-alignment")

    def test_unresolved_target_excluded_from_confirmatory_one_shot(self):
        bundle = self.bundle()
        bundle["tasks"][0]["intent_status"] = "unresolved"
        bundle["tasks"][0]["admissible_target_ids"] = []
        self.assert_issue(bundle, "Unresolved task")

    def test_ambiguous_item_needs_adjudicated_admissible_target_set(self):
        bundle = self.bundle()
        bundle["tasks"][0]["intent_status"] = "admissibly_ambiguous"
        bundle["tasks"][0]["admissible_target_ids"] = []
        self.assert_issue(bundle, "Adjudicated task")

    def test_incompatible_evidence_grade_is_detected(self):
        bundle = self.bundle()
        bundle["tasks"][0]["criteria"][1]["evidence_grade"]="expert_review"
        self.assert_issue(bundle, "labels expert judgment as automatic")

    def test_output_is_descriptive_and_not_confidence_interval(self):
        summary=descriptive_summary(self.bundle())
        self.assertFalse(summary["statistical_confidence_interval_computed"])
        self.assertEqual(summary["domains"]["code"]["assigned_trial_count"],2)
        self.assertIsNone(summary["six_domain_macro_average"])
        self.assertIn("NOT empirical evidence",summary["interpretation"])

    def test_duplicate_json_key_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/"dup.json"
            p.write_text('{"a":1,"a":2}',encoding="utf-8")
            with self.assertRaisesRegex(ValueError,"Duplicate JSON"):
                load_json(p)

    def test_nonfinite_json_value_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/"nan.json"
            p.write_text('{"v":NaN}',encoding="utf-8")
            with self.assertRaisesRegex(ValueError,"Non-finite"):
                load_json(p)


class ManuscriptV5Tests(unittest.TestCase):
    """Check that the published V5 manuscript preserves original V3 evidence."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.original = (ROOT / "historical-v3-source.md").read_text(encoding="utf-8")
        cls.v5 = (
            ROOT.parents[1] / "essays" / "typed-generativity.md"
        ).read_text(encoding="utf-8")

    @staticmethod
    def tables(source: str) -> list[str]:
        """Return complete source tables, including all original data cells."""
        return re.findall(
            r'<table data-source-table="\d+" id="table-\d+">[\s\S]*?</table>',
            source,
        )

    def test_all_original_tables_byte_exact(self) -> None:
        original = self.tables(self.original)
        self.assertEqual(len(original), 15)
        self.assertEqual(self.tables(self.v5), original)

    def test_original_headings_preserved(self) -> None:
        original = set(re.findall(r'<h[23] id="([^"]+)"', self.original))
        current = set(re.findall(r'<h[23] id="([^"]+)"', self.v5))
        self.assertTrue(original <= current)
        self.assertGreater(len(current), len(original))

    def test_no_duplicate_html_ids(self) -> None:
        ids = re.findall(r'\bid="([^"]+)"', self.v5)
        self.assertEqual(len(ids), len(set(ids)))

    def test_domain_and_outcome_sections_included(self) -> None:
        for anchor in (
            "domain-specific-acceptance-and-evidence",
            "trial-disposition-and-missing-evidence",
            "appendix-e.-primary-outcome-derivation",
            "appendix-f.-domain-evidence-boundaries",
        ):
            with self.subTest(anchor=anchor):
                self.assertIn(f'id="{anchor}"', self.v5)

    def test_reader_map_has_real_section_7_4(self) -> None:
        self.assertIn("Sections 6.4, 7.4, 8, 9, and 11", self.v5)
        self.assertIn('id="identification-and-analysis-protocol"', self.v5)

    def test_editorial_provenance_and_current_checksum(self) -> None:
        self.assertIn("AUTHORITATIVE-DOCX SHA256", self.original)
        self.assertIn("AUTHORITATIVE-DOCX SHA256", self.v5)
        self.assertNotIn("Publication editorial revision V5", self.original)
        self.assertIn("Publication editorial revision V5", self.v5)
        publication_record = json.loads(
            (ROOT.parents[1] / "sources" / "originals.json").read_text(
                encoding="utf-8"
            )
        )["documents"]["typed-generativity"]
        self.assertEqual(
            hashlib.sha256(self.v5.encode("utf-8")).hexdigest(),
            publication_record["markdown_sha256"],
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
