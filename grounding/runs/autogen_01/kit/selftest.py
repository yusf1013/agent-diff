"""Offline self-test of the kit (no model or service calls).

    python -m grounding.runs.autogen_01.kit.selftest

1. The worked examples build without problems, and their expanded seeds equal the pilot's own seeds for BOX-01 and
   CAL-01 (the seed operations reproduce the hand-built rows).
2. Their suites have the expected tests.
3. Known defects are caught: a non-UUID Linear label id, a Slack reaction the replica rejects, a decoy that also
   meets the request, an escape clause in the request, a missing primary fact.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path

from grounding.runs.autogen_01.kit import derive, scenario

KIT = Path(__file__).resolve().parent
PILOT = KIT.parents[1] / "fact_coverage_01" / "pilot" / "cases"


def rows_equal(a, b):
    def norm(seed):
        return {t: sorted(json.dumps(r, sort_keys=True) for r in rows) for t, rows in seed.items() if rows}
    na, nb = norm(a), norm(b)
    diffs = []
    for t in sorted(set(na) | set(nb)):
        if na.get(t) != nb.get(t):
            diffs.append(t)
    return diffs


def main():
    failures = 0
    for name, pilot_id in (("box-example.json", "box/BOX-01.json"), ("calendar-example.json", "calendar/CAL-01.json")):
        s = json.loads((KIT / "examples" / name).read_text())
        brief = {"scenario_id": s["scenario_id"], "domain": s["domain"],
                 "facts": sorted({d["fact"] for d in s["reference"]["decoys"]})}
        case, problems = scenario.build(s, brief)
        print(name, "problems:", problems or "none")
        failures += bool(problems)
        pilot = json.loads((PILOT / pilot_id).read_text())
        diffs = rows_equal(case["seed"], pilot["seed"])
        print("  seed tables differing from the pilot:", diffs or "none")
        failures += bool(diffs)
        tests = derive.suite(case)
        print("  suite:", [(t["case_id"], m["form"]) for t, m in tests])

    # Known defects
    base = json.loads((KIT / "examples" / "box-example.json").read_text())
    brief = {"scenario_id": base["scenario_id"], "domain": "box", "facts": ["A:File.extension"]}
    cases = {
        "escape clause": lambda s: s.__setitem__("request", s["request"] + " If there isn't one, just tell me."),
        "decoy also matches": lambda s: s["seed"].__setitem__(4, ["file", {"id": "1002", "name": "Q3 expense summary.pdf",
                                                                            "parent": "100", "owner": "MC", "creator": "MC",
                                                                            "modifier": "LP"}]),
        "missing primary fact": lambda s: s["reference"].__setitem__("decoys", s["reference"]["decoys"][1:2] and
                                                                     [d for d in s["reference"]["decoys"]
                                                                      if d["fact"] != "A:File.extension"]),
        "id in request": lambda s: s.__setitem__("request", s["request"].replace("the PDF", "the PDF 1001")),
    }
    for label, mutate in cases.items():
        s = copy.deepcopy(base)
        mutate(s)
        _, problems = scenario.build(s, brief)
        print(f"defect '{label}':", "caught" if problems else "MISSED", problems[:2])
        failures += not problems
    lin = {"scenario_id": "T-LIN", "domain": "linear", "request": "Set the priority to High on the bug.", "answer": "one",
           "seed": [["team", {"id": "t1", "name": "Web", "key": "WEB"}], ["label", {"id": "lab-bug", "name": "Bug"}]],
           "conditions": [], "reference": {"name": "x", "target": ["i1"], "query": {"table": "issues"}, "decoys": [],
                                           "effect": {"table": "issues", "changes": ["update"]}}, "write": {}}
    _, problems = scenario.build(lin, {"scenario_id": "T-LIN", "domain": "linear", "facts": []})
    print("defect 'non-UUID label id':", "caught" if any("UUID" in p for p in problems) else "MISSED", problems[:1])
    failures += not any("UUID" in p for p in problems)
    slk = {"scenario_id": "T-SLK", "domain": "slack", "request": "Add a :white_check_mark: to Diego's message.",
           "answer": "one", "seed": [["channel", {"id": "C1", "name": "general", "members": ["diego"]}],
                                     ["message", {"channel": "C1", "author": "diego", "text": "hi",
                                                  "at": "2026-09-21T14:06:00Z", "ref": "m"}]],
           "conditions": [], "reference": {"name": "x", "target": ["@m"],
                                           "query": {"table": "messages", "filters": [], "edges": []}, "decoys": [],
                                           "effect": {"table": "message_reactions", "changes": ["insert"]}},
           "write": {"slack": "reactions.add", "params": {"name": "white_check_mark"}}}
    _, problems = scenario.build(slk, {"scenario_id": "T-SLK", "domain": "slack", "facts": []})
    ok = any("rejects" in p for p in problems)
    print("defect 'Slack reaction':", "caught" if ok else "MISSED", problems[:2])
    failures += not ok
    print("FAILURES:", failures)
    return failures


if __name__ == "__main__":
    raise SystemExit(main())
