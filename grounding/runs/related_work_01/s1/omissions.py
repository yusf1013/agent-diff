"""Which of a plural request's targets its own assertions would notice missing (no model calls).

A target is pinned when an assertion's `where` names its id (eq, or an `in` list); a group of targets is counted when
an assertion on their table fixes an exact count equal to the number of targets; any other target could be left out
and the test would still pass (the invisible ones). Run: python -m grounding.runs.related_work_01.s1.omissions
"""
import json
from pathlib import Path

from grounding.runs.related_work_01.s1.probes import PROBES, SAME_AS

REPO = Path(__file__).resolve().parents[4]
HERE = Path(__file__).parent
ID_FIELDS = {"message_id", "channel_id", "user_id", "id", "item_id", "file_id", "issueId", "issue_id"}


def ids_in_where(where):
    out = set()
    for field, pred in (where or {}).items():
        if not isinstance(pred, dict):
            out.add(str(pred))
            continue
        for op, val in pred.items():
            if op in ("eq",) and isinstance(val, (str, int)):
                out.add(str(val))
            if op == "in" and isinstance(val, list):
                out |= {str(v) for v in val}
    return out


def main():
    tests = {json.loads(l)["test_id"]: json.loads(l) for l in (REPO / "datasets/agent-diff-bench/all_numbered.jsonl").read_text().splitlines()}
    rows = []
    pairs = [(tid, oi) for tid, oi, _k, _p in PROBES] + [(t, next(o for tt, o, _k, _p in PROBES if tt == s)) for t, s in SAME_AS.items()]
    for tid, oi in pairs:
        service = tid.split("_")[0]
        card = next(t for t in json.loads((REPO / f"grounding/domains/{service}/analysis/analysis.json").read_text())
                    if t["test_id"] == tid)["obligations"][oi - 1]["card"]
        targets = [str(t) for t in card["Referent set"]]
        assertions = json.loads(tests[tid]["answer"])["assertions"]
        pinned = set()
        for a in assertions:
            pinned |= ids_in_where(a.get("where")) & set(targets)
        exact_counts = [a for a in assertions if isinstance(a.get("expected_count"), int) and
                        a["expected_count"] == len(targets) and not (ids_in_where(a.get("where")) & set(targets))]
        invisible = [t for t in targets if t not in pinned] if not exact_counts else []
        rows.append({"test": tid, "obligation": oi, "targets": len(targets), "pinned": len(pinned),
                     "exact_count_assertion": bool(exact_counts), "invisible_if_omitted": len(invisible)})
    (HERE / "omissions.json").write_text(json.dumps(rows, indent=1) + "\n")
    for r in rows:
        print(f"{r['test']:<10} O{r['obligation']} targets={r['targets']:<3} pinned={r['pinned']:<3} "
              f"exact count={r['exact_count_assertion']!s:<5} invisible if omitted={r['invisible_if_omitted']}")
    tot = sum(r["targets"] for r in rows)
    inv = sum(r["invisible_if_omitted"] for r in rows)
    blind = sum(r["invisible_if_omitted"] > 0 for r in rows)
    print(f"{len(rows)} plural obligations, {tot} targets; {inv} targets invisible if omitted; "
          f"{blind} obligations whose assertions miss at least one omission")


if __name__ == "__main__":
    main()
