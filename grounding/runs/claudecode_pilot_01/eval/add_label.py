"""Add my manual label for one pilot trial (written before any verdict exists on it).

    python3 add_label.py CASE_ID OUTCOME MECHANISM "NOTE" [FACT ...]
"""
import json
import sys
from datetime import datetime
from pathlib import Path

LABELS = Path(__file__).resolve().parent / "labels_pilot_01.json"
OUTCOMES = {"correct", "correct_absent", "incorrect", "presented", "false_absence", "incomplete", "not_established",
            "artifact"}

doc = json.loads(LABELS.read_text()) if LABELS.exists() else {
    "_about": "My labels (manual) for the Claude Code pilot's blind sample (blind_pilot_01.json: all 32 trials). Each "
              "trial is labelled once it has ended, from label_view.py (no verdict, no mechanical attribution), "
              "before any judge verdict on it exists. Rules as in autogen_02/kit/prompts/judge_v2.md."}
case_id, outcome, mechanism, note, *facts = sys.argv[1:]
assert outcome in OUTCOMES, outcome
key = f"pilot_01/t1/{case_id}"
assert key not in doc, f"{key} is already labelled"
doc[key] = {"outcome": outcome, "exposed": facts, "mechanism": mechanism, "note": note,
            "labelled_at": datetime.now().isoformat(timespec="seconds")}
LABELS.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
print(f"{key}: {outcome} {facts}; {len(doc) - 1} labelled")
