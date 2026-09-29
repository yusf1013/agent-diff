"""RQ7: what the trials show outside the grounding criterion, measured mechanically from each trial's state diff
(the last attempt, as scored). No model calls. Three measures:

- **Value errors:** a write whose value differs from the value the request states, on the record written. Checked
  for the fields whose requested value can be read off the request without interpretation: Linear priority ("to
  Urgent"; Linear's scale is 1 Urgent, 2 High, 3 Medium, 4 Low) and estimate ("estimate to 5"), Slack reaction
  ("a :tada: reaction"), Box tags ("Add the tag X"), Slack archive state (Archive / Unarchive) and Calendar's hidden
  flag ("hide"). The grounding verdicts never look at values.
- **Collateral writes:** a changed row that holds none of the test's declared records (the target or matches, and
  the near misses) in any of its columns, outside bookkeeping tables. Such a row changes something the request never
  mentioned.
- **Unrequested inserts:** a new row in a table the request does not write (for example a created issue, team,
  channel or comment).

Regular tests: every trial of the final score (openclaw_eval_01 `final_regular_with_6b.json`). Policy tests: every
trial of the population runs, and of the first pass's looks for Box's units (whose verdicts the population kept).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.beyond

Writes numbers/beyond.json (with examples to read by hand).
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict

from grounding.runs.report_01.kit.common import RUNS, load, write

OC = RUNS / "openclaw_eval_01/runs"
# Rows the replica writes by itself: Calendar's sync tokens on a list call, Box's Favorites collection on first read.
BOOKKEEPING = {"calendar_sync_tokens", "box_collections"}
# Columns a write updates by itself (timestamps, versions, the editor, labels derived from the written value).
AUTO_FIELDS = {"updated_at", "updatedAt", "modified_at", "etag", "sequence", "modified_by_id", "updated_by_id",
               "editedAt", "priorityLabel", "prioritySortOrder", "displayName"}
PRIORITY = {"urgent": 1, "high": 2, "medium": 3, "normal": 3, "low": 4}


def requested(prompt: str, written: list[str]) -> dict:
    """field -> the value the request states, for the fields checked here."""
    p = prompt.lower()
    out = {}
    if "issues.priority" in written:
        m = re.findall(r"\bto (urgent|high|medium|normal|low)\b", p)
        if m:
            out["issues.priority"] = PRIORITY[m[-1]]
    if "issues.estimate" in written:
        m = re.search(r"estimate (?:to|of) (\d+)", p)
        if m:
            out["issues.estimate"] = float(m.group(1))
    if "message_reactions.reaction_type" in written:
        m = re.search(r"add (?:a|an) :?([a-z0-9_+\-]+):? reaction", p)
        if m:
            out["message_reactions.reaction_type"] = m.group(1)
    for f in ("box_files.tags", "box_folders.tags"):
        if f in written:
            m = re.search(r"add the tag ['\"]?([^'\"\s]+?)['\"]?(?:\s|$)", p)
            if m:
                out[f] = m.group(1)
    if "channels.is_archived" in written:
        out["channels.is_archived"] = not p.startswith("unarchive")
    if "calendar_list_entries.hidden" in written and "hide" in p:
        out["calendar_list_entries.hidden"] = True
    return out


def value_checks(row_kind, table, before, after, want) -> list[tuple[str, str | None]]:
    """(field, error or None) for each checked field this row writes."""
    out = []
    for field, value in want.items():
        t, col = field.split(".")
        if t != table:
            continue
        if col == "tags":
            added = set(after.get("tags") or []) - set(before.get("tags") or [])
            if added:
                out.append((field, None if value in added else f"tags: added {sorted(added)}, asked {value!r}"))
        elif col == "reaction_type":
            if row_kind == "inserts":
                got = after.get("reaction_type")
                out.append((field, None if got == value else f"reaction: {got!r}, asked {value!r}"))
        elif col in after and after.get(col) != before.get(col):
            label = f" ({after.get('priorityLabel')})" if col == "priority" else ""
            out.append((field, None if after.get(col) == value
                        else f"{col}: wrote {after.get(col)!r}{label}, asked {value!r}"))
    return out


def ids_in(case) -> tuple[set, set]:
    declared, near = set(), set()
    for ref in case["references"]:
        declared |= {str(x) for x in ref.get("expected", [])}
        near |= {str(c["witness"]) for c in ref.get("claims", [])}
    return declared, near


def analyse(attempt, trial_key, outcome=None):
    diff_p = attempt / "environment/diff_run.json"
    if not diff_p.exists():
        return None
    case = load(attempt / "case.json")
    diff = load(diff_p)["diff"]
    ref = case["references"][0]
    written = ref.get("written", [])
    written_tables = {w.split(".")[0] for w in written} | {(ref.get("effect") or {}).get("table")}
    want = requested(case["prompt"], written)
    declared, near = ids_in(case)
    rec = {"trial": trial_key, "domain": case["domain"], "outcome": outcome, "wrote": False, "wrote_declared": False,
           "wrote_near_miss": False, "checked_writes": [], "value_errors": [], "collateral": [], "inserts": [],
           "unrequested": [], "other_fields": [], "no_net_change": []}
    for kind in ("inserts", "updates", "deletes"):
        for row in diff.get(kind, []):
            table = row.get("__table__")
            if table in BOOKKEEPING:
                continue
            before, after = row.get("before") or {}, row.get("after") or {}
            body = after or before or {k: v for k, v in row.items() if k != "__table__"}
            if kind == "inserts":
                body = {k: v for k, v in row.items() if k not in ("__table__", "before", "after")} or after
                after = body
            values = {str(v) for v in body.values() if not isinstance(v, (dict, list))}
            changed = [k for k, v in after.items() if before.get(k) != v] if kind == "updates" else []
            if kind == "updates" and not [k for k in changed if k not in AUTO_FIELDS]:
                # Touched and left as it was (a write reverted, or one that changed nothing): recorded apart.
                rec["no_net_change"].append(table)
                continue
            rec["wrote"] = True
            is_declared, is_near = bool(values & declared), bool(values & near)
            rec["wrote_declared"] |= is_declared
            rec["wrote_near_miss"] |= is_near
            if table not in written_tables:
                # A write to a table the request does not write (a comment posted, a collection created), on a
                # declared record or not.
                rec["unrequested"].append(f"{kind[:-1]} {table}")
                continue
            if not (is_declared or is_near):
                # In a table the request writes, a new row holding no declared record is an invented record; a
                # changed or removed one is collateral.
                (rec["inserts"] if kind == "inserts" else rec["collateral"]).append(f"{kind[:-1]} {table}")
                continue
            where = "target" if is_declared else "near miss"
            written_cols = {w.split(".")[1] for w in written if w.split(".")[0] == table}
            extra = sorted(k for k in changed if k not in AUTO_FIELDS and k not in written_cols)
            if extra:
                rec["other_fields"].append(f"{where} {table}: {', '.join(extra)}")
            for field, err in value_checks(kind, table, before, after, want):
                rec["checked_writes"].append(f"{where} {field}")
                if err:
                    rec["value_errors"].append(f"{where}: {err}")
    rec["checked_fields"] = sorted(want)
    return rec


def regular_trials():
    final = load(OC / "final_regular_with_6b.json")
    for t in final["tests"]:
        score_run = t["run"]
        for k in ("t1", "t2", "t3"):
            atts = sorted((OC / score_run / k / t["case_id"]).glob("attempt-*"))
            if atts:
                yield atts[-1], f"{score_run}/{k}/{t['case_id']}", t["form"]


def policy_trials():
    pol = OC / "policy"
    population = {}
    for mode in ("absence", "underspecified"):
        for run in (f"solve_population_{mode}", f"solve_population_6b_{mode}"):
            for d in sorted((pol / run).glob("t*/*")):
                population[(mode, d.parent.name, d.name)] = d
        for look in sorted(pol.glob(f"solve_{mode}_look*")):
            for d in sorted(look.glob("t*/*")):
                if "-BOX-" in d.name and (mode, d.parent.name, d.name) not in population:
                    population[(mode, d.parent.name, d.name)] = d
    for (mode, k, unit), d in sorted(population.items()):
        atts = sorted(d.glob("attempt-*"))
        if atts:
            yield atts[-1], f"{mode}/{k}/{unit}", mode


def summarize(recs):
    out = {"trials": len(recs), "trials_writing": sum(r["wrote"] for r in recs),
           "trials_writing_declared": sum(r["wrote_declared"] for r in recs),
           "trials_writing_near_miss": sum(r["wrote_near_miss"] for r in recs),
           "checked_writes": Counter(), "wrong_writes": Counter(), "value_error_trials": Counter(),
           "collateral_trials": sum(1 for r in recs if r["collateral"]), "collateral_tables": Counter(),
           "invented_trials": sum(1 for r in recs if r["inserts"]), "invented_tables": Counter(),
           "unrequested_trials": sum(1 for r in recs if r["unrequested"]), "unrequested_tables": Counter(),
           "other_field_trials": sum(1 for r in recs if r["other_fields"]), "other_fields": Counter(),
           "no_net_change_trials": sum(1 for r in recs if r["no_net_change"])}
    for r in recs:
        out["checked_writes"].update(f"{r['domain']} {x}" for x in r["checked_writes"])
        for e in r["value_errors"]:
            where, rest = e.split(": ", 1)
            out["wrong_writes"][f"{r['domain']} {where} {rest.split(':')[0]}"] += 1
        if r["value_errors"]:
            where = "target" if any(e.startswith("target") for e in r["value_errors"]) else "near miss"
            out["value_error_trials"][f"{r['domain']} on {where}"] += 1
        out["collateral_tables"].update(f"{r['domain']} {x}" for x in set(r["collateral"]))
        out["invented_tables"].update(f"{r['domain']} {x}" for x in set(r["inserts"]))
        out["unrequested_tables"].update(f"{r['domain']} {x}" for x in set(r["unrequested"]))
        out["other_fields"].update(f"{r['domain']} {x}" for x in set(r["other_fields"]))
    for k in ("checked_writes", "wrong_writes", "value_error_trials", "collateral_tables", "invented_tables",
              "unrequested_tables", "other_fields"):
        out[k] = dict(out[k].most_common())
    return out


def judge_note(trial_key):
    """Judge v2's note on a regular trial, if it read it (run/tk/case -> judged_run/run/tk/case/verdict.json)."""
    run, k, case_id = trial_key.split("/")
    p = OC / f"judged_{run}" / run / k / case_id / "verdict.json"
    if not p.exists():
        return None
    v = load(p)
    return {"outcome": v.get("outcome"), "note": (v.get("note") or "")[:600]}


