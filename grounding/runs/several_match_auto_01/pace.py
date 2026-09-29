"""The solver's pace beside its timeouts, per 20-minute window: the self-host is shared with other sessions' runs,
so a timeout (a failure by the PI's rule) can come from slow turns as much as from the agent.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.several_match_auto_01.pace RUN_DIR [RUN_DIR ...]

Per window in which trials finished (the latest attempt of each): trials, median agent seconds per turn, timeouts,
and the timeouts whose environment already held every target changed (the work done, the answer cut off; several-
match cases only). Prints a table; writes nothing.
"""
from __future__ import annotations

import json
import statistics
import sys
import time
from collections import defaultdict
from pathlib import Path

from grounding.runs.several_match_01 import grade as base


def main(runs):
    windows = defaultdict(list)
    for run in runs:
        for s in Path(run).glob("t*/*/attempt-*/execution_summary.json"):
            att = s.parent
            if att != sorted(att.parent.glob("attempt-*"))[-1]:
                continue
            d = json.loads(s.read_text())
            if not d.get("turns"):
                continue
            t = time.localtime(s.stat().st_mtime)
            key = f"{t.tm_mon:02d}-{t.tm_mday:02d} {t.tm_hour:02d}:{(t.tm_min // 20) * 20:02d}"
            done = False
            if d.get("termination") == "timeout" and (att / "environment/diff_run.json").exists() and \
                    att.parent.name.startswith("SMA-"):
                case = json.loads((att / "case.json").read_text())
                done = {str(x) for x in case["references"][0]["expected"]} <= base.acted(case, att)
            windows[key].append(((d.get("clock") or {}).get("agent_seconds", 0) / d["turns"],
                                 d.get("termination") == "timeout", done))
    print("window        trials  s/turn  timeouts  (work done)")
    for k in sorted(windows):
        v = windows[k]
        print(f"{k}  {len(v):6}  {statistics.median(x for x, _, _ in v):6.1f}  {sum(1 for _, t, _ in v if t):8}"
              f"  {sum(1 for _, _, w in v if w):5}")


if __name__ == "__main__":
    main(sys.argv[1:])
