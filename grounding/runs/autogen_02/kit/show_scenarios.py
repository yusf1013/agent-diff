"""Print the accepted scenarios of a generation run for my validity review: the request, the author's conditions,
the target and every near miss with the author's explanation and the record, and the generation history.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.kit.show_scenarios RUN_DIR [ID ...]
"""
import json
import sys
from pathlib import Path

from grounding.runs.autogen_01.kit.bundle import compact_row


def main():
    run = Path(sys.argv[1]).resolve()
    only = set(sys.argv[2:])
    for outcome_path in sorted(run.glob("*/outcome.json")):
        o = json.loads(outcome_path.read_text())
        sid = o["scenario_id"]
        if only and sid not in only:
            continue
        print(f"\n{'#' * 100}\n## {sid} [{o['status']}] versions {o['versions']}, check rounds {o['check_rounds']}, "
              f"reader rounds {o['reader_rounds']}, {o.get('seconds')}s; brief {o['brief']['facts']}")
        for h in o.get("history", []):
            if h.get("problems"):
                print(f"   v{h['version']} {h['stage']}: " + " | ".join(p[:220] for p in h["problems"]))
        case_path = outcome_path.parent / "case.json"
        if not case_path.exists():
            continue
        case = json.loads(case_path.read_text())
        print(f"REQUEST: {case['prompt']}")
        for c in case.get("conditions", []):
            print(f"  {c['id']}: {c['text']}  {c['facts']}")
        ref = case["references"][0]
        table, key = ref["query"]["table"], ref["query"].get("key", ["id"])[0]
        rows = {str(r.get(key)): r for r in case["seed"].get(table, [])}
        for t in ref["expected"]:
            print(f"  TARGET {t}: {compact_row(rows.get(str(t), {}), 500)}")
        for cl in ref["claims"]:
            flag = f" [reader: {cl['contestable'][:120]}]" if cl.get("contestable") else ""
            print(f"  DECOY {cl['witness']} ({cl['requirement']}, {cl.get('family')}): {cl['explanation']}{flag}")
            print(f"     {compact_row(rows.get(str(cl['witness']), {}), 400)}")
        others = [k for k in rows if k not in {str(x) for x in ref["expected"]} | {str(c["witness"]) for c in ref["claims"]}]
        if others:
            print(f"  other {table} rows: {others}")


if __name__ == "__main__":
    main()
