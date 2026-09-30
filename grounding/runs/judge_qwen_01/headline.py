"""What happens to the study's headline numbers if Qwen's verdicts replace Muse's (no model calls).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.judge_qwen_01.headline --out runs/selfhost

**Regular suite** (report_01's Table 7, openclaw_eval_01's final_regular_with_6b.json). A test exposes a fact when
one of its trials fails on it, under the PI's rulings as openclaw_eval_01's adjudicate.py applies them: a trial over
the solver's budget exposes nothing, and a trial that acted only on flawed near misses does not count. A trial's
outcome is its verdict when it was judged; the unjudged final trials are all mechanically clean (checked here), so
they expose nothing.

**Policy stage** (Table 11, decisions_population_<mode>.json). For each cell, the valid units in policy.py's fixed
order, each trial's verdict (a trial over the budget counts as "incorrect"), and policy.pooled_decision, the rule
fixed before the runs.

Each part is computed first with Muse's verdicts and checked against the published file, so the code is known to
reproduce the study; then Qwen's verdicts replace Muse's on the same trials. A trial Qwen has no verdict for keeps
the mechanical triage's outcome, as the pipeline would after a failed judge call, and is counted.

The saved Muse verdicts name attempt folders in worktrees that no longer exist, so the budget check reads each
execution's attempt folder in this checkout (common.attempt_path), the same folder the manifest names.
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

from grounding.runs.autogen_02.kit import judge2, sampler
from grounding.runs.judge_qwen_01.common import FAIL, HERE, OC, attempt_path, final_keys, load, muse_dir
from grounding.runs.openclaw_eval_01 import policy, rulings


def muse_of(key: str) -> dict | None:
    p = muse_dir(key) / "verdict.json"
    return load(p) if p.exists() else None


def qwen_reader(out: Path, fill_with_muse: bool = False):
    """Qwen's verdict where it has one. Without one (a judge call that never gave a verdict), the triage's outcome
    stands, as in the pipeline; with fill_with_muse (a partial replay), Muse's verdict stands instead."""
    fallbacks = []

    def read(key: str) -> dict | None:
        p = out / key / "verdict.json"
        if p.exists():
            return load(p)
        m = muse_of(key)
        if m is None:
            return None
        fallbacks.append(key)
        if fill_with_muse:
            return m
        return {"outcome": m["provisional"], "exposed": m["provisional_exposed"] if m["provisional"] in FAIL else [],
                "acted_on": []}
    return read, fallbacks


def totals(rows: list[dict]) -> dict:
    return {"tests": len(rows), "tests_exposing": sum(bool(r["exposed"]) for r in rows),
            "facts_detect3": len({f for r in rows for f in r["exposed"]}),
            "facts_detect1": len({f for r in rows for f in r["exposed_t1"]})}


def regular(verdict_of) -> dict:
    rows = []
    for t in load(OC / "final_regular_with_6b.json")["tests"]:
        exposed, exposed_t1 = set(), set()
        for trial in ("t1", "t2", "t3"):
            key = f"{t['run']}/{trial}/{t['case_id']}"
            v = verdict_of(key)
            if v is None or v.get("outcome") not in FAIL:
                continue
            if rulings.over_budget(attempt_path(key)):
                continue
            if rulings.trial_not_counted(t["scenario"], v.get("acted_on")):
                continue
            exposed |= set(v.get("exposed") or [])
            if trial == "t1":
                exposed_t1 |= set(v.get("exposed") or [])
        rows.append({"case_id": t["case_id"], "run": t["run"], "domain": t["domain"], "form": t["form"],
                     "exposed": sorted(exposed), "exposed_t1": sorted(exposed_t1)})
    by = defaultdict(list)
    for r in rows:
        by[f"domain:{r['domain']}"].append(r)
        by[f"form:{r['form']}"].append(r)
    return {"final": totals(rows), "by": {k: totals(v) for k, v in sorted(by.items())},
            "facts_detect3": sorted({f for r in rows for f in r["exposed"]}),
            "facts_detect1": sorted({f for r in rows for f in r["exposed_t1"]}), "tests": rows}


def unjudged_are_clean() -> dict:
    """Every final regular trial without a verdict is mechanically clean (the selection judged every other)."""
    keys = [k for k in final_keys() if k.split("/")[0].startswith("full_") and muse_of(k) is None]
    outcomes = defaultdict(int)
    for key in keys:
        run, trial, _ = key.split("/")
        outcomes[judge2.triage(run, trial, attempt_path(key))[2]["outcome"]] += 1
    return dict(outcomes)


