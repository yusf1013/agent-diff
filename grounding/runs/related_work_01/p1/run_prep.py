"""P1's run: the matched 48 variants, as cases our runner and judge v2 read. Rules fixed before any run.

    python -m grounding.runs.related_work_01.p1.run_prep --out grounding/runs/related_work_01/p1/runs/p1_01
    (then run.py with --cases-dir <out>/cases; the blind sample is drawn from that folder first)

**Which variants** (from the 332 reviewed valid, plain form: probe-form and unverified ones are out):
- **state-changing:** the obligation writes a table (its card's written attributes), so the policy is about acting;
- **attributable:** the written table is the referent's table, or has a foreign key to it, so the triage can tell
  which record an action touched;
- **graded by tiers, in this order within a cell:** (0) clean, no other obligation of the test writes that table;
  (1) separable, others write the table but not the obligation's columns (the effect then counts only updates to
  those columns); (2) shared, others write the same table and column. Tier 2 exists because 67 of the 78 valid
  underspecified variants are in tests that change several records of one kind; there the triage cannot tell the
  parts apart and judge v2's reading decides (the 60 blind labels check it).
- **every case lists the test's other obligations** as context references (their records, "another record the
  request names" in judge v2's bundle), so acting on them reads as part of the request.

**How many:** 8 per service and mode. Box has only 2 underspecified variants that qualify, so the mode's 6 other
slots go to Slack and Linear, 3 each (the mode keeps 24). Within a cell, lower tiers first; within a tier, variants
from different tests first, in a fixed shuffle (seed 4801).

**The case:** the Agent-Diff test's prompt, unchanged; its impersonated user; the variant's seed (materialize.py);
one reference, for the mutated obligation, with the targets judge v2's policy rules expect:
- absence (`AT-` prefix, form "absence twin"): no target;
- underspecified (`U-` prefix): the original and its copy, both TARGET.
The effect locator is the written table (and the column that points at the referent), for the triage. No near
misses are listed (P1 designs none). Writes <out>/cases/<domain>/<case_id>.json and <out>/p1_selection.json.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
from collections import OrderedDict
from pathlib import Path

from grounding.runs.related_work_01.p1.generate import pk_of
from grounding.runs.related_work_01.p1.materialize import build

REPO = Path(__file__).resolve().parents[4]
HERE = Path(__file__).parent
PER_CELL = {("slack", "absence"): 8, ("box", "absence"): 8, ("linear", "absence"): 8,
            ("slack", "underspecified"): 11, ("box", "underspecified"): 2, ("linear", "underspecified"): 11}
SEED = 4801


def cards_of(service: str) -> dict:
    return {t["test_id"]: t for t in json.loads((REPO / f"grounding/domains/{service}/analysis/analysis.json").read_text())}


def effect_for(schema: dict, written: list[str], referent_table: str) -> dict | None:
    tables = list(dict.fromkeys(w.split(".")[0] for w in written))
    for t in sorted(tables, key=lambda t: t != referent_table):  # the referent's own table first
        if t not in schema:
            continue
        if t == referent_table:
            return {"table": t, "key": pk_of(schema, t), "changes": ["insert", "delete", "update"]}
        fk = next((f["column"] for f in schema[t]["fks"] if f["ref_table"] == referent_table), None)
        if fk:
            return {"table": t, "key": pk_of(schema, t), "field": fk, "changes": ["insert", "delete", "update"]}
    return None


def eligible() -> list[dict]:
    review = {json.loads(l)["variant"]: json.loads(l) for l in (HERE / "review.jsonl").read_text().splitlines()}
    schemas = json.loads((HERE / "schemas.json").read_text())
    cards = {s: cards_of(s) for s in ("slack", "box", "linear")}
    out = []
    for line in (HERE / "candidates.jsonl").read_text().splitlines():
        c = json.loads(line)
        if review.get(c["variant"], {}).get("verdict") != "valid":
            continue
        test = cards[c["service"]][c["test_id"]]
        obs = test["obligations"]
        card = obs[c["obligation"] - 1]["card"]
        written = card.get("Written attributes") or []
        if c.get("task_type") != "state-changing" or not written:
            continue
        effect = effect_for(schemas[c["service"]], written, c["referent_table"])
        if not effect:
            continue
        mine = {w.split(".")[1] for w in written if w.split(".")[0] == effect["table"]}
        others = {(w.split(".")[0], w.split(".")[1]) for i, o in enumerate(obs) if i != c["obligation"] - 1
                  for w in (o["card"].get("Written attributes") or [])}
        same_table = {col for t, col in others if t == effect["table"]}
        if not same_table:
            tier = 0
        elif not (same_table & mine) and effect["table"] == c["referent_table"]:
            tier, effect = 1, {**effect, "columns": sorted(mine), "changes": ["update"]}
        else:
            tier = 2
        out.append({**c, "effect": effect, "card": card, "tier": tier, "obligations": obs})
    return out


def select(pool: list[dict]) -> list[dict]:
    chosen = []
    for (service, mode), n in PER_CELL.items():
        picked = []
        for tier in (0, 1, 2):
            cell = [c for c in pool if c["service"] == service and c["mode"] == mode and c["tier"] == tier]
            random.Random(f"{SEED}-{service}-{mode}-{tier}").shuffle(cell)
            by_test = OrderedDict()
            for c in cell:
                by_test.setdefault(c["test_id"], []).append(c)
            while len(picked) < n and any(by_test.values()):  # one per test before any test gets a second
                for t in list(by_test):
                    if by_test[t] and len(picked) < n:
                        picked.append(by_test[t].pop(0))
        chosen += picked
    return chosen


def case_for(c: dict) -> dict:
    schemas = json.loads((HERE / "schemas.json").read_text())
    tests = {json.loads(l)["test_id"]: json.loads(l)
             for l in (REPO / "datasets/agent-diff-bench/all_numbered.jsonl").read_text().splitlines()}
    t = tests[c["test_id"]]
    info = json.loads(t["info"])
    seed, _service = build(c["variant"])
    key = pk_of(schemas[c["service"]], c["referent_table"])
    if c["mode"] == "absence":
        case_id, form, expected, resolution = "AT-" + c["variant"], "absent", [], "absent"
    else:
        copy_id = c["flags"]["changed"][key[0]]
        case_id, form, expected, resolution = "U-" + c["variant"], "present", \
            [str(x) for x in c["referents"]] + [str(copy_id)], "underspecified"
        assert any(str(r.get(key[0])) == str(copy_id) for r in seed[c["referent_table"]]), c["variant"]
    for x in expected:
        assert any(str(r.get(key[0])) == x for r in seed[c["referent_table"]]), (c["variant"], x)
    if c["mode"] == "absence":
        assert not any(str(r.get(key[0])) in {str(x) for x in c["referents"]} for r in seed[c["referent_table"]])
    ref = {"id": f"{case_id}.r1", "name": c["name"], "description": c["description"], "use": "target",
           "query": {"table": c["referent_table"], "key": key}, "expected": expected, "claims": [], "labels": {},
           "resolution": resolution, "written": c["card"].get("Written attributes") or [], "effect": c["effect"]}
    refs = [ref]
    for i, o in enumerate(c["obligations"], 1):
        if i == c["obligation"] or not o["card"].get("Referent set"):
            continue
        table = o.get("referent_entity")
        if table not in schemas[c["service"]]:
            continue
        refs.append({"id": f"{case_id}.r{len(refs) + 1}", "name": o["card"].get("Grounding obligation name", ""),
                     "description": o["card"].get("Grounding obligation description", "")[:300], "use": "context",
                     "query": {"table": table, "key": pk_of(schemas[c["service"]], table)},
                     "expected": [str(x) for x in o["card"]["Referent set"]], "claims": [], "labels": {},
                     "resolution": o["card"].get("Resolution"), "written": o["card"].get("Written attributes") or [],
                     "effect": None})
    card = {**c["card"], "Test ID": case_id, "Resolution": resolution, "Referent set": expected}
    case = {"case_id": case_id, "domain": c["service"], "form": form, "mode": resolution, "plural": False,
            "acting_user_id": info["impersonate_user_id"], "seed": seed, "prompt": t["question"],
            "references": refs, "probes": [], "cards": [card], "p1_tier": c["tier"],
            "task_spec": [{"line": 1, "text": t["question"], "obligations": [1]}],
            "variant_of": c["test_id"], "p1_variant": c["variant"], "coverage_claims": []}
    case["case_sha256"] = hashlib.sha256(json.dumps(case, sort_keys=True, default=str).encode()).hexdigest()
    return case


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    pool = eligible()
    chosen = select(pool)
    cases = args.out / "cases"
    for c in chosen:
        case = case_for(c)
        dest = cases / case["domain"] / f"{case['case_id']}.json"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(json.dumps(case, ensure_ascii=False) + "\n")
    cells = {}
    for c in pool:
        cells.setdefault(f"{c['service']} {c['mode']}", [0, 0, [0, 0, 0]])[0] += 1
    for c in chosen:
        cells[f"{c['service']} {c['mode']}"][1] += 1
        cells[f"{c['service']} {c['mode']}"][2][c["tier"]] += 1
    (args.out / "p1_selection.json").write_text(json.dumps({
        "rule": __doc__.split("**Which variants**")[1].split("**The case:**")[0].strip(),
        "eligible_and_chosen_by_cell": cells, "chosen": [c["variant"] for c in chosen]}, indent=1) + "\n")
    for k, (n, m, tiers) in sorted(cells.items()):
        print(f"{k:<24} eligible {n:<4} chosen {m} (by tier 0/1/2: {tiers})")
    print(len(chosen), "cases ->", cases)


if __name__ == "__main__":
    main()
