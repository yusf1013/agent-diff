"""Clean up what the OpenClaw attempts cut off at 08:01 (the stop at 16 in flight, cycle 6) left behind, with the calls
the runtime makes on its normal path (integrations/openclaw/runtime.py, run_attempt's `finally`): the AgentDiff
environment (`client.delete_env`, under the DDL lock), the installed template (`cleanup_template`), and the attempt's
OpenClaw state directory. Only attempts of runs/oc_01 whose status is still "solver_running" or "preflight" are
touched, each by the ids its own records hold. No model calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.qwen_writer_01.cleanup_cut_off

Writes runs/oc_01_cleanup.json: per attempt, what was removed or why not.
"""
import json
import os
import shutil
from pathlib import Path

from agent_diff import AgentDiff

from grounding.integrations.agentdiff.runtime import ddl_lock
from grounding.integrations.openclaw import runtime as oc

HERE = Path(__file__).resolve().parent
RUN = HERE / "runs" / "oc_01"
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://postgres@127.0.0.1:15432/agentdiff_campaign")
BACKEND_URL = "http://127.0.0.1:18001"


def main():
    client = AgentDiff(base_url=BACKEND_URL)
    report = []
    for path in sorted(RUN.glob("t*/*/attempt-*/execution_summary.json")):
        summary = json.loads(path.read_text())
        if summary.get("status") not in ("solver_running", "preflight"):
            continue
        attempt = path.parent
        row = {"attempt": str(attempt.relative_to(RUN)), "status": summary.get("status")}
        env_id = summary.get("environment_id")
        if env_id:
            try:
                with ddl_lock():
                    client.delete_env(envId=env_id)
                row["environment"] = f"deleted {env_id}"
            except Exception as exc:
                row["environment"] = f"{env_id}: {type(exc).__name__}: {str(exc)[:200]}"
        else:
            row["environment"] = "none recorded"
        prepared_files = list((attempt / "environment").glob("**/prepared.json"))
        if prepared_files:
            prepared = json.loads(prepared_files[0].read_text())
            case = json.loads((attempt / "case.json").read_text())
            try:
                oc.cleanup_template(case, prepared, DATABASE_URL)
                row["template"] = f"cleaned {prepared.get('template_name')}"
            except Exception as exc:
                row["template"] = f"{prepared.get('template_name')}: {type(exc).__name__}: {str(exc)[:200]}"
        else:
            row["template"] = "no prepared.json (stopped before the template was recorded)"
        config = attempt / "solver" / "config.json"
        state = json.loads(config.read_text()).get("state_dir") if config.exists() else None
        if state and Path(state).exists():
            shutil.rmtree(state, ignore_errors=True)
            row["state_dir"] = f"removed {state}"
        else:
            row["state_dir"] = "none recorded or already gone"
        report.append(row)
        print(json.dumps(row))
    (HERE / "runs" / "oc_01_cleanup.json").write_text(json.dumps(report, indent=1) + "\n")
    print(f"{len(report)} cut-off attempts processed")


if __name__ == "__main__":
    main()
