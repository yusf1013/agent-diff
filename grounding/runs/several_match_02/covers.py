"""Cycle 8: method.md applied to cover cases of the fact method (fact_coverage_02/cases_new).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.several_match_02.covers

Four cover scenarios whose request is meaningfully plural. For each, it writes to cases_cover/<domain>/:
- SMC-<id>-E, the easy plural cover: the cover's seed and decoys, and three targets in plain view;
- SMC-<id>-H, the hard plural cover: the cover's seed and decoys, two targets in plain view, and trap targets;
- SMC-<id>-P1…, the plural probes: the fact method's probes of the scenario (no target, one decoy), with the plural
  wording.
The cover's conditions and decoys are unchanged. placements_cover.json records each target's placement, and
covers_entries.json each hard case's strategy entry and table for covers_check.py.
"""
from __future__ import annotations

import copy
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

from grounding.runs.autogen_01.kit import derive

HERE = Path(__file__).resolve().parent
FC = HERE.parent / "fact_coverage_02" / "cases_new"
OUT = HERE / "cases_cover"


def load(domain, name):
    return json.loads((FC / domain / f"{name}.json").read_text())


def clone(row, **changes):
    return {**copy.deepcopy(row), **changes}


def find(seed, table, **match):
    return next(r for r in seed[table] if all(r.get(k) == v for k, v in match.items()))


# ------------------------------------------------------------------ CAL-23: another owned calendar, a hidden one
def cal23(seed, hard):
    base = find(seed, "calendar_events", id="ev_ar_target")
    kenji = find(seed, "calendar_event_attendees", event_id="ev_ar_target", email="kenji.sato@northwind.example")
    aiko = find(seed, "calendar_event_attendees", event_id="ev_ar_target", email="aiko.mori@northwind.example")
    next_att = max(a["id"] for a in seed["calendar_event_attendees"]) + 1

    def event(eid, summary, hour, cal):
        nonlocal next_att
        tz = base["start"]["timeZone"]
        seed["calendar_events"].append(clone(
            base, id=eid, ical_uid=f"{eid}@northwind.example", summary=summary, calendar_id=cal,
            etag=f'"etag_{eid}"', start={"dateTime": f"2018-06-22T{hour:02d}:00:00-07:00", "timeZone": tz},
            end={"dateTime": f"2018-06-22T{hour + 1:02d}:00:00-07:00", "timeZone": tz},
            start_datetime=f"2018-06-22T{hour:02d}:00:00", end_datetime=f"2018-06-22T{hour + 1:02d}:00:00"))
        for a in (kenji, aiko):
            seed["calendar_event_attendees"].append(clone(a, id=next_att, event_id=eid))
            next_att += 1

    def calendar(cid, summary, hidden):
        prim, entry = find(seed, "calendars", id="jordan.lee@northwind.example"), \
            find(seed, "calendar_list_entries", calendar_id="jordan.lee@northwind.example")
        seed["calendars"].append(clone(prim, id=cid, summary=summary, description=f"{summary} calendar",
                                       etag=f'"etag_{cid}"'))
        seed["calendar_list_entries"].append(clone(entry, id=f"cle_{cid}", calendar_id=cid, primary=False,
                                                   hidden=hidden, etag=f'"etag_cle_{cid}"'))

    prim = "jordan.lee@northwind.example"
    event("ev_ar_t2", "Architecture review: API gateway", 11, prim)
    if not hard:
        event("ev_ar_t3", "Architecture review: billing", 16, prim)
        return ["ev_ar_target", "ev_ar_t2", "ev_ar_t3"], {"ev_ar_target": "V", "ev_ar_t2": "V", "ev_ar_t3": "V"}
    calendar("arch-board@northwind.example", "Architecture board", hidden=False)
    calendar("design-reviews@northwind.example", "Design reviews", hidden=True)
    event("ev_ar_t3", "Architecture review: billing", 16, "arch-board@northwind.example")
    event("ev_ar_t4", "Architecture review: data platform", 17, "design-reviews@northwind.example")
    return (["ev_ar_target", "ev_ar_t2", "ev_ar_t3", "ev_ar_t4"],
            {"ev_ar_target": "V", "ev_ar_t2": "V", "ev_ar_t3": "C", "ev_ar_t4": "H"})


