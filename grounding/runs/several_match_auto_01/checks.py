"""Check 2 of method.md on the hard cases: every shortcut, run as API calls on the case's own seed.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.several_match_auto_01.checks [SMA-...-H ...]

The shortcut table and its parameters come from the request's kind (several_match_02/strategies.py): calendar
events on the user's calendars; Box files anywhere or in a named folder; Linear issues in a team; Slack messages in
a named channel or anywhere. The parameters are the case's own: the target's day and time zone, its folder and
extension, its team, its channel, and the writer's search words. For each shortcut: the targets it misses. The
thorough route must find every target; a shortcut that misses one is defeated. Writes checks.json.
"""
from __future__ import annotations

import json
import os
import sys
from datetime import date, timedelta
from pathlib import Path

from grounding.runs.several_match_02 import strategies
from grounding.runs.several_match_auto_01 import seedkit
from grounding.runs.several_match_auto_01.build import pinned

HERE = Path(__file__).resolve().parent
DB = os.environ.get("DATABASE_URL", "postgresql://postgres@127.0.0.1:15432/agentdiff_campaign")
BASE = os.environ.get("AGENTDIFF_BASE_URL", "http://127.0.0.1:18001")


def plan(case, words):
    """The shortcut table and its parameters for this case."""
    ref = case["references"][0]
    q = ref["query"]
    table = q["table"]
    target = seedkit.find_row(case, table, str(ref["expected"][0]))
    if table == "calendar_events":
        start = target["start"] if isinstance(target["start"], dict) else json.loads(target["start"])
        stamp = start.get("dateTime") or f"{start.get('date')}T00:00:00+00:00"
        day, offset = stamp[:10], stamp[19:] or "+00:00"
        nxt = (date.fromisoformat(day) + timedelta(days=1)).isoformat()
        return "calendar", {"from": f"{day}T00:00:00{offset}", "to": f"{nxt}T00:00:00{offset}", "q": words}
    if table == "box_files":
        ext = str(target.get("extension") or str(target.get("name")).rpartition(".")[2])
        if pinned(q):
            return "box", {"folder": target["parent_id"], "words": words, "ext": ext, "person": "Leo"}
        return "box-anywhere", {"folder": "0", "guess": target["parent_id"], "words": words, "ext": ext}
    if table == "issues":
        team = next(t for t in case["seed"]["teams"] if t["id"] == target["teamId"])
        name = team["name"]
        return "linear", {"team": name, "filtered":
                          f'{{ issues(first: 250, filter: {{team: {{name: {{eq: "{name}"}}}}}}) {{ nodes {{ id }} }} }}'}
    if table == "messages":
        chan = next(c for c in case["seed"]["channels"] if c["channel_id"] == target["channel_id"])
        if pinned(q):
            return "slack", {"prefix": chan["channel_name"], "search": words, "channel": chan["channel_id"]}
        return "slack-messages", {"search": words}
    return None, None


def main(ids):
    from agent_diff import AgentDiff
    answers = json.loads((HERE / "writer.json").read_text())
    client, engine = AgentDiff(base_url=BASE), strategies.engine_for(DB)
    out_path = HERE / "checks.json"
    done = json.loads(out_path.read_text()) if out_path.exists() else {}
    for path in sorted((HERE / "cases").glob("*/SMA-*-H.json")):
        cid = path.stem
        if (ids and cid not in ids) or (not ids and cid in done):
            continue
        case = json.loads(path.read_text())
        words = (answers.get(case["source_cover"]) or {}).get("search_words") or ""
        table, entry = plan(case, words)
        if not table:
            continue
        probe = {"id": cid, "domain": case["domain"], "place": "the hard case's own seed", "seed_tables": case["seed"],
                 "actor": case["acting_user_id"], "targets": [str(t) for t in case["references"][0]["expected"]],
                 "entry": entry, "strategies": table}
        try:
            r = strategies.run_probe(client, engine, probe)
        except Exception as exc:  # recorded: the case cannot be checked
            done[cid] = {"error": f"{type(exc).__name__}: {exc}"[:400]}
            print(cid, "ERROR", done[cid]["error"][:150])
            continue
        s = r["strategies"]
        lazy = {n: v for n, v in s.items() if not v.get("thorough")}
        thorough_ok = all(not v.get("missed") and "error" not in v for v in s.values() if v.get("thorough"))
        done[cid] = {"table": table, "entry": entry, "strategies": s, "thorough_finds_all": thorough_ok,
                     "defeated": sorted(n for n, v in lazy.items() if v.get("missed")),
                     "not_defeated": sorted(n for n, v in lazy.items() if not v.get("missed") and "error" not in v),
                     "errors": sorted(n for n, v in s.items() if "error" in v)}
        out_path.write_text(json.dumps(done, indent=1, default=str) + "\n")
        print(f"{cid:22} thorough={thorough_ok} defeated {len(done[cid]['defeated'])}/{len(lazy)} "
              f"errors={done[cid]['errors']}")
    engine.dispose()


if __name__ == "__main__":
    main(set(sys.argv[1:]))
