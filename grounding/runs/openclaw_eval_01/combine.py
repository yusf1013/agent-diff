"""The regular suite's final score on OpenClaw (the discussion after 6a, 2026-09-28): Box's tests from full_02 (their
ids are numbers, so they did not change) and the Calendar, Linear and Slack tests from full_03 (re-run with opaque
ids and test-side clocks), both adjudicated under the PI's rulings (adjudicate.py). No model calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.openclaw_eval_01.combine

Writes runs/final_regular.json: totals, per domain and per form, the facts at detect@3 and detect@1, and where each
test's result comes from.
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from grounding.runs.openclaw_eval_01.adjudicate import totals

HERE = Path(__file__).resolve().parent
PARTS = (("full_02", {"box"}), ("full_03", {"calendar", "linear", "slack"}))


def main():
    rows, left_out, not_counted, over_budget = [], [], [], []
    for run, domains in PARTS:
        adj = json.loads((HERE / "runs" / f"{run}.adjudicated.json").read_text())
        rows += [{**r, "run": run} for r in adj["tests"] if r["domain"] in domains]
        left_out += [{**x, "run": run} for x in adj["left_out_tests"] if _domain(x["case_id"]) in domains]
        not_counted += [{**x, "run": run} for x in adj["trials_not_counted"]
                        if _domain(x["trial"].split("/", 1)[1]) in domains]
        over_budget += [{**x, "run": run} for x in adj["trials_over_budget"]
                        if _domain(x["trial"].split("/", 1)[1]) in domains]
    groups = defaultdict(list)
    for r in rows:
        groups[f"domain:{r['domain']}"].append(r)
        groups[f"form:{r['form']}"].append(r)
    result = {"parts": {run: sorted(d) for run, d in PARTS}, "final": totals(rows, "exposed", "exposed_t1"),
              "by": {g: totals(rs, "exposed", "exposed_t1") for g, rs in sorted(groups.items())},
              "facts_detect3": sorted({f for r in rows for f in r["exposed"]}),
              "facts_detect1": sorted({f for r in rows for f in r["exposed_t1"]}),
              "left_out_tests": left_out, "trials_not_counted": not_counted, "trials_over_budget": over_budget,
              "tests": [{k: r[k] for k in ("case_id", "domain", "form", "scenario", "run", "exposed", "exposed_t1")}
                        for r in sorted(rows, key=lambda r: r["case_id"])]}
    (HERE / "runs" / "final_regular.json").write_text(json.dumps(result, indent=1) + "\n")
    print(json.dumps({k: result[k] for k in ("parts", "final", "by")}, indent=1))


def _domain(case_id: str) -> str:
    """A test's domain from its scenario id (…-BOX-…, …-CAL-…, …-LIN-…, …-SLK-…)."""
    for code, domain in (("-BOX-", "box"), ("-CAL-", "calendar"), ("-LIN-", "linear"), ("-SLK-", "slack")):
        if code in f"-{case_id}":
            return domain
    return "?"


if __name__ == "__main__":
    main()
