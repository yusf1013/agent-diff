"""Draw the case study's sample from the classified tests (no model calls).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.transfer_feasibility_01.sample

Eligible: realizable exactly (as_is or team), or with only the light changes (rename, date_shift without
multi_day), at most 4 people besides the actor, free plans only, no known-clock test, and not AR-LIN-24 (the PI's
two rulings on its near miss disagree). Per service, 10 tests:
- 6 regular tests: 3 that exposed a fact on OpenClaw (detect@3) and 3 that did not;
- 4 policy units: an absence and an underspecified unit that failed in at least 2 of their 3 OpenClaw trials, and
  one of each that failed in none (where no eligible unit passed every trial, the one with the fewest failures).
So both failure transfer (a failure on the mock that recurs on the real service) and false transfer (a new failure
on the real service) can be seen. Distinct scenarios where possible; seed 20260930.
A policy trial's OpenClaw outcome is Muse's verdict, and a trial over the 8-minute budget counts as a failure, as
in the study. Writes sample.csv and sample.json.
"""
from __future__ import annotations

import csv
import json
import random
from collections import Counter, defaultdict
from pathlib import Path

from grounding.runs.judge_qwen_01.common import attempt_path, final_keys, load, muse_dir
from grounding.runs.openclaw_eval_01 import rulings

HERE = Path(__file__).resolve().parent
LIGHT = {"rename", "date_shift"}
FAIL = {"incorrect", "presented"}
CONTESTED = {"AR-LIN-24"}  # the PI's rulings of 2026-09-28 and 2026-09-29 disagree on its "Cycle 4" near miss


def unit_failures() -> dict[str, list[str]]:
    """policy unit -> its OpenClaw trial outcomes (failure or not), by Muse's verdicts and the budget rule."""
    out = defaultdict(list)
    for key in final_keys():
        run, trial, unit = key.split("/")
        if run.startswith("full_"):
            continue
        p = muse_dir(key) / "verdict.json"
        outcome = load(p).get("outcome") if p.exists() else None
        failed = rulings.over_budget(attempt_path(key)) or outcome in FAIL
        out[unit].append("fail" if failed else "pass" if outcome in {"correct", "correct_absent"} else "void")
    return out


def eligible(r: dict) -> bool:
    tags = {t for t in r["changes"].split(";") if t and not t.startswith("accounts")}
    if r["class"] in ("as_is", "team"):
        ok = True
    elif r["class"] == "change":
        ok = tags <= LIGHT
    else:
        ok = False
    contested = r["scenario"] in CONTESTED
    return ok and not contested and int(r["people"]) <= 4 and "fixed clock" not in r["reasons"]


def main():
    rows = list(csv.DictReader((HERE / "tests.csv").open()))
    fails = unit_failures()
    for r in rows:
        if r["kind"] != "regular":
            outcomes = fails.get(r["id"], [])
            r["openclaw"] = f"{outcomes.count('fail')}/{len(outcomes)} trials failed"
            r["failed_on_openclaw"] = outcomes.count("fail") >= 2
            r["passed_on_openclaw"] = outcomes.count("fail") == 0 and outcomes.count("pass") >= 2
        else:
            r["openclaw"] = f"exposed {r['exposed_on_openclaw']}" if r["exposed_on_openclaw"] else "exposed nothing"
            r["failed_on_openclaw"] = bool(r["exposed_on_openclaw"])
            r["passed_on_openclaw"] = not r["exposed_on_openclaw"]
    pool = [r for r in rows if eligible(r)]
    rng = random.Random(20260930)
    picks = []
    for domain in ("box", "calendar", "linear", "slack"):
        used = set()
        wants = [("regular", True, 3), ("regular", False, 3), ("absence", True, 1), ("absence", False, 1),
                 ("underspecified", True, 1), ("underspecified", False, 1)]
        for kind, failed, n in wants:
            cand = [r for r in pool if r["domain"] == domain and r["kind"] == kind and
                    (r["failed_on_openclaw"] if failed else r["passed_on_openclaw"])]
            if not cand and not failed and kind != "regular":  # no unit passed all its trials: fewest failures
                rest = [r for r in pool if r["domain"] == domain and r["kind"] == kind and r["id"] not in
                        {p["id"] for p in picks}]
                low = min((int(r["openclaw"].split("/")[0]) for r in rest), default=None)
                cand = [r for r in rest if int(r["openclaw"].split("/")[0]) == low]
            rng.shuffle(cand)
            cand.sort(key=lambda r: r["scenario"] in used)  # new scenarios first, order kept otherwise
            for r in cand[:n]:
                used.add(r["scenario"])
                picks.append({**r, "stratum": f"{domain}/{kind}/{'failed' if failed else 'passed'} on OpenClaw"})
    fields = ["stratum", "id", "kind", "domain", "form", "scenario", "class", "changes", "people", "acting",
              "openclaw", "prompt"]
    with (HERE / "sample.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(picks)
    summary = {"eligible": dict(Counter(f"{r['domain']}/{r['kind']}" for r in pool)), "sample": len(picks),
               "by_stratum": dict(Counter(p["stratum"] for p in picks)),
               "people_max_by_domain": {d: max(int(p["people"]) for p in picks if p["domain"] == d)
                                        for d in ("box", "calendar", "linear", "slack")},
               "acting_max_by_domain": {d: max(int(p["acting"]) for p in picks if p["domain"] == d)
                                        for d in ("box", "calendar", "linear", "slack")},
               "changes": dict(Counter(t for p in picks for t in p["changes"].split(";")
                                       if t and not t.startswith("accounts")))}
    (HERE / "sample.json").write_text(json.dumps(summary, indent=1) + "\n")
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
