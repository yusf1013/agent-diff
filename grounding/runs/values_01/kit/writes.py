"""Write commands in the transcript, set against the final state diff. No model calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.values_01.kit.writes

The diff shows only the end state. A write the agent undid, a write of the value already there, and a write the
service rejected leave no trace in it (a reaction added and removed leaves no row at all). This reads each step's
command for the service's write operations:
- Box and Calendar: HTTP PUT, POST, PATCH or DELETE (Calendar's freeBusy and watch calls are reads);
- Slack: the Web API's write methods (reactions.add, conversations.archive, ...);
- Linear: GraphQL mutations (`issueUpdate(`, ...), also inside files the agent wrote and posted with `-d @file`.

For each write step: the operation, the record ids it names (from the URL, the parameters or the mutation's `id`),
and whether the response shows an error. Then per execution:
- **not in the diff**: a record some accepted write step names, whose final diff row is missing or shows no net
  change: a write undone later (restored), a write of the value already there (a no-op), or a write the replica
  accepted without applying. The transcript tells which; `later_write` marks a later write step on the same record.
- **rejected**: write steps whose response is an error (a write the service refused still shows intent).
- **inverse**: an undoing operation (reactions.remove, conversations.unarchive after archive, attachmentDelete).

What this cannot see: writes built inside loops or scripts from variables (their ids are unresolved; counted apart),
and whether a response the agent piped through a filter reported success.
"""
from __future__ import annotations

import json
import re
from collections import Counter

from grounding.runs.values_01.kit.common import case, diff, dump, executions, transcript
from grounding.runs.values_01.kit.values import BOOKKEEPING_TABLES, auto_cols, rows_of

SLACK_WRITES = {"chat.postMessage", "chat.update", "chat.delete", "chat.postEphemeral", "chat.meMessage",
                "reactions.add", "reactions.remove", "conversations.archive", "conversations.unarchive",
                "conversations.invite", "conversations.kick", "conversations.join", "conversations.leave",
                "conversations.open", "conversations.create", "conversations.rename", "conversations.setTopic",
                "conversations.setPurpose", "conversations.close", "pins.add", "pins.remove", "stars.add",
                "stars.remove", "users.profile.set", "files.upload", "files.delete", "bookmarks.add"}
INVERSE = {"reactions.remove", "conversations.unarchive", "attachmentDelete", "commentDelete", "issueDelete",
           "documentDelete", "DELETE"}
# Cycle 2: also the mutations whose names end otherwise (attachmentLinkURL, issueAddLabel, ...), which cycle 1 missed.
LINEAR_MUT = re.compile(r"\b([a-z][A-Za-z]+(?:Create|Update|Delete|Archive|Unarchive|Add|Remove|Resolve|Unresolve|Set|"
                        r"Link[A-Za-z]*|Upsert|Merge|Move|Subscribe|Unsubscribe|AddLabel|RemoveLabel|Import))\s*\(")
HTTP_WRITE = re.compile(r"(?:-X|--request)\s*['\"]?(PUT|POST|DELETE|PATCH)\b")
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")


def step_text(step: dict) -> str:
    return step.get("action") or ""


def obs_text(step: dict) -> str:
    o = step.get("observation")
    if isinstance(o, dict):
        return f"{o.get('stdout') or ''}\n{o.get('stderr') or ''}\n{o.get('error') or ''}"
    return str(o or "")


def error_in(domain: str, op: str, out: str) -> bool:
    if domain == "slack":
        return bool(re.search(r"[\"']ok[\"']\s*:\s*(false|False)", out)) and not re.search(
            r"[\"']ok[\"']\s*:\s*(true|True)", out)
    if domain == "linear":
        return bool(re.search(r"\"errors\"\s*:|'errors'\s*:", out)) and not re.search(
            r"[\"']success[\"']\s*:\s*(true|True)", out)
    return bool(re.search(r"\"type\"\s*:\s*\"error\"|\"error\"\s*:\s*\{|'type': 'error'|HTTP/\S+ [45]\d\d", out))


