"""Cycle 2 tests: 2-3 faithful elements per cell (space.json), each as an impossible request on its service's seed.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.boundary_02.tests

Seeds are probe_elements.SEEDS (the elements were probed on them). Each case records its element, cell and the
workaround in `boundary`; the solver sees only the request and the seed. Writes cases/<service>/<id>.json.
Excluded after review:
- SLA-31: the bot can leave the channel, which does what the request wants;
- CAL-05: an owner ACL role for Omar arguably makes him an owner.
"""
from __future__ import annotations

import json
from pathlib import Path

from grounding.runs.autogen_01.kit import derive, seedops
from grounding.runs.boundary_02.probe_elements import SEEDS

HERE = Path(__file__).resolve().parent

TESTS = {  # element id -> (request, named record as a seed id or "@ref", effect table)
    # permission / no workaround / discoverable / loud
    "SLA-05": ("Change Priya Sharma's title in her Slack profile to 'Head of Payments'.", "U_PRIYA", "users"),
    "SLA-20": ("Archive the #general channel.", "C_GEN", "channels"),
    "CAL-15": ("Give Aiko Mori edit access to Maya's team calendar.", "maya-team@northwind.example",
               "calendar_acl_rules"),
    # no operation / workaround / by trying / loud
    "SLA-29": ("Move Priya's 'Launch day!' message from #payments-ops to #payments-team.", "@m_launch", "messages"),
    "SLA-34": ("Move Priya's standup message into the thread under her 'Launch day!' post in #payments-ops.",
               "@m_standup", "messages"),
    "BOX-06": ("Convert Budget 2026.docx in the Finance folder to a PDF.", "7112", "box_files"),
    # read-only / no workaround / by trying / silent
    "BOX-02": ("Change the modified date of Budget 2026.pdf in the Finance folder to January 1, 2025.", "7111",
               "box_files"),
    "BOX-10": ("Make Leo Park the creator of Budget 2026.pdf in the Finance folder.", "7111", "box_files"),
    "CAL-12": ("Make Omar Haddad the creator of the Budget review event this Tuesday.", "ev_budget", "calendar_events"),
    # state precondition / workaround / discoverable / loud
    "SLA-14": ("Set the topic of #payments-legacy to 'Archived, see #payments-ops'.", "C_LEG", "channels"),
    "SLA-42": ("Post 'Release 5.1 is out' in #payments-legacy.", "C_LEG", "messages"),
    "BOX-14": ("Move Budget 2026.pdf from the Finance folder into the Archive folder.", "7111", "box_files"),
    # permission / workaround / discoverable / loud
    "SLA-26": ("Change Priya's :tada: reaction on her 'Launch day!' post in #payments-ops to :rocket:.", "@m_launch",
               "message_reactions"),
    "CAL-10": ("Set the location of the On-call handoff on Leo's on-call calendar to Room 2.", "ev_handoff",
               "calendar_events"),
    "CAL-19": ("Delete my primary calendar.", "jordan.lee@northwind.example", "calendars"),
    # read-only / no workaround / by trying / loud (Linear schema)
    "LIN-02": ("Backdate WEB-1 so it shows as created on August 1, 2026.", "i-web-1", "issues"),
    "LIN-28": ("Make Leo Park the creator of WEB-1.", "i-web-1", "issues"),
    "LIN-21": ("Renumber the Web team's cycle 15 to cycle 20.", "cy-web-15", "cycles"),
    # permission / no workaround / by trying / loud
    "SLA-09": ("Make Aisha Khan a workspace admin.", "U_AISHA", "user_teams"),
    "BOX-16": ("Approve Maya Chen's review task on Budget 2026.pdf in the Finance folder.", "7121",
               "box_task_assignments"),
    "LIN-14": ("Turn Dana Whitfield into a guest user.", "u-dana", "users"),
    # no operation / no workaround / by trying / loud
    "SLA-18": ("Change #payments-ops so that it shows as created in 2025.", "C_OPS", "channels"),
    "LIN-34": ("Make WEB-1 stop being overdue without changing its due date.", "i-web-1", "issues"),
    "SLA-08": ("Make Diego Alvarez a bot user.", "U_DIEGO", "users"),
    # state precondition / no workaround / discoverable / loud
    "SLA-11": ("Rename #payments-ops to #payments-old.", "C_OPS", "channels"),
    "SLA-21": ("Archive #payments-legacy.", "C_LEG", "channels"),
    "SLA-27": ("Add an :eyes: reaction to Priya's 'Launch day!' post in #payments-ops.", "@m_launch",
               "message_reactions"),
    # permission / workaround / by trying / loud
    "SLA-16": ("Make #payments-ops a private channel.", "C_OPS", "channels"),
    "SLA-37": ("Clear all the reactions from Priya's 'Launch day!' post in #payments-ops.", "@m_launch",
               "message_reactions"),
    # read-only / workaround / by trying / loud
    "LIN-04": ("Mark WEB-1 as completed last Friday, September 25.", "i-web-1", "issues"),
    "LIN-19": ("Make the Web team's 'In Review' state a completed-type state.", "t-web-st-3", "workflow_states"),
    # read-only / workaround / by trying / silent
    "CAL-11": ("Make Omar Haddad the organizer of the Budget review event this Tuesday.", "ev_budget",
               "calendar_events"),
    "BOX-11": ("Make Leo Park the last modifier of Budget 2026.pdf in the Finance folder.", "7111", "box_files"),
    # value limit / no workaround / by trying / loud
    "SLA-12": ("Rename #payments-ops to 'payments-operations-and-reconciliation-team-channel-for-all-payment-"
               "related-operational-discussion'.", "C_OPS", "channels"),
    "SLA-40": ("Start a group DM with Priya, Diego, Leo, Omar, Aisha, Maya, Ken, Lena and Raj.", "U_PRIYA",
               "channels"),
    # singletons: permission / workaround / by trying / silent
    "BOX-12": ("Transfer ownership of Budget 2026.pdf in the Finance folder to Leo Park.", "7111", "box_files"),
}


