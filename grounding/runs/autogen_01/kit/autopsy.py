"""Arm R, fact by fact: the exemplar's decoys next to the generated ones, with what each exposed; and the wording.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_01.kit.autopsy > grounding/runs/autogen_01/eval/autopsy.md

For every brief fact: each side's decoys (family, the author's explanation) and whether that decoy's single-decoy
probe exposed the fact at 3 trials (exemplar: fact_coverage_02's manual labels via eval/exemplar_outcomes.json;
generated: the scored run with my adjudication). Then, per scenario, the two requests with simple wording counts:
characters, the number of conditions, and phrases that name a field.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from grounding.runs.autogen_01.inputs.make_briefs import SLACK_ALIASES
from grounding.runs.autogen_01.kit.tables import EVAL, FC2, RUNS, adjudicated, load, outcomes
from grounding.runs.fact_coverage_02.followups import _conditions

FIELD_WORDS = re.compile(r"\b(whose|titled|named|called|description|purpose|topic|location|status|priority|"
                         r"created|modified|updated|due|size|tagged|labeled|labelled|attached|link|login|email)\b", re.I)


def canon(f):
    return SLACK_ALIASES.get(f, f)


def main():
    ex = load(EVAL / "exemplar_outcomes.json", {})
    score = load(RUNS / "solve_arm_r.score.json")
    score["_run"] = "solve_arm_r"
    tests, _ = adjudicated(score, load(EVAL / "judge_review.json", {}), load(EVAL / "validity.json", {}))
    by_case = {t["case_id"]: t for t in tests}
    print("# Arm R autopsy: decoys and wording, exemplar vs generated\n")
    wording = ["| Scenario | Exemplar request | chars / conditions / field words | Generated request | "
               "chars / conditions / field words |", "|---|---|---|---|---|"]
    for sid, o in sorted(outcomes("gen_arm_r").items()):
        ex_id = o["brief"]["exemplar"]
        ex_case = json.loads((FC2 / "cases_new" / o["domain"] / f"{ex_id}.json").read_text())
        gen_case = load(RUNS / "gen_arm_r" / sid / "case.json")
        print(f"## {ex_id} vs {sid}\n")
        for fact in o["brief"]["facts"]:
            print(f"**`{fact}`**: exemplar exposed: {'yes' if fact in ex.get(ex_id, {}).get('exposed', []) else 'no'}")
            for i, c in enumerate(ex_case["references"][0]["claims"]):
                if canon(c["requirement"]) != fact:
                    continue
                probe = ex.get(ex_id, {}).get("by_test", {}).get(f"P-{ex_id}-I1{i + 1}", {})
                print(f"- exemplar decoy ({c.get('family') or probe.get('family')}), probe failed "
                      f"{probe.get('failures', '?')}/{probe.get('established', '?')}: {c['explanation']}")
            if gen_case:
                for i, c in enumerate(gen_case["references"][0]["claims"]):
                    if c["requirement"] != fact:
                        continue
                    t = by_case.get(f"P-{sid}-I1{i + 1}", {})
                    fails = sum(1 for r in t.get("trials", {}).values() if r["outcome"] in ("incorrect", "presented"))
                    print(f"- generated decoy ({c.get('family')}), probe failed {fails}/{len(t.get('trials', {}))}"
                          f"{' (exposed after adjudication)' if t.get('exposed_adjudicated') else ''}: "
                          f"{c['explanation']}")
            print()
        if gen_case:
            def stats(case):
                p = case["prompt"]
                return f"{len(p)} / {_conditions(case['references'][0]['query'])} / {len(FIELD_WORDS.findall(p))}"
            wording.append(f"| {ex_id} | {ex_case['prompt']} | {stats(ex_case)} | {gen_case['prompt']} | "
                           f"{stats(gen_case)} |")
    print("## Wording\n")
    print("\n".join(wording))


if __name__ == "__main__":
    main()
