"""Which catalog facts P1's valid variants touch (occurrence level: the facts the obligation's identifying conditions
use), and so which fact–mode requirements of our policy space. An upper bound on what P1 exercises: occurrence, not the
credit rule (P1's seeds hold near misses only by chance).
    python -m grounding.runs.related_work_01.p1.facts"""
import json
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
HERE = Path(__file__).parent
ENTITY_TABLE = {}


def catalog(service):
    reqs = json.loads((REPO / f"grounding/runs/fact_coverage_01/catalog/{service}.json").read_text())["requirements"]
    by_col = defaultdict(set)
    for r in reqs:
        if r.get("table") and r.get("field"):
            by_col[f"{r['table']}.{r['field']}"].add(r["id"])
            ENTITY_TABLE[(service, r["entity"])] = r["table"]
    for r in reqs:
        for role in r.get("roles") or []:
            ent, _, col = role.partition(".")
            table = ENTITY_TABLE.get((service, ent), ent)
            if col:
                by_col[f"{table}.{col}"].add(r["id"])
            else:  # an association table: any of its columns
                by_col[f"{table}.*"].add(r["id"])
    return by_col


def facts_of(service, card, by_col):
    out, unmatched = set(), set()
    for alt in card.get("Alternative sufficient identifying sets") or []:
        for item in alt or []:
            table, _, col = item.partition(".")
            hits = by_col.get(item) or by_col.get(f"{table}.*")
            if hits:
                out |= hits
            else:
                unmatched.add(item)
    return out, unmatched


def main():
    candidates = {json.loads(l)["variant"]: json.loads(l) for l in (HERE / "candidates.jsonl").read_text().splitlines()}
    review = [json.loads(l) for l in (HERE / "review.jsonl").read_text().splitlines()]
    cards = {}
    for s in ("slack", "box", "linear"):
        for t in json.loads((REPO / f"grounding/domains/{s}/analysis/analysis.json").read_text()):
            for i, o in enumerate(t["obligations"], 1):
                cards[(s, t["test_id"], i)] = o["card"]
    maps = {s: catalog(s) for s in ("slack", "box", "linear")}
    ours = json.loads((REPO / "grounding/runs/report_01/numbers/coverage.json").read_text())
    touched = defaultdict(set)
    unmatched = Counter()
    per_variant = {}
    for r in review:
        if r["verdict"] not in ("valid", "valid_unverified"):
            continue
        c = candidates[r["variant"]]
        facts, un = facts_of(c["service"], cards[(c["service"], c["test_id"], c["obligation"])], maps[c["service"]])
        per_variant[r["variant"]] = sorted(facts)
        for f in facts:
            touched[(c["service"], c["mode"])].add(f)
        for u in un:
            unmatched[(c["service"], u)] += 1
    out = {"per_variant": per_variant,
           "facts_touched": {f"{s}/{m}": sorted(v) for (s, m), v in sorted(touched.items())},
           "unmatched_columns": {f"{s}/{u}": n for (s, u), n in unmatched.most_common()}}
    (HERE / "facts.json").write_text(json.dumps(out, indent=1) + "\n")
    for (s, m), v in sorted(touched.items()):
        print(s, m, len(v), sorted(v))
    print("variants with no fact:", sum(1 for v in per_variant.values() if not v), "of", len(per_variant))
    print("unmatched columns:", out["unmatched_columns"])


if __name__ == "__main__":
    main()
