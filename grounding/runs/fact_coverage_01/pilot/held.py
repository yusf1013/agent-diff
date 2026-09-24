"""Strict per-fact 'tested' counts: a run tests a fact only if its near-miss was the sole candidate, or was fetched
(strict) / fetched or listed (lenient) during the trajectory. Fact-sensitive forms only."""
import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
rows = json.loads((HERE / "results.json").read_text())
stats = {"strict": defaultdict(lambda: [0, 0]), "lenient": defaultdict(lambda: [0, 0])}
for r in rows:
    if r.get("status") != "completed" or r["outcome"] in ("invalid_env",) or not r["reference"].endswith(".r1"):
        continue
    cid = r["case_id"]
    if not (r["design"] in ("present", "absent-told") or cid.startswith(("CON-", "ALT-", "WRD-"))):
        continue
    if cid.endswith("-plain"):
        continue
    attempt_dirs = sorted((HERE / "runs" / r["run"] / cid).glob("attempt-*"))
    attempt = next((a for a in reversed(attempt_dirs)
                    if json.loads((a / "execution_summary.json").read_text()).get("status") == "completed"), None)
    case = json.loads((attempt / "case.json").read_text())
    rec = json.loads((attempt / "solver" / f"{cid}.json").read_text())
    actions = " ".join(s.get("action") or "" for s in rec.get("steps", []))
    obs = " ".join(json.dumps(s.get("observation", {})) for s in rec.get("steps", []))
    sole = cid.startswith(("CON-", "ALT-", "WRD-"))
    ref = case["references"][0]
    for c in ref["claims"]:
        w, req = str(c["witness"]), c["requirement"]
        failed = req in r["exposed"] and r["outcome"] in ("incorrect", "recovered")
        fetched, listed = w in actions, w in obs
        for mode, ok in (("strict", sole or fetched or failed), ("lenient", sole or fetched or listed or failed)):
            if ok:
                stats[mode][req][0] += 1
                stats[mode][req][1] += failed
for mode, s in stats.items():
    tested = [k for k in s]
    failing = [k for k in s if s[k][1]]
    print(f"{mode}: facts tested={len(tested)}, failed at least once={len(failing)}, held in every test={len(tested) - len(failing)}")
