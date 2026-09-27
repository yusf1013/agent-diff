"""The Phase 3 population: autogen_01's 49 accepted generated scenarios and their (scenario, fact) pairs.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.kit.population [--survey]

`--survey` runs the code-only derivations on every pair (absence twin; drop-F without a request) and prints the
problems, so that construction gaps show before any agent is called.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from grounding.runs.autogen_01.kit.derive import normalize_effects

STUDY = Path(__file__).resolve().parents[1]
A1_RUNS = STUDY.parent / "autogen_01" / "runs"
ARMS = ("gen_arm_r", "gen_arm_p", "gen_arm_p_v2")


def scenarios() -> list[dict]:
    """The accepted generated scenario cases, effects keyed by their table's real key (as autogen_01 scored them)."""
    out = []
    for arm in ARMS:
        for outcome in sorted((A1_RUNS / arm).glob("*/outcome.json")):
            if json.loads(outcome.read_text()).get("status") != "accepted":
                continue
            case = json.loads((outcome.parent / "case.json").read_text())
            case["_arm"] = arm
            out.append(normalize_effects(case))
    return out


def pairs(cases: list[dict] | None = None) -> list[tuple[dict, str]]:
    from grounding.runs.autogen_02.kit.policy import facts_of
    return [(c, f) for c in (cases or scenarios()) for f in facts_of(c)]


def survey():
    from grounding.runs.autogen_02.kit.policy import absence_twins, drop_f
    cases = scenarios()
    ps = pairs(cases)
    print(f"{len(cases)} scenarios, {len(ps)} (scenario, fact) pairs;",
          dict(Counter(c["domain"] for c, _ in ps)))
    twin_problems = 0
    for c in cases:
        for twin, meta in absence_twins(c):
            if meta["errors"]:
                twin_problems += 1
                print(f"TWIN {meta['scenario']} {meta['fact']}: {meta['errors']}")
    print(f"absence twins with problems: {twin_problems}")
    reasons = Counter()
    for c, f in ps:
        _, meta = drop_f(c, f, None, semantic=True)
        if meta["problems"]:
            kinds = sorted({p.split(":")[0].split(" (")[0][:40] for p in meta["problems"]})
            reasons.update(kinds)
            print(f"DROPF {c['case_id']} {f}: keys={meta['dropped_keys']} matches={meta['matches']} "
                  f"left={meta['conditions_left']} {meta['problems']}")
    print("drop-F problem kinds:", dict(reasons))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--survey", action="store_true")
    args = parser.parse_args()
    if args.survey:
        survey()
    else:
        ps = pairs()
        print(json.dumps([{"scenario": c["case_id"], "domain": c["domain"], "fact": f} for c, f in ps], indent=1))
