"""Probe seeds for the strategy runner (cycle 1): each isolates one candidate hiding place.

A probe has a service, a seed, the targets (the matches of an imagined plural request), the place being probed, and
the entry parameters the strategies use (the named folder, team or channel, the search words, the time window).
Near misses do not matter to retrieval, so the probes carry none; they come back when tests are built.
"""
from __future__ import annotations

A = "jordan.lee@northwind.example"
WEEK = {"from": "2018-06-18T00:00:00-07:00", "to": "2018-06-23T00:00:00-07:00"}


def box_tree():
    return {"id": "BX-TREE", "domain": "box",
            "place": "a folder tree: 2 matches in the named folder, 1 a level down, 1 two levels down",
            "seed": [["folder", {"id": "5100", "name": "Finance"}],
                     ["folder", {"id": "5101", "name": "Q1", "parent": "5100"}],
                     ["folder", {"id": "5102", "name": "Q2", "parent": "5100"}],
                     ["folder", {"id": "5103", "name": "Receipts", "parent": "5102"}],
                     ["file", {"id": "5111", "name": "Budget 2026.pdf", "parent": "5100", "owner": "MC"}],
                     ["file", {"id": "5112", "name": "Cash forecast.pdf", "parent": "5100", "owner": "MC"}],
                     ["file", {"id": "5113", "name": "Q1 close summary.pdf", "parent": "5101", "owner": "MC"}],
                     ["file", {"id": "5114", "name": "Travel receipts June.pdf", "parent": "5103", "owner": "MC"}]],
            "targets": ["5111", "5112", "5113", "5114"],
            "entry": {"folder": "5100", "words": "Finance", "ext": "pdf"}}


def box_page():
    seed = [["folder", {"id": "5200", "name": "Contracts"}],
            ["file", {"id": "5201", "name": "Acme MSA 2026.pdf", "parent": "5200", "modifier": "LP"}],
            ["file", {"id": "5202", "name": "Birchwood lease.pdf", "parent": "5200", "modifier": "LP"}],
            ["file", {"id": "5203", "name": "Walker NDA.pdf", "parent": "5200", "modifier": "LP"}],
            ["file", {"id": "5204", "name": "Zenith SOW.pdf", "parent": "5200", "modifier": "LP"}]]
    seed += [["file", {"id": str(5300 + i), "name": f"M-{i:03d} supplier terms.docx", "parent": "5200"}]
             for i in range(1, 147)]
    return {"id": "BX-PAGE", "domain": "box", "place": "a 150-item folder: 2 matches on the first page, 2 after it",
            "seed": seed, "targets": ["5201", "5202", "5203", "5204"],
            "entry": {"folder": "5200", "words": "Contracts", "ext": "pdf"}}


def calendars(hidden: bool):
    seed = [["calendar", {"id": "projects@northwind.example", "summary": "Projects"}],
            ["calendar", {"id": "vendors@northwind.example", "summary": "Vendors", "hidden": hidden}],
            ["calendar", {"id": "maya-team@northwind.example", "summary": "Maya's team", "owner": "maya",
                          "access": "writer"}]]
    ev = lambda i, cal, day: ["event", {"id": i, "calendar": cal, "summary": "Vendor sync",
                                        "start": f"2018-06-{day}T10:00:00", "end": f"2018-06-{day}T10:30:00"}]
    seed += [ev("ev_a", "primary", "18"), ev("ev_b", "primary", "20"), ev("ev_c", "projects@northwind.example", "19"),
             ev("ev_d", "vendors@northwind.example", "21")]
    return {"id": "CL-HIDDEN" if hidden else "CL-OWNED", "domain": "calendar",
            "place": ("an owned calendar hidden in the calendar list" if hidden else
                      "owned secondary calendars, all visible in the calendar list")
            + ": 2 matches on primary, 1 on Projects, 1 on Vendors",
            "seed": seed, "targets": ["ev_a", "ev_b", "ev_c", "ev_d"], "entry": {**WEEK, "q": "Vendor sync"}}


