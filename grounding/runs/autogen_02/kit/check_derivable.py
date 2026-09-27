"""Does code alone reproduce my Phase 1 derivability calls for drop-F? (Phase 2 bar: the same call on >= 90% of facts.)

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.kit.check_derivable

Runs `drop_f` without a request (so only the wording-independent checks apply: the match set, at least two matches,
scope D2) and compares with phase1_dropf.json, where a row with `not_derivable` is my call. Both constructions are
run: the Phase 1 one (labelled keys) and the semantic one used from Phase 2 on; they must agree on the exemplars.
"""
import json
from pathlib import Path

from grounding.runs.autogen_02.kit.policy import drop_f
from grounding.runs.autogen_02.phase1_build import exemplars

STUDY = Path(__file__).resolve().parents[1]


def main():
    cases = {c["case_id"]: c for c in exemplars()}
    spec = json.loads((STUDY / "phase1_dropf.json").read_text())["variants"]
    agree = same_construction = 0
    for v in spec:
        _, meta = drop_f(cases[v["scenario"]], v["fact"], None)
        _, sem = drop_f(cases[v["scenario"]], v["fact"], None, semantic=True)
        code_ok, mine_ok = not sem["problems"], "prompt" in v
        agree += code_ok == mine_ok
        same = (meta["dropped_keys"], meta["dropped_facts"], bool(meta["problems"])) == \
            (sem["dropped_keys"], sem["dropped_facts"], bool(sem["problems"]))
        same_construction += same
        if code_ok != mine_ok or not mine_ok:
            print(f"{v['scenario']} {v['fact']}: mine={'derivable' if mine_ok else v['not_derivable']} | "
                  f"code={sem['problems'] or 'derivable'} (matches {sem['matches']}, "
                  f"conditions left {sem['conditions_left']})")
        if not same:
            print(f"  CONSTRUCTIONS DIFFER on {v['scenario']} {v['fact']}: labelled {meta['dropped_keys']} "
                  f"{meta['dropped_facts']} {meta['problems']} | semantic {sem['dropped_keys']} {sem['dropped_facts']} "
                  f"{sem['problems']}")
    print(f"same call as mine on {agree} of {len(spec)} facts; semantic = labelled construction on "
          f"{same_construction} of {len(spec)}")


if __name__ == "__main__":
    main()
