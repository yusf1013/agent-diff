"""The three tables the PI asked for (2026-10-01, evening), written to grounding/denominator_tables.md:

1. the denominator per service, filled of prescribed (1,108 items);
2. of the filled items, how many ran on OpenClaw with each agent (Qwen, Sol) and how many showed a failure — only
   OpenClaw runs count, so the boundary items (run only on the bare toy loop) show no run;
3. the attempts: every prescribed item was attempted once through the pipeline (the writer, the code checks, the
   replica pre-checks, the cold reader, the derivation and its witness check, the variant builders); how many items
   the pipeline did not produce or rejected, how many manual review removed afterwards, how many are filled.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.denominator_01.kit.tables
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

import grounding.runs.regen_01.rules  # noqa: F401
from grounding.runs.autogen_02.kit import sampler
from grounding.runs.denominator_01.kit.outcomes import (QWEN_REGEN_POLICY, QWEN_SCORES, SOL_POLICY, SOL_SCORES, SUITES,
                                                       base_fact, scores, single_scenarios)
from grounding.runs.denominator_01.kit.single_decoy import CAT, prescribed
from grounding.runs.openclaw_eval_01 import policy, rulings
from grounding.runs.report_01.kit.common import DOMAINS, RUNS, load, replica_gaps
from grounding.runs.sol_eval_01.kit import policy as solpolicy

HERE = Path(__file__).resolve().parents[1]
OUT_MD = RUNS.parents[0] / "denominator_tables.md"      # grounding/denominator_tables.md
NAMES = {"box": "Box", "calendar": "Calendar", "linear": "Linear", "slack": "Slack"}
PRESCRIBED = {"box": {"cover": 21, "packed": 60, "single": 80, "absence": 60, "underspecified": 60, "boundary": 21},
              "calendar": {"cover": 16, "packed": 34, "single": 48, "absence": 34, "underspecified": 34, "boundary": 24},
              "linear": {"cover": 35, "packed": 85, "single": 112, "absence": 85, "underspecified": 85, "boundary": 20},
              "slack": {"cover": 18, "packed": 34, "single": 46, "absence": 34, "underspecified": 34, "boundary": 28}}
FORMS = ("cover", "packed", "single", "absence", "underspecified", "boundary")
LABELS = {"cover": "Covers", "packed": "Packed probes", "single": "Single-decoy probes", "absence": "Absence tests",
          "underspecified": "Underspecified tests", "boundary": "Boundary tests"}
BOUNDARY_FILLED = {"box": 20, "calendar": 23, "linear": 20, "slack": 27}    # round 1's valid requests plus the one retry


def main():
    filling = load(HERE / "numbers/filling.json")["final+retry"]
    designated = filling["designated_tests"]
    gaps = replica_gaps()
    servable = {(d, f) for d in DOMAINS for f in CAT[d] if f not in set(gaps[d])}

    # ---- tests on record ---------------------------------------------------------------------------------------
    test_meta, rows_by_scenario, cover_decoys = {}, defaultdict(list), {}
    for index, folder in SUITES:
        doc = load(index)
        for m in (doc["tests"] if isinstance(doc, dict) else doc):
            if isinstance(m, str):
                continue
            case = load(folder / m["domain"] / f"{m['case_id']}.json")
            excluded = rulings.test_exclusion(case)
            bad = rulings.flawed(rulings.scenario_of(case["case_id"]))
            d = case["domain"]
            facts = {base_fact(d, c["requirement"]) for ref in case["references"] for c in ref.get("claims", []) if str(c["witness"]) not in bad}
            all_facts = {base_fact(d, c["requirement"]) for ref in case["references"] for c in ref.get("claims", [])}
            test_meta[m["case_id"]] = {"domain": d, "form": m["form"], "scenario": m["scenario"], "facts": facts, "all_facts": all_facts,
                                       "muse": m["scenario"].startswith("G4-"), "excluded": excluded}
            if excluded:
                continue
            rows_by_scenario[m["scenario"]].append(m["case_id"])
            if m["form"] == "cover":
                dv = defaultdict(set)
                for ref in case["references"]:
                    for c in ref.get("claims", []):
                        if str(c["witness"]) not in bad:
                            dv[base_fact(d, c["requirement"])].add(str(c["witness"]))
                for f, ws in dv.items():
                    cover_decoys[(m["scenario"], f)] = ws
    valid_meta = {k: v for k, v in test_meta.items() if not v["excluded"]}

    # ---- items and the test that fills each -------------------------------------------------------------------
    items = defaultdict(list)     # form -> [(domain, item key, test id)]
    for cid, meta in valid_meta.items():
        if meta["form"] == "cover" and meta["muse"]:
            items["cover"].append((meta["domain"], meta["scenario"], cid))
    packed_by_item = {}
    for key, sid in designated.items():
        form, d, f = key.split(" ", 2)
        if form == "probe":
            cands = [c for c in rows_by_scenario[sid] if valid_meta[c]["form"] in ("probe", "fact probe") and f in valid_meta[c]["facts"]]
            fp = [c for c in cands if valid_meta[c]["form"] == "fact probe"]
            test = fp[0] if fp else (cands[0] if len(cover_decoys.get((sid, f), ())) == 1 and cands else None)
            if test:
                items["packed"].append((d, f, test)); packed_by_item[(d, f)] = test
        elif form in ("absence", "underspecified"):
            items[form].append((d, f, sid))
    single_scn = single_scenarios(designated, valid_meta, rows_by_scenario)
    for (d, f), sid in single_scn.items():
        if (d, f) not in servable:
            continue
        singles = sorted(c for c in rows_by_scenario[sid] if valid_meta[c]["form"] == "probe" and f in valid_meta[c]["facts"])
        for k, cid in enumerate(singles[:prescribed(d, f)]):
            items["single"].append((d, f"{f} #{k + 1}", cid))
    filled = {d: {form: sum(1 for it in items[form] if it[0] == d) for form in FORMS if form != "boundary"} for d in DOMAINS}
    for d in DOMAINS:
        filled[d]["boundary"] = BOUNDARY_FILLED[d]

    # ---- table 2: runs and failures on OpenClaw, per item -----------------------------------------------------
    unit_meta = {}
    for mode in ("absence", "underspecified"):
        for cell, seq in policy.population_plan(mode)["cells"].items():
            for u in seq:
                unit_meta[u["unit"]] = {**u, "mode": mode}
        for u in load(RUNS / "regen_01/suite/units.json")["units"]:
            if u["mode"] == mode:
                unit_meta[u["unit"]] = dict(u)
    runs = {}
    for agent, score_paths in (("qwen", QWEN_SCORES), ("sol", SOL_SCORES)):
        sc, _ = scores(score_paths)
        outcomes = {}
        for mode in ("absence", "underspecified"):
            if agent == "qwen":
                o = solpolicy.qwen_outcomes(mode); o.update(policy.population_outcomes([QWEN_REGEN_POLICY[mode]]))
            else:
                o = solpolicy.outcomes_of([p for p in SOL_POLICY[mode] if p.exists()])
            outcomes.update(o)
        per = {d: {form: {"run": 0, "failed": 0} for form in FORMS} for d in DOMAINS}
        for form in ("cover", "packed", "single"):
            for d, key, cid in items[form]:
                t = sc.get(cid)
                if not t:
                    continue
                per[d][form]["run"] += 1
                exposed = {base_fact(d, x) for x in t.get("exposed", [])}
                fact = key.split(" #")[0]
                hit = bool(exposed) if form == "cover" else (fact in exposed)
                per[d][form]["failed"] += 1 if hit else 0
        for form in ("absence", "underspecified"):
            for d, key, uid in items[form]:
                outs = [x for x in outcomes.get(uid, {}).values() if x in sampler.FAIL | sampler.PASS]
                if not outs:
                    continue
                per[d][form]["run"] += 1
                per[d][form]["failed"] += 1 if any(x in sampler.FAIL for x in outs) else 0
        runs[agent] = per      # boundary stays 0: no OpenClaw run

    # ---- table 3: attempts, pipeline, manual review, filled -----------------------------------------------------
    reasons = filling["unfilled_reasons"]
    failed_brief_facts = set()
    for k, v in reasons.items():
        if v == "the brief failed":
            _, d, f = k.split(" ", 2); failed_brief_facts.add((d, f))
    t3 = {d: {form: {"pipeline": 0, "review": 0} for form in FORMS} for d in DOMAINS}
    for k, v in reasons.items():
        form, d, f = k.split(" ", 2)
        form = {"probe": "packed"}.get(form, form)
        if v == "the brief failed" or v.startswith("no test") or "no packed form" in v:
            t3[d][form]["pipeline"] += 1
        else:
            t3[d][form]["review"] += 1
    # single-decoy items: the shortfall per fact, attributed
    for (d, f) in sorted(servable):
        n = prescribed(d, f)
        sid = single_scn.get((d, f))
        built = len([c for c in rows_by_scenario.get(sid, []) if valid_meta[c]["form"] == "probe" and f in valid_meta[c]["facts"]]) if sid else 0
        short = max(0, n - built)
        if not short:
            continue
        if (d, f) in failed_brief_facts or sid is None:
            t3[d]["single"]["pipeline"] += short
            continue
        ruled = sum(1 for cid, meta in test_meta.items() if meta["excluded"] and meta["form"] == "probe" and meta["scenario"] == sid and f in meta["all_facts"])
        r = min(ruled, short)
        t3[d]["single"]["review"] += r
        t3[d]["single"]["pipeline"] += short - r
    for d in DOMAINS:   # boundary: the cold reader's three rejections (Slack, Calendar, Box), one restored by the retry (Linear)
        t3[d]["boundary"]["pipeline"] = PRESCRIBED[d]["boundary"] - BOUNDARY_FILLED[d]
    # covers: the four failed briefs (3 Linear, 1 Box), all in the pipeline
    t3["linear"]["cover"]["pipeline"] = 3; t3["box"]["cover"]["pipeline"] = 1

    # ---- the markdown -------------------------------------------------------------------------------------------
    def tot(dct, form, k):
        return sum(dct[d][form][k] if isinstance(dct[d][form], dict) else dct[d][form] for d in DOMAINS)
    L = []
    L.append("# The denominator: three tables\n")
    L.append("*Built by `runs/denominator_01/kit/tables.py` from the kits' numbers on 2026-10-01. The definitions are in "
             "[protocols/denominator.md](protocols/denominator.md). Only OpenClaw runs count as runs of the agents under test.*\n")
    L.append("## Table 1. The denominator per service, filled of prescribed\n")
    L.append("| Service | " + " | ".join(LABELS[f] for f in FORMS) + " | Total |")
    L.append("|---|" + "---:|" * (len(FORMS) + 1))
    for d in DOMAINS:
        cells = [f"{filled[d][f]} of {PRESCRIBED[d][f]}" for f in FORMS]
        L.append(f"| {NAMES[d]} | " + " | ".join(cells) + f" | {sum(filled[d].values())} of {sum(PRESCRIBED[d].values())} |")
    tf = {f: sum(filled[d][f] for d in DOMAINS) for f in FORMS}; tp = {f: sum(PRESCRIBED[d][f] for d in DOMAINS) for f in FORMS}
    L.append("| **All** | " + " | ".join(f"**{tf[f]} of {tp[f]}**" for f in FORMS) + f" | **{sum(tf.values())} of {sum(tp.values()):,}** |")
    L.append("\nThe main denominator (732) is the four right-hand columns; covers and single-decoy probes are tracked beside it. "
             "One test can fill two items: a fact with one decoy has one probe that is both its packed form and its single-decoy "
             "probe; an underspecified test whose dropped condition carries two facts fills both facts' items.\n")
    L.append("## Table 2. Of the filled items, runs on OpenClaw and failures found\n")
    L.append("A regular item \"failed\" when its test exposed its fact in any of its three trials (a cover: any fact); a policy item "
             "when its test had a failing trial. The boundary items have run only on the bare toy loop, which does not count.\n")
    L.append("| Item | Filled | Qwen: run | Qwen: failed | Sol: run | Sol: failed |")
    L.append("|---|---:|---:|---:|---:|---:|")
    for f in FORMS:
        L.append(f"| {LABELS[f]} | {tf[f]} | {tot(runs['qwen'], f, 'run')} | {tot(runs['qwen'], f, 'failed')} | {tot(runs['sol'], f, 'run')} | {tot(runs['sol'], f, 'failed')} |")
    L.append(f"| **All** | **{sum(tf.values())}** | **{sum(tot(runs['qwen'], f, 'run') for f in FORMS)}** | **{sum(tot(runs['qwen'], f, 'failed') for f in FORMS)}** | "
             f"**{sum(tot(runs['sol'], f, 'run') for f in FORMS)}** | **{sum(tot(runs['sol'], f, 'failed') for f in FORMS)}** |")
    L.append("\nSol did not run the tests of one Linear brief (three facts; their scenario's clock lies past the login's expiry).\n")
    L.append("## Table 3. The attempts: every prescribed item attempted once\n")
    L.append("Every servable fact had one generation attempt through the pipeline (its brief's writer session with the code checks, "
             "the replica pre-checks and the cold reader; then the derivation with its witness check and the variant builders), plus "
             "one retry where the first attempt produced no scenario; every faithful boundary had one request written and read. "
             "\"Pipeline\" counts the items the pipeline rejected or could not produce; \"manual review\" the items a ruling removed "
             "afterwards (the PI's rulings, or a session's review).\n")
    L.append("| Item | Attempted | Not produced or rejected in the pipeline | Removed in manual review | Filled |")
    L.append("|---|---:|---:|---:|---:|")
    for f in FORMS:
        p_ = tot(t3, f, "pipeline"); r_ = tot(t3, f, "review")
        L.append(f"| {LABELS[f]} | {tp[f]} | {p_} | {r_} | {tf[f]} |")
    L.append(f"| **All** | **{sum(tp.values()):,}** | **{sum(tot(t3, f, 'pipeline') for f in FORMS)}** | **{sum(tot(t3, f, 'review') for f in FORMS)}** | **{sum(tf.values())}** |")
    L.append("\nIn the pipeline: four briefs (eleven facts) got no scenario, all from the cold reader after its rounds ran out; "
             "the derivation's witness check dropped the probes of six facts; the underspecified builder could not make a variant "
             "for 30 facts (the writer declined 16, the reader rejected 12, code found 3 not derivable); the writer built fewer "
             "single decoys than the catalog names for some facts; the cold reader rejected three boundary requests. In manual "
             "review: rulings on near misses and variants (23 items), and single-decoy probes holding a ruled near miss.\n")
    OUT_MD.write_text("\n".join(L) + "\n")
    json.dump({"filled": filled, "prescribed": PRESCRIBED, "runs": runs, "attempts": t3}, open(HERE / "numbers/tables.json", "w"), indent=1)
    print("\n".join(L))


if __name__ == "__main__":
    main()