def lin_page():
    seed = [["team", {"id": "t-plat", "name": "Platform", "key": "PLAT"}]]
    people = ["maya", "priya", "leo", "dana", "omar"]

    def day(i):
        return f"2026-{1 + (i - 1) // 28:02d}-{1 + (i - 1) % 28:02d}T09:00:00"
    for i in range(1, 71):
        sam = i in (1, 2, 69, 70)
        seed.append(["issue", {"id": f"i-plat-{i:02d}", "team": "t-plat", "title": f"Platform task {i}",
                               "state": "Todo", "assignee": "sam" if sam else people[i % 5], "created": day(i)}])
    filtered = ('{ issues(first: 250, filter: {team: {name: {eq: "Platform"}}, assignee: {name: {eq: "Sam Rivera"}}, '
                'state: {type: {nin: ["completed", "canceled"]}}}) { nodes { id } } }')
    return {"id": "LN-PAGE", "domain": "linear", "place": "70 issues in one team: 2 matches first, 2 last",
            "seed": seed, "targets": ["i-plat-01", "i-plat-02", "i-plat-69", "i-plat-70"],
            "entry": {"team": "Platform", "filtered": filtered}}


def lin_subteam():
    seed = [["team", {"id": "t-pay", "name": "Payments", "key": "PAY"}],
            ["team", {"id": "t-paym", "name": "Payments Mobile", "key": "PAYM", "parent": "t-pay"}],
            ["team", {"id": "t-payw", "name": "Payments Web", "key": "PAYW", "parent": "t-pay"}],
            ["team", {"id": "t-plat", "name": "Platform", "key": "PLAT"}],
            ["label", {"name": "Bug", "ref": "bug"}],
            ["issue", {"id": "i-pay-1", "team": "t-pay", "title": "Refund totals off", "labels": ["@bug"]}],
            ["issue", {"id": "i-pay-2", "team": "t-pay", "title": "Duplicate charge", "labels": ["@bug"]}],
            ["issue", {"id": "i-paym-1", "team": "t-paym", "title": "Pay sheet closes", "labels": ["@bug"]}],
            ["issue", {"id": "i-payw-1", "team": "t-payw", "title": "Card field focus", "labels": ["@bug"]}],
            ["issue", {"id": "i-plat-1", "team": "t-plat", "title": "Worker leak", "labels": ["@bug"]}]]
    filtered = ('{ issues(first: 250, filter: {team: {name: {eq: "Payments"}}, labels: {some: {name: {eq: "Bug"}}}}) '
                '{ nodes { id } } }')
    return {"id": "LN-SUBTEAM", "domain": "linear", "place": "sub-teams: 2 matches in the named team, 1 in each "
            "sub-team", "seed": seed, "targets": ["i-pay-1", "i-pay-2", "i-paym-1", "i-payw-1"],
            "entry": {"team": "Payments", "filtered": filtered}}


def slk_private():
    members = ["omar", "leo", "priya"]
    seed = [["channel", {"id": "C_IDB", "name": "incident-db", "members": members}],
            ["channel", {"id": "C_IAU", "name": "incident-auth", "members": members}],
            ["channel", {"id": "C_IPY", "name": "incident-payments", "members": members, "private": True}],
            ["channel", {"id": "C_GEN", "name": "general", "members": members}]]
    msgs = [("C_IDB", "Starting the rollback of migration 212.", "t1"),
            ("C_IAU", "Rollback of auth-service 3.1 complete.", "t2"),
            ("C_IPY", "Payments rollback to 5.0.2 is underway.", "t3"),
            ("C_IPY", "Rollback finished; refunds are flowing.", "t4")]
    for n, (ch, text, ref) in enumerate(msgs):
        seed.append(["message", {"channel": ch, "author": "omar", "text": text,
                                 "at": f"2026-09-1{4 + n}T12:0{n}:00Z", "ref": ref}])
    return {"id": "SK-PRIVATE", "domain": "slack", "place": "a private channel inside a name-prefix scope: 2 matches "
            "in public channels, 2 in the private one", "seed": seed, "targets": ["@t1", "@t2", "@t3", "@t4"],
            "entry": {"prefix": "incident-", "search": "rollback", "channel": "C_IDB"}}


