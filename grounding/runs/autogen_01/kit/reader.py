"""The cold reader: a fresh Sonnet session that reads a scenario's request without knowing how it was built.

Turn 1 sees the request alone: the reader's own conditions, and phrases that can be read two ways.
Turn 2 (same session) sees every seeded record and the writer's conditions: for each candidate record (every row
of the reference's root table), which of the writer's conditions it fails. Then: whether the writer's conditions
are faithful to the request, whether any ambiguity changes which records match, and whether the request is natural.

`problems(...)` turns the reader's answers into findings for the writer, checked in code:
- every target fails nothing;
- every decoy fails at least one condition, and only conditions that name its fact;
- every other candidate fails at least two conditions (otherwise it is an undeclared near miss or a second match);
- the conditions are faithful, no ambiguity changes the matches, and the request is natural.
"""
from __future__ import annotations

import json
from pathlib import Path

from grounding.runs.autogen_01.kit import agent
from grounding.runs.autogen_01.kit.bundle import compact_row

KIT = Path(__file__).resolve().parent
CONTEXT = {
    "calendar": "The person making the request is Jordan Lee (jordan.lee@northwind.example).",
    "box": "The person making the request is Jordan Lee (user 30000000001).",
    "linear": "The person making the request is Jordan Lee (user u-actor).",
    "slack": "The person making the request is the workspace's assistant bot (U01AGENBOT9), acting for the team.",
}
SERVICE = {"box": "Box", "calendar": "Google Calendar", "linear": "Linear", "slack": "Slack"}
TURN1 = {
    "type": "object",
    "properties": {
        "conditions": {"type": "array", "items": {"type": "string"}},
        "ambiguities": {"type": "array", "items": {
            "type": "object", "properties": {"phrase": {"type": "string"},
                                             "readings": {"type": "array", "items": {"type": "string"}}},
            "required": ["phrase", "readings"]}},
    },
    "required": ["conditions", "ambiguities"],
}
TURN2 = {
    "type": "object",
    "properties": {
        "records": {"type": "array", "items": {
            "type": "object", "properties": {"id": {"type": "string"},
                                             "fails": {"type": "array", "items": {"type": "string"}},
                                             "contestable": {"type": "boolean"},
                                             "note": {"type": "string"}},
            "required": ["id", "fails", "contestable", "note"]}},
        "faithful": {"type": "boolean"},
        "differences": {"type": "string"},
        "ambiguity_effects": {"type": "array", "items": {
            "type": "object", "properties": {"phrase": {"type": "string"},
                                             "careful_reader_unsure": {"type": "boolean"},
                                             "changes_matches": {"type": "boolean"},
                                             "explain": {"type": "string"}},
            "required": ["phrase", "careful_reader_unsure", "changes_matches", "explain"]}},
        "natural": {"type": "boolean"},
        "naturalness_note": {"type": "string"},
    },
    "required": ["records", "faithful", "differences", "ambiguity_effects", "natural", "naturalness_note"],
}


READER_NOISE = {"etag", "sequence_id", "sha1", "sha_1", "bodyData", "reactionData", "currentProgress",
                "progressHistory", "completedIssueCountHistory", "completedScopeHistory", "inProgressScopeHistory",
                "issueCountHistory", "scopeHistory", "inviteHash"}


def render_seed(case) -> str:
    """Every record in full, minus a few bookkeeping columns. (Until the main runs finished, the reader saw
    compact_row output, which drops `url` fields and cuts rows at 900 characters; see report §7.)"""
    lines = []
    for table in sorted(case["seed"]):
        rows = case["seed"][table]
        if not rows:
            continue
        lines.append(f"### {table} ({len(rows)})")
        lines += [json.dumps({k: v for k, v in r.items() if k not in READER_NOISE and v not in (None, "", [], {})},
                             ensure_ascii=False, default=str) for r in rows]
    return "\n".join(lines)


def candidates(case) -> tuple[str, list[str]]:
    ref = case["references"][0]
    table, key = ref["query"]["table"], ref["query"].get("key", ["id"])[0]
    return table, [str(r.get(key)) for r in case["seed"].get(table, [])]


