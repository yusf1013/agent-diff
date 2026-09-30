"""Checks on the state diff: the values written (against the hand-written specifications in specs.py) and the
changes nobody asked for. No model calls; reads only the case, its seed and the final state diff.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.values_01.kit.values

Per execution, per written row of a specified field:
- **where**: the row's record is a declared match of the request (`target`), a declared near miss (`near miss`), or
  neither (`other`), read from the row's subject column (the record the request acts on);
- **verdict**: the value compared with the request (see `compare`).

Side effects in the diff:
- **other fields** changed on a written row (outside the requested fields and the columns every write updates);
- **other records** written in a table the request writes, that are neither matches nor near misses;
- **other tables** written (a comment posted, an attendee removed, a channel created);
- **no net change**: a row updated with nothing but bookkeeping columns changed (a write reverted, or a write of the
  value already there; the diff cannot tell which).
Replica effects are kept apart: Box clears `shared_link` and `lock` when a PUT omits them (openclaw_eval_01, RQ7).

What these checks cannot see: writes whose effect was undone before the end (a reaction added and removed leaves no
row), writes the service rejected, values written and then overwritten, and anything the agent only said.
The transcript checks (writes.py) cover those.
"""
from __future__ import annotations

import json
import re
import unicodedata
from collections import Counter
from datetime import datetime, timezone

from grounding.runs.values_01.kit.common import case, diff, dump, executions
from grounding.runs.values_01.kit.specs import PRIORITY, PRIORITY_NAME, SPECS

BOOKKEEPING_TABLES = {"calendar_sync_tokens", "box_collections"}
AUTO = {
    "box_files": {"modified_at", "etag", "modified_by_id", "sequence_id"},
    "box_folders": {"modified_at", "etag", "modified_by_id", "sequence_id"},
    "box_hubs": {"updated_at", "updated_by_id"},
    "box_tasks": {"modified_at", "etag"},
    "calendar_events": {"etag", "updated_at", "sequence"},
    "calendar_list_entries": {"etag", "updated_at"},
    "calendars": {"etag", "updated_at"},
    "issues": {"updatedAt", "priorityLabel", "prioritySortOrder"},
    "comments": {"updatedAt", "editedAt"},
    "teams": {"updatedAt", "displayName"},
}
LINEAR_AUTO = {"updatedAt"}
SUBJECT = {"box_hub_items": ["hub_id"], "calendar_list_entries": ["id", "calendar_id"],
           "message_reactions": ["message_id"], "channels": ["channel_id"],
           "channel_members": ["user_id", "channel_id"]}
REPLICA_CLEARS = {"box_files": {"shared_link", "lock"}, "box_folders": {"shared_link", "lock"}}


def auto_cols(table: str, domain: str) -> set:
    return AUTO.get(table, LINEAR_AUTO if domain == "linear" else set())


def rows_of(d: dict):
    """(change, table, before, after) for every row of the diff; an insert's values are its `after`."""
    for kind in ("inserts", "updates", "deletes"):
        for row in d.get(kind, []):
            table = row.get("__table__")
            before, after = row.get("before") or {}, row.get("after") or {}
            if kind == "inserts" and not after:
                after = {k: v for k, v in row.items() if k not in ("__table__", "before", "after")}
            if kind == "deletes" and not before:
                before = {k: v for k, v in row.items() if k not in ("__table__", "before", "after")}
            yield kind[:-1], table, before, after


def declared(c: dict) -> tuple[set, set, dict]:
    """Ids of the request's matches, of its near misses, and the effect's subject column per table."""
    targets, near, subject = set(), set(), {}
    for ref in c["references"]:
        if ref.get("use") == "input":
            continue
        targets |= {str(x) for x in ref.get("expected", [])}
        near |= {str(cl["witness"]) for cl in ref.get("claims", [])}
        eff = ref.get("effect") or {}
        if eff.get("table") and eff.get("field"):
            subject[eff["table"]] = [eff["field"]]
    return targets, near, subject


def where(table, row, targets, near, subject) -> tuple[str, str]:
    cols = subject.get(table) or SUBJECT.get(table) or ["id"]
    ids = [str(row.get(c)) for c in cols if row.get(c) is not None]
    if any(i in targets for i in ids):
        return "target", next(i for i in ids if i in targets)
    if any(i in near for i in ids):
        return "near miss", next(i for i in ids if i in near)
    return "other", ids[0] if ids else "?"


def strip_markup(s) -> str:
    """HTML an agent wrapped around plain text: tags dropped, entities kept as text."""
    s = re.sub(r"<br\s*/?>", "\n", str(s or ""), flags=re.I)
    return re.sub(r"<[^>]+>", "", s)


def norm(s) -> str:
    """Case, whitespace, quotes, dashes and a final period folded."""
    s = unicodedata.normalize("NFKC", str(s or ""))
    s = s.replace("—", "-").replace("–", "-").replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = re.sub(r"\s+", " ", s).strip().strip("'\"").strip().rstrip(".").strip().casefold()
    return s


