"""Method v1 and its cover-style control, applied to the new scenarios (facts the pilot never tested). No service calls.

    python -m grounding.runs.fact_coverage_02.suite_new [--check]

For every scenario: the control is the scenario as written (target present, all decoys, as in the pilot's cover);
the method's tests are one probe per decoy and a packed plain test when a reference has two or more F0 decoys;
a module's panel() adds that domain's policy panel.
Writes cases_new/<domain>/<case_id>.json and suite_new.json.
"""
from __future__ import annotations

import argparse
import importlib
import json
from pathlib import Path

from grounding.runs.fact_coverage_01.pilot.common import finish
from grounding.runs.fact_coverage_01.pilot.variants import isolate
from grounding.runs.fact_coverage_02.suite_pilot import digest, keep_claims, rename, told

HERE = Path(__file__).resolve().parent
MODULES = ["scenarios_box", "scenarios_calendar", "scenarios_linear", "scenarios_slack"]


def build():
    tests, cases = [], []

    def add(case, form, scenario, fact=None, family=None, note=""):
        case, results, errs = finish(case)
        if errs:
            raise SystemExit(f"{case['case_id']}: {errs}")
        case["coverage_claims"] = sorted({c["requirement"] for r in results for c in r["claims"] if c["credited"]})
        case["case_sha256"] = digest({k: v for k, v in case.items() if k != "case_sha256"})
        cases.append(case)
        tests.append({"case_id": case["case_id"], "domain": case["domain"], "form": form, "scenario": scenario,
                      "fact": fact, "family": family, "note": note})

    for name in MODULES:
        try:
            module = importlib.import_module(f"grounding.runs.fact_coverage_02.{name}")
        except ModuleNotFoundError as exc:
            if name in str(exc):
                continue
            raise
        for builder in module.SCENARIOS:
            base = builder()
            scenario = base["case_id"]
            plural = base.get("plural", False)
            add(base, "cover control", scenario)
            for ri, ref in enumerate(base["references"]):
                plain = []
                for ci, claim in enumerate(ref["claims"]):
                    key = f"I{ri + 1}{ci + 1}"
                    keep = claim.get("keep", ())
                    probe = told(rename(isolate(base, ri, ci, keep), f"P-{scenario}-{key}"), plural)
                    add(probe, "probe", scenario, claim["requirement"], claim["family"])
                    if claim["family"] == "F0":
                        plain.append(ci)
                if len(plain) > 1:
                    packed = told(rename(keep_claims(base, ri, set(plain)), f"PP-{scenario}-R{ri + 1}"), plural)
                    add(packed, "packed plain", scenario, None, "F0",
                        note="plain decoys: " + ", ".join(ref["claims"][i]["requirement"] for i in plain))
        for case, note in getattr(module, "panel", list)():
            add(case, "policy panel", case["variant_of"], note=note)
    return tests, cases


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    tests, cases = build()
    outputs = {HERE / "cases_new" / c["domain"] / f"{c['case_id']}.json": json.dumps(c, indent=1, ensure_ascii=False) + "\n"
               for c in cases}
    outputs[HERE / "suite_new.json"] = json.dumps(tests, indent=1) + "\n"
    if args.check:
        stale = [str(p.relative_to(HERE)) for p, t in outputs.items() if not p.exists() or p.read_text() != t]
        if stale:
            raise SystemExit("Stale: " + ", ".join(stale))
        print("suite current")
        return
    for path, text in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
    for path in (HERE / "cases_new").glob("*/*.json"):
        if path not in outputs:
            path.unlink()  # a case the current scenarios no longer produce
    summary = {}
    for t in tests:
        d = summary.setdefault(t["domain"], {})
        d[t["form"]] = d.get(t["form"], 0) + 1
    families = {}
    for t in tests:
        if t["form"] == "probe":
            families[t["family"]] = families.get(t["family"], 0) + 1
    print(json.dumps({"tests": len(tests), "by_domain": summary, "probe_families": dict(sorted(families.items()))}))


if __name__ == "__main__":
    main()
