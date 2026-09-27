"""Phase 1: the per-fact policy variants of fact_coverage_02's 18 new scenarios, built by hand and checked by code.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.phase1_build [absence] [underspecified] [clone]

- **absence:** an absence twin per fact, derived by code (kit/policy.py).
- **underspecified:** a drop-F variant per fact, from the requests I rewrote by hand in phase1_dropf.json.
- **clone:** one clone per scenario, from the fields I chose by hand in phase1_clones.json.

Writes runs/phase1/cases/<domain>/<id>.json for the runner, and runs/phase1/index.json (meta and check results per
variant). A variant with a failed check is written to runs/phase1/rejected/ instead, with its problems.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from grounding.runs.autogen_02.kit import policy

STUDY = Path(__file__).resolve().parent
FC2 = STUDY.parent / "fact_coverage_02"
OUT = STUDY / "runs" / "phase1"


def exemplars() -> list[dict]:
    out = []
    for path in sorted((FC2 / "cases_new").glob("*/*.json")):
        case = json.loads(path.read_text())
        cid = case["case_id"]
        if cid.startswith(("P-", "FP-", "PP-")) or "TWIN" in cid or "-A" in cid:
            continue
        out.append(case)
    return out


FOLDER = {"absence twin": "cases", "underspecified": "cases_under", "underspecified clone": "cases_clone"}


def write(case: dict, meta: dict, index: dict):
    """Each form gets its own cases folder, so one form's solver run never picks up another's cases."""
    problems = meta.get("problems") or meta.get("errors") or []
    folder = (OUT / "rejected") if problems else (OUT / FOLDER[meta["form"]] / case["domain"])
    folder.mkdir(parents=True, exist_ok=True)
    (folder / f"{case['case_id']}.json").write_text(json.dumps(case, indent=1, ensure_ascii=False) + "\n")
    index[case["case_id"]] = {**meta, "domain": case["domain"], "prompt": case["prompt"], "accepted": not problems}


def main():
    which = set(sys.argv[1:]) or {"absence", "underspecified", "clone"}
    index_path = OUT / "index.json"
    index = json.loads(index_path.read_text()) if index_path.exists() else {}
    cases = {c["case_id"]: c for c in exemplars()}
    if "absence" in which:
        for case in cases.values():
            for twin, meta in policy.absence_twins(case):
                write(twin, meta, index)
    if "underspecified" in which:
        table = json.loads((STUDY / "phase1_dropf.json").read_text())
        for row in table["variants"]:
            case = cases[row["scenario"]]
            if row.get("not_derivable"):
                index[f"U-{row['scenario']}-{row['fact']}"] = {"form": "underspecified", "scenario": row["scenario"],
                                                              "fact": row["fact"], "accepted": False,
                                                              "not_derivable": row["not_derivable"]}
                continue
            variant, meta = policy.drop_f(case, row["fact"], row["prompt"], row.get("id"))
            write(variant, {**meta, "note": row.get("note", "")}, index)
    if "clone" in which:
        table = json.loads((STUDY / "phase1_clones.json").read_text())
        for row in table["clones"]:
            if row.get("not_derivable"):
                index[f"UC-{row['scenario']}"] = {"form": "underspecified clone", "scenario": row["scenario"],
                                                  "accepted": False, "not_derivable": row["not_derivable"]}
                continue
            variant, meta = policy.clone(cases[row["scenario"]], row["changes"], row["new_key"], row.get("id"),
                                         row.get("skip_children", ()))
            if variant is None:
                index[f"UC-{row['scenario']}"] = {**meta, "accepted": False}
                continue
            write(variant, {**meta, "note": row.get("note", "")}, index)
    OUT.mkdir(parents=True, exist_ok=True)
    index_path.write_text(json.dumps(index, indent=1, ensure_ascii=False) + "\n")
    forms = {}
    for v in index.values():
        f = forms.setdefault(v["form"], [0, 0])
        f[0] += 1
        f[1] += bool(v.get("accepted"))
    print({k: f"{a}/{n} accepted" for k, (n, a) in forms.items()})
    for cid, v in index.items():
        if not v.get("accepted"):
            print("  not accepted:", cid, v.get("not_derivable") or (v.get("problems") or v.get("errors") or [])[:3])


if __name__ == "__main__":
    main()
