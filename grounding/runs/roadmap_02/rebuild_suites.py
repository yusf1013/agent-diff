"""Rebuild every accepted generated scenario (autogen_01's three arms, autogen_02's Phase 4) with the kit as it stands,
and record digests of each built case and derived test, the tests the derivation drops, and the build's problems.
Run before and after a kit change; `compare` lists exactly what changed. No model or replica calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.roadmap_02.rebuild_suites snapshot OUT.json
    python grounding/runs/fact_coverage_02/launch.py grounding.runs.roadmap_02.rebuild_suites compare BEFORE AFTER
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

from grounding.runs.autogen_01.kit import derive, scenario

RUNS = Path(__file__).resolve().parents[1]
SOURCES = [RUNS / "autogen_01/runs" / f"gen_arm_{a}" for a in ("r", "p", "p_v2")] + [RUNS / "autogen_02/runs/phase4_gen"]


def digest(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:16]


def accepted():
    """(source run, scenario folder, latest scenario version) for every scenario with a built case."""
    for run in SOURCES:
        for case_path in sorted(run.glob("*/case.json")):
            folder = case_path.parent
            versions = sorted(folder.glob("scenario-v*.json"), key=lambda p: int(re.search(r"v(\d+)", p.name).group(1)))
            if versions:
                yield run.name, folder, versions[-1]


def snapshot(out: Path):
    doc = {}
    for run, folder, version in accepted():
        s = json.loads(version.read_text())
        brief = {"scenario_id": s["scenario_id"], "domain": s["domain"],
                 "facts": sorted({d["fact"] for d in s["reference"]["decoys"]})}
        case, problems = scenario.build(s, brief)
        entry = {"run": run, "version": version.name, "problems": problems}
        if case is not None:
            if hasattr(derive, "suite_with_dropped"):
                kept, dropped = derive.suite_with_dropped(case)
            else:
                kept, dropped = derive.suite(case), []
            entry.update(case=digest(case), seed=digest(case["seed"]),
                         tests={t["case_id"]: digest(t) for t, _ in kept},
                         dropped={t["case_id"]: m.get("errors", []) for t, m in dropped})
        doc[f"{run}/{folder.name}"] = entry
    out.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    print(f"{len(doc)} scenarios -> {out}")


def compare(before: Path, after: Path):
    a, b = json.loads(before.read_text()), json.loads(after.read_text())
    same = 0
    for key in sorted(set(a) | set(b)):
        x, y = a.get(key, {}), b.get(key, {})
        notes = []
        if x.get("seed") != y.get("seed"):
            notes.append("seed changed")
        elif x.get("case") != y.get("case"):
            notes.append("case changed (not the seed)")
        tx, ty = x.get("tests", {}), y.get("tests", {})
        gone = sorted(set(tx) - set(ty))
        new = sorted(set(ty) - set(tx))
        changed = sorted(t for t in set(tx) & set(ty) if tx[t] != ty[t])
        if gone:
            notes.append(f"tests no longer in the suite: {gone}")
        if new:
            notes.append(f"new tests: {new}")
        if changed:
            notes.append(f"tests changed: {changed}")
        if sorted(y.get("dropped", {})) != sorted(x.get("dropped", {})):
            notes.append(f"dropped: {sorted(y.get('dropped', {}))}")
        px, py = set(x.get("problems", [])), set(y.get("problems", []))
        if py - px:
            notes.append(f"new build problems: {sorted(py - px)}")
        if px - py:
            notes.append(f"problems gone: {sorted(px - py)}")
        if notes:
            print(key, "|", "; ".join(notes))
        else:
            same += 1
    print(f"{same} of {len(set(a) | set(b))} scenarios identical")


if __name__ == "__main__":
    if sys.argv[1] == "snapshot":
        snapshot(Path(sys.argv[2]))
    else:
        compare(Path(sys.argv[2]), Path(sys.argv[3]))