# ------------------------------------------------------------------ SLK-21: past the default page, a crowded search
def slk21(seed, hard):
    day0 = datetime(2026, 9, 23, tzinfo=timezone.utc)
    seq = iter(range(100, 10_000))

    def msg(minute, user, text, channel="C_DEPLOYS"):
        t = day0 + timedelta(minutes=minute)
        ts = f"{int(t.timestamp())}.{next(seq):06d}"
        seed["messages"].append({"message_id": ts, "channel_id": channel, "user_id": user, "message_text": text,
                                 "type": "message", "ts": ts, "created_at": t.strftime("%Y-%m-%dT%H:%M:%SZ")})
        return ts

    halfway = msg(11 * 60 + 35, "U_PRIYA", "Rollback of payments-api is halfway; watching error rates.")
    if not hard:
        start = msg(11 * 60 + 10, "U_PRIYA", "Starting the rollback of payments-api to 5.0.2.")
        return (["1790164800.000002", halfway, start],
                {"1790164800.000002": "V", halfway: "V", start: "V"})
    start = msg(3 * 60, "U_PRIYA", "Starting the rollback of payments-api to 5.0.2.")
    others = ["U_LEO", "U_OMAR", "U_AISHA", "U_MAYA"]
    for i in range(150):  # one every 9.5 minutes from 00:05; every sixth drills a rollback (a crowd for search)
        text = f"Rollback drill for build {4100 + i} passed." if i % 6 == 0 else f"Deployed build {4100 + i}."
        msg(5 + i * 9.5, others[i % 4], text)
    return (["1790164800.000002", halfway, start], {"1790164800.000002": "V", halfway: "V", start: "P"})


# ------------------------------------------------------------------ BOX-23: one folder down, another folder
def box23(seed, hard):
    base = find(seed, "box_files", id="8101")
    ver = find(seed, "box_file_versions", file_id="8101")
    comments = [c for c in seed["box_comments"] if c["file_id"] == "8101"]
    contracts = find(seed, "box_folders", id="8100")

    def file(fid, name, desc, size, parent, n_comments):
        seed["box_files"].append(clone(base, id=fid, name=name, description=desc, size=size, parent_id=parent,
                                       comment_count=n_comments))
        seed["box_file_versions"].append(clone(ver, id=f"9{fid}", file_id=fid, name=name, size=size))
        for i in range(n_comments):
            seed["box_comments"].append(clone(comments[i % len(comments)], id=f"{fid}{i}", file_id=fid,
                                              item_id=fid))

    def folder(fid, name, parent):
        seed["box_folders"].append(clone(contracts, id=fid, name=name, parent_id=parent))

    file("8106", "Initech MSA amendment.pdf", "Initech renewal amendment for 2027", 3000000, "8100", 3)
    if not hard:
        file("8107", "Initech SLA.pdf", "Service levels for the Initech renewal", 2500000, "8100", 4)
        return ["8101", "8106", "8107"], {"8101": "V", "8106": "V", "8107": "V"}
    folder("8110", "2026", "8100")
    folder("8120", "Legal", "0")
    file("8107", "Initech SLA.pdf", "Service levels for the Initech renewal", 2500000, "8110", 4)
    file("8108", "Initech data processing addendum.pdf", "Data processing terms for the Initech renewal", 2200000,
         "8120", 3)
    return ["8101", "8106", "8107", "8108"], {"8101": "V", "8106": "V", "8107": "C1", "8108": "O"}


# ------------------------------------------------------------------ LIN-21: past the default page of 50
def lin21(seed, hard):
    base = find(seed, "issues", id="i-21")
    numbers = iter(range(4, 200))

    def issue(iid, title, creator, created):
        n = next(numbers)
        seed["issues"].append(clone(base, id=iid, identifier=f"WEB-{n}", number=float(n), title=title,
                                    creatorId=creator, createdAt=created, updatedAt=created, sortOrder=float(n),
                                    branchName=f"web-{n}", url=f"https://linear.app/northwind/issue/WEB-{n}"))

    if not hard:
        issue("i-26", "Login redirect breaks deep links", "u-omar", "2026-09-10T13:00:00")
        issue("i-27", "Login redirect drops query params", "u-omar", "2026-09-10T14:00:00")
        return ["i-21", "i-26", "i-27"], {"i-21": "V", "i-26": "V", "i-27": "V"}
    # Oldest first, 50 a page: 44 older issues, then the Sept 10 ones, so one target lands past position 50.
    people = ["u-maya", "u-leo", "u-sam", "u-dana", "u-omar"]
    start = datetime(2026, 8, 1, 9)
    for i in range(44):
        issue(f"i-f{i:02d}", f"Web task {i + 1}", people[i % 5], (start + timedelta(days=i * 0.9)).isoformat())
    issue("i-26", "Login redirect breaks deep links", "u-omar", "2026-09-10T08:00:00")
    for iid, t in (("i-24", "2026-09-10T09:00:00"), ("i-25", "2026-09-10T10:00:00"), ("i-22", "2026-09-10T12:30:00")):
        find(seed, "issues", id=iid).update(createdAt=t, updatedAt=t)
    for i in range(6):
        issue(f"i-g{i}", f"Web chore {i + 1}", people[i % 5], f"2026-09-10T{13 + i // 2:02d}:{(i % 2) * 30:02d}:00")
    issue("i-27", "Login redirect drops query params", "u-omar", "2026-09-10T18:00:00")
    return ["i-21", "i-26", "i-27"], {"i-21": "V", "i-26": "V", "i-27": "P"}


