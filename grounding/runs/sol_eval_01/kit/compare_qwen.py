"""Sol beside Qwen on the same regular tests, under the same rulings and 10-minute budget. No model calls.

Sol's rows are this study's adjudicated sets (kit/score.py: eval/regular_p4.adjudicated.json and
eval/regular_6b.adjudicated.json). Qwen's are the Qwen round's final score (openclaw_eval_01/runs/
final_regular_with_6b.json: Box from full_02, Calendar, Linear and Slack from full_03, 6b from full_04), restricted
to the same test ids; and, for reference, to all 294 Muse-written tests (with G4-LIN-08's 10, which Sol could not run).

Copies report_01/kit/exposure.py's counting: a fact is a (service, catalog fact id) pair (`totals`), and trials are
counted per test from each run's score and adjudication (`trials`: over the budget, not counted, failing and
counted with judge v2's mechanism, passing, void). Adds the per-test cross-table (both expose, only one, neither) and
the fact overlap.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.sol_eval_01.kit.compare_qwen [--before-br]
        # eval/side_by_side_regular[_before_br].json; --before-br: both agents under the rulings file as it was before
        # the two blind-review rulings (kit/score.py; Qwen's adjudication recomputed there, eval/qwen_*_before_br.json)
"""
from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

from grounding.runs.autogen_02.kit import sampler
from grounding.runs.report_01.kit.common import fact_id

STUDY = Path(__file__).resolve().parents[1]
EVAL = STUDY / "eval"
QRUNS = STUDY.parent / "openclaw_eval_01" / "runs"
SETS = ("regular_p4", "regular_6b")
DOMAINS = ("box", "calendar", "linear", "slack")
FORMS = ("cover", "probe", "fact probe")


def load(p: Path):
    return json.loads(p.read_text())


def facts(rows, key):
    return {(r["domain"], fact_id(r["domain"], f)) for r in rows for f in r[key]}


def totals(rows) -> dict:
    return {"tests": len(rows), "tests_exposing": sum(1 for r in rows if r["exposed"]),
            "facts_detect3": len(facts(rows, "exposed")), "facts_detect1": len(facts(rows, "exposed_t1"))}


def trials(parts: list[tuple[Path, Path, set[str]]], keep: set[str]) -> tuple[Counter, Counter]:
    """exposure.py's trial accounting over (score, adjudicated, domains) parts, for the tests in `keep`."""
    counts, mechanisms = Counter(), Counter()
    for score_path, adj_path, domains in parts:
        score, adj = load(score_path), load(adj_path)
        over = {x["trial"] for x in adj["trials_over_budget"]}
        stalled = {x["trial"] for x in adj.get("trials_stalled", [])}
        not_counted = {x["trial"] for x in adj["trials_not_counted"]}
        left = {x["case_id"] for x in adj["left_out_tests"]}
        for t in score["tests"]:
            if t["domain"] not in domains or t["case_id"] in left or t["case_id"] not in keep:
                continue
            for k, tr in t["trials"].items():
                key = f"{k}/{t['case_id']}"
                counts["run"] += 1
                if key in stalled:
                    counts["provider stall (void, to be re-run)"] += 1
                    continue
                if key in over:
                    counts["over the solver's budget, 10 minutes (no exposure)"] += 1
                    continue
                if tr["outcome"] in sampler.FAIL:
                    if key in not_counted:
                        counts["failing, acted only on flawed near misses (not counted)"] += 1
                        continue
                    counts["failing, counted"] += 1
                    mechanisms[tr.get("mechanism") or "(not judged: mechanically clear)"] += 1
                elif tr["outcome"] in sampler.PASS:
                    counts["passing"] += 1
                else:
                    counts[f"void ({tr['outcome']})"] += 1
    return counts, mechanisms


