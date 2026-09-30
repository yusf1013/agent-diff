"""Mark the run's timeouts under host load (host_load.py, the lead's rule of 2026-09-30) as infrastructure errors, so
that the runner's --retry-infrastructure reruns them, on a quiet server, in a new attempt folder. The attempt stays on
disk; its summary keeps every original field under `reclassified_from` and says why. No model calls.

    python3 grounding/runs/qwen_writer_01/reclassify_host_load.py [RUN]

Writes nothing unless eval/host_load_RUN.json lists trials under host load; prints what it changed.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    run = sys.argv[1] if len(sys.argv) > 1 else "oc_01"
    doc = json.loads((HERE / "eval" / f"host_load_{run}.json").read_text())
    for row in doc["trials"]:
        if not row["host_load"]:
            continue
        path = HERE / "runs" / run / row["trial"] / row["attempt"] / "execution_summary.json"
        summary = json.loads(path.read_text())
        if summary.get("status") != "completed":
            print("already reclassified or not completed:", row["trial"], summary.get("status"))
            continue
        original = {k: summary[k] for k in ("status", "termination", "error") if k in summary}
        summary.update(status="infrastructure_error",
                       error="timeout under host load (the lead's rule, 2026-09-30: few requests, each slow; "
                             f"{row['requests']} requests, median {row['median_request_s']} s); rerun when quiet",
                       reclassified_from={**original, "at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                          "by": "qwen_writer_01/reclassify_host_load.py"})
        path.write_text(json.dumps(summary, indent=1) + "\n")
        print("reclassified", row["trial"], row["attempt"])


if __name__ == "__main__":
    main()