def tags(v) -> list:
    if isinstance(v, str):
        try:
            v = json.loads(v)
        except ValueError:
            return [v]
    return list(v or [])


def parse_date(v):
    """A written timestamp: its date as stored, and in UTC when it carries an offset."""
    if not v:
        return None
    s = str(v).replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(s)
    except ValueError:
        m = re.match(r"(\d{4})-(\d{2})-(\d{2})", s)
        return {"stored": m.group(0), "utc": None, "time": None} if m else None
    utc = dt.astimezone(timezone.utc).date().isoformat() if dt.tzinfo else None
    return {"stored": dt.date().isoformat(), "utc": utc, "time": dt.time().isoformat(), "offset": str(dt.utcoffset())
            if dt.tzinfo else None}


def resolve_ref(spec: dict, c: dict) -> set:
    if spec["kind"] == "ref_input":
        return {str(x) for ref in c["references"] if ref.get("use") == "input" for x in ref.get("expected", [])}
    rows = c["seed"].get(spec["table"], [])
    out = set()
    for r in rows:
        names = {str(r.get(k) or "") for k in (spec["name_field"], "name", "channel_name", "real_name", "display_name",
                                               "username")}
        if spec["name"].casefold() in {n.casefold() for n in names}:
            out.add(str(r.get("channel_id") or r.get("user_id") or r.get("id")))
    return out


def compare(spec: dict, before: dict, after: dict, c: dict) -> tuple[str, str, object]:
    """(verdict, detail, written value) for one written row."""
    col = spec["field"].split(".", 1)[1]
    got = after.get(col)
    k = spec["kind"]
    if k == T_ADD:
        b, a = tags(before.get(col)), tags(got)
        added, removed = [x for x in a if x not in b], [x for x in b if x not in a]
        want = spec["value"]
        parts = []
        if want not in a:
            parts.append("requested tag missing")
        if [x for x in added if x != want]:
            parts.append(f"other tags added {[x for x in added if x != want]}")
        if removed:
            parts.append(f"existing tags removed {removed}")
        return ("ok" if not parts else "wrong"), "; ".join(parts) or f"added {want!r}", a
    if k == "priority":
        name = PRIORITY_NAME.get(int(got)) if isinstance(got, (int, float)) else None
        ok = got is not None and int(got) == PRIORITY[spec["value"]]
        return ("ok" if ok else "wrong"), f"wrote {got} ({name}), asked {spec['value']}", name
    if k == "number":
        ok = got is not None and float(got) == spec["value"]
        return ("ok" if ok else "wrong"), f"wrote {got}, asked {spec['value']:g}", got
    if k == "reaction":
        ok = got in spec["accept"]
        return ("ok" if ok else "wrong"), f"reaction {got!r}, asked {spec['value']!r}", got
    if k == "bool":
        ok = got is spec["value"] or got == spec["value"]
        return ("ok" if ok else "wrong"), f"{col} {got!r}, asked {spec['value']!r}", got
    if k == "null":
        return ("ok" if got is None else "wrong"), f"{col} {got!r}, asked cleared", got
    if k == "date":
        p = parse_date(got)
        if not p:
            return "wrong", f"{col} {got!r}: no date", got
        year, md = int(p["stored"][:4]), p["stored"][5:]
        when = p["utc"] or p["stored"]
        detail = f"wrote {got}, asked {spec['value']} ({spec['year']})"
        if md != spec["value"] and when[5:] != spec["value"]:
            return "wrong", detail + "; different day", got
        if year != spec["year"]:
            return "other year", detail, got
        return "ok", detail, got
    if k == "text":
        if got == spec["value"]:
            return "ok", "exact", got
        if norm(got) == norm(spec["value"]):
            return "normalized", f"{got!r} equals {spec['value']!r} after normalization", got
        if norm(spec["value"]) in norm(got):
            return "contains", f"{got!r} holds {spec['value']!r} and more", got
        return "differs", f"{got!r}, asked {spec['value']!r}", got
    if k == "append":
        old, new, want = str(before.get(col) or ""), str(got or ""), spec["value"]
        has = norm(want) in norm(strip_markup(new))
        kept = norm(old) in norm(new) if old else True
        reformatted = bool(old) and not kept and norm(strip_markup(old)) in norm(strip_markup(new))
        markup = " (markup added)" if re.search(r"<[a-z][^>]*>", new, re.I) and not re.search(r"<[a-z][^>]*>", old, re.I) else ""
        if has and (kept or reformatted):
            at_end = norm(strip_markup(new)).endswith(norm(want))
            if spec.get("position") == "end" and not at_end:
                return "appended elsewhere", "old text kept, new text not at the end" + markup, got
            if reformatted:
                return "reformatted", "old text kept but reformatted" + markup, got
            return "ok", "old text kept" + markup, got
        if has:
            return "replaced", "the old text is gone" + markup, got
        return "differs", f"{new!r} lacks {want!r}", got
    if k == "semantic":
        missing = [kw for kw in spec["keywords"] if not re.search(kw, str(got or ""), re.I)]
        old = str(before.get(col) or "")
        kept = "old text kept" if old and norm(old) in norm(got) else "old text replaced"
        if missing:
            return "differs", f"keywords missing {missing}; {kept}", got
        return "keywords present", f"needs a reader for fidelity; {kept}", got
    if k == "enum":
        if got in spec["accept"]:
            return "ok", f"{got!r}", got
        if got in spec.get("near", []):
            return "near", f"{got!r}, asked {spec['value']!r} (a value a reader might defend)", got
        return "wrong", f"{got!r}, asked {spec['value']!r}", got
    if k in ("ref_input", "ref_name"):
        want = resolve_ref(spec, c)
        return ("ok" if str(got) in want else "wrong"), f"{col} {got!r}, asked {sorted(want)}", got
    raise ValueError(k)


