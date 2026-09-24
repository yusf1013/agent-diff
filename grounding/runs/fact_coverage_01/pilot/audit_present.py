"""Audit target-present runs: was each near-miss actually looked at?

A near-miss is 'fetched' when its id appears in an action (explicit read), 'listed' when it appears only in
observations (e.g., a folder listing). A correct run whose near-misses were never fetched exercised only
listing-visible facts; relationship facts that need a detail read were not tested by that run.
"""
import json
import sys
from pathlib import Path

for run in sys.argv[1:]:
    for attempt in sorted(Path(run).glob("*/attempt-*")):
        case = json.loads((attempt / "case.json").read_text())
        rec = attempt / "solver" / f"{case['case_id']}.json"
        if case["form"] != "present" or not rec.exists():
            continue
        steps = json.loads(rec.read_text()).get("steps", [])
        actions = " ".join(s.get("action") or "" for s in steps)
        obs = " ".join(json.dumps(s.get("observation", {})) for s in steps)
        for ref in case["references"]:
            fetched, listed, unseen = [], [], []
            for c in ref["claims"]:
                w = str(c["witness"])
                (fetched if w in actions else listed if w in obs else unseen).append(c["requirement"])
            print(f"{case['case_id']:10} {attempt.parent.parent.name:14} {ref['id'][-2:]} fetched={fetched} "
                  f"listed_only={listed} unseen={unseen}")
