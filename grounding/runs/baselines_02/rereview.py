"""The reviewer cross-check the lead asked for: I re-review a seeded draw of baselines_01's Muse twin tests (and, as a
clean control, of N1's) under the same rules, then compare with the other session's review of the same tests.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.baselines_02.rereview build OUT
    python grounding/runs/fact_coverage_02/launch.py grounding.runs.baselines_02.pool show OUT X01 [X02 ...]
    python grounding/runs/fact_coverage_02/launch.py grounding.runs.baselines_02.rereview compare OUT MINE.json

- **The draw:** 5 tests from N0M and 5 from N1M (the twins, `twin2/*/runs/gen_01/suite/`), and 5 from N1
  (`n1/runs/gen_01/*/cases/`) as a control, every test of the arm eligible, valid or not; shuffled under ids X01...
  `manifest.json` maps them back and is read only by `compare`.
- **Not fully blind for the twins:** an hour before the draw, a consistency audit of my own review printed the other
  session's non-F0 near misses (test id, fact, family, a few words) for every twin test, and its set-form and
  unsound-oracle tests. N1's review was never printed in this session, so the N1 draw is the clean control.
- **The comparison,** per test: validity and flaw causes, form, target, the near-miss records, the fact of each
  shared near miss, designated-or-plain and the family itself, and the facts credited as proper.
"""
from __future__ import annotations

import json
import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
B1 = HERE.parent / "baselines_01"
ARMS = {"N0M": (B1 / "twin2/n0m/runs/gen_01", "suite/*/*.json"),
        "N1M": (B1 / "twin2/n1m/runs/gen_01", "suite/*/*.json"),
        "N1": (B1 / "n1/runs/gen_01", "*/cases/*.json")}
PER_ARM, DRAW_SEED, SHUFFLE_SEED = 5, 2026093031, 2026093032


def build(out: Path) -> None:
    if out.exists():
        raise SystemExit(f"{out} exists: the draw is made once")
    rng, entries = random.Random(DRAW_SEED), []
    for arm, (gen, pattern) in ARMS.items():
        paths = sorted(gen.glob(pattern))
        entries += [{"arm": arm, "path": str(p)} for p in rng.sample(paths, PER_ARM)]
    random.Random(SHUFFLE_SEED).shuffle(entries)
    (out / "items").mkdir(parents=True)
    manifest = {}
    for i, e in enumerate(entries, start=1):
        pid = f"X{i:02}"
        case = json.loads(Path(e["path"]).read_text())
        manifest[pid] = {**e, "case_id": case["case_id"]}
        item = {"pool_id": pid, "domain": case["domain"], "request": case["prompt"],
                "acting_user_id": case.get("acting_user_id"), "seed": case["seed"],
                "expected": case["baseline"]["expected"], "assertions": case["baseline"]["assertions"]}
        (out / "items" / f"{pid}.json").write_text(json.dumps(item, indent=1, ensure_ascii=False) + "\n")
    (out / "manifest.json").write_text(json.dumps(manifest, indent=1) + "\n")
    print(f"{len(entries)} tests -> {out}")


def designated(family: str) -> bool:
    return family != "F0"


def compare_one(mine: dict, theirs: dict) -> dict:
    m_nm = {str(n["record"]): n for n in mine["near_misses"]}
    t_nm = {str(n["record"]): n for n in theirs["near_misses"]}
    shared = sorted(m_nm.keys() & t_nm.keys())
    return {"valid_same": mine["valid"] == theirs["valid"],
            "flaws_mine": [f["cause"] for f in mine["flaws"]], "flaws_theirs": [f["cause"] for f in theirs["flaws"]],
            "form_same": mine["form"] == theirs["form"], "form_mine": mine["form"], "form_theirs": theirs["form"],
            "near_misses_mine": len(m_nm), "near_misses_theirs": len(t_nm), "shared": len(shared),
            "only_mine": sorted(m_nm.keys() - t_nm.keys()), "only_theirs": sorted(t_nm.keys() - m_nm.keys()),
            "fact_same": sum(m_nm[w]["fact"] == t_nm[w]["fact"] for w in shared),
            "designated_same": sum(designated(m_nm[w]["family"]) == designated(t_nm[w]["family"]) for w in shared),
            "family_same": sum(m_nm[w]["family"] == t_nm[w]["family"] for w in shared),
            "designated_mine": sum(designated(n["family"]) for n in m_nm.values()),
            "designated_theirs": sum(designated(n["family"]) for n in t_nm.values()),
            "proper_mine": sorted(mine["proper"]), "proper_theirs": sorted(theirs["proper"]),
            "family_pairs": [(w, t_nm[w]["family"], m_nm[w]["family"]) for w in shared
                             if m_nm[w]["family"] != t_nm[w]["family"]]}


def compare(out: Path, mine_path: Path) -> None:
    manifest = json.loads((out / "manifest.json").read_text())
    mine = {r["pool_id"]: r for r in json.loads(mine_path.read_text())}
    theirs = {}
    for arm, (gen, _) in ARMS.items():
        theirs.update({r["test"]: r for r in json.loads((gen / "review.json").read_text())})
    rows = []
    for pid, e in sorted(manifest.items()):
        rows.append({"pool_id": pid, "arm": e["arm"], "case_id": e["case_id"],
                     **compare_one(mine[pid], theirs[e["case_id"]])})
    total = {}
    for group, members in (("twins", ("N0M", "N1M")), ("N1", ("N1",)), ("all", ("N0M", "N1M", "N1"))):
        rs = [r for r in rows if r["arm"] in members]
        total[group] = {"tests": len(rs), "valid_same": sum(r["valid_same"] for r in rs),
                        "form_same": sum(r["form_same"] for r in rs),
                        "near_misses_mine": sum(r["near_misses_mine"] for r in rs),
                        "near_misses_theirs": sum(r["near_misses_theirs"] for r in rs),
                        "shared": sum(r["shared"] for r in rs), "fact_same": sum(r["fact_same"] for r in rs),
                        "designated_same": sum(r["designated_same"] for r in rs),
                        "family_same": sum(r["family_same"] for r in rs),
                        "designated_mine": sum(r["designated_mine"] for r in rs),
                        "designated_theirs": sum(r["designated_theirs"] for r in rs),
                        "proper_mine": sum(len(r["proper_mine"]) for r in rs),
                        "proper_theirs": sum(len(r["proper_theirs"]) for r in rs),
                        "proper_same_tests": sum(r["proper_mine"] == r["proper_theirs"] for r in rs)}
    result = {"totals": total, "rows": rows}
    (out / "compare.json").write_text(json.dumps(result, indent=1) + "\n")
    print(json.dumps(total, indent=1))


def main():
    cmd, out = sys.argv[1], Path(sys.argv[2]).resolve()
    if cmd == "build":
        build(out)
    elif cmd == "compare":
        compare(out, Path(sys.argv[3]).resolve())


if __name__ == "__main__":
    main()