def slk_history(search_crowd: bool):
    seed = [["channel", {"id": "C_DEP", "name": "deploys", "members": ["priya", "diego", "leo", "omar", "aisha"]}]]
    authors = ["leo", "omar", "aisha", "priya"]

    def at(i):
        h = 3 * (i - 1)
        return f"2026-09-{1 + h // 24:02d}T{h % 24:02d}:10:00Z"
    special = {3: "t1", 6: "t2", 134: "t3", 137: "t4"}
    for i in range(1, 141):
        if i in special:
            seed.append(["message", {"channel": "C_DEP", "author": "diego", "text": f"Deploying payments-api 4.{i}.",
                                     "at": at(i), "ref": special[i]}])
        else:
            text = (f"payments-api canary check {i} passed." if search_crowd and i % 4 == 0
                    else f"Deployed search-api build {1000 + i}.")
            seed.append(["message", {"channel": "C_DEP", "author": authors[i % 4], "text": text, "at": at(i)}])
    return {"id": "SK-SEARCH" if search_crowd else "SK-HISTORY", "domain": "slack",
            "place": ("a busy search: 34 other messages also mention payments-api" if search_crowd else
                      "a 140-message channel history: 2 matches among the newest 100, 2 older"),
            "seed": seed, "targets": ["@t1", "@t2", "@t3", "@t4"],
            "entry": {"prefix": "deploys", "search": "payments-api", "channel": "C_DEP"}}


# ------------------------------------------------------------------ cycle 2
def box_tree_modifier():
    """A tree, and a condition no search can express: the last modifier (shown in listings). Mixed file types, so an
    extension search spans only some targets."""
    seed = [["folder", {"id": "5100", "name": "Finance"}],
            ["folder", {"id": "5101", "name": "Q1", "parent": "5100"}],
            ["folder", {"id": "5102", "name": "Q2", "parent": "5100"}],
            ["folder", {"id": "5103", "name": "Receipts", "parent": "5102"}],
            ["file", {"id": "5111", "name": "Budget 2026.pdf", "parent": "5100", "modifier": "LP"}],
            ["file", {"id": "5112", "name": "Cash forecast.xlsx", "parent": "5100", "modifier": "LP"}],
            ["file", {"id": "5113", "name": "Q1 close summary.docx", "parent": "5101", "modifier": "LP"}],
            ["file", {"id": "5114", "name": "Travel receipts June.pdf", "parent": "5103", "modifier": "LP"}],
            ["file", {"id": "5121", "name": "Headcount plan.xlsx", "parent": "5100", "modifier": "MC"}],
            ["file", {"id": "5122", "name": "Q2 close summary.docx", "parent": "5102", "modifier": "DW"}]]
    return {"id": "BX-TREE-MOD", "domain": "box",
            "place": "a folder tree with the last modifier as the condition: 2 matches in the named folder, 1 a "
                     "level down, 1 two levels down; mixed file types",
            "seed": seed, "targets": ["5111", "5112", "5113", "5114"],
            "entry": {"folder": "5100", "words": "Finance", "ext": "pdf", "person": "Leo Park"}}


def lin_subteam_big():
    base = lin_subteam()
    seed = list(base["seed"])
    people = ["maya", "priya", "leo", "dana", "omar"]
    seed += [["issue", {"id": f"i-plat-f{i:03d}", "team": "t-plat", "title": f"Platform chore {i}",
                        "assignee": people[i % 5]}] for i in range(1, 281)]
    return {**base, "id": "LN-SUBTEAM-BIG", "seed": seed,
            "place": "sub-teams in a 285-issue workspace: 2 matches in the named team, 1 in each sub-team"}


def slk_channels():
    members = ["omar", "leo", "priya"]
    chans = [("C_MIG1", "infra-migration", False, "Tracking the Q3 migration cutover"),
             ("C_MIG2", "db-upgrade", False, "Q3 migration: database steps"),
             ("C_MIG3", "payments-cutover", True, "Q3 migration for payments (private)"),
             ("C_MIG4", "auth-cutover", True, "Auth work for the Q3 migration"),
             ("C_OTH1", "general", False, "Company announcements"),
             ("C_OTH2", "random", False, "Anything goes")]
    seed = [["channel", {"id": c, "name": n, "members": members, "private": p, "topic": t}] for c, n, p, t in chans]
    seed += [["message", {"channel": c, "author": "omar", "text": "Kickoff notes are in the doc.",
                          "at": f"2026-09-1{i}T12:00:00Z"}] for i, (c, *_rest) in enumerate(chans[:4], 1)]
    return {"id": "SK-CHANNELS", "domain": "slack", "strategies": "slack-channels",
            "place": "a request about channels (topic mentions the Q3 migration): 2 public, 2 private",
            "seed": seed, "targets": ["C_MIG1", "C_MIG2", "C_MIG3", "C_MIG4"], "entry": {"topic": "Q3 migration"}}