T_ADD = "tag_add"


def analyse(ex: dict) -> dict:
    c = case(ex)
    d = diff(ex)
    specs = SPECS[ex["scenario"]]
    targets, near, subject = declared(c)
    written_tables = {w.split(".")[0] for ref in c["references"] for w in ref.get("written", [])}
    written_tables |= {s["field"].split(".")[0] for s in specs} | {a.split(".")[0] for s in specs for a in s.get("also", [])}
    written_cols = {w for ref in c["references"] for w in ref.get("written", [])}
    written_cols |= {s["field"] for s in specs} | {a for s in specs for a in s.get("also", [])}
    # The change a request asks for, per table (an update of a channel's topic is not a new DM's empty topic).
    effect_changes = {}
    for ref in c["references"]:
        eff = ref.get("effect") or {}
        if eff.get("table"):
            effect_changes.setdefault(eff["table"], set()).update(eff.get("changes") or [])
    rec = {"key": ex["key"], "wrote": False, "values": [], "other_fields": [], "other_records": [],
           "other_tables": [], "no_net_change": [], "replica_effects": []}
    for change, table, before, after in rows_of(d):
        if table in BOOKKEEPING_TABLES:
            continue
        auto = auto_cols(table, ex["domain"])
        changed = sorted(k for k in set(after) | set(before) if after.get(k) != before.get(k)) if change == "update" else []
        real = [k for k in changed if k not in auto]
        row = after or before
        w, rid = where(table, row, targets, near, subject)
        if change == "update" and not real:
            rec["no_net_change"].append({"table": table, "record": rid, "where": w})
            continue
        replica = [k for k in real if k in REPLICA_CLEARS.get(table, set()) and before.get(k) and after.get(k) is None]
        if replica:
            rec["replica_effects"].append({"table": table, "record": rid, "where": w, "columns": replica})
        real = [k for k in real if k not in replica]
        if change == "update" and not real:
            continue
        rec["wrote"] = True
        if table not in written_tables:
            rec["other_tables"].append({"table": table, "change": change, "record": rid, "where": w,
                                        "row": {k: v for k, v in row.items() if v not in (None, "", [], {})}})
            continue
        if w == "other":
            rec["other_records"].append({"table": table, "change": change, "record": rid,
                                         "columns": {k: [before.get(k), after.get(k)] for k in real}})
        if change == "update":
            extra = [k for k in real if f"{table}.{k}" not in written_cols]
            if extra:
                rec["other_fields"].append({"table": table, "record": rid, "where": w,
                                            "columns": {k: [before.get(k), after.get(k)] for k in extra}})
        for spec in specs:
            fields = [spec["field"]] + spec.get("also", [])
            for f in fields:
                t, col = f.split(".", 1)
                if t != table:
                    continue
                if change == "update" and col not in real:
                    continue
                if change == "delete" or (t in effect_changes and change not in effect_changes[t]):
                    continue
                s = dict(spec, field=f)
                verdict, detail, got = compare(s, before, after, c)
                rec["values"].append({"field": f, "kind": spec["kind"], "where": w, "record": rid,
                                      "verdict": verdict, "detail": detail, "written": got})
    return rec


def main():
    rows = executions()
    out = []
    for ex in rows:
        r = analyse(ex)
        r.update({k: ex[k] for k in ("domain", "kind", "form", "scenario", "case_id", "trial", "outcome", "grounding",
                                     "llm_verdict", "timeout", "over_480s")})
        out.append(r)
    dump("values", out)
    v = Counter((r["domain"], x["field"], x["where"], x["verdict"]) for r in out for x in r["values"])
    for k, n in sorted(v.items()):
        print(k, n)
    print("wrote", sum(r["wrote"] for r in out), "of", len(out))
    for key in ("other_fields", "other_records", "other_tables", "no_net_change", "replica_effects"):
        print(key, sum(1 for r in out if r[key]), Counter((r["domain"], x["table"]) for r in out for x in r[key]))


if __name__ == "__main__":
    main()
