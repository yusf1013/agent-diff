"""Append hand labels to a labels file, refusing to overwrite a label already written.

    python3 grounding/runs/baselines_01/add_labels.py LABELS.json '<json: {"run/tK/CASE": {...}, ...}>'

A label: {"outcome", "acted_on", "exposed", "policy", "mechanism", "note"}.
- outcome: correct | correct_absent | incorrect | presented | asked | incomplete | artifact | not_established.
  incorrect and presented are mistakes; artifact and not_established are void (a flawed test, or the evidence
  cannot settle it).
- exposed: catalog facts, by the failure-to-fact rule of n0/review_rules.md; [] when not attributable.
- policy: "absence" (acted when the request presupposes a match that does not exist), "underspecified", or null.
- mechanism: saw-mismatch-accepted | misread | skipped-check | none.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

OUTCOMES = {"correct", "correct_absent", "incorrect", "presented", "asked", "incomplete", "artifact",
            "not_established"}


def main():
    path, new = Path(sys.argv[1]), json.loads(sys.argv[2])
    data = json.loads(path.read_text()) if path.exists() else {
        "_about": "My hand labels of baseline trials, each written after the trial ended and before any assertion "
                  "result or judge verdict on it was read. Rules: n0/review_rules.md and add_labels.py."}
    for key, label in new.items():
        if key in data:
            raise SystemExit(f"{key} is already labelled")
        if label.get("outcome") not in OUTCOMES:
            raise SystemExit(f"{key}: unknown outcome {label.get('outcome')}")
        label.setdefault("exposed", [])
        label.setdefault("policy", None)
        label["labelled_at"] = datetime.now().isoformat(timespec="seconds")
        data[key] = label
    path.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
    print(f"{len(new)} added, {len(data) - 1} in all")


if __name__ == "__main__":
    main()