def ids_named(domain: str, text: str) -> set[str]:
    ids = set()
    if domain == "box":
        ids |= set(re.findall(r"/(?:files|folders|tasks|hubs|comments|web_links|collaborations)/(\d+)", text))
        ids |= set(re.findall(r"\"(?:id|item_id|file_id)\"\s*:\s*\"?(\d{3,})", text))
    elif domain == "calendar":
        ids |= set(re.findall(r"/events/([A-Za-z0-9_]+)", text))
        ids |= set(re.findall(r"/calendarList/([^/?\s'\"]+)", text))
        ids |= set(re.findall(r"/calendars/([^/?\s'\"]+)(?=[?'\"\s]|$)", text))
        ids = {i.replace("%40", "@") for i in ids if i not in ("primary",)}
    elif domain == "slack":
        # A reaction's record is its message (the diff's message_reactions row holds the timestamp, not the
        # channel); a channel operation's record is the channel, and an invitation's also the users.
        ts = set(re.findall(r"(?:timestamp|ts)[\"']?\s*[=:]\s*[\"']?(\d{10}\.\d{6})", text))
        if re.search(r"reactions\.(?:add|remove)", text):
            return ts
        ids |= set(re.findall(r"(?:channel|users?)[\"']?\s*[=:]\s*[\"']?([CDGU][A-Z0-9]{6,})", text))
    elif domain == "linear":
        # The record a mutation writes is its own `id` argument (not the ids inside its input).
        for m in LINEAR_MUT.finditer(text):
            head = text[m.end():m.end() + 160]
            got = re.match(r"\s*(?:input\s*:\s*\{\s*)?\\?[\"']?id\\?[\"']?\s*:\s*\\?[\"']([^\"'\\]+)", head)
            if got:
                ids.add(got.group(1))
        ids |= set(re.findall(r"[\"']id[\"']\s*:\s*[\"']([0-9a-f-]{36}|[A-Z]{2,5}-\d+)[\"']", text))
    return {i for i in ids if not i.startswith("$")}


def write_ops(domain: str, text: str) -> list[str]:
    if domain == "slack":
        # conversations.open returns the existing DM when there is one: a lookup, unless the diff shows a new channel.
        return [m for m in re.findall(r"slack\.com/api/([a-zA-Z_.]+)", text) if m in SLACK_WRITES
                and m != "conversations.open"]
    if domain == "linear":
        return LINEAR_MUT.findall(text) if re.search(r"\bmutation\b|Update\s*\(|Create\s*\(", text) else []
    ops = HTTP_WRITE.findall(text)
    if domain == "calendar" and re.search(r"freeBusy|/watch|channels/stop", text):
        ops = [o for o in ops if o != "POST"]
    # A curl with a body and no method is a POST; cycle 2: only within the curl invocation itself (an `unzip -d` in the
    # same command is not a body), and not with -G, which sends the data as query parameters (a GET).
    if not ops and domain == "box" and any(
            re.search(r"\bcurl\b", seg) and re.search(r"api\.box\.com", seg) and not re.search(r"\s(?:-G|--get)\b", seg)
            and re.search(r"(?:\s-d\s|\s-d'|\s-d\"|--data(?:-raw|-binary|-urlencode)?[\s=]|\s-F\s)", seg)
            for seg in re.split(r"\||;|&&|\n", text)):
        ops = ["POST"]
    return ops


def file_bodies(steps: list[dict]) -> dict[str, str]:
    """Files the agent wrote with the write tool (a mutation posted later with `-d @file`)."""
    out = {}
    for s in steps:
        if s.get("tool") == "write":
            args = s.get("arguments") or {}
            path = args.get("path") or args.get("file_path") or ""
            out[path.split("/")[-1]] = args.get("content") or step_text(s)
    return out


def writes_of(ex: dict) -> list[dict]:
    steps = transcript(ex).get("steps", [])
    files = file_bodies(steps)
    out = []
    for i, s in enumerate(steps):
        if s.get("tool") not in ("exec", "process"):
            continue
        text = step_text(s)
        for name in re.findall(r"-d\s*@['\"]?([^\s'\"]+)", text):
            body = files.get(name.split("/")[-1])
            if body:
                text += "\n" + body
        ops = write_ops(ex["domain"], text)
        if not ops:
            continue
        looped = bool(re.search(r"\bfor\b.+\bin\b|\$\{?\w+\}?|python3?\s+-c|<<", text))
        # Cycle 2: a Calendar write that asks the service to email the attendees (no diff shows it).
        notify = ex["domain"] == "calendar" and bool(
            re.search(r"sendUpdates=(?:all|externalOnly)|sendNotifications=true|\"sendUpdates\"\s*:\s*\"(?:all|externalOnly)",
                      text))
        out.append({"step": i, "ops": ops, "ids": sorted(ids_named(ex["domain"], text)),
                    "error": error_in(ex["domain"], ops[0], obs_text(s)), "looped": looped,
                    "inverse": any(o in INVERSE for o in ops), "notify": notify})
    return out


