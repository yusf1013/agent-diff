"""Classify every regular test and policy unit by whether it can be set up on the real service (no model calls).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.transfer_feasibility_01.classify

Reads inventory.json (what each test depends on), rules.json (what each construct needs, with sources.json behind
it) and the case files for the checks that need the seed itself. For each test or unit:
- **class**: `as_is` (one account, the actor's, creates it exactly), `team` (exact, but other people must be real
  accounts), `change` (possible with a stated change), `no` (not with ordinary accounts);
- **changes**: the tags of every construct that needs one (date_shift, multi_day, rename, ui, plan:<plan>,
  workspace, pilot), and `accounts:<n>`;
- **people**: accounts other than the actor; `acting`: those that must use their own API token.
The lead's three classes are as_is + team ("realizable as is, with test accounts"), change, and no.

Per-test checks: Linear seeds with more than 2 teams need a paid plan (Free allows 2); a Box test on collections
is realizable only with a single collection renamed to Favorites; Calendar events of type focusTime, outOfOffice or
workingLocation need a work account and a primary calendar; a group ACL needs a Google Group and a domain ACL a
Workspace domain; room attendees need a Workspace domain; records created after their last modification cannot
exist; a test on a fixed clock is seeded on the right real day.

Writes tests.csv (one row per test or unit) and classification.json (the counts).
"""
from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

from grounding.runs.openclaw_eval_01 import policy
from grounding.runs.transfer_feasibility_01.inventory import OC, SUITES, load

HERE = Path(__file__).resolve().parent
RANK = {"as_is": 0, "team": 1, "change": 2, "no": 3}
SERVER_TIME_FACTS = {"A:File.created_at", "A:File.modified_at", "A:Folder.created_at", "A:Folder.modified_at",
                     "A:Comment.created_at", "A:Task.created_at", "A:Hub.created_at", "A:Conversation.created_at",
                     "A:Message.created_at", "A:Issue.updatedAt", "A:Comment.resolvedAt"}
PRIMARY_ONLY_TYPES = {"focusTime", "outOfOffice", "workingLocation"}


def cases() -> dict:
    """case id -> case, for the regular tests and the policy units (the same files inventory.py read)."""
    out = {}
    for index, folder in SUITES:
        for m in load(index):
            path = folder / m["domain"] / f"{m['case_id']}.json"
            if path.exists():
                out[m["case_id"]] = load(path)
    for mode in ("absence", "underspecified"):
        for seq in policy.population_plan(mode)["cells"].values():
            for u in policy.population_units(seq)[0]:
                out[u["unit"]] = policy.unit_case(u)
    return out


def rule_for(rules: dict, domain: str, table: str, field: str):
    r = rules[domain]
    return r.get(f"{table}.{field}") or r.get(f"{table}.*")


def seed_checks(case: dict, constructs: set[str]) -> list[tuple[str, list[str], str]]:
    """(class, tags, reason) from the seed itself."""
    out, seed, d = [], case["seed"], case["domain"]
    if d == "linear":
        teams = len(seed.get("teams", []))
        if teams > 2:
            out.append(("change", ["plan:Linear Basic"], f"{teams} teams; the Free plan allows 2"))
    if d == "box" and any(c.startswith(("box_collections.", "box_files.collections", "box_folders.collections"))
                          for c in constructs):
        named = [c for c in seed.get("box_collections", []) if (c.get("name") or "").lower() != "favorites"]
        if len(seed.get("box_collections", [])) > 1:
            out.append(("no", [], f"{len(seed['box_collections'])} collections; only Favorites exists"))
        elif named:
            out.append(("change", ["rename"], f"collection '{named[0].get('name')}' becomes Favorites"))
    if d == "box":
        witnesses = {str(c["witness"]) for ref in case["references"] for c in ref.get("claims", [])}
        facts = {c["requirement"] for ref in case["references"] for c in ref.get("claims", [])}
        names = {str(u["id"]): u.get("name") for u in seed.get("box_users", [])}
        folders = {str(f["id"]): f for f in seed.get("box_folders", [])}
        stray = [r for r in seed.get("box_files", []) + seed.get("box_folders", [])
                 if str(r.get("parent_id")) in folders
                 and str(folders[str(r["parent_id"])].get("owned_by_id")) != str(r.get("owned_by_id"))]
        if stray:
            if facts & {"R:File.owned_by_id", "R:Folder.owned_by_id"}:
                out.append(("no", ["pilot"], f"{len(stray)} item(s) owned by someone other than their folder's owner, "
                                             "and the test turns on ownership; on Box a folder's owner owns what is in "
                                             "it (inferred from the move rule; confirm with one collaborator upload)"))
            else:
                out.append(("change", ["consistency", "pilot"], f"{len(stray)} item(s) owned by someone other than "
                                                                "their folder's owner; on Box ownership follows the "
                                                                "folder (inferred from the move rule)"))
        if any(f.get("uploader_display_name") and names.get(str(f.get("created_by_id"))) != f["uploader_display_name"]
               for f in seed.get("box_files", [])):
            out.append(("change", ["consistency", "pilot"], "a file's uploader is not its creator; on Box the "
                                                            "uploader creates the file ('in most cases'), so "
                                                            "created_by follows the uploader"))
        for table in ("box_files", "box_folders"):
            for r in seed.get(table, []):
                if r.get("created_at") and r.get("modified_at") and r["created_at"] > r["modified_at"]:
                    if str(r.get("id")) in witnesses:
                        out.append(("no", [], f"near miss {r['id']} was created after its last modification"))
                    else:
                        out.append(("change", ["date_shift"],
                                    f"record {r['id']} was created after its last modification; seed it in order"))
    if d == "calendar":
        primary = {c["id"] for c in seed.get("calendars", []) if c.get("id") == c.get("owner_id")} | \
            {e["calendar_id"] for e in seed.get("calendar_list_entries", []) if e.get("primary")}
        for ev in seed.get("calendar_events", []):
            if ev.get("event_type") in PRIMARY_ONLY_TYPES:
                if ev.get("calendar_id") in primary:
                    out.append(("change", ["workspace"], f"a {ev['event_type']} event needs a work account"))
                else:
                    out.append(("no", [], f"a {ev['event_type']} event on a secondary calendar"))
        for acl in seed.get("calendar_acl_rules", []):
            if acl.get("scope_type") == "group":
                out.append(("change", ["rename"], "a group ACL needs a Google Group (its email replaces the seed's)"))
            elif acl.get("scope_type") == "domain":
                out.append(("change", ["workspace"], "a domain ACL needs a Workspace domain"))
        if any(a.get("resource") for a in seed.get("calendar_event_attendees", [])):
            out.append(("change", ["workspace"], "a room attendee needs a Workspace domain's resources"))
    return out


