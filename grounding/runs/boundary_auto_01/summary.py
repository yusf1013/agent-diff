"""The boundary automation's numbers, in the PI's terms, from the saved outputs.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.boundary_auto_01.summary

- The coverage space: the 93 faithful boundaries of boundary_02 (the phase-1 derivation, taken as input).
- Tests generated (the writer's requests) and valid (the cold reader agreed: the record, no hint, natural wording).
- The generated specs' agreement with the hand specs on the graded phase-1 trials (specs.json).
- Phase 3: the automated tests' verdicts (grades-p3a.json, grades-p3b.json) on valid tests; the failures exposed
  (elements with a failing trial), and pass rates by the alternative the actor had, beside phase 1's hand-worded
  tests on the same elements (boundary_02's oracle verdicts).
- The judge's true and false positives and false negatives from review.json (my review of a sample).
- Muse tokens and cost; the solver's tokens.
Writes summary.json and prints it.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
BD2 = HERE.parent / "boundary_02"


def load(p, default):
    return json.loads(p.read_text()) if p.exists() else default


def main():
    space = {r["id"]: r for r in json.loads((BD2 / "space.json").read_text()) if r["verdict"] == "faithful"}
    writer, reader, specs = load(HERE / "writer.json", {}), load(HERE / "reader.json", {}), load(HERE / "specs.json", {})
    review = load(HERE / "review.json", {})
    valid = {e for e, v in reader.items() if v.get("agreed")}
    auto = {}
    for name in ("grades-p3a.json", "grades-p3b.json"):
        auto.update(load(HERE / name, {}))
    manual = {}
    for f in ("oracle-verdicts.json", "oracle-c5.json", "oracle-c6.json"):
        for k, v in load(BD2 / f, {}).items():
            if not v["oracle"].startswith("void"):
                manual[k] = v["oracle"]
    by_kind = defaultdict(lambda: {"auto": Counter(), "manual": Counter(), "elements": set()})
    failing, review_needed, fail_kinds = set(), 0, defaultdict(set)
    read = (review.get("trials") or {}) if isinstance(review, dict) else {}
    for trial, v in auto.items():
        eid = trial.split("/")[1].removeprefix("BDA-")
        if eid not in valid:
            continue
        verdict = v["oracle"]
        if verdict.startswith("review"):
            mine = next((r["verdict"] for k, r in read.items() if k.endswith(trial) and r["drawn"] == "flagged"), None)
            if mine != "TP":  # unread, or void: a replica server error on a call the answer needs
                review_needed += 1
                continue
            verdict = "fail: no answer (after a replica server error on a call the answer does not need)"
        kind = space[eid].get("alternative_kind")
        by_kind[kind]["auto"][verdict.split(":")[0]] += 1
        by_kind[kind]["elements"].add(eid)
        if verdict.startswith("fail"):
            failing.add(eid)
            fail_kinds[verdict.split(" (")[0]].add(eid)
    for trial, verdict in manual.items():
        eid = trial.split("/")[-1].removeprefix("BD2-")
        if eid in space:
            by_kind[space[eid].get("alternative_kind")]["manual"][verdict.split(":")[0]] += 1
    agree = sum(r.get("agree", 0) for r in specs.values())
    judged = sum(r.get("trials", 0) for r in specs.values())
    reviewed = [v for v in read.values() if v["judge"].startswith("fail")]
    sample = [v for v in read.values() if v["judge"].startswith("pass")]
    muse = [json.loads(line) for line in (HERE / "runs" / "calls.jsonl").read_text().splitlines()] \
        if (HERE / "runs" / "calls.jsonl").exists() else []
    solver = Counter()
    for s in (HERE / "runs").glob("p3*/t*/BDA-*/attempt-*/execution_summary.json"):
        u = json.loads(s.read_text()).get("usage") or {}
        solver["input"] += u.get("input_tokens") or 0
        solver["output"] += u.get("output_tokens") or 0
        solver["attempts"] += 1
    out = {
        "coverage space (faithful boundaries)": len(space),
        "tests generated": len(writer), "valid (reader agreed)": len(valid),
        "not valid": {e: {k: reader[e][k] for k in ("same_record", "hints_limit", "natural")} for e in reader
                      if e not in valid},
        "generated spec vs hand spec, phase-1 trials": f"{agree} of {judged}",
        "phase 3 trials on valid tests (graded)": sum(sum(k["auto"].values()) for k in by_kind.values()),
        "trials held for review (no answer after replica server errors)": review_needed,
        "elements with a failing trial": len(failing),
        "elements failing, by the judge's kind of failure": {k: len(v) for k, v in sorted(fail_kinds.items())},
        "pass rate by the alternative the actor had (automated vs phase 1)": {
            k: {"elements": len(v["elements"]),
                "automated": f"{v['auto']['pass']}/{v['auto']['pass'] + v['auto']['fail']}",
                "phase 1": f"{v['manual']['pass']}/{v['manual']['pass'] + v['manual']['fail']}"}
            for k, v in sorted(by_kind.items(), key=lambda kv: str(kv[0]))},
        "judge (a seeded quarter of the trials, read by me; review.py)": {
            "failures in the sample": len(reviewed), "read": sum(1 for v in reviewed if v["verdict"] != "unread"),
            "true positives": sum(1 for v in reviewed if v["verdict"] == "TP"),
            "false positives": sum(1 for v in reviewed if v["verdict"] == "FP"),
            "passes in the sample": len(sample), "passes read": sum(1 for v in sample if v["verdict"] != "unread"),
            "false negatives": sum(1 for v in sample if v["verdict"] == "FN"),
            "flagged trials": {r: sum(1 for v in read.values() if v["drawn"] == "flagged" and v["verdict"] == r)
                               for r in ("void", "TP", "unread")}},
        "muse": {"calls": len(muse), "input tokens": sum(r.get("input_tokens") or 0 for r in muse),
                 "output tokens": sum(r.get("output_tokens") or 0 for r in muse),
                 "billed usd": round(sum(r.get("cost_usd_billed") or 0 for r in muse), 4),
                 "list usd": round(sum(r.get("cost_usd_list_price") or 0 for r in muse), 4)},
        "solver (self-hosted Qwen, no charge)": dict(solver),
    }
    (HERE / "summary.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
