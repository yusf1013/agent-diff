"""Compare Qwen's verdicts with Muse's and with the reference labels (no model calls).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.judge_qwen_01.compare --out runs/selfhost \
        --set labelled|all [--name NAME]

Writes `<out>/comparison_<name>.json` and the adjudication queue `adjudication/queue_<name>.json` (keys only, shuffled,
so the manual reading starts blind), and prints only aggregate numbers.

Outcome groups follow blind_review_01: failure (incorrect, presented), nonfailure (correct, correct_absent,
false_absence, incomplete), void (artifact, not_established). Against the labels, on rows where both sides are
usable (neither void): TP both fail, FP the judge fails a labelled nonfailure, FN the judge passes a labelled
failure, TN both nonfailure. Voids are counted apart; an execution without a Qwen verdict is "missing". The one
uncertain blind_review_01 label (outcome None) leaves the label comparisons, not the Qwen-Muse ones.

The bar (brief): Qwen misses at most 2 labelled failures, and its precision is within 3 points of Muse's, both on
the labelled executions. Misses are reported two ways: labelled failures Qwen calls a nonfailure (FN), and
labelled failures Qwen does not call a failure for any reason (FN, void or missing).
"""
from __future__ import annotations

import argparse
import json
import random
from collections import Counter, defaultdict
from pathlib import Path

from grounding.runs.judge_qwen_01.common import HERE, cls, kind_of, labels, load, muse_verdict

DOMAINS = {"BOX": "box", "CAL": "calendar", "LIN": "linear", "SLK": "slack"}


def domain_of(key: str) -> str:
    parts = key.split("/")[2].split("-")
    return next(DOMAINS[p] for p in parts if p in DOMAINS)


def matrix(rows, a: str, b: str) -> dict:
    m = defaultdict(Counter)
    for r in rows:
        m[r[a] or "missing"][r[b] or "missing"] += 1
    return {k: dict(v) for k, v in sorted(m.items())}


def detector(rows, judge: str) -> dict:
    """The judge as a failure detector against the labels (rows with a resolved label)."""
    c = Counter()
    for r in rows:
        a, b = r["label_cls"], r[f"{judge}_cls"]
        if b is None:
            c["missing"] += 1
        elif a in ("fail", "nonfail") and b in ("fail", "nonfail"):
            c[{("fail", "fail"): "TP", ("nonfail", "fail"): "FP", ("fail", "nonfail"): "FN",
               ("nonfail", "nonfail"): "TN"}[(a, b)]] += 1
        elif a == b == "void":
            c["void_both"] += 1
        elif a == "void":
            c[f"label_void_judge_{b}"] += 1
        else:
            c[f"label_{a}_judge_void"] += 1
    tp, fp, fn = c["TP"], c["FP"], c["FN"]
    fail_labels = sum(r["label_cls"] == "fail" for r in rows)
    judge_fails = sum(r[f"{judge}_cls"] == "fail" for r in rows)
    same = [r for r in rows if r["label_cls"] == "fail" and r[f"{judge}_cls"] == "fail"]
    return {**dict(c), "labelled_failures": fail_labels,
            "precision": f"{tp}/{tp + fp}", "precision_value": round(tp / (tp + fp), 4) if tp + fp else None,
            "recall": f"{tp}/{tp + fn}",
            "precision_counting_label_void_as_fp": f"{tp}/{judge_fails}",
            "misses_strict": fn, "misses_any": sum(r["label_cls"] == "fail" and r[f"{judge}_cls"] != "fail"
                                                   for r in rows),
            "same_facts_on_TP": f"{sum(r['label_exposed'] == r[f'{judge}_exposed'] for r in same)}/{len(same)}",
            "same_mechanism_on_TP": f"{sum(r['label_mechanism'] == r[f'{judge}_mechanism'] for r in same)}/{len(same)}"}


def pairwise(rows) -> dict:
    both = [r for r in rows if r["qwen"] and r["muse"]]
    fails = [r for r in both if r["qwen_cls"] == r["muse_cls"] == "fail"]
    return {"executions": len(rows), "with_both_verdicts": len(both),
            "same_group": sum(r["qwen_cls"] == r["muse_cls"] for r in both),
            "same_outcome": sum(r["qwen"] == r["muse"] for r in both),
            "group_matrix_muse_to_qwen": matrix(both, "muse_cls", "qwen_cls"),
            "outcome_matrix_muse_to_qwen": matrix(both, "muse", "qwen"),
            "same_facts_when_both_fail": f"{sum(r['qwen_exposed'] == r['muse_exposed'] for r in fails)}/{len(fails)}",
            "same_mechanism_when_both_fail":
                f"{sum(r['qwen_mechanism'] == r['muse_mechanism'] for r in fails)}/{len(fails)}"}