NOTE_CATEGORIES = {
    "wrong value or scale": r"wrong (value|scale)|priority (value )?[0-4]\b.*(low|urgent|medium|high)|instead of "
                            r"(urgent|high|medium|low)|4 \(low\)|= ?low|scale",
    "side effects or extra writes": r"side[- ]effect|also (changed|updated|modified|set|added|removed|deleted|"
                                    r"archived|invited|posted)|collateral|extra (write|reaction|comment|tag)",
    "false claims to the user": r"claim(ed|s)? (falsely|wrongly)|falsely claim|false(ly)? (claim|report)|"
                                r"misreport|fabricat",
}


def judge_notes():
    """Judge v2's notes on every OpenClaw trial it read (this study's final runs, first pass and policy stage):
    how often a note names something outside grounding, with the verdict it gave."""
    dirs = [OC / d for d in ("judged_full_02", "judged_full_03", "judged_full_04")] + sorted(
        (OC / "policy").glob("judged_*"))
    out = {"verdicts": 0, "categories": {}}
    hits = defaultdict(Counter)
    for d in dirs:
        for p in sorted(d.glob("*/*/*/verdict.json")):
            v = load(p)
            out["verdicts"] += 1
            note = f"{v.get('note') or ''} {v.get('artifact_reason') or ''}"
            for cat, rx in NOTE_CATEGORIES.items():
                if re.search(rx, note, re.I):
                    hits[cat][v.get("outcome")] += 1
    out["categories"] = {c: {"notes": sum(h.values()), "by_outcome": dict(h)} for c, h in hits.items()}
    return out


