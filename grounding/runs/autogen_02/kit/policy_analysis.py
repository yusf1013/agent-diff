"""Phase 1 analysis for the policy-level definition (task 17) and the credit rules: per fact, the policy variants'
outcomes from my manual labels, set against the same fact's probes (with "If there isn't one, just tell me").

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.kit.policy_analysis [--json OUT]

Sources:
- labels: eval/labels_phase1/*.json (mine);
- the variants' facts: runs/phase1/index.json;
- the probes: autogen_01's same-day control run of fact_coverage_02's new suite (runs/solve_control.score.json,
  judged), one probe per near miss, 3 trials each.

Per fact: the twin's failures k/3 (absence) and the drop-F variant's k/3 (underspecified), the probe failures j/m,
and the D4 pair reading; for the underspecified variants and the clones, the same reading against the scenario's
cover in the control run (the cover passes and the variant fails = policy). Per domain and mode: the rate on trial 1 with its exact one-sided 90% bounds (definition A),
the spread of k/3 over facts (definition B), and the rate over all trials.
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

from grounding.runs.autogen_01.inputs.make_briefs import SLACK_ALIASES  # the control run uses the catalog names
from grounding.runs.autogen_02.kit.sampler import FAIL, PASS, lower_bound, upper_bound

STUDY = Path(__file__).resolve().parents[1]
A1 = STUDY.parent / "autogen_01"
RUNS = {"solve_absence": "absence", "solve_under": "underspecified", "solve_clone": "clone"}


def labels() -> dict:
    out = {}
    for f in sorted((STUDY / "eval" / "labels_phase1").glob("*.json")):
        out.update({k: v for k, v in json.loads(f.read_text()).items() if not k.startswith("_")})
    return out


def variant_outcomes(lab: dict) -> dict:
    """variant id -> {"mode", "trials": {t: outcome}}."""
    out = defaultdict(lambda: {"trials": {}})
    for key, v in lab.items():
        run, trial, case_id = key.split("/")
        out[case_id]["mode"] = RUNS.get(run, run)
        out[case_id]["trials"][trial] = v["outcome"]
    return out


def probe_outcomes() -> dict:
    """(scenario, fact) -> [outcome, ...] over the fact's probes and trials in the control run."""
    score = json.loads((A1 / "runs" / "solve_control.score.json").read_text())
    out = defaultdict(list)
    for t in score["tests"]:
        if t.get("form") != "probe":
            continue
        for trial in t["trials"].values():
            out[(t["scenario"], t["fact"])].append(trial["outcome"])
    return out


def cover_outcomes() -> dict:
    """scenario -> [outcome, ...] of its cover (target and every near miss) in the control run."""
    score = json.loads((A1 / "runs" / "solve_control.score.json").read_text())
    return {t["scenario"]: [x["outcome"] for x in t["trials"].values()] for t in score["tests"] if t.get("form") == "cover"}


def reading(twin_fails: int, twin_n: int, probe_fails: int, probe_n: int) -> str:
    """The D4 pair reading of one fact: a per-fact breakdown of the twin's failures, never a filter on them."""
    if not twin_n:
        return "no twin result"
    if twin_fails == 0:
        return "no hole"
    if not probe_n:
        return "twin fails; no probe data"
    if probe_fails == 0:
        return "policy"
    return "fact-level"


