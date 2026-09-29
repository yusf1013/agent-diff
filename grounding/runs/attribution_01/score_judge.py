"""Source 1: the judges' own `artifact` calls against the development set's owners (plan.md).

    python grounding/runs/attribution_01/score_judge.py

For each judge and split, a "not the agent" flag is the verdict `artifact`; `not_established` is counted beside it.
Recall is over trials owned by the test, the mock or the harness; false alarms are over agent-owned failures and over
passing trials. The component a flag names is read from its `artifact_reason` by keyword and listed for review.
Also lists the judges' artifact calls on trials no one labelled, for a manual check of their precision.
Writes source1_judge.json. No model calls.
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS = HERE.parent
NOT_AGENT = ("test-wording", "test-construction", "mock", "harness")
SPLITS = {  # verdict folder -> split name
    "autogen_02/runs/judge2_phase3_attempt01": "autogen_02 Phase 3 (blind labels)",
    "autogen_02/runs/judge2_phase1": "autogen_02 Phase 1 (2 labels revised after v2)",
    "autogen_02/runs/judge2_phase3": "autogen_02 Phase 3 (blind labels)",
    "autogen_02/runs/judge2_phase4_policy": "autogen_02 Phase 4 policy (blind labels)",
    "autogen_02/runs/phase4/judged": "autogen_02 Phase 4 (blind labels)",
    "autogen_02/runs/judge2_panel": "fact_coverage_02 panel",
    "autogen_02/runs/muse_judge_dev": "fact_coverage_02 dev split",
    "autogen_02/runs/judge1_phase1": "autogen_02 Phase 1",
    "autogen_01/runs/judge_dev_02": "fact_coverage_02 dev split (tuned on)",
    "autogen_01/runs/judge_test_01": "fact_coverage_02 test split (held out)",
}
COMPONENT = [  # (component, pattern over the lower-cased artifact_reason), first match wins
    ("harness", r"timeout|timed out|turn limit|crash|sandbox|infrastructure"),
    ("test-construction", r"seed|uuid|label ids|invalid_name|not a valid|scenario"),
    ("mock", r"replica|ignor|filter|unreadable|error|rejected|not supported|returns null|lead:null"),
    ("test-wording", r"wording|ambigu|two readings|could mean|reads as|the request can"),
]


def component(reason: str) -> str:
    r = (reason or "").lower()
    return next((c for c, p in COMPONENT if re.search(p, r)), "unclear")


def score(rows, judge):
    tab = defaultdict(lambda: defaultdict(Counter))  # split -> owner -> judge outcome
    tests = defaultdict(lambda: defaultdict(set))  # split -> owner -> tests flagged / all
    named = []
    for r in rows:
        v = r.get("judge_" + judge)
        if not v:
            continue
        split = SPLITS[v["folder"]]
        tab[split][r["owner"]][v["outcome"]] += 1
        tests[split][r["owner"] + ":all"].add(r["test"])
        if v["outcome"] == "artifact":
            tests[split][r["owner"] + ":flagged"].add(r["test"])
            named.append({"key": r["key"], "owner": r["owner"], "also": r["also"], "doubtful": r["doubtful"],
                          "named": component(v.get("artifact_reason", "")),
                          "reason": (v.get("artifact_reason") or "")[:240]})
    out = {}
    for split, by_owner in tab.items():
        s = {}
        for owner, c in sorted(by_owner.items()):
            s[owner] = {"trials": sum(c.values()), "artifact": c["artifact"], "not_established": c["not_established"],
                        "tests": len(tests[split][owner + ":all"]),
                        "tests_flagged": len(tests[split][owner + ":flagged"]), "outcomes": dict(c)}
        out[split] = s
    return out, named


def pooled(rows, judge, doubtful=True):
    pos = [r for r in rows if r.get("judge_" + judge) and r["owner"] in NOT_AGENT and (doubtful or not r["doubtful"])]
    neg = [r for r in rows if r.get("judge_" + judge) and r["owner"] == "agent" and (doubtful or not r["doubtful"])]
    ok = [r for r in rows if r.get("judge_" + judge) and r["owner"] == "none"]
    flag = lambda r: r["judge_" + judge]["outcome"] == "artifact"
    return {"not_agent_trials": len(pos), "flagged": sum(map(flag, pos)),
            "by_owner": {o: [sum(flag(r) for r in pos if r["owner"] == o), sum(r["owner"] == o for r in pos)]
                         for o in NOT_AGENT},
            "agent_failures": len(neg), "false_alarms": sum(map(flag, neg)),
            "passing": len(ok), "flagged_passing": sum(map(flag, ok))}


def unlabelled_calls(labelled):
    calls = []
    for folder, split in SPLITS.items():
        for p in sorted((RUNS / folder).rglob("verdict.json")):
            v = json.loads(p.read_text())
            if v.get("outcome") == "artifact" and v["key"] not in labelled:
                calls.append({"folder": folder, "key": v["key"], "named": component(v.get("artifact_reason", "")),
                              "reason": (v.get("artifact_reason") or "")[:300]})
    return calls


def main():
    rows = json.loads((HERE / "devset.json").read_text())["rows"]
    result = {}
    for judge in ("v2", "v1_muse", "v1_sonnet"):
        by_split, named = score(rows, judge)
        result[judge] = {"pooled": pooled(rows, judge), "pooled_without_doubtful": pooled(rows, judge, False),
                         "by_split": by_split, "flags": named}
        print(f"\n=== judge {judge}: pooled {result[judge]['pooled']}")
        for split, s in by_split.items():
            print(f"  -- {split}")
            for owner, x in s.items():
                print(f"     {owner:18} trials {x['trials']:3d} (tests {x['tests']:3d})  artifact {x['artifact']:2d} "
                      f"(tests {x['tests_flagged']:2d})  not_established {x['not_established']:2d}  {x['outcomes']}")
        print("  flags and the component their reason names:")
        for f in named:
            mark = "ok " if f["named"] == f["owner"] or f["named"] in f["also"] else "-- "
            print(f"   {mark}{f['key']} owner={f['owner']} named={f['named']}: {f['reason'][:150]}")
    labelled = {r["key"] for r in rows}
    result["unlabelled_artifact_calls"] = unlabelled_calls(labelled)
    print(f"\n=== artifact calls on unlabelled trials: {len(result['unlabelled_artifact_calls'])}")
    for c in result["unlabelled_artifact_calls"]:
        print(f"   {c['folder'].split('/')[-1]:22} {c['key']} named={c['named']}: {c['reason'][:170]}")
    (HERE / "source1_judge.json").write_text(json.dumps(result, indent=1) + "\n")


if __name__ == "__main__":
    main()