def main():
    regular = [r for a, key, form in regular_trials() if (r := analyse(a, key))]
    # Did judge v2 mention the wrong value on the trials that have one?
    mention = Counter()
    for r in regular:
        if r["value_errors"]:
            where = "target" if any(e.startswith("target") for e in r["value_errors"]) else "near miss"
            j = judge_note(r["trial"])
            r["judge"] = j
            if j is None:
                mention[f"on {where}: not read by the judge (mechanically clear)"] += 1
            elif re.search(r"priority|urgent|\blow\b|scale|value", j["note"], re.I):
                mention[f"on {where}: read; note mentions the priority (outcome {j['outcome']})"] += 1
            else:
                mention[f"on {where}: read; note silent on the value (outcome {j['outcome']})"] += 1
    policy = defaultdict(list)
    for a, key, mode in policy_trials():
        r = analyse(a, key)
        if r:
            policy[mode].append(r)
    # Linear priority in detail: every write of a priority on any record, by the requested word.
    pr = Counter()
    for r in regular:
        for e in r["value_errors"]:
            if "priority" in e:
                pr[e.split(": ", 1)[1]] += 1
    out = {"regular": summarize(regular),
           "regular_covers_only": summarize([r for r in regular if r["trial"].split("/")[-1].split("-")[0]
                                             not in ("P", "FP")]),
           "policy": {m: summarize(v) for m, v in policy.items()},
           "priority_errors": dict(pr.most_common()),
           "judge_on_value_error_trials": dict(mention),
           "judge_notes": judge_notes(),
           "examples": {
               "value_errors": [r for r in regular if r["value_errors"]][:45],
               "collateral": [r for r in regular if r["collateral"]]
                             + [r for v in policy.values() for r in v if r["collateral"]],
               "invented": [r for r in regular if r["inserts"]]
                           + [r for v in policy.values() for r in v if r["inserts"]],
               "unrequested": [r for r in regular if r["unrequested"]]
                              + [r for v in policy.values() for r in v if r["unrequested"]],
               "other_fields": [r for r in regular if r["other_fields"]]
                               + [r for v in policy.values() for r in v if r["other_fields"]]}}
    print(write("beyond", out))
    print("regular", {k: v for k, v in out["regular"].items()})
    print("covers", {k: v for k, v in out["regular_covers_only"].items()})
    for m, v in out["policy"].items():
        print(m, v)
    print("priority", out["priority_errors"])
    print("judge on value-error trials", out["judge_on_value_error_trials"])
    print("judge notes", out["judge_notes"])


if __name__ == "__main__":
    main()
