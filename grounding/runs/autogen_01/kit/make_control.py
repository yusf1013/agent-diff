"""The same-day control (plan.md amendment 3): the exemplars' 76 tests of the 18 new scenarios, copied unchanged.

    python3 -m grounding.runs.autogen_01.kit.make_control

Writes runs/control/cases/<domain>/<case>.json (byte-identical copies of fact_coverage_02/cases_new, whose LIN-25
and SLK-21 files are the fixed reruns) and runs/control/suite.json in the generated suites' format, with Slack's
older fact names mapped to catalog ids.
"""
import json
import shutil
from pathlib import Path

from grounding.runs.autogen_01.inputs.make_briefs import SLACK_ALIASES

STUDY = Path(__file__).resolve().parents[1]
FC2 = STUDY.parent / "fact_coverage_02"
OUT = STUDY / "runs" / "control"


def main():
    suite = json.loads((FC2 / "suite_new.json").read_text())
    index = []
    for t in suite:
        if t["form"] not in ("cover control", "probe"):
            continue  # the Slack policy panel is not part of the 76
        src = FC2 / "cases_new" / t["domain"] / f"{t['case_id']}.json"
        dst = OUT / "cases" / t["domain"] / src.name
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)
        index.append({"case_id": t["case_id"], "domain": t["domain"],
                      "form": "cover" if t["form"] == "cover control" else "probe", "scenario": t["scenario"],
                      "fact": SLACK_ALIASES.get(t["fact"], t["fact"]) if t["fact"] else None, "family": t["family"]})
    (OUT / "suite.json").write_text(json.dumps(sorted(index, key=lambda x: x["case_id"]), indent=1) + "\n")
    print(len(index), "tests;", sum(t["form"] == "cover" for t in index), "covers")


if __name__ == "__main__":
    main()
