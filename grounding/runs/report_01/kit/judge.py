"""RQ5: judge v2 against the hand labels. Each blind sample was drawn at random from its run and labelled by hand
before any verdict on its trials was read. Outcomes collapse to fail (incorrect, presented), pass (correct,
correct_absent) and void (artifact, timeout, not established, incomplete). On trials both call usable: TP = both
fail, FP = judge fails a labelled pass, FN = judge passes a labelled failure, TN = both pass. Void disagreements are
counted apart. Also the same-facts agreement on trials both call failing.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.judge

Writes numbers/judge.json.
"""
from __future__ import annotations

from collections import Counter

from grounding.runs.report_01.kit.common import RUNS, load, write

FAIL, PASS = {"incorrect", "presented"}, {"correct", "correct_absent"}
OCP = "openclaw_eval_01/runs/policy"
# (agent, test kind, comparison file). OpenClaw: every blind sample of this study. Qwen in the toy harness
# (Purdue): judge v2's blind samples in autogen_02 (Phase 3's looks, the robustness runs, Phase 4's runs).
SAMPLES = [
    ("OpenClaw", "regular", "openclaw_eval_01/runs/judged_full_02/comparison_blind.json"),
    ("OpenClaw", "regular", "openclaw_eval_01/runs/judged_full_03/comparison_blind.json"),
    ("OpenClaw", "regular", "openclaw_eval_01/runs/judged_full_04/comparison_blind.json"),
    *[("OpenClaw", "absence", f"{OCP}/judged_absence_look{i}/comparison_blind.json") for i in (1, 2, 3, 4)],
    ("OpenClaw", "absence", f"{OCP}/judged_population_absence/comparison_blind.json"),
    ("OpenClaw", "absence", f"{OCP}/judged_population_6b_absence/comparison_blind.json"),
    *[("OpenClaw", "underspecified", f"{OCP}/judged_underspecified_look{i}/comparison_blind.json")
      for i in (1, 2, 3, 4)],
    ("OpenClaw", "underspecified", f"{OCP}/judged_population_underspecified/comparison_blind.json"),
    ("OpenClaw", "underspecified", f"{OCP}/judged_population_6b_underspecified/comparison_blind.json"),
    ("Qwen toy harness", "regular", "autogen_02/runs/phase4/judged/comparison_batch1_blind.json"),
    ("Qwen toy harness", "regular", "autogen_02/runs/phase4/judged/comparison_batch2_blind.json"),
    *[("Qwen toy harness", "absence", f"autogen_02/runs/judge2_phase3/comparison_absence_look{i}_blind.json")
      for i in (1, 2, 3)],
    ("Qwen toy harness", "absence", "autogen_02/runs/judge2_phase3/comparison_absence_look4_robustness_blind.json"),
    *[("Qwen toy harness", "underspecified",
       f"autogen_02/runs/judge2_phase3/comparison_underspecified_look{i}_blind.json") for i in (1, 2)],
    ("Qwen toy harness", "underspecified",
     "autogen_02/runs/judge2_phase3/comparison_underspecified_look2_robustness_blind.json"),
    ("Qwen toy harness", "policy (14 absence, 16 underspecified)",
     "autogen_02/runs/judge2_phase4_policy/comparison_batch1_policy_blind.json"),
]


def cls(outcome):
    return "fail" if outcome in FAIL else "pass" if outcome in PASS else "void"


def confusion(doc):
    c = Counter()
    for ref, judged in doc["confusion_ref_to_judge"].items():
        for j, n in judged.items():
            c[(cls(ref), cls(j))] += n
    fd = doc.get("failure_detection", {})
    same = fd.get("same_exposed_facts_when_both_fail", "")
    same_n, _, same_d = same.partition("/")
    return {"trials": sum(c.values()), "agree": sum(n for (a, b), n in c.items() if a == b),
            "TP": c[("fail", "fail")], "FP": c[("pass", "fail")], "FN": c[("fail", "pass")], "TN": c[("pass", "pass")],
            "void_both": c[("void", "void")], "judge_void_only": c[("fail", "void")] + c[("pass", "void")],
            "label_void_only": c[("void", "fail")] + c[("void", "pass")],
            "same_facts": int(same_n) if same_n.isdigit() else 0, "same_facts_of": int(same_d) if same_d.isdigit() else 0}


def main():
    rows = []
    for agent, kind, path in SAMPLES:
        rows.append({"agent": agent, "kind": kind, "file": path, **confusion(load(RUNS / path))})
    groups = {}
    for r in rows:
        for key in ((r["agent"], r["kind"]), (r["agent"], "all")):
            g = groups.setdefault(" / ".join(key), Counter())
            for k, v in r.items():
                if isinstance(v, int):
                    g[k] += v
    for g in groups.values():
        g["precision"] = f"{g['TP']}/{g['TP'] + g['FP']}"
        g["recall"] = f"{g['TP']}/{g['TP'] + g['FN']}"
    # 6c: judges given our tests, on the same hand-labelled trials (judge_baselines_01).
    score = load(RUNS / "judge_baselines_01/score.json")
    baselines = {k: score[k] for k in ("openclaw", "blind", "phase1", "all") if k in score}
    out = {"samples": rows, "groups": {k: dict(v) for k, v in groups.items()}, "judge_baselines_01": baselines}
    print(write("judge", out))
    for k, v in groups.items():
        print(f"{k:45s}", dict(v))


if __name__ == "__main__":
    main()
