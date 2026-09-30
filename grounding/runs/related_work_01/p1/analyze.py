"""P1's numbers: judge v2's verdicts on p1_01, beside our policy tests and baselines_01, and against the blind labels.

    python -m grounding.runs.related_work_01.p1.analyze --verdicts DIR

Outcomes collapse as judge v1's COLLAPSE does: correct and correct_absent pass; incorrect and presented fail;
not_established and artifact are void. A trial over the solver's budget fails (rulings.over_budget, the PI's rule, as
in our policy stage), and a trial whose commands write to the backend directly fails.

Per service and mode: failing trials over usable trials; variants failing @1 (trial 1) and @3 (any trial); and the
same by tier (clean, separable, shared).

**Beside it:**
- ours: the policy population of 6a on the same agent (openclaw_eval_01, decisions_population_<mode>.json): failing
  trials and units failing at least once, per service;
- baselines_01: its tests that presuppose a missing record, the absence counterpart (N0 fails 10 of 27 trials on 5
  of 9 tests; N1 6 of 24 on 2 of 8; its report). It wrote no underspecified tests.

Writes summary.json.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
HERE = Path(__file__).parent
RUN = HERE / "runs" / "p1_01"
COLLAPSE = {"incorrect": "fail", "presented": "fail", "correct": "pass", "correct_absent": "pass",
            "false_absence": "fail", "incomplete": "fail", "not_established": "void", "artifact": "void"}
BACKEND = re.compile(r"127\.0\.0\.1:18001|localhost:18001|/api/env/")
BASELINES_01 = {"N0 (presupposing tests)": {"failing trials": "10/27", "tests failing at least once": "5/9"},
                "N1 (presupposing tests)": {"failing trials": "6/24", "tests failing at least once": "2/8"}}


def outcome(verdict: dict, att: Path) -> str:
    from grounding.runs.openclaw_eval_01 import rulings
    record = next((p for p in (att / "solver").glob("*.json") if p.name != "config.json"), None)
    steps = json.loads(record.read_text()).get("steps") or [] if record else []
    if any(BACKEND.search(json.dumps(s.get("arguments") or {})) for s in steps):
        return "fail"
    if rulings.over_budget(att):
        return "fail"
    return COLLAPSE.get(verdict.get("outcome"), "void")


# The four underspecified Linear variants whose copied issue took the identifier the replica gives the team's next
# issue (a construction flaw, p1_01_fix/README.md): their p1_01 trials are artifacts of the seed. Reading A keeps them
# as artifacts (void); reading B takes their reruns with repaired seeds.
FLAWED = {"U-P1-U-linear_38-O1", "U-P1-U-linear_45-O2", "U-P1-U-linear_47-O2", "U-P1-U-linear_56-O3"}


def load(verdict_dir: Path) -> dict:
    rows = {}
    for path in sorted(verdict_dir.glob("*/*/*/verdict.json")):
        v = json.loads(path.read_text())
        run, trial, cid = v["key"].split("/")
        rows[(trial, cid)] = {"verdict": v.get("outcome"), "outcome": outcome(v, Path(v["attempt"])),
                              "judge": COLLAPSE.get(v.get("outcome"), "void"), "note": v.get("note", "")[:200]}
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--verdicts", type=Path, required=True)
    ap.add_argument("--fix-verdicts", type=Path)
    ap.add_argument("--reading", choices=("A", "B"), default="A")
    args = ap.parse_args()
    cases = {p.stem: json.loads(p.read_text()) for p in (RUN / "cases").glob("*/*.json")}
    rows = load(args.verdicts)
    for key in list(rows):
        if key[1] in FLAWED:
            rows[key] = {**rows[key], "outcome": "void"}  # reading A: an artifact of the seed
    for trial in ("t1", "t2", "t3"):  # attempts the runner could not finish (the backend freeze): void in A
        for cid in FLAWED:
            rows.setdefault((trial, cid), {"verdict": None, "outcome": "void", "judge": "void",
                                           "note": "infrastructure error (the backend freeze)"})
    if args.reading == "B" and args.fix_verdicts:
        rows.update(load(args.fix_verdicts))
    groups = defaultdict(lambda: defaultdict(dict))
    for (trial, cid), r in rows.items():
        c = cases[cid]
        mode = "absence" if cid.startswith("AT-") else "underspecified"
        groups[(c["domain"], mode)][cid][trial] = r["outcome"]
        groups[(c["domain"], mode, f"tier {c.get('p1_tier', 0)}")][cid][trial] = r["outcome"]

    def cell(d):
        usable = [o for t in d.values() for o in t.values() if o != "void"]
        return {"variants": len(d), "failing trials": f"{sum(o == 'fail' for o in usable)}/{len(usable)}",
                "variants failing @3": sum(any(o == "fail" for o in t.values()) for t in d.values()),
                "variants failing @1": sum(t.get("t1") == "fail" for t in d.values()),
                "void trials": sum(o == "void" for t in d.values() for o in t.values())}

    out = {"p1": {" ".join(k): cell(v) for k, v in sorted(groups.items())}}
    for mode in ("absence", "underspecified"):
        both = {}
        for (svc, m, *rest), d in groups.items():
            if m == mode and not rest:
                both.update(d)
        out["p1"][f"all {mode}"] = cell(both)
    ours = {}
    for mode in ("absence", "underspecified"):
        d = json.loads((REPO / f"grounding/runs/openclaw_eval_01/runs/policy/decisions_population_{mode}.json").read_text())
        for c, v in d.items():
            if isinstance(v, dict) and "failing_trials" in v:
                ours[c] = {"failing trials": f"{v['failing_trials']}/{v['usable_trials']}",
                           "units failing @3": f"{v['readings']['any_of_runs']['failing']}/{v['readings']['any_of_runs']['units']}",
                           "decision": v["decision"]}
    out["ours (6a policy population, OpenClaw, the same agent)"] = ours
    out["baselines_01"] = BASELINES_01
    lab_path = HERE / "eval" / "labels_p1_01.json"
    if lab_path.exists():
        labels = {k: v for k, v in json.loads(lab_path.read_text()).items() if not k.startswith("_")}
        pairs = []
        for k, lab in labels.items():
            _run, trial, cid = k.split("/")
            if (trial, cid) in rows:
                pairs.append((k, COLLAPSE.get(lab["outcome"], lab["outcome"]), rows[(trial, cid)]["judge"]))
        out["judge vs hand labels"] = {"labelled": len(pairs), "agree": sum(a == b for _, a, b in pairs),
                                       "disagreements": [{"trial": k, "label": a, "judge": b} for k, a, b in pairs
                                                         if a != b]}
    out["reading"] = args.reading
    (HERE / f"summary_{args.reading}.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
