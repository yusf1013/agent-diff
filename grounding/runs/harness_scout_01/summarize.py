"""The smoke runs as a table: one row per attempt (plain python3; reads runs/*/<case>/attempt-*/)."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def row(attempt: Path) -> dict:
    summary = json.loads((attempt / "execution_summary.json").read_text())
    config_path = attempt / "solver" / "config.json"
    config = json.loads(config_path.read_text()) if config_path.exists() else {}
    usage = summary.get("usage") or {}
    flags = summary.get("flags") or {}
    diff_path = attempt / "environment" / "diff_run.json"
    changed = []
    if diff_path.exists():
        diff = json.loads(diff_path.read_text())["diff"]
        changed = sorted({f"{kind}:{r.get('__table__')}" for kind, rows in diff.items() for r in rows
                          if r.get("__table__") != "calendar_sync_tokens"})
    if summary.get("harness") == "claude":
        requests = usage.get("requests")
        result = usage.get("result_usage") or {}
        tokens_in = (result.get("input_tokens") or 0) + (result.get("cache_read_input_tokens") or 0) + \
            (result.get("cache_creation_input_tokens") or 0)
        tokens_out = result.get("output_tokens")
    else:
        requests = (usage.get("rollout") or {}).get("requests")
        tokens_in, tokens_out = usage.get("input_tokens"), usage.get("output_tokens")
    return {"run": attempt.parent.parent.name, "case": attempt.parent.name, "attempt": attempt.name,
            "model": config.get("model"), "status": summary.get("status"), "termination": summary.get("termination"),
            "seconds": summary.get("duration_s"), "tool_calls": flags.get("tool_calls"), "requests": requests,
            "tokens_in": tokens_in, "tokens_out": tokens_out, "state_changes": changed,
            "clock": (config.get("clock") or {}).get("method"), "leaks": flags.get("prompt_leaks"),
            "error": summary.get("error") or (flags.get("errors") or [None])[0]}


def main() -> None:
    rows = [row(a) for a in sorted((HERE / "runs").glob("*/*/attempt-*")) if (a / "execution_summary.json").exists()]
    (HERE / "smoke_table.json").write_text(json.dumps(rows, indent=2) + "\n")
    print("| run | case | attempt | model | status | s | tool calls | requests | tokens in / out | state changes |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        print(f"| {r['run']} | {r['case']} | {r['attempt'][-2:]} | {r['model']} | {r['status']} ({r['termination']}) | "
              f"{r['seconds']} | {r['tool_calls']} | {r['requests']} | {r['tokens_in']} / {r['tokens_out']} | "
              f"{', '.join(r['state_changes']) or 'none'} |")


if __name__ == "__main__":
    main()
