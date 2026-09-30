"""Markdown tables for the README from compare.py's output (no model calls).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.judge_qwen_01.tables --out runs/selfhost --name labelled
"""
from __future__ import annotations

import argparse
from pathlib import Path

from grounding.runs.judge_qwen_01.common import HERE, load

GROUPS = ("fail", "nonfail", "void", "missing")
NAMES = {"fail": "failure", "nonfail": "nonfailure", "void": "void", "missing": "no verdict"}
OUTCOMES = ("incorrect", "presented", "correct", "correct_absent", "false_absence", "incomplete", "not_established",
            "artifact", "missing")


def detector_rows(against: dict, groups: list[str]) -> list[str]:
    head = ("| Labelled executions | Judge | TP | FP | FN | TN | Both void | Label void, judge not | "
            "Judge void, label not | No verdict | Precision | Recall | Same facts on TP |")
    out = [head, "|" + "---|" * 13]
    for g in groups:
        block = against[g]
        for judge in ("muse", "qwen"):
            d = block[judge]
            label_void = sum(v for k, v in d.items() if k.startswith("label_void_judge_"))
            judge_void = sum(v for k, v in d.items() if k.startswith("label_") and k.endswith("_judge_void")
                             and not k.startswith("label_void"))
            out.append(f"| {g} ({block['executions']}) | {judge.capitalize()} | {d.get('TP', 0)} | {d.get('FP', 0)} | "
                       f"{d.get('FN', 0)} | {d.get('TN', 0)} | {d.get('void_both', 0)} | {label_void} | {judge_void} | "
                       f"{d.get('missing', 0)} | {d['precision']} | {d['recall']} | {d['same_facts_on_TP']} |")
    return out


def matrix_rows(m: dict, row_name: str, col_name: str, keys) -> list[str]:
    cols = [k for k in keys if any(k in r for r in m.values())]
    rows = [k for k in keys if k in m]
    out = [f"| {row_name} \\ {col_name} | " + " | ".join(NAMES.get(c, c) for c in cols) + " | All |",
           "|---|" + "---:|" * (len(cols) + 1)]
    for r in rows:
        out.append(f"| {NAMES.get(r, r)} | " + " | ".join(str(m[r].get(c, 0) or "·") for c in cols) +
                   f" | {sum(m[r].values())} |")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--name", required=True)
    args = ap.parse_args()
    out = args.out if args.out.is_absolute() else HERE / args.out
    c = load(out / f"comparison_{args.name}.json")
    lines = []
    if "against_labels" in c:
        lines += ["**Against the reference labels**", ""]
        lines += detector_rows(c["against_labels"], ["all", "regular", "absence", "underspecified", "lead_310",
                                                     "blind_review_01"])
        lines += ["", "**Reference label (rows) against Qwen (columns), all labelled**", ""]
        lines += matrix_rows(c["against_labels"]["all"]["label_to_qwen"], "Label", "Qwen", GROUPS)
        lines += ["", "**Reference label (rows) against Muse (columns), all labelled**", ""]
        lines += matrix_rows(c["against_labels"]["all"]["label_to_muse"], "Label", "Muse", GROUPS)
        lines += ["", f"**The bar:** {c['bar']}", ""]
    q = c["qwen_vs_muse"]
    lines += ["**Qwen against Muse**", "", "| Executions | Both verdicts | Same group | Same outcome | "
              "Same facts when both fail | Same mechanism when both fail |", "|---|---:|---:|---:|---:|---:|"]
    for g, d in q.items():
        lines.append(f"| {g} ({d['executions']}) | {d['with_both_verdicts']} | {d['same_group']} | {d['same_outcome']} "
                     f"| {d['same_facts_when_both_fail']} | {d['same_mechanism_when_both_fail']} |")
    lines += ["", "**Muse (rows) against Qwen (columns), outcome groups**", ""]
    lines += matrix_rows(q["all"]["group_matrix_muse_to_qwen"], "Muse", "Qwen", GROUPS)
    lines += ["", "**Muse (rows) against Qwen (columns), exact outcomes**", ""]
    lines += matrix_rows(q["all"]["outcome_matrix_muse_to_qwen"], "Muse", "Qwen", OUTCOMES)
    lines += ["", f"**Disagreement types:** {c['disagreement_types']}", "", f"**Reliability:** {c['reliability']}"]
    print("\n".join(lines))


if __name__ == "__main__":
    main()
