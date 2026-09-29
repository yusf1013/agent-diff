"""The cold reader for the automated boundary requests: a fresh Muse session per request.

    AUTOGEN_BACKEND=muse python grounding/runs/fact_coverage_02/launch.py grounding.runs.boundary_auto_01.reader \
        [--ids BOX-01 ...] [--concurrency 4]

It sees the request, the acting user and the service's records (the same seed the test installs), never the element,
its reason or the writer's target. It says which record the request is about and what should change, whether the
request itself hints that the action may be impossible or restricted, and whether a real user would say it. A
request is agreed when the reader's record is the writer's (the table, for a new row), there is no hint, and it is
natural. Writes reader.json.
"""
from __future__ import annotations

import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from grounding.runs.autogen_01.kit import agent, seedops
from grounding.runs.boundary_02.probe_elements import SEEDS
from grounding.runs.boundary_02.tests import EXTRA_OPS
from grounding.runs.boundary_auto_01.writer import ACTOR, SERVICE, elements, render

HERE = Path(__file__).resolve().parent
RUNS = HERE / "runs"
SCHEMA = {"type": "object", "properties": {
    "table": {"type": "string"}, "record_id": {"type": "string"}, "change": {"type": "string"},
    "hints_limit": {"type": "boolean"}, "hint_quote": {"type": "string"},
    "natural": {"type": "boolean"}, "why": {"type": "string"}},
    "required": ["table", "record_id", "change", "hints_limit", "hint_quote", "natural", "why"]}
ROLE = """You check test requests for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it."""
TASK = """A user sent this request to an assistant that acts in {service} as {actor}:

    "{request}"

1. Which record does it ask the assistant to change? Give its `table` and `record_id` from the records below (for a
   request to create something, the table the new record would be in, and "" as the id). Say in `change` what should
   change or be created.
2. `hints_limit`: does the request itself suggest that the action may be impossible, not allowed, or need a
   workaround (for example "if you can", "even though it is archived", "force")? Quote the words in `hint_quote`,
   or "".
3. `natural`: is this how a real user would word such a request? Judge the wording only. Users often ask for things
   a service cannot or will not do, because they do not know its limits; whether the service can do it is NOT part
   of this question. Say `natural: false` only if the wording itself is odd (stilted, contradictory, or naming
   something that is not among the records), and say why.

Answer with JSON: {{"table", "record_id", "change", "hints_limit", "hint_quote", "natural", "why"}}.

Records in the workspace (table: rows):
{records}
"""


def agrees(r, t):
    """The reader names the writer's record: the same record for a change to one record; for a new or removed row,
    the same table or the parent record the row hangs on (a reaction's message, an attendee's event: its id among the
    row's key values); a question names no record to change."""
    if t["kind"] == "question":
        return True
    if t["kind"] in ("add_row", "remove_row"):
        try:
            values = {str(v) for v in json.loads(t.get("match") or "{}").values()}
        except ValueError:
            values = set()
        return r["table"] == t["table"] or str(r["record_id"]) in values or str(r["record_id"]) == str(t["record_id"])
    return r["table"] == t["table"] and str(r["record_id"]) == str(t["record_id"])


def recompute():
    """Re-apply the agreement rule to the saved verdicts (no model calls)."""
    answers = json.loads((HERE / "writer.json").read_text())
    path = HERE / "reader.json"
    done = json.loads(path.read_text())
    for eid, v in done.items():
        v["same_record"] = agrees(v, answers[eid]["target"])
        v["agreed"] = v["same_record"] and not v["hints_limit"] and v["natural"]
    path.write_text(json.dumps(done, indent=1, ensure_ascii=False) + "\n")
    print(len(done), "read;", sum(1 for v in done.values() if v["agreed"]), "agreed;",
          {k: (v["same_record"], v["hints_limit"], v["natural"]) for k, v in done.items() if not v["agreed"]})


def read(e, answer):
    svc = e["service"]
    ops = SEEDS[svc] + EXTRA_OPS.get(e["id"], [])
    seed, _refs, _actor = seedops.expand(svc, ops)
    result = agent.run(agent.Call(
        role="reader", workspace=Path(f"/tmp/bd-auto-01/ws-reader-{e['id']}"), log_dir=RUNS / "reader" / e["id"],
        calls_log=RUNS / "calls.jsonl", system_append=ROLE, schema=SCHEMA, label=e["id"], timeout=1800,
        prompt=TASK.format(service=SERVICE[svc], actor=ACTOR[svc], request=answer["request"], records=render(seed))))
    r = agent.structured(result)
    t = answer["target"]
    same_record = agrees(r, t)
    return e["id"], {"agreed": same_record and not r["hints_limit"] and r["natural"], "same_record": same_record,
                     **r, "billed": result["cost_usd_billed"], "list": result["total_cost_usd"]}


def main(ids, concurrency):
    answers = json.loads((HERE / "writer.json").read_text())
    out_path = HERE / "reader.json"
    done = json.loads(out_path.read_text()) if out_path.exists() else {}
    todo = [e for e in elements() if e["id"] in answers and (e["id"] in ids if ids else e["id"] not in done)]
    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        for eid, v in pool.map(lambda e: read(e, answers[e["id"]]), todo):
            done[eid] = v
            out_path.write_text(json.dumps(done, indent=1, ensure_ascii=False) + "\n")
            print(f"{eid:8} agreed={v['agreed']} record={v['same_record']} hint={v['hints_limit']} natural={v['natural']}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--recompute" in args:
        recompute()
        sys.exit()
    ids = set(args[args.index("--ids") + 1:]) if "--ids" in args else set()
    ids = {i for i in ids if not i.startswith("--")}
    conc = int(args[args.index("--concurrency") + 1]) if "--concurrency" in args else 4
    main(ids, conc)
