"""Print the several-match route tables (the shortcuts per kind of request)."""
from grounding.runs.several_match_02 import strategies
import grounding.runs.several_match_auto_01.checks  # noqa: F401  (adds the slack-channels-any table)
for kind, table in strategies.STRATEGIES.items():
    print("==", kind)
    for name, (thorough, _run) in table.items():
        print("   ", "T" if thorough else "-", name)
