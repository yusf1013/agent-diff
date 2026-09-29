"""Freeze a metadata-only stratified draw. Never reads execution scores or judge verdicts."""
from __future__ import annotations

import hashlib
import json
import random
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
GROUNDING = HERE.parents[1]
RUNS = HERE.parent
OC = RUNS / "openclaw_eval_01"
SEED = 2026092902


def read(p):
    return json.loads(p.read_text())


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    dest = HERE / "manifest.json"
    if dest.exists():
        raise SystemExit("manifest.json already exists; the draw is immutable")
    source = RUNS / "report_01/numbers/concise.json"
    keys = read(source)["final_execution_keys"]
    assert len(keys) == len(set(keys)) == 3018
    previous, label_sources = set(), {}
    for p in sorted((OC / "eval").glob("labels_*/*.json")):
        obj = read(p)
        if isinstance(obj, dict):
            previous.update(k for k in obj if k in keys)  # Keys only, never display/read label values.
        label_sources[str(p.relative_to(GROUNDING))] = sha(p)
    meta = {}
    for p in (OC / "suite/suite.json", RUNS / "completion_01/suite/cases/suite.json"):
        meta.update({m["case_id"]: m for m in read(p)})
    strata, excluded = defaultdict(list), []
    for key in sorted(keys):
        run, trial, case_id = key.split("/")
        reason = "previous_reference_label" if key in previous else "previously_displayed_case_result" if case_id == "AP-BOX-01" else None
        if reason:
            excluded.append({"key": key, "reason": reason})
            continue
        mode = "absence" if run.startswith("solve_") and "absence" in run else "underspecified" if run.startswith("solve_") else meta[case_id]["form"]
        domain = next(d for abbreviation, d in (("BOX", "box"), ("CAL", "calendar"), ("LIN", "linear"), ("SLK", "slack")) if f"-{abbreviation}-" in case_id)
        parent = OC / "runs" / ("policy" if run.startswith("solve_") else "") / key
        attempts = sorted(parent.glob("attempt-*"))
        assert attempts, key
        strata[f"{domain}/{mode}"].append({"key": key, "domain": domain, "form": mode,
            "attempt": str(attempts[-1].relative_to(GROUNDING))})
    eligible = sum(map(len, strata.values()))
    allocation = {s: (200 * len(v)) // eligible for s, v in strata.items()}
    priority = sorted(strata, key=lambda s: (-(200 * len(strata[s]) % eligible), s))
    for s in priority[:200-sum(allocation.values())]:
        allocation[s] += 1
    rng = random.Random(SEED)
    sample = []
    for s, records in sorted(strata.items()):
        for rec in rng.sample(records, allocation[s]):
            sample.append({**rec, "stratum": s, "weight": len(records) / allocation[s]})
    rng.shuffle(sample)
    for i, rec in enumerate(sample, 1):
        rec["blind_id"] = f"BR{i:03d}"
        at = GROUNDING / rec["attempt"]
        solver = sorted(p for p in (at / "solver").glob("*.json") if p.name != "config.json")
        assert len(solver) == 1, (rec["key"], solver)
        rec["solver_record"] = str(solver[0].relative_to(GROUNDING))
        paths = [at / "case.json", at / "execution_summary.json", solver[0],
                 at / "solver/final_response.md", at / "environment/diff_run.json",
                 at / "environment/initial_state.json", at / "environment/final_state.json"]
        rec["source_hashes"] = {str(p.relative_to(GROUNDING)): sha(p) if p.exists() else None for p in paths}
    assert len(sample) == len({x["key"] for x in sample}) == 200
    out = {"created_utc": datetime.now(timezone.utc).isoformat(), "seed": SEED,
           "population_size": len(keys), "eligible_size": eligible, "sample_size": len(sample),
           "population_manifest": str(source.relative_to(GROUNDING)), "population_sha256": sha(source),
           "label_source_hashes": label_sources, "excluded": excluded,
           "strata": {s: {"eligible": len(v), "sampled": allocation[s]} for s, v in sorted(strata.items())},
           "sample": sample}
    dest.write_text(json.dumps(out, indent=2) + "\n")
    (HERE / "draw.sha256").write_text(f"{sha(dest)}  manifest.json\n")
    print(json.dumps({"eligible": eligible, "excluded": len(excluded), "sample": len(sample),
                      "forms": dict(Counter(r["form"] for r in sample)), "domains": dict(Counter(r["domain"] for r in sample)),
                      "distinct_cases": len({r["key"].split('/')[-1] for r in sample}),
                      "strata": out["strata"]}, indent=2))


if __name__ == "__main__":
    main()