def diff_ids(ex: dict) -> tuple[set, set]:
    """Record ids with a real change in the diff, and ids whose rows changed only bookkeeping columns."""
    changed, nochange = set(), set()
    for change, table, before, after in rows_of(diff(ex)):
        if table in BOOKKEEPING_TABLES:
            continue
        row = after or before
        vals = {str(v) for k, v in row.items() if isinstance(v, (str, int)) and k in (
            "id", "channel_id", "message_id", "user_id", "calendar_id", "hub_id", "item_id", "file_id", "issueId",
            "event_id")}
        if change == "update":
            real = [k for k in set(after) | set(before) if after.get(k) != before.get(k)
                    and k not in auto_cols(table, ex["domain"])]
            (changed if real else nochange).update(vals)
        else:
            changed |= vals
    return changed, nochange


def canonical(ex: dict):
    """Ids as the diff holds them: Linear issue identifiers (WEB-3) become their ids; Calendar ids lose their
    domain part (an agent may write `c_x%40group.calendar.google.com` or a shortened `c_x`)."""
    alias = {}
    if ex["domain"] == "linear":
        alias = {str(i.get("identifier")): str(i["id"]) for i in case(ex)["seed"].get("issues", []) if i.get("identifier")}

    def f(i: str) -> str:
        i = alias.get(i, i)
        return i.split("@")[0] if ex["domain"] == "calendar" else i
    return f


def analyse(ex: dict) -> dict:
    ws = writes_of(ex)
    canon = canonical(ex)
    changed, nochange = diff_ids(ex)
    changed, nochange = {canon(i) for i in changed}, {canon(i) for i in nochange}
    for w in ws:
        w["ids"] = sorted({canon(i) for i in w["ids"]})
    accepted = [w for w in ws if not w["error"]]
    named = Counter(i for w in accepted for i in w["ids"])
    missing = []
    for rid in sorted(named):
        if rid in changed:
            continue
        steps = [w["step"] for w in accepted if rid in w["ids"]]
        missing.append({"record": rid, "steps": steps, "row": "no net change" if rid in nochange else "no row",
                        "later_write": len(steps) > 1,
                        "inverse": any(w["inverse"] for w in accepted if rid in w["ids"])})
    return {"key": ex["key"], "write_steps": len(ws), "accepted": len(accepted),
            # A response with an error whose record still changed: Linear's documentUpdate and attachmentUpdate apply
            # the change and answer with an error (a known replica defect, openclaw_eval_01).
            # "applied": the record changed although no accepted write step names it.
            "rejected": [{"step": w["step"], "ops": w["ops"], "ids": w["ids"],
                          "applied": bool((set(w["ids"]) & changed) - set(named))} for w in ws if w["error"]],
            "unresolved": [w["step"] for w in ws if not w["ids"]],
            "not_in_diff": missing,
            "inverse_ops": [{"step": w["step"], "ops": w["ops"], "ids": w["ids"]} for w in accepted if w["inverse"]],
            "notify": [{"step": w["step"], "ids": w["ids"]} for w in accepted if w.get("notify")],
            "ops": Counter(o for w in ws for o in w["ops"])}


def main():
    rows = executions()
    out = []
    for ex in rows:
        r = analyse(ex)
        r.update({k: ex[k] for k in ("domain", "kind", "scenario", "grounding", "outcome", "timeout")})
        out.append(r)
    dump("writes", out)
    print("executions with write steps", sum(1 for r in out if r["write_steps"]))
    print("with rejected writes", sum(1 for r in out if r["rejected"]), Counter(r["domain"] for r in out if r["rejected"]))
    print("  error answered but applied", Counter(o for r in out for x in r["rejected"] if x["applied"] for o in x["ops"]))
    print("with unresolved write ids", sum(1 for r in out if r["unresolved"]))
    nd = [r for r in out if r["not_in_diff"]]
    print("with accepted writes not in the diff", len(nd), Counter(r["domain"] for r in nd))
    print("  of which a later write on the same record", sum(1 for r in nd if any(m["later_write"] for m in r["not_in_diff"])))
    print("  of which an inverse op", sum(1 for r in nd if any(m["inverse"] for m in r["not_in_diff"])))
    print("  rows:", Counter(m["row"] for r in nd for m in r["not_in_diff"]))
    print("inverse ops", sum(1 for r in out if r["inverse_ops"]))
    print("calendar writes that notify attendees", sum(1 for r in out if r["notify"]))


if __name__ == "__main__":
    main()
