"""The random sample of the plain-twin ablation: 48 probes with a designated substitute (F1 to F8), 12 per service,
drawn without looking at whether they exposed a fact (the PI's choice of 48, 2026-09-28).

    python3 grounding/runs/baselines_01/plain48/pick.py      # writes pick.json and prints it

- **Population:** the frozen suite of this worktree (`openclaw_eval_01/suite/suite.json`, the version cycle 2 and
  ours.json used), form `probe`, family F1 to F8.
- **Left out:** the scenarios cycle 2 left out (plain_pick.json); G4-BOX-01, whose wording OpenClaw reads as
  tag-and-comment (cycle 2); and, from the lead's current known-defects list (exp/roadmap-02, copied here as
  known_defects.roadmap-02.json), every case marked "leave out" or "read before it runs", every scenario ruled
  flawed for its near miss, and every scenario that needed a test-side clock (this suite has no such clock).
- **Draw:** per service, 12 at random with a fixed seed. Cycle 2's 12 probes may be drawn again.
- **Replacement (rule fixed before any plain version was built):** a probe whose substitute cannot be removed without
  making the near miss fail a second condition of the request, or without offering another designated substitute,
  has no plain twin; it is replaced by the next probe of a seeded reserve order of the same service (REPLACED).
"""
from __future__ import annotations

import json
import random
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SUITE = HERE.parents[1] / "openclaw_eval_01" / "suite" / "suite.json"
SEED = 20260929
PER_DOMAIN = 12
DESIGNATED = {f"F{i}" for i in range(1, 9)}
REPLACED = {
    "P-AP-LIN-06-I11": "the substitute is the attachment's URL, which the request also asks for: a near miss must "
                       "keep it",
    "P-G4-SLK-05-I12": "the near miss is Maya's own message, so its conversation always contains her: any other "
                       "conversation type is the designated 'conversation containing the person' of D:dm_with",
}


def excluded() -> tuple[set[str], set[str], dict]:
    kd = json.loads((HERE / "known_defects.roadmap-02.json").read_text())
    cases = {e["id"] for part in ("curated", "from_the_witness_check") for e in kd[part]
             if e.get("frozen_suite", "").startswith(("leave out", "read before"))}
    near = {e["scenario"] for e in kd["near_misses"] if e.get("ruling") == "flawed"}
    clocks = {e["scenario"] for e in kd["clocks"]}
    cycle2 = set(json.loads((HERE.parent / "plain_pick.json").read_text())["excluded_scenarios"])
    scenarios = cycle2 | near | clocks | {"G4-BOX-01"}
    return scenarios, cases, {"cycle2": sorted(cycle2), "near_miss_flawed": sorted(near), "clocks": sorted(clocks),
                              "reading": ["G4-BOX-01"], "cases_left_out": sorted(cases)}


def main():
    scenarios, cases, why = excluded()
    idx = json.loads(SUITE.read_text())
    pool = [e for e in idx if e["form"] == "probe" and e.get("family") in DESIGNATED
            and e["scenario"] not in scenarios and e["case_id"] not in cases]
    rng = random.Random(SEED)
    pick, reserve, replaced = {}, {}, {}
    for domain in ("box", "calendar", "linear", "slack"):
        ids = sorted(e["case_id"] for e in pool if e["domain"] == domain)
        drawn = sorted(rng.sample(ids, PER_DOMAIN))
        rest = [c for c in ids if c not in drawn]
        random.Random(SEED + 1).shuffle(rest)
        reserve[domain] = rest
        for c in [c for c in drawn if c in REPLACED]:
            sub = next(r for r in rest if r not in REPLACED and r not in drawn and r not in replaced.values())
            drawn[drawn.index(c)] = sub
            replaced[c] = sub
        pick[domain] = sorted(drawn)
    fam = {e["case_id"]: e["family"] for e in idx}
    out = {"design": "random: F1-F8 probes of the frozen suite, not selected on exposure, 12 per service",
           "seed": SEED, "excluded": why,
           "pool_sizes": dict(Counter(e["domain"] for e in pool)),
           "pick": pick, "replaced": {c: {"by": r, "why": REPLACED[c]} for c, r in replaced.items()},
           "reserve_order": reserve,
           "families": dict(Counter(fam[c] for ids in pick.values() for c in ids)),
           "cycle2_overlap": sorted(set(c for ids in pick.values() for c in ids)
                                    & set(c for ids in json.loads((HERE.parent / "plain_pick.json").read_text())
                                          ["pick"].values() for c in ids))}
    (HERE / "pick.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps({k: out[k] for k in ("pool_sizes", "replaced", "families", "cycle2_overlap")}, indent=1))


if __name__ == "__main__":
    main()