def slk_archived():
    members = ["diego", "leo"]
    seed = [["channel", {"id": "C_DEP", "name": "deploys", "members": members}],
            ["channel", {"id": "C_DEP2", "name": "deploys-2025", "members": members, "set": {"is_archived": True}}]]
    for n, (ch, ref) in enumerate([("C_DEP", "t1"), ("C_DEP", "t2"), ("C_DEP2", "t3"), ("C_DEP2", "t4")]):
        seed.append(["message", {"channel": ch, "author": "diego", "text": f"Deploying payments-api 4.{n}.",
                                 "at": f"2026-0{3 + n}-10T12:00:00Z", "ref": ref}])
    return {"id": "SK-ARCHIVED", "domain": "slack",
            "place": "an archived channel inside a name-prefix scope: 2 matches in the live channel, 2 in the archived "
                     "one", "seed": seed, "targets": ["@t1", "@t2", "@t3", "@t4"],
            "entry": {"prefix": "deploys", "search": "payments-api", "channel": "C_DEP"}}


# ------------------------------------------------------------------ cycle 4
def slk_dms():
    """A message-level request with no channel scope: 2 matches in public channels, 1 in a group DM, 1 in a DM."""
    seed = [["channel", {"id": "C_OPS", "name": "payments-ops", "members": ["priya", "diego"]}],
            ["channel", {"id": "C_INC", "name": "incidents", "members": ["priya", "leo"]}],
            ["channel", {"id": "G_TRIO", "name": "mpdm-priya--leo--bot", "members": ["priya", "leo"], "gc": True,
                         "private": True}],
            ["dm", {"id": "D_PRIYA", "person": "priya"}]]
    msgs = [("C_OPS", "t1"), ("C_INC", "t2"), ("G_TRIO", "t3"), ("D_PRIYA", "t4")]
    for n, (ch, ref) in enumerate(msgs):
        seed.append(["message", {"channel": ch, "author": "priya", "text": f"Rollback plan step {n + 1} is ready.",
                                 "at": f"2026-09-21T12:0{n}:00Z", "ref": ref}])
    return {"id": "SK-DMS", "domain": "slack", "strategies": "slack-messages",
            "place": "a message request with no channel scope: 2 matches in public channels, 1 in a group DM, 1 in "
                     "a DM", "seed": seed, "targets": ["@t1", "@t2", "@t3", "@t4"], "entry": {"search": "rollback"}}


def from_scenarios():
    """The built tests' own seeds (cycle 3 on): check on each that every lazy strategy misses a match."""
    import json
    from pathlib import Path
    out = []
    for path in sorted((Path(__file__).resolve().parent / "scenarios").glob("*.json")):
        s = json.loads(path.read_text())
        channel_level = s["reference"]["query"]["table"] == "channels"
        out.append({"id": s["scenario_id"], "domain": s["domain"], "seed": s["seed"],
                    "strategies": "slack-channels" if channel_level else s["domain"],
                    "place": "the test's own seed", "targets": s["reference"]["target"],
                    "entry": s["strategy_entry"]})
    return out


def box_combined():
    """Cycle 6: one seed with every Box placement, under a condition the listing shows and search cannot express
    (not a Word document; the matches are PDFs and spreadsheets): 2 in the named folder, 1 two levels down, and 1
    beyond the first 1000 items of a large subfolder."""
    seed = [["folder", {"id": "5100", "name": "Finance"}],
            ["folder", {"id": "5102", "name": "Q2", "parent": "5100"}],
            ["folder", {"id": "5103", "name": "Receipts", "parent": "5102"}],
            ["folder", {"id": "5104", "name": "Supplier terms", "parent": "5100"}],
            ["file", {"id": "5111", "name": "Budget 2026.pdf", "parent": "5100"}],
            ["file", {"id": "5112", "name": "Cash forecast.xlsx", "parent": "5100"}],
            ["file", {"id": "5121", "name": "Board memo.docx", "parent": "5100"}],
            ["file", {"id": "5114", "name": "Travel receipts June.pdf", "parent": "5103"}],
            ["file", {"id": "5115", "name": "Zeta rates.xlsx", "parent": "5104"}]]
    seed += [["file", {"id": str(90000 + i), "name": f"S-{i:04d} supplier terms.docx", "parent": "5104"}]
             for i in range(1, 1101)]
    return {"id": "BX-COMBINED", "domain": "box",
            "place": "every placement in one seed: 2 in the named folder, 1 two levels down, 1 beyond the first 1000 "
                     "items of a subfolder; the condition (not a Word document) no search expresses",
            "seed": seed, "targets": ["5111", "5112", "5114", "5115"],
            "entry": {"folder": "5100", "words": "Finance", "ext": "pdf", "person": "Leo Park"}}


