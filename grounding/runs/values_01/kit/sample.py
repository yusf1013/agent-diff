"""Draws the hand-reading samples from the frozen check outputs, before any reading. No model calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.values_01.kit.sample

- **precision:** per check (stratum), a seeded draw of flagged executions (all of a stratum when it is small);
- **restore:** every execution whose diff has a no-net-change row, or whose transcript has an accepted write the final
  diff does not show (the brief: read each with its trajectory);
- **recall:** executions that wrote something and that no check flags, a seeded draw stratified by service.

Writes eval/sample.json (keys, strata, seed, the check outputs' hashes). An execution drawn in several strata is read
once and labelled per stratum.
"""
from __future__ import annotations

import hashlib
import json
import random

from grounding.runs.values_01.kit.common import DATA, HERE, executions, read
from grounding.runs.values_01.kit.counts import OK, family

SEED = 20260930
PLAN = {"V:priority": 6, "V:run-date": 2, "V:colour": 4, "V:reaction": 1, "V:paraphrase": 4, "S:other fields": 6,
        "S:other records": 5, "S:other tables": 5, "S:replica effect": 3, "R1": 6, "R2": 3, "R2b": 1, "R3": 8, "R4": 8}


def strata(e, v, w, r) -> set[str]:
    out = set()
    for x in v.get("values", []):
        f = family(x["field"], e["scenario"])
        if x["verdict"] == "keywords present":
            out.add("V:paraphrase")
        elif x["verdict"] not in OK:
            out.add({"Linear priority": "V:priority", "run-date dependent date": "V:run-date",
                     "Calendar colour": "V:colour", "Slack reaction": "V:reaction"}.get(f, f"V:{f}"))
    for k, name in (("other_fields", "S:other fields"), ("other_records", "S:other records"),
                    ("other_tables", "S:other tables"), ("replica_effects", "S:replica effect")):
        if v.get(k):
            out.add(name)
    for f in r.get("flags", []):
        out.add(f["check"])
    return out


def main():
    ex = executions()
    values, writes, reply = read("values"), read("writes"), read("reply")
    rng = random.Random(SEED)
    pools, clean_writers = {}, {}
    restore = []
    for e in ex:
        v, w, r = values[e["key"]], writes[e["key"]], reply[e["key"]]
        for s in strata(e, v, w, r):
            pools.setdefault(s, []).append(e["key"])
        if v.get("no_net_change") or w.get("not_in_diff"):
            restore.append(e["key"])
        if v.get("wrote") and not strata(e, v, w, r) and not v.get("no_net_change") and not w.get("not_in_diff"):
            clean_writers.setdefault(e["domain"], []).append(e["key"])
    assert set(PLAN) >= set(pools), set(pools) - set(PLAN)
    precision = {}
    for s, n in PLAN.items():
        pool = sorted(pools.get(s, []))
        precision[s] = {"pool": len(pool), "drawn": sorted(rng.sample(pool, min(n, len(pool))))}
    recall = {d: sorted(rng.sample(sorted(keys), 8 if d != "calendar" else 6)) for d, keys in sorted(clean_writers.items())}
    hashes = {n: hashlib.sha256((DATA / f"{n}.json").read_bytes()).hexdigest() for n in ("values", "writes", "reply")}
    out = {"seed": SEED, "check_outputs_sha256": hashes, "precision": precision, "restore": sorted(restore),
           "recall": {"pool": {d: len(k) for d, k in clean_writers.items()}, "drawn": recall}}
    (HERE / "eval").mkdir(exist_ok=True)
    (HERE / "eval/sample.json").write_text(json.dumps(out, indent=1) + "\n")
    keys = {k for s in precision.values() for k in s["drawn"]} | set(restore) | {k for ks in recall.values() for k in ks}
    print({s: (p["pool"], len(p["drawn"])) for s, p in precision.items()})
    print("restore", len(restore), "recall", {d: len(k) for d, k in recall.items()}, "distinct executions to read", len(keys))


if __name__ == "__main__":
    main()
