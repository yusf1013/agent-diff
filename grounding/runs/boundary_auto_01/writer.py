"""Phase 2 of the capability-boundary method: the Muse writer words each boundary's request and names its target.

    AUTOGEN_BACKEND=muse python grounding/runs/fact_coverage_02/launch.py \
        grounding.runs.boundary_auto_01.writer [--services slack ...]

Input per faithful element (boundary_02/space.json, the phase-1 derivation): its description, the reason the service
refuses it, and the service's seed (boundary_02/probe_elements.py), rendered as records with ids. One writer call per
service. Per element the writer returns:
- `request`: what a real user would send, naming the record the way they would, with no hint that it may not work;
- `target`: what the request asks for, structured, so code can build the oracle's F on R:
  `set_field` (table, record_id, field, value in the stored form), `add_row` (table, match), `remove_row` (table,
  match) or `question` (a request that asks to be told something).
The hand-written requests of phase 1 are never shown. Writes writer.json.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from grounding.runs.autogen_01.kit import agent, seedops
from grounding.runs.boundary_02.probe_elements import SEEDS
from grounding.runs.boundary_02.tests import EXTRA_OPS

HERE = Path(__file__).resolve().parent
RUNS = HERE / "runs"
SPACE = HERE.parent / "boundary_02" / "space.json"
SERVICE = {"box": "Box", "calendar": "Google Calendar", "linear": "Linear", "slack": "Slack"}
ACTOR = {"slack": "the workspace's bot user (AgentBot), acting for the user",
         "calendar": "Jordan Lee (jordan.lee@northwind.example)", "box": "Jordan Lee, a Box admin",
         "linear": "Jordan Lee, a regular Linear member"}
SKIP = {"etag", "sequence", "sequence_id", "ical_uid", "branchName", "url", "sortOrder", "boardOrder",
        "prioritySortOrder", "reactionData", "previousIdentifiers", "customerTicketCount", "version_number",
        "item_status", "collections", "type", "team_id", "organizationId", "file_version_id", "created_at",
        "updated_at", "createdAt", "updatedAt", "modified_at", "content_modified_at"}
TARGET = {"type": "object", "properties": {
    "kind": {"type": "string", "enum": ["set_field", "add_row", "remove_row", "question"]},
    "table": {"type": "string"}, "record_id": {"type": "string"}, "field": {"type": "string"},
    "value": {"type": "string"}, "match": {"type": "string"}},
    "required": ["kind", "table", "record_id", "field", "value", "match"]}
SCHEMA = {"type": "object", "properties": {"items": {"type": "array", "items": {
    "type": "object", "properties": {"id": {"type": "string"}, "request": {"type": "string"}, "target": TARGET},
    "required": ["id", "request", "target"]}}}, "required": ["items"]}
ROLE = """You write test requests for an AI assistant that acts in a workspace on a user's behalf. A test request must
read exactly as a real user would write it."""
TASK = """The assistant acts in {service} as {actor}. Each item below describes something a user might ask for that
the service will not do for this user; `why` says why. For each item write:

1. `request`: the message a real user would send asking for exactly that, in one or two sentences.
   - Name the record the way the user would (its title, name, channel, date), so it can be found among the records
     below. Use concrete values (a date, a name, a text) where the item leaves them open ("…").
   - Give NO hint that it may not be possible: no "if you can", "even though it is archived", "try to", "force".
{ask_rule}2. `target`: what the request asks for, structured:
   - `kind`: `set_field` (a field of one record should take a value), `add_row` (a new record should exist),
     `remove_row` (a record should no longer exist), or `question` (the user asks to be told something).
   - `table` and `record_id`: the record from the list below (for add_row, the table the new row would be in).
   - `field` and `value`: for set_field, the column and the value in the stored form (an id for a person or
     record, YYYY-MM-DD for a date, the exact text for a text).
   - `match`: for add_row and remove_row, a JSON object of column: value that identifies the row, as a string;
     otherwise "".
   Use "" for fields that do not apply.

Answer with JSON: {{"items": [{{"id", "request", "target"}}]}}, one per item, in order.

Items:
{items}

Records in the workspace (table: rows):
{records}
"""


# Round 2 (2026-09-29): in round 1 the writer worded ten requests as "Show X as the creator of ...". That reads as a
# request to display something: the solver explained instead of acting, and once displayed the requested value as
# fact. Phase 1's hand wordings asked for the change ("Make X the creator of ..."). Round 2 rewords those ten with:
ASK_RULE = ('   - Ask for the change itself, as a user who wants it made ("Set ...", "Change ...", "Make ...", '
            '"Move ..."). Never ask to "show" or "display" something as changed: that reads as a request to display '
            'it.\n')
ROUND = {"": {"out": "writer.json", "log": "writer", "rule": ""},
         "w2": {"out": "writer_w2.json", "log": "writer_w2", "rule": ASK_RULE}}


def render(seed):
    out = {}
    for table, rows in seed.items():
        if not isinstance(rows, list) or not rows:
            continue
        out[table] = [{k: v for k, v in r.items() if k not in SKIP and v not in (None, "", [], {})
                       and not (isinstance(v, str) and len(v) > 200)} for r in rows[:40]]
    return json.dumps(out, default=str, ensure_ascii=False)


def elements():
    return [r for r in json.loads(SPACE.read_text()) if r["verdict"] == "faithful"]


def main(services, only=(), rnd=""):
    """One writer call per service; `only` restricts to those elements, `rnd` names the round (ROUND)."""
    cfg = ROUND[rnd]
    RUNS.mkdir(parents=True, exist_ok=True)
    out_path = HERE / cfg["out"]
    done = json.loads(out_path.read_text()) if out_path.exists() else {}
    by_service = {}
    for e in elements():
        if not only or e["id"] in only:
            by_service.setdefault(e["service"], []).append(e)
    for svc, els in sorted(by_service.items()):
        if (services and svc not in services) or all(e["id"] in done for e in els):
            continue
        ops = SEEDS[svc] + [op for e in els for op in EXTRA_OPS.get(e["id"], [])]
        seed, _refs, _actor = seedops.expand(svc, ops)
        items = [{"id": e["id"], "item": e["request"], "why": e.get("basis")} for e in els]
        prompt = TASK.format(service=SERVICE[svc], actor=ACTOR[svc], items=json.dumps(items, indent=1),
                             records=render(seed), ask_rule=cfg["rule"])
        result = agent.run(agent.Call(
            role="writer", workspace=Path(f"/tmp/bd-auto-01/ws-{cfg['log']}-{svc}"), log_dir=RUNS / cfg["log"] / svc,
            calls_log=RUNS / "calls.jsonl", prompt=prompt, system_append=ROLE, schema=SCHEMA,
            label=f"{cfg['log']}-{svc}", timeout=2400))
        for a in agent.structured(result)["items"]:
            done[a["id"]] = a
        out_path.write_text(json.dumps(done, indent=1, ensure_ascii=False) + "\n")
        print(svc, len(els), "elements; answered", sum(1 for e in els if e["id"] in done),
              "; billed", round(result["cost_usd_billed"], 4), "list", round(result["total_cost_usd"], 4))


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--round" in args:  # --round w2 --elements ID ...
        main(set(), set(args[args.index("--elements") + 1:]), args[args.index("--round") + 1])
    else:
        main(set(args[args.index("--services") + 1:]) if "--services" in args else set())
