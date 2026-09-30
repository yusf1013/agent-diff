"""Per generation batch (runs/gen_*): attempts, accepted, rejected and why, versions and rounds, calls and cost. No
model calls; plain python3 is enough.

    python3 grounding/runs/regen_01/batches.py [--json]

Costs are Muse's list price (muse-spark-1.3, the number reports use) and the billed contributor price, summed from
each run's calls.jsonl. A brief with no outcome.json is still running, or stopped (error.txt).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def batch(gen: Path) -> dict:
    calls = [json.loads(line) for line in (gen / "calls.jsonl").read_text().splitlines()] \
        if (gen / "calls.jsonl").exists() else []
    briefs = {}
    for folder in sorted(p for p in gen.glob("G4-*") if p.is_dir()):
        o = json.loads((folder / "outcome.json").read_text()) if (folder / "outcome.json").exists() else None
        if o is None:
            briefs[folder.name] = {"status": "error" if (folder / "error.txt").exists() else "running"}
            continue
        last = o["history"][-1] if o["history"] else {}
        briefs[folder.name] = {"status": o["status"], "versions": o["versions"], "check_rounds": o["check_rounds"],
                               "reader_rounds": o["reader_rounds"], "seconds": o["seconds"],
                               **({"why": f"{last.get('stage')}: " + " | ".join(p[:300] for p in last.get("problems", []))}
                                  if o["status"] != "accepted" else {})}
    by = lambda s: sorted(k for k, v in briefs.items() if v["status"] == s)  # noqa: E731
    return {"run": gen.name, "attempts": len(briefs), "accepted": by("accepted"), "rejected": by("rejected"),
            "errors": by("error"), "running": by("running"), "briefs": briefs, "calls": len(calls),
            "writer_calls": sum(c["role"] == "writer" for c in calls),
            "reader_calls": sum(c["role"] == "reader" for c in calls),
            "failed_calls": sum(bool(c.get("is_error")) for c in calls),
            "cost_usd_list": round(sum(c.get("cost_usd_list_price") or 0 for c in calls), 4),
            "cost_usd_billed": round(sum(c.get("cost_usd_billed") or 0 for c in calls), 4),
            "input_tokens": sum(c.get("input_tokens") or 0 for c in calls),
            "cached_input_tokens": sum(c.get("cache_read_input_tokens") or 0 for c in calls),
            "output_tokens": sum(c.get("output_tokens") or 0 for c in calls)}


def main():
    rows = [batch(g) for g in sorted((HERE / "runs").glob("gen_*")) if g.is_dir()]
    if "--json" in sys.argv:
        print(json.dumps(rows, indent=1))
        return
    for r in rows:
        print(f"{r['run']}: {r['attempts']} attempts, {len(r['accepted'])} accepted, {len(r['rejected'])} rejected, "
              f"{len(r['errors'])} errors, {len(r['running'])} running; {r['calls']} calls ({r['writer_calls']} writer, "
              f"{r['reader_calls']} reader, {r['failed_calls']} failed); ${r['cost_usd_list']:.2f} list, "
              f"${r['cost_usd_billed']:.3f} billed")
        for sid, b in r["briefs"].items():
            extra = f" v{b['versions']} (checks {b['check_rounds']}, reader {b['reader_rounds']}, {b['seconds']}s)" \
                if "versions" in b else ""
            print(f"  {sid}: {b['status']}{extra}{' | ' + b['why'][:300] if b.get('why') else ''}")
    total = lambda k: sum(r[k] for r in rows)  # noqa: E731
    print(f"all: {total('attempts')} attempts, {sum(len(r['accepted']) for r in rows)} accepted; {total('calls')} "
          f"calls; ${total('cost_usd_list'):.2f} list, ${total('cost_usd_billed'):.3f} billed")


if __name__ == "__main__":
    main()
