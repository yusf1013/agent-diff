"""Every table of autogen_02's report, generated from the run data.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.kit.tables > grounding/runs/autogen_02/tables.md
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

from grounding.runs.autogen_02.kit import policy_analysis
from grounding.runs.autogen_02.kit.sampler import FAIL, PASS, lower_bound, upper_bound

STUDY = Path(__file__).resolve().parents[1]
RUNS = STUDY / "runs"


def md(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def bounds(k, n):
    return f"[{lower_bound(k, n):.2f}, {upper_bound(k, n):.2f}]" if n else "-"


def phase1():
    res = policy_analysis.analyse()
    out = ["## Phase 1: the per-fact policy variants of fact_coverage_02's 18 scenarios (my labels)\n"]
    rows = []
    for mode in ("absence", "underspecified", "clone"):
        for domain in ("box", "calendar", "linear", "slack"):
            fs = [f for f in res["facts"] if f["mode"] == mode and f["domain"] == domain]
            if not fs:
                continue
            t1 = [f["t1"] in FAIL for f in fs if f["t1"] in FAIL | PASS]
            spread = Counter(f"{f['fails']}/3" for f in fs if f["usable"] == 3)
            rows.append([mode, domain, len(fs), f"{sum(f['fails'] for f in fs)}/{sum(f['usable'] for f in fs)}",
                         f"{sum(t1)}/{len(t1)}", bounds(sum(t1), len(t1)),
                         ", ".join(f"{k}: {v}" for k, v in sorted(spread.items(), reverse=True))])
    out.append(md(["Mode", "Domain", "Variants", "Failing trials", "Trial 1 fails", "90% bounds (t1)",
                   "Variants by failures in 3 trials"], rows))
    for mode, against in (("absence", "the fact's probes"), ("underspecified", "the scenario's cover"),
                          ("clone", "the scenario's cover")):
        readings = Counter(f.get("reading") for f in res["facts"] if f["mode"] == mode)
        if readings:
            out.append(f"\n**The pair reading, {mode}** (against {against} in autogen_01's same-day control run, 3 "
                       "trials each): " + ", ".join(f"{k}: {v}" for k, v in readings.most_common()) + ".")
    out.append("")
    under = [f for f in res["facts"] if f["mode"] == "underspecified"]
    if under:
        by_count = defaultdict(lambda: [0, 0, 0])
        for f in under:
            k = f.get("other_near_misses")
            by_count[k][0] += 1
            by_count[k][1] += f["fails"]
            by_count[k][2] += f["usable"]
        out.append("\n**Amendment 1 §2 (decision D7): failures of the drop-F variants by the number of other near misses "
                   "kept in the seed as distractors.**\n")
        out.append(md(["Other near misses in the seed", "Variants", "Failing trials"],
                      [[k, v[0], f"{v[1]}/{v[2]}"] for k, v in sorted(by_count.items(), key=lambda kv: str(kv[0]))]))
        out.append("")
    rows = [[f["variant"], f["fact"], f.get("family") or "", f"{f['fails']}/{f['usable']}",
             f"{f.get('probe_fails', '')}/{f.get('probe_n', '')}" if f["mode"] == "absence" else
             f"cover {f.get('cover_fails', '')}/{f.get('cover_n', '')}",
             f.get("reading", "") if f["mode"] == "absence" else f"{f.get('reading', '')}; {f.get('matches')} "
             f"matches, {f.get('other_near_misses')} other near misses"] for f in res["facts"]]
    out.append(md(["Variant", "Fact", "Family", "Fails", "Probe or cover fails", "Reading; match set"], rows))
    return "\n".join(out)


def actions_table():
    """What the policy trials did, from the state diff, over the usable trials (void ones by my label, or by judge
    v2's verdict when I have no label, are left out)."""
    void = {"artifact", "not_established"}
    outcome = {}
    for path in RUNS.glob("judge2_phase*/*/*/*/verdict.json"):
        v = json.loads(path.read_text())
        outcome[v["key"]] = v.get("outcome")
    outcome.update({k: v["outcome"] for k, v in policy_analysis.labels().items()})
    cats = ("near miss", "other record", "one match", "some matches", "all matches", "no change")
    rows = []
    for run in ("phase1/solve_absence", "phase1/solve_under", "phase1/solve_clone", "phase3/solve_absence_look1",
                "phase3/solve_underspecified_look1", "phase3/solve_absence_look2", "phase3/solve_underspecified_look2"):
        folder = RUNS / run
        if not folder.exists():
            continue
        got = {k: c for k, c in policy_analysis.actions(folder).items() if outcome.get(k) not in void}
        n = Counter(got.values())
        rows.append([run, len(got)] + [n.get(c, 0) for c in cats])
    return ("## What the policy trials did (state diff, first reference; usable trials)\n\n"
            + md(["Run", "Trials"] + list(cats), rows)
            + "\n\n\"no change\" covers asking, reporting that nothing matches, and giving up alike; the verdicts "
              "tell them apart.")


def construction():
    out = ["## Construction: how many policy variants derive\n"]
    rows = []
    idx = json.loads((RUNS / "phase1" / "index.json").read_text())
    by_form = defaultdict(Counter)
    for v in idx.values():
        by_form[v.get("form")]["accepted" if v.get("accepted") else "not"] += 1
    for form, c in by_form.items():
        rows.append(["exemplars (Phase 1, by hand)", form, c["accepted"], c["not"]])
    for name, form in (("phase3_dropf", "underspecified (automated)"), ("phase3_clone", "clone (automated)"),
                       ("phase2_cal2_dropf", "underspecified (automated, exemplars, cal2)")):
        folder = RUNS / name
        if folder.exists():
            st = Counter(json.loads(p.read_text())["status"] for p in folder.glob("*/record.json"))
            rows.append([name, form, st.get("accepted", 0), ", ".join(f"{k} {v}" for k, v in st.items()
                                                                      if k != "accepted")])
    out.append(md(["Source", "Variant", "Derived", "Not derived"], rows))
    return "\n".join(out)


def phase3():
    out = ["## Phase 3: sampled policy tests on autogen_01's 49 generated scenarios (judge v2)\n"]
    rows = []
    for mode in ("absence", "underspecified"):
        path = RUNS / "phase3" / f"decisions_{mode}.json"
        if not path.exists():
            out.append(f"({mode}: no decisions yet)")
            continue
        for cell, d in json.loads(path.read_text()).items():
            rows.append([cell, d["valid_units"], d["look_reached"], f"{d['failures']}/{d['draws']}",
                         f"[{d['lower_90']:.2f}, {d['upper_90']:.2f}]", d["decision"],
                         ", ".join(f"{k}: {v}" for k, v in sorted(d["spread"].items(), reverse=True))])
    if rows:
        out.append(md(["Cell", "Valid units", "Look", "Failures (one draw per unit)", "90% bounds", "Decision",
                       "Units by failures in 3 trials"], rows))
    return "\n".join(out)


def generation():
    out = ["## Phase 4: generation on Muse\n"]
    folder = RUNS / "phase4_gen"
    rows = []
    for o in sorted(folder.glob("G4-*/outcome.json")):
        d = json.loads(o.read_text())
        cost = 0.0
        calls = folder / "calls.jsonl"
        rows.append([d["scenario_id"], d["status"], d["versions"], d["check_rounds"], d["reader_rounds"],
                     d.get("seconds")])
    errors = sorted(p.parent.name for p in folder.glob("G4-*/error.txt"))
    out.append(md(["Scenario", "Status", "Versions", "Check rounds", "Reader rounds", "Seconds"], rows))
    if errors:
        out.append(f"\nEnded with an error (no outcome): {', '.join(errors)}.")
    st = Counter(r[1] for r in rows)
    out.append(f"\n{len(rows)} briefs with an outcome: " + ", ".join(f"{k} {v}" for k, v in st.items()) + ".")
    by = defaultdict(lambda: [0.0, 0.0, 0])
    calls = folder / "calls.jsonl"
    if calls.exists():
        for line in calls.read_text().splitlines():
            r = json.loads(line)
            b = by[r.get("label")]
            b[0] += r.get("cost_usd_list_price") or 0
            b[1] += r.get("cost_usd_billed") or 0
            b[2] += 1
        acc = [r[0] for r in rows if r[1] == "accepted"]
        tot_list = sum(v[0] for v in by.values())
        tot_billed = sum(v[1] for v in by.values())
        out.append(f"Generation cost: ${tot_list:.2f} at list price, ${tot_billed:.3f} billed, for {len(acc)} accepted "
                   f"scenarios (${tot_list / max(len(acc), 1):.2f} and ${tot_billed / max(len(acc), 1):.3f} per "
                   "accepted scenario, failed briefs included).")
    return "\n".join(out)


def phase4_scores():
    out = ["## Phase 4: yield of the generated suites on Qwen\n"]
    rows = []
    for path in sorted((RUNS / "phase4").glob("*.score.json")):
        s = json.loads(path.read_text())
        a = s.get("all", {})
        rows.append([path.stem.replace(".score", ""), a.get("tests"), a.get("trials"), len(a.get("facts_detect3", [])),
                     len(a.get("facts_detect1", [])), len(a.get("facts_detect3_uncontested", [])),
                     a.get("yield_per_test"), a.get("void_trials")])
        forms = {k.split(":", 1)[1]: v for k, v in s.get("by", {}).items() if k.startswith("form:")}
        for form, v in forms.items():
            rows.append([f"  {form}", v["tests"], v["trials"], len(v["facts_detect3"]), len(v["facts_detect1"]),
                         len(v.get("facts_detect3_uncontested", [])), v["yield_per_test"], v["void_trials"]])
    if rows:
        out.append(md(["Run / form", "Tests", "Trials", "Facts exposed (3 trials)", "Facts exposed (trial 1)",
                       "Uncontested", "Facts per test", "Void trials"], rows))
    else:
        out.append("(no scored run yet)")
    return "\n".join(out)


def costs():
    out = ["## Muse usage per run (tokens and cost at list and billed rates)\n"]
    rows = []
    for calls in sorted(RUNS.glob("*/calls.jsonl")):
        n = inp = cached = outp = 0
        lst = billed = secs = 0.0
        for line in calls.read_text().splitlines():
            r = json.loads(line)
            n += 1
            inp += r.get("input_tokens") or 0
            cached += r.get("cache_read_input_tokens") or 0
            outp += r.get("output_tokens") or 0
            lst += r.get("cost_usd_list_price") or r.get("total_cost_usd") or 0
            billed += r.get("cost_usd_billed") or 0
            secs += r.get("seconds") or 0
        rows.append([calls.parent.name, n, f"{inp:,}", f"{cached:,}", f"{outp:,}", f"${lst:.2f}", f"${billed:.3f}",
                     f"{secs / 3600:.1f}"])
    out.append(md(["Run", "Calls", "Input tokens", "Cached", "Output tokens", "List", "Billed", "Agent hours"],
                  rows))
    return "\n".join(out)


def main():
    print("# autogen_02 tables\n\nGenerated by `kit/tables.py` from the run data.\n")
    for section in (phase1, actions_table, construction, phase3, generation, phase4_scores, costs):
        try:
            print(section())
        except Exception as exc:  # a section whose data is not there yet
            print(f"(section {section.__name__} unavailable: {exc})")
        print()


if __name__ == "__main__":
    main()
