"""The evidence a judge sees for one trial: the test, the candidates, the trajectory, the answer and the diff.

Built only from the attempt folder and the case (request, seed, references with their decoy claims). Reference labels
and manual verdicts are never read here.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

BOILERPLATE = {"etag", "sequence_id", "sha1", "sha_1", "type", "item_status", "file_version", "permissions",
               "representations", "watermark_info", "metadata", "classification", "bodyData", "reactionData",
               "currentProgress", "progressHistory", "completedIssueCountHistory", "completedScopeHistory",
               "inProgressScopeHistory", "issueCountHistory", "scopeHistory", "sortOrder", "prioritySortOrder",
               "subIssueSortOrder", "boardOrder", "inviteHash", "url", "branchName", "color", "icon", "slugId",
               "frequencyResolution", "slackIssueComments", "slackIssueStatuses", "slackNewIssue", "trashed_at",
               "purged_at", "content_created_at", "content_modified_at", "uploader_display_name", "is_package"}
OBS_LIMIT = 6000
WINDOW = 400


def compact_row(row: dict, limit: int = 700) -> str:
    keep = {k: v for k, v in row.items() if k not in BOILERPLATE and v not in (None, "", [], {}, "[]")}
    text = json.dumps(keep, ensure_ascii=False, default=str)
    return text if len(text) <= limit else text[:limit] + "…"


def _rows(case, table, key):
    return {str(r.get(key[0])): r for r in case["seed"].get(table, [])} if len(key) == 1 else {}


def candidates(case: dict) -> tuple[str, list[str]]:
    """Text describing each reference's target(s) and decoys, and the handles to watch for in responses."""
    lines, handles = [], []
    for ref in case["references"]:
        query = ref["query"]
        table, key = query["table"], query.get("key", ["id"])
        rows = _rows(case, table, key)
        role = "what the request asks to act on" if ref.get("use") == "target" else "another record the request names"
        lines.append(f"### Reference {ref['id'].split('.')[-1]} ({role}); records live in `{table}`")
        if ref["expected"]:
            for x in ref["expected"]:
                lines.append(f"- TARGET `{x}`: {compact_row(rows.get(str(x), {}))}")
        else:
            lines.append("- No target: no record meets this reference.")
        for c in ref["claims"]:
            w = str(c["witness"])
            fam = f", family {c['family']}" if c.get("family") else ""
            lines.append(f"- DECOY `{w}` (fact `{c['requirement']}`{fam}): {c['explanation']}\n"
                         f"  record: {compact_row(rows.get(w, {}))}")
        for x in list(ref["expected"]) + [c["witness"] for c in ref["claims"]]:
            row = rows.get(str(x), {})
            handles.append(str(x))
            for f in ("identifier", "ts", "name", "title", "summary"):
                if isinstance(row.get(f), str) and len(row[f]) >= 4:
                    handles.append(row[f])
    return "\n".join(lines), sorted(set(handles), key=len, reverse=True)


def excerpt(text: str, handles: list[str], limit: int = OBS_LIMIT) -> str:
    """Keep short observations whole; for long ones keep the head, windows around candidate handles, and the tail."""
    if len(text) <= limit:
        return text
    head = limit // 2
    spans = [(0, head), (len(text) - 500, len(text))]
    for h in handles:
        for m in re.finditer(re.escape(h), text):
            spans.append((max(0, m.start() - WINDOW), min(len(text), m.end() + WINDOW)))
    spans.sort()
    merged = []
    for s, e in spans:
        if merged and s <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], e))
        else:
            merged.append((s, e))
    out, budget, last = [], limit * 2, 0
    for s, e in merged:
        if s > last:
            out.append(f" […{s - last} chars omitted…] ")
        piece = text[s:e]
        out.append(piece[:budget])
        budget -= len(piece)
        last = e
        if budget <= 0:
            out.append(f" […{len(text) - e} chars omitted…]")
            break
    return "".join(out)


