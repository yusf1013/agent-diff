"""Phase 2: the underspecified variants, derived automatically (plan, Phase 2; ../decisions.md N10, N12).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.kit.variants2 dropf \
        --source exemplars|population [--scenarios ID ...] [--facts FACT ...] --out DIR [--concurrency 4]
    python ... variants2 clone --source exemplars|population [--scenarios ID ...] --out DIR [--concurrency 4]
    AUTOGEN_BACKEND=muse is required (the agents run on Muse, N7).

**Drop-F.** Code decides whether the fact is derivable and what the relaxed query selects (`policy.drop_f`,
semantic construction). The Muse writer then rewords the request without the condition (prompts/dropf_writer.md).
Code checks the reworded request (no plural or universal word), and the Muse reader reads it cold; its matches must be
exactly the intended set (`reader2`). Findings go back to the writer, for up to two repairs.

**Clone.** The Muse writer describes a copy of the target that differs only in fields the request does not use
(prompts/clone_writer.md), or says the service does not allow one. Code builds it and checks the match set
(`policy.clone`) and the fields it changed; the reader checks the unchanged request against the new seed. Findings
go back to the writer, for up to two repairs.

Every call is logged under DIR/<variant>/, with tokens and costs in DIR/calls.jsonl. No manual label or manual
variant reaches an agent: the writer sees the scenario (request, query, seed rows, the author's near-miss
explanations) and the replica notes.
"""
from __future__ import annotations

import argparse
import json
import re
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from grounding.runs.autogen_01.kit import agent
from grounding.runs.autogen_01.kit.derive import _foreign_keys, effect_key
from grounding.runs.autogen_02.kit import reader2
from grounding.runs.autogen_02.kit.policy import _nodes, clone, drop_f, facts_of

KIT = Path(__file__).resolve().parent
STUDY = KIT.parent
WORKSPACES = Path("/tmp/autogen-02/ws/variants")
SERVICE = {"box": "Box", "calendar": "Google Calendar", "linear": "Linear", "slack": "Slack"}
OPS = {"eq": "=", "ne": "!=", "gt": ">", "ge": ">=", "lt": "<", "le": "<="}
ROUNDS = (1, 2, 3)  # the first answer and up to two repairs
UNIQUE_FIELDS = re.compile(r"^(identifier|number|url|slugId|slug|ts|ical_uid|iCalUID|etag|branchName)$")
DROPF_SCHEMA = {"type": "object", "properties": {
    "possible": {"type": "boolean"}, "request": {"type": "string"}, "removed_words": {"type": "string"},
    "reason": {"type": "string"}}, "required": ["possible", "request", "removed_words", "reason"]}
CLONE_SCHEMA = {"type": "object", "properties": {
    "possible": {"type": "boolean"}, "reason": {"type": "string"}, "new_key": {"type": "string"},
    "changes": {"type": "array", "items": {"type": "object", "properties": {
        "field": {"type": "string"}, "value": {"type": "string"}}, "required": ["field", "value"]}},
    "skip_children": {"type": "array", "items": {"type": "string"}}},
    "required": ["possible", "reason", "new_key", "changes", "skip_children"]}


def render_query(query: dict, removed=frozenset()) -> str:
    """The query as an indented tree a writer can read; conditions in `removed` are marked."""
    head = f"Records of `{query['table']}`"
    for mode, word in (("argmax", "largest"), ("argmin", "smallest")):
        if query.get(mode):
            head += f"; of those, only the one(s) with the {word} `{query[mode]}`"
    return head + ", where:\n" + "\n".join(_render_node(query, removed, 1))


def _render_node(node: dict, removed, depth: int) -> list[str]:
    pad = "  " * depth
    lines = []
    for f in node.get("filters", []):
        mark = "  << REMOVE" if f.get("key") in removed else ""
        lines.append(f"{pad}- `{f['field']}` {OPS.get(f['op'], f['op'])} {json.dumps(f.get('value'), ensure_ascii=False)}"
                     f"{mark}")
    for e in node.get("edges", []):
        mark = "  << REMOVE" if e.get("key") in removed else ""
        j = e["join"]
        link = f"linked by `{j['parent']}` {j.get('op', 'eq')} `{e['node']['table']}.{j['child']}`"
        if e.get("negate"):
            what = f"no record of `{e['node']['table']}`"
        elif "count" in e:
            what = f"a number {OPS.get(e['count']['op'], e['count']['op'])} {e['count']['value']} of records of " \
                   f"`{e['node']['table']}`"
        else:
            what = f"at least one record of `{e['node']['table']}`"
        inner = _render_node(e["node"], removed, depth + 1)
        lines.append(f"{pad}- {what} {link}" + (", where:" if inner else "") + mark)
        lines += inner
    return lines


