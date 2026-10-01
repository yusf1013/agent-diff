"""What the Phase-4 grouping rule gives when applied to all 213 servable facts, and the per-brief dedup of the forms."""
import json
from collections import Counter, defaultdict
from pathlib import Path
from grounding.runs.report_01.kit.common import DOMAINS, RUNS, catalog, replica_gaps, load
cat = catalog(); gaps = replica_gaps()
def entity(fid): return fid.split(":", 1)[1].split(".")[0]
total = 0; per = {}
for d in DOMAINS:
    facts = [f for f in cat[d] if f not in set(gaps[d])]  # catalog order
    groups = defaultdict(list)
    for f in facts: groups[entity(f)].append(f)
    n = 0
    for e, fs in groups.items():
        k, r = divmod(len(fs), 3)
        n += k + (1 if r == 2 else 0)
        if r == 1 and k == 0: n += 1  # a lone fact in an entity is its own brief
    per[d] = (len(facts), len(groups), n); total += n
print("rule applied to all servable facts: (facts, entities, briefs) per domain:", per, "total briefs:", total)
# the briefs as made
files = {"dev": "autogen_01/inputs/briefs_dev.json", "arm_r": "autogen_01/inputs/briefs_arm_r.json", "arm_p": "autogen_01/inputs/briefs_arm_p.json", "phase4": "autogen_02/inputs/briefs_phase4.json"}
by_dom = Counter(); sizes = Counter()
for name, p in files.items():
    for b in load(RUNS / p):
        by_dom[(b["domain"], name)] += 1; sizes[len(b["facts"])] += 1
print("briefs as made by domain and source:", dict(sorted(by_dom.items())), "sizes:", dict(sorted(sizes.items())))
# policy units deduplicated by brief
units = []
for mode in ("absence", "underspecified"):
    p = load(RUNS / f"autogen_02/runs/phase3/plan_{mode}.json")
    for cell, seq in p["cells"].items():
        for u in seq: units.append({**u, "mode": mode})
ext = load(RUNS / "openclaw_eval_01/runs/policy/plan_extension.json")
for cell, seq in ext["cells"].items():
    for u in seq: units.append({**u, "mode": cell.split("/")[1]})
from grounding.runs.openclaw_eval_01 import policy, rulings
for mode in ("absence", "underspecified"):
    us = [u for u in units if u["mode"] == mode]
    valid = [u for u in us if not rulings.test_exclusion(policy.unit_case(u))]
    pairs = {(u["scenario"].replace("AP2-", "AP-"), tuple(u["facts"])) for u in valid}
    facts = {(u["domain"], f) for u in valid for f in u["facts"]}
    print(f"{mode}: units {len(us)}, valid {len(valid)}, distinct (brief, fact set) {len(pairs)}, distinct facts {len(facts)}")
