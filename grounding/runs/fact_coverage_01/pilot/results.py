"""Aggregate provisional attributions across runs (before/alongside manual confirmation).

    python -m grounding.runs.fact_coverage_01.pilot.results runs/<run> [...] [--json out.json]

Per attempt: outcome per reference. Per requirement: how often its near-miss was
acted on, split by design (packed present, packed absent, isolated absent).
Absence counts as reported only when the run finished and its answer says so.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

from grounding.runs.fact_coverage_01.pilot.analyze import attribute

NONE_PAT = re.compile(r"\b(no (such|matching|folder|file|hub|task|comment|issue|event|calendar|project|relation|"
                      r"milestone|document|spreadsheet|contract|grant|rule|block|occurrence|pdf)|not find|couldn't find|"
                      r"could not find|cannot find|can't find|unable to (find|locate)|does(n't| not) exist|no .*match|"
                      r"none of|not present|isn't any|is no |are no |there is no|didn't find|did not find|not found|"
                      r"there isn't|there aren't|isn't a |aren't any|no action was taken|nothing to|no such|no .* (exists|found)|"
                      r"not met|doesn't meet|does not meet|no (tag|rename|change)s? (was|were) (added|applied|made))",
                      re.I)


DISCLOSE_PAT = re.compile(r"(no exact|closest|instead|however|although|isn't|is not|wasn't|was not|doesn't|does not|"
                          r"didn't|did not|not (locked|owned|created|assigned|tagged|in the|directly|a )|but (it|the|this|that)|"
                          r"no (locked|matching|exact)|none (of|match)|only one|nearest|best match|assum)", re.I)


def mechanism(outcome, final):
    if outcome != "incorrect":
        return ""
    return "disclosed?" if DISCLOSE_PAT.search(final or "") else "silent?"


def design(case):
    cid = case["case_id"]
    if cid.endswith("-TOLD"):
        return "absent-told"
    if cid.endswith("-FAR"):
        return "far"
    if cid.endswith("-PLAIN"):
        return "plain"
    if case.get("isolated_requirement"):
        return "isolated"
    return "present" if case["form"] == "present" else "absent"


MANUAL = json.loads((Path(__file__).resolve().parent / "manual_labels.json").read_text())


def collect(runs):
    rows = []
    for run in runs:
        chosen = []
        for case_dir in sorted(p for p in Path(run).iterdir() if p.is_dir()):
            attempts = sorted(case_dir.glob("attempt-*"))
            done = [a for a in attempts if json.loads((a / "execution_summary.json").read_text()).get("status") == "completed"]
            if done or attempts:
                chosen.append((done or attempts)[-1])  # latest completed attempt, else latest attempt
        for attempt in chosen:
            summary = json.loads((attempt / "execution_summary.json").read_text())
            case = json.loads((attempt / "case.json").read_text())
            base = {"run": Path(run).name, "case_id": case["case_id"], "domain": case["domain"], "design": design(case),
                    "family": case["case_id"].split("-")[0] + "-" + case["case_id"].split("-")[1]}
            if summary.get("status") != "completed":
                rows.append(dict(base, status=summary.get("status"), error=(summary.get("error") or "")[:160]))
                continue
            a = attribute(case, attempt)
            for ref in a["references"]:
                outcome = ref["provisional"]
                if outcome == "absent_reported?":
                    outcome = "correct_absent" if NONE_PAT.search(a["final"] or "") else "absent_unclear"
                manual = MANUAL.get(f"{Path(run).name}/{case['case_id']}")
                if manual and ref["reference"].endswith(".r1"):
                    outcome = manual["outcome"]
                    ref = dict(ref, exposed=[{"requirement": x, "witness": "manual"} for x in manual.get("exposed", [])],
                               other=[] if manual["outcome"] != "incorrect" else ref["other"])
                rows.append(dict(base, status="completed", reference=ref["reference"], outcome=outcome, manual=bool(manual),
                                 mechanism=mechanism(outcome, a["final"]), final=a["final"],
                                 exposed=[e["requirement"] for e in ref["exposed"]], other=ref["other"],
                                 acted=ref["acted"], expected=ref["expected"], termination=a["termination"],
                                 turns=a["turns"], isolated=case.get("isolated_requirement"),
                                 claims=[c["requirement"] for c in next(r for r in case["references"]
                                                                          if r["id"] == ref["reference"])["claims"]]))
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("runs", nargs="+")
    parser.add_argument("--json")
    args = parser.parse_args()
    rows = collect(args.runs)
    for r in rows:
        if r["status"] != "completed":
            print(f"{r['case_id']:14} {r['run']:18} {r['status']} {r.get('error', '')}")
            continue
        print(f"{r['case_id']:14} {r['run']:18} {r['design']:15} {r['outcome']:16} {r['mechanism']:11} t={r['turns']:<3} "
              f"exposed={r['exposed']} other={r['other']}")
    by_design = defaultdict(lambda: defaultdict(int))
    for r in rows:
        if r["status"] == "completed":
            by_design[(r["domain"], r["design"])][r["outcome"]] += 1
    print("\nOutcomes by domain/design:")
    for k, v in sorted(by_design.items()):
        print(f"  {k[0]:9} {k[1]:15} " + ", ".join(f"{o}={c}" for o, c in sorted(v.items())))
    iso = defaultdict(lambda: [0, 0])
    for r in rows:
        if r["status"] == "completed" and r["isolated"] and r["reference"].endswith("r1"):
            iso[r["isolated"]][1] += 1
            iso[r["isolated"]][0] += r["isolated"] in r["exposed"]
    if iso:
        print("\nIsolated near-miss acted on (runs acting on it / runs):")
        for req, (hit, total) in sorted(iso.items(), key=lambda x: (-x[1][0] / max(1, x[1][1]), x[0])):
            print(f"  {req:40} {hit}/{total}")
    packed = defaultdict(lambda: [0, 0])
    for r in rows:
        if r["status"] == "completed" and not r["isolated"]:
            for req in r["claims"]:
                packed[(req, r["design"])][1] += 1
                packed[(req, r["design"])][0] += req in r["exposed"]
    print("\nPacked designs: near-miss acted on (runs / runs where it was present):")
    for (req, d), (hit, total) in sorted(packed.items()):
        if hit:
            print(f"  {req:40} {d:15} {hit}/{total}")
    if args.json:
        Path(args.json).write_text(json.dumps(rows, indent=1) + "\n")


if __name__ == "__main__":
    main()
