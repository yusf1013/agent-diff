"""Print accepted scenarios for manual validity review (markdown): request, conditions, target, decoys, background.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_01.kit.review_scenarios GEN_RUN > review.md
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from grounding.runs.autogen_01.kit.bundle import compact_row


def main():
    for run in sys.argv[1:]:
        for outcome_path in sorted(Path(run).glob("*/outcome.json")):
            o = json.loads(outcome_path.read_text())
            print(f"\n## {o['scenario_id']} ({o['domain']}): {o['status']}, {o['versions']} versions")
            print(f"Brief facts: {', '.join(o['brief']['facts'])}")
            if o["status"] != "accepted":
                last = o["history"][-1]
                print("Last findings:", *[f"\n- {p[:400]}" for p in last["problems"]])
                continue
            case = json.loads((outcome_path.parent / "case.json").read_text())
            ref = case["references"][0]
            table, key = ref["query"]["table"], ref["query"].get("key", ["id"])[0]
            rows = {str(r.get(key)): r for r in case["seed"].get(table, [])}
            print(f"\n**Request:** {case['prompt']}")
            print("\n**Conditions:** " + "; ".join(f"{c['id']} \"{c['text']}\" {c['facts']}" for c in case["conditions"]))
            for t in ref["expected"]:
                print(f"\n- TARGET `{t}`: {compact_row(rows.get(str(t), {}), 500)}")
            for c in ref["claims"]:
                w = str(c["witness"])
                flag = f" **contestable ({c['contestable'][:160]})**" if c.get("contestable") else ""
                print(f"- DECOY `{w}` {c['requirement']} {c.get('family')} [{c['mutation']['type']}]: "
                      f"{c['explanation']}{flag}\n  {compact_row(rows.get(w, {}), 500)}")
            decoys = {str(c["witness"]) for c in ref["claims"]} | {str(t) for t in ref["expected"]}
            others = [r for k, r in rows.items() if k not in decoys]
            if others:
                print(f"- background {table}: " + " | ".join(compact_row(r, 200) for r in others))
            for extra in case["references"][1:]:
                print(f"- other reference {extra['name']}: {extra['expected']}")
            print(f"- write: {json.dumps(case.get('write_check'))[:300]}")


if __name__ == "__main__":
    main()
