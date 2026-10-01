"""How the 732-case denominator is filled by the generation attempts on record, under alternative one-attempt rules.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.denominator_01.kit.filling

Items: the 213 servable facts, each prescribing one packed probe, one absence test and one underspecified test, and
the 93 faithful boundary elements. For each generation attempt of each brief, which items it fills with a test
that is valid under the rulings as they stand (invalid whenever discovered).
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

import grounding.runs.regen_01.rules  # noqa: F401  (teaches the rulings the regenerated scenarios' ids)
from grounding.runs.openclaw_eval_01 import policy, rulings
from grounding.runs.report_01.kit.common import DOMAINS, RUNS, catalog, fact_id, load, replica_gaps

OUT = Path(__file__).resolve().parents[1] / "numbers"


def base_fact(d: str, f: str) -> str:
    f = fact_id(d, f)
    return f if ":" not in f.split(":", 2)[-1] else ":".join(f.split(":")[:2])


def main() -> None:
    cat = catalog()
    gaps = replica_gaps()
    servable = {d: sorted(set(cat[d]) - set(gaps[d])) for d in DOMAINS}
    all_servable = {(d, f) for d in DOMAINS for f in servable[d]}

    # ---- briefs and attempts -------------------------------------------------------------------------------
    # attempt key -> (brief id, writer, order of the attempt for that brief)
    brief_of = {}      # scenario id -> brief id
    attempt_of = {}    # scenario id -> attempt label
    for b in load(RUNS / "autogen_01/inputs/briefs_arm_r.json"):
        brief_of[b["scenario_id"]] = b["scenario_id"]; attempt_of[b["scenario_id"]] = "sonnet_r"
    for b in load(RUNS / "autogen_01/inputs/briefs_arm_p.json"):
        brief_of[b["scenario_id"]] = b["scenario_id"]; attempt_of[b["scenario_id"]] = "sonnet_p1"
        v2 = b["scenario_id"].replace("AP-", "AP2-")
        brief_of[v2] = b["scenario_id"]; attempt_of[v2] = "sonnet_p2"
    phase4_orders = {b["scenario_id"]: b["order"] for b in load(RUNS / "autogen_02/inputs/briefs_phase4.json")}
    for sid, order in phase4_orders.items():
        brief_of[sid] = sid
        attempt_of[sid] = "muse_phase4" if order <= 32 else "muse_6b"
    retried_in_6b = set()
    for b in load(RUNS / "completion_01/inputs/briefs_6b.json"):
        brief_of[b["scenario_id"]] = b["scenario_id"]
        if "generated again" in b["source"]:
            retried_in_6b.add(b["scenario_id"])          # second attempt of a Phase 4 brief
        else:
            attempt_of.setdefault(b["scenario_id"], "muse_6b")
    regen_second_draw = {"G4-SLK-18", "G4-LIN-30"}       # gen_04 (the lead's yes): a second attempt
    regen_brief = {}
    for b in load(RUNS / "regen_01/inputs/briefs_regen.json"):
        sid = b["scenario_id"]
        src = (b.get("sonnet") or [None])[0]
        regen_brief[sid] = (src or sid).replace("AP2-", "AP-")
        brief_of[sid] = regen_brief[sid]
        attempt_of[sid] = "muse_regen"
    brief_facts = defaultdict(set)
    for p in ("autogen_01/inputs/briefs_arm_r.json", "autogen_01/inputs/briefs_arm_p.json",
              "autogen_02/inputs/briefs_phase4.json", "completion_01/inputs/briefs_6b.json",
              "regen_01/inputs/briefs_regen.json"):
        for b in load(RUNS / p):
            bid = brief_of[b["scenario_id"]]
            for f in b["facts"]:
                brief_facts[bid].add((b["domain"], base_fact(b["domain"], f)))
    print(f"briefs: {len(brief_facts)}; facts in briefs: {len(set().union(*brief_facts.values()))}")

    # ---- the tests on record, per scenario -----------------------------------------------------------------
    # (scenario, fact) -> {"packed": bool, "single": n, "cover": bool}; scenario -> run source
    SUITES = [(RUNS / "openclaw_eval_01/suite/suite.json", RUNS / "openclaw_eval_01/suite/cases"),
              (RUNS / "completion_01/suite/cases/suite.json", RUNS / "completion_01/suite/cases"),
              (RUNS / "regen_01/runs/full_01_cases/suite.json", RUNS / "regen_01/runs/full_01_cases")]
    decoys = defaultdict(set)         # (scenario, fact) -> valid witnesses declared in the cover
    forms = defaultdict(Counter)      # (scenario, fact) -> form -> valid tests
    scenarios = {}                    # scenario -> {"domain", "usable"(cover valid), "excluded"}
    tests_total = Counter(); tests_valid = Counter()
    for index, folder in SUITES:
        doc = load(index)
        rows = doc["tests"] if isinstance(doc, dict) else doc
        for m in rows:
            if isinstance(m, str):      # regen's cut index lists ids; its suite index has the forms
                continue
            case = load(folder / m["domain"] / f"{m['case_id']}.json")
            d = case["domain"]; sid = m["scenario"]
            excluded = rulings.test_exclusion(case)
            tests_total[(attempt_of.get(sid, "?"), m["form"])] += 1
            if not excluded:
                tests_valid[(attempt_of.get(sid, "?"), m["form"])] += 1
            bad = rulings.flawed(rulings.scenario_of(case["case_id"]))
            claims = [(base_fact(d, c["requirement"]), str(c["witness"]))
                      for ref in case["references"] for c in ref.get("claims", [])]
            if m["form"] == "cover":
                scenarios[sid] = {"domain": d, "usable": excluded is None, "excluded": excluded}
                for f, w in claims:
                    if w not in bad:
                        decoys[(sid, f)].add(w)
                continue
            if excluded:
                continue
            facts_here = {f for f, w in claims if w not in bad}
            for f in facts_here:
                forms[(sid, f)][m["form"]] += 1
    print(f"scenarios with a cover on record: {len(scenarios)}; usable: {sum(s['usable'] for s in scenarios.values())}")

    def packed(sid, f):
        c = forms.get((sid, f), {})
        if c.get("fact probe", 0):
            return True
        return len(decoys.get((sid, f), ())) == 1 and c.get("probe", 0) >= 1

    # ---- the policy units on record ------------------------------------------------------------------------
    units = []   # {"unit", "mode", "domain", "scenario", "facts", "valid"}
    seen = set()
    for mode in ("absence", "underspecified"):
        for cell, seq in load(RUNS / f"autogen_02/runs/phase3/plan_{mode}.json")["cells"].items():
            for u in seq:
                units.append({**u, "mode": mode, "_case": policy.unit_case(u)})
        ext = load(RUNS / "openclaw_eval_01/runs/policy/plan_extension.json")
        for cell, seq in ext["cells"].items():
            if cell.endswith("/" + mode):
                for u in seq:
                    units.append({**u, "mode": mode, "_case": policy.unit_case(u)})
    for u in load(RUNS / "regen_01/suite/units.json")["units"] if isinstance(load(RUNS / "regen_01/suite/units.json"), dict) and "units" in load(RUNS / "regen_01/suite/units.json") else []:
        pass
    regen_units_doc = load(RUNS / "regen_01/suite/units.json")
    regen_rows = regen_units_doc["units"] if isinstance(regen_units_doc, dict) and "units" in regen_units_doc else (
        regen_units_doc if isinstance(regen_units_doc, list) else list(regen_units_doc.values())[0])
    for u in regen_rows:
        path = RUNS / "regen_01/suite/units" / u["domain"] / f"{u['unit']}.json"
        if not path.exists():
            continue
        units.append({**u, "_case": load(path)})
    for u in units:
        if u["unit"] in seen:
            u["valid"] = False; u["why"] = "listed twice"; continue
        seen.add(u["unit"])
        canon = rulings.DUPLICATE_UNITS.get(u["unit"])
        why = rulings.test_exclusion(u["_case"])
        u["valid"] = why is None and canon is None
        u["why"] = why or ("duplicate" if canon else None)
        u["facts"] = [base_fact(u["domain"], f) for f in u["facts"]]
    print("units on record:", Counter((attempt_of.get(u['scenario'], '?'), u['mode']) for u in units),
          "valid:", Counter((attempt_of.get(u['scenario'], '?'), u['mode']) for u in units if u['valid']))

    # ---- the rules: which attempt of each brief is the designated one ----------------------------------------
    def designated(rule: str) -> dict[str, str | None]:
        """brief id -> the scenario id whose tests count under the rule (None: no usable scenario)."""
        cands = defaultdict(list)
        for sid, bid in brief_of.items():
            if sid in scenarios or sid in retried_in_6b or sid in regen_second_draw or attempt_of.get(sid) == "muse_regen":
                cands[bid].append(sid)
        out = {}
        for bid, sids in cands.items():
            order = []
            for sid in sids:
                a = attempt_of.get(sid)
                retry = sid in retried_in_6b or sid in regen_second_draw
                if rule.startswith("first"):
                    rank = {"sonnet_r": 0, "sonnet_p1": 0, "muse_phase4": 0, "muse_6b": 0, "sonnet_p2": 1, "muse_regen": 2}[a]
                    if a == "muse_regen" and not any(attempt_of.get(x, "").startswith("sonnet") for x in sids):
                        rank = 0        # a brief new in the regeneration (G4-LIN-35): its first attempt
                else:   # final pipeline: Muse through the frozen generator; Sonnet attempts are the comparison
                    if a.startswith("sonnet"):
                        continue
                    rank = 0
                if sid in retried_in_6b:
                    rank = 1            # the 6b regeneration of a Phase 4 brief is that brief's second attempt
                if sid in regen_second_draw and a == "muse_regen":
                    pass                # G4-SLK-18's and G4-LIN-30's first draws failed; the second is in gen_04
                order.append((rank, sid, retry))
            order.sort()
            if not order:
                out[bid] = None; continue
            first = [o for o in order if o[0] == 0]
            if first and scenarios.get(first[0][1], {}).get("usable"):
                out[bid] = first[0][1]
            elif rule.endswith("+retry"):
                retries = [o for o in order if o[0] == 1 or (o[1] in regen_second_draw)]
                ok = [o for o in retries if scenarios.get(o[1], {}).get("usable")]
                out[bid] = ok[0][1] if ok else None
            else:
                out[bid] = None
        return out

    # G4-SLK-18's only usable scenario is its second draw: under a no-retry rule it counts as a failed brief.
    def fill(rule: str):
        des = designated(rule)
        chosen = {sid for sid in des.values() if sid}
        if not rule.endswith("+retry"):
            chosen -= regen_second_draw
        have = {"probe": set(), "absence": set(), "underspecified": set(), "cover": set()}
        prod = Counter()
        for sid in chosen:
            d = scenarios[sid]["domain"]
            prod["covers"] += 1
            for (s, f), c in forms.items():
                if s != sid:
                    continue
                if (d, f) in all_servable:
                    have["cover"].add((d, f))
                    if packed(sid, f):
                        have["probe"].add((d, f))
                prod["packed probes"] += 1 if packed(sid, f) else 0
                prod["single-decoy probes beside a packed one"] += c.get("probe", 0) if c.get("fact probe", 0) else 0
                prod["probes without a packed form"] += 0 if packed(sid, f) else c.get("probe", 0)
            for u in units:
                if u["scenario"] == sid and u["valid"]:
                    prod[f"{u['mode']} units"] += 1
                    for f in u["facts"]:
                        if (d, f) in all_servable:
                            have[u["mode"]].add((d, f))
        per_domain = {d: {k: sum(1 for (dd, f) in v if dd == d) for k, v in have.items()} for d in DOMAINS}
        briefs_failed = sorted(b for b, s in des.items() if s is None)
        # One test per item (the PI's rule): the test from the scenario of the fact's own brief; failing that, the
        # earliest-generated other scenario (Phase 4, then 6b, then the regeneration; then by id). Outcome-blind.
        RANK = {"sonnet_r": 0, "sonnet_p1": 0, "sonnet_p2": 1, "muse_phase4": 2, "muse_6b": 3, "muse_regen": 4}
        designated_tests = {}; spares = Counter(); shared = Counter()
        hist = defaultdict(Counter); examples = defaultdict(list)
        for form in ("probe", "absence", "underspecified"):
            for (d, f) in sorted(have[form]):
                cands = []
                if form == "probe":
                    for (s, fx), c in forms.items():
                        if fx == f and s in chosen and scenarios[s]["domain"] == d and packed(s, fx):
                            cands.append(s)
                else:
                    for u in units:
                        if u["valid"] and u["mode"] == form and u["scenario"] in chosen and u["domain"] == d and f in u["facts"]:
                            cands.append(u["unit"])
                            if len(u["facts"]) > 1:
                                shared[form] += 1
                def key(x):
                    s = x if form == "probe" else next(u["scenario"] for u in units if u["unit"] == x)
                    own = 0 if (d, f) in brief_facts.get(brief_of.get(s, s), set()) else 1
                    return (own, RANK.get(attempt_of.get(s, ""), 9), s, x)
                cands = sorted(set(cands), key=key)
                designated_tests[f"{form} {d} {f}"] = cands[0]
                spares[form] += len(cands) - 1
                hist[form][len(cands)] += 1
                if len(cands) > 1 and len(examples[form]) < 3:
                    examples[form].append((d, f, cands))
        return {"rule": rule, "scenarios": len(chosen), "briefs_without_a_usable_scenario": briefs_failed,
                "filled": {k: len(v) for k, v in have.items()}, "per_domain": per_domain, "production": dict(prod),
                "spare_tests_beyond_one_per_item": dict(spares),
                "units_carrying_two_items": dict(shared),
                "candidates_per_item": {k: dict(v) for k, v in hist.items()}, "examples": dict(examples),
                "designated_tests": designated_tests,
                "unfilled": {k: sorted(f"{d} {f}" for (d, f) in all_servable - v) for k, v in have.items() if k != "cover"}}

    results = {}
    for rule in ("first", "first+retry", "final", "final+retry"):
        r = fill(rule); results[rule] = r
        print(f"\n== {rule}: {r['scenarios']} scenarios; briefs without a usable scenario: {len(r['briefs_without_a_usable_scenario'])} {r['briefs_without_a_usable_scenario']}")
        print("   filled of 213:", r["filled"], "| production:", r["production"])
        print("   per domain:", {d: v for d, v in r["per_domain"].items()})
        print("   spares beyond one per item:", r["spare_tests_beyond_one_per_item"], "| units carrying two items:", r["units_carrying_two_items"])
    # the union of everything on record, for reference
    have_all = {"probe": set(), "absence": set(), "underspecified": set()}
    for (sid, f) in forms:
        d = scenarios.get(sid, {}).get("domain")
        if d and scenarios[sid]["usable"] and (d, f) in all_servable and packed(sid, f):
            have_all["probe"].add((d, f))
    for u in units:
        if u["valid"] and scenarios.get(u["scenario"], {}).get("usable"):
            for f in u["facts"]:
                if (u["domain"], f) in all_servable:
                    have_all[u["mode"]].add((u["domain"], f))
    print("\n== union of every attempt on record: filled of 213:", {k: len(v) for k, v in have_all.items()})
    results["union"] = {k: len(v) for k, v in have_all.items()}
    (OUT / "filling.json").write_text(json.dumps(results, indent=1) + "\n")


if __name__ == "__main__":
    main()
