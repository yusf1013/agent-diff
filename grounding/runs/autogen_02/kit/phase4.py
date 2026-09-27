"""Phase 4: select the trials to judge and score a generated suite's run, with autogen_01's rules and this study's
triage (effects keyed by the real table key for tests outside autogen_01's folder).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.kit.phase4 select RUN_DIR SUITE > trials.json
    python ... phase4 score RUN_DIR SUITE JUDGED [--json OUT]
    python ... phase4 cases SUITE SCENARIO_ID ... > ids.txt     # the case ids of some scenarios, for `solve --cases`

select: every trial that is not mechanically clean, plus 20% of the clean ones (seed 7), as autogen_01.
score: a trial's outcome is judge v2's verdict when judged, else the provisional label (autogen_01's score_run).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from grounding.runs.autogen_01.kit import judge as v1
from grounding.runs.autogen_01.kit import score_run
from grounding.runs.autogen_02.kit.judge2 import triage

v1.triage = triage          # select_run looks it up in judge's module
score_run.triage = triage   # trial_outcomes imported it by name


def main():
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "select":
        print(json.dumps(v1.select_run(Path(args[0]).resolve(), Path(args[1]).resolve()), indent=1))
    elif cmd == "score":
        result = score_run.score(Path(args[0]).resolve(), Path(args[1]).resolve(), Path(args[2]).resolve())
        if "--json" in args:
            Path(args[args.index("--json") + 1]).write_text(json.dumps(result, indent=1) + "\n")
        print(json.dumps(result.get("all", result), indent=1)[:3000])
    elif cmd == "cases":
        wanted = set(args[1:])
        for t in json.loads(Path(args[0]).read_text()):
            if t.get("scenario") in wanted:
                print(t["case_id"])


if __name__ == "__main__":
    main()
