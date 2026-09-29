"""The creative step: the Muse writer turns single-target covers into plural requests.

    AUTOGEN_BACKEND=muse python grounding/runs/fact_coverage_02/launch.py \
        grounding.runs.several_match_auto_01.writer [--domains box ...]

One writer call per service, over every cover of that service (population.py). For each cover the writer says:
- whether a real user could plausibly ask the same thing about several records (plural_worthy, with the reason);
- the plural request: every condition kept, none added, the action kept, and nothing said about where the records
  are beyond what the original says (method.md, check 8);
- the words a user would type into the service's search to find such records (the search shortcut's words);
- three other values of the record's main text that a real record could have while still meeting every condition
  (the extra matches' texts; code checks each one against the reference query).
Code then checks the wording for hiding-place words the original did not use. Writes writer.json.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from grounding.runs.autogen_01.kit import agent
from grounding.runs.several_match_auto_01.population import covers

HERE = Path(__file__).resolve().parent
RUNS = HERE / "runs"
# The record kind a cover's query selects, and the text column its extra matches vary.
KIND = {"messages": ("a Slack message", "message_text"), "issues": ("a Linear issue", "title"),
        "calendar_events": ("a Google Calendar event", "summary"), "box_files": ("a Box file", "name"),
        "channels": ("a Slack channel", "channel_name"), "box_folders": ("a Box folder", "name"),
        "calendar_list_entries": ("an entry in the user's Google Calendar list", "summary_override"),
        "calendars": ("a Google Calendar calendar", "summary"), "documents": ("a Linear document", "title"),
        "box_tasks": ("a Box task", "message"), "comments": ("a Linear comment", "body"),
        "cycles": ("a Linear cycle", "name"), "attachments": ("a Linear attachment", "title"),
        "users": ("a Slack user", "real_name"), "teams": ("a Linear team", "name"),
        "projects": ("a Linear project", "name"), "box_hubs": ("a Box hub", "title"),
        "calendar_acl_rules": ("a sharing rule on a calendar", "role")}
SERVICE = {"box": "Box", "calendar": "Google Calendar", "linear": "Linear", "slack": "Slack"}
HIDING = re.compile(r"\b(including|hidden|private|archived|subfolders?|sub-folders?|sub-teams?|any calendar|"
                    r"all (my |of my )?calendars|every calendar|all channels|every channel|any channel|every page|"
                    r"all pages|anywhere|wherever|nested|inside any)\b", re.I)
# When the records are themselves channels or calendars, "every channel" is the plural request, not a hiding place.
OWN_KIND = {"channels": "channel", "calendars": "calendar", "calendar_list_entries": "calendar"}
SCHEMA = {"type": "object", "properties": {"items": {"type": "array", "items": {
    "type": "object", "properties": {
        "id": {"type": "string"}, "plural_worthy": {"type": "boolean"}, "reason": {"type": "string"},
        "plural_request": {"type": "string"}, "search_words": {"type": "string"},
        "variants": {"type": "array", "items": {"type": "string"}}},
    "required": ["id", "plural_worthy", "reason", "plural_request", "search_words", "variants"]}}},
    "required": ["items"]}
ROLE = """You write test requests for an AI agent that acts in a workspace on a user's behalf. You are careful with
wording: a test request must read exactly as a real user would write it, and must ask for exactly what is intended."""
TASK = """Each item below is a request that asks the agent to act on ONE record in {service}. For each item:

