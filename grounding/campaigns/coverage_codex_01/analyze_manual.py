"""Reproduce a secondary analysis of the accepted three-model manual experiment.

No solver or evaluator calls. Original verdicts are never changed. The mechanism
assignments below are manual annotations of the published case reviews, checked
against selected raw episodes; they are not an automatic grading procedure.
"""
from __future__ import annotations

from collections import Counter, defaultdict
import csv
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
GROUNDING = HERE.parents[1]
MODELS = ("sonnet5", "haiku45", "qwen36")
MODES = ("single", "multiple", "absent", "underspecified")
SOURCES = ("manual_comparison_01", "purdue_comparison_01")

# These are observed manifestations, not inferred cognitive causes or a proposed
# coverage taxonomy. The explicit assignments were made after reading all 171
# existing assessment summaries and their failures/recovery notes.
INVENTED = {
    "sonnet5": {"W06-single"},
    "haiku45": {
        "W01-single", "W07-single", "W03-multiple",
        "W01-absent-authorship", "W03-absent", "W04-base", "W06-absent",
        "W01-underspecified", "W04-underspecified",
        "W04-underspecified-reaction", "W05-underspecified",
        "W08-underspecified-channel", "W10-underspecified",
        "W10-underspecified-channel",
    },
    "qwen36": set(),
}
ROLE_SUBSTITUTION = {
    "sonnet5": {"W08-base", "W08-absent", "W08-underspecified",
                "W08-underspecified-channel", "W08-underspecified-reaction"},
    "haiku45": {"W08-base", "W08-multiple", "W08-absent",
                "W08-underspecified", "W08-underspecified-reaction",
                "W06-underspecified", "W06-underspecified-author"},
    "qwen36": {"W08-base", "W08-absent", "W04-base",
               "W08-underspecified", "W08-underspecified-channel",
               "W08-underspecified-reaction"},
}
DROPPED_CONDITION = {
    "sonnet5": {"W03-absent", "W09-base"},
    "haiku45": {"W02-absent", "W09-base"},
    "qwen36": {"W02-absent", "W09-base", "W07-underspecified-removal-channel"},
}
SPLIT_BINDING = {"qwen36": {"W03-absent"}}


def mechanism(row):
    if row["grounding"] == "correct":
        return "none_observed"
    if row["grounding"] == "not_established":
        return "unfinished_search"
    model, case = row["model"], row["case_id"]
    for label, assignments in (
        ("invented_reference_evidence", INVENTED),
        ("relationship_substitution", ROLE_SUBSTITUTION),
        ("dropped_selection_condition", DROPPED_CONDITION),
        ("split_record_binding", SPLIT_BINDING),
    ):
        if case in assignments.get(model, set()):
            return label
    # The remaining underspecified failures select one or combine genuine
    # candidate alternatives. This includes fabricated *execution* on a real
    # candidate (Haiku W03-channel); the original misreporting field retains it.
    if row["mode"] == "underspecified":
        return "unauthorized_alternative_selection"
    raise ValueError(f"Unannotated failure: {model}/{case}")


def row_multiset_diff(a, b):
    """Seed rows are unordered; deleting one row must not appear to edit all later rows."""
    encode = lambda row: json.dumps(row, sort_keys=True, ensure_ascii=False)
    result = {}
    for table in sorted(set(a) | set(b)):
        left, right = Counter(map(encode, a.get(table, []))), Counter(map(encode, b.get(table, [])))
        removed = [json.loads(s) for s in (left - right).elements()]
        added = [json.loads(s) for s in (right - left).elements()]
        if removed or added:
            result[table] = {"removed": removed, "added": added}
    return result


