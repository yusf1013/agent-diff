"""The pilot in numbers: per-run time, tool calls, requests, tokens, list-price cost and the plan's windows, with the
Sol pilot (OpenClaw, GPT-6.1 Sol, the same 32 tests) alongside. Plain python3; reads execution summaries only.

    python3 grounding/runs/claudecode_pilot_01/summarize.py [RUN_DIR] [SOL_RUN_DIR]

Writes pilot_summary.json next to this file.
"""
import json
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUN = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "runs" / "pilot_01"
SOL = Path(sys.argv[2]) if len(sys.argv) > 2 else \
    Path("/home/yusf/PyProj/agent-diff/grounding/runs/sol_pilot_01/runs/pilot_01")


def latest(run: Path):
    for case_dir in sorted((run / "t1").iterdir()):
        attempts = sorted(case_dir.glob("attempt-*/execution_summary.json"))
        if attempts:
            yield json.loads(attempts[-1].read_text())


def dist(values):
    values = [v for v in values if v is not None]
    if not values:
        return None
    values = sorted(values)
    return {"n": len(values), "median": statistics.median(values), "mean": round(statistics.mean(values), 2),
            "p90": values[min(len(values) - 1, int(0.9 * len(values)))], "max": values[-1], "sum": round(sum(values), 4)}


def claude_rows(run: Path):
    rows = []
    for s in latest(run):
        u = s.get("usage") or {}
        r = u.get("result_usage") or {}
        tokens_in = sum(r.get(k) or 0 for k in ("input_tokens", "cache_read_input_tokens", "cache_creation_input_tokens"))
        rows.append({"case_id": s["case_id"], "status": s.get("status"), "termination": s.get("termination"),
                     "seconds": (s.get("turn_durations_s") or [None])[0], "tool_calls": s.get("turns"),
                     "requests": u.get("requests"), "input_tokens": tokens_in,
                     "cached_input_tokens": r.get("cache_read_input_tokens"), "output_tokens": r.get("output_tokens"),
                     "thinking_tokens": u.get("thinking_tokens"), "list_cost_usd": u.get("list_cost_usd"),
                     "windows_first": u.get("plan_windows_first"), "windows_last": u.get("plan_windows_last"),
                     "started": s.get("started_utc"), "ended": s.get("ended_utc"), "error": s.get("error")})
    return rows


def sol_rows(run: Path):
    rows = []
    if not run.exists():
        return rows
    for s in latest(run):
        u = s.get("usage") or {}
        rows.append({"case_id": s["case_id"], "status": s.get("status"), "seconds": (s.get("turn_durations_s") or [None])[0],
                     "tool_calls": s.get("turns"), "requests": u.get("requests"), "input_tokens": u.get("input_tokens"),
                     "cached_input_tokens": u.get("cached_input_tokens"), "output_tokens": u.get("output_tokens"),
                     "reasoning_tokens": u.get("reasoning_tokens")})
    return rows


def windows(rows):
    """The plan's windows as the earliest and the latest run saw them (shared with every other use of the account)."""
    seen = [(r["started"], r["windows_first"]) for r in rows if r.get("windows_first")] + \
           [(r["ended"], r["windows_last"]) for r in rows if r.get("windows_last")]
    seen.sort(key=lambda x: x[0] or "")
    if not seen:
        return None
    first, last = seen[0], seen[-1]

    def flat(w):
        return {k: {"utilization": v.get("utilization"),
                    "resets_at": datetime.fromtimestamp(v["resets_at"], timezone.utc).isoformat() if v.get("resets_at") else None}
                for k, v in (w[1].get("windows") or {}).items()}
    return {"first": {"at": first[0], **flat(first)}, "last": {"at": last[0], **flat(last)}}


def main():
    claude, sol = claude_rows(RUN), sol_rows(SOL)
    done = [r for r in claude if r["status"] == "completed"]
    out = {
        "run": str(RUN), "attempts": len(claude),
        "status": {k: sum(1 for r in claude if r["status"] == k) for k in sorted({r["status"] for r in claude})},
        "termination": {k: sum(1 for r in claude if r["termination"] == k) for k in sorted({str(r["termination"]) for r in claude})},
        "claude": {k: dist([r[k] for r in done]) for k in ("seconds", "tool_calls", "requests", "input_tokens",
                                                          "cached_input_tokens", "output_tokens", "thinking_tokens",
                                                          "list_cost_usd")},
        "plan_windows": windows(claude),
        "sol_pilot": {"run": str(SOL), "attempts": len(sol),
                      **{k: dist([r[k] for r in sol if r["status"] == "completed"])
                         for k in ("seconds", "tool_calls", "requests", "input_tokens", "cached_input_tokens",
                                   "output_tokens", "reasoning_tokens")}},
        "rows": claude}
    (HERE / "pilot_summary.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k != "rows"}, indent=1))


if __name__ == "__main__":
    main()
