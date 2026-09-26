"""Every table of report.md, from the runs, the review files and the exemplars' outcomes. No service calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_01.kit.tables > grounding/runs/autogen_01/tables.md

Yields are given two ways:
- **automated:** the judge's verdicts as they are;
- **adjudicated:** my reading of every failing verdict (eval/judge_review.json) applied. Exposures that rest only on a
  decoy I judged contestable or invalid (eval/validity.json) are then left out of the "valid" column.
"""
from __future__ import annotations

import json
import statistics
from collections import Counter, defaultdict
from pathlib import Path

from grounding.runs.autogen_01.inputs.make_briefs import SLACK_ALIASES
from grounding.runs.autogen_01.kit.judge import COLLAPSE
from grounding.runs.fact_coverage_02.followups import _conditions

STUDY = Path(__file__).resolve().parents[1]
RUNS = STUDY / "runs"
EVAL = STUDY / "eval"
FC2 = STUDY.parent / "fact_coverage_02"
ARMS = {"Arm R": ("gen_arm_r", "solve_arm_r"), "Arm P": ("gen_arm_p", "solve_arm_p"),
        "Arm P, method v2": ("gen_arm_p_v2", "solve_arm_p_v2")}
YIELD_ARMS = {**ARMS, "Control (exemplars today)": ("control", "solve_control")}


def load(path, default=None):
    return json.loads(path.read_text()) if path.exists() else default


def outcomes(gen):
    out = {}
    for p in sorted((RUNS / gen).glob("*/outcome.json")):
        o = json.loads(p.read_text())
        out[o["scenario_id"]] = o
    return out


def attempts_errored(gen):
    return sorted(p.name.split(".")[0] for p in (RUNS / gen).glob("*.attempt1-http429"))


def table_generation():
    rows = ["## Generation", "",
            "| Arm | Briefs | Accepted | Rejected | Versions (median, max) | Check rounds | Reader rounds | "
            "Briefs rerun after HTTP 429 |", "|---|---:|---:|---:|---|---:|---:|---:|"]
    for arm, (gen, _) in ARMS.items():
        o = outcomes(gen)
        acc = [x for x in o.values() if x["status"] == "accepted"]
        versions = [x["versions"] for x in o.values()]
        rows.append(f"| {arm} | {len(o)} | {len(acc)} | {len(o) - len(acc)} | "
                    f"{statistics.median(versions) if versions else '-'}, {max(versions) if versions else '-'} | "
                    f"{sum(x['check_rounds'] for x in o.values())} | {sum(x['reader_rounds'] for x in o.values())} | "
                    f"{len(attempts_errored(gen))} |")
    rows += ["", "Versions sent back, by the stage that found problems:", "",
             "| Arm | Checks | Replica pre-checks | Reader |", "|---|---:|---:|---:|"]
    for arm, (gen, _) in ARMS.items():
        stages = Counter(h["stage"] for x in outcomes(gen).values() for h in x["history"] if h["problems"])
        rows.append(f"| {arm} | {stages['checks']} | {stages['replica']} | {stages['reader']} |")
    return rows


