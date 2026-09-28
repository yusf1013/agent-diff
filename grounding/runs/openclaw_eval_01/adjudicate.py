"""A run's score adjudicated by the manual validity reviews, as autogen_01 reported its arms and as the policy stage
chooses its units. No model calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.openclaw_eval_01.adjudicate RUN_NAME

- **The reviews:** autogen_01's (`autogen_01/eval/validity.json`) for its scenarios, autogen_02's
  (`autogen_02/eval/phase4_review.json`) for Phase 4's. Each gives a verdict per scenario and per near miss.
- **Left out:** the tests of a scenario a review judged invalid, and the tests it lists as invalid. The policy stage
  leaves out their units the same way (`sampler.review_exclusion`).
- **Not counted:** a failing trial whose acted-on records are all near misses a review judged contestable or invalid
  (autogen_01's `tables.adjudicated`). A trial that presents a near miss without acting on one still counts.
- Writes runs/<RUN_NAME>.adjudicated.json: the totals before and after, per domain and form, and every trial and test
  the adjudication set aside, with the review's reason.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS = HERE.parent
REVIEWS = [RUNS / "autogen_01" / "eval" / "validity.json", RUNS / "autogen_02" / "eval" / "phase4_review.json"]
FAIL = {"incorrect", "presented"}


def reviews() -> dict:
    out = {}
    for path in REVIEWS:
        out.update({sid: v for sid, v in json.loads(path.read_text()).items() if not sid.startswith("_")})
    return out


def kind(verdict: str) -> str:
    return verdict.split(":")[0].split(";")[0].strip()


def totals(tests: list[dict], key: str, key_t1: str) -> dict:
    return {"tests": len(tests), "tests_exposing": sum(1 for t in tests if t[key]),
            "facts_detect3": len({f for t in tests for f in t[key]}),
            "facts_detect1": len({f for t in tests for f in t[key_t1]})}


def adjudicate(run: str) -> dict:
    score = json.loads((HERE / "runs" / f"{run}.score.json").read_text())
    judged = HERE / "runs" / f"judged_{run}" / run
    rev = reviews()
    bad = {(sid, str(w)): verdict for sid, v in rev.items() for w, verdict in v.get("decoys", {}).items()
           if kind(verdict) in ("contestable", "invalid")}
    invalid_scenarios = {sid: v.get("note", "")[:200] for sid, v in rev.items() if kind(v.get("verdict", "")) == "invalid"}
    invalid_tests = {c for v in rev.values() for c in v.get("invalid_tests") or []}
    left_out, not_counted, rows = [], [], []
    for t in score["tests"]:
        base = {"case_id": t["case_id"], "domain": t["domain"], "form": t["form"], "scenario": t["scenario"],
                "exposed_raw": t["exposed"], "exposed_t1_raw": t["exposed_t1"]}
        if t["scenario"] in invalid_scenarios or t["case_id"] in invalid_tests:
            why = (f"scenario invalid in review: {invalid_scenarios[t['scenario']]}" if t["scenario"] in invalid_scenarios
                   else "test invalid in review")
            left_out.append({"case_id": t["case_id"], "exposed_raw": t["exposed"], "why": why})
            continue
        exposed, exposed_t1 = set(), set()
        for trial, r in t["trials"].items():
            if r["outcome"] not in FAIL:
                continue
            verdict = json.loads((judged / trial / t["case_id"] / "verdict.json").read_text())
            acted = [str(a) for a in verdict.get("acted_on") or []]
            if acted and all((t["scenario"], a) in bad for a in acted):
                not_counted.append({"trial": f"{trial}/{t['case_id']}", "acted_on": acted, "exposed": r["exposed"],
                                    "why": [bad[(t["scenario"], a)][:200] for a in acted]})
                continue
            exposed |= set(r["exposed"])
            if trial == "t1":
                exposed_t1 |= set(r["exposed"])
        rows.append({**base, "exposed": sorted(exposed), "exposed_t1": sorted(exposed_t1)})
    everything = [{"exposed": t["exposed"], "exposed_t1": t["exposed_t1"], "domain": t["domain"], "form": t["form"]}
                  for t in score["tests"]]
    result = {"run": run, "reviews": [str(p.relative_to(RUNS)) for p in REVIEWS],
              "raw": totals(everything, "exposed", "exposed_t1"),
              "adjudicated": totals(rows, "exposed", "exposed_t1"), "by": {}}
    groups = defaultdict(list)
    for r in rows:
        groups[f"domain:{r['domain']}"].append(r)
        groups[f"form:{r['form']}"].append(r)
    result["by"] = {g: totals(rs, "exposed", "exposed_t1") for g, rs in sorted(groups.items())}
    raw_facts = {f for t in everything for f in t["exposed"]}
    kept_facts = {f for r in rows for f in r["exposed"]}
    result["facts_lost"] = sorted(raw_facts - kept_facts)
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
        print("  NOT COUNTED", x["trial"], x["acted_on"], x["exposed"], "|", x["why"][0][:100])
