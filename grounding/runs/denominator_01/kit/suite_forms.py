"""The denominator as the suite stands: per brief (fact set) and per (brief, fact), which forms exist."""
import json
from collections import Counter, defaultdict
from pathlib import Path
from grounding.runs.report_01.kit.common import DOMAINS, RUNS, SUITES, catalog, fact_id, load, replica_gaps, suite_tests, valid_claims
from grounding.runs.openclaw_eval_01 import rulings

cat = catalog(); gaps = replica_gaps()
servable = {d: set(cat[d]) - set(gaps[d]) for d in DOMAINS}
def brief_of(scenario):  # AP2-X -> AP-X (same brief)
    return scenario.replace("AP2-", "AP-")
# per scenario: form counts, facts, decoys
scen = defaultdict(lambda: {"forms": Counter(), "valid_forms": Counter(), "facts": set(), "decoys": defaultdict(set), "domain": None, "source": None, "excluded_cover": None})
per_fact_forms = defaultdict(lambda: defaultdict(set))  # (domain, fact) -> form -> scenarios (valid)
single_decoy_extra = 0; single_decoy_extra_valid = 0
fact_probe_like = Counter(); probes_per_fact = defaultdict(set)
for m, case in suite_tests():
    s = scen[m["scenario"]]; s["domain"] = case["domain"]; s["source"] = m["source"]
    excluded = rulings.test_exclusion(case)
    s["forms"][m["form"]] += 1
    if not excluded: s["valid_forms"][m["form"]] += 1
    if m["form"] == "cover":
        s["excluded_cover"] = excluded or None
        for f, w, fam in valid_claims(case):
            s["facts"].add(f); s["decoys"][f].add(w)
    if not excluded:
        for f, w, fam in valid_claims(case):
            per_fact_forms[(case["domain"], f)][m["form"]].add(m["scenario"])
    if m["form"] in ("probe", "fact probe") and not excluded:
        fs = {f for f, w, fam in valid_claims(case)}
        for f in fs: probes_per_fact[(m["scenario"], f)].add((m["form"], case["case_id"]))
# briefs with a usable cover
briefs = defaultdict(list)
for sid, s in scen.items(): briefs[brief_of(sid)].append(sid)
usable = {b: [sid for sid in v if scen[sid]["excluded_cover"] is None] for b, v in briefs.items()}
print("scenarios:", len(scen), "briefs with a scenario:", len(briefs), "briefs with a usable cover:", sum(1 for v in usable.values() if v))
print("briefs with two scenarios:", sum(1 for v in briefs.values() if len(v) > 1), "excluded covers:", [(sid, s['excluded_cover']) for sid, s in scen.items() if s['excluded_cover']])
# per (scenario, fact): probe forms present
kinds = Counter()
for (sid, f), forms in probes_per_fact.items():
    nP = sum(1 for k, c in forms if k == "probe"); nFP = sum(1 for k, c in forms if k == "fact probe")
    kinds[(nFP, min(nP, 3))] += 1
print("per (scenario, fact) with a valid probe: (fact probes, single-decoy probes):", dict(sorted(kinds.items())))
pairs = len(probes_per_fact)
packed = sum(1 for forms in probes_per_fact.values() if any(k == "fact probe" for k, c in forms))
single_only = sum(1 for forms in probes_per_fact.values() if not any(k == "fact probe" for k, c in forms) and sum(1 for k, c in forms if k == "probe") == 1)
multi_single_only = sum(1 for forms in probes_per_fact.values() if not any(k == "fact probe" for k, c in forms) and sum(1 for k, c in forms if k == "probe") > 1)
extra_single = sum(sum(1 for k, c in forms if k == "probe") for forms in probes_per_fact.values() if any(k == "fact probe" for k, c in forms))
print(f"(scenario, fact) pairs with a valid probe of any kind: {pairs}; with a packed fact probe: {packed}; with exactly one single-decoy probe and no fact probe: {single_only}; with several single-decoy probes and no fact probe: {multi_single_only}; single-decoy probes beside a fact probe (the extra set): {extra_single}")
# facts in covers (valid claims) per scenario -> the prescribed per-fact slots
slots = sum(len(s["facts"]) for s in scen.values() if s["excluded_cover"] is None)
slots_dedup = len({(brief_of(sid), f) for sid, s in scen.items() if s["excluded_cover"] is None for f in s["facts"]})
print("(usable cover, fact) slots:", slots, "deduplicated by brief:", slots_dedup)
print("distinct facts with valid credit:", len({k for k, v in per_fact_forms.items() if v}))
# totals by form
tot = Counter(); totv = Counter()
for s in scen.values(): tot.update(s["forms"]); totv.update(s["valid_forms"])
print("tests by form:", dict(tot), "valid:", dict(totv))
# AP/AP2 duplicate tests
dup_tests = sum(v for sid, s in scen.items() if sid.startswith("AP2-") and brief_of(sid) in usable and len(usable[brief_of(sid)]) > 1 for v in s["valid_forms"].values())
print("valid tests in AP2 scenarios whose brief also has an AP scenario:", dup_tests)
json.dump({"scen": {sid: {"facts": sorted(s["facts"]), "domain": s["domain"], "source": s["source"], "valid_forms": dict(s["valid_forms"]), "excluded": s["excluded_cover"]} for sid, s in scen.items()}}, open("/home/yusf/.claude/jobs/4970fedb/tmp/denominator_scen.json", "w"), indent=1)
