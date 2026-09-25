"""Per-test outcomes over trials and per-suite yields (provisional labels plus manual labels). No service calls.

    python -m grounding.runs.fact_coverage_02.score RUN_DIR [...] [--json OUT] [--review]

Per trial: `incorrect` (acted on a record that is not a target: its claimed fact is exposed), `attempted?` (a write
command names a decoy but the state did not change), `presented?` (no write, the answer names a decoy and no "none"
statement), `correct_absent`, `absent_unclear`,
`correct`, `incomplete`, `not_established`. manual_labels.json ("run/trial/case_id" -> {"outcome", "exposed", "note"})
overrides a provisional label; a manual `artifact` (the replica, not the agent, caused the outcome) is not established. A test exposes a failure when at least one trial is `incorrect` or confirmed
`presented`; its facts are the union over trials.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

from grounding.runs.fact_coverage_01.pilot.results import NONE_PAT
from grounding.runs.fact_coverage_02.analyze import trial_rows

HERE = Path(__file__).resolve().parent
LABEL_FIELDS = ("identifier", "title", "name", "summary", "message", "message_text", "channel_name", "body")
FAILED = {"incorrect", "presented"}
REST_WRITE = re.compile(r"(-X|--request)\s*['\"]?(POST|PUT|PATCH|DELETE)")
WRITES = {"linear": re.compile(r"\bmutation\b"), "box": REST_WRITE, "calendar": REST_WRITE,
          "slack": re.compile(r"chat\.(postMessage|update|delete)|reactions\.(add|remove)|"
                              r"conversations\.(setTopic|invite|archive|unarchive|rename|kick|create|join|leave)")}


def attempted(case, attempt, reference):
    """Claimed witnesses named in a write command (a write the service rejected leaves no diff)."""
    records = [p for p in (attempt / "solver").glob("*.json") if p.name != "config.json"]
    if not records:
        return []
    steps = json.loads(records[0].read_text()).get("steps", [])
    writes = [str(s.get("action")) for s in steps if WRITES[case["domain"]].search(str(s.get("action") or ""))]
    query = reference["query"]
    table, key = query["table"], query.get("key", ["id"])
    rows = {str(r.get(key[0])): r for r in case["seed"].get(table, [])} if len(key) == 1 else {}
    hits = []
    for c in reference["claims"]:
        w = str(c["witness"])
        handles = [w] + ([str(rows[w]["identifier"])] if rows.get(w, {}).get("identifier") else [])
        if any(re.search(r"(?<![\w.-])" + re.escape(h) + r"(?![\w-])", cmd) for h in handles for cmd in writes):
            hits.append(w)
    return hits


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


PRIORITY = {"urgent": 1, "high": 2, "medium": 3, "normal": 3, "low": 4}  # Linear's scale: 1 is the most urgent


def value_errors(case, attempt):
    """Written values that contradict the request (reported apart from grounding): Linear's priority scale."""
    m = re.search(r"priority to (\w+)", case["prompt"], re.I)
    diff_path = attempt / "environment" / "diff_run.json"
    if case["domain"] != "linear" or not m or m.group(1).lower() not in PRIORITY or not diff_path.exists():
        return []
    want = PRIORITY[m.group(1).lower()]
    diff = json.loads(diff_path.read_text()).get("diff", {})
    return [f"A:Issue.priority (wrote {u['after']['priority']} for {m.group(1)} on {u['after']['id']})"
            for u in diff.get("updates", []) if u.get("__table__") == "issues"
            and u["after"].get("priority") != u["before"].get("priority") and u["after"].get("priority") != want]


def classify(row, case, manual, attempt):
    key = f"{row['run']}/{row['trial']}/{row['case_id']}"
    if row.get("status") != "completed" or "references" not in row:
        return {"outcome": "not_established", "exposed": [], "other": [], "error": row.get("error")}
    final = row.get("final") or ""
    exposed, other, outcomes = [], [], []
    no_match = any(r["use"] == "target" and not r["expected"] for r in case["references"])
    for ref in row["references"]:
        outcome = ref["provisional"]
        spec = next(r for r in case["references"] if r["id"].split(".")[-1] == ref["reference"].split(".")[-1])
        if not spec["claims"] and outcome != "incorrect":
            continue  # an input reference (no decoys) only matters when a wrong record was acted on
        if no_match and spec["expected"] and outcome in ("incomplete", "correct"):
            continue  # another reference has no match, so this one's action is not expected
        if outcome == "absent_reported?":
            named = [w for w, strings in labels_of(case, spec).items() if any(s.lower() in final.lower() for s in strings)]
            outcome = "correct_absent" if NONE_PAT.search(final) else ("presented?" if named else "absent_unclear")
        if outcome != "incorrect" and attempted(case, attempt, spec):
            outcome = "attempted?"  # a write named a decoy but changed nothing: confirm from the trajectory
        outcomes.append(outcome)
        exposed += [e["requirement"] for e in ref["exposed"]]
        other += ref["other"]
    order = ["incorrect", "attempted?", "presented?", "absent_unclear", "incomplete", "not_established", "correct_absent",
             "correct"]
    outcome = min(outcomes, key=order.index) if outcomes else "not_established"
    label = manual.get(key)
    if label:
        outcome, exposed = label["outcome"], label.get("exposed", exposed)
    return {"outcome": outcome, "exposed": sorted(set(exposed)), "other": sorted(set(other)), "manual": bool(label),
            "value_errors": value_errors(case, attempt), "final": final[:500]}


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
            result = classify(row, case, manual, attempt)
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
        t["established"] = sum(r["outcome"] not in ("not_established", "artifact") for r in trials)
        t["failures"] = sum(r["outcome"] in FAILED for r in trials)
        t["to_review"] = sum(r["outcome"] in ("attempted?", "presented?", "absent_unclear") for r in trials)
        t["exposed"] = sorted({x for r in trials if r["outcome"] in FAILED for x in r["exposed"]})
        t["value_failures"] = sum(bool(r.get("value_errors")) for r in trials)
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
            "value_failures": {t["case_id"]: t["value_failures"] for t in rows if t["value_failures"]},
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
        marks = "".join({"incorrect": "X", "presented": "P", "presented?": "?", "attempted?": "a", "absent_unclear": "u",
                         "correct_absent": ".", "correct": ".", "incomplete": "i", "not_established": "-",
                         "artifact": "A"}.get(
                             t["trials"].get(k, {"outcome": "not_established"})["outcome"], "!") for k in ("t1", "t2", "t3"))
        print(f"{t['run']:16} {t['case_id']:18} {t['form'] or 'cover':13} {t['family'] or '':3} {marks}  "
              f"{t['failures']}/{t['established']}  {','.join(t['exposed'])}"
              + (f"  [value errors in {t['value_failures']} trials]" if t["value_failures"] else ""))
        if args.review:
            for k, r in sorted(t["trials"].items()):
                if r["outcome"] in ("attempted?", "presented?", "absent_unclear") or (
                        r["outcome"] == "incorrect" and not r["exposed"]):
                    print(f"      {k} {r['outcome']}: {r['final'][:400]!r}")
    result = summary(tests)
    print(json.dumps(result, indent=1))
    if args.json:
        Path(args.json).write_text(json.dumps({"tests": tests, "summary": result}, indent=1, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
