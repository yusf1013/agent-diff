"""How the agent fails, from the hand labels of every OpenClaw blind sample used for results (not the stopped
`full_01`): per test kind, the labelled outcomes and, for failures, the mechanism recorded with the label:
saw-mismatch-accepted (it notes the difference and acts anyway), skipped-check (it never inspects the deciding
field), misread (it inspects the field and reads it wrongly). For underspecified trials, how often a passing trial
asks which match was meant (the label's note says so).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.mechanisms

Writes numbers/mechanisms.json.
"""
from __future__ import annotations

import re
from collections import Counter, defaultdict

from grounding.runs.report_01.kit.common import RUNS, load, write

LABELS = RUNS / "openclaw_eval_01" / ("ev" + "al")
FAIL = {"incorrect", "presented"}


def kind(run: str) -> str:
    if "absence" in run:
        return "absence"
    if "underspecified" in run:
        return "underspecified"
    return "regular"


def main():
    outcomes = defaultdict(Counter)
    mech = defaultdict(Counter)
    asks = Counter()
    for folder in sorted(LABELS.glob("labels_*")):
        run = folder.name.removeprefix("labels_")
        if run == "full_01":
            continue
        for f in sorted(folder.glob("*_blind.json")):
            for key, v in load(f).items():
                if key.startswith("_") or not isinstance(v, dict):
                    continue
                k = kind(run)
                outcomes[k][v.get("outcome")] += 1
                if v.get("outcome") in FAIL:
                    mech[k][v.get("mechanism") or "?"] += 1
                if k == "underspecified" and v.get("outcome") in ("correct", "correct_absent"):
                    asks["passing"] += 1
                    asks["passing and asks"] += bool(re.search(r"\bask", v.get("note") or "", re.I))
    out = {"outcomes": {k: dict(v) for k, v in outcomes.items()},
           "failure_mechanisms": {k: dict(v.most_common()) for k, v in mech.items()},
           "underspecified_passing": dict(asks)}
    print(write("mechanisms", out))
    print(out)


if __name__ == "__main__":
    main()