def main():
    suffix = "_before_br" if "--before-br" in sys.argv else ""
    sol = []
    for s in SETS:
        path = EVAL / f"{s}.adjudicated{suffix}.json"
        if path.exists():
            sol += [{**r, "set": s} for r in load(path)["tests"]]
    final = load(EVAL / "qwen_final_regular_before_br.json" if suffix else QRUNS / "final_regular_with_6b.json")
    qwen_all = {r["case_id"]: r for r in final["tests"]}
    ids = {r["case_id"] for r in sol}
    qwen = [qwen_all[c] for c in sorted(ids) if c in qwen_all]
    missing = sorted(ids - set(qwen_all))
    set_ids = {s: {m["case_id"] for m in load(STUDY / "cases" / s / "suite.json")} for s in SETS}
    muse_ids = set_ids["regular_p4"] | set_ids["regular_6b"]
    left_clock = set(load(STUDY / "cases" / "selection.json")["left_out_clock_after_login_expiry"])
    qwen_muse = [r for r in final["tests"] if r["case_id"] in muse_ids | left_clock]

    groups = {"all": lambda r: True}
    groups.update({f"domain:{d}": (lambda d: lambda r: r["domain"] == d)(d) for d in DOMAINS})
    groups.update({f"form:{f}": (lambda f: lambda r: r["form"] == f)(f) for f in FORMS})
    groups.update({f"set:{s}": (lambda s: lambda r: r["case_id"] in set_ids[s])(s) for s in SETS})
    # Probes by near-miss family (exposure.py's probes_by_family): a probe holds one near miss.
    family = {m["case_id"]: m.get("family") for s in SETS for m in load(STUDY / "cases" / s / "suite.json")
              if m.get("form") == "probe"}
    for fam in sorted({f for f in family.values() if f}):
        groups[f"probe family:{fam}"] = (lambda fam: lambda r: r["form"] == "probe" and family.get(r["case_id"]) == fam)(fam)
    out = {"_about": __doc__.split("\n\n")[0], "sol_tests": len(sol), "qwen_matched": len(qwen),
           "missing_in_qwen": missing, "groups": {}}
    by_id_q = {r["case_id"]: r for r in qwen}
    for name, keep in groups.items():
        s_rows = [r for r in sol if keep(r)]
        q_rows = [by_id_q[r["case_id"]] for r in s_rows if r["case_id"] in by_id_q]
        s3, q3 = facts(s_rows, "exposed"), facts(q_rows, "exposed")
        cross = Counter()
        for r in s_rows:
            q = by_id_q.get(r["case_id"])
            cross[("sol" if r["exposed"] else "-") + "/" + ("qwen" if q and q["exposed"] else "-")] += 1
        out["groups"][name] = {"sol": totals(s_rows), "qwen_same_tests": totals(q_rows),
                               "tests_exposing": {"both": cross["sol/qwen"], "sol_only": cross["sol/-"],
                                                  "qwen_only": cross["-/qwen"], "neither": cross["-/-"]},
                               "facts_detect3": {"both": len(s3 & q3), "sol_only": len(s3 - q3),
                                                 "qwen_only": len(q3 - s3)}}
    out["qwen_all_muse_tests"] = {"tests": len(qwen_muse), **totals(qwen_muse)}
    out["facts_detect3"] = {"sol": sorted(f"{d} {f}" for d, f in facts(sol, "exposed")),
                            "qwen_same_tests": sorted(f"{d} {f}" for d, f in facts(qwen, "exposed"))}
    out["facts_detect1"] = {"sol": sorted(f"{d} {f}" for d, f in facts(sol, "exposed_t1")),
                            "qwen_same_tests": sorted(f"{d} {f}" for d, f in facts(qwen, "exposed_t1"))}
    sol_parts = [(EVAL / f"{s}.score.json", EVAL / f"{s}.adjudicated{suffix}.json", set(DOMAINS)) for s in SETS
                 if (EVAL / f"{s}.adjudicated{suffix}.json").exists()]
    qwen_parts = [(QRUNS / f"{run}.score.json", EVAL / f"qwen_{run}.adjudicated{suffix}.json" if suffix else
                   QRUNS / f"{run}.adjudicated.json", set(d)) for run, d in final["parts"].items()]
    st, sm = trials(sol_parts, ids)
    qt, qm = trials(qwen_parts, ids)
    out["trials"] = {"sol": dict(st), "qwen_same_tests": dict(qt)}
    out["failing_trial_mechanisms_judge_v2"] = {"sol": dict(sm.most_common()), "qwen_same_tests": dict(qm.most_common())}
    out["tests"] = [{"case_id": r["case_id"], "domain": r["domain"], "form": r["form"], "set": r["set"],
                     "sol_exposed": r["exposed"], "sol_exposed_t1": r["exposed_t1"],
                     "qwen_exposed": by_id_q.get(r["case_id"], {}).get("exposed"),
                     "qwen_exposed_t1": by_id_q.get(r["case_id"], {}).get("exposed_t1")} for r in sol]
    (EVAL / f"side_by_side_regular{suffix}.json").write_text(json.dumps(out, indent=1) + "\n")
    for name, g in out["groups"].items():
        print(f"{name:28} sol {g['sol']} | qwen {g['qwen_same_tests']} | tests {g['tests_exposing']} | facts "
              f"{g['facts_detect3']}")
    print("qwen, all Muse tests:", out["qwen_all_muse_tests"])
    print("trials", out["trials"])
    print("mechanisms", out["failing_trial_mechanisms_judge_v2"])


if __name__ == "__main__":
    main()
