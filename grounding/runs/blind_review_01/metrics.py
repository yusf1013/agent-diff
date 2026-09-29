"""Agreement summaries; no source-file access or label generation."""
from __future__ import annotations

from collections import Counter

GROUPS = ("nonfailure", "failure", "void")


def group(outcome):
    if outcome is None:
        return "uncertain"
    if outcome in {"incorrect", "presented"}:
        return "failure"
    if outcome in {"artifact", "not_established"}:
        return "void"
    assert outcome in {"correct", "correct_absent", "false_absence", "incomplete"}, outcome
    return "nonfailure"


def ratio(num, den):
    return num / den if den else None


def summarize(rows, comparator):
    """Rows have reference, comparator object/None, and fixed stratification weight."""
    available = [r for r in rows if r[comparator] is not None]
    eligible = [r for r in available if r["reference"]["outcome"] is not None]
    binary = [r for r in eligible if group(r["reference"]["outcome"]) != "void"
              and group(r[comparator]["outcome"]) != "void"]
    joint_fail = [r for r in binary if group(r["reference"]["outcome"]) == "failure"
                  and group(r[comparator]["outcome"]) == "failure"]

    def measure(pool, predicate):
        numerator = sum(bool(predicate(r)) for r in pool)
        weighted_num = sum(r["weight"] for r in pool if predicate(r))
        weighted_den = sum(r["weight"] for r in pool)
        return {"matches": numerator, "n": len(pool), "rate": ratio(numerator, len(pool)),
                "weighted_matches": weighted_num, "weighted_n": weighted_den,
                "weighted_rate": ratio(weighted_num, weighted_den)}

    def agree(r):
        return group(r["reference"]["outcome"]) == group(r[comparator]["outcome"])

    matrix = {g: {h: 0 for h in GROUPS} for g in GROUPS}
    weighted_matrix = {g: {h: 0.0 for h in GROUPS} for g in GROUPS}
    for r in eligible:
        ref = group(r["reference"]["outcome"])
        pred = group(r[comparator]["outcome"])
        matrix[ref][pred] += 1
        weighted_matrix[ref][pred] += r["weight"]
    tp, fn = matrix["failure"]["failure"], matrix["failure"]["nonfailure"]
    fp, tn = matrix["nonfailure"]["failure"], matrix["nonfailure"]["nonfailure"]
    # Conditional binary diagnostics exclude voids on either side; full matrix remains visible.
    binary_kappa = None
    if binary:
        n = len(binary)
        observed = (tp + tn) / n
        expected = ((tp + fn) * (tp + fp) + (tn + fp) * (tn + fn)) / n**2
        binary_kappa = (observed - expected) / (1 - expected) if expected != 1 else None
    return {
        "available": len(available), "uncertain_excluded": len(available) - len(eligible),
        "exact_outcome": measure(eligible, lambda r: r["reference"]["outcome"] == r[comparator]["outcome"]),
        "three_way": measure(eligible, agree), "binary": measure(binary, agree),
        "matrix_rows_reference_columns_comparator": matrix, "weighted_matrix": weighted_matrix,
        "binary_diagnostics": {"true_positive": tp, "false_positive": fp, "true_negative": tn,
                               "false_negative": fn, "precision": ratio(tp, tp + fp),
                               "recall": ratio(tp, tp + fn), "specificity": ratio(tn, tn + fp),
                               "kappa": binary_kappa},
        "exposed_fact_sets": measure(eligible, lambda r: set(r["reference"]["exposed"]) == set(r[comparator].get("exposed", []))),
        "exposed_fact_sets_joint_failures": measure(joint_fail, lambda r: set(r["reference"]["exposed"]) == set(r[comparator].get("exposed", []))),
        "mechanism_joint_failures": measure(joint_fail, lambda r: r["reference"]["mechanism"] == r[comparator].get("mechanism")),
        "reference_outcomes": dict(Counter(r["reference"]["outcome"] for r in eligible)),
        "comparator_outcomes": dict(Counter(r[comparator]["outcome"] for r in eligible)),
    }
