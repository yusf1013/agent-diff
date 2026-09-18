"""Demonstrate slack_98 assertion gaps using constructed diffs, without API calls.

Run from backend:
    .venv/bin/python ../grounding/solver/slack/audit_slack98.py
"""
from copy import deepcopy
import json
from pathlib import Path
import sys

from grounding.paths import REPO_ROOT as ROOT
sys.path.insert(0, str(ROOT / "backend"))

from src.platform.evaluationEngine.assertion import AssertionEngine
from src.platform.evaluationEngine.compiler import DSLCompiler


def main():
    rows = [json.loads(line) for line in
            (ROOT / "datasets/agent-diff-bench/all_numbered.jsonl").read_text().splitlines()]
    row = next(row for row in rows if row["test_id"] == "slack_98")
    spec = json.loads(row["answer"])
    evaluator = AssertionEngine(DSLCompiler().compile(spec))
    unrelated_work = {
        "inserts": [
            {"__table__": "channels", "channel_id": "C_BOGUS",
             "channel_name": "unrelated-junk", "is_private": False},
            {"__table__": "messages", "message_id": "M_BOGUS",
             "channel_id": "C01ABCD1234", "user_id": "U01AGENBOT9",
             "message_text": "banana"},
        ],
        "updates": [], "deletes": [],
    }
    unrelated_removal = deepcopy(unrelated_work)
    unrelated_removal["deletes"].append({
        "__table__": "channel_members", "channel_id": "C_INFRA", "user_id": "U_SOPHIE",
    })
    cases = {"unrelated_channel_and_message": unrelated_work,
             "also_remove_unrelated_member": unrelated_removal}
    output = {"test_id": row["test_id"], "question": row["question"], "expected_output": spec,
              "method": "Constructed diffs passed to the actual compiler and assertion engine; no database or model calls.",
              "cases": {name: {"diff": diff, "evaluation": evaluator.evaluate(diff)}
                        for name, diff in cases.items()}}
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
