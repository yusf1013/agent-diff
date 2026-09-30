"""Print the drop-F variants of a derivation run for my read before any runs (the standing rule; its question: can
the action be done to each intended match?): per variant, its status, the dropped fact and words, the scenario's
request and the variant's, every intended match and every near miss left, with the cold reader's note on each record,
and the writer's reasons. Only I read this; it never reaches an agent. No model calls; plain python3 is enough.

    python3 grounding/runs/regen_01/variant_view.py DROPF_DIR [UNIT ...] [--accepted]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def original(sid: str) -> dict:
    for gen in sorted((HERE / "runs").glob("gen_*")):
        path = gen / sid / "case.json"
        if path.exists() and json.loads((gen / sid / "outcome.json").read_text())["status"] == "accepted":
            return json.loads(path.read_text())
    return {}


def main():
    folder = Path(sys.argv[1])
    only = {a for a in sys.argv[2:] if not a.startswith("--")}
    accepted_only = "--accepted" in sys.argv
    for rec_path in sorted(folder.glob("U-*/record.json")):
        rec = json.loads(rec_path.read_text())
        if only and rec["id"] not in only:
            continue
        if accepted_only and rec["status"] != "accepted":
            continue
        case = original(rec["scenario"])
        print(f"\n{'#' * 90}\n## {rec['id']} [{rec['status']}] fact {rec['fact']} (dropped {rec.get('dropped_facts')}), "
              f"{rec.get('matches')} matches, {rec.get('other_near_misses')} near misses left")
        print(f"ORIGINAL: {case.get('prompt')}")
        last = rec["rounds"][-1] if rec.get("rounds") else {}
        w = last.get("writer", {})
        print(f"VARIANT:  {w.get('request')}\n  removed: {w.get('removed_words')!r}; writer: {w.get('reason')}")
        if rec["status"] != "accepted":
            print(f"  PROBLEMS: {rec.get('problems')}")
        vpath = rec_path.parent / "variant.json"
        if not vpath.exists():
            continue
        v = json.loads(vpath.read_text())
        ref = v["references"][0]
        notes = {str(r["id"]): r for r in (last.get("reader", {}).get("turn2", {}).get("records") or [])}
        claims = {str(c["witness"]): c for c in ref.get("claims", [])}
        for x in ref["expected"]:
            n = notes.get(str(x), {})
            print(f"  MATCH {x}: fails {n.get('fails')} {'(contestable)' if n.get('contestable') else ''} | {n.get('note')}")
        for x, c in claims.items():
            n = notes.get(x, {})
            print(f"  NEAR MISS {x} ({c['requirement']}): reader fails {n.get('fails')} | {n.get('note')}")
        t2 = last.get("reader", {}).get("turn2", {})
        print(f"  reader: one={t2.get('asks_for_one')} natural={t2.get('natural')} faithful={t2.get('faithful')} | "
              f"{t2.get('naturalness_note')} | {t2.get('differences')}")


if __name__ == "__main__":
    main()