def table_validity():
    v = load(EVAL / "validity.json", {})
    rows = ["## Manual validity review", "",
            "| Arm | Scenarios reviewed | Valid | Flawed | Invalid | Decoys | Valid decoys | Contestable | Invalid |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for arm, prefix in (("Arm R", "AR-"), ("Arm P", "AP-"), ("Arm P, method v2", "AP2-")):
        sc = {k: x for k, x in v.items() if k.startswith(prefix)}
        verdicts = Counter(x["verdict"] for x in sc.values())
        decoys = [d for x in sc.values() for d in x["decoys"].values()]
        kinds = Counter(next(k for k in ("valid", "contestable", "invalid", "other") if d.startswith(k) or k == "other")
                        for d in decoys)
        rows.append(f"| {arm} | {len(sc)} | {verdicts['valid']} | {verdicts['flawed']} | {verdicts['invalid']} | "
                    f"{len(decoys)} | {kinds['valid']} | {kinds['contestable']} | {kinds['invalid']} |")
    rows += ["", "Exemplar reference (fact_coverage_02, 21 new scenarios): 2 had to be fixed after running (LIN-25 "
             "label ids, SLK-21 reaction name), 1 test is invalid (BOX-31), 1 decoy is contestable (BOX-22)."]
    return rows


def design(case):
    ref = case["references"][0]
    claims = ref["claims"]
    return {"conditions": _conditions(ref["query"]), "facts": len({c["requirement"] for c in claims}),
            "decoys": len(claims), "families": Counter(c.get("family") for c in claims)}


def table_design():
    rows = ["## Request size and families", "",
            "| Set | Scenarios | Conditions median (range) | Facts tested median (range) | Decoys median (range) | "
            "Families |", "|---|---:|---|---|---|---|"]

    def line(label, cases):
        ds = [design(c) for c in cases]
        if not ds:
            return
        fam = Counter()
        for d in ds:
            fam.update(d["families"])

        def mr(key):
            vals = [d[key] for d in ds]
            return f"{statistics.median(vals)} ({min(vals)}-{max(vals)})"
        rows.append(f"| {label} | {len(ds)} | {mr('conditions')} | {mr('facts')} | {mr('decoys')} | "
                    + ", ".join(f"{k} {n}" for k, n in sorted(fam.items())) + " |")
    ex = []
    for p in sorted((FC2 / "cases_new").glob("*/*.json")):
        c = json.loads(p.read_text())
        if not c["case_id"].startswith(("P-", "PP-")) and "-A" not in c["case_id"] and "TWIN" not in c["case_id"]:
            if not c["case_id"].startswith(("P-", "FP-")):
                for r in c["references"]:
                    for cl in r["claims"]:
                        cl.setdefault("family", None)
                ex.append(c)
    fam_ex = load(FC2 / "suite_new.json", [])
    by_scen = defaultdict(list)
    for t in fam_ex:
        if t["form"] == "probe":
            by_scen[t["scenario"]].append(t["family"])
    for c in ex:
        fams = by_scen.get(c["case_id"], [])
        for cl, f in zip(c["references"][0]["claims"], fams):
            cl["family"] = f
    line("Exemplars (fact_coverage_02 new scenarios)", ex)
    for arm, (gen, _) in ARMS.items():
        cases = [load(RUNS / gen / sid / "case.json") for sid, o in outcomes(gen).items() if o["status"] == "accepted"]
        line(f"Generated, {arm}", [c for c in cases if c])
    return rows


def adjudicated(score, review, validity):
    """Per test: exposed facts after my review (overrides applied) and without contestable or invalid decoys."""
    bad = {}
    for sid, v in validity.items():
        if sid.startswith("_"):
            continue
        for witness, verdict in v["decoys"].items():
            kind = verdict.split(":")[0].split(";")[0].strip()
            if kind in ("contestable", "invalid"):
                bad[(sid, witness)] = kind
    run = score.get("_run")
    judged_dir = RUNS / f"{run}_judged" / run
    invalid_tests = {c for sid, v in validity.items() if not sid.startswith("_") for c in v.get("invalid_tests", [])}
    out = []
    for t in score["tests"]:
        if t["case_id"] in invalid_tests:
            out.append({**t, "exposed_adjudicated": [], "invalid": True})
            continue
        exposed = set()
        scenario = t.get("scenario")
        for trial, r in t["trials"].items():
            key = f"{run}/{trial}/{t['case_id']}"
            rv = review.get(key, {})
            outcome = rv.get("outcome", r["outcome"]) if rv.get("review") == "override" else r["outcome"]
            facts = rv.get("exposed", r["exposed"]) if rv.get("review") == "override" else r["exposed"]
            if COLLAPSE.get(outcome) != "fail" or rv.get("contestable"):
                continue
            # A trial whose acted-on records are all decoys I judged contestable or invalid does not count.
            verdict = load(judged_dir / trial / t["case_id"] / "verdict.json", {}) or {}
            acted = [str(a) for a in verdict.get("acted_on", [])]
            if acted and all((scenario, a) in bad for a in acted):
                continue
            exposed |= set(facts)
        out.append({**t, "exposed_adjudicated": sorted(exposed)})
    return out, bad


def table_yield():
    review = load(EVAL / "judge_review.json", {})
    validity = load(EVAL / "validity.json", {})
    rows = ["## Yield on Qwen (3 trials)", "",
            "| Arm | Form | Tests | Tests exposing | Facts, detect@1 | Facts, detect@3 (automated) | "
            "Facts, detect@3 (adjudicated) | Facts per test (adjudicated) |", "|---|---|---:|---:|---:|---:|---:|---:|"]
    facts_by_arm = {}
    for arm, (gen, solve) in YIELD_ARMS.items():
        score = load(RUNS / f"{solve}.score.json")
        if not score:
            continue
        score["_run"] = solve
        tests, _ = adjudicated(score, review, validity)
        facts_by_arm[arm] = tests
        for form in ("probe", "fact probe", "cover", "cover+probe", None):
            if form == "cover+probe":  # the exemplars' composition (no fact probes)
                ts = [t for t in tests if t.get("form") in ("cover", "probe")]
            else:
                ts = [t for t in tests if form is None or t.get("form") == form]
            if not ts:
                continue
            f1 = {x for t in ts for x in t["exposed_t1"]}
            f3 = {x for t in ts for x in t["exposed"]}
            fa = {x for t in ts for x in t["exposed_adjudicated"]}
            rows.append(f"| {arm} | {form or '**all**'} | {len(ts)} | {sum(bool(t['exposed']) for t in ts)} | "
                        f"{len(f1)} | {len(f3)} | {len(fa)} | {len(fa) / len(ts):.2f} |")
    rows += ["", "Tests are every derived test that ran; a test I judged invalid (P-AP-SLK-05-I12) counts and exposes "
             "nothing after adjudication.", "",
             "Exemplar reference (fact_coverage_02 §6, the same 36 facts as Arm R): 76 tests (18 covers, 58 "
             "probes), 14 facts at detect@3 (13 uncontested), 0.18 per test; probes 13 facts (0.22 per probe), "
             "covers 2 (0.11)."]
    for arm, tests in facts_by_arm.items():
        fa = sorted({x for t in tests for x in t["exposed_adjudicated"]})
        rows.append(f"\n{arm}, facts exposed (adjudicated): " + ", ".join(f"`{f}`" for f in fa))
    generated = [arm for arm in facts_by_arm if arm in ARMS]  # families are labelled in the generated suites only
    fam_rows = ["", "### Probes by family (adjudicated): exposing probes / probes", "",
                "| Family | " + " | ".join(generated) + " | Facts (all generated arms) |",
                "|---|" + "---:|" * len(generated) + "---|"]
    fam = defaultdict(lambda: defaultdict(list))
    for arm in generated:
        for t in facts_by_arm[arm]:
            if t.get("form") == "probe":
                fam[t.get("family")][arm].append(t)
    for f in sorted(fam, key=str):
        cells = [f"{sum(bool(t['exposed_adjudicated']) for t in fam[f][arm])}/{len(fam[f][arm])}" for arm in generated]
        facts = sorted({x for arm in generated for t in fam[f][arm] for x in t["exposed_adjudicated"]})
        fam_rows.append(f"| {f} | " + " | ".join(cells) + " | " + ", ".join(facts) + " |")
    return rows + fam_rows


def table_runtime():
    """Trial outcomes per arm: the judge's (automated) and after my overrides (adjudicated)."""
    review = load(EVAL / "judge_review.json", {})
    rows = ["## Trial outcomes (runtime validity)", "",
            "| Arm | Trials | Pass | Fail | Artifact | Not established | Incomplete or false absence | "
            "Artifacts after review |", "|---|---:|---:|---:|---:|---:|---:|---:|"]
    for arm, (_, solve) in YIELD_ARMS.items():
        score = load(RUNS / f"{solve}.score.json")
        if not score:
            continue
        auto, adj = Counter(), Counter()
        for t in score["tests"]:
            for trial, r in t["trials"].items():
                auto[r["outcome"]] += 1
                rv = review.get(f"{solve}/{trial}/{t['case_id']}", {})
                adj[rv.get("outcome", r["outcome"]) if rv.get("review") == "override" else r["outcome"]] += 1
        c = Counter()
        for k, n in auto.items():
            c[COLLAPSE.get(k, k)] += n
        rows.append(f"| {arm} | {sum(auto.values())} | {c['pass']} | {c['fail']} | {auto['artifact']} | "
                    f"{auto['not_established']} | {c['incomplete'] + c['false_absence']} | {adj['artifact']} |")
    return rows


def table_reproduction():
    ex = load(EVAL / "exemplar_outcomes.json", {})
    score = load(RUNS / "solve_arm_r.score.json")
    if not score:
        return []
    score["_run"] = "solve_arm_r"
    review, validity = load(EVAL / "judge_review.json", {}), load(EVAL / "validity.json", {})
    tests, _ = adjudicated(score, review, validity)
    control = load(RUNS / "solve_control.score.json")
    ctests = []
    if control:
        control["_run"] = "solve_control"
        ctests, _ = adjudicated(control, review, validity)
    rows = ["## Arm R, fact by fact", "",
            "| Exemplar | Fact | Exemplar exposed (recorded) | Exemplar exposed today (control, adjudicated) | "
            "Generated exposed (adjudicated) |", "|---|---|---|---|---|"]
    counts = Counter()
    for sid, o in sorted(outcomes("gen_arm_r").items()):
        ex_id = o["brief"].get("exemplar")
        mine = [t for t in tests if t.get("scenario") == sid]
        got = {x for t in mine for x in t["exposed_adjudicated"]}
        today = {SLACK_ALIASES.get(x, x) for t in ctests if t.get("scenario") == ex_id for x in t["exposed_adjudicated"]}
        for fact in o["brief"]["facts"]:
            e = fact in ex.get(ex_id, {}).get("exposed", [])
            c = fact in today
            g = fact in got
            counts["recorded"] += e
            counts["control"] += c
            counts["generated"] += g
            counts["control_and_generated"] += c and g
            rows.append(f"| {ex_id} | `{fact}` | {'yes' if e else ''} | {'yes' if c else ''} | "
                        f"{'yes' if g else ('not run' if not mine else '')} |")
    rows += ["", f"Brief facts exposed: recorded exemplar runs {counts['recorded']}; exemplars today {counts['control']}; "
                 f"generated {counts['generated']}; both today's exemplars and the generated suites "
                 f"{counts['control_and_generated']}."]
    return rows


def table_v1_v2():
    """Arm P, the same briefs under method v1 and v2 (amendment 4): facts exposed, adjudicated."""
    review, validity = load(EVAL / "judge_review.json", {}), load(EVAL / "validity.json", {})
    scored = {}
    for label, solve in (("v1", "solve_arm_p"), ("v2", "solve_arm_p_v2")):
        score = load(RUNS / f"{solve}.score.json")
        if not score:
            return []
        score["_run"] = solve
        scored[label], _ = adjudicated(score, review, validity)
    rows = ["## Arm P: method v1 against v2, same briefs", "",
            "| Brief | Fact | v1 status | v1 exposed | v2 status | v2 exposed |", "|---|---|---|---|---|---|"]
    v1_out, v2_out = outcomes("gen_arm_p"), outcomes("gen_arm_p_v2")
    counts = Counter()
    for sid, o in sorted(v1_out.items()):
        sid2 = sid.replace("AP-", "AP2-")
        o2 = v2_out.get(sid2, {})
        g1 = {x for t in scored["v1"] if t.get("scenario") == sid for x in t["exposed_adjudicated"]}
        g2 = {x for t in scored["v2"] if t.get("scenario") == sid2 for x in t["exposed_adjudicated"]}
        for fact in o["brief"]["facts"]:
            e1, e2 = fact in g1, fact in g2
            counts["v1"] += e1
            counts["v2"] += e2
            rows.append(f"| {sid} | `{fact}` | {o['status']} | {'yes' if e1 else ''} | {o2.get('status', '-')} | "
                        f"{'yes' if e2 else ''} |")
    for label in ("v1", "v2"):
        tests = scored[label]
        cp = [t for t in tests if t.get("form") in ("cover", "probe")]  # as in table_yield: an invalid test exposes nothing
        facts_all = {x for t in tests for x in t["exposed_adjudicated"]}
        facts_cp = {x for t in cp for x in t["exposed_adjudicated"]}
        rows.append(f"\n{label}: brief facts exposed {counts[label]}; all tests {len(tests)}, facts {len(facts_all)} "
                    f"({len(facts_all) / max(1, len(tests)):.2f} per test); covers and probes {len(cp)}, facts "
                    f"{len(facts_cp)} ({len(facts_cp) / max(1, len(cp)):.2f} per test).")
    return rows


def table_judge():
    rows = ["## Judge", "", "| Split | Trials | Collapsed agreement | Exposed-fact agreement | Artifacts caught |",
            "|---|---:|---:|---:|---:|"]
    for name in ("judge_dev_01", "judge_dev_02", "judge_test_01"):
        c = load(RUNS / name / "comparison.json")
        if c:
            rows.append(f"| {name} | {c['trials']} | {c['collapsed_agreement']} | "
                        f"{c['exposed_agreement_on_shared_fails']} | {c['artifact_recall']} |")
    review = load(EVAL / "judge_review.json", {})
    marks = Counter(v.get("review") for k, v in review.items() if not k.startswith("_"))
    rows += ["", f"On the generated runs, I read every failing, void or unclear verdict: {marks['agree']} agree, "
                 f"{marks['override']} overridden."]
    return rows


def table_tokens():
    rows = ["## Tokens (Claude Code Sonnet agents; list-price estimate, billed to the subscription)", "",
            "| Run | Role | Calls | Output tokens | Cache writes | Cache reads | Uncached input | List-price USD |",
            "|---|---|---:|---:|---:|---:|---:|---:|"]
    total = 0.0
    for calls in sorted(RUNS.glob("*/calls.jsonl")):
        agg = defaultdict(Counter)
        for line in calls.read_text().splitlines():
            r = json.loads(line)
            a = agg[r["role"]]
            a["calls"] += 1
            for k in ("output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "input_tokens"):
                a[k] += r.get(k) or 0
            a["usd"] += r.get("cost_usd_list_price") or 0
        for role, a in sorted(agg.items()):
            total += a["usd"]
            rows.append(f"| {calls.parent.name} | {role} | {a['calls']} | {a['output_tokens']:,} | "
                        f"{a['cache_creation_input_tokens']:,} | {a['cache_read_input_tokens']:,} | "
                        f"{a['input_tokens']:,} | {a['usd']:.2f} |")
    failed = defaultdict(Counter)
    for path in RUNS.glob("**/*.failed.json"):
        run = path.relative_to(RUNS).parts[0]
        result = (load(path, {}) or {}).get("result") or {}
        for model in (result.get("modelUsage") or {}).values():
            f = failed[run]
            f["calls"] += 1
            f["output_tokens"] += model.get("outputTokens") or 0
            f["cache_creation"] += model.get("cacheCreationInputTokens") or 0
            f["cache_read"] += model.get("cacheReadInputTokens") or 0
            f["usd"] += model.get("costUSD") or 0
        if not result.get("modelUsage"):
            failed[run]["calls_without_usage"] += 1
    failed_usd = sum(f["usd"] for f in failed.values())
    rows += ["", "Failed calls (mostly HTTP 429 at the session limit), from their *.failed.json records:", "",
             "| Run | Failed calls with usage | Without usage | Output tokens | Cache writes | Cache reads | "
             "List-price USD |", "|---|---:|---:|---:|---:|---:|---:|"]
    for run, f in sorted(failed.items()):
        rows.append(f"| {run} | {f['calls']} | {f['calls_without_usage']} | {f['output_tokens']:,} | "
                    f"{f['cache_creation']:,} | {f['cache_read']:,} | {f['usd']:.2f} |")
    rows += ["", f"Total list-price estimate: ${total:.2f} for completed calls, ${failed_usd:.2f} for failed ones."]

    def usd(run):
        path = RUNS / run / "calls.jsonl"
        lines = path.read_text().splitlines() if path.exists() else []
        return sum(json.loads(x).get("cost_usd_list_price") or 0 for x in lines), len(lines)

    rows += ["", "| Arm | Generation USD (writer and reader, completed + failed calls) | Accepted | Per accepted scenario | "
             "Judge USD | Judge calls | Per judged trial |", "|---|---:|---:|---:|---:|---:|---:|"]
    for arm, (gen, solve) in YIELD_ARMS.items():
        g, _ = usd(gen)
        g += failed[gen]["usd"]
        j, calls = usd(f"{solve}_judged")
        acc = sum(x["status"] == "accepted" for x in outcomes(gen).values())
        rows.append(f"| {arm} | {g:.2f} | {acc or '-'} | {f'{g / acc:.2f}' if acc else '-'} | {j:.2f} | {calls} | "
                    f"{j / max(1, calls):.3f} |")
    return rows


def table_solver_tokens():
    """The solver's usage (Qwen on Purdue GenAI Studio), from each trial's usage_summary.json, retries included."""
    rows = ["## Solver tokens (Qwen `qwen3.8:27b` on Purdue GenAI Studio; every attempt, retries included)", "",
            "| Run | Attempts | Requests | Failed requests | Input tokens | Output tokens |",
            "|---|---:|---:|---:|---:|---:|"]
    for run in ("solve_dev_01", "solve_arm_r", "solve_arm_p", "solve_arm_p_v2", "solve_control"):
        c = Counter()
        for path in sorted((RUNS / run).glob("t*/usage_summary.json")):
            for a in load(path, {}).get("attempts", []):
                u = a.get("usage") or {}
                c["attempts"] += 1
                for k in ("total_requests", "failed_requests", "input_tokens", "output_tokens"):
                    c[k] += u.get(k) or 0
        if c["attempts"]:
            rows.append(f"| {run} | {c['attempts']} | {c['total_requests']:,} | {c['failed_requests']:,} | "
                        f"{c['input_tokens']:,} | {c['output_tokens']:,} |")
    return rows


def main():
    parts = [table_generation(), table_validity(), table_design(), table_runtime(), table_yield(), table_reproduction(),
             table_v1_v2(), table_judge(), table_tokens(), table_solver_tokens()]
    print("# Tables for report.md (generated by kit/tables.py)\n")
    for p in parts:
        print("\n".join(p) + "\n")


if __name__ == "__main__":
    main()
