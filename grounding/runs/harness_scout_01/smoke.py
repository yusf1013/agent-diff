"""Smoke runs of our cases on a vendor harness (adapter.py), one attempt per case, sequentially.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.harness_scout_01.smoke \
        --harness claude|codex --backend plan|selfhost --out grounding/runs/harness_scout_01/runs/<run> \
        --cases G4-CAL-06 AR-LIN-24 P-G4-SLK-04-I11 [--model M] [--effort medium] [--attempt N]

Cases come from openclaw_eval_01's re-run folder (full_03_cases: opaque ids and test-side clocks, the PI's rulings
applied), which holds Calendar, Linear and Slack. An existing attempt folder is never overwritten.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from grounding.integrations.agentdiff.runtime import write
from grounding.paths import REPO_ROOT
from grounding.runs.harness_scout_01 import adapter

CASES = REPO_ROOT / "grounding/runs/openclaw_eval_01/runs/full_03_cases"


def find_case(case_id: str) -> tuple[dict, Path]:
    found = sorted(CASES.glob(f"*/{case_id}.json"))
    if not found:
        raise SystemExit(f"no case {case_id} under {CASES}")
    return json.loads(found[0].read_text()), found[0]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--harness", choices=("claude", "codex"), required=True)
    parser.add_argument("--backend", choices=("plan", "selfhost"), required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--cases", nargs="+", required=True)
    parser.add_argument("--model")
    parser.add_argument("--effort", default="medium")
    parser.add_argument("--attempt", type=int, default=1)
    parser.add_argument("--timeout", type=int, default=adapter.TIMEOUT_SECONDS)
    parser.add_argument("--keep-state", action="store_true")
    parser.add_argument("--database-url", default=os.getenv("DATABASE_URL",
                                                            "postgresql://postgres@127.0.0.1:15432/agentdiff_campaign"))
    parser.add_argument("--base-url", default="http://127.0.0.1:18001")
    args = parser.parse_args()
    os.environ.setdefault("DATABASE_URL", args.database_url)
    out = args.out if args.out.is_absolute() else REPO_ROOT / args.out
    for case_id in args.cases:
        case, path = find_case(case_id)
        attempt = out / case_id / f"attempt-{args.attempt:02d}"
        if attempt.exists():
            print(f"{case_id}: {attempt} exists, skipped")
            continue
        attempt.mkdir(parents=True)
        write(attempt / "case_source.json", {"path": str(path.relative_to(REPO_ROOT)), "case_sha256": case.get("case_sha256")})
        summary = adapter.run_attempt(case, attempt, harness=args.harness, backend=args.backend,
                                      database_url=args.database_url, backend_url=args.base_url, model=args.model,
                                      effort=args.effort, timeout_s=args.timeout, keep_state=args.keep_state)
        usage = summary.get("usage") or {}
        print(f"{case_id}: {summary.get('status')} {summary.get('termination')} {summary.get('duration_s')}s "
              f"tools={summary.get('flags', {}).get('tool_calls')} err={summary.get('error')} "
              f"cost_list={usage.get('total_cost_usd_list')}")


if __name__ == "__main__":
    main()
