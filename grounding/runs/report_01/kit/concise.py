"""Read-only recomputation for report_concise.md; writes only numbers/concise.json.

Run with the same Python/PYTHONPATH as the other report kit modules. No model calls.
The baseline worktree is read if its unmerged evidence is absent from main.
"""
from __future__ import annotations

import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path

from grounding.runs.report_01.kit.common import (
    DOMAINS, RUNS, WRITERS, catalog, load, suite_tests, valid_claims,
)
from grounding.runs.report_01.kit import beyond
from grounding.runs.report_01.kit.exposure import totals
from grounding.runs.openclaw_eval_01 import policy, rulings

HERE = Path(__file__).resolve().parents[1]
OC = RUNS / "openclaw_eval_01/runs"
REPO = RUNS.parents[1]


def writer(m):
    return "Muse" if WRITERS[m["source"]].startswith("Muse") else "Sonnet"


def cls(o):
    return "fail" if o in {"incorrect", "presented"} else "pass" if o in {"correct", "correct_absent"} else "void"


def expected_union(sets, n=12):
    """Exact expected distinct facts in a uniform sample without replacement."""
    counts = Counter(f for s in sets for f in s)
    N = len(sets)
    assert N >= n
    return sum(1 - (math.comb(N-k, n) / math.comb(N, n) if N-k >= n else 0) for k in counts.values())