def read(case: dict, workspace: Path, log_dir: Path, calls_log: Path, label: str, author_conditions: bool = True
         ) -> dict:
    """Run both turns; returns {"turn1", "turn2"} (structured answers) and session info.

    Without author conditions (a scenario written by hand, which has none), turn 2 uses the reader's own conditions
    from turn 1, numbered r1, r2, ..."""
    system = (KIT / "prompts" / "reader.md").read_text()
    domain = case["domain"]
    from grounding.common import dates
    when = f" {dates.today_text(case['written_for'])}" if case.get("written_for") else ""
    first = agent.run(agent.Call(
        role="reader", workspace=workspace, log_dir=log_dir, calls_log=calls_log, tools=[], schema=TURN1,
        system_append=system, label=label,
        prompt=f"A user of {SERVICE[domain]} gave an assistant this request:\n\n> {case['prompt']}\n\n"
               f"{CONTEXT[domain]}{when}\n\nStep 1: list the conditions a record must meet for this request to refer "
               "to it, and every phrase that could reasonably be read in more than one way."))
    table, ids = candidates(case)
    if author_conditions:
        conds = "The author lists these conditions of the request:\n" + \
            "\n".join(f"- {c['id']}: {c['text']}" for c in case["conditions"])
    else:
        own = (agent.structured(first) or {}).get("conditions", [])
        conds = ("Use your own conditions from step 1 as the author's conditions, with these ids:\n" +
                 "\n".join(f"- r{i + 1}: {c}" for i, c in enumerate(own)))
    second_prompt = (f"Step 2. These are all the records in the service:\n\n{render_seed(case)}\n\n{conds}\n\n"
                     f"The candidate records are the rows of `{table}`: {', '.join(ids)}.\n"
                     "For every candidate, give the ids of the author's conditions it fails under the careful reading "
                     "(an empty list if it meets all of them), whether a careful colleague could still argue that it "
                     "meets the request (contestable), and a short note. Then say whether the author's conditions "
                     "faithfully capture the request as you read it in step 1 (and what differs). For each "
                     "ambiguity you listed, say whether a careful reader would genuinely be unsure which reading was "
                     "meant, and whether the readings select different candidates. Finally, say whether the request "
                     "reads like something a real user would write, without hints that only a test would contain.")
    second = agent.run(agent.Call(
        role="reader", workspace=workspace, log_dir=log_dir, calls_log=calls_log, tools=[], schema=TURN2,
        system_append=system, label=label, resume=first["session_id"], prompt=second_prompt))
    answer2 = agent.structured(second) or {}
    missing = [i for i in ids if i not in {str(r.get("id")) for r in answer2.get("records", [])}]
    if missing:
        third = agent.run(agent.Call(
            role="reader", workspace=workspace, log_dir=log_dir, calls_log=calls_log, tools=[], schema=TURN2,
            system_append=system, label=label, resume=first["session_id"],
            prompt=f"You did not assess these candidates: {', '.join(missing)}. Give your complete answer again, "
                   "covering every candidate."))
        answer2 = agent.structured(third) or answer2
    return {"turn1": agent.structured(first) or {}, "turn2": answer2, "session_id": first.get("session_id")}


def contestable(case: dict, verdict: dict) -> dict:
    """Decoys the reader marks contestable (a careful reader could argue they meet the request): witness -> note."""
    decoys = {str(c["witness"]) for c in case["references"][0]["claims"]}
    return {str(r["id"]): r.get("note", "") for r in verdict.get("turn2", {}).get("records", [])
            if r.get("contestable") and str(r.get("id")) in decoys}


def problems(case: dict, verdict: dict) -> list[str]:
    ref = case["references"][0]
    conds = {c["id"]: c for c in case["conditions"]}
    by_id = {str(r.get("id")): r for r in verdict.get("turn2", {}).get("records", [])}
    targets = {str(x) for x in ref["expected"]}
    decoys = {str(c["witness"]): c for c in ref["claims"]}
    _, ids = candidates(case)
    out = []
    for i in ids:
        r = by_id.get(i)
        if r is None:
            out.append(f"The reader did not assess record `{i}`.")
            continue
        fails = sorted(set(r["fails"]))
        unknown = [f for f in fails if f not in conds]
        fails = [f for f in fails if f in conds]
        note = r.get("note", "")
        if unknown:
            out.append(f"The reader named conditions that do not exist for `{i}`: {unknown}.")
        if i in targets:
            if fails:
                out.append(f"The reader says the TARGET `{i}` fails {fails} ({note}).")
        elif i in decoys:
            fact = decoys[i]["requirement"]
            allowed = sorted(cid for cid, c in conds.items() if fact in c.get("facts", []))
            if not fails:
                out.append(f"The reader says the decoy `{i}` (for {fact}) meets every condition, so a reader could "
                           f"take it as a match ({note}).")
            elif set(fails) - set(allowed):
                out.append(f"The reader says the decoy `{i}` (for {fact}, conditions {allowed}) fails {fails}: it "
                           f"fails more than its own fact ({note}).")
        else:
            if not fails:
                out.append(f"The reader says the undeclared record `{i}` meets every condition: a second match "
                           f"({note}).")
            elif len(fails) == 1:
                out.append(f"The reader says the undeclared record `{i}` fails only {fails}: it is a near miss that "
                           f"is not declared as a decoy. Make it fail at least two conditions, or declare it as a "
                           f"decoy ({note}).")
    t2 = verdict.get("turn2", {})
    if t2.get("faithful") is False:
        out.append(f"The reader finds the conditions unfaithful to the request: {t2.get('differences')}")
    for a in t2.get("ambiguity_effects", []):
        if a.get("changes_matches") and a.get("careful_reader_unsure"):
            out.append(f"The reader finds the phrase \"{a.get('phrase')}\" genuinely ambiguous, in a way that "
                       f"changes which records match: {a.get('explain')}")
    if t2.get("natural") is False:
        out.append(f"The reader finds the request unnatural: {t2.get('naturalness_note')}")
    return out