FUNCTION_WORDS = {"a", "an", "the", "that", "which", "who", "whose", "where", "is", "are", "was", "were", "has",
                  "have", "had", "and", "or", "of", "to", "in", "on", "at", "for", "with", "from", "by", "it", "its",
                  "this", "one", "my", "me", "i", "s"}


# Generic nouns for a record: dropping the condition carried by a specific noun ("reply" for a thread's hierarchy)
# leaves the record's generic name ("message"). Added after cal1, where the check flagged SLK-22's "Diego Alvarez's
# message", which I had also written by hand.
GENERIC_NOUNS = {"message", "messages", "post", "event", "events", "meeting", "issue", "issues", "file", "files",
                 "folder", "folders", "document", "doc", "item", "items", "record", "entry", "task", "comment",
                 "thread", "channel", "calendar", "hub", "label", "cycle", "team", "user", "person", "one"}


def added_words(original: str, edited: str) -> list[str]:
    """Content words of the edited request that the original does not contain (rules 2 and 5 of the writer). A word
    counts as present when it shares a stem of at least four letters with an original word ("edit", "edited"), and
    a record's generic noun is allowed."""
    words = lambda text: re.findall(r"[a-z0-9]+", text.lower())
    before = set(words(original))

    def known(w):
        return w in before or any(len(w) >= 4 and len(o) >= 4 and (o.startswith(w) or w.startswith(o))
                                  for o in before)
    return sorted({w for w in words(edited) if not known(w) and w not in FUNCTION_WORDS | GENERIC_NOUNS})


def _rows(case, table, key, ids):
    return [r for r in case["seed"].get(table, []) if str(r.get(key)) in {str(i) for i in ids}]


def _dumps(rows):
    return "\n".join(json.dumps(r, ensure_ascii=False, default=str) for r in rows)


# ---------------------------------------------------------------- drop-F

def _dropf_prompt(case: dict, meta: dict) -> str:
    ref = case["references"][0]
    freed = [c for c in ref["claims"] if c["requirement"] in meta["dropped_facts"]]
    near = "\n".join(f"- `{c['witness']}`: {c['explanation']}" for c in freed)
    return (f"Service: {SERVICE[case['domain']]}.\n\nRequest:\n> {case['prompt']}\n\n"
            f"Conditions of the request:\n{render_query(ref['query'], set(meta['dropped_keys']))}\n\n"
            f"Near misses that fail only the removed condition (the author's explanations):\n{near}\n\n"
            "Remove the marked condition from the request, following the rules.")


def derive_dropf(case: dict, fact: str, out: Path, calls_log: Path) -> dict:
    """One drop-F variant, written and checked; returns its record (written to out/<id>/record.json)."""
    _, meta = drop_f(case, fact, None, semantic=True)
    vid = f"U-{case['case_id']}-{fact.split(':')[-1].replace('.', '_')}"
    dest = out / vid
    dest.mkdir(parents=True, exist_ok=True)
    record = {"id": vid, "scenario": case["case_id"], "domain": case["domain"], "fact": fact,
              "dropped_facts": meta["dropped_facts"], "dropped_keys": meta["dropped_keys"],
              "matches": meta["matches"], "other_near_misses": meta["other_near_misses"],
              "conditions_left": meta["conditions_left"], "family": meta["family"], "rounds": []}
    if meta["problems"]:
        record.update(status="not_derivable", problems=meta["problems"])
        (dest / "record.json").write_text(json.dumps(record, indent=1, ensure_ascii=False) + "\n")
        return record
    system = (KIT / "prompts" / "dropf_writer.md").read_text()
    ws = WORKSPACES / out.name / vid
    session, prompt = None, _dropf_prompt(case, meta)
    for round_no in ROUNDS:
        result = agent.run(agent.Call(role="writer", workspace=ws / "writer", prompt=prompt, log_dir=dest / "writer",
                                      calls_log=calls_log, tools=[], schema=DROPF_SCHEMA, system_append=system,
                                      label=vid, resume=session))
        session = result.get("session_id")
        answer = agent.structured(result) or {}
        entry = {"round": round_no, "writer": answer}
        record["rounds"].append(entry)
        if not answer.get("possible"):
            record.update(status="writer_declined", request=None, problems=[answer.get("reason", "")])
            break
        variant, vmeta = drop_f(case, fact, answer["request"], variant_id=vid, semantic=True)
        findings = list(vmeta["problems"])
        added = added_words(case["prompt"], answer["request"])
        if added:
            findings.append(f"The edit adds words that are not in the original request: {added}. Remove only the "
                            "condition; keep every other word as it was.")
        if not findings:
            verdict = reader2.read(variant, ws / f"reader-{round_no}", dest / f"reader-{round_no}", calls_log, vid)
            entry["reader"] = verdict
            findings = reader2.problems(variant, verdict, variant["references"][0]["expected"])
            entry["contestable"] = reader2.contestable(variant, verdict, variant["references"][0]["expected"])
        entry["findings"] = findings
        if not findings:
            record.update(status="accepted", request=answer["request"], problems=[])
            (dest / "variant.json").write_text(json.dumps(variant, indent=1, ensure_ascii=False) + "\n")
            break
        record.update(status="rejected", request=answer["request"], problems=findings)
        prompt = ("The edited request was checked, with these findings:\n" + "\n".join(f"- {f}" for f in findings) +
                  "\n\nRevise the edit under the same rules, or answer possible: false if it cannot be done.")
    (dest / "record.json").write_text(json.dumps(record, indent=1, ensure_ascii=False, default=str) + "\n")
    return record


