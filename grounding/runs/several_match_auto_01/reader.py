"""The cold reader: a fresh Muse session per case says which records the plural request means.

    AUTOGEN_BACKEND=muse python grounding/runs/fact_coverage_02/launch.py grounding.runs.several_match_auto_01.reader \
        [--cases SMA-... ...] [--concurrency 4]

It sees the request, the acting user, and every record of the kind the request is about, rendered neutrally with
what the agent could see: the fields, the related rows the request's conditions look at, and each record's
container and visibility (the calendar and whether it is hidden in the list; the channel and whether it is private
or archived; the folder path; the team). It never sees the targets, the near-miss claims or the placements.
A case is agreed when the reader's set equals the target set and it is unsure of none of the targets. A trap target
the reader leaves out marks that placement contestable for this request (method.md, check 8).
Writes reader.json.
"""
from __future__ import annotations

import json
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

from grounding.runs.autogen_01.kit import agent
from grounding.runs.fact_coverage_01 import fdc

HERE = Path(__file__).resolve().parent
RUNS = HERE / "runs"
LA = ZoneInfo("America/Los_Angeles")
SERVICE = {"box": "Box", "calendar": "Google Calendar", "linear": "Linear", "slack": "Slack"}
SKIP = {"etag", "sequence", "sequence_id", "ical_uid", "branchName", "url", "sortOrder", "boardOrder",
        "prioritySortOrder", "reactionData", "previousIdentifiers", "customerTicketCount", "version_number",
        "item_status", "collections", "type", "team_id", "organizationId", "file_version_id", "creator_self",
        "organizer_self"}
SCHEMA = {"type": "object", "properties": {
    "ids": {"type": "array", "items": {"type": "string"}},
    "unsure": {"type": "array", "items": {"type": "object", "properties": {"id": {"type": "string"},
                                                                          "why": {"type": "string"}},
                                          "required": ["id", "why"]}},
    "notes": {"type": "string"}}, "required": ["ids", "unsure", "notes"]}
ROLE = """You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it."""
TASK = """A user sent the assistant this request in their {service} workspace:

    "{request}"

The user is {actor}. Below is every {kind} in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {{"ids": [...], "unsure": [{{"id", "why"}}], "notes": "..."}}.

Records:
{records}
"""


def clean(row):
    return {k: v for k, v in row.items() if k not in SKIP and not k.startswith("__") and v not in (None, "", [], {})}


def names(seed, domain):
    if domain == "slack":
        return {u["user_id"]: u.get("real_name") or u.get("username") for u in seed.get("users") or []}
    if domain == "linear":
        return {u["id"]: u.get("name") for u in seed.get("users") or []}
    if domain == "box":
        return {u["id"]: u.get("name") for u in seed.get("box_users") or []}
    return {}


def container(case, row):
    """Where the record lives, and how visible that place is to the acting user."""
    seed, d = case["seed"], case["domain"]
    if d == "calendar" and "calendar_id" in row:
        cal = next((c for c in seed.get("calendars") or [] if c["id"] == row["calendar_id"]), {})
        entry = next((e for e in seed.get("calendar_list_entries") or [] if e.get("calendar_id") == row["calendar_id"]),
                     None)
        return {"calendar": cal.get("summary"), "calendar owner": cal.get("data_owner"),
                "in the user's calendar list": entry is not None,
                "user's access": (entry or {}).get("access_role"), "hidden in the list": (entry or {}).get("hidden"),
                "primary": (entry or {}).get("primary")}
    if d == "slack" and "channel_id" in row:
        ch = next((c for c in seed.get("channels") or [] if c["channel_id"] == row["channel_id"]), {})
        t = datetime.fromisoformat(str(row.get("created_at")).replace("Z", "+00:00"))
        return {"channel": ch.get("channel_name"), "private": ch.get("is_private"), "archived": ch.get("is_archived"),
                "direct message": ch.get("is_dm"), "posted (UTC)": t.astimezone(timezone.utc).isoformat(),
                "posted (user's time zone, Los Angeles)": t.astimezone(LA).isoformat()}
    if d == "linear" and "teamId" in row:
        team = next((t for t in seed.get("teams") or [] if t["id"] == row["teamId"]), {})
        state = next((s for s in seed.get("workflow_states") or [] if s["id"] == row.get("stateId")), {})
        return {"team": team.get("name"), "state": state.get("name")}
    if d == "box" and "parent_id" in row:
        folders = {f["id"]: f for f in seed.get("box_folders") or []}
        path, cur = [], row.get("parent_id")
        while cur is not None and cur in folders and len(path) < 10:
            path.append(folders[cur].get("name"))
            cur = folders[cur].get("parent_id")
        return {"folder path": " / ".join(reversed(path))}
    return {}


