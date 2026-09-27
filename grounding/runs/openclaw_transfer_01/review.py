"""Print what manual review needs for OpenClaw attempts: prompt, grading, changes, reply, tool calls, reasoning.

    python3 -m grounding.runs.openclaw_transfer_01.review rows.json [--outcomes acted_wrong asked ...] [--cases ...]

rows.json comes from analyze.py --json.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def show(row: dict, width: int = 260) -> None:
    attempt = Path(row["attempt"])
    case = json.loads((attempt / "case.json").read_text())
    record = json.loads((attempt / "solver" / f"{row['case_id']}.json").read_text())
    print("=" * 100)
    print(f"{row['run']}/{row['case_id']}  [{row.get('condition')}]  outcome={row.get('outcome')} oc={row.get('oc_outcome')} "
          f"acted={row.get('acted')} expected={row.get('expected')} exposed={row.get('exposed')} "
          f"followup={row.get('followup_outcome')} {row.get('followup_acted', '')}")
    print("PROMPT:", record.get("question"))
    for claim in case.get("references", [{}])[0].get("claims", []):
        print(f"  claim {claim['requirement']} witness={claim['witness']}: {claim.get('explanation')}")
    for i, step in enumerate(record.get("steps", [])):
        if step.get("tool") == "read":
            print(f"  [{i}] read {str(step['arguments'].get('path', '')).split('skills/')[-1]}")
        elif step.get("tool"):
            print(f"  [{i}] {step['tool']}: {(step.get('action') or '')[:width]}".replace("\n", " "))
            print(f"       -> {(step.get('observation') or {}).get('stdout', '')[:width]}".replace("\n", " "))
    last_thinking = next((s["thinking"] for s in reversed(record.get("steps", [])) if s.get("thinking")), "")
    print("LAST THINKING:", last_thinking[:900].replace("\n", " "))
    print("REPLY:", (attempt / "solver/final_response.md").read_text().strip()[:1500])
    if (attempt / "solver/followup_response.md").exists():
        print("FOLLOW-UP REPLY:", (attempt / "solver/followup_response.md").read_text().strip()[:800])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("rows", type=Path)
    parser.add_argument("--outcomes", nargs="*")
    parser.add_argument("--cases", nargs="*")
    parser.add_argument("--conditions", nargs="*")
    args = parser.parse_args()
    for row in json.loads(args.rows.read_text()):
        if row.get("status") != "completed" or not row.get("reference", "").endswith(".r1"):
            continue
        if args.outcomes and row.get("oc_outcome") not in args.outcomes:
            continue
        if args.cases and row["case_id"] not in args.cases:
            continue
        if args.conditions and row.get("condition") not in args.conditions:
            continue
        show(row)


if __name__ == "__main__":
    main()
