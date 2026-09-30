"""The second agent (the section after RQ6, and §0.4's separate count): GPT-6.1 Sol on OpenClaw, the Muse-written
half, beside Qwen's final trials of the same tests and units. Copies every number those passages cite from the Sol
round's own files, `sol_eval_01/eval/`, which sol_eval_01's kit wrote; it computes nothing new beyond sums over the
four sets, shares, the per-unit failures from the policy verdicts, rounding half up for display, and the what-if's
differences from the final numbers. No model calls, no agent runs.

Reads, all under grounding/runs/sol_eval_01/:
- eval/side_by_side_regular.json: exposure by group (all, service, form, set, probe family), the test crosstab,
  facts, trials by outcome and judge v2's mechanisms;
- eval/policy_decisions.json: the eight cells for Sol and for Qwen on the same units (rate, bounds, decision,
  readings, the writers' parts), the per-fact view and the regular-policy overlap;
- eval/judge_accuracy.json: judge v2 against the blind labels, per set and pooled;
- eval/observations.json: timings, tool calls, requests, tokens, awareness, visible text, the attempts the retry
  pass replaced and memory_search, for Sol and for Qwen on the same trials;
- eval/judge_cost.json: the judge's calls and list price (the billed amount is not copied; reports give list prices);
- eval/whatif_G4-BOX-15_9102.json: the open validity question's what-if (kit/whatif.py --json);
- eval/blind_*.json, eval/<set>.score.json, the policy verdicts under eval/judged_policy_*/, and
  cases/selection.json and cases/policy_selection.json for the counts of what ran.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.sol

Writes numbers/sol.json.
"""
from __future__ import annotations

from collections import Counter
from decimal import ROUND_HALF_UP, Decimal

from grounding.runs.report_01.kit.common import RUNS, load, write

SOL = RUNS / "sol_eval_01"
EVAL = SOL / "eval"
SETS = ("regular_p4", "regular_6b", "policy_absence", "policy_underspecified")
MODES = ("absence", "underspecified")
FAIL = {"incorrect", "presented"}
GROUPS = ("all", "domain:box", "domain:calendar", "domain:linear", "domain:slack", "form:cover", "form:probe",
          "form:fact probe", "set:regular_p4", "set:regular_6b")


def half_up(x: float, places: int = 2) -> str:
    return str(Decimal(str(x)).quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_UP))


def rate_display(r: dict) -> str:
    return f"{half_up(r['rate'])} [{half_up(r['p10'])}, {half_up(r['p90'])}]"