def related(seed, table, row, node, depth=0):
    out = {}
    for e in node.get("edges") or []:
        try:
            rows = fdc._joined(seed, table, row, e)
        except ValueError:
            continue
        child = e["node"]["table"]
        items = []
        for c in rows[:12]:
            item = clean(c)
            if depth < 1:
                item.update(related(seed, child, c, e["node"], depth + 1))
            items.append(item)
        out[child] = items
    return out


def render(case):
    ref = case["references"][0]
    q, seed = ref["query"], case["seed"]
    who = names(seed, case["domain"])
    records = []
    for row in seed.get(q["table"]) or []:
        item = {"id": str(fdc.handle(q, row)), **clean(row)}
        for k in ("user_id", "creatorId", "assigneeId", "created_by_id", "modified_by_id", "owned_by_id"):
            if k in item and item[k] in who:
                item[k] = f"{item[k]} ({who[item[k]]})"
        item.update(container(case, row))
        item.update(related(seed, q["table"], row, q))
        records.append(item)
    return records


def actor_name(case):
    seed, a = case["seed"], case.get("acting_user_id")
    return names(seed, case["domain"]).get(a) or a or "the workspace's user"


def read(path: Path, kind: str):
    case = json.loads(path.read_text())
    targets = sorted(str(t) for t in case["references"][0]["expected"])
    prompt = TASK.format(service=SERVICE[case["domain"]], request=case["prompt"], actor=actor_name(case), kind=kind,
                         records=json.dumps(render(case), indent=1, default=str, ensure_ascii=False))
    result = agent.run(agent.Call(
        role="reader", workspace=Path(f"/tmp/sm-auto-01/ws-reader-{case['case_id']}"),
        log_dir=RUNS / "reader" / case["case_id"], calls_log=RUNS / "calls.jsonl", prompt=prompt,
        system_append=ROLE, schema=SCHEMA, label=case["case_id"], timeout=1800))
    ans = agent.structured(result)
    got = sorted(str(i) for i in ans.get("ids") or [])
    unsure = {str(u["id"]): u["why"] for u in ans.get("unsure") or []}
    return case["case_id"], {"agreed": got == targets and not (set(unsure) & set(targets)),
                             "missing": sorted(set(targets) - set(got)), "extra": sorted(set(got) - set(targets)),
                             "unsure": unsure, "notes": ans.get("notes"),
                             "billed": result["cost_usd_billed"], "list": result["total_cost_usd"]}


def main(ids, concurrency):
    from grounding.runs.several_match_auto_01.writer import KIND
    out_path = HERE / "reader.json"
    done = json.loads(out_path.read_text()) if out_path.exists() else {}
    todo = []
    for path in sorted((HERE / "cases").glob("*/SMA-*.json")):
        cid = path.stem
        if (ids and cid not in ids) or (not ids and cid in done):
            continue
        table = json.loads(path.read_text())["references"][0]["query"]["table"]
        todo.append((path, KIND.get(table, (table,))[0].split(" ", 1)[-1]))
    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        for cid, verdict in pool.map(lambda a: read(*a), todo):
            done[cid] = verdict
            out_path.write_text(json.dumps(done, indent=1, ensure_ascii=False) + "\n")
            print(f"{cid:22} agreed={verdict['agreed']} missing={verdict['missing']} extra={verdict['extra']} "
                  f"unsure={list(verdict['unsure'])[:3]}")


if __name__ == "__main__":
    args = sys.argv[1:]
    ids = set(args[args.index("--cases") + 1:]) if "--cases" in args else set()
    ids = {i for i in ids if not i.startswith("--")}
    conc = int(args[args.index("--concurrency") + 1]) if "--concurrency" in args else 4
    main(ids, conc)