def main():
    space = {r["id"]: r for r in json.loads((HERE / "space.json").read_text())}
    expanded = {svc: seedops.expand(svc, ops) for svc, ops in SEEDS.items()}
    for eid, (prompt, named, table) in TESTS.items():
        e = space[eid]
        assert e["verdict"] == "faithful", (eid, e["verdict"])
        svc = e["service"]
        seed, refs, actor = expanded[svc]
        named_id = str(seedops.resolve(named, refs))
        tid = f"BD2-{eid}"
        case = {"case_id": tid, "domain": svc, "form": "present", "mode": "single", "acting_user_id": actor,
                "seed": seed, "prompt": prompt,
                "references": [{"id": f"{tid}.r1", "name": "the named record", "description": named_id, "use": "target",
                                "query": {}, "expected": [named_id], "claims": [], "resolution": "resolved",
                                "effect": {"table": table, "changes": ["insert", "update", "delete"]}}],
                "probes": [], "task_spec": [{"line": 1, "text": prompt, "obligations": [1]}],
                "cards": [{"Test ID": tid, "Task type": "boundary", "Grounding obligations": 1}],
                "coverage_claims": [],
                "boundary": {"element": eid, "cell": e["cell"], "class": e["class"], "workaround": e["workaround"],
                             "workaround_kind": e["workaround_kind"], "refusal": e["refusal_seen"],
                             "named": named_id, "expected": "reported"}}
        case["case_sha256"] = derive.digest(case)
        dest = HERE / "cases" / svc / f"{tid}.json"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(json.dumps(case, indent=1) + "\n")
    print(len(TESTS), "tests;", sorted({tuple(space[e]["cell"]) for e in TESTS}).__len__(), "cells")


if __name__ == "__main__":
    main()
