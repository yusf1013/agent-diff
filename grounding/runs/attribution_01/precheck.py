"""Source 2: would the kit's replica pre-checks have caught the development set's flawed tests before any run?

    SOLVER_BACKEND=purdue python grounding/runs/fact_coverage_02/launch.py grounding.runs.attribution_01.precheck

Runs autogen_01's `preflight.check` (install, reads, observability, write feasibility; no model calls) on the case
files the trials actually ran, for the flawed tests whose flaw a pre-check could see, and on their repaired reruns as
controls. The hand-made cases have no `write_check`; the one added here performs the write the request asks for on
the case's own target (built from the case's seed and reference, recorded in the output). Case ids get a suffix so
the temporary templates cannot collide with other work. Writes precheck/<case>/preflight.json and precheck.json.
"""
from __future__ import annotations

import copy
import json
import os
from pathlib import Path

from grounding.runs.autogen_01.kit import preflight

HERE = Path(__file__).resolve().parent
FC = HERE.parent / "fact_coverage_02/runs"
DB = os.environ.get("DATABASE_URL", "postgresql://postgres@127.0.0.1:15432/agentdiff_campaign")
BASE = os.environ.get("AGENTDIFF_BASE_URL", "http://127.0.0.1:18001")


def slack_reaction(case: dict, name: str) -> dict:
    ts = case["references"][0]["expected"][0]
    msg = next(m for m in case["seed"]["messages"] if str(m.get("message_id")) == str(ts))
    return {"slack": "reactions.add", "params": {"channel": msg["channel_id"], "timestamp": ts, "name": name}}


def linear_label(case: dict, issue_number: int, team_key: str) -> dict:
    team = next(t for t in case["seed"]["teams"] if t.get("key") == team_key)
    issue = next(i for i in case["seed"]["issues"] if i.get("teamId") == team["id"] and i.get("number") == issue_number)
    label = case["references"][0]["expected"][0]
    return {"graphql": f'mutation {{ issueUpdate(id: "{issue["id"]}", input: {{labelIds: ["{label}"]}}) '
                       f'{{ issue {{ id labels {{ nodes {{ id name }} }} }} }} }}'}


CHECKS = [  # (suffix, label, case file the trial ran, write check builder or None, what a pre-check could see)
    ("v1", "SLK-21 v1 (flawed: test-construction)", FC / "method_new/t1/SLK-21/attempt-01/case.json",
     lambda c: slack_reaction(c, "white_check_mark"), "the request's reaction name"),
    ("rerun", "SLK-21 rerun (control)", FC / "method_new_slk21/t1/SLK-21/attempt-01/case.json",
     lambda c: slack_reaction(c, "thumbsup"), "the request's reaction name"),
    ("v1", "LIN-25 v1 (flawed: test-construction)", FC / "method_new/t1/LIN-25/attempt-01/case.json",
     lambda c: linear_label(c, 3, "MOB"), "the seed's label ids"),
    ("rerun", "LIN-25 rerun (control)", FC / "method_new_lin25/t1/LIN-25/attempt-01/case.json",
     lambda c: linear_label(c, 3, "MOB"), "the seed's label ids"),
    ("v1", "P-LIN-03-I12 (mock: a project's lead is unreadable)", FC / "method_pilot/t1/P-LIN-03-I12/attempt-02/case.json",
     None, "observability of the deciding value"),
]


def main():
    out, summary = HERE / "precheck", []
    for suffix, label, path, build, sees in CHECKS:
        if not path.exists():
            summary.append({"label": label, "case": str(path), "error": "case file not found"})
            continue
        case = copy.deepcopy(json.loads(path.read_text()))
        case["case_id"] = f"{case['case_id']}-attr01-{suffix}"
        if build:
            case["write_check"] = build(case)
        report, problems = preflight.check(case, out / case["case_id"], DB, BASE)
        summary.append({"label": label, "case": path.relative_to(HERE.parent).as_posix(), "sees": sees,
                        "write_check": case.get("write_check"), "observability": report.get("observability"),
                        "write": report.get("write"), "problems": problems})
        print(f"\n== {label}\n   problems: {json.dumps(problems)[:900]}")
    (HERE / "precheck.json").write_text(json.dumps(summary, indent=1, default=str) + "\n")


if __name__ == "__main__":
    main()
