"""Print each judge disagreement with the reference note and the judge's note (for reading, dev split only).

    python -m grounding.runs.autogen_01.kit.show_disagreements JUDGE_OUT
"""
import json
import sys
from pathlib import Path

from grounding.runs.autogen_01.kit.judge import FC2

out = Path(sys.argv[1])
labels = json.loads((FC2 / "manual_labels.json").read_text())
comparison = json.loads((out / "comparison.json").read_text())
for d in comparison["disagreements"]:
    v = json.loads((out / d["key"] / "verdict.json").read_text())
    ref = labels.get(d["key"], {})
    print(f"### {d['key']} form={v.get('form')}")
    print(f"  REF   {d['ref']} {d['ref_exposed']} :: {ref.get('note', '(clean, unlabelled)')[:600]}")
    print(f"  JUDGE {d['judge']} {d['judge_exposed']} mech={v.get('mechanism')} :: {v.get('note', '')[:600]}"
          + (f" | artifact: {v.get('artifact_reason')[:200]}" if v.get("artifact_reason") else ""))
