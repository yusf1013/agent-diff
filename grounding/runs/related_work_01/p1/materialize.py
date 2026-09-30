"""Build a P1 variant's seed: the service's shared seed with the variant's patch applied (rows removed, or rows added).

    python -m grounding.runs.related_work_01.p1.materialize P1-A-slack_57-O1 [--out seed.json]
    python -m grounding.runs.related_work_01.p1.materialize --check-all     # every valid variant; no file written

The prompt is the test's own (datasets/agent-diff-bench/all_numbered.jsonl), unchanged. The check confirms that every
foreign key of the resulting seed points at a row (a seed with a dangling key would not install).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from grounding.runs.related_work_01.p1.generate import SEEDS, fks_of, pk_of

REPO = Path(__file__).resolve().parents[4]
HERE = Path(__file__).parent


def build(variant: str) -> tuple[dict, str]:
    patch = next(json.loads(l) for l in (HERE / "patches.jsonl").read_text().splitlines()
                 if json.loads(l)["variant"] == variant)
    service = patch["service"]
    schema = json.loads((HERE / "schemas.json").read_text())[service]
    seed = json.loads((REPO / SEEDS[service]).read_text())
    for table, keys in (patch.get("remove") or {}).items():
        pk = pk_of(schema, table)
        drop = {json.dumps([k.get(c) for c in pk]) for k in keys}
        seed[table] = [r for r in seed[table] if json.dumps([r.get(c) for c in pk]) not in drop]
    for table, rows in (patch.get("add") or {}).items():
        seed.setdefault(table, []).extend(rows)
    return seed, service


def dangling(seed: dict, service: str) -> list[str]:
    schema = json.loads((HERE / "schemas.json").read_text())[service]
    out = []
    for child, col, parent, pcol in fks_of(schema):
        if child not in seed or parent not in seed:
            continue
        present = {r.get(pcol) for r in seed[parent]}
        out += [f"{child}.{col}={r.get(col)!r}" for r in seed[child] if r.get(col) is not None and r.get(col) not in present]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("variant", nargs="?")
    ap.add_argument("--out")
    ap.add_argument("--check-all", action="store_true")
    args = ap.parse_args()
    if args.check_all:
        review = [json.loads(l) for l in (HERE / "review.jsonl").read_text().splitlines()]
        bad = {}
        for r in review:
            if r["verdict"].startswith("valid"):
                seed, service = build(r["variant"])
                d = dangling(seed, service)
                if d:
                    bad[r["variant"]] = d[:3]
        print(f"{sum(r['verdict'].startswith('valid') for r in review)} valid variants built; with dangling keys: {len(bad)}")
        for k, v in bad.items():
            print(" ", k, v)
        return
    seed, _ = build(args.variant)
    text = json.dumps(seed, ensure_ascii=False, indent=1)
    (Path(args.out).write_text(text) if args.out else print(text[:2000]))


if __name__ == "__main__":
    main()
