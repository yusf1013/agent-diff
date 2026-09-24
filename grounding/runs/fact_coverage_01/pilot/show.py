"""Print a compact trajectory for manual review: actions, truncated observations, answer, net changes.

    python -m grounding.runs.fact_coverage_01.pilot.show <attempt dir> [--obs 600]
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from grounding.runs.fact_coverage_01.pilot.analyze import attribute, changed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("attempt", type=Path)
    parser.add_argument("--obs", type=int, default=600)
    args = parser.parse_args()
    attempt = args.attempt
    case = json.loads((attempt / "case.json").read_text())
    record = json.loads(next((attempt / "solver").glob(f"{case['case_id']}.json")).read_text())
    print("PROMPT:", case["prompt"])
    for step in record.get("steps", []):
        action = step.get("action")
        if action:
            obs = step.get("observation", {})
            out = (obs.get("stdout") or "") + (("\n[stderr] " + obs["stderr"]) if obs.get("stderr") else "")
            print(f"\n--- turn {step['turn']} ACTION:\n{action[:1200]}")
            print(f"--- OBS: {out[:args.obs]}")
    print("\nTERMINATION:", record.get("termination"), "| FINAL:", (record.get("final") or "")[:1500])
    env = attempt / "environment"
    initial = json.loads((env / "initial_state.json").read_text())
    final = json.loads((env / "final_state.json").read_text())
    print("\nNET CHANGES:")
    for table in sorted(set(initial) | set(final)):
        key = ["id"] if initial.get(table) and "id" in initial[table][0] else None
        if not key:
            rows_a, rows_b = initial.get(table, []), final.get(table, [])
            if rows_a != rows_b:
                print(f"  {table}: {len(rows_a)} -> {len(rows_b)} rows")
            continue
        ch = changed(initial, final, table, key)
        if any(ch.values()):
            print(f"  {table}: " + ", ".join(f"{k}={sorted(v)}" for k, v in ch.items() if v))
    print("\nATTRIBUTION:", json.dumps(attribute(case, attempt)["references"], indent=1))


if __name__ == "__main__":
    main()
