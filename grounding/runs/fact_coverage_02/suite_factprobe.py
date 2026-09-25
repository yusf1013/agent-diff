"""Fact probes: one test per fact that has two or more decoys, keeping all of that fact's decoys. No service calls.

    python -m grounding.runs.fact_coverage_02.suite_factprobe [--check]

A fact probe is the scenario with its target and every other fact's decoys removed, all decoys of one fact kept,
and "If there isn't one, just tell me." It is compared with the same decoys' single-decoy probes, which already ran.
- New facts: every (scenario, fact) with 2+ claims in the new scenarios (15).
- Pilot facts: the 4 facts whose F0 decoy got a nearest-value F7 variant (PB-*). The two decoys were one record at
  two values, so the fact probe keeps the original and adds a clone (fresh ids, the nearest value, a distinct name).
Writes cases_factprobe/<domain>/<case_id>.json and suite_factprobe.json.
"""
from __future__ import annotations

import argparse
import copy
import importlib
import json
from collections import defaultdict
from pathlib import Path

from grounding.runs.fact_coverage_01.pilot.common import finish
from grounding.runs.fact_coverage_02.anchors import missing_anchors
from grounding.runs.fact_coverage_02.suite_pilot import FAMILY, NEAREST, digest, keep_claims, rename, sources, told

HERE = Path(__file__).resolve().parent
MODULES = ["scenarios_box", "scenarios_calendar", "scenarios_linear", "scenarios_slack"]

# Pilot clones: scenario, claim key -> (fresh ids for the decoy and its dependents, field changes on the clone).
CLONES = {
    ("BOX-08", "I13"): ({"9004": "9014", "99004": "99014", "9105": "9115", "9208": "9218", "9209": "9219"},
                       {"box_files": {"name": "Education pricing EMEA.xlsx"},
                        "box_file_versions": {"name": "Education pricing EMEA.xlsx"},
                        "box_tasks": {"due_at": "2026-10-01T09:00:00"}}),
    ("LIN-01", "I12"): ({"i-mob-14": "i-mob-14n"},
                       {"issues": {"title": "Settings toggle misaligned on phones", "priority": 3.0,
                                   "priorityLabel": "Medium"}}),
    ("LIN-05", "I13"): ({"i-plt-5": "i-plt-5n"}, {"issues": {"title": "Tune cache pool sizes", "estimate": 4.0}}),
    ("LIN-05", "I15"): ({"i-plt-7": "i-plt-7n"}, {"issues": {"title": "Add tracing to the workers",
                                                            "dueDate": "2026-09-23"}}),
}


def clone_decoy(case, ids, changes, base):
    """Copy every row that mentions an old id as a whole field value, re-keyed to the fresh ids. A Linear clone is
    numbered past every issue of its team in the full scenario (base), so no identifier is reused across its tests."""
    case = copy.deepcopy(case)
    taken = {str(v) for rows in case["seed"].values() for r in rows for v in r.values() if isinstance(v, (str, int))}
    clash = set(ids.values()) & taken
    if clash:
        raise SystemExit(f"{case['case_id']}: fresh ids already used: {sorted(clash)}")
    for table, rows in case["seed"].items():
        new = []
        for r in rows:
            if any(isinstance(v, str) and v in ids for v in r.values()):
                c = {k: (ids[v] if isinstance(v, str) and v in ids else v) for k, v in r.items()}
                c.update(changes.get(table, {}))
                new.append(c)
        if table == "issues":  # a Linear clone needs its own number and identifier
            for c in new:
                team = [x for x in base["seed"]["issues"] if x["teamId"] == c["teamId"]]
                number = max(float(x["number"]) for x in team) + 1 + new.index(c)
                key = c["identifier"].split("-")[0]
                c.update(number=number, identifier=f"{key}-{int(number)}", branchName=f"{key.lower()}-{int(number)}",
                         url=f"https://linear.app/northwind/issue/{key}-{int(number)}")
        rows.extend(new)
    return case


def fact_groups(ref):
    groups = defaultdict(list)
    for ci, c in enumerate(ref["claims"]):
        groups[c["requirement"]].append(ci)
    return {fact: idx for fact, idx in groups.items() if len(idx) > 1}


def build():
    tests, cases = [], []

    def add(case, scenario, fact, families, singles, note=""):
        case, results, errs = finish(case)
        errs += missing_anchors(case)  # the request's other named entities must survive target removal
        if errs:
            raise SystemExit(f"{case['case_id']}: {errs}")
        case["coverage_claims"] = sorted({c["requirement"] for r in results for c in r["claims"] if c["credited"]})
        case["case_sha256"] = digest({k: v for k, v in case.items() if k != "case_sha256"})
        cases.append(case)
        tests.append({"case_id": case["case_id"], "domain": case["domain"], "form": "fact probe", "scenario": scenario,
                      "fact": fact, "families": families, "singles": singles, "note": note})

    for name in MODULES:  # new facts
        for builder in importlib.import_module(f"grounding.runs.fact_coverage_02.{name}").SCENARIOS:
            base = builder()
            scenario, plural = base["case_id"], base.get("plural", False)
            for ri, ref in enumerate(base["references"]):
                for fact, idx in fact_groups(ref).items():
                    keys = [f"I{ri + 1}{ci + 1}" for ci in idx]
                    case = told(rename(keep_claims(base, ri, set(idx)), f"FP-{scenario}-{'-'.join(keys)}"), plural)
                    add(case, scenario, fact, [ref["claims"][ci]["family"] for ci in idx],
                        [f"P-{scenario}-{k}" for k in keys])
    src = sources()  # pilot facts: original decoy plus a nearest-value clone
    for scenario, key, table, match, field, value, note in NEAREST:
        builder, plural = src[scenario]
        base = builder()
        ri, ci = int(key[1]) - 1, int(key[2]) - 1
        ids, changes = CLONES[(scenario, key)]
        case = clone_decoy(keep_claims(base, ri, {ci}), ids, changes, base)
        ref = case["references"][ri]
        original = ref["claims"][0]
        clone = copy.deepcopy(original)
        clone["witness"] = ids[str(original["witness"])] if str(original["witness"]) in ids else original["witness"]
        clone["explanation"] = note
        ref["claims"].append(clone)
        case = told(rename(case, f"FP-{scenario}-{key}-N"), plural)
        add(case, scenario, original["requirement"], [FAMILY[scenario][key], "F7"],
            [f"P-{scenario}-{key}", f"PB-{scenario}-{key}"], note=f"the nearest-value decoy is a clone: {note}")
    return tests, cases


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    tests, cases = build()
    outputs = {HERE / "cases_factprobe" / c["domain"] / f"{c['case_id']}.json":
               json.dumps(c, indent=1, ensure_ascii=False) + "\n" for c in cases}
    outputs[HERE / "suite_factprobe.json"] = json.dumps(tests, indent=1) + "\n"
    if args.check:
        stale = [str(p.relative_to(HERE)) for p, t in outputs.items() if not p.exists() or p.read_text() != t]
        if stale:
            raise SystemExit("Stale: " + ", ".join(stale))
        print("suite current")
        return
    for path, text in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
    print(json.dumps({"tests": len(tests), "decoys": sum(len(t["families"]) for t in tests),
                      "by_domain": {d: sum(1 for t in tests if t["domain"] == d) for d in ("box", "calendar", "linear", "slack")}}))


if __name__ == "__main__":
    main()
