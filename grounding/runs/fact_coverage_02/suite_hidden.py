"""Hidden-target follow-up (method.md, "hidden-target tests"): the wording check and the pilot. No service calls.

    python -m grounding.runs.fact_coverage_02.suite_hidden [--check]

- Wording check (WC-*): the three covers whose failures happened with the target out of sight (BOX-09 and LIN-15
  as the pilot ran them in B1, BOX-24 as run in method_new), unchanged except for "If there isn't one, just tell
  me." The target and every decoy stay.
- Hidden-target pilot (H-*): the scenarios of scenarios_hidden.py, target present, presupposing wording. Each must
  pass hiding.hiding_errors (one decoy on the easy paths, no target). Arm B scenarios also get a probe twin (P-*):
  the same decoy alone, no target, "If there isn't one, just tell me"; Arm A decoys already have their probes.
Writes cases_hidden/<domain>/<case_id>.json and suite_hidden.json.
"""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path

from grounding.runs.fact_coverage_01.pilot.common import finish
from grounding.runs.fact_coverage_01.pilot.variants import isolate
from grounding.runs.fact_coverage_02.anchors import missing_anchors
from grounding.runs.fact_coverage_02.hiding import hiding_errors
from grounding.runs.fact_coverage_02.scenarios_hidden import ARM_A, ARM_B
from grounding.runs.fact_coverage_02.suite_pilot import FAMILY, digest, rename, told

HERE = Path(__file__).resolve().parent
PILOT = HERE.parent / "fact_coverage_01/pilot/cases"
WORDING = [(PILOT / "box/BOX-09.json", "b1"), (PILOT / "linear/LIN-15.json", "b1"),
           (HERE / "cases_new/box/BOX-24.json", "method_new")]


def fresh(path):
    """A built case without the fields finish() derives from the prompt."""
    case = json.loads(path.read_text())
    for key in ("cards", "task_spec", "coverage_claims", "case_sha256"):
        case.pop(key, None)
    return case


def build():
    tests, cases = [], []

    def add(case, form, scenario, note="", **extra):
        case, results, errs = finish(case)
        errs += missing_anchors(case)
        if form == "hidden target":
            errs += hiding_errors(case)  # one decoy on the easy paths, and no target on any of them
        if errs:
            raise SystemExit(f"{case['case_id']}: {errs}")
        case["coverage_claims"] = sorted({c["requirement"] for r in results for c in r["claims"] if c["credited"]})
        case["case_sha256"] = digest({k: v for k, v in case.items() if k != "case_sha256"})
        cases.append(case)
        tests.append({"case_id": case["case_id"], "domain": case["domain"], "form": form, "scenario": scenario,
                      "note": note, **extra})

    for path, run in WORDING:
        base = fresh(path)
        case = told(rename(copy.deepcopy(base), f"WC-{base['case_id']}"), plural=False)
        add(case, "wording check", base["case_id"], note=f"the cover as run in {run}, plus the escape clause",
            cover_run=run)
    for builder, ci, scenario in ARM_A:
        case = builder()
        hidden = case["references"][0]["claims"][ci]
        add(rename(case, f"H-{scenario}-I1{ci + 1}"), "hidden target", scenario, arm="A", fact=hidden["requirement"],
            family=FAMILY[scenario][f"I1{ci + 1}"], probe=f"P-{scenario}-I1{ci + 1}",
            note="pilot scenario; other decoys removed" + ("; lures " + json.dumps(case["lures"]) if case.get("lures") else ""))
    for builder in ARM_B:
        base = builder()
        scenario = base["case_id"]
        hidden = base["references"][0]["claims"][0]
        add(rename(copy.deepcopy(base), f"H-{scenario}-I11"), "hidden target", scenario, arm="B",
            fact=hidden["requirement"], family=hidden.get("family"), probe=f"P-{scenario}-I11",
            note="constructed scenario")
        twin = told(rename(isolate(base, 0, 0), f"P-{scenario}-I11"), plural=False)
        add(twin, "probe twin", scenario, arm="B", fact=hidden["requirement"], family=hidden.get("family"),
            note="the hidden test's decoy alone")
    return tests, cases


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    tests, cases = build()
    outputs = {HERE / "cases_hidden" / c["domain"] / f"{c['case_id']}.json":
               json.dumps(c, indent=1, ensure_ascii=False) + "\n" for c in cases}
    outputs[HERE / "suite_hidden.json"] = json.dumps(tests, indent=1) + "\n"
    if args.check:
        stale = [str(p.relative_to(HERE)) for p, t in outputs.items() if not p.exists() or p.read_text() != t]
        if stale:
            raise SystemExit("Stale: " + ", ".join(stale))
        print("suite current")
        return
    for path, text in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
    for path in (HERE / "cases_hidden").glob("*/*.json"):
        if path not in outputs:
            path.unlink()  # a case the current builder no longer produces
    print(json.dumps({"tests": len(tests), "by_form": {f: sum(1 for t in tests if t["form"] == f)
                                                       for f in sorted({t["form"] for t in tests})}}))


if __name__ == "__main__":
    main()