def main():
    rows = [(m, c) for m, c in suite_tests() if not rulings.test_exclusion(c)]
    meta = {m["case_id"]: m for m, _ in rows}
    final = load(OC / "final_regular_with_6b.json")["tests"]
    assert set(meta) == {t["case_id"] for t in final}
    cat = catalog()
    groups = {}
    for w in ("Sonnet", "Muse"):
        rs = [(m, c) for m, c in rows if writer(m) == w]
        covered = {d: sorted({f for m, c in rs if c["domain"] == d
                              for f, _, _ in valid_claims(c) if f in cat[d]}) for d in DOMAINS}
        groups[w] = {"forms": dict(Counter(m["form"] for m, c in rs)), "coverage": covered,
                     "exposure": totals([r for r in final if writer(meta[r["case_id"]]) == w])}

    # The final manifest chooses a specific execution, never just a case ID.
    attempts = {}
    for a, key, form in beyond.regular_trials():
        attempts[key] = {"path": a, "kind": "regular", "form": form}
    units = {mode: [u for seq in policy.population_plan(mode)["cells"].values()
                    for u in policy.population_units(seq)[0]] for mode in ("absence", "underspecified")}
    for a, _, mode in beyond.policy_trials():
        unit = a.parent.name
        assert unit in {u["unit"] for u in units[mode]}
        key = "/".join(a.relative_to(OC / "policy").parts[:3])
        assert key not in attempts
        attempts[key] = {"path": a, "kind": mode}
    assert Counter(v["kind"] for v in attempts.values()) == {"regular": 1695, "absence": 732, "underspecified": 591}
    assert len({(v["kind"], v["path"].parent.name) for v in attempts.values()}) == 1006

    scenario_writer = {m["scenario"]: writer(m) for m, c in rows}
    policy_by_writer = {}
    for mode, us in units.items():
        policy_by_writer[mode] = dict(Counter(scenario_writer[u["scenario"]] for u in us))

    # Retain only blind labels and verdicts on final selected executions.
    labels = {}
    for f in (RUNS / "openclaw_eval_01/eval").glob("labels_*/*_blind.json"):
        for key, v in load(f).items():
            if key in attempts and isinstance(v, dict):
                assert key not in labels
                labels[key] = v
    verdicts = {}
    for key, rec in attempts.items():
        run = key.split("/")[0]
        folder = OC / f"judged_{run}" if rec["kind"] == "regular" else OC / "policy" / run.replace("solve_", "judged_", 1)
        p = folder / key / "verdict.json"
        if p.exists():
            verdicts[key] = load(p)
    accuracy, mechanisms = defaultdict(Counter), defaultdict(Counter)
    asks = Counter()
    for key, label in labels.items():
        v = verdicts[key]
        kind = attempts[key]["kind"]
        a, b = cls(label["outcome"]), cls(v["outcome"])
        for group in (kind, "all"):
            c = accuracy[group]
            c["trials"] += 1
            c["agree"] += a == b
            name = {("fail", "fail"): "TP", ("pass", "pass"): "TN", ("pass", "fail"): "FP",
                    ("fail", "pass"): "FN", ("void", "void"): "void_both"}.get((a, b))
            c[name or ("label_void_only" if a == "void" else "judge_void_only")] += 1
            if a == b == "fail":
                c["same_facts_of"] += 1
                c["same_facts"] += set(label.get("exposed", [])) == set(v.get("exposed", []))
        if a == "fail":
            mechanisms[kind][label.get("mechanism") or "?"] += 1
        if kind == "underspecified" and a == "pass":
            asks["passing"] += 1
            asks["asking"] += bool(re.search(r"\bask", label.get("note", ""), re.I))

    note_hits = defaultdict(Counter)
    for v in verdicts.values():
        note = f"{v.get('note') or ''} {v.get('artifact_reason') or ''}"
        for category, rx in beyond.NOTE_CATEGORIES.items():
            if re.search(rx, note, re.I):
                note_hits[category][v["outcome"]] += 1

    base = RUNS / "baselines_01"
    if not base.exists():
        base = REPO / ".claude/worktrees/baselines-01/grounding/runs/baselines_01"
    # Same 48-test budget, now drawing from all Muse tests and using final outcomes.
    by_id = {t["case_id"]: t for t in final}
    ours = Counter()
    for d in DOMAINS:
        rs = [(m, c) for m, c in rows if c["domain"] == d and writer(m) == "Muse"]
        ours["facts_covered"] += expected_union([{f for f, _, _ in valid_claims(c)} for m, c in rs])
        ours["designated_facts_covered"] += expected_union([{f for f, _, fam in valid_claims(c) if fam != "F0"} for m, c in rs])
        for field in ("exposed", "exposed_t1"):
            ours[field] += expected_union([set(by_id[m["case_id"]][field]) for m, c in rs])
        ours["tests_exposing"] += 12 * sum(bool(by_id[m["case_id"]]["exposed"]) for m, c in rs) / len(rs)

    # Judge comparisons have a smaller intersection with the final manifest.
    jb = RUNS / "judge_baselines_01"
    judge_comparison = defaultdict(Counter)
    retained_comparison_keys = []
    for item in load(jb / "trials.json"):
        if not item["key"].startswith("openclaw_eval_01/") or item["truth"] is None:
            continue
        key = item["key"].removeprefix("openclaw_eval_01/")
        if key not in attempts:
            continue
        retained_comparison_keys.append(item["key"])
        predictions = {"judge_v2": item["v2_says_mistake"]}
        for name, folder in (("J0", jb / "runs/j0"), ("J1", jb / "runs/j1"), ("plain", base / "q4/plain_openclaw")):
            p = folder / item["key"] / "verdict.json"
            predictions[name] = load(p).get("mistake") if p.exists() else None
        for name, says in predictions.items():
            c = judge_comparison[name]
            c["trials"] += 1
            c["label_fail"] += bool(item["truth"])
            c["missing_or_void" if says is None else ("TP" if says else "FN") if item["truth"] else ("FP" if says else "TN")] += 1

    usage = load(HERE / "numbers/qwen_usage.json")["opening_table_scope"]
    estimate = {k: usage[k] * 3018 / 4464 for k in ("input_tokens", "output_tokens", "cached_input_tokens",
                                                   "cache_creation_input_tokens", "total_tokens")}
    estimate["uncached_input_tokens"] = estimate["input_tokens"] - estimate["cached_input_tokens"]
    estimate["method"] = "Historical token averages multiplied by 3018/4464; not an exact final-execution audit."

    out = {"scope": "Final 1006 methodology cases, 3018 executions; final outcomes only.",
           "writers": groups, "policy_by_scenario_writer": policy_by_writer,
           "judge_accuracy": {k: dict(v) for k, v in accuracy.items()},
           "judge_verdicts_on_final_executions": len(verdicts),
           "manual_failure_mechanisms": {k: dict(v) for k, v in mechanisms.items()},
           "underspecified_asking": dict(asks),
           "judge_notes_on_final_executions": {k: dict(v) for k, v in note_hits.items()},
           "equal_budget_muse_final": dict(ours),
           "judge_comparison_final": {k: dict(v) for k, v in judge_comparison.items()},
           "judge_comparison_keys": retained_comparison_keys,
           "baseline_comparison": load(base / "compare.json"), "baseline_policy_facts": load(base / "policy_facts.json"),
           "token_estimate": estimate,
           "final_execution_keys": sorted(attempts), "blind_label_keys": sorted(labels)}
    dest = HERE / "numbers/concise.json"
    dest.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k not in {"baseline_comparison", "baseline_policy_facts",
                                                            "final_execution_keys", "blind_label_keys", "judge_comparison_keys"}}, indent=2))


if __name__ == "__main__":
    main()