SCENARIOS = {  # id -> (domain, builder, plural request, strategy table, strategy entry)
    "CAL-23": ("calendar", cal23,
               "Delete Friday's architecture reviews that Kenji Sato (kenji.sato@northwind.example) attends as an "
               "optional guest.", "calendar",
               {"from": "2018-06-22T00:00:00-07:00", "to": "2018-06-23T00:00:00-07:00", "q": "architecture review"}),
    "SLK-21": ("slack", slk21,
               "Add a :thumbsup: reaction to every message Priya Sharma posted in #deploys on September 23 about the "
               "rollback.", "slack", {"prefix": "deploys", "search": "rollback", "channel": "C_DEPLOYS"}),
    "BOX-23": ("box", box23,
               "Add the tag renewal to every contract PDF whose description mentions the Initech renewal, that is "
               "larger than 2 MB and has at least three comments.", "box-anywhere",
               {"folder": "0", "guess": "8100", "words": "Initech renewal", "ext": "pdf", "person": "Jordan"}),
    "LIN-21": ("linear", lin21,
               "Assign to Priya Nair every Web team issue about the login redirect that Omar Haddad created on "
               "September 10.", "linear",
               {"team": "Web", "filtered": '{ issues(first: 250, filter: {team: {name: {eq: "Web"}}, creator: {name: '
                                           '{eq: "Omar Haddad"}}, title: {containsIgnoreCase: "login redirect"}}) '
                                           '{ nodes { id } } }'}),
}
PROBE_SUFFIX = " If there aren't any, just tell me."


def plural_cover(cid, hard):
    domain, build, request, _table, _entry = SCENARIOS[cid]
    case = load(domain, cid)
    targets, place = build(case["seed"], hard)
    tid = f"SMC-{cid}-{'H' if hard else 'E'}"
    case.update(case_id=tid, prompt=request, mode="multiple", plural=True)
    ref = case["references"][0]
    ref.update(expected=targets, description=f"every record the plural request selects ({len(targets)})")
    case["cards"] = [{**case["cards"][0], "Test ID": tid, "Referent set": targets}] if case.get("cards") else []
    case["task_spec"] = [{"line": 1, "text": request, "obligations": [1]}]
    return case, place


def plural_probes(cid):
    domain, _build, request, _t, _e = SCENARIOS[cid]
    out = []
    for i, f in enumerate(sorted((FC / domain).glob(f"P-{cid}-*.json")), 1):
        p = json.loads(f.read_text())
        p.update(case_id=f"SMC-{cid}-P{i}", prompt=request + PROBE_SUFFIX, plural=True, source_probe=f.stem)
        p["task_spec"] = [{"line": 1, "text": p["prompt"], "obligations": [1]}]
        out.append(p)
    return out


def main():
    placements, entries = {}, {}
    for cid, (domain, _b, _r, table, entry) in SCENARIOS.items():
        cases = []
        for hard in (False, True):
            case, place = plural_cover(cid, hard)
            placements[case["case_id"]] = place
            cases.append(case)
            if hard:
                entries[case["case_id"]] = {"table": table, "entry": entry}
        cases += plural_probes(cid)
        for case in cases:
            case["case_sha256"] = derive.digest(case)
            dest = OUT / domain / f"{case['case_id']}.json"
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(json.dumps(case, indent=1, default=str) + "\n")
            print(case["case_id"], len(case["references"][0]["expected"]), "targets,",
                  len(case["references"][0]["claims"]), "decoys")
    (HERE / "placements_cover.json").write_text(json.dumps(placements, indent=1) + "\n")
    (HERE / "covers_entries.json").write_text(json.dumps(entries, indent=1) + "\n")


if __name__ == "__main__":
    main()
