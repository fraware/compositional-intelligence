#!/usr/bin/env python3
"""Unit tests for synthetic polynomial commutation diagnostics.

These checks establish software behavior only, not measured model capability.
"""
from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from evaluate import Case, LABELS, classify, first_disagreement, load_cases, polynomial, value_at

HERE = Path(__file__).resolve().parent


class SyntheticCommutationTests(unittest.TestCase):
    def test_fixture_taxonomy_is_complete(self) -> None:
        cases = load_cases(HERE / "synthetic_cases.json")
        self.assertGreaterEqual(len(cases), 8)
        self.assertEqual({classify(c)["classification"] for c in cases}, LABELS)
        for case in cases:
            self.assertEqual(classify(case)["classification"], case.expected_classification)

    def test_missing_finite_witness_does_not_imply_equivalence(self) -> None:
        """The manuscript's n=1 agreement coexists with an n=2 counterexample."""
        left = polynomial([0, 1, 1])
        right = polynomial([1, 0, 1])
        self.assertEqual(value_at(left, 1), value_at(right, 1))
        self.assertNotEqual(value_at(left, 2), value_at(right, 2))
        self.assertIsNotNone(first_disagreement(left, right))

    def test_polynomial_root_bound_finds_late_witness(self) -> None:
        """Difference n(n-1) has roots at 0 and 1; point 2 identifies it."""
        left = polynomial([0, -1, 1])
        zero = polynomial([0])
        self.assertEqual(first_disagreement(left, zero), 2)
        self.assertIsNone(first_disagreement(polynomial([3, 0, 0]), polynomial([3])))

    def test_agreement_is_not_sufficient_for_correctness(self) -> None:
        case = Case(
            "case_invalid", polynomial([1, 0, 1]),
            polynomial([0, 1, 1]), polynomial([0, 1, 1]),
            "invalid_agreement",
        )
        result = classify(case)
        self.assertTrue(result["path_agreement"])
        self.assertFalse(result["transform_then_translate_valid"])
        self.assertFalse(result["translate_then_transform_valid"])
        self.assertEqual(result["classification"], "invalid_agreement")

    def test_disagreement_does_not_always_localize_a_fault(self) -> None:
        case = Case(
            "case_ambiguous", polynomial([1, 0, 1]),
            polynomial([0, 1, 1]), polynomial([2, 0, 1]),
            "unresolved_disagreement",
        )
        self.assertEqual(classify(case)["classification"], "unresolved_disagreement")

    def test_reject_invalid_coefficients(self) -> None:
        for value in ([], [True], [1.5], ["1"], [10**7], [0]*10, 1, None):
            with self.subTest(value=value), self.assertRaises(ValueError):
                polynomial(value)

    def test_reject_mislabelled_or_duplicate_fixtures(self) -> None:
        data = json.loads((HERE / "synthetic_cases.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.json"
            duplicate = dict(data)
            duplicate["cases"] = [data["cases"][0], data["cases"][0]]
            path.write_text(json.dumps(duplicate), encoding="utf-8")
            with self.assertRaises(ValueError):
                load_cases(path)
            mislabeled = dict(data)
            bad = dict(data["cases"][0])
            bad["expected_classification"] = "invalid_agreement"
            mislabeled["cases"] = [bad]
            path.write_text(json.dumps(mislabeled), encoding="utf-8")
            with self.assertRaises(ValueError):
                load_cases(path)


if __name__ == "__main__":
    unittest.main()