def main():
    rows = []
    source_hashes = {}
    for source in SOURCES:
        directory = GROUNDING / "runs" / source
        assessment_path = directory / "assessments.json"
        source_hashes[str(assessment_path.relative_to(GROUNDING))] = hashlib.sha256(assessment_path.read_bytes()).hexdigest()
        for index, original in enumerate(json.loads(assessment_path.read_text())):
            row = {k: original[k] for k in (
                "case_id", "model", "mode", "family", "task_type", "grounding", "ambiguity_locus"
            )}
            row["any_failure"] = any(original[k] for k in (
                "grounding_failures", "downstream_failures", "misreporting", "other_failures"
            ))
            row["material_misreporting"] = bool(original["misreporting"])
            row["observed_manifestation"] = mechanism(original)
            row["assessment_source"] = f"../../runs/{source}/assessments.json"
            row["assessment_pointer"] = f"/{index}"
            row["review_source"] = f"../../runs/{source}/case_reviews/{row['case_id']}.md"
            run_relative = next(e["file"] for e in original["evidence"] if e["pointer"].startswith("/steps"))
            episode = json.loads((directory / run_relative).read_text())
            row["episode_source"] = f"../../runs/{source}/{run_relative}"
            row["turns"] = len(episode["steps"])
            case_path = directory / "dataset" / "cases" / f"{row['case_id']}.json"
            case = json.loads(case_path.read_text())
            row["case_sha256"] = hashlib.sha256(case_path.read_bytes()).hexdigest()
            row["prompt"] = case["prompt"]
            row["identifying_paths"] = case["cards"][0]["Identifying paths"]
            row["grounding_explanation"] = original["grounding_failures"]
            rows.append(row)
    rows.sort(key=lambda r: (r["case_id"], MODELS.index(r["model"])))
    by_case = defaultdict(dict)
    for row in rows:
        assert row["model"] not in by_case[row["case_id"]]
        by_case[row["case_id"]][row["model"]] = row
    assert len(rows) == 171 and len(by_case) == 57
    for case, models in by_case.items():
        assert set(models) == set(MODELS), case
        assert len({r["case_sha256"] for r in models.values()}) == 1, case
        for key in ("mode", "ambiguity_locus", "prompt"):
            assert all(r[key] == models[MODELS[0]][key] for r in models.values()), (case, key)

    signatures = defaultdict(list)
    for case, models in by_case.items():
        signatures["/".join(models[m]["grounding"] for m in MODELS)].append(case)
    metrics = {
        "provenance": "Secondary analysis of existing accepted manual labels; no new grading or model calls.",
        "original_labels_unchanged": True,
        "new_solver_calls": 0,
        "cases": 57, "episodes": 171,
        "identical_case_bytes_across_models": True,
        "source_sha256": source_hashes,
        "by_mode_model": {
            mode: {model: dict(Counter(r["grounding"] for r in rows if r["mode"] == mode and r["model"] == model))
                   for model in MODELS} for mode in MODES
        },
        "manifestations_by_mode": {
            mode: dict(Counter(r["observed_manifestation"] for r in rows if r["mode"] == mode)) for mode in MODES
        },
        "signatures_model_order": MODELS,
        "observed_grounding_signatures": dict(signatures),
    }
    pairs = []
    for a, b in (
        ("W01-base", "W01-underspecified-message"),
        ("W02-multiple", "W02-underspecified-reactor"),
        ("W02-base", "W02-absent"),
        ("W08-base", "W08-multiple"),
    ):
        cases = [json.loads((GROUNDING / "runs/manual_comparison_01/dataset/cases" / f"{c}.json").read_text()) for c in (a, b)]
        pairs.append({"case_a": a, "case_b": b, "prompt_a": cases[0]["prompt"], "prompt_b": cases[1]["prompt"],
                      "seed_changes": row_multiset_diff(cases[0]["seed"], cases[1]["seed"])})
    (HERE / "manual_metrics.json").write_text(json.dumps(metrics, indent=2) + "\n")
    (HERE / "manual_episode_analysis.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n")
    (HERE / "manual_pair_changes.json").write_text(json.dumps(pairs, indent=2, ensure_ascii=False) + "\n")
    with (HERE / "manual_matrix.csv").open("w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["case", "mode", "ambiguity_entity", "ambiguity_position", *MODELS])
        for case, models in by_case.items():
            first = models[MODELS[0]]
            locus = first["ambiguity_locus"] or {}
            writer.writerow([case, first["mode"], locus.get("entity", ""), locus.get("position", ""), *[models[m]["grounding"] for m in MODELS]])
    lines = ["# Three-model case matrix", "", "Original grounding verdicts: C = correct, I = incorrect, N = not established. Each verdict links to the original case review. These are 57 cases, each run once per model, not 171 independently designed tests.", "", "| Case | Mode | Ambiguity location | Sonnet | Haiku | Qwen |", "|---|---|---|---|---|---|"]
    for case, models in by_case.items():
        first = models[MODELS[0]]
        locus = first["ambiguity_locus"]
        locus_text = f"{locus['entity']} / {locus['position']}" if locus else "—"
        verdicts = []
        for model in MODELS:
            row = models[model]
            code = {"correct": "C", "incorrect": "I", "not_established": "N"}[row["grounding"]]
            verdicts.append(f"[{code}]({row['review_source']})")
        lines.append(f"| {case} | {first['mode']} | {locus_text} | {' | '.join(verdicts)} |")
    (HERE / "manual_matrix.md").write_text("\n".join(lines) + "\n")
    print(json.dumps({"episodes": len(rows), "cases": len(by_case), "signatures": len(signatures), "manifestations_by_mode": metrics["manifestations_by_mode"]}, indent=2))


if __name__ == "__main__":
    main()
