"""Qwen against itself: two replays of the same executions with the same settings (no model calls).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.judge_qwen_01.repeat_compare \
        --first runs/selfhost --second runs/selfhost_repeat --set labelled

Run-to-run agreement (outcome group, exact outcome, facts on joint failures) of two draws at the model's default
sampling, and, for the labelled set, each draw's standing against the bar (compare.detector on the same rows).
Writes <second>/repeat_<set>.json.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from grounding.runs.judge_qwen_01.common import HERE, cls, labels, load
from grounding.runs.judge_qwen_01.compare import detector, matrix


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--first", type=Path, required=True)
    ap.add_argument("--second", type=Path, required=True)
    ap.add_argument("--set", choices=["labelled", "all", "rest"], required=True)
    args = ap.parse_args()
    first, second = (p if p.is_absolute() else HERE / p for p in (args.first, args.second))
    ref = labels()
    rows = []
    for key in load(HERE / "sets" / f"{args.set}.json"):
        a, b = first / key / "verdict.json", second / key / "verdict.json"
        if not (a.exists() and b.exists()):
            continue
        va, vb, lab = load(a), load(b), ref.get(key)
        rows.append({"key": key, "first": va.get("outcome"), "second": vb.get("outcome"),
                     "first_cls": cls(va.get("outcome")), "second_cls": cls(vb.get("outcome")),
                     "first_exposed": sorted(va.get("exposed") or []), "second_exposed": sorted(vb.get("exposed") or []),
                     "label_cls": cls(lab["outcome"]) if lab else None,
                     "label_exposed": sorted(lab["exposed"]) if lab else [],
                     "label_mechanism": lab.get("mechanism") if lab else None,
                     "first_mechanism": va.get("mechanism"), "second_mechanism": vb.get("mechanism")})
    fails = [r for r in rows if r["first_cls"] == r["second_cls"] == "fail"]
    result = {"executions_with_both": len(rows), "same_group": sum(r["first_cls"] == r["second_cls"] for r in rows),
              "same_outcome": sum(r["first"] == r["second"] for r in rows),
              "same_facts_when_both_fail": f"{sum(r['first_exposed'] == r['second_exposed'] for r in fails)}/{len(fails)}",
              "group_matrix_first_to_second": matrix(rows, "first_cls", "second_cls"),
              "differing": [r["key"] for r in rows if r["first_cls"] != r["second_cls"]]}
    labelled = [r for r in rows if r["label_cls"]]
    if labelled:
        # detector() reads "<judge>_cls", "<judge>_exposed", "<judge>_mechanism"
        result["first_against_labels"] = detector(labelled, "first")
        result["second_against_labels"] = detector(labelled, "second")
    (second / f"repeat_{args.set}.json").write_text(json.dumps(result, indent=1) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "differing"}, indent=1),
          f"\n{len(result['differing'])} executions differ in outcome group")


if __name__ == "__main__":
    main()
