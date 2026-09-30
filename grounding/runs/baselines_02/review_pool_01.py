"""My blind review of the pool `runs/pool_01` (both Sonnet arms and 20 of our Muse tests, under anonymous ids), by
baselines_01's rules ([n0/review_rules.md](../baselines_01/n0/review_rules.md)), written before any agent ran them and
before `manifest.json` was read.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.baselines_02.review_pool_01   # writes the JSON

The record shape is baselines_01's (`n0/review_gen_01.py`, `t()`), keyed by pool id, with the answer key added:
- `target`: the intended record ids (empty when no record is right: a presupposing request or a probe);
- `table`: the table of the records acted on (the candidates);
- `effect`: how the diff shows an action on them: `{"table", "changes": [...], "field"?}` (`field` maps an inserted
  or changed row back to the record, e.g. a comment's `item_id`);
- `labels`: for a request answered in words, the strings that name each candidate.

Families follow the method's table (`autogen_01/kit/docs/method.md`): F7 only for ordered values; a flipped flag or a
missing relation is F0 unless it offers a substitute; paraphrase is never a substitute.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "runs" / "pool_01" / "review.json"


def r(pid, form, facts, target=(), table=None, effect=None, near=(), far=(), proper=(), flaws=(), quality=(),
      oracle_ok=True, oracle_note="", labels=None, note=""):
    return {"pool_id": pid, "form": form, "facts_exercised": list(facts), "target": [str(x) for x in target],
            "table": table, "effect": effect, "labels": labels or {},
            "near_misses": [dict(zip(("record", "fact", "family", "note"), n)) for n in near],
            "far": list(far), "proper": list(proper), "valid": not flaws,
            "flaws": [dict(zip(("cause", "note"), f)) for f in flaws], "quality": list(quality),
            "oracle_sound": oracle_ok, "oracle_note": oracle_note, "note": note}


def upd(table, field=None, columns=None):
    e = {"table": table, "key": ["id"], "changes": ["update"]}
    if field:
        e["field"] = field
    if columns:
        e["columns"] = columns
    return e


def ins(table, field):
    return {"table": table, "key": ["id"], "field": field, "changes": ["insert"]}


REVIEW = [
]


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(REVIEW, indent=1, ensure_ascii=False) + "\n")
    print(json.dumps({"reviewed": len(REVIEW), "valid": sum(r["valid"] for r in REVIEW),
                      "forms": Counter(r["form"] for r in REVIEW),
                      "flaw_causes": Counter(f["cause"] for r in REVIEW for f in r["flaws"])}))


if __name__ == "__main__":
    main()
