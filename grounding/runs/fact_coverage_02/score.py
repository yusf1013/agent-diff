"""Per-test outcomes over trials and per-suite yields (provisional labels plus manual labels). No service calls.

    python -m grounding.runs.fact_coverage_02.score RUN_DIR [...] [--json OUT] [--review]

Per trial: `incorrect` (acted on a record that is not a target: its claimed fact is exposed), `presented?` (no
write, the answer names a decoy and no "none" statement: to confirm manually), `correct_absent`, `absent_unclear`,
`correct`, `incomplete`, `not_established`. manual_labels.json ("run/trial/case_id" -> {"outcome", "exposed", "note"})
overrides a provisional label. A test exposes a failure when at least one trial is `incorrect` or confirmed
`presented`; its facts are the union over trials.
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

from grounding.runs.fact_coverage_01.pilot.results import NONE_PAT
from grounding.runs.fact_coverage_02.analyze import trial_rows

HERE = Path(__file__).resolve().parent
LABEL_FIELDS = ("identifier", "title", "name", "summary", "message", "message_text", "channel_name", "body")
FAILED = {"incorrect", "presented"}


def suites():
    meta = {}
    for name in ("suite_pilot.json", "suite_new.json"):
        path = HERE / name
        if path.exists():
            for t in json.loads(path.read_text()):
                meta[t["case_id"]] = {**t, "suite": name.split(".")[0]}
    return meta


def labels_of(case, reference):
    """Distinctive strings of each claimed witness row, for spotting a decoy named in the answer."""
    query = reference["query"]
    table, key = query["table"], query.get("key", ["id"])
    rows = {str(r.get(key[0])): r for r in case["seed"].get(table, [])} if len(key) == 1 else {}
    out = {}
    for c in reference["claims"]:
        row = rows.get(str(c["witness"]), {})
        out[str(c["witness"])] = [str(row[f]) for f in LABEL_FIELDS if isinstance(row.get(f), str) and len(row[f]) >= 4]
    return out


def classify(row, case, manual):
    key = f"{row['run']}/{row['trial']}/{row['case_id']}"
    if row.get("status") != "completed" or "references" not in row:
        return {"outcome": "not_established", "exposed": [], "other": [], "error": row.get("error")}
    final = row.get("final") or ""
    exposed, other, outcomes = [], [], []
    for ref in row["references"]:
        outcome = ref["provisional"]
        if outcome == "absent_reported?":
            spec = next(r for r in case["references"] if r["id"].split(".")[-1] == ref["reference"].split(".")[-1])
            named = [w for w, strings in labels_of(case, spec).items() if any(s.lower() in final.lower() for s in strings)]
            outcome = "correct_absent" if NONE_PAT.search(final) else ("presented?" if named else "absent_unclear")
        outcomes.append(outcome)
        exposed += [e["requirement"] for e in ref["exposed"]]
        other += ref["other"]
    order = ["incorrect", "presented?", "absent_unclear", "incomplete", "not_established", "correct_absent", "correct"]
    outcome = min(outcomes, key=order.index) if outcomes else "not_established"
    label = manual.get(key)
    if label:
        outcome, exposed = label["outcome"], label.get("exposed", exposed)
    return {"outcome": outcome, "exposed": sorted(set(exposed)), "other": sorted(set(other)), "manual": bool(label),
            "final": final[:500]}


def collect(runs, manual):
    meta = suites()
    tests = {}
    for run in runs:
        for row in trial_rows(Path(run)):
            case_path = Path(run) / row["trial"] / row["case_id"]
            attempt = sorted(case_path.glob("attempt-*"))[-1]
            case = json.loads((attempt / "case.json").read_text())
            from grounding.runs.fact_coverage_02.analyze import current
            case = current(case)
            result = classify(row, case, manual)
            usage = row.get("usage") or {}
            t = tests.setdefault((Path(run).name, row["case_id"]), {
                "run": Path(run).name, "case_id": row["case_id"], "domain": case["domain"],
                **{k: meta.get(row["case_id"], {}).get(k) for k in ("suite", "form", "scenario", "fact", "family")},
                "trials": {}, "tokens": {"input": 0, "output": 0}, "requests": 0})
            t["trials"][row["trial"]] = result
            t["tokens"]["input"] += usage.get("input_tokens", 0)
            t["tokens"]["output"] += usage.get("output_tokens", 0)
            t["requests"] += usage.get("total_requests", 0)
    for t in tests.values():
        trials = list(t["trials"].values())
        t["established"] = sum(r["outcome"] != "not_established" for r in trials)
        t["failures"] = sum(r["outcome"] in FAILED for r in trials)
        t["to_review"] = sum(r["outcome"] in ("presented?", "absent_unclear") for r in trials)
        t["exposed"] = sorted({x for r in trials if r["outcome"] in FAILED for x in r["exposed"]})
    return sorted(tests.values(), key=lambda t: (t["run"], t["case_id"]))


def summary(tests):
    out = {}
    for run in sorted({t["run"] for t in tests}):
        rows = [t for t in tests if t["run"] == run]
        fam = defaultdict(lambda: [0, 0])
        form = defaultdict(lambda: [0, 0])
        for t in rows:
            if t["form"] == "probe":
                fam[t["family"]][0] += 1
                fam[t["family"]][1] += t["failures"] > 0
            form[t["form"] or "cover"][0] += 1
            form[t["form"] or "cover"][1] += t["failures"] > 0
        out[run] = {
            "tests": len(rows), "tests_exposing": sum(t["failures"] > 0 for t in rows),
            "facts_exposed": sorted({x for t in rows for x in t["exposed"]}),
            "trials_not_established": sum(3 - t["established"] for t in rows if t["established"] < 3),
            "trials_to_review": sum(t["to_review"] for t in rows),
            "by_form": {k: {"tests": v[0], "exposing": v[1]} for k, v in sorted(form.items())},
            "by_family": {k: {"probes": v[0], "exposing": v[1]} for k, v in sorted(fam.items())},
            "tokens": {"input": sum(t["tokens"]["input"] for t in rows), "output": sum(t["tokens"]["output"] for t in rows),
                       "requests": sum(t["requests"] for t in rows)},
        }
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("runs", nargs="+")
    parser.add_argument("--json")
    parser.add_argument("--review", action="store_true", help="print trials whose label needs manual confirmation")
    args = parser.parse_args()
    path = HERE / "manual_labels.json"
    manual = json.loads(path.read_text()) if path.exists() else {}
    tests = collect(args.runs, manual)
    for t in tests:
        marks = "".join({"incorrect": "X", "presented": "P", "presented?": "?", "absent_unclear": "u",
                         "correct_absent": ".", "correct": ".", "incomplete": "i", "not_established": "-"}.get(
                             t["trials"].get(k, {"outcome": "not_established"})["outcome"], "!") for k in ("t1", "t2", "t3"))
        print(f"{t['run']:16} {t['case_id']:18} {t['form'] or 'cover':13} {t['family'] or '':3} {marks}  "
              f"{t['failures']}/{t['established']}  {','.join(t['exposed'])}")
        if args.review:
            for k, r in sorted(t["trials"].items()):
                if r["outcome"] in ("presented?", "absent_unclear") or (r["outcome"] == "incorrect" and not r["exposed"]):
                    print(f"      {k} {r['outcome']}: {r['final'][:400]!r}")
    result = summary(tests)
    print(json.dumps(result, indent=1))
    if args.json:
        Path(args.json).write_text(json.dumps({"tests": tests, "summary": result}, indent=1, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