def _visible(step: dict) -> str:
    """The solver's visible reasoning for a step (the text block without its <action>)."""
    content = (step.get("response") or {}).get("content") or []
    text = " ".join(c.get("text", "") for c in content if c.get("type") == "text")
    text = re.sub(r"<action>.*?</action>", "", text, flags=re.S)
    text = re.sub(r"</?thinking>", "", text).strip()
    return text[:1500]


def trajectory(record: dict, handles: list[str]) -> str:
    out = []
    for step in record.get("steps", []):
        obs = step.get("observation")
        obs = obs if isinstance(obs, str) else json.dumps(obs, ensure_ascii=False, default=str)
        action = str(step.get("action") or "")
        out.append(f"#### Step {step.get('turn')}\nReasoning: {_visible(step)}\nCommand: {action[:2500]}\n"
                   f"Response: {excerpt(obs or '', handles)}")
    return "\n\n".join(out) if out else "(no steps recorded)"


def diff_text(attempt: Path) -> str:
    path = attempt / "environment" / "diff_run.json"
    if not path.exists():
        return "(no diff recorded)"
    diff = json.loads(path.read_text()).get("diff") or {}
    lines = []
    for row in diff.get("inserts", []):
        lines.append(f"- INSERT {row.get('__table__')}: {compact_row({k: v for k, v in row.items() if k != '__table__'})}")
    for u in diff.get("updates", []):
        before, after = u.get("before", {}), u.get("after", {})
        changed = {k: [before.get(k), after.get(k)] for k in set(before) | set(after)
                   if before.get(k) != after.get(k) and k not in {"updated_at", "updatedAt", "modified_at", "etag",
                                                                    "sequence_id"}}
        ident = after.get("id") or after.get("message_id") or after.get("channel_id")
        lines.append(f"- UPDATE {u.get('__table__')} `{ident}`: " +
                     json.dumps(changed, ensure_ascii=False, default=str)[:800])
    for row in diff.get("deletes", []):
        lines.append(f"- DELETE {row.get('__table__')}: {compact_row({k: v for k, v in row.items() if k != '__table__'})}")
    return "\n".join(lines) if lines else "(no changes)"


def solver_record(attempt: Path) -> dict:
    records = [p for p in (attempt / "solver").glob("*.json") if p.name != "config.json"] \
        if (attempt / "solver").exists() else []
    return json.loads(records[0].read_text()) if records else {}


def build(case: dict, attempt: Path, form: str | None, triage: dict, summary: dict) -> str:
    cand, handles = candidates(case)
    record = solver_record(attempt)
    final = ""
    if (attempt / "solver" / "final_response.md").exists():
        final = (attempt / "solver" / "final_response.md").read_text().strip()
    final = final or (record.get("final") or "")
    present = any(r["use"] == "target" and r["expected"] for r in case["references"])
    termination = record.get("termination") or summary.get("termination")
    status = summary.get("status")
    acted = {r["reference"].split(".")[-1]: r.get("acted", []) for r in triage.get("references", [])}
    return "\n\n".join([
        f"# Trial of test `{case['case_id']}` ({case['domain']})",
        f"Test form: {form or 'unknown'}. Target present: {'yes' if present else 'no'}.",
        f"## Request given to the solver\n{case['prompt']}",
        f"## Candidates\n{cand}",
        f"## Solver steps\nRun status: {status}; termination: {termination}; steps: {len(record.get('steps', []))}."
        + (f" Error: {summary.get('error')}" if summary.get("error") else "") + "\n\n" + trajectory(record, handles),
        f"## Final answer\n{final or '(none)'}",
        f"## State diff\n{diff_text(attempt)}",
        "## Mechanical attribution (from the diff and write commands; may be wrong)\n"
        f"Acted-on records per reference: {json.dumps(acted)}. Provisional outcome: {triage.get('outcome')}. "
        f"Provisional exposed facts: {triage.get('exposed')}.",
    ])
