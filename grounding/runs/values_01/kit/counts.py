"""The counts behind the report: every check, with its denominator, by service, test form and grounding outcome, and
clustered by scenario (one belief, such as Linear's priority scale, repeats over a scenario's trials and variants).
No model calls; reads data/values.json, writes.json and reply.json.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.values_01.kit.counts

Writes data/counts.json.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict

from grounding.runs.values_01.kit.common import DATA, executions, read
from grounding.runs.values_01.kit.specs import SPECS

FAMILY = {"issues.priority": "Linear priority", "issues.estimate": "Linear estimate",
          "box_files.tags": "Box tag", "box_folders.tags": "Box tag",
          "message_reactions.reaction_type": "Slack reaction", "channels.is_archived": "archive state",
          "calendar_list_entries.hidden": "Calendar hidden", "cycles.endsAt": "date", "box_tasks.due_at": "date",
          "calendar_events.color_id": "Calendar colour", "calendars.time_zone": "time zone",
          "comments.resolvedAt": "reopen", "comments.resolvingUserId": "reopen",
          "documents.projectId": "record as value", "box_hub_items.item_id": "record as value",
          "channel_members.channel_id": "record as value", "channel_members.user_id": "record as value"}
OK = {"ok", "normalized"}


def family(field: str, scenario: str | None = None) -> str:
    """The field's family; a request whose right value depends on the run date is its own family (the lead)."""
    if scenario and any(s.get("run_date") and s["field"] == field for s in SPECS.get(scenario, [])):
        return "run-date dependent date"
    return FAMILY.get(field, "free text")


def by(rows, key):
    out = defaultdict(list)
    for r in rows:
        out[key(r)].append(r)
    return out


