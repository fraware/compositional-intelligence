#!/usr/bin/env python3
"""Verify synthetic commuting-square cases over exact integer polynomials.

This module validates a diagnostic taxonomy and a fixture file. It does not
evaluate a language model, estimate benchmark performance, or establish an
advantage over metamorphic testing. No dynamic code execution is performed.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
import re
from typing import Any

LABELS = frozenset({
    "valid_agreement",
    "invalid_agreement",
    "left_path_fault",
    "right_path_fault",
    "unresolved_disagreement",
})
CASE_FIELDS = frozenset({
    "id", "reference", "transform_then_translate",
    "translate_then_transform", "expected_classification",
})
MAX_DEGREE = 8
MAX_COEFFICIENT = 1_000_000


@dataclass(frozen=True, slots=True)
class Case:
    """One synthetic case with a complete, independently fixed polynomial oracle."""

    case_id: str
    reference: tuple[int, ...]
    left: tuple[int, ...]
    right: tuple[int, ...]
    expected_classification: str


def polynomial(value: Any) -> tuple[int, ...]:
    """Parse a bounded coefficient vector, lowest power first.

    Reject booleans, floats, oversized vectors, and noncanonical empty inputs.
    Trailing zeros are harmless representation differences.
    """
    if not isinstance(value, list) or not 1 <= len(value) <= MAX_DEGREE + 1:
        raise ValueError("Polynomial coefficients must form a nonempty bounded list")
    if any(type(c) is not int or abs(c) > MAX_COEFFICIENT for c in value):
        raise ValueError("Polynomial coefficients must be bounded integers")
    while len(value) > 1 and value[-1] == 0:
        value = value[:-1]
    return tuple(value)


def value_at(coefficients: tuple[int, ...], n: int) -> int:
    """Evaluate an integer polynomial exactly by Horner's rule."""
    result = 0
    for coefficient in reversed(coefficients):
        result = result * n + coefficient
    return result


def first_disagreement(
    left: tuple[int, ...], right: tuple[int, ...]
) -> int | None:
    """Find a complete witness for unequal polynomials over the integers.

    A nonzero polynomial of degree d has at most d distinct roots. Testing
    integer points 0 through d is complete for this bounded polynomial domain.
    No completeness claim applies to arbitrary programs or sampled validators.
    """
    if left == right:
        return None
    degree_bound = max(len(left), len(right)) - 1
    for n in range(degree_bound + 1):
        if value_at(left, n) != value_at(right, n):
            return n
    raise AssertionError("A nonzero polynomial cannot have more roots than its degree")


def classify(case: Case) -> dict[str, Any]:
    """Separate path agreement, independent correctness, and fault attribution."""
    agree = case.left == case.right
    left_valid = case.left == case.reference
    right_valid = case.right == case.reference
    if agree:
        label = "valid_agreement" if left_valid else "invalid_agreement"
    elif right_valid and not left_valid:
        label = "left_path_fault"
    elif left_valid and not right_valid:
        label = "right_path_fault"
    else:
        label = "unresolved_disagreement"

    return {
        "id": case.case_id,
        "classification": label,
        "path_agreement": agree,
        "transform_then_translate_valid": left_valid,
        "translate_then_transform_valid": right_valid,
        "disagreement_witness": first_disagreement(case.left, case.right),
    }


def load_cases(path: Path) -> list[Case]:
    """Read the complete fixture schema and reject mislabeled or duplicate cases."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"Cannot read synthetic fixture file: {exc}") from exc
    if not isinstance(data, dict) or set(data) != {
        "schema_version", "purpose", "cases"
    }:
        raise ValueError("Incorrect synthetic fixture document schema")
    if data["schema_version"] != 1 or data["purpose"] != "synthetic_control_only":
        raise ValueError("Fixture must explicitly identify its synthetic status")
    raw = data["cases"]
    if not isinstance(raw, list) or not 1 <= len(raw) <= 256:
        raise ValueError("Fixture must contain 1–256 synthetic cases")
    seen: set[str] = set()
    cases: list[Case] = []
    for record in raw:
        if not isinstance(record, dict) or set(record) != CASE_FIELDS:
            raise ValueError("Incorrect synthetic case fields")
        case_id = record["id"]
        if (not isinstance(case_id, str)
            or not re.fullmatch(r"case_[a-z0-9_]+", case_id)
            or case_id in seen):
            raise ValueError("Missing, invalid, or duplicate case identifier")
        seen.add(case_id)
        label = record["expected_classification"]
        if label not in LABELS:
            raise ValueError(f"Unrecognized diagnostic label: {label!r}")
        case = Case(
            case_id=case_id,
            reference=polynomial(record["reference"]),
            left=polynomial(record["transform_then_translate"]),
            right=polynomial(record["translate_then_transform"]),
            expected_classification=label,
        )
        observed = classify(case)["classification"]
        if observed != case.expected_classification:
            raise ValueError(
                f"{case_id}: fixture label {label!r} conflicts with {observed!r}"
            )
        cases.append(case)
    return cases


def main() -> int:
    """Validate every fixture and print deterministic, clearly labeled records."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--fixtures", type=Path,
        default=Path(__file__).with_name("synthetic_cases.json"),
    )
    args = parser.parse_args()
    try:
        cases = load_cases(args.fixtures)
    except ValueError as exc:
        parser.exit(2, f"Invalid synthetic fixtures: {exc}\n")
    report = {
        "status": "synthetic_control_only_not_empirical_evidence",
        "acceptance_relation": "exact_integer_polynomial_equality",
        "fixture_count": len(cases),
        "records": [classify(case) for case in cases],
    }
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
