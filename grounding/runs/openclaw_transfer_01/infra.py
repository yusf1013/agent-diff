"""Mark finished attempts whose turn-1 outcome was decided by infrastructure, so run.py --retry-infrastructure reruns them.

    python3 -m grounding.runs.openclaw_transfer_01.infra runs/t1 [runs/t2 ...] [--apply]

Two rules, applied from each attempt's own records (proxy metas in requests.tar.xz, execution_summary usage):
- R1 provider hang: the turn ended normally, but its last model request came back as a cut stream (HTTP 200, no finish
  reason, no terminator), or OpenClaw compacted after a cut stream to recover. The reply is not the agent's answer.
- R2 rate-limit timeout: the turn hit the time limit after the shared rate limiter had held its requests for more than
  a quarter of the turn budget (150 of 600 s). Our own request budget, not the agent, ran the clock out.
A marked attempt keeps all its files; its execution_summary.json gets status "infrastructure_error" and a
"status_revised" entry with the rule and evidence. Nothing is deleted.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from grounding.runs.openclaw_transfer_01.streams import cut_requests

LIMITER_SHARE = 0.25


def verdict(attempt: Path, summary: dict) -> str | None:
    cut, total, _ = cut_requests(attempt)
    termination = summary.get("termination")
    budget = json.loads((attempt / "solver" / "config.json").read_text()).get("timeout_seconds_per_turn", 600) \
        if (attempt / "solver" / "config.json").exists() else 600
    waited = (summary.get("usage") or {}).get("limiter_wait_s", 0) or 0
    compacted = (summary.get("flags") or {}).get("compactions")
    if termination == "done" and cut and (cut[-1] == f"{total:04d}" or compacted):
        return f"R1 provider hang: model request {cut[-1]} came back as a cut stream" + \
               (" and OpenClaw compacted to recover" if cut[-1] != f"{total:04d}" else "")
    if termination == "timeout" and waited > LIMITER_SHARE * budget:
        return f"R2 rate-limit timeout: the turn hit the {budget} s limit after {waited:.0f} s waiting for the shared rate limiter"
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("runs", nargs="+", type=Path)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    for run in args.runs:
        for path in sorted(run.glob("*/attempt-*/execution_summary.json")):
            summary = json.loads(path.read_text())
            revised = summary.get("status_revised")
            if summary.get("status") != "completed" and not revised:
                continue
            reason = verdict(path.parent, summary)
            if not reason:
                if revised:
                    print(f"{path.parent}: previously revised, no rule applies now: {revised.get('reason')}")
                continue
            if revised and revised.get("reason") == reason:
                continue
            print(f"{path.parent}: {reason}" + (f" (replaces earlier reason: {revised['reason']})" if revised else ""))
            if args.apply:
                entry = {"from": revised["from"] if revised else summary["status"], "rule": reason.split(":")[0],
                         "reason": reason, "by": "infra.py"}
                if revised:
                    entry["earlier_reason"] = revised.get("reason")
                summary.update(status="infrastructure_error", error=reason, status_revised=entry)
                path.write_text(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