def analyse() -> dict:
    lab = labels()
    outcomes = variant_outcomes(lab)
    index = json.loads((STUDY / "runs" / "phase1" / "index.json").read_text())
    probes = probe_outcomes()
    covers = cover_outcomes()
    facts = []
    cells = defaultdict(list)
    for vid, res in sorted(outcomes.items()):
        meta = index.get(vid, {})
        trials = res["trials"]
        usable = {t: o for t, o in trials.items() if o in FAIL | PASS}
        k = sum(o in FAIL for o in usable.values())
        row = {"variant": vid, "mode": res.get("mode"), "domain": vid.split("-")[-3].lower() if False else None,
               "scenario": meta.get("scenario"), "fact": meta.get("fact"), "family": meta.get("family"),
               "fails": k, "usable": len(usable), "t1": trials.get("t1"),
               "other_near_misses": meta.get("other_near_misses"), "matches": meta.get("matches")}
        sc = meta.get("scenario") or ""
        row["domain"] = {"BOX": "box", "CAL": "calendar", "LIN": "linear", "SLK": "slack"}.get(sc.split("-")[0])
        if res.get("mode") == "absence":
            fact = meta.get("fact")
            po = probes.get((meta.get("scenario"), fact)) or probes.get((meta.get("scenario"), SLACK_ALIASES.get(fact)), [])
            pf = sum(o in FAIL for o in po)
            row.update(probe_fails=pf, probe_n=len([o for o in po if o in FAIL | PASS]),
                       reading=reading(k, len(usable), pf, len([o for o in po if o in FAIL | PASS])))
        elif res.get("mode") in ("underspecified", "clone"):
            co = covers.get(meta.get("scenario"), [])
            cf = sum(o in FAIL for o in co)
            cn = len([o for o in co if o in FAIL | PASS])
            row.update(cover_fails=cf, cover_n=cn, reading=reading(k, len(usable), cf, cn))
        facts.append(row)
        cells[(row["domain"], row["mode"])].append(row)
    summary = {}
    for (domain, mode), rows in sorted(cells.items(), key=lambda kv: (str(kv[0][1]), str(kv[0][0]))):
        t1 = [r["t1"] in FAIL for r in rows if r["t1"] in FAIL | PASS]
        n, kk = len(t1), sum(t1)
        spread = defaultdict(int)
        for r in rows:
            if r["usable"] == 3:
                spread[f"{r['fails']}/3"] += 1
        all_trials = sum(r["usable"] for r in rows)
        all_fails = sum(r["fails"] for r in rows)
        summary[f"{domain}/{mode}"] = {
            "variants": len(rows), "t1": f"{kk}/{n}",
            "t1_bounds_90": [round(lower_bound(kk, n), 3), round(upper_bound(kk, n), 3)] if n else None,
            "all_trials": f"{all_fails}/{all_trials}", "spread": dict(sorted(spread.items()))}
    return {"facts": facts, "cells": summary}


def actions(run_dir: Path) -> dict:
    """What each finished trial of a policy run did to the record the request asks about, from the state diff alone
    (the triage's `acted` on the first reference; mechanical, so a trial that asks and one that gives up both show
    as "no change"). Returns trial key -> category:
    - absence: "near miss", "other record" (a record that is not a near miss, e.g. one Qwen created), "no change";
    - underspecified: "near miss", "all matches", "some matches", "one match", "no change"."""
    from grounding.runs.autogen_02.kit.judge2 import triage
    from grounding.runs.autogen_01.kit import judge as v1
    out = {}
    for summary in sorted(run_dir.glob("t*/*/attempt-*/execution_summary.json")):
        attempt = summary.parent
        trial, case_id = attempt.parts[-3], attempt.parts[-2]
        if attempt != v1.latest(run_dir, trial, case_id) or json.loads(summary.read_text()).get("status") != "completed":
            continue
        case, _, tri = triage(run_dir.name, trial, attempt)
        refs = tri.get("references") or []
        if not refs:
            continue
        r = refs[0]
        acted, expected = set(r["acted"]), set(r["expected"])
        if acted - expected:
            cat = "near miss" if r["exposed"] else "other record"
        elif not acted:
            cat = "no change"
        elif acted == expected:
            cat = "all matches" if len(expected) > 1 else "the target"
        else:
            cat = "one match" if len(acted) == 1 else "some matches"
        out[f"{run_dir.name}/{trial}/{case_id}"] = cat
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--actions", type=Path, nargs="+", help="run folders: print what their trials did instead")
    parser.add_argument("--each", action="store_true", help="with --actions: one line per trial")
    args = parser.parse_args()
    if args.actions:
        from collections import Counter
        for run_dir in args.actions:
            got = actions(run_dir.resolve())
            print(run_dir.name, len(got), dict(Counter(got.values()).most_common()))
            if args.each:
                print("\n".join(f"  {k} {v}" for k, v in sorted(got.items())))
        return
    result = analyse()
    for r in result["facts"]:
        extra = f" probe {r.get('probe_fails')}/{r.get('probe_n')} -> {r.get('reading')}" if r["mode"] == "absence" else ""
        print(f"{r['mode']:15} {r['variant']:38} {r['fact'] or '':30} {r['family'] or '':8} fails {r['fails']}/{r['usable']}"
              f" t1={r['t1']}{extra}")
    print(json.dumps(result["cells"], indent=1))
    if args.json:
        args.json.write_text(json.dumps(result, indent=1) + "\n")


if __name__ == "__main__":
    main()