def classify(row: dict, case: dict, rules: dict, unknown: Counter) -> dict:
    classes, tags, reasons = [], set(), []
    constructs, facts = set(), set()
    for c in row["constructs"]:
        via, table, field, fact, to = c.split("|")
        if fact:
            facts.add(fact)
        for t, f in ([(table, field)] if table and field else []) + \
                ([tuple(to.split(".", 1))] if to and "." in to else []):
            constructs.add(f"{t}.{f}")
            r = rule_for(rules, row["domain"], t, f)
            if r is None:
                unknown[(row["domain"], f"{t}.{f}")] += 1
                continue
            classes.append(r["class"])
            if r["class"] != "as_is":
                tags.update(r.get("tags", []))
                reasons.append(f"{t}.{f}: {r['why']}")
    for cls, t, why in seed_checks(case, constructs):
        classes.append(cls)
        tags.update(t)
        reasons.append(why)
    if row["clock"] and row["domain"] != "calendar":
        classes.append("change")
        tags.add("date_shift")
        reasons.append(f"runs on a fixed clock ({row['clock']}); seed on a matching real day")
    server_facts = facts & SERVER_TIME_FACTS
    if server_facts and (row["absolute_date"] or "date_shift" in tags):
        if row["absolute_date"] or any(w in row["prompt"].lower() for w in (
                "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "yesterday")):
            tags.add("multi_day")
            reasons.append(f"a near miss differs by {sorted(server_facts)} on a named day: seed over several days")
    uploaders = set()
    if row["domain"] == "box":
        actor = {str(u["id"]): u.get("name") for u in case["seed"].get("box_users", [])}.get(str(case.get("acting_user_id")))
        uploaders = {f["uploader_display_name"] for f in case["seed"].get("box_files", [])
                     if f.get("uploader_display_name") and f["uploader_display_name"] != actor}
        known = {str(u["id"]): u.get("name") for u in case["seed"].get("box_users", [])}
        uploaders -= {known.get(a) for a in row["acting_users"]}
    people = len(row["acting_users"]) + row["existing_users"] + len(uploaders)
    if people:
        classes.append("team")
        tags.add(f"accounts:{people}")
    cls = max(classes or ["as_is"], key=RANK.get)
    return {"id": row["id"], "kind": row["kind"], "domain": row["domain"], "form": row["form"],
            "scenario": row["scenario"], "class": cls,
            "lead_class": {"as_is": "as is", "team": "as is with test accounts", "change": "with a change",
                           "no": "not realizable"}[cls],
            "people": people, "acting": len(row["acting_users"]) + len(uploaders),
            "changes": ";".join(sorted(tags)), "blocking": " | ".join(r for r in reasons if "no" == cls and
                                                                   any(k in r for k in ("only Favorites",
                                                                                        "secondary calendar",
                                                                                        "Hubs", "hub",
                                                                                        "created after",
                                                                                        "turns on ownership"))),
            "reasons": " | ".join(reasons), "exposed_on_openclaw": ";".join(row.get("exposed") or []),
            "prompt": row["prompt"]}


def main():
    rules = load(HERE / "rules.json")
    rows = load(HERE / "inventory.json")
    by_id = cases()
    unknown = Counter()
    out = [classify(r, by_id[r["id"]], rules, unknown) for r in rows]
    with (HERE / "tests.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)
    summary = {"tests": len(out), "unknown_constructs": {f"{d}:{c}": n for (d, c), n in unknown.items()},
               "by_class": dict(Counter(o["class"] for o in out)),
               "by_domain_kind_class": defaultdict(dict), "change_tags": dict(Counter(
                   t.split(":")[0] if t.startswith("accounts") else t for o in out for t in o["changes"].split(";") if t)),
               "people": dict(sorted(Counter(o["people"] for o in out).items()))}
    for o in out:
        k = f"{o['domain']}/{o['kind']}"
        summary["by_domain_kind_class"][k][o["class"]] = summary["by_domain_kind_class"][k].get(o["class"], 0) + 1
    (HERE / "classification.json").write_text(json.dumps(summary, indent=1) + "\n")
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
