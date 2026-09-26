"""How the judge's verdicts compare with the scorer's mechanical label on the sampled clean trials of a run.

    python3 -m grounding.runs.autogen_01.kit.clean_agreement TRIALS.json JUDGED_DIR
"""
import json
import sys
from collections import Counter
from pathlib import Path

trials = {(t["trial"], t["case_id"]): t for t in json.loads(Path(sys.argv[1]).read_text())}
judged = Path(sys.argv[2])
pairs = Counter()
for path in judged.glob("*/*/*/verdict.json"):
    v = json.loads(path.read_text())
    trial, case = path.parts[-3], path.parts[-2]
    t = trials.get((trial, case), {})
    if t.get("clean_sample"):
        pairs[(t["provisional"], v["outcome"])] += 1
agree = sum(n for (a, b), n in pairs.items() if a == b)
print(f"clean sample: {sum(pairs.values())} trials, judge agrees with the mechanical label on {agree}")
for (a, b), n in sorted(pairs.items()):
    print(f"  {a} -> {b}: {n}")
