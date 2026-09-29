"""Compare locked references with selected saved scores. No model calls or source edits."""
from __future__ import annotations

import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from finalize import verify_lock
from metrics import group, summarize

HERE = Path(__file__).resolve().parent
GROUNDING = HERE.parents[1]
OC = GROUNDING / "runs/openclaw_eval_01/runs"
SOURCES = {}


def read(path):
    data = path.read_bytes()
    SOURCES[str(path.relative_to(GROUNDING))] = hashlib.sha256(data).hexdigest()
    return json.loads(data)


def main():
    verify_lock()
    assert (HERE / "unblinding.json").exists()
    manifest = read(HERE / "manifest.json")
    reference = {r["blind_id"]: r for r in read(HERE / "effective_labels.json")}
    scores = {run: {t["case_id"]: t for t in read(OC / f"{run}.score.json")["tests"]}
              for run in sorted({r["key"].split("/")[0] for r in manifest["sample"] if r["key"].startswith("full_")})}
    adjudications = {run: read(OC / f"{run}.adjudicated.json") for run in scores}
    rows = []
    for m in manifest["sample"]:
        run, trial, cid = m["key"].split("/")
        policy = run.startswith("solve_")
        base = OC / "policy" if policy else OC
        folder = run.replace("solve_", "judged_", 1) if policy else "judged_" + run
        path = base / folder / m["key"] / "verdict.json"
        judge = read(path) if path.exists() else None
        if judge:
            assert judge["key"] == m["key"]
        if policy:
            assert judge is not None, m["key"]
            pipeline = judge.copy()
        else:
            pipeline = scores[run][cid]["trials"][trial].copy()
            assert pipeline["judged"] == (judge is not None), m["key"]
            if judge:
                assert pipeline["outcome"] == judge["outcome"], m["key"]
                assert set(pipeline["exposed"]) == set(judge["exposed"]), m["key"]
        summary = read(GROUNDING / m["attempt"] / "execution_summary.json")
        turn_seconds = (summary.get("turn_durations_s") or [0])[0]
        wait_seconds = (summary.get("usage") or {}).get("limiter_wait_s") or 0
        over_budget = summary.get("status") == "completed" and turn_seconds - wait_seconds > 480
        exclusion = None
        if not policy:
            exclusions = {r["trial"]: r for r in adjudications[run]["trials_not_counted"]}
            exclusion = exclusions.get(f"{trial}/{cid}")
            saved_budget = {r["trial"] for r in adjudications[run]["trials_over_budget"]}
            assert over_budget == (f"{trial}/{cid}" in saved_budget), m["key"]
        row = {k:m[k] for k in ("blind_id", "key", "domain", "form", "stratum", "weight", "attempt", "solver_record")}
        row.update(kind="policy" if policy else "regular", reference=reference[m["blind_id"]],
                   judge=judge, pipeline=pipeline, mechanical=pipeline if judge is None else None,
                   comparator_source="LLM" if judge else "mechanical",
                   judge_path=str(path.relative_to(GROUNDING)) if judge else None,
                   score_path=None if policy else str((OC / f"{run}.score.json").relative_to(GROUNDING)),
                   over_budget=over_budget, agent_seconds=turn_seconds - wait_seconds,
                   historical_trial_exclusion=exclusion)
        rows.append(row)
    assert len(rows) == len({r["key"] for r in rows}) == 200
    numbers = {"generated_utc": datetime.now(timezone.utc).isoformat(),
               "population": manifest["population_size"], "eligible_population": manifest["eligible_size"],
               "sample": len(rows), "distinct_cases": len({r["key"].split("/")[-1] for r in rows}),
               "reference_outcomes": dict(Counter(r["reference"]["outcome"] or "uncertain" for r in rows)),
               "comparators": {c: summarize(rows, c) for c in ("judge", "mechanical", "pipeline")},
               "by_domain": {d: {c:summarize([r for r in rows if r["domain"] == d],c) for c in ("judge","mechanical","pipeline")}
                             for d in sorted({r["domain"] for r in rows})},
               "by_form": {f: {c:summarize([r for r in rows if r["form"] == f],c) for c in ("judge","mechanical","pipeline")}
                           for f in sorted({r["form"] for r in rows})},
               "by_kind": {k: {c:summarize([r for r in rows if r["kind"] == k],c) for c in ("judge","mechanical","pipeline")}
                           for k in ("regular","policy")},
               "disagreements": {c: [r["blind_id"] for r in rows if r[c] and r["reference"]["outcome"] is not None
                                     and r["reference"]["outcome"] != r[c]["outcome"]]
                                 for c in ("judge","mechanical","pipeline")},
               "over_budget": [r["blind_id"] for r in rows if r["over_budget"]],
               "historical_trial_exclusions": [r["blind_id"] for r in rows if r["historical_trial_exclusion"]]}
    (HERE / "comparison.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n")
    (HERE / "numbers.json").write_text(json.dumps(numbers, indent=2, ensure_ascii=False) + "\n")
    (HERE / "comparison_sources.sha256.json").write_text(json.dumps(SOURCES, indent=2) + "\n")
    print(json.dumps({k:v for k,v in numbers.items() if k not in {"by_domain", "by_form", "by_kind"}}, indent=2))


if __name__ == "__main__":
    main()