1. Decide `plural_worthy`: could a real user plausibly ask the same thing about SEVERAL records at once, because
   several records can meet the same conditions? (Example: "Cancel the 8 a.m. meeting with Dana" -> "Cancel all the
   8 a.m. meetings with Dana" is plausible.) Answer false when the request picks out one record by something only
   one record can have (an exact unique title or name, "the most recent", "the one that...", a record the
   conditions make unique by nature), or when doing the action to several records makes no sense. Give the reason.
2. Write `plural_request`: the request rewritten to ask for every record that meets the same conditions.
   - Keep every condition of the original, word for word where you can, and add no new condition.
   - Keep the action and its values (tags, dates, names, emoji) unchanged.
   - Say it the way a user would ("every", "all", plural nouns).
   - Do not say where the records are beyond what the original says: no "including ...", "on any calendar",
     "in all channels", "hidden", "private", "archived", "subfolders", "every page", "anywhere".
   If `plural_worthy` is false, still write your best plural wording.
3. Write `search_words`: the one to three words a user would type into {service}'s search box to look for these
   records (content words, no search operators).
4. Write `variants`: three different values of the record's {field} that a real record meeting EVERY condition of
   the request could have. Keep every word or phrase a condition needs (a quoted phrase, a topic, a file extension,
   a name the condition checks) and change the rest, so the three read like three different real records.
   The current value is given. Keep each variant about as long as the current value.

Answer with JSON: {{"items": [{{"id", "plural_worthy", "reason", "plural_request", "search_words", "variants"}}]}},
one entry per item, in the same order.

Items:
{items}
"""


def target_row(case):
    """The referent's row and its table, from the reference query's root table."""
    ref = case["references"][0]
    table = ref["query"]["table"]
    from grounding.runs.several_match_auto_01.seedkit import find_row
    return table, find_row(case, table, ref["expected"][0])


def items_for(cases):
    out = []
    for c in cases:
        table, row = target_row(c)
        kind, field = KIND.get(table, (f"a record in {table}", "name"))
        out.append({"id": c["case_id"], "record": kind, "request": c["prompt"],
                    "text_field": field, "current_value": (row or {}).get(field)})
    return out


def check(item, original, table=None):
    """Code checks on one answer: hiding-place words the original did not use."""
    problems = []
    new_words = {m.group(0).lower() for m in HIDING.finditer(item["plural_request"])} - \
        {m.group(0).lower() for m in HIDING.finditer(original)}
    if table in OWN_KIND:
        new_words = {w for w in new_words if OWN_KIND[table] not in w}
    if new_words:
        problems.append(f"names a hiding place: {sorted(new_words)}")
    if len(item["variants"]) < 2:
        problems.append("fewer than 2 variants")
    return problems


def main(domains):
    RUNS.mkdir(parents=True, exist_ok=True)
    out_path = HERE / "writer.json"
    done = json.loads(out_path.read_text()) if out_path.exists() else {}
    by_domain = {}
    for c in covers():
        by_domain.setdefault(c["domain"], []).append(c)
    for domain, cases in sorted(by_domain.items()):
        if domains and domain not in domains:
            continue
        cases = [c for c in cases if c["case_id"] not in done]
        if not cases:
            continue
        items = items_for(cases)
        field_note = "main text"
        prompt = TASK.format(service=SERVICE[domain], field=field_note,
                             items=json.dumps([{k: v for k, v in i.items()} for i in items], indent=1))
        result = agent.run(agent.Call(
            role="writer", workspace=Path(f"/tmp/sm-auto-01/ws-writer-{domain}"), log_dir=RUNS / "writer" / domain,
            calls_log=RUNS / "calls.jsonl", prompt=prompt, system_append=ROLE, schema=SCHEMA,
            label=f"writer-{domain}", timeout=1800))
        answers = {a["id"]: a for a in agent.structured(result)["items"]}
        for c in cases:
            a = answers.get(c["case_id"])
            if a is None:
                done[c["case_id"]] = {"missing": True}
                continue
            a["problems"] = check(a, c["prompt"], c["references"][0]["query"]["table"])
            a["original"] = c["prompt"]
            done[c["case_id"]] = a
        out_path.write_text(json.dumps(done, indent=1, ensure_ascii=False) + "\n")
        print(domain, len(cases), "covers;", sum(1 for c in cases if done[c["case_id"]].get("plural_worthy")),
              "plural-worthy; billed", round(result["cost_usd_billed"], 4), "list", round(result["total_cost_usd"], 4))


def recheck():
    """Re-run the code checks on the saved answers (no model calls)."""
    path = HERE / "writer.json"
    done = json.loads(path.read_text())
    tables = {c["case_id"]: c["references"][0]["query"]["table"] for c in covers()}
    for cid, a in done.items():
        if not a.get("missing"):
            a["problems"] = check(a, a["original"], tables.get(cid))
    path.write_text(json.dumps(done, indent=1, ensure_ascii=False) + "\n")
    print("problems:", {k: a["problems"] for k, a in done.items() if a.get("problems")})


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--recheck" in args:
        recheck()
        sys.exit()
    main(set(args[args.index("--domains") + 1:]) if "--domains" in args else set())
