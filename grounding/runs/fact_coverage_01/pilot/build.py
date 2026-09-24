"""Emit pilot cases and verify every credit claim mechanically.

    python -m grounding.runs.fact_coverage_01.pilot.build [--check]

Writes cases/<domain>/<case>.json, checks.json (per-claim results) and
coverage.json (credited requirements per case and domain). No service calls.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib
import json
from pathlib import Path

from grounding.runs.fact_coverage_01.pilot.common import finish

HERE = Path(__file__).resolve().parent
CATALOGS = HERE.parent / "catalog"
MODULES = ["cases_slack", "cases_box", "cases_calendar", "cases_linear", "cases_isolated", "cases_linear_variants", "cases_calendar_variants", "cases_told", "cases_contrast", "cases_altsweep", "cases_wording"]


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--only", nargs="*", help="Domains to build")
    args = parser.parse_args()
    outputs, checks, errors = {}, [], []
    coverage = {}
    for module_name in MODULES:
        try:
            module = importlib.import_module(f"grounding.runs.fact_coverage_01.pilot.{module_name}")
        except ModuleNotFoundError as exc:
            if module_name in str(exc):
                continue
            raise
        for builder in module.CASES:
            raw = builder()
            domain = raw["domain"]
            if args.only and domain not in args.only:
                continue
            catalog = json.loads((CATALOGS / f"{domain}.json").read_text())
            known = {r["id"] for r in catalog["requirements"]}
            case, results, errs = finish(raw)
            errors += [f"{case['case_id']}: {x}" for x in errs]
            credited = []
            for result in results:
                for c in result["claims"]:
                    if c["requirement"] not in known:
                        errors.append(f"{case['case_id']}: unknown requirement {c['requirement']}")
                    if c["credited"]:
                        credited.append(c["requirement"])
            case["coverage_claims"] = sorted(set(credited))
            case["case_sha256"] = digest({k: v for k, v in case.items() if k != "case_sha256"})
            outputs[HERE / "cases" / domain / f"{case['case_id']}.json"] = json.dumps(case, indent=1, ensure_ascii=False) + "\n"
            checks.append({"case_id": case["case_id"], "domain": domain, "form": case["form"], "mode": case["mode"],
                           "references": results})
            entry = coverage.setdefault(domain, {"catalog_size": len(known), "cases": [], "controls": []})
            row = {"case_id": case["case_id"], "form": case["form"], "mode": case["mode"], "credited": case["coverage_claims"]}
            if case.get("variant_of"):  # experimental controls do not enter the cover
                entry["controls"].append(dict(row, variant_of=case["variant_of"]))
            else:
                entry["cases"].append(row)
    for domain, info in coverage.items():
        seen, rows = set(), []
        for c in info["cases"]:
            new = [r for r in c["credited"] if r not in seen]
            seen.update(c["credited"])
            c["new"] = new
        info["covered"] = sorted(seen)
        info["covered_count"] = len(seen)
        info["redundant_cases"] = [c["case_id"] for c in info["cases"] if not c["new"]]
    if errors:
        raise SystemExit("\n".join(errors))
    outputs[HERE / "checks.json"] = json.dumps(checks, indent=1, ensure_ascii=False) + "\n"
    outputs[HERE / "coverage.json"] = json.dumps(coverage, indent=1, ensure_ascii=False) + "\n"
    if args.check:
        stale = [str(p.relative_to(HERE)) for p, t in outputs.items() if not p.exists() or p.read_text() != t]
        if stale:
            raise SystemExit("Stale: " + ", ".join(stale))
        print("pilot cases current")
        return
    for path, text in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
    print(json.dumps({d: {"cases": len(i["cases"]), "controls": len(i["controls"]), "covered": i["covered_count"],
                          "of": i["catalog_size"], "redundant": i["redundant_cases"]} for d, i in coverage.items()}))


if __name__ == "__main__":
    main()
