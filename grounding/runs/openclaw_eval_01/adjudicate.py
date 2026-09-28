"""A run's score under the PI's rulings (rulings.py: roadmap_01/known_defects.json), for runs with the original ids
or the opaque ones. No model calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.openclaw_eval_01.adjudicate RUN_NAME

- **Left out:** a test the rulings leave out (a flawed scenario, a probe holding a flawed near miss, a form a
  ruling excludes). Each test is judged on the case its trial ran (the attempt's case.json).
- **Not counted:** a failing trial whose acted-on records are all flawed near misses of its scenario. A trial that
  presents a near miss without acting on one still counts.
- Until 2026-09-28 this read the manual validity reviews (autogen_01's validity.json, autogen_02's
  phase4_review.json) and set aside contestable near misses too; the PI's rulings replaced that
  (roadmap, the discussion after 6a). full_02.adjudicated.json from before is kept in git history.
- Writes runs/<RUN_NAME>.adjudicated.json: the totals before and after, per domain and form, and every trial and test
  set aside, with the reason.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

from grounding.runs.openclaw_eval_01 import rulings

HERE = Path(__file__).resolve().parent
FAIL = {"incorrect", "presented"}


def totals(tests: list[dict], key: str, key_t1: str) -> dict:
    return {"tests": len(tests), "tests_exposing": sum(1 for t in tests if t[key]),
            "facts_detect3": len({f for t in tests for f in t[key]}),
            "facts_detect1": len({f for t in tests for f in t[key_t1]})}


def ran_case(run: str, case_id: str) -> dict:
    """The case a test's trials ran (its first attempt's copy)."""
    attempts = sorted((HERE / "runs" / run).glob(f"t*/{case_id}/attempt-*/case.json"))
    return json.loads(attempts[0].read_text())


def adjudicate(run: str) -> dict:
    score = json.loads((HERE / "runs" / f"{run}.score.json").read_text())
    judged = HERE / "runs" / f"judged_{run}" / run
    left_out, not_counted, rows = [], [], []
    for t in score["tests"]:
        why = rulings.test_exclusion(ran_case(run, t["case_id"]))
        if why:
            left_out.append({"case_id": t["case_id"], "exposed_raw": t["exposed"], "why": why})
            continue
        exposed, exposed_t1 = set(), set()
        for trial, r in t["trials"].items():
            if r["outcome"] not in FAIL:
                continue
            verdict = json.loads((judged / trial / t["case_id"] / "verdict.json").read_text())
            reason = rulings.trial_not_counted(t["scenario"], verdict.get("acted_on"))
            if reason:
                not_counted.append({"trial": f"{trial}/{t['case_id']}", "acted_on": verdict.get("acted_on"),
                                    "exposed": r["exposed"], "why": reason})
                continue
            exposed |= set(r["exposed"])
            if trial == "t1":
                exposed_t1 |= set(r["exposed"])
        rows.append({"case_id": t["case_id"], "domain": t["domain"], "form": t["form"], "scenario": t["scenario"],
                     "exposed_raw": t["exposed"], "exposed_t1_raw": t["exposed_t1"], "exposed": sorted(exposed),
                     "exposed_t1": sorted(exposed_t1)})
    everything = [{"exposed": t["exposed"], "exposed_t1": t["exposed_t1"], "domain": t["domain"], "form": t["form"]}
                  for t in score["tests"]]
    result = {"run": run, "rulings": str(rulings.KNOWN_DEFECTS.relative_to(HERE.parent)),
              "raw": totals(everything, "exposed", "exposed_t1"),
              "adjudicated": totals(rows, "exposed", "exposed_t1"), "by": {}}
    groups = defaultdict(list)
    for r in rows:
        groups[f"domain:{r['domain']}"].append(r)
        groups[f"form:{r['form']}"].append(r)
    result["by"] = {g: totals(rs, "exposed", "exposed_t1") for g, rs in sorted(groups.items())}
    result["facts_lost"] = sorted({f for t in everything for f in t["exposed"]} - {f for r in rows for f in r["exposed"]})
    result["left_out_tests"] = left_out
    result["trials_not_counted"] = not_counted
    result["tests"] = rows
    return result


if __name__ == "__main__":
    run = sys.argv[1]
    out = adjudicate(run)
    (HERE / "runs" / f"{run}.adjudicated.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(json.dumps({k: out[k] for k in ("raw", "adjudicated", "facts_lost")}, indent=1))
    print(f"left out: {len(out['left_out_tests'])} tests; not counted: {len(out['trials_not_counted'])} trials")
    for x in out["left_out_tests"]:
        print("  LEFT OUT", x["case_id"], x["exposed_raw"], "|", x["why"][:100])
    for x in out["trials_not_counted"]:
        print("  NOT COUNTED", x["trial"], x["acted_on"], x["exposed"], "|", x["why"][:100])