def main():
    ex = executions()
    values, writes, reply = read("values"), read("writes"), read("reply")
    rows = []
    for e in ex:
        v, w, r = values[e["key"]], writes[e["key"]], reply[e["key"]]
        form = e["form"]
        rows.append({**{k: e[k] for k in ("key", "domain", "kind", "scenario", "outcome", "grounding", "timeout")},
                     "form": form, "v": v, "w": w, "r": r})
    out = {"executions": len(rows)}

    # Values: rows written to a specified field, by family and where; errors are verdicts outside OK.
    vrows = [(x, row) for row in rows for x in row["v"].get("values", [])]
    fam = defaultdict(Counter)
    for x, row in vrows:
        f = family(x["field"], row["scenario"])
        c = fam[f]
        c["writes"] += 1
        c[f"writes on {x['where']}"] += 1
        c[f"verdict {x['verdict']}"] += 1
        if x["verdict"] not in OK:
            c[f"not ok on {x['where']}"] += 1
    out["values_by_family"] = {f: dict(c) for f, c in sorted(fam.items())}
    # Executions with a value error, by grounding outcome (does a passing verdict hide it?).
    def is_error(x, row):
        return x["verdict"] not in OK | {"keywords present"} and family(x["field"], row["scenario"]) != \
            "run-date dependent date"
    err_ex = [row for row in rows if any(is_error(x, row) for x in row["v"].get("values", []))]
    out["value_error_executions"] = {
        "executions": len(err_ex),
        "wrote_specified_field": sum(1 for row in rows if row["v"].get("values")),
        "by_grounding": dict(Counter(row["grounding"] for row in err_ex)),
        "by_kind": dict(Counter(row["kind"] for row in err_ex)),
        "by_form": dict(Counter(row["form"] for row in err_ex)),
        "by_domain": dict(Counter(row["domain"] for row in err_ex)),
        "on_target_with_passing_grounding": sum(
            1 for row in err_ex if row["grounding"] == "pass" and any(
                x["where"] == "target" and is_error(x, row) for x in row["v"]["values"])),
        "run_date_dependent_other_year": sum(1 for x, row in vrows if family(x["field"], row["scenario"]) ==
                                             "run-date dependent date" and x["verdict"] == "other year"),
        "scenarios": len({row["scenario"] for row in err_ex}),
        "by_family_scenarios": {f: len({row["scenario"] for x, row in vrows if family(x["field"], row["scenario"]) == f
                                        and x["verdict"] not in OK | {"keywords present"}})
                                for f in fam},
        "needs_reader": sum(1 for x, row in vrows if x["verdict"] == "keywords present"),
    }
    # Denominators by form: executions, executions that wrote anything, wrote a specified field.
    out["denominators"] = {
        f"{k}": {"executions": len(rs), "wrote": sum(1 for r in rs if r["v"].get("wrote")),
                 "wrote_specified": sum(1 for r in rs if r["v"].get("values")),
                 "reply_checked": sum(1 for r in rs if r["r"].get("checked"))}
        for k, rs in sorted(by(rows, lambda r: (r["domain"], r["form"])).items())}

    # Side effects.
    se = {}
    for key in ("other_fields", "other_records", "other_tables", "no_net_change", "replica_effects"):
        hit = [row for row in rows if row["v"].get(key)]
        se[key] = {"executions": len(hit), "by_domain_table": dict(Counter(
            f"{row['domain']} {x['table']}" for row in hit for x in row["v"][key])),
            "by_kind": dict(Counter(row["kind"] for row in hit)), "by_grounding": dict(Counter(
                row["grounding"] for row in hit)), "scenarios": len({row["scenario"] for row in hit})}
    hit = [row for row in rows if row["w"].get("not_in_diff")]
    se["writes_not_in_diff"] = {"executions": len(hit), "by_kind": dict(Counter(row["kind"] for row in hit)),
                                "later_write": sum(1 for row in hit if any(m.get("later_write")
                                                                           for m in row["w"]["not_in_diff"])),
                                "inverse_op": sum(1 for row in hit if any(m.get("inverse")
                                                                          for m in row["w"]["not_in_diff"])),
                                "keys": [row["key"] for row in hit]}
    hit = [row for row in rows if row["w"].get("rejected")]
    se["rejected_writes"] = {"executions": len(hit), "by_domain": dict(Counter(row["domain"] for row in hit)),
                             "ops": dict(Counter(o for row in hit for x in row["w"]["rejected"] for o in x["ops"])),
                             "error_but_applied": dict(Counter(o for row in hit for x in row["w"]["rejected"]
                                                               if x.get("applied") for o in x["ops"]))}
    se["unresolved_write_ids"] = sum(1 for row in rows if row["w"].get("unresolved"))
    # Cycle 2: Calendar writes that ask the service to email attendees, by the record written.
    notify = [row for row in rows if row["w"].get("notify")]
    where = Counter()
    for row in notify:
        recs = {x["record"]: x["where"] for x in row["v"].get("values", [])}
        for n in row["w"]["notify"]:
            ws = {recs.get(i) or recs.get(i + "@group.calendar.google.com") for i in n["ids"]} - {None}
            where[next(iter(ws)) if len(ws) == 1 else ("several" if ws else "unmatched")] += 1
    se["calendar_notifications"] = {"executions": len(notify), "writes_by_record": dict(where),
                                    "calendar_executions_writing": sum(1 for row in rows if row["domain"] == "calendar"
                                                                       and row["v"].get("wrote"))}
    out["side_effects"] = se

    # Replies.
    checked = [row for row in rows if row["r"].get("checked")]
    rp = {"replies_checked": len(checked), "no_reply": dict(Counter(row["r"].get("no_reply") for row in rows
                                                                    if not row["r"].get("checked")))}
    for chk in ("R1", "R2", "R2b", "R2c", "R3", "R4"):
        hit = [row for row in checked if any(f["check"] == chk for f in row["r"].get("flags", []))]
        rp[chk] = {"executions": len(hit), "by_kind": dict(Counter(row["kind"] for row in hit)),
                   "by_domain": dict(Counter(row["domain"] for row in hit)),
                   "by_grounding": dict(Counter(row["grounding"] for row in hit)),
                   "scenarios": len({row["scenario"] for row in hit})}
    rp["stance"] = {
        "claims_change": sum(1 for row in checked if row["r"]["stance"].get("claims_change")),
        "no_match": sum(1 for row in checked if row["r"]["stance"].get("no_match")),
        "no_change": sum(1 for row in checked if row["r"]["stance"].get("no_change")),
        "asks": sum(1 for row in checked if row["r"]["stance"].get("asks")),
        "claims_change_among_writers": sum(1 for row in checked if row["v"].get("values")
                                           and row["r"]["stance"].get("claims_change")),
        "writers": sum(1 for row in checked if row["v"].get("values"))}
    out["replies"] = rp

    # Any finding, per execution, and whether the grounding verdict passed it.
    def findings(row):
        f = set()
        if any(is_error(x, row) for x in row["v"].get("values", [])):
            f.add("value")
        if any(family(x["field"], row["scenario"]) == "run-date dependent date" and x["verdict"] == "other year"
               for x in row["v"].get("values", [])):
            f.add("value, run-date dependent")
        if any(row["v"].get(k) for k in ("other_fields", "other_records", "other_tables")):
            f.add("side effect")
        if row["v"].get("no_net_change") or row["w"].get("not_in_diff"):
            f.add("undone or no-op write")
        for fl in row["r"].get("flags", []):
            f.add(f"reply {fl['check']}")
        return f
    anyf = [(row, findings(row)) for row in rows]
    out["any_finding"] = {
        "executions": sum(1 for _, f in anyf if f),
        "by_grounding": dict(Counter(row["grounding"] for row, f in anyf if f)),
        "passing_grounding": sum(1 for row, f in anyf if f and row["grounding"] == "pass"),
        "kinds": dict(Counter(k for _, f in anyf for k in f)),
        "kinds_on_passing": dict(Counter(k for row, f in anyf if row["grounding"] == "pass" for k in f)),
    }
    (DATA / "counts.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps({k: out[k] for k in ("value_error_executions", "any_finding")}, indent=1))
    print(json.dumps(out["replies"], indent=1)[:3000])


if __name__ == "__main__":
    main()
