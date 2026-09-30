"""The generation funnel of this study, as report_01's Table 5 counts it, with the policy units and the Muse cost
(generation, drop-F variants, and judge v2's verdicts in runs/judged_*).
No model calls; plain python3 is enough (run after suite.py, policy_units.py and cut.py).

    python3 grounding/runs/regen_01/funnel.py [--json]

Writes nothing unless --json is given, in which case it prints the numbers as JSON (the README's tables come from it).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS = HERE / "runs"


def calls(folder: Path) -> list[dict]:
    path = folder / "calls.jsonl"
    return [json.loads(line) for line in path.read_text().splitlines()] if path.exists() else []


def cost(rows: list[dict]) -> dict:
    return {"calls": len(rows), "failed_calls": sum(bool(r.get("is_error")) for r in rows),
            "list_usd": round(sum(r.get("cost_usd_list_price") or 0 for r in rows), 2),
            "billed_usd": round(sum(r.get("cost_usd_billed") or 0 for r in rows), 3)}


def main():
    review = {k: v for k, v in json.loads((HERE / "eval" / "review.json").read_text()).items() if not k.startswith("_")}
    variants = json.loads((HERE / "eval" / "variant_review.json").read_text())["dropf"]
    outcomes = [json.loads(p.read_text()) for p in sorted(RUNS.glob("gen_*/G4-*/outcome.json"))]
    check = json.loads((HERE / "suite" / "check.json").read_text())
    units = json.loads((HERE / "suite" / "units.json").read_text())
    cut = {r: json.loads((RUNS / f"{r}_cases.json").read_text()) for r in ("full_01", "absence_01", "underspecified_01")}
    dropf = [json.loads(p.read_text()) for p in sorted(RUNS.glob("dropf_*/U-*/record.json"))]
    near = [(sid, w, v) for sid, r in review.items() for w, v in r["decoys"].items()]
    verdicts = {}
    for r in review.values():
        head = r["verdict"].split(":")[0]
        verdicts[head] = verdicts.get(head, 0) + 1
    absence_built = [u for u in units["units"] if u["mode"] == "absence"]
    absence_excluded = [u for u in units["excluded_by_derivation"] if u.get("mode") == "absence"]
    status = {}
    for r in dropf:
        status[r["status"]] = status.get(r["status"], 0) + 1
    gen_calls = [c for g in sorted(RUNS.glob("gen_*")) for c in calls(g)]
    dropf_calls = [c for d in sorted(RUNS.glob("dropf_*")) for c in calls(d)]
    judged = {d.name: calls(d) for d in sorted(RUNS.glob("judged_*")) if d.is_dir()}
    judge_calls = [c for rows in judged.values() for c in rows]
    result = {
        "briefs": 35, "brief_attempts": len(outcomes),
        "accepted_scenarios": sum(o["status"] == "accepted" for o in outcomes),
        "attempts_rejected": sum(o["status"] == "rejected" for o in outcomes),
        "rejected": sorted(f"{o['scenario_id']}" for o in outcomes if o["status"] == "rejected"),
        "scenario_verdicts": verdicts, "usable_scenarios": sum(1 for r in review.values() if not r["verdict"].startswith("invalid")),
        "near_misses_declared": len(near), "near_misses_flawed": sum(v.startswith("flawed") for _, _, v in near),
        "near_misses_borderline": sum("borderline" in v and not v.startswith("flawed") for _, _, v in near),
        "regular": {"derived_candidates": check["tests"] + len(check["dropped"]), "dropped_by_witness_check": len(check["dropped"]),
                    "left_out_by_rulings": len(cut["full_01"]["left_out"]), "valid": len(cut["full_01"]["tests"])},
        "absence": {"candidates": len(absence_built) + len(absence_excluded), "excluded_by_derivation": len(absence_excluded),
                    "left_out_by_rulings": len(cut["absence_01"]["left_out"]), "valid": len(cut["absence_01"]["tests"])},
        "underspecified": {"jobs": len(dropf), "job_status": status,
                           "read_invalid": sum(not v["valid"] for v in variants.values()),
                           "duplicates": sum("duplicate" in why for why in cut["underspecified_01"]["left_out"].values()),
                           "left_out": len(cut["underspecified_01"]["left_out"]), "valid": len(cut["underspecified_01"]["tests"])},
        "cost": {"generation": cost(gen_calls), "drop_f": cost(dropf_calls),
                 "judge": {**cost(judge_calls), "by_folder": {name: cost(rows) for name, rows in judged.items()}},
                 "all": cost(gen_calls + dropf_calls + judge_calls)},
    }
    result["tests_to_run"] = result["regular"]["valid"] + result["absence"]["valid"] + result["underspecified"]["valid"]
    if "--json" in sys.argv:
        print(json.dumps(result, indent=1))
        return
    for k, v in result.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