def policy_decisions(mode: str, verdict_of) -> dict:
    by_unit = defaultdict(list)
    for key in final_keys():
        run = key.split("/")[0]
        if not run.startswith("full_") and mode in run:
            by_unit[key.split("/")[2]].append(key)
    result = {}
    for cell, seq in policy.population_plan(mode)["cells"].items():
        valid, _ = policy.population_units(seq)
        per_unit, missing = [], []
        for u in valid:
            outcomes = []
            for key in by_unit.get(u["unit"], []):
                v = verdict_of(key)
                if v is None:
                    continue
                outcomes.append("incorrect" if rulings.over_budget(attempt_path(key)) else v.get("outcome"))
            usable = [o for o in outcomes if o in sampler.FAIL | sampler.PASS]
            if not outcomes:
                missing.append(u["unit"])
            if usable:
                per_unit.append((sum(o in sampler.FAIL for o in usable), len(usable)))
        result[cell] = {"valid_units": len(valid), "missing": missing, **policy.pooled_decision(per_unit)}
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path, help="Qwen's verdict folder; without it, only the check against Muse runs")
    ap.add_argument("--fill-with-muse", action="store_true",
                    help="a partial replay: Muse's verdict where Qwen has none yet (writes headline_partial.json)")
    args = ap.parse_args()
    report = {"unjudged_final_regular_trials_by_triage": unjudged_are_clean()}
    published = load(OC / "final_regular_with_6b.json")
    muse_regular = regular(muse_of)
    check = {"final": muse_regular["final"] == published["final"],
             "by": all(muse_regular["by"].get(k) == v for k, v in published["by"].items()),
             "facts": muse_regular["facts_detect3"] == published["facts_detect3"]
             and muse_regular["facts_detect1"] == published["facts_detect1"],
             "tests": {(t["case_id"], tuple(t["exposed"]), tuple(t["exposed_t1"])) for t in muse_regular["tests"]} ==
             {(t["case_id"], tuple(t["exposed"]), tuple(t["exposed_t1"])) for t in published["tests"]}}
    report["regular"] = {"muse": {k: muse_regular[k] for k in ("final", "by")}, "muse_reproduces_published": check}
    report["policy"] = {}
    for mode in ("absence", "underspecified"):
        muse_policy = policy_decisions(mode, muse_of)
        pub = load(OC / "policy" / f"decisions_population_{mode}.json")
        same = {c: all(pub[c].get(k) == r.get(k) for k in ("rate", "p10", "p90", "decision"))
                for c, r in muse_policy.items()}
        report["policy"][mode] = {"muse": muse_policy, "muse_reproduces_published": same}
    if args.out:
        out = args.out if args.out.is_absolute() else HERE / args.out
        read, fallbacks = qwen_reader(out, args.fill_with_muse)
        qwen_regular = regular(read)
        report["regular"]["qwen"] = {k: qwen_regular[k] for k in ("final", "by")}
        mt = {t["case_id"]: t for t in muse_regular["tests"]}
        report["regular"]["tests_that_change"] = [
            {"case_id": t["case_id"], "muse": mt[t["case_id"]]["exposed"], "qwen": t["exposed"],
             "muse_t1": mt[t["case_id"]]["exposed_t1"], "qwen_t1": t["exposed_t1"]}
            for t in qwen_regular["tests"] if (t["exposed"], t["exposed_t1"]) !=
            (mt[t["case_id"]]["exposed"], mt[t["case_id"]]["exposed_t1"])]
        report["regular"]["facts_detect3_only_muse"] = sorted(set(muse_regular["facts_detect3"]) -
                                                              set(qwen_regular["facts_detect3"]))
        report["regular"]["facts_detect3_only_qwen"] = sorted(set(qwen_regular["facts_detect3"]) -
                                                              set(muse_regular["facts_detect3"]))
        for mode in ("absence", "underspecified"):
            report["policy"][mode]["qwen"] = policy_decisions(mode, read)
        report["qwen_verdicts_missing" + ("_filled_with_muse" if args.fill_with_muse else "_triage_stands")] = \
            len(set(fallbacks)) if args.fill_with_muse else sorted(set(fallbacks))
    dest = (HERE / "headline.json") if not args.out else \
        out / ("headline_partial.json" if args.fill_with_muse else "headline.json")
    dest.write_text(json.dumps(report, indent=1) + "\n")
    summary = {"unjudged": report["unjudged_final_regular_trials_by_triage"],
               "regular": {k: v for k, v in report["regular"].items() if k in ("muse_reproduces_published",)},
               "regular_final": {k: report["regular"][k]["final"] for k in ("muse", "qwen") if k in report["regular"]},
               "policy": {m: {"muse_reproduces_published": all(p["muse_reproduces_published"].values()),
                              **{j: {c: (r.get("rate"), r.get("p10"), r.get("p90"), r.get("decision"))
                                     for c, r in p[j].items()} for j in ("muse", "qwen") if j in p}}
                          for m, p in report["policy"].items()}}
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