def slk_combined():
    """Cycle 6: one seed with every placement for a request about messages in a set of channels (incident-*), under
    a condition history shows (the author): 1 in a public channel's newest page, 1 beyond its largest page, 1 in a
    private channel, 1 in an archived channel. Search words that name no condition are crowded out."""
    members = ["omar", "leo", "priya"]
    seed = [["channel", {"id": "C_IDB", "name": "incident-db", "members": members}],
            ["channel", {"id": "C_IPY", "name": "incident-payments", "members": members, "private": True}],
            ["channel", {"id": "C_IOLD", "name": "incident-2025", "members": members, "set": {"is_archived": True}}],
            ["channel", {"id": "C_GEN", "name": "general", "members": members}]]

    def at(i):  # message i of 1100 in incident-db, one every 30 minutes from 2026-07-01
        m = 30 * (i - 1)
        return f"2026-{7 + m // (60 * 24 * 31):02d}-{1 + (m // (60 * 24)) % 31:02d}T{(m // 60) % 24:02d}:{m % 60:02d}:00Z"
    for i in range(1, 1101):
        ref = {20: "t2", 1090: "t1"}.get(i)
        msg = {"channel": "C_IDB", "author": "leo" if ref else ["omar", "priya"][i % 2],
               "text": f"Rollback check {i} logged.", "at": at(i)}
        if ref:
            msg["ref"] = ref
        seed.append(["message", msg])
    seed += [["message", {"channel": "C_IPY", "author": "leo", "text": "Rollback check for payments logged.",
                          "at": "2026-09-10T12:00:00Z", "ref": "t3"}],
             ["message", {"channel": "C_IOLD", "author": "leo", "text": "Rollback check from last year.",
                          "at": "2025-11-02T12:00:00Z", "ref": "t4"}],
             ["message", {"channel": "C_GEN", "author": "leo", "text": "Rollback check done everywhere.",
                          "at": "2026-09-11T12:00:00Z"}]]
    return {"id": "SK-COMBINED", "domain": "slack",
            "place": "every placement in one seed: newest page, beyond the largest page, a private channel, an "
                     "archived channel; the condition (the author) is in every history message",
            "seed": seed, "targets": ["@t1", "@t2", "@t3", "@t4"],
            "entry": {"prefix": "incident-", "search": "rollback", "channel": "C_IDB"}}


def lin_combined():
    """Cycle 6: LN-SUBTEAM's sub-teams with 70 more issues in the named team, so the default page of 50 leaves
    matches out too (the oldest two and the newest two)."""
    base = lin_subteam()
    created = {"i-pay-1": "2026-01-01T09:00:00", "i-pay-2": "2026-01-02T09:00:00",
               "i-paym-1": "2026-06-01T09:00:00", "i-payw-1": "2026-06-02T09:00:00"}
    seed = [[k, {**r, "created": created[r["id"]]}] if k == "issue" and r["id"] in created else [k, r]
            for k, r in base["seed"]]
    seed += [["issue", {"id": f"i-pay-f{i:02d}", "team": "t-pay", "title": f"Payments task {i}",
                        "created": f"2026-{2 + (i - 1) // 28:02d}-{1 + (i - 1) % 28:02d}T09:00:00"}]
             for i in range(1, 71)]
    return {**base, "id": "LN-COMBINED", "seed": seed,
            "place": "sub-teams and a 75-issue named team: the oldest 2 matches in the named team, the newest 2 in "
                     "its sub-teams"}


PROBES = [box_tree(), box_page(), calendars(False), calendars(True), lin_page(), lin_subteam(), slk_private(),
          slk_history(False), slk_history(True), box_tree_modifier(), lin_subteam_big(), slk_channels(),
          slk_archived(), slk_dms(), box_combined(), slk_combined(), lin_combined()] + from_scenarios()
