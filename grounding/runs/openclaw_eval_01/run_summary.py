"""One line per trial of a run: status, termination, tool calls, duration, requests and tokens, compactions, Calendar
clock suspects, and the mechanical triage (provisional outcome and exposed facts, before any judge).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.openclaw_eval_01.run_summary RUN_DIR [--json OUT]
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

from grounding.runs.autogen_01.kit.judge import latest
from grounding.runs.autogen_02.kit import judge2


def rows(run_dir: Path) -> list[dict]:
    out = []
    for summary_path in sorted(run_dir.glob("t*/*/attempt-*/execution_summary.json")):
        attempt = summary_path.parent
        trial, case_id = attempt.parts[-3], attempt.parts[-2]
        if attempt != latest(run_dir, trial, case_id):
            continue
        s = json.loads(summary_path.read_text())
        usage, flags = s.get("usage") or {}, s.get("flags") or {}
        row = {"trial": trial, "case_id": case_id, "attempt": attempt.name, "status": s.get("status"),
               "termination": s.get("termination"), "tool_calls": s.get("turns"),
               "seconds": (s.get("turn_durations_s") or [None])[0], "requests": usage.get("requests"),
               "input_tokens": usage.get("input_tokens"), "output_tokens": usage.get("output_tokens"),
               "limiter_wait_s": usage.get("limiter_wait_s"), "compactions": flags.get("compactions"),
               "clock_suspects": len(flags.get("clock_suspects") or []), "error": s.get("error")}
        if s.get("status") == "completed":
            _, _, tri = judge2.triage(run_dir.name, trial, attempt)
            row.update(provisional=tri["outcome"], exposed=tri["exposed"])
        out.append(row)
    return out


def main():
    run_dir = Path(sys.argv[1]).resolve()
    table = rows(run_dir)
    for r in table:
        print(f"{r['trial']}/{r['case_id']:28} {r['status']:20} {str(r['termination']):8} calls={r['tool_calls']} "
              f"{r['seconds']}s req={r['requests']} in={r['input_tokens']} out={r['output_tokens']} "
              f"wait={r['limiter_wait_s']} compact={r['compactions']} clock={r['clock_suspects']} "
              f"-> {r.get('provisional')} {r.get('exposed') or ''}" + (f" ERROR {r['error']}" if r["error"] else ""))
    print(dict(Counter(r["status"] for r in table)), dict(Counter(r.get("provisional") for r in table)))
    if "--json" in sys.argv:
        Path(sys.argv[sys.argv.index("--json") + 1]).write_text(json.dumps(table, indent=1) + "\n")


if __name__ == "__main__":
    main()
