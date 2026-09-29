"""RQ4: the failures the regular suite exposes on OpenClaw (6a and 6b), under the PI's rulings and the 8-minute
budget, by writer, fact kind, near-miss family and form; trial-level counts; judge v2's failure mechanisms.

A test **exposes** a fact when a counted trial acts on (or presents) a near miss of that fact; detect@3 uses all
three trials, detect@1 the first. The final per-test results are openclaw_eval_01's `final_regular_with_6b.json`
(Box from `full_02`, Calendar, Linear and Slack from the opaque-id re-run `full_03`, 6b from `full_04`).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.exposure

Writes numbers/exposure.json.
"""
from __future__ import annotations

from collections import Counter, defaultdict

from grounding.runs.autogen_02.kit import sampler
from grounding.runs.report_01.kit.common import (DOMAINS, NUMBERS, RUNS, WRITER_ORDER, WRITERS, fact_id, load,
                                                 suite_tests)

OC = RUNS / "openclaw_eval_01/runs"


def totals(rows, facts_covered=None):
    f3 = {(r["domain"], fact_id(r["domain"], f)) for r in rows for f in r["exposed"]}
    f1 = {(r["domain"], fact_id(r["domain"], f)) for r in rows for f in r["exposed_t1"]}
    out = {"tests": len(rows), "tests_exposing": sum(1 for r in rows if r["exposed"]),
           "facts_detect3": len(f3), "facts_detect1": len(f1)}
    if facts_covered is not None:
        out["facts_covered"] = facts_covered
    return out


def main():
    final = load(OC / "final_regular_with_6b.json")
    meta = {m["case_id"]: m for m, _ in suite_tests()}
    cov = load(NUMBERS / "coverage.json")
    rows = final["tests"]
    for r in rows:
        m = meta[r["case_id"]]
        r["writer"] = WRITERS[m["source"]]
        r["family"] = m.get("family")

    by_writer = {w: totals([r for r in rows if r["writer"] == w],
                           sum(cov["achieved"][d]["per_writer"][w] for d in DOMAINS)) for w in WRITER_ORDER}
    by_domain = {d: totals([r for r in rows if r["domain"] == d], cov["achieved"][d]["covered"]) for d in DOMAINS}
    by_form = {f: totals([r for r in rows if r["form"] == f]) for f in ("cover", "probe", "fact probe")}

    # By fact kind: facts exposed against facts covered.
    exposed3 = {(r["domain"], fact_id(r["domain"], f)) for r in rows for f in r["exposed"]}
    exposed1 = {(r["domain"], fact_id(r["domain"], f)) for r in rows for f in r["exposed_t1"]}
    by_kind = {}
    for k in "ARHBD":
        covered = {(d, f) for d in DOMAINS for f in cov["achieved"][d]["covered_facts"] if f.startswith(k + ":")}
        by_kind[k] = {"facts_covered": len(covered), "facts_detect3": len(exposed3 & covered),
                      "facts_detect1": len(exposed1 & covered)}

    # Probes by near-miss family (a probe holds one near miss; a fact probe all of one fact's).
    by_family = defaultdict(Counter)
    for r in rows:
        if r["form"] == "probe":
            fam = r["family"] or "?"
            by_family[fam]["probes"] += 1
            by_family[fam]["exposing"] += bool(r["exposed"])
    designated = [r for r in rows if r["form"] == "probe" and (r["family"] or "F0") != "F0"]
    plain = [r for r in rows if r["form"] == "probe" and r["family"] == "F0"]

    # Trials: every trial of the tests in the final score, from each run's score, under the rulings and the budget.
    trials = Counter()
    mechanisms = Counter()
    for run, domains in final["parts"].items():
        score = load(OC / f"{run}.score.json")
        adj = load(OC / f"{run}.adjudicated.json")
        over = {x["trial"] for x in adj["trials_over_budget"]}
        not_counted = {x["trial"] for x in adj["trials_not_counted"]}
        left = {x["case_id"] for x in adj["left_out_tests"]}
        for t in score["tests"]:
            if t["domain"] not in domains or t["case_id"] in left:
                continue
            for k, tr in t["trials"].items():
                key = f"{k}/{t['case_id']}"
                trials["run"] += 1
                if key in over:
                    trials["over the 8-minute budget (no exposure)"] += 1
                    continue
                if tr["outcome"] in sampler.FAIL:
                    if key in not_counted:
                        trials["failing, acted only on flawed near misses (not counted)"] += 1
                        continue
                    trials["failing, counted"] += 1
                    mechanisms[tr.get("mechanism") or "(not judged: mechanically clear)"] += 1
                elif tr["outcome"] in sampler.PASS:
                    trials["passing"] += 1
                else:
                    trials[f"void ({tr['outcome']})"] += 1

    out = {"final": final["final"], "by_domain": by_domain, "by_form": by_form, "by_writer": by_writer,
           "by_kind": by_kind, "probes_by_family": {k: dict(v) for k, v in sorted(by_family.items())},
           "probes_designated_vs_plain": {"designated (F1-F8)": totals(designated), "plain (F0)": totals(plain)},
           "trials": dict(trials), "failing_trial_mechanisms_judge_v2": dict(mechanisms.most_common()),
           "facts_detect3": sorted(f"{d} {f}" for d, f in exposed3),
           "facts_detect1": sorted(f"{d} {f}" for d, f in exposed1)}
    print(NUMBERS / "exposure.json")
    (NUMBERS / "exposure.json").write_text(__import__("json").dumps(out, indent=1) + "\n")
    for k in ("final", "by_domain", "by_form", "by_writer", "by_kind", "probes_designated_vs_plain", "trials",
              "failing_trial_mechanisms_judge_v2"):
        print(k, out[k])
    print("families", out["probes_by_family"])


if __name__ == "__main__":
    main()