# ---------------------------------------------------------------- clone

def _children(case: dict, table: str, col: str, target_id: str) -> dict:
    out = {}
    for child, fk_col, ref_table, ref_col in _foreign_keys(case["domain"]):
        if ref_table == table and ref_col == col and child != table:
            rows = [r for r in case["seed"].get(child, []) if str(r.get(fk_col)) == target_id]
            if rows:
                out[child] = rows
    return out


def _clone_prompt(case: dict) -> str:
    ref = case["references"][0]
    table = ref["query"]["table"]
    col = effect_key(case["domain"], table)[0]
    target_id = str(ref["expected"][0])
    rows = case["seed"].get(table, [])
    target = [r for r in rows if str(r.get(col)) == target_id]
    others = [r for r in rows if str(r.get(col)) != target_id][:5]
    kids = _children(case, table, col, target_id)
    notes = (STUDY / "inputs" / case["domain"] / "replica.md").read_text()
    return (f"Service: {SERVICE[case['domain']]}.\n\nRequest:\n> {case['prompt']}\n\n"
            f"Conditions of the request:\n{render_query(ref['query'])}\n\n"
            f"The target record (table `{table}`, key `{col}`):\n{_dumps(target)}\n\n"
            f"Other records of `{table}`, for their conventions:\n{_dumps(others) or '(none)'}\n\n"
            f"Keys already used in `{table}` (the copy needs a new one): "
            f"{', '.join(str(r.get(col)) for r in rows)}\n\n"
            "Rows that point at the target (copied with the target):\n" +
            ("\n".join(f"`{t}`:\n{_dumps(rs)}" for t, rs in kids.items()) or "(none)") +
            f"\n\nReplica notes:\n\n{notes}\n\nDescribe the copy, following the rules.")


def _value(text: str, like=None):
    """The writer's value (JSON text), typed like the target's field: a Slack ts written as a bare number stays the
    exact string the writer wrote (a float would change its digits)."""
    try:
        value = json.loads(text)
    except (TypeError, ValueError):
        return text
    if isinstance(like, str) and not isinstance(value, str):
        return text.strip() if isinstance(value, (int, float)) else value
    if isinstance(like, bool) or like is None:
        return value
    if isinstance(like, (int, float)) and isinstance(value, str):
        try:
            return type(like)(float(value))
        except ValueError:
            return value
    return value


def _target_row(case: dict) -> dict:
    ref = case["references"][0]
    table = ref["query"]["table"]
    col = effect_key(case["domain"], table)[0]
    return next((r for r in case["seed"][table] if str(r.get(col)) == str(ref["expected"][0])), {})


def _clone_checks(case: dict, changes: dict, new_key: str) -> list[str]:
    """The new key must be free, and fields the seed keeps unique must change. (Whether every condition still holds is
    checked by fdc in `policy.clone`, and by the reader.)"""
    ref = case["references"][0]
    root = ref["query"]
    out = []
    table = root["table"]
    col = effect_key(case["domain"], table)[0]
    target = next(r for r in case["seed"][table] if str(r.get(col)) == str(ref["expected"][0]))
    if str(new_key) == str(target.get(col)) or any(str(r.get(col)) == str(new_key) for r in case["seed"][table]):
        out.append(f"The new key `{new_key}` is already used in `{table}`.")
    rows = case["seed"][table]
    for f, v in target.items():
        if not UNIQUE_FIELDS.match(f) or v in (None, "", [], {}) or f == col:
            continue
        values = [json.dumps(r.get(f), sort_keys=True, default=str) for r in rows]
        if len(rows) < 2 or len(set(values)) < len(values):  # only fields the seed keeps unique
            continue
        if f not in changes:
            out.append(f"The copy keeps the target's `{f}` ({v!r}), which is unique in every other record.")
        elif json.dumps(changes[f], sort_keys=True, default=str) in values:
            out.append(f"The copy's `{f}` ({changes[f]!r}) is already used by another record.")
    return out