def scope(obs: dict, pol: dict, side: dict) -> dict:
    trials = {s: obs["sets"][s]["sol"]["trials"] for s in SETS}
    clock_regular = len(load(SOL / "cases" / "selection.json")["left_out_clock_after_login_expiry"])
    psel = load(SOL / "cases" / "policy_selection.json")
    clock = {m: len(psel[m]["left_out_clock"]) for m in MODES}
    missing = sorted(u for m in MODES for c in pol[m]["cells"].values() for u in c["sol"]["missing"])
    ran = {"regular_tests": side["sol_tests"], "absence_units": trials["policy_absence"] // 3,
           "underspecified_units": trials["policy_underspecified"] // 3}
    left_after_running = [x["case_id"] for s in ("regular_p4", "regular_6b")
                          for x in load(EVAL / f"{s}.adjudicated.json")["left_out_tests"]]
    muse = {"regular": ran["regular_tests"] + clock_regular, "absence": ran["absence_units"] + clock["absence"],
            "underspecified": ran["underspecified_units"] + len(missing) + clock["underspecified"]}
    return {"muse_cases": sum(muse.values()), "muse_cases_by_kind": muse, "ran": ran, "cases_ran": sum(ran.values()),
            "left_out_for_the_clock": {"regular": clock_regular, **clock,
                                       "total": clock_regular + sum(clock.values())},
            "not_run": missing, "trials_per_set": trials, "trials_run": sum(trials.values()),
            "trials_on_final_tests_and_units": side["trials"]["sol"]["run"] + trials["policy_absence"]
            + trials["policy_underspecified"],
            "left_out_by_the_rulings_after_running": left_after_running}


def regular(side: dict) -> dict:
    groups = {g: {"sol": side["groups"][g]["sol"], "qwen": side["groups"][g]["qwen_same_tests"],
                  "tests_exposing": side["groups"][g]["tests_exposing"]} for g in GROUPS}
    fam = {g.split(":", 1)[1]: {"probes": v["sol"]["tests"], "sol": v["sol"]["tests_exposing"],
                                "qwen": v["qwen_same_tests"]["tests_exposing"]}
           for g, v in side["groups"].items() if g.startswith("probe family:")}
    shown = ("F8", "F0", "F1", "F7")
    other = {k: sum(v[k] for f, v in fam.items() if f not in shown) for k in ("probes", "sol", "qwen")}
    families = {}
    for s in ("regular_p4", "regular_6b"):
        families.update({m["case_id"]: m.get("family") for m in load(SOL / "cases" / s / "suite.json")})
    exposing = [{"case_id": t["case_id"], "form": t["form"], "family": families.get(t["case_id"]),
                 "sol_exposed": t["sol_exposed"], "qwen_exposed": t["qwen_exposed"]}
                for t in side["tests"] if t["sol_exposed"]]
    all_ = groups["all"]
    voids = []
    for s in ("regular_p4", "regular_6b"):
        for t in load(EVAL / f"{s}.score.json")["tests"]:
            voids += [f"{s}/{trial}/{t['case_id']}" for trial, r in t["trials"].items()
                      if r["outcome"] in ("not_established", "artifact")]
    kept = {t["case_id"] for t in side["tests"]}
    return {"groups": groups,
            "share_of_tests_exposing_percent": {w: round(100 * all_[w]["tests_exposing"] / all_[w]["tests"], 1)
                                                for w in ("sol", "qwen")},
            "probe_families": fam, "probe_families_other_than": {"shown": list(shown), **other},
            "sol_facts_detect3": side["facts_detect3"]["sol"],
            "sol_fact_kinds": dict(Counter(f.split(" ", 1)[1].split(":", 1)[0] for f in side["facts_detect3"]["sol"])),
            "sol_exposing_tests": exposing,
            "sol_facts_through_F8_probes": sorted({f for t in exposing if t["family"] == "F8" for f in t["sol_exposed"]}),
            "sol_only_tests": [t["case_id"] for t in exposing if not t["qwen_exposed"]],
            "sol_void_trials": sorted(v for v in voids if v.rsplit("/", 1)[1] in kept),
            "trials": side["trials"], "mechanisms_judge_v2": side["failing_trial_mechanisms_judge_v2"]}


def policy(pol: dict) -> dict:
    out = {}
    for mode in MODES:
        cells, totals = {}, {}
        for cell, r in pol[mode]["cells"].items():
            row = {"units": r["sol"]["valid_units"]}
            for who, key in (("sol", "sol"), ("qwen", "qwen_same_units")):
                x = r[key]
                row[who] = {k: x[k] for k in ("failing_trials", "usable_trials", "rate", "p10", "p90", "decision",
                                              "missing")}
                row[who]["display"] = rate_display(x)
                row[who]["units_failing_some_trial"] = x["readings"]["any_of_runs"]["failing"]
                row[who]["units_failing_all_trials"] = x["readings"]["all_runs"]["failing"]
                row[who]["units_with_a_usable_trial"] = x["readings"]["any_of_runs"]["units"]
                row[who]["other_readings"] = {k: x["readings"][k]["decision"] for k in ("any_of_runs", "all_runs")}
                row[who]["by_writer_rate"] = {p: x[p].get("rate") for p in ("phase4_only", "6b_only")}
                t = totals.setdefault(who, Counter())
                for k in ("failing_trials", "usable_trials", "units_failing_some_trial", "units_failing_all_trials",
                          "units_with_a_usable_trial"):
                    t[k] += row[who][k]
            cells[cell] = row
        fails = Counter()
        for path in (EVAL / f"judged_policy_{mode}").glob(f"policy_{mode}/t*/*/verdict.json"):
            if load(path).get("outcome") in FAIL:
                fails[path.parent.name] += 1
        out[mode] = {"cells": cells, "totals": {w: dict(t) for w, t in totals.items()},
                     "facts": {w: {k: len(pol[mode]["facts"][key][k]) for k in
                                   ("facts_valid", "facts_failing_detect3", "facts_failing_detect1")}
                               for w, key in (("sol", "sol"), ("qwen", "qwen_same_units"))},
                     "regular_vs_policy_facts": {w: pol[mode]["regular_vs_policy_facts"][key]
                                                 for w, key in (("sol", "sol"), ("qwen", "qwen_same_units"))},
                     "sol_failing_units": dict(fails.most_common())}
    rates = {w: [c[w]["rate"] for m in MODES for c in out[m]["cells"].values()] for w in ("sol", "qwen")}
    out["rate_range"] = {w: [half_up(min(v)), half_up(max(v))] for w, v in rates.items()}
    cal = out["underspecified"]["cells"]["calendar/underspecified"]["sol"]
    out["not_run_worst_case"] = {"unit": cal["missing"], "failing_trials": cal["failing_trials"] + 3,
                                 "usable_trials": cal["usable_trials"] + 3,
                                 "rate": half_up((cal["failing_trials"] + 3) / (cal["usable_trials"] + 3))}
    return out


def judge(acc: dict) -> dict:
    kinds = {"regular": ("regular_p4", "regular_6b"), "absence": ("policy_absence",),
             "underspecified": ("policy_underspecified",)}
    rows = {}
    for kind, sets in kinds.items():
        c = Counter()
        for s in sets:
            x = acc["sets"][s]
            d = x["failure_detection"]
            c["labelled"] += x["labelled"]
            c["agree"] += int(x["collapsed_agreement"].split("/")[0])
            c["exact"] += int(x["exact_agreement"].split("/")[0])
            c["TP"] += d["both_fail"]
            c["FP"] += d["judge_fail"] - d["both_fail"]
            c["FN"] += d["label_fail"] - d["both_fail"]
            c["usable_by_both"] += d["usable_by_both"]
            c["judge_void_only"] += d["void_by_judge_only"]
            c["label_void_only"] += d["void_by_label_only"]
            c["same_facts"] += int(d["same_exposed_facts_when_both_fail"].split("/")[0])
        c["TN"] = c["usable_by_both"] - c["TP"] - c["FP"] - c["FN"]
        c["void_both"] = c["labelled"] - c["usable_by_both"] - c["judge_void_only"] - c["label_void_only"]
        rows[kind] = dict(c)
    rows["all"] = {k: sum(r[k] for r in rows.values()) for k in rows["regular"]}
    drawn = {s: len(load(EVAL / f"blind_{s}.json")["keys"]) for s in SETS}
    pairs = Counter()
    for s in SETS:
        pairs.update(acc["sets"][s]["mechanism_label_to_judge_when_both_fail"])
    alls = rows["all"]
    return {"rows": rows, "drawn": drawn, "drawn_total": sum(drawn.values()),
            "never_ran": sum(drawn.values()) - alls["labelled"],
            "mechanism_agreement": acc["pooled"]["mechanism_agreement_when_both_fail"],
            "mechanism_pairs_label_to_judge": dict(pairs),
            "outcome_differences": [d["key"] for s in SETS for d in acc["sets"][s]["differences"]
                                    if d["label"] != d["judge"]],
            "mechanism_only_differences": [d["key"] for s in SETS for d in acc["sets"][s]["differences"]
                                           if d["label"] == d["judge"]],
            "rule_of_three": {"false_alarm_rate_below": round(3 / alls["TN"], 3),
                              "miss_rate_below": round(3 / alls["TP"], 3)}}


def speed(obs: dict) -> dict:
    out = {}
    for who, key in (("sol", "sol"), ("qwen", "qwen_same_tests")):
        per = [obs["sets"][s][key] for s in SETS]
        med = {m: [p[m]["median"] for p in per] for m in ("seconds", "tool_calls", "input", "output", "reasoning")}
        tot = {m: sum(p[m].get("sum") or 0 for p in per) for m in ("seconds", "requests", "input", "cached", "output",
                                                                    "reasoning")}
        out[who] = {"trials": sum(p["trials"] for p in per), "median_range_by_set": {m: [min(v), max(v)]
                                                                                      for m, v in med.items()},
                    "sums": tot, "agent_hours": round(tot["seconds"] / 3600, 1),
                    "cached_share_of_input": round(tot["cached"] / tot["input"], 3) if tot["cached"] else None,
                    "ended_by_the_budget": sum(p["over_budget"] for p in per),
                    "longest_trial_seconds": max(p["seconds"]["max"] for p in per),
                    "trials_with_reasoning_tokens": sum(p["trials_with_reasoning_tokens"] for p in per),
                    "most_reasoning_tokens_in_a_trial": max(p["reasoning"]["max"] for p in per)}
    return out


def fraction_sum(values: list[str]) -> list[int]:
    return [sum(int(v.split("/")[i]) for v in values) for i in (0, 1)]


def main():
    side = load(EVAL / "side_by_side_regular.json")
    pol = load(EVAL / "policy_decisions.json")
    acc = load(EVAL / "judge_accuracy.json")
    obs = load(EVAL / "observations.json")
    cost = load(EVAL / "judge_cost.json")["total"]
    what = load(EVAL / "whatif_G4-BOX-15_9102.json")
    sets = [obs["sets"][s] for s in SETS]
    aware = {k: fraction_sum([s["awareness"][k] for s in sets])
             for k in ("sol_trials_remarking", "qwen_trials_remarking_any_text", "qwen_trials_remarking_final_answer")}
    memory = {w: {k: sum(s["memory_search"][w][k] for s in sets) for k in sets[0]["memory_search"][w]}
              for w in ("sol", "qwen_same_tests")}
    replaced = [a for s in sets for a in s["replaced_attempts"]["attempts"]]
    base = side["groups"]["all"]
    wreg = what["regular"]
    decisions_same = all(
        what[m]["cells"][cell][w]["decision"] == pol[m]["cells"][cell][w]["decision"]
        for m in MODES for cell in what[m]["cells"] for w in ("sol", "qwen_same_units"))
    out = {
        "_about": __doc__.split("\n\n")[0],
        "scope": scope(obs, pol, side),
        "regular": regular(side),
        "policy": policy(pol),
        "judge": judge(acc),
        "speed_and_tokens": speed(obs),
        "awareness": {k: {"of": v[1], "trials": v[0]} for k, v in aware.items()},
        "sol_steps_with_visible_text": fraction_sum([s["sol_steps_with_visible_text"] for s in sets]),
        "memory_search": memory,
        "replaced_attempts": {"attempts": len(replaced), "trials": len({a["trial"] for a in replaced}),
                              "by_kind": dict(Counter(a["kind"] for a in replaced))},
        "judge_cost": {"calls": cost["calls"], "failed_calls": cost["failed"], "list_usd": cost["list"],
                       "verdicts": sum(1 for s in SETS for _ in EVAL.glob(f"judged_{s}/*/t*/*/verdict.json"))},
        "whatif_G4-BOX-15_9102": {
            "regular_tests_removed": {"sol": base["sol"]["tests"] - wreg["sol"]["tests"],
                                      "qwen": base["qwen_same_tests"]["tests"] - wreg["qwen_same_tests"]["tests"]},
            "regular_facts_detect3_removed": {
                "sol": base["sol"]["facts_detect3"] - wreg["sol"]["facts_detect3"],
                "qwen": base["qwen_same_tests"]["facts_detect3"] - wreg["qwen_same_tests"]["facts_detect3"]},
            "sol_fact_lost": sorted(set(side["facts_detect3"]["sol"]) - set(wreg["sol_facts_detect3"])),
            "policy_decisions_unchanged": decisions_same,
            "cells": {m: what[m]["cells"] for m in MODES}},
    }
    path = write("sol", out)
    print(f"wrote {path.relative_to(RUNS)}")
    print("scope", out["scope"]["muse_cases"], out["scope"]["cases_ran"], out["scope"]["trials_on_final_tests_and_units"],
          out["scope"]["trials_run"])
    print("judge all", out["judge"]["rows"]["all"])


if __name__ == "__main__":
    main()
