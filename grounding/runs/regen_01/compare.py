"""The halves side by side on OpenClaw's regular suite: the Sonnet-written half (autogen_01's arms, scored from
openclaw_eval_01's runs full_02 for Box and full_03 for the rest), the Muse-written half (Phase 4 in the same runs,
6b in full_04), and this study's regenerated half (runs/full_01), all scored by score.py (adjudicate's logic under
today's rulings, the 10-minute budget, the exposure filter). No model calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.regen_01.compare [--no-regen]

Writes eval/compare_regular.json: per half, tests, tests exposing a fact, facts at detect@3 and @1, by service and
form, and which of the 81 facts report_01 credits to the Sonnet half each half exposes at detect@3 (facts qualified
by service, as report_01 and coverage.py count them). A test belongs to the half of its scenario's writer (the suite
indexes' `source`).
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

from grounding.runs.regen_01 import score

HERE = Path(__file__).resolve().parent
OE_RUNS = HERE.parent / "openclaw_eval_01" / "runs"
REPORT = HERE.parent / "report_01" / "numbers" / "concise.json"  # as coverage.py: the Sonnet half's 81 credited facts


def half(scenario: str) -> str:
    if scenario.startswith(("AR-", "AP-", "AP2-")):
        return "Sonnet"
    return "Muse"


def totals(rows: list[dict]) -> dict:
    return {"tests": len(rows), "tests_exposing": sum(1 for r in rows if r["exposed"]),
            "facts_detect3": len({f for r in rows for f in r["exposed"]}),
            "facts_detect1": len({f for r in rows for f in r["exposed_t1"]})}


def qualified(rows: list[dict]) -> set[str]:
    """The facts exposed at detect@3, qualified by service ("linear A:Cycle.name")."""
    return {f"{r['domain']} {f}" for r in rows for f in r["exposed"]}


def main():
    groups: dict[str, list[dict]] = defaultdict(list)
    extra = {}
    for run in ("full_02", "full_03", "full_04"):
        out = score.adjudicate(run, OE_RUNS)
        rows = out["tests"]
        if run == "full_02":  # Box only: full_03 re-ran Calendar, Linear and Slack with opaque ids
            rows = [r for r in rows if r["domain"] == "box"]
        for r in rows:
            groups[half(r["scenario"])].append(r)
        extra[run] = {k: len(out[k]) for k in ("left_out_tests", "trials_not_counted", "trials_over_budget",
                                                "timeouts_under_host_load", "exposures_filtered")}
    if "--no-regen" not in sys.argv and (HERE / "runs" / "full_01.score.json").exists():
        out = score.adjudicate("full_01", HERE / "runs")
        groups["Muse regenerated"] = out["tests"]
        extra["full_01"] = {k: len(out[k]) for k in ("left_out_tests", "trials_not_counted", "trials_over_budget",
                                                     "timeouts_under_host_load", "exposures_filtered")}
    result = {"_about": __doc__.split("\n\n")[0], "counts": extra, "halves": {}}
    for name, rows in groups.items():
        by = defaultdict(list)
        for r in rows:
            by[f"domain:{r['domain']}"].append(r)
            by[f"form:{r['form']}"].append(r)
        result["halves"][name] = {"all": totals(rows), "by": {k: totals(v) for k, v in sorted(by.items())},
                                  "facts": sorted({f for r in rows for f in r["exposed"]})}
    if "Muse" in result["halves"] and "Muse regenerated" in result["halves"]:
        both = groups["Muse"] + groups["Muse regenerated"]
        result["halves"]["Muse-only suite"] = {"all": totals(both), "facts": sorted({f for r in both for f in r["exposed"]})}
    the81 = {f"{d} {f}" for d, fs in json.loads(REPORT.read_text())["writers"]["Sonnet"]["coverage"].items() for f in fs}
    result["the_81"] = {"facts": len(the81)}
    for name in ("Sonnet", "Muse regenerated"):
        if name in groups:
            hit = qualified(groups[name]) & the81
            result["the_81"][name] = {"exposed_detect3": len(hit), "facts": sorted(hit)}
    if "Sonnet" in groups and "Muse regenerated" in groups:
        s3, r3 = qualified(groups["Sonnet"]) & the81, qualified(groups["Muse regenerated"]) & the81
        result["the_81"]["both"] = sorted(s3 & r3)
        result["the_81"]["sonnet_only"] = sorted(s3 - r3)
        result["the_81"]["regenerated_only"] = sorted(r3 - s3)
    (HERE / "eval" / "compare_regular.json").write_text(json.dumps(result, indent=1) + "\n")
    for name, h in result["halves"].items():
        print(name, h["all"])
    print({k: (v if not isinstance(v, dict) else v.get("exposed_detect3")) for k, v in result["the_81"].items()
           if not isinstance(v, list)}, {k: len(v) for k, v in result["the_81"].items() if isinstance(v, list)})
    print(extra)


if __name__ == "__main__":
    main()
