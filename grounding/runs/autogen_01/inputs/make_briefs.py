"""Write the briefs of plan.md: dev (4), Arm R (the 18 fact_coverage_02 scenarios' fact sets) and Arm P (16).

    python3 -m grounding.runs.autogen_01.inputs.make_briefs

Arm R takes each fact_coverage_02 new scenario's claimed facts. The Slack scenarios used older names for five
facts; they are mapped to the catalog ids the writer sees (SLACK_ALIASES).
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
FC2 = HERE.parents[1] / "fact_coverage_02" / "cases_new"
SLACK_ALIASES = {"A:Channel.is_private": "A:Conversation.is_private",
                 "A:Channel.purpose_text": "A:Conversation.purpose_text",
                 "H:Message.parent_id": "H:messages.parent_id", "R:Message.channel_id": "R:messages.channel_id",
                 "R:Message.user_id": "R:messages.user_id"}
DEV = [
    ("DV-BOX-01", "box", ["A:Hub.title", "A:Hub.description", "A:Hub.created_at"]),
    ("DV-CAL-01", "calendar", ["A:Event.status", "A:Event.hangout_link", "A:EventAttendee.resource"]),
    ("DV-LIN-01", "linear", ["A:ProjectMilestone.status", "A:ProjectMilestone.targetDate",
                             "R:Issue.projectMilestoneId"]),
    ("DV-SLK-01", "slack", ["A:User.title", "A:User.timezone", "A:User.is_active"]),
]
ARM_P = [
    ("AP-BOX-01", "box", ["A:Folder.size", "A:Folder.shared_link", "A:Folder.modified_at"]),
    ("AP-BOX-02", "box", ["A:File.created_at", "A:Comment.created_at"]),
    ("AP-CAL-01", "calendar", ["A:Calendar.summary", "A:CalendarListEntry.selected"]),
    ("AP-CAL-02", "calendar", ["R:CalendarListEntry.calendar_id", "B:AclRule.calendar_id"]),
    ("AP-LIN-01", "linear", ["A:Issue.completedAt", "A:Issue.description", "R:Issue.stateId"]),
    ("AP-LIN-02", "linear", ["A:User.email", "A:User.name", "A:User.guest"]),
    ("AP-LIN-03", "linear", ["A:Team.key", "A:Team.description", "A:Team.private"]),
    ("AP-LIN-04", "linear", ["A:Cycle.name", "A:Cycle.startsAt", "B:Issue.cycleId"]),
    ("AP-LIN-05", "linear", ["A:Comment.createdAt", "A:Comment.resolvedAt", "B:Comment.issueId"]),
    ("AP-LIN-06", "linear", ["A:Attachment.title", "A:Attachment.url", "R:Attachment.issueId"]),
    ("AP-LIN-07", "linear", ["A:Document.title", "A:Document.content", "R:Document.teamId"]),
    ("AP-SLK-01", "slack", ["A:User.username", "A:User.display_name", "A:User.real_name"]),
    ("AP-SLK-02", "slack", ["A:Conversation.channel_name", "A:Conversation.topic_text",
                            "A:Conversation.is_archived"]),
    ("AP-SLK-03", "slack", ["A:Reaction.reaction_type", "R:message_reactions", "B:message_reactions.user"]),
    ("AP-SLK-04", "slack", ["D:reply_count", "A:Message.message_text", "B:messages.user_id"]),
    ("AP-SLK-05", "slack", ["D:member_count", "A:Conversation.created_at", "A:WorkspaceMembership.role"]),
]


def catalog_ids(domain):
    data = json.loads((HERE.parents[1] / "fact_coverage_01" / "catalog" / f"{domain}.json").read_text())
    return {r["id"] for r in data["requirements"]}


def arm_r():
    out = []
    for path in sorted(FC2.glob("*/*.json")):
        case = json.loads(path.read_text())
        if case["case_id"].startswith(("P-", "PP-")) or "-A" in case["case_id"] or "TWIN" in case["case_id"]:
            continue  # probes, packed tests and the policy panel are derived, not scenarios
        facts = sorted({SLACK_ALIASES.get(c["requirement"], c["requirement"])
                        for r in case["references"] for c in r["claims"]})
        out.append((f"AR-{case['case_id']}", case["domain"], facts, case["case_id"]))
    return out


def main():
    sets = {"dev": [(i, d, f, None) for i, d, f in DEV], "arm_r": arm_r(), "arm_p": [(i, d, f, None) for i, d, f in ARM_P]}
    for name, items in sets.items():
        briefs = []
        for sid, domain, facts, source in items:
            unknown = set(facts) - catalog_ids(domain)
            if unknown:
                raise SystemExit(f"{sid}: facts not in the {domain} catalog: {sorted(unknown)}")
            brief = {"scenario_id": sid, "domain": domain, "facts": facts}
            if source:
                brief["exemplar"] = source  # for the comparison only; the writer never sees this field
            briefs.append(brief)
        (HERE / f"briefs_{name}.json").write_text(json.dumps(briefs, indent=1) + "\n")
        print(name, len(briefs), sum(len(b["facts"]) for b in briefs), "facts")


if __name__ == "__main__":
    main()
