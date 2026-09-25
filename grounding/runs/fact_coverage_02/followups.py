"""Analyses of the recorded trials that answer follow-up questions (no service calls); tables.py includes them.

- packed_vs_alone: the 8 B1 covers that are already "no target, all decoys, just tell me" against the one-decoy
  probes of the same decoys.
- run_budget: if every run (not every test) counted against the budget: new facts per run by kind of run, and fixed
  run budgets replayed on the recorded trials in order (t1, t2, t3).
- hidden_targets: what each target-present trial saw first, the backtest of the hiding rule, the wording check
  and the hidden-target pilot (method.md, "hidden-target tests").
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
PILOT = HERE.parent / "fact_coverage_01/pilot/cases"
FAIL = {"incorrect", "presented"}
TOLD_COVERS = ["BOX-02-TOLD", "BOX-04-TOLD", "BOX-06-TOLD", "CAL-03-TOLD", "CAL-05-TOLD", "CAL-08-TOLD", "LIN-02-TOLD",
               "LIN-04-TOLD"]
YIELD_ORDER = {"F8": 0, "F1": 1, "F6": 2, "F4": 3, "F5": 4, "F3": 5, "F2": 6, "F7": 7, "F0": 8}


def _facts(runs):
    out = set()
    for t, trial in runs:
        r = t["trials"].get(trial)
        if r and r["outcome"] in FAIL:
            out |= {x for x in r["exposed"] if not x.startswith("policy:")}
    return out


def packed_vs_alone(load):
    b1 = {t["case_id"]: t for t in load(["b1"])}
    probes = [t for t in load(["method_pilot"]) if t["form"] == "probe"]
    acted_packed = est_packed = acted_alone = est_alone = 0
    packed_facts, alone_facts, n_alone = set(), set(), 0
    for cid in TOLD_COVERS:
        scen = cid.replace("-TOLD", "")
        domain = {"B": "box", "C": "calendar", "L": "linear"}[scen[0]]
        cover = json.loads((PILOT / domain / f"{cid}.json").read_text())
        facts = [c["requirement"] for r in cover["references"] if not r["expected"] for c in r["claims"]]
        t = b1[cid]
        packed_facts |= set(t["exposed"])
        for fact in facts:
            acted_packed += sum(1 for r in t["trials"].values() if r["outcome"] in FAIL and fact in r["exposed"])
            est_packed += t["established"]
            for p in (x for x in probes if x["scenario"] == scen and x["fact"] == fact):
                n_alone += 1
                acted_alone += p["failures"]
                est_alone += p["established"]
                if p["failures"]:
                    alone_facts |= set(p["exposed"])
    return ["## Packed \"just tell me\" vs one decoy at a time (8 pilot scenarios)", "",
            "| Form | Tests | Distinct facts | Decoy-trials acted on |", "|---|---:|---:|---:|",
            f"| All decoys, no target, \"just tell me\" (B1 -TOLD covers) | {len(TOLD_COVERS)} | {len(packed_facts)} | "
            f"{acted_packed}/{est_packed} |",
            f"| One decoy per probe (same decoys) | {n_alone} | {len(alone_facts)} | {acted_alone}/{est_alone} |", "",
            f"Only packed: {sorted(packed_facts - alone_facts) or 'none'}. Only alone: {sorted(alone_facts - packed_facts)}.", ""]


def _fisher_ge(a, n1, b, n2):
    """One-sided hypergeometric P(first group gets >= a of the a+b failures | equal per-run rates)."""
    from math import comb
    k, n = a + b, n1 + n2
    if k == 0:
        return 1.0
    return sum(comb(n1, i) * comb(n2, k - i) for i in range(a, min(k, n1) + 1) if k - i <= n2) / comb(n, k)


def fact_probes_equal_runs(load):
    """Each fact probe given as many runs as its single-decoy probes had in total (3 per decoy): the original
    factprobe trials plus factprobe_extra, against the singles; per fact and in total."""
    suite = json.loads((HERE / "suite_factprobe.json").read_text())
    if not (HERE / "runs/factprobe_extra").exists():
        return []
    together = defaultdict(lambda: [0, 0, set()])
    for t in load(["factprobe", "factprobe_extra"]):
        c = together[t["case_id"]]
        c[0] += t["failures"]
        c[1] += t["established"]
        c[2] |= set(t["exposed"])
    singles = {t["case_id"]: t for t in load(["method_new", "method_new_lin25", "method_new_slk21", "method_pilot"])}
    out = ["## Fact probes at equal runs per fact", "",
           "| Fact probe | Fact | Together: failing/established runs | Alone: failing/established runs | "
           "p (together more) | p (alone more) |", "|---|---|---:|---:|---:|---:|"]
    f_t, f_a = set(), set()
    for s in suite:
        a, n1, _ = together[s["case_id"]]
        b = sum(singles[x]["failures"] for x in s["singles"])
        n2 = sum(singles[x]["established"] for x in s["singles"])
        if a:
            f_t.add(s["fact"])
        if b:
            f_a.add(s["fact"])
        out.append(f"| {s['case_id']} | `{s['fact']}` | {a}/{n1} | {b}/{n2} | {_fisher_ge(a, n1, b, n2):.3f} | "
                   f"{_fisher_ge(b, n2, a, n1):.3f} |")
    out += ["", f"Facts exposed together: {len(f_t)}; alone: {len(f_a)}; only together: {sorted(f_t - f_a) or 'none'}; "
                f"only alone: {sorted(f_a - f_t) or 'none'}.", ""]
    return out


def run_budget(load):
    sets = {
        "Pilot facts": ([t for t in load(["b1"]) if t["form"] in (None, "target-present layer")],
                        [t for t in load(["method_pilot"]) if t["form"] == "probe"], 200),
        "New facts": ([t for t in load(["method_new", "method_new_lin25", "method_new_slk21"]) if t["form"] == "cover control"],
                      [t for t in load(["method_new", "method_new_lin25", "method_new_slk21"]) if t["form"] == "probe"], 100),
    }
    pooled = {k: [0, set()] for k in ("First run of a probe", "Repeat of a probe (2nd or 3rd run)",
                                      "Cover run, counting only facts the probes did not find")}
    rows = defaultdict(dict)
    for label, (covers, probes, budget) in sets.items():
        ranked = sorted(probes, key=lambda t: YIELD_ORDER.get(t["family"], 9))
        first = [(t, "t1") for t in ranked]
        rep = [(t, "t2") for t in ranked] + [(t, "t3") for t in ranked]
        cov1 = [(t, "t1") for t in covers]
        covrep = [(t, "t2") for t in covers] + [(t, "t3") for t in covers]
        cov3 = [(t, tr) for t in covers for tr in ("t1", "t2", "t3")]
        for name, runs in [("Probes once each, then repeat probes", first + rep),
                           ("Probes once, covers once, then repeat probes", first + cov1 + rep),
                           ("Covers ×3, then probes once", cov3 + first),
                           ("Probes once, covers once, then repeat covers", first + cov1 + covrep),
                           ("Covers only, ×3", cov3)]:
            runs = [(t, tr) for t, tr in runs if tr in t["trials"]][:budget]
            rows[name][label] = (len(runs), len(_facts(runs)))
        f1 = _facts(first)
        fr = _facts(rep) - f1
        fc = _facts(cov3) - f1 - fr
        keys = list(pooled)
        pooled[keys[0]][0] += sum(1 for t, tr in first if tr in t["trials"])
        pooled[keys[0]][1] |= {(label, f) for f in f1}
        pooled[keys[1]][0] += sum(1 for t, tr in rep if tr in t["trials"])
        pooled[keys[1]][1] |= {(label, f) for f in fr}
        pooled[keys[2]][0] += sum(1 for t, tr in cov3 if tr in t["trials"])
        pooled[keys[2]][1] |= {(label, f) for f in fc}
    out = ["## Budget counted in runs", "", "| Use of a run (both fact sets pooled) | Runs | New facts | Per run |",
           "|---|---:|---:|---:|"]
    out += [f"| {k} | {n} | {len(fs)} | {len(fs) / n:.3f} |" for k, (n, fs) in pooled.items()]
    out += ["", "| Policy (runs used, facts) | Pilot facts, 200 runs | New facts, 100 runs |", "|---|---:|---:|"]
    for name, cells in rows.items():
        out.append(f"| {name} | " + " | ".join(f"{cells[k][1]} ({cells[k][0]} runs)" for k in sets) + " |")
    return out + ["", "Probes are ordered by family yield (F8, F1, F6, …), itself measured on these runs.", ""]


def _trial_class(run, case_id, trial):
    """What came first, the target or the test's hidden decoy (not the scenario's other decoys)."""
    from grounding.runs.fact_coverage_02.analyze import current
    from grounding.runs.fact_coverage_02.hiding import first_seen, hiding_class
    suite = {t["case_id"]: t for t in json.loads((HERE / "suite_hidden.json").read_text())}
    hidden = suite.get(case_id, {}).get("hidden_decoy")
    attempt = sorted((HERE / "runs" / run / trial / case_id).glob("attempt-*"))[-1]
    case = current(json.loads((attempt / "case.json").read_text()))
    refs = [r for r in case["references"] if r.get("claims") and r.get("expected")]
    if not refs:
        return "no target"
    return hiding_class(*first_seen(attempt, case, refs[0], only={hidden} if hidden else None))


OUTCOME_WORDS = {"incorrect": "acted on the decoy", "presented": "presented the decoy", "correct": "target",
                 "false_absence": "said none", "correct_absent": "said none"}


def _cell(t, trial, manual):
    r = t["trials"].get(trial)
    if not r:
        return "-"
    out = OUTCOME_WORDS.get(r["outcome"], r["outcome"])
    mech = (manual.get(f"{t['run']}/{trial}/{t['case_id']}") or {}).get("mechanism")
    if mech:
        out += f" ({mech})"
    if not t["case_id"].startswith("P-") and r["outcome"] not in ("not_established", "artifact"):
        out += f"; {_trial_class(t['run'], t['case_id'], trial)}"
    return out


def hidden_targets(load):
    from grounding.runs.fact_coverage_02.hiding import HIDDEN_HELD, backtest
    manual = json.loads((HERE / "manual_labels.json").read_text())
    rows, per_ref = backtest(load)
    counts = defaultdict(lambda: [0, 0])
    for r in rows:
        counts[r["class"]][0] += 1
        counts[r["class"]][1] += r["acted"]
    out = ["## Hidden targets: what the agent saw first (target-present covers)", "",
           "| First appearance of target and decoy ids | Trials | Acted on a decoy |", "|---|---:|---:|"]
    for k in ["decoy only", "decoy first", "together, decoy listed first", "together, target listed first",
              "target first", "target only", "neither seen"]:
        if counts[k][0]:
            out.append(f"| {k} | {counts[k][0]} | {counts[k][1]} |")
    confusion = defaultdict(list)
    for rid, v in sorted(per_ref.items()):
        seen = any(c.rstrip("*") in HIDDEN_HELD for c in v["classes"])
        confusion[(v["layout"]["strict"], seen)].append(rid.replace(".r1", ""))
    out += ["", "Backtest of the strict rule (a decoy on some easy path, no target on any) against what happened:", "",
            "| Rule marks the layout hidden | Decoy came back without the target in some trial | References |",
            "|---|---|---|"]
    for (strict, seen), refs in sorted(confusion.items(), key=lambda kv: (not kv[0][0], not kv[0][1])):
        shown = ", ".join(refs) if len(refs) <= 8 else f"{len(refs)} references"
        out.append(f"| {'yes' if strict else 'no'} | {'yes' if seen else 'no'} | {shown} |")
    if not (HERE / "runs/wording_check").exists():
        return out + [""]
    covers = {t["case_id"]: t for t in load(["b1", "method_new"])}
    out += ["", "## Wording check: the hidden-target covers plus \"If there isn't one, just tell me\"", "",
            "| Test | The cover without the clause | t1 | t2 | t3 |", "|---|---|---|---|---|"]
    for t in load(["wording_check"]):
        cover = covers[t["case_id"][3:]]
        before = f"{cover['failures']}/{cover['established']} acted on the decoy"
        out.append(f"| {t['case_id']} | {before} | " + " | ".join(_cell(t, k, manual) for k in ("t1", "t2", "t3")) + " |")
    if not (HERE / "runs/hidden_pilot").exists():
        return out + [""]
    pilot = {t["case_id"]: t for t in load(["hidden_pilot"])}
    probes = {t["case_id"]: t for t in load(["method_pilot"])}
    out += ["", "## Hidden-target pilot", "",
            "| Hidden-target test | Fact | t1 | t2 | t3 | Same decoy as a probe |", "|---|---|---|---|---|---|"]
    for cid, t in sorted(pilot.items()):
        if not cid.startswith("H-"):
            continue
        probe = pilot.get("P-" + cid[2:]) or probes.get("P-" + cid[2:])
        probe_cell = f"{probe['case_id']}: {probe['failures']}/{probe['established']} acted" if probe else "none"
        out.append(f"| {cid} | `{t.get('fact') or ''}` | " + " | ".join(_cell(t, k, manual) for k in ("t1", "t2", "t3"))
                   + f" | {probe_cell} |")
    return out + [""]
