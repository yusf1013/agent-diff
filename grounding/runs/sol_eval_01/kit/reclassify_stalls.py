"""Reclassify provider stalls recorded before the runtime learned to catch them (2026-09-30, 00:55).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.sol_eval_01.kit.reclassify_stalls [--dry-run]

OpenClaw gives up on a model request after 120 s of silence ("LLM idle timeout (120s): no response from model") and
ends the turn as aborted; the runner recorded such attempts as completed with termination "timeout", which the
scoring would count as the solver's budget failure. They are the provider's failure (runtime rule R3, extended at
00:55), so this marks them `infrastructure_error`, keeping the original status in `reclassified_from`, and the
retry pass (`runs/run_retry.sh`, `--retry-infrastructure`) runs them again. Found by the sol_score session.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
STALL = re.compile(r"LLM idle timeout|no response from model")


def main() -> None:
    dry = "--dry-run" in sys.argv
    changed = []
    for summary_path in sorted((HERE / "runs").glob("*/t*/*/attempt-*/execution_summary.json")):
        s = json.loads(summary_path.read_text())
        if s.get("status") != "completed" or s.get("termination") != "timeout":
            continue
        stderr = summary_path.parent / "solver" / "openclaw" / "openclaw_turn1.stderr.txt"
        text = stderr.read_text(errors="replace") if stderr.exists() else ""
        turn = (s.get("turn_durations_s") or [0])[0]
        if not (STALL.search(text) or turn < 540):
            continue
        s.update(reclassified_from="completed", reclassified_at=datetime.now(timezone.utc).isoformat(),
                 status="infrastructure_error",
                 error=f"R3 provider stall: LLM idle timeout after {turn} s (reclassified by kit/reclassify_stalls.py)")
        changed.append(str(summary_path.relative_to(HERE)))
        if not dry:
            summary_path.write_text(json.dumps(s, indent=1, ensure_ascii=False) + "\n")
    print(f"{'would reclassify' if dry else 'reclassified'} {len(changed)} attempt(s)")
    for c in changed:
        print(" ", c)


if __name__ == "__main__":
    main()