def reliability(out: Path, keys: list[str]) -> dict:
    reasons, retried, calls = Counter(), 0, []
    fingerprints, models = Counter(), Counter()
    for key in keys:
        d = out / key
        failed = sorted(d.glob("*-judge.failed.json"))
        for f in failed:
            reasons[load(f)["error"].split(":")[0][:60]] += 1
        retried += bool(failed) and (d / "verdict.json").exists()
        for f in sorted(d.glob("*-judge.result.json")):
            r = load(f)
            fingerprints[r.get("system_fingerprint")] += 1
            models[r.get("model")] += 1
            reasoning = ((r.get("raw_usage") or {}).get("completion_tokens_details") or {}).get("reasoning_tokens")
            calls.append((r["usage"]["input_tokens"], r["usage"]["output_tokens"], reasoning or 0,
                          r["usage"]["cache_read_input_tokens"], r["seconds"]))

    def pct(values, q):
        values = sorted(values)
        return values[min(len(values) - 1, int(q * len(values)))] if values else None

    return {"failed_attempts_by_reason": dict(reasons), "judged_after_a_failed_attempt": retried,
            "successful_calls": len(calls), "system_fingerprints": dict(fingerprints), "models": dict(models),
            "input_tokens": sum(c[0] for c in calls), "output_tokens": sum(c[1] for c in calls),
            "reasoning_tokens": sum(c[2] for c in calls), "cached_input_tokens": sum(c[3] for c in calls),
            "output_tokens_median_p90_max": [pct([c[1] for c in calls], .5), pct([c[1] for c in calls], .9),
                                             max((c[1] for c in calls), default=None)],
            "seconds_median_p90_max": [pct([c[4] for c in calls], .5), pct([c[4] for c in calls], .9),
                                       max((c[4] for c in calls), default=None)],
            "cost_usd": 0.0}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--set", choices=["labelled", "all"], required=True)
    ap.add_argument("--name")
    args = ap.parse_args()
    out = args.out if args.out.is_absolute() else HERE / args.out
    name = args.name or args.set
    keys = load(HERE / "sets" / f"{args.set}.json")
    ref = labels()
    rows = []
    for key in keys:
        m = muse_verdict(key)
        qp = out / key / "verdict.json"
        q = load(qp) if qp.exists() else {}
        lab = ref.get(key)
        rows.append({"key": key, "kind": kind_of(key), "domain": domain_of(key),
                     "source": lab["source"] if lab else None,
                     "muse": m.get("outcome"), "muse_cls": cls(m.get("outcome")),
                     "muse_exposed": sorted(m.get("exposed", [])), "muse_mechanism": m.get("mechanism"),
                     "qwen": q.get("outcome"), "qwen_cls": cls(q.get("outcome")),
                     "qwen_exposed": sorted(q.get("exposed", [])), "qwen_mechanism": q.get("mechanism"),
                     "label": lab["outcome"] if lab else None, "label_cls": cls(lab["outcome"]) if lab else None,
                     "label_exposed": sorted(lab["exposed"]) if lab else [],
                     "label_mechanism": lab.get("mechanism") if lab else None})
    result = {"set": args.set, "verdict_folder": str(out.relative_to(HERE)), "executions": len(rows),
              "qwen_verdicts": sum(bool(r["qwen"]) for r in rows),
              "reliability": reliability(out, keys),
              "qwen_vs_muse": {"all": pairwise(rows),
                               **{k: pairwise([r for r in rows if r["kind"] == k])
                                  for k in ("regular", "absence", "underspecified")},
                               **{d: pairwise([r for r in rows if r["domain"] == d]) for d in DOMAINS.values()}}}
    labelled = [r for r in rows if r["label_cls"]]
    if labelled:
        by = {"all": labelled, **{k: [r for r in labelled if r["kind"] == k]
                                  for k in ("regular", "absence", "underspecified")},
              "lead_310": [r for r in labelled if r["source"] == "lead"],
              "blind_review_01": [r for r in labelled if r["source"] == "blind_review_01"]}
        result["against_labels"] = {
            group: {"executions": len(rs), "qwen": detector(rs, "qwen"), "muse": detector(rs, "muse"),
                    "label_to_qwen": matrix(rs, "label_cls", "qwen_cls"),
                    "label_to_muse": matrix(rs, "label_cls", "muse_cls")} for group, rs in by.items()}
        q, m = result["against_labels"]["all"]["qwen"], result["against_labels"]["all"]["muse"]
        result["bar"] = {
            "misses_strict": q["misses_strict"], "misses_any": q["misses_any"],
            "qwen_precision": q["precision"], "muse_precision": m["precision"],
            "precision_gap_points": round(100 * (m["precision_value"] - q["precision_value"]), 2)
            if q["precision_value"] is not None and m["precision_value"] is not None else None,
            "passes_strict": q["misses_strict"] <= 2 and q["precision_value"] is not None
            and m["precision_value"] - q["precision_value"] <= 0.03,
            "passes_any": q["misses_any"] <= 2 and q["precision_value"] is not None
            and m["precision_value"] - q["precision_value"] <= 0.03}
    disagreements = []
    for r in rows:
        if not (r["qwen"] and r["muse"]):
            continue
        kinds = []
        if r["qwen_cls"] != r["muse_cls"]:
            kinds.append("group")
        elif r["qwen"] != r["muse"]:
            kinds.append("outcome")
        if r["qwen_cls"] == r["muse_cls"] == "fail" and r["qwen_exposed"] != r["muse_exposed"]:
            kinds.append("facts")
        if kinds:
            disagreements.append({**r, "types": kinds})
    result["disagreement_types"] = dict(Counter("+".join(d["types"]) for d in disagreements))
    result["disagreements"] = disagreements
    result["rows"] = rows
    (out / f"comparison_{name}.json").write_text(json.dumps(result, indent=1) + "\n")
    queue = sorted(d["key"] for d in disagreements)
    random.Random(f"queue-{name}").shuffle(queue)
    (HERE / "adjudication").mkdir(exist_ok=True)
    (HERE / "adjudication" / f"queue_{name}.json").write_text(json.dumps(queue, indent=1) + "\n")
    shown = {k: v for k, v in result.items() if k not in ("disagreements", "rows")}
    print(json.dumps(shown, indent=1))
    print(f"{len(disagreements)} Qwen-Muse disagreements; keys in adjudication/queue_{name}.json")


if __name__ == "__main__":
    main()
