"""Score the plain judge (told nothing about grounding) against the same 178 hand labels J0 was scored on.

    python3 grounding/runs/baselines_01/q4/score_plain.py      # writes q4/plain_openclaw.score.json and prints it
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
JB = HERE.parents[1] / "judge_baselines_01"


def kind(key: str) -> str:
    case = key.split("/")[-1]
    if case.startswith("AT-"):
        return "absence twin"
    if case.startswith(("U-", "UC-")):
        return "underspecified"
    return "regular"


def main():
    trials = [t for t in json.loads((JB / "trials.json").read_text())
              if t["key"].startswith("openclaw_eval_01/") and t["truth"] is not None]
    verdicts = {}
    for name, folder in (("plain", HERE / "plain_openclaw"), ("j0", JB / "runs" / "j0")):
        verdicts[name] = {json.loads(p.read_text())["key"]: json.loads(p.read_text()).get("mistake")
                          for p in folder.rglob("verdict.json")}
    out = {}
    for name, v in verdicts.items():
        cells = defaultdict(lambda: {"TP": 0, "FP": 0, "FN": 0, "TN": 0, "none": 0})
        for t in trials:
            says = v.get(t["key"])
            for group in ("all", kind(t["key"])):
                c = cells[group]
                if says is None:
                    c["none"] += 1
                elif t["truth"] and says:
                    c["TP"] += 1
                elif t["truth"]:
                    c["FN"] += 1
                elif says:
                    c["FP"] += 1
                else:
                    c["TN"] += 1
        for c in cells.values():
            c["precision"] = round(c["TP"] / (c["TP"] + c["FP"]), 3) if c["TP"] + c["FP"] else None
            c["recall"] = round(c["TP"] / (c["TP"] + c["FN"]), 3) if c["TP"] + c["FN"] else None
        out[name] = dict(cells)
    (HERE / "plain_openclaw.score.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