def derive_clone(case: dict, out: Path, calls_log: Path) -> dict:
    vid = f"UC-{case['case_id']}"
    dest = out / vid
    dest.mkdir(parents=True, exist_ok=True)
    record = {"id": vid, "scenario": case["case_id"], "domain": case["domain"], "rounds": []}
    system = (KIT / "prompts" / "clone_writer.md").read_text()
    ws = WORKSPACES / out.name / vid
    session, prompt = None, _clone_prompt(case)
    for round_no in ROUNDS:
        result = agent.run(agent.Call(role="writer", workspace=ws / "writer", prompt=prompt, log_dir=dest / "writer",
                                      calls_log=calls_log, tools=[], schema=CLONE_SCHEMA, system_append=system,
                                      label=vid, resume=session))
        session = result.get("session_id")
        answer = agent.structured(result) or {}
        entry = {"round": round_no, "writer": answer}
        record["rounds"].append(entry)
        if not answer.get("possible"):
            record.update(status="writer_declined", problems=[answer.get("reason", "")])
            break
        like = _target_row(case)
        changes = {c["field"]: _value(c["value"], like.get(c["field"])) for c in answer.get("changes", [])}
        new_key = answer["new_key"]
        findings = _clone_checks(case, changes, new_key)
        variant = None
        if not findings:
            variant, vmeta = clone(case, changes, new_key, variant_id=vid,
                                   skip_children=tuple(answer.get("skip_children", [])))
            findings = list(vmeta["problems"])
            entry["child_rows_copied"] = vmeta.get("child_rows_copied")
        if not findings:
            verdict = reader2.read(variant, ws / f"reader-{round_no}", dest / f"reader-{round_no}", calls_log, vid)
            entry["reader"] = verdict
            # The request is the scenario's own: only the match set is the clone's to get right (amendment 3).
            findings = reader2.problems(variant, verdict, variant["references"][0]["expected"], wording=False)
            entry["wording_notes"] = reader2.wording_notes(verdict)
            entry["contestable"] = reader2.contestable(variant, verdict, variant["references"][0]["expected"])
        entry["findings"] = findings
        record.update(changes=changes, new_key=new_key, skip_children=answer.get("skip_children", []))
        if not findings:
            record.update(status="accepted", problems=[])
            (dest / "variant.json").write_text(json.dumps(variant, indent=1, ensure_ascii=False) + "\n")
            break
        record.update(status="rejected", problems=findings)
        prompt = ("The copy was built and checked, with these findings:\n" + "\n".join(f"- {f}" for f in findings) +
                  "\n\nRevise the copy under the same rules, or answer possible: false if it cannot be done.")
    (dest / "record.json").write_text(json.dumps(record, indent=1, ensure_ascii=False, default=str) + "\n")
    return record


# ---------------------------------------------------------------- driver

def source_cases(source: str) -> list[dict]:
    if source == "exemplars":
        from grounding.runs.autogen_02.phase1_build import exemplars
        return exemplars()
    from grounding.runs.autogen_02.kit.population import scenarios
    return scenarios()


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("kind", choices=["dropf", "clone"])
    parser.add_argument("--source", choices=["exemplars", "population"], required=True)
    parser.add_argument("--scenarios", nargs="+")
    parser.add_argument("--facts", nargs="+", help="scenario:fact pairs, e.g. BOX-21:A:Folder.created_at")
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--concurrency", type=int, default=4)
    args = parser.parse_args()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    calls_log = out / "calls.jsonl"
    cases = [c for c in source_cases(args.source) if not args.scenarios or c["case_id"] in args.scenarios]
    jobs = []
    for case in cases:
        if args.kind == "clone":
            jobs.append((derive_clone, (case, out, calls_log), f"UC-{case['case_id']}"))
            continue
        for fact in facts_of(case):
            if args.facts and f"{case['case_id']}:{fact}" not in args.facts:
                continue
            jobs.append((derive_dropf, (case, fact, out, calls_log), f"{case['case_id']} {fact}"))
    done = 0
    with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        futures = {pool.submit(fn, *a): label for fn, a, label in jobs}
        for fut in as_completed(futures):
            done += 1
            try:
                r = fut.result()
                print(f"[{done}/{len(jobs)}] {r['id']}: {r['status']} {r.get('request') or ''} "
                      f"{r.get('problems') or ''}"[:600], flush=True)
            except Exception:
                print(f"[{done}/{len(jobs)}] {futures[fut]}: FAILED {traceback.format_exc()[-800:]}", flush=True)


if __name__ == "__main__":
    main()
