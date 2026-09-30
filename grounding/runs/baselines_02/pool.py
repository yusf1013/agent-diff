"""The blind review pool: every loaded test of both Sonnet arms and 20 of our Muse tests, under anonymous ids.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.baselines_02.pool build POOL GEN_RUN ...
    python grounding/runs/fact_coverage_02/launch.py grounding.runs.baselines_02.pool show POOL R001 [R002 ...]

- **Ours:** 5 regular tests per service, drawn with a fixed seed from the 292 valid Muse-written tests of the final
  score (`openclaw_eval_01/runs/final_regular_with_6b.json`, scenarios `G4-`), each as the case that ran (trial 1's
  latest attempt).
- **Anonymous ids:** the pool is shuffled with a fixed seed and numbered R001, R002, ...; `manifest.json` maps each
  pool id to its arm and case and is not read during the review.
- **The view** is the same for every test: the service, the request, the acting user, the seeded records by table,
  and the test's own expected outcome and assertions. Our tests have no such oracle (their answer key is withheld),
  so they can be told apart; the review is blind to the arm, not to ours against theirs.
"""
from __future__ import annotations

import json
import random
import sys
from pathlib import Path

from grounding.runs.autogen_01.kit.bundle import compact_row

HERE = Path(__file__).resolve().parent
OC = HERE.parent / "openclaw_eval_01" / "runs"
DOMAINS = ("box", "calendar", "linear", "slack")
OURS_PER_DOMAIN, OURS_SEED, POOL_SEED = 5, 20260930, 2026093001
USER_TABLES = {"box": "box_users", "calendar": "calendar_users", "linear": "users", "slack": "users"}


def our_draw() -> list[dict]:
    final = json.loads((OC / "final_regular_with_6b.json").read_text())["tests"]
    muse = sorted((t for t in final if t["scenario"].startswith("G4-")), key=lambda t: t["case_id"])
    rng, picked = random.Random(OURS_SEED), []
    for d in DOMAINS:
        picked += rng.sample([t for t in muse if t["domain"] == d], OURS_PER_DOMAIN)
    out = []
    for t in picked:
        attempt = sorted((OC / t["run"] / "t1" / t["case_id"]).glob("attempt-*"))[-1]
        out.append({"source": "ours", "case_id": t["case_id"], "path": str(attempt / "case.json")})
    return out


def build(pool: Path, gen_runs: list[Path]) -> None:
    if pool.exists():
        raise SystemExit(f"{pool} exists")
    entries = []
    for run in gen_runs:
        for path in sorted(run.glob("*/cases/*.json")):
            case = json.loads(path.read_text())
            entries.append({"source": case["baseline"]["generator"], "case_id": case["case_id"], "path": str(path)})
    entries += our_draw()
    random.Random(POOL_SEED).shuffle(entries)
    (pool / "items").mkdir(parents=True)
    manifest = {}
    for i, e in enumerate(entries, start=1):
        pid = f"R{i:03}"
        manifest[pid] = e
        case = json.loads(Path(e["path"]).read_text())
        item = {"pool_id": pid, "domain": case["domain"], "request": case["prompt"],
                "acting_user_id": case.get("acting_user_id"), "seed": case["seed"]}
        if "baseline" in case:
            item["expected"] = case["baseline"]["expected"]
            item["assertions"] = case["baseline"]["assertions"]
        (pool / "items" / f"{pid}.json").write_text(json.dumps(item, indent=1, ensure_ascii=False) + "\n")
    (pool / "manifest.json").write_text(json.dumps(manifest, indent=1) + "\n")
    print(f"{len(entries)} tests in the pool: {pool}")


def show(pool: Path, pid: str) -> str:
    item = json.loads((pool / "items" / f"{pid}.json").read_text())
    users = {str(r.get("id")): r for r in item["seed"].get(USER_TABLES[item["domain"]], [])}
    actor = users.get(str(item.get("acting_user_id")), {})
    lines = [f"# {pid} ({item['domain']})", f"Request: {item['request']}",
             f"Acting user: {item.get('acting_user_id')} {compact_row(actor, 200) if actor else ''}", "## Records"]
    for table, rows in item["seed"].items():
        if not isinstance(rows, list) or not rows:
            continue
        lines.append(f"### {table} ({len(rows)})")
        lines += [f"- {compact_row(r, 900)}" for r in rows]
    if "expected" in item:
        lines += ["## The test's expected outcome", json.dumps(item["expected"], ensure_ascii=False),
                  "## The test's assertions", json.dumps(item["assertions"], ensure_ascii=False)]
    else:
        lines += ["## The test's expected outcome", "(an answer key, withheld)"]
    return "\n".join(lines)


def facts(domain: str) -> str:
    """The catalog's facts for a service, as the review reads them: id, meaning, designated substitutes, families."""
    doc = json.loads((HERE.parent / "autogen_01" / "inputs" / domain / "facts.json").read_text())
    return "\n".join(f"{f['id']} | {f.get('meaning') or f.get('subkind') or ''} | subst: "
                     f"{'; '.join(f.get('designated_substitutes') or [])} | fam: "
                     f"{', '.join(f.get('suggested_families') or [])}" for f in doc["facts"])


def main():
    if sys.argv[1] == "facts":
        print(facts(sys.argv[2]))
        return
    cmd, pool = sys.argv[1], Path(sys.argv[2]).resolve()
    if cmd == "build":
        build(pool, [Path(p).resolve() for p in sys.argv[3:]])
    elif cmd == "show":
        print("\n\n".join(show(pool, pid) for pid in sys.argv[3:]))


if __name__ == "__main__":
    main()
