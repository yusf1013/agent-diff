"""Which trials of a run have ended and are not yet labelled.

    python3 grounding/runs/baselines_01/progress.py RUN_DIR LABELS.json
"""
import json
import sys
from pathlib import Path

run, labels_path = Path(sys.argv[1]), Path(sys.argv[2])
labels = json.loads(labels_path.read_text()) if labels_path.exists() else {}
done, todo, running = 0, [], 0
for summary in sorted(run.glob("t*/*/attempt-*/execution_summary.json")):
    s = json.loads(summary.read_text())
    if summary.parent != sorted(summary.parent.parent.glob("attempt-*"))[-1]:
        continue
    if s.get("status") in ("preflight", "solver_running"):
        running += 1
        continue
    done += 1
    key = f"{run.name}/{summary.parent.parent.parent.name}/{summary.parent.parent.name}"
    if key not in labels:
        todo.append(key.split("/", 1)[1])
print(json.dumps({"ended": done, "running": running, "unlabelled": todo}))
