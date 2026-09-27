"""A mechanical-only look at a solver run (no judge): provisional failures and facts per form. For monitoring only.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_01.kit.peek SOLVE_RUN SUITE.json
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

from grounding.runs.autogen_01.kit.judge import latest, triage

run, suite = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
meta = {t["case_id"]: t for t in json.loads(suite.read_text())}
facts = defaultdict(set)
tests = defaultdict(set)
trials = 0
for summary in sorted(run.glob("t*/*/attempt-*/execution_summary.json")):
    attempt = summary.parent
    trial, case_id = attempt.parts[-3], attempt.parts[-2]
    if attempt != latest(run, trial, case_id) or json.loads(summary.read_text()).get("status") != "completed":
        continue
    trials += 1
    _, _, tri = triage(run.name, trial, attempt)
    form = meta.get(case_id, {}).get("form")
    if tri["outcome"] == "incorrect":
        tests[form].add(case_id)
        facts[form] |= set(tri["exposed"])
print(trials, "completed trials")
for form in sorted(tests, key=str):
    print(form, "tests with a provisional failure:", len(tests[form]), "facts:", sorted(facts[form]))
print("all facts:", sorted(set().union(*facts.values())) if facts else [])
