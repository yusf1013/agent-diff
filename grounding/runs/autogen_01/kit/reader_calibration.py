"""Calibrate the cold reader on the hand-built exemplars: does it accept them, and does it catch the known defects?

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_01.kit.reader_calibration --out DIR

The exemplars have no author condition list, so the reader judges the candidates against its own conditions from
step 1. Checks in code:
- the target meets every condition;
- each decoy fails at least one condition;
- no genuine ambiguity changes the matches;
- the request reads naturally.

Also reported: decoys marked contestable, and decoys that fail more than one of the reader's conditions. Known
verdicts from fact_coverage_02:
- H-BOX-31-I11 is invalid (ambiguous wording);
- BOX-22's "Pricing sheet 2025.xlsx" decoy is contestable;
- every other scenario is valid.
"""
from __future__ import annotations

import argparse
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from grounding.runs.autogen_01.kit import reader

FC2 = Path(__file__).resolve().parents[2] / "fact_coverage_02"
WORK = Path("/tmp/autogen-5840209d/ws/reader_calibration")
SCENARIOS = [f"box/BOX-2{i}" for i in range(1, 5)] + [f"calendar/CAL-2{i}" for i in range(1, 5)] + \
    [f"linear/LIN-2{i}" for i in range(1, 7)] + [f"slack/SLK-2{i}" for i in range(1, 5)]
HIDDEN = ["box/H-BOX-31-I11", "box/H-BOX-32-I11", "calendar/H-CAL-09-I11", "linear/H-LIN-31-I11"]


def load(rel):
    for d in ("cases_new", "cases_hidden"):
        path = FC2 / d / f"{rel}.json"
        if path.exists():
            return json.loads(path.read_text())
    raise FileNotFoundError(rel)


def findings(case, verdict):
    ref = case["references"][0]
    targets = {str(x) for x in ref["expected"]}
    decoys = {str(c["witness"]): c["requirement"] for c in ref["claims"]}
    t2 = verdict.get("turn2", {})
    out = {"blocking": [], "contestable": [], "decoys_failing_several": []}
    for r in t2.get("records", []):
        rid, fails = str(r["id"]), r.get("fails", [])
        if rid in targets and fails:
            out["blocking"].append(f"target {rid} fails {fails}: {r.get('note', '')[:200]}")
        if rid in decoys:
            if not fails:
                out["blocking"].append(f"decoy {rid} ({decoys[rid]}) meets every condition: {r.get('note', '')[:200]}")
            elif len(fails) > 1:
                out["decoys_failing_several"].append(f"{rid} ({decoys[rid]}) fails {fails}")
            if r.get("contestable"):
                out["contestable"].append(f"{rid} ({decoys[rid]}): {r.get('note', '')[:200]}")
        elif rid not in targets and not fails:
            out["blocking"].append(f"undeclared record {rid} meets every condition")
    for a in t2.get("ambiguity_effects", []):
        if a.get("careful_reader_unsure") and a.get("changes_matches"):
            out["blocking"].append(f"ambiguous \"{a.get('phrase')}\": {a.get('explain', '')[:250]}")
    if t2.get("natural") is False:
        out["blocking"].append(f"unnatural: {t2.get('naturalness_note', '')[:200]}")
    return out


def one(rel, out_dir):
    case = load(rel)
    dest = out_dir / case["case_id"]
    if (dest / "findings.json").exists():
        return json.loads((dest / "findings.json").read_text())
    verdict = reader.read(case, WORK / out_dir.name / case["case_id"], dest, out_dir / "calls.jsonl",
                          case["case_id"], author_conditions=False)
    result = {"case_id": case["case_id"], "prompt": case["prompt"], **findings(case, verdict)}
    (dest / "verdict.json").write_text(json.dumps(verdict, indent=1))
    (dest / "findings.json").write_text(json.dumps(result, indent=1))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--concurrency", type=int, default=4)
    args = parser.parse_args()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        results = list(pool.map(lambda r: one(r, out), SCENARIOS + HIDDEN))
    for r in results:
        flag = "BLOCK" if r["blocking"] else "ok"
        print(f"{r['case_id']:14} {flag:5} blocking={len(r['blocking'])} contestable={len(r['contestable'])} "
              f"several={len(r['decoys_failing_several'])}")
        for b in r["blocking"] + [f"(contestable) {c}" for c in r["contestable"]]:
            print("     ", b[:300])
    (out / "summary.json").write_text(json.dumps(results, indent=1) + "\n")


if __name__ == "__main__":
    main()
