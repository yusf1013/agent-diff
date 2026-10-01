"""The adopted set (the Muse pipeline's attempt per brief, one retry after a failed attempt, one test per item; the
PI, 2026-10-01: Muse is the writer) against the runs on record: what each agent's verdicts give on the designated
tests alone, against every Muse-written test and against everything on record. No model calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.denominator_01.kit.outcomes

Reads numbers/filling.json (kit/filling.py) for the designated units and the chosen scenarios, the suite indexes for
the designated probes, the adjudicated score files for each test's exposed facts under the rulings (Qwen:
openclaw_eval_01's full_03 and full_04, regen_01's full_01; Sol: sol_eval_01's score files), the verdict folders for
per-trial outcomes with the budget rule (`policy.population_outcomes`), and the run folders for attempts per trial.
Writes numbers/outcomes.json.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

import grounding.runs.regen_01.rules  # noqa: F401
from grounding.runs.autogen_02.kit import sampler
from grounding.runs.openclaw_eval_01 import policy, rulings
from grounding.runs.report_01.kit.common import DOMAINS, RUNS, catalog, fact_id, load

CATALOG = catalog()
from grounding.runs.sol_eval_01.kit import policy as solpolicy

HERE = Path(__file__).resolve().parents[1]
RULE = "final+retry"

SUITES = [(RUNS / "openclaw_eval_01/suite/suite.json", RUNS / "openclaw_eval_01/suite/cases"),
          (RUNS / "completion_01/suite/cases/suite.json", RUNS / "completion_01/suite/cases"),
          (RUNS / "regen_01/runs/full_01_cases/suite.json", RUNS / "regen_01/runs/full_01_cases")]
# per-test scores with the rulings applied: case_id -> record with exposed / exposed_t1
# the adjudicated per-test lists (rulings and budget applied; the first round's Box tests come from full_02)
QWEN_SCORES = [RUNS / "openclaw_eval_01/runs/final_regular_with_6b.json", RUNS / "regen_01/runs/full_01.adjudicated.json"]
SOL_SCORES = [RUNS / "sol_eval_01/eval/final_regular.json", RUNS / "sol_eval_01/eval/final_regular_regen.json"]
QWEN_REGULAR_VERDICTS = [RUNS / "openclaw_eval_01/runs/judged_full_03", RUNS / "openclaw_eval_01/runs/judged_full_04",
                         RUNS / "regen_01/runs/judged_full_01"]
SOL_REGULAR_VERDICTS = [RUNS / "sol_eval_01/eval/judged_regular_p4", RUNS / "sol_eval_01/eval/judged_regular_6b",
                        RUNS / "sol_eval_01/eval/judged_regen_full_01"]
QWEN_REGEN_POLICY = {"absence": RUNS / "regen_01/runs/judged_absence_01", "underspecified": RUNS / "regen_01/runs/judged_underspecified_01"}
SOL_POLICY = {"absence": [RUNS / "sol_eval_01/eval/judged_policy_absence", RUNS / "sol_eval_01/eval/judged_regen_absence_01"],
              "underspecified": [RUNS / "sol_eval_01/eval/judged_policy_underspecified", RUNS / "sol_eval_01/eval/judged_regen_underspecified_01"]}
QWEN_RUNS = [RUNS / "openclaw_eval_01/runs/full_03", RUNS / "openclaw_eval_01/runs/full_04", RUNS / "regen_01/runs/full_01",
             RUNS / "openclaw_eval_01/runs/policy/solve_population_absence", RUNS / "openclaw_eval_01/runs/policy/solve_population_6b_absence",
             RUNS / "openclaw_eval_01/runs/policy/solve_population_underspecified", RUNS / "openclaw_eval_01/runs/policy/solve_population_6b_underspecified",
             RUNS / "regen_01/runs/absence_01", RUNS / "regen_01/runs/underspecified_01",
             *sorted((RUNS / "openclaw_eval_01/runs/policy").glob("solve_*_look*"))]
SOL_RUNS = [RUNS / "sol_eval_01/runs" / r for r in ("regular_p4", "regular_6b", "policy_absence", "policy_underspecified",
                                                   "regen_full_01", "regen_absence_01", "regen_underspecified_01")]


def base_fact(d, f):
    f = fact_id(d, f)
    if f in CATALOG[d]:
        return f
    parts = f.split(":")
    return ":".join(parts[:2]) if len(parts) > 2 else f


def suite_rows():
    for index, folder in SUITES:
        doc = load(index)
        for m in (doc["tests"] if isinstance(doc, dict) else doc):
            if isinstance(m, str):
                continue
            yield m, folder


def scores(paths):
    """case -> adjudicated record; and the voided / over-budget trials per case."""
    out, voided = {}, defaultdict(list)
    for p in paths:
        doc = load(p)
        for t in doc["tests"]:
            out[t["case_id"]] = t
        for x in doc.get("trials_not_counted", []):
            voided[x["trial"].split("/", 1)[1]].append(x["why"])
        for x in doc.get("trials_over_budget", []):
            trial = x["trial"] if isinstance(x, str) else x.get("trial", "")
            voided[trial.split("/", 1)[1]].append("over budget")
    return out, voided


def first_attempt_reason(run_dirs, case_id, trial):
    for run in run_dirs:
        s = run / trial / case_id / "attempt-01" / "execution_summary.json"
        if s.exists():
            d = load(s)
            return f"{d.get('status')}/{d.get('termination')}: {str(d.get('error') or '')[:60]}"
    return "?"


def attempts_per_trial(run_dirs, case_ids):
    """case -> {trial: number of attempt folders}, over the run folders that hold the case."""
    out = defaultdict(dict)
    for run in run_dirs:
        if not run.exists():
            continue
        for trial_dir in sorted(run.glob("t*")):
            for case_dir in trial_dir.iterdir():
                if case_dir.name in case_ids:
                    n = len(list(case_dir.glob("attempt-*")))
                    out[case_dir.name][trial_dir.name] = max(n, out[case_dir.name].get(trial_dir.name, 0))
    return out


def main():
    filling = load(HERE / "numbers/filling.json")[RULE]
    designated = filling["designated_tests"]            # "form domain fact" -> scenario (probe) or unit id
    chosen_scenarios = set()
    for key, value in designated.items():
        if key.startswith("probe "):
            chosen_scenarios.add(value)
    # every Muse-written scenario on record (G4-*): the chosen ones and their spares
    muse_scenarios = set()

    # ---- the designated probes: resolve (scenario, fact) to one test -------------------------------------------
    rows_by_scenario = defaultdict(list)
    valid_all, valid_muse = set(), set()
    test_meta = {}
    for m, folder in suite_rows():
        case = load(folder / m["domain"] / f"{m['case_id']}.json")
        if rulings.test_exclusion(case):
            continue
        bad = rulings.flawed(rulings.scenario_of(case["case_id"]))
        facts = {base_fact(case["domain"], c["requirement"]) for ref in case["references"] for c in ref.get("claims", [])
                 if str(c["witness"]) not in bad}
        decoys_valid = {base_fact(case["domain"], c["requirement"]): set() for ref in case["references"] for c in ref.get("claims", [])}
        for ref in case["references"]:
            for c in ref.get("claims", []):
                if str(c["witness"]) not in bad:
                    decoys_valid[base_fact(case["domain"], c["requirement"])].add(str(c["witness"]))
        test_meta[m["case_id"]] = {"domain": m["domain"], "form": m["form"], "scenario": m["scenario"], "facts": facts,
                                   "decoys_valid": decoys_valid}
        rows_by_scenario[m["scenario"]].append(m["case_id"])
        valid_all.add(m["case_id"])
        if m["scenario"].startswith("G4-"):
            valid_muse.add(m["case_id"]); muse_scenarios.add(m["scenario"])
    cover_decoys = {}   # (scenario, fact) -> valid decoys declared in the cover
    for cid, meta in test_meta.items():
        if meta["form"] == "cover":
            for f, ws in meta["decoys_valid"].items():
                cover_decoys[(meta["scenario"], f)] = ws
    designated_probe = {}   # "probe domain fact" -> case id
    for key, sid in designated.items():
        if not key.startswith("probe "):
            continue
        _, d, f = key.split(" ", 2)
        cands = [cid for cid in rows_by_scenario[sid] if test_meta[cid]["form"] in ("probe", "fact probe") and f in test_meta[cid]["facts"]]
        fp = [c for c in cands if test_meta[c]["form"] == "fact probe"]
        if fp:
            designated_probe[key] = fp[0]
        elif len(cover_decoys.get((sid, f), ())) == 1 and cands:
            designated_probe[key] = cands[0]
        else:
            designated_probe[key] = None
    missing = [k for k, v in designated_probe.items() if v is None]
    print(f"designated probes resolved: {sum(1 for v in designated_probe.values() if v)} of {len(designated_probe)}; unresolved: {missing}")
    designated_probe_ids = {v for v in designated_probe.values() if v}
    des_units = {"absence": {}, "underspecified": {}}
    for key, uid in designated.items():
        form, d, f = key.split(" ", 2)
        if form in des_units:
            des_units[form][(d, f)] = uid

    # ---- regular exposure per agent ----------------------------------------------------------------------------
    result = {"rule": RULE, "designated_probes": len(designated_probe_ids), "agents": {}}
    for agent, score_paths, verdict_dirs, run_dirs in (("qwen", QWEN_SCORES, QWEN_REGULAR_VERDICTS, QWEN_RUNS),
                                                       ("sol", SOL_SCORES, SOL_REGULAR_VERDICTS, SOL_RUNS)):
        sc, voided = scores(score_paths)
        per_trial = policy.population_outcomes([d for d in verdict_dirs if d.exists()])
        if agent == "sol":   # a provider stall caught after the fact is void, as sol_eval_01 scores it
            per_trial = solpolicy.outcomes_of([d for d in verdict_dirs if d.exists()])
        def exposure(test_ids):
            f3, f1, exposing = set(), set(), 0
            ran = 0
            for cid in test_ids:
                t = sc.get(cid)
                if not t:
                    continue
                ran += 1
                d = test_meta[cid]["domain"]
                e3 = {base_fact(d, x) for x in t.get("exposed", [])}
                e1 = {base_fact(d, x) for x in t.get("exposed_t1", [])}
                f3 |= {(d, x) for x in e3}; f1 |= {(d, x) for x in e1}
                exposing += 1 if e3 else 0
            return {"tests": len(test_ids), "ran": ran, "tests_exposing": exposing, "facts_detect3": len(f3), "facts_detect1": len(f1),
                    "_f3": f3, "_f1": f1}
        # the item's own fact, through its designated probe
        item_hits3, item_hits1 = set(), set()
        trials_usable = Counter(); trials_total = Counter(); ran_items = 0
        for key, cid in designated_probe.items():
            if not cid or cid not in sc:
                continue
            _, d, f = key.split(" ", 2); ran_items += 1
            t = sc[cid]
            if f in {base_fact(d, x) for x in t.get("exposed", [])}:
                item_hits3.add((d, f))
            if f in {base_fact(d, x) for x in t.get("exposed_t1", [])}:
                item_hits1.add((d, f))
            outs = per_trial.get(cid, {})
            trials_total[len(outs)] += 1
            trials_usable[sum(1 for o in outs.values() if o in sampler.FAIL | sampler.PASS)] += 1
        des = exposure(designated_probe_ids)
        muse = exposure(valid_muse)
        everything = exposure(valid_all)
        # the tracked denominators: the chosen scenarios' covers, the designated packed probes, and per fact its
        # single-decoy probes in claim order up to the catalog's prescribed number (outcome-blind)
        from grounding.runs.denominator_01.kit.single_decoy import prescribed as _prescribed
        tracked_ids = set(designated_probe_ids)
        for cid, meta in test_meta.items():
            if meta["form"] == "cover" and meta["scenario"] in chosen_scenarios:
                tracked_ids.add(cid)
        for key, sid in designated.items():
            if not key.startswith("probe "):
                continue
            _, d, f = key.split(" ", 2)
            singles = sorted(cid for cid in rows_by_scenario[sid] if test_meta[cid]["form"] == "probe" and f in test_meta[cid]["facts"])
            tracked_ids.update(singles[:_prescribed(d, f)])
        tracked = exposure(tracked_ids)
        lost = sorted(f"{d} {f}" for (d, f) in everything["_f3"] - des["_f3"])
        # why each lost fact is lost: exposed only by Sonnet tests / only by covers / only by spare probes
        why = {}
        des_scenario = {k.split(" ", 2)[2]: v for k, v in designated.items() if k.startswith("probe ")}
        for (d, f) in everything["_f3"] - des["_f3"]:
            forms = Counter()
            for cid in valid_all:
                t = sc.get(cid)
                if not t or f not in {base_fact(d, x) for x in t.get("exposed", [])} or test_meta[cid]["domain"] != d:
                    continue
                meta = test_meta[cid]
                if not meta["scenario"].startswith("G4-"):
                    src = "a Sonnet-written test"
                elif meta["form"] == "cover":
                    src = "a cover"
                elif meta["scenario"] == des_scenario.get(f) and meta["form"] == "probe":
                    src = "a single-decoy probe beside the packed one"
                elif meta["scenario"] != des_scenario.get(f):
                    src = "another Muse scenario's test (a tie-break spare)"
                else:
                    src = f"a {meta['form']} of the designated scenario naming this fact among others"
                forms[src] += 1
            why[f"{d} {f}"] = dict(forms)
        lost_by_kind = Counter()
        for k, forms in why.items():
            kinds = set(forms)
            lost_by_kind["only " + next(iter(kinds)) if len(kinds) == 1 else "several kinds"] += 1
        att = attempts_per_trial(run_dirs, designated_probe_ids | set(des_units["absence"].values()) | set(des_units["underspecified"].values()))
        replaced = {cid: {tr: f"{n} attempts; first: {first_attempt_reason(run_dirs, cid, tr)}" for tr, n in v.items() if n > 1}
                    for cid, v in att.items() if any(n > 1 for n in v.values())}
        replaced_reasons = Counter(s.split("; first: ")[1].split(":")[0] for v in replaced.values() for s in v.values())
        void_trials = {cid: voided[cid] for cid in designated_probe_ids | set(des_units["absence"].values()) | set(des_units["underspecified"].values()) if cid in voided}
        trials_seen = Counter(len(v) for v in att.values())
        result["agents"][agent] = {
            "designated_items_ran": ran_items,
            "items_exposed_detect3": len(item_hits3), "items_exposed_detect1": len(item_hits1),
            "designated_probes": {k: v for k, v in des.items() if not k.startswith("_")},
            "tracked_denominators_set": {k: v for k, v in tracked.items() if not k.startswith("_")},
            "facts_lost_from_all_muse_to_tracked": sorted(f"{d} {f}" for (d, f) in muse["_f3"] - tracked["_f3"]),
            "facts_lost_from_tracked_to_designated": sorted(f"{d} {f}" for (d, f) in tracked["_f3"] - des["_f3"]),
            "all_muse_tests": {k: v for k, v in muse.items() if not k.startswith("_")},
            "everything_on_record": {k: v for k, v in everything.items() if not k.startswith("_")},
            "facts_lost_from_everything_to_designated": lost, "why_lost": why, "lost_by_kind": dict(lost_by_kind),
            "facts_lost_from_all_muse_to_designated": sorted(f"{d} {f}" for (d, f) in muse["_f3"] - des["_f3"]),
            "designated_probe_trials_judged": dict(trials_total), "designated_probe_usable_trials": dict(trials_usable),
            "designated_tests_with_a_replaced_attempt": len(replaced), "replaced_attempts": replaced,
            "replaced_first_attempt_statuses": dict(replaced_reasons),
            "designated_tests_with_a_voided_trial": len(void_trials), "voided_trials": void_trials,
            "voided_trial_reasons": dict(Counter(r.split(" [")[0][:60] for v in void_trials.values() for r in v)),
            "trials_per_designated_test_on_disk": dict(trials_seen),
        }

    # ---- policy cells on the designated units, per agent ---------------------------------------------------------
    unit_meta = {}
    for mode in ("absence", "underspecified"):
        for cell, seq in policy.population_plan(mode)["cells"].items():
            for u in seq:
                unit_meta[u["unit"]] = {**u, "mode": mode, "cell": cell}
        for u in load(RUNS / "regen_01/suite/units.json")["units"]:
            if u["mode"] == mode:
                unit_meta[u["unit"]] = {**u, "cell": f"{u['domain']}/{mode}"}
    policy_result = {}
    for agent in ("qwen", "sol"):
        policy_result[agent] = {}
        for mode in ("absence", "underspecified"):
            if agent == "qwen":
                outcomes = solpolicy.qwen_outcomes(mode)
                outcomes.update(policy.population_outcomes([QWEN_REGEN_POLICY[mode]]))
            else:
                outcomes = solpolicy.outcomes_of([d for d in SOL_POLICY[mode] if d.exists()])
            by_cell_des = defaultdict(list); by_cell_all = defaultdict(list)
            des_ids = set(des_units[mode].values())
            for uid in des_ids:
                m = unit_meta.get(uid)
                if not m:
                    continue
                by_cell_des[m["cell"]].append({"unit": uid})
            # every valid Muse unit (chosen scenarios' units, spares included): the current "whole suite" reading
            for uid, m in unit_meta.items():
                if m["mode"] == mode and m["scenario"].startswith("G4-") and m["scenario"] in (chosen_scenarios | muse_scenarios):
                    if rulings.test_exclusion(_regen_or_first(m)) is None and uid not in rulings.DUPLICATE_UNITS:
                        by_cell_all[m["cell"]].append({"unit": uid})
            for cell in sorted(set(by_cell_des) | set(by_cell_all)):
                pu_des = solpolicy.per_unit(by_cell_des.get(cell, []), outcomes)
                pu_all = solpolicy.per_unit(by_cell_all.get(cell, []), outcomes)
                policy_result[agent][cell] = {
                    "designated": {"units": len(by_cell_des.get(cell, [])), **{k: v for k, v in policy.pooled_decision(pu_des).items() if k != "units"}, "units_with_a_usable_trial": len(pu_des)},
                    "all_valid_muse_units": {"units": len(by_cell_all.get(cell, [])), **{k: v for k, v in policy.pooled_decision(pu_all).items() if k != "units"}, "units_with_a_usable_trial": len(pu_all)}}
    result["policy"] = policy_result
    (HERE / "numbers/outcomes.json").write_text(json.dumps(result, indent=1, default=sorted) + "\n")
    for agent, r in result["agents"].items():
        print(f"\n== {agent}: designated probes ran {r['designated_items_ran']}; items exposed @3 {r['items_exposed_detect3']}, @1 {r['items_exposed_detect1']}")
        print("   designated:", r["designated_probes"]); print("   tracked set (covers + packed + capped singles):", r["tracked_denominators_set"]); print("   all Muse tests:", r["all_muse_tests"]); print("   everything:", r["everything_on_record"])
        print("   lost all-Muse -> tracked:", r["facts_lost_from_all_muse_to_tracked"])
        print("   lost (everything -> designated):", len(r["facts_lost_from_everything_to_designated"]), r["lost_by_kind"])
        print("   replaced first-attempt statuses:", r["replaced_first_attempt_statuses"], "| voided trials in designated tests:", r["designated_tests_with_a_voided_trial"], r["voided_trial_reasons"])
        print("   lost (all Muse -> designated):", r["facts_lost_from_all_muse_to_designated"])
        print("   trials judged per designated probe:", r["designated_probe_trials_judged"], "usable:", r["designated_probe_usable_trials"])
        print("   designated tests with a replaced attempt:", r["designated_tests_with_a_replaced_attempt"], "trials on disk:", r["trials_per_designated_test_on_disk"])
    for agent, cells in policy_result.items():
        print(f"\n== {agent} policy cells (designated | all valid Muse units):")
        for cell, v in cells.items():
            a, b = v["designated"], v["all_valid_muse_units"]
            print(f"   {cell}: {a['units']} units {a.get('failing_trials')}/{a.get('usable_trials')} {a.get('rate')} {a.get('decision')} | {b['units']} units {b.get('failing_trials')}/{b.get('usable_trials')} {b.get('rate')} {b.get('decision')}")


def _regen_or_first(m):
    p = RUNS / "regen_01/suite/units" / m["domain"] / f"{m['unit']}.json"
    return load(p) if p.exists() else policy.unit_case(m)


if __name__ == "__main__":
    main()
