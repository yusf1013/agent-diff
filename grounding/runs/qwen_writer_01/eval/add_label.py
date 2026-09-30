"""Add my manual label for one blind-sample trial of this study's OpenClaw run, written before any verdict on it
exists. I read the trial with claudecode_pilot_01/eval/label_view.py (no verdict, no mechanical attribution).

    python3 add_label.py RUN/TRIAL/CASE_ID OUTCOME MECHANISM "NOTE" [FACT ...]
"""
import json
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTCOMES = {"correct", "correct_absent", "incorrect", "presented", "false_absence", "incomplete", "not_established",
            "artifact"}

key, outcome, mechanism, note, *facts = sys.argv[1:]
run = key.split("/")[0]
labels = HERE / f"labels_{run}.json"
blind = json.loads((HERE / f"blind_{run}.json").read_text())
assert key in blind["keys"], f"{key} is not in the blind sample"
assert outcome in OUTCOMES, outcome
doc = json.loads(labels.read_text()) if labels.exists() else {
    "_about": f"My labels (manual) for the blind sample of {run} (blind_{run}.json). Each trial is labelled once it "
              "has ended, from label_view.py (no verdict, no mechanical attribution), before any judge verdict on it "
              "exists. Rules as in autogen_02/kit/prompts/judge_v2.md."}
assert key not in doc, f"{key} is already labelled"
doc[key] = {"outcome": outcome, "exposed": facts, "mechanism": mechanism, "note": note,
            "labelled_at": datetime.now().isoformat(timespec="seconds")}
labels.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
print(f"{key}: {outcome} {facts}; {len(doc) - 1} labelled")
