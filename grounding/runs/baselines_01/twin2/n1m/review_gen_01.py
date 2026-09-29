"""My hand review of N1M's tests (N1 plus the PI's added lines, run gen_01), written 2026-09-28 before any agent ran
them, by n0/review_rules.md. Same record shape and family judgments as n0/review_gen_01.py and n1/review_gen_01.py;
the replica behaviour applied is listed in twin2/n0m/review_gen_01.py.

    python3 grounding/runs/baselines_01/twin2/n1m/review_gen_01.py     # writes runs/gen_01/review.json, prints totals

A "latest" condition's previous record is F7 (the nearest value on the wrong side), as for N1-SLK-T08 in round 1.
The `oracle_sound` counts are not comparable with round 1's (see twin2/n0m/review_gen_01.py).
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from grounding.runs.baselines_01.n0.review_gen_01 import t  # same record shape
from grounding.runs.baselines_01.twin2.n0m.review_gen_01 import BOT_DELETE, CANCEL, NO_CHECK_MARK

HERE = Path(__file__).resolve().parent
OUT = HERE / "runs" / "gen_01" / "review.json"
CAL_DELETE = "expects the calendar row removed; the replica marks a deleted calendar `deleted` (an update)"
NOT_OWNER = ("a", "only a calendar's owner may delete it (403 in the replica, as in Google Calendar); the actor is a "
                  "writer, so the expected delete is impossible")
ALREADY_MEMBER = ("a", "the seed makes both people members of the channel already, so there is no one to invite (the "
                       "invite returns already_in_channel) and the expected new membership cannot appear")

REVIEW = [
    # ------------------------------------------------------------------ Box
    t("N1M-BOX-T01", "present", ["A:File.name", "A:File.modified_at"],
      near=[("8101", "A:File.modified_at", "F7", "the previous version (May) for the most recently modified (August)")],
      proper=["A:File.modified_at"]),
    t("N1M-BOX-T02", "present", ["A:File.name", "A:File.shared_link"],
      near=[("8201", "A:File.shared_link", "F0", "the same name without a shared link")]),
    t("N1M-BOX-T03", "present", ["A:File.name", "A:File.uploader_display_name"],
      near=[("8301", "A:File.uploader_display_name", "F0", "the same name uploaded by Maya Chen")]),
    t("N1M-BOX-T04", "present", ["A:File.name", "R:TaskAssignment.assigned_by_id",
                                 "A:TaskAssignment.resolution_state", "B:TaskAssignment.task_id"],
      near=[("8402", "A:TaskAssignment.resolution_state", "F0", "Leo's assignment is still incomplete"),
            ("8403", "R:TaskAssignment.assigned_by_id", "F0", "the completed assignment was made by Maya Chen")]),
    t("N1M-BOX-T05", "present", ["A:File.name", "R:TaskAssignment.assigned_to_id", "A:User.name"],
      near=[("8502", "R:TaskAssignment.assigned_to_id", "F8", "assigned to Maya Lopez for Maya Chen")],
      proper=["R:TaskAssignment.assigned_to_id"]),
    t("N1M-BOX-T06", "present", ["A:File.name", "A:Comment.message", "R:Comment.file_id"],
      near=[("8602", "A:Comment.message", "F0", "its second comment is about the timeline, not the budget")]),
    t("N1M-BOX-T07", "present", ["A:Hub.title", "R:Hub.created_by_id", "R:HubItem.file", "R:HubItem.folder"],
      far=["8702: created by Omar and without the Assets folder"]),
    t("N1M-BOX-T08", "present", ["A:File.name", "R:TaskAssignment.assigned_to_id", "B:Task.item_id"],
      near=[("8802", "B:Task.item_id", "F5", "Leo and Dana are each assigned on a separate task of the file")],
      proper=["B:Task.item_id"]),
    t("N1M-BOX-T09", "present", ["A:File.name", "A:Comment.message", "H:Comment.item_id:comment"],
      near=[("89013", "H:Comment.item_id:comment", "F4", "Leo's identical top-level comment for Dana's reply")],
      proper=["H:Comment.item_id:comment"]),
    t("N1M-BOX-T10", "present", ["A:Folder.name", "H:Folder.parent_id"],
      near=[("9002", "H:Folder.parent_id", "F0", "a Contracts folder at the root (not a level)")]),
    t("N1M-BOX-T11", "present", ["A:Folder.name", "R:Folder.created_by_id", "R:Folder.owned_by_id"],
      near=[("9102", "R:Folder.owned_by_id", "F0", "owned by Jordan"),
            ("9103", "R:Folder.created_by_id", "F0", "created by Leo")]),
    t("N1M-BOX-T12", "absence_presupposed", ["A:Hub.title", "R:HubItem.folder", "A:Folder.name"],
      near=[("92011", "(outside the catalog: record type)", "F0", "the hub holds a file named Datasets"),
            ("92012", "R:HubItem.folder", "F0", "the Datasets folder is not in the hub")],
      quality=["removing a hub item returns 501 in the replica, so a wrong removal cannot land in the diff"]),
    # ------------------------------------------------------------------ Calendar
    t("N1M-CAL-T01", "present", ["A:Event.summary"],
      near=[("ev-a", "A:Event.summary", "F8", "'Design review: Cart' shares 'Design review:' with the requested title")],
      proper=["A:Event.summary"], oracle_ok=False, oracle_note=CANCEL),
    t("N1M-CAL-T02", "present", ["A:Event.summary", "A:Event.start"],
      near=[("ev-b", "A:Event.start", "F0", "the same appointment four days later")],
      oracle_ok=False, oracle_note=CANCEL),
    t("N1M-CAL-T03", "present", ["A:Event.summary", "A:Event.location"],
      near=[("ev-a", "A:Event.location", "F0", "Room 5C for Room 4B")],
      oracle_ok=False, oracle_note=CANCEL),
    t("N1M-CAL-T04", "present", ["A:Event.summary", "A:Event.organizer_email", "A:Event.creator_email"],
      near=[("ev-b", "A:Event.creator_email", "F0", "created by Priya; Omar appears nowhere on it"),
            ("ev-c", "A:Event.organizer_email", "F0", "organized by Omar; Priya appears nowhere on it")],
      oracle_ok=False, oracle_note=CANCEL),
    t("N1M-CAL-T05", "present", ["A:Event.summary", "A:Event.transparency"],
      near=[("ev-a", "A:Event.transparency", "F0", "the same lunch shown as busy")],
      oracle_ok=False, oracle_note=CANCEL),
    t("N1M-CAL-T06", "present", ["A:Event.summary", "R:EventAttendee.event_id", "A:EventAttendee.response_status",
                                 "B:EventAttendee.event_id"],
      near=[("ev-b", "A:EventAttendee.response_status", "F0", "Omar accepted"),
            ("ev-c", "R:EventAttendee.event_id", "F0", "Omar is not invited")],
      oracle_ok=False, oracle_note=CANCEL),
    t("N1M-CAL-T07", "present", ["A:Event.summary", "R:EventAttendee.event_id", "A:EventAttendee.response_status",
                                 "B:EventAttendee.event_id"],
      near=[("ev-a", "A:EventAttendee.response_status", "F0", "Omar is tentative; nobody declined"),
            ("ev-b", "A:EventAttendee.response_status", "F0", "Priya is tentative; nobody accepted")],
      oracle_ok=False, oracle_note=CANCEL),
    t("N1M-CAL-T08", "present", ["A:Event.summary", "A:Event.start", "D:local_time", "D:primary"],
      near=[("ev-b", "D:primary", "F0", "the same event on the Side projects calendar"),
            ("ev-c", "A:Event.start", "F7", "a movie night on the next day, June 20")],
      proper=["A:Event.start"], oracle_ok=False, oracle_note=CANCEL,
      quality=["the target is on June 19 in Los Angeles but June 20 in UTC"]),
    t("N1M-CAL-T09", "present", ["A:Calendar.summary", "A:Calendar.time_zone"],
      near=[("cal-a@northwind.example", "A:Calendar.time_zone", "F0", "the same name in Los Angeles time")],
      oracle_ok=False, oracle_note=CAL_DELETE),
    t("N1M-CAL-T10", "present", ["A:Calendar.summary", "A:Calendar.data_owner", "A:CalendarListEntry.access_role"],
      near=[("cal-b@northwind.example", "A:Calendar.data_owner", "F0", "Jordan's own calendar of that name"),
            ("cal-c@northwind.example", "A:CalendarListEntry.access_role", "F7", "Kenji's, but Jordan only reads it")],
      proper=["A:CalendarListEntry.access_role"], flaws=[NOT_OWNER], oracle_ok=False, oracle_note=CAL_DELETE),
    t("N1M-CAL-T11", "present", ["A:CalendarListEntry.summary_override", "A:CalendarListEntry.hidden"],
      near=[("cal-c@northwind.example", "A:CalendarListEntry.hidden", "F0", "the same nickname, not hidden")],
      far=["cal-b@northwind.example: 'Weekend trips' is its real name, not a nickname, and it is not hidden"],
      oracle_ok=False, oracle_note=CAL_DELETE),
    t("N1M-CAL-T12", "absence_presupposed", ["A:Event.summary", "R:EventAttendee.event_id", "A:Event.start"],
      near=[("ev-b", "R:EventAttendee.event_id", "F0", "the June 22 budget sync is with Sam")],
      far=["ev-a: with Priya, on June 20"]),
    # ------------------------------------------------------------------ Linear
    t("N1M-LIN-T01", "present", ["A:Issue.identifier"],
      near=[("i-t01-a", "A:Issue.identifier", "F8", "HRB-1 for HRB-12, the same title")],
      proper=["A:Issue.identifier"]),
    t("N1M-LIN-T02", "present", ["A:Issue.title", "A:Issue.dueDate", "A:Issue.estimate"],
      near=[("i-t02-a", "A:Issue.estimate", "F0", "estimate 3 for 8"),
            ("i-t02-b", "A:Issue.dueDate", "F0", "due November 1")]),
    t("N1M-LIN-T03", "present", ["A:Issue.title", "D:overdue"],
      near=[("i-t03-b", "D:overdue", "F0", "due October 20, not yet due"),
            ("i-t03-c", "D:overdue", "F6", "past due but Done: a completed issue with a past due date")],
      proper=["D:overdue"], quality=["holds while the run date is between 2026-09-10 and 2026-10-20"]),
    t("N1M-LIN-T04", "present", ["A:Issue.title", "R:Issue.assigneeId", "A:User.name"],
      near=[("i-t04-b", "R:Issue.assigneeId", "F1", "Maya created it; Priya is the assignee")],
      proper=["R:Issue.assigneeId"]),
    t("N1M-LIN-T05", "present", ["A:Issue.title", "R:Issue.projectId", "A:Project.name"],
      near=[("i-t05-b", "R:Issue.projectId", "F0", "the same title in project Boreas")]),
    t("N1M-LIN-T06", "present", ["A:Issue.title", "R:Issue.cycleId", "A:Cycle.number"],
      near=[("i-t06-b", "A:Cycle.number", "F0", "the same title in cycle 5")]),
    t("N1M-LIN-T07", "present", ["A:Issue.title", "R:Issue.cycleId", "R:Cycle.teamId", "A:Team.name",
                                 "A:Cycle.endsAt"],
      near=[("i-t07-b", "R:Cycle.teamId", "F1", "the same-numbered, same-dated cycle of the Mobile team"),
            ("i-t07-c", "A:Cycle.endsAt", "F1", "the Web cycle that starts, not ends, on 2026-12-01")],
      proper=["R:Cycle.teamId", "A:Cycle.endsAt"]),
    t("N1M-LIN-T08", "present", ["A:Issue.title", "R:issue_label_issue_association", "A:IssueLabel.name"],
      near=[("i-t08-b", "R:issue_label_issue_association", "F0", "the same title labelled Feature")]),
    t("N1M-LIN-T09", "present", ["A:Issue.title", "R:issue_label_issue_association", "A:IssueLabel.name"],
      near=[("i-t09-b", "R:issue_label_issue_association", "F0", "Bug only"),
            ("i-t09-c", "R:issue_label_issue_association", "F0", "Frontend only")]),
    t("N1M-LIN-T10", "present", ["R:Attachment.issueId", "A:Attachment.title", "A:Attachment.sourceType",
                                 "R:Attachment.creatorId", "B:Attachment.issueId"],
      near=[("i-t10-b", "B:Attachment.issueId", "F5",
             "Maya's 'Launch checklist' is from Slack and her GitHub attachment is another one"),
            ("i-t10-c", "R:Attachment.creatorId", "F0", "the GitHub 'Launch checklist' uploaded by Priya")],
      proper=["B:Attachment.issueId"]),
    t("N1M-LIN-T11", "present", ["A:Issue.title", "R:Issue.projectMilestoneId", "A:ProjectMilestone.name",
                                 "R:ProjectMilestone.projectId", "A:Project.name"],
      near=[("i-t11-b", "A:ProjectMilestone.name", "F0", "Atlas's Alpha milestone"),
            ("i-t11-c", "R:ProjectMilestone.projectId", "F1", "the same-named Beta milestone of project Boreas")],
      proper=["R:ProjectMilestone.projectId"]),
    t("N1M-LIN-T12", "absence_presupposed", ["A:Issue.identifier"],
      near=[("i-t12-a", "A:Issue.identifier", "F8", "VLT-1 for VLT-9"),
            ("i-t12-b", "A:Issue.identifier", "F8", "VLT-2 for VLT-9")]),
    # ------------------------------------------------------------------ Slack
    t("N1M-SLK-T01", "present", ["D:dm_with", "A:User.real_name"],
      near=[("C_K1", "D:dm_with", "F6", "#ops-priya, a channel containing Priya")],
      proper=["D:dm_with"]),
    t("N1M-SLK-T02", "present", ["A:Message.message_text", "A:Message.blocks", "R:messages.channel_id"],
      near=[("m1", "A:Message.blocks", "F0", "the same text without the chart image")],
      flaws=[NO_CHECK_MARK]),
    t("N1M-SLK-T03", "present", ["A:User.real_name", "A:User.email", "R:channel_members"],
      near=[("w1", "A:User.email", "F8", "the other Alex Rivera, alex.rivera@contractor.example")],
      proper=["A:User.email"], flaws=[ALREADY_MEMBER]),
    t("N1M-SLK-T04", "present", ["A:User.real_name", "A:User.is_bot", "R:channel_members"],
      near=[("s1", "A:User.is_bot", "F0", "the bot named Sam Carter")],
      quality=["the request names the competitor to avoid: 'not the bot'"], flaws=[ALREADY_MEMBER]),
    t("N1M-SLK-T05", "present", ["A:Message.message_text", "R:message_reactions", "A:Reaction.reaction_type",
                                 "B:message_reactions.message"],
      near=[("m1", "R:message_reactions", "F0", "only Priya's eyes"),
            ("m2", "R:message_reactions", "F0", "only Diego's white_check_mark")]),
    t("N1M-SLK-T06", "present", ["R:messages.user_id", "A:Message.message_text", "R:messages.channel_id",
                                 "B:messages.channel_id"],
      near=[("m3", "R:messages.channel_id", "F0", "Leo's identical message in #ops-south, where Diego did not post")]),
    t("N1M-SLK-T07", "present", ["D:dm_with", "A:User.real_name"],
      near=[("D_H1", "D:dm_with", "F0", "the DM with Diego")]),
    t("N1M-SLK-T08", "present", ["R:messages.user_id", "D:latest_message", "R:messages.channel_id"],
      near=[("m1", "D:latest_message", "F7", "Leo's earlier update"),
            ("m2", "R:messages.user_id", "F0", "Maya's message")],
      proper=["D:latest_message"], flaws=[BOT_DELETE]),
    t("N1M-SLK-T09", "present", ["A:Message.message_text", "D:reaction_count", "A:Reaction.reaction_type"],
      near=[("m1", "D:reaction_count", "F0", "one thumbsup"),
            ("m3", "D:reaction_count", "F0", "one thumbsup and one eyes")],
      flaws=[BOT_DELETE]),
    t("N1M-SLK-T10", "present", ["R:messages.user_id", "A:Message.message_text", "R:messages.channel_id"],
      near=[("m1", "R:messages.user_id", "F0", "Diego's identical message")]),
    t("N1M-SLK-T11", "present", ["R:messages.user_id", "A:Message.message_text", "H:messages.parent_id"],
      near=[("m3", "H:messages.parent_id", "F4", "Diego's identical top-level message for his reply")],
      far=["m1: the thread's root, Priya's"], proper=["H:messages.parent_id"], flaws=[BOT_DELETE]),
    t("N1M-SLK-T12", "absence_presupposed", ["D:reaction_count", "A:Reaction.reaction_type"],
      near=[("m1", "D:reaction_count", "F0", "two rockets"), ("m2", "D:reaction_count", "F0", "one rocket")]),
]


def main():
    OUT.write_text(json.dumps(REVIEW, indent=1) + "\n")
    valid = [r for r in REVIEW if r["valid"]]
    print(json.dumps({
        "tests": len(REVIEW), "forms": Counter(r["form"] for r in REVIEW),
        "near_miss_families": Counter(n["family"] for r in REVIEW for n in r["near_misses"]),
        "tests_with_proper_credit_valid": sum(1 for r in valid if r["proper"]),
        "facts_exercised": len({f for r in REVIEW for f in r["facts_exercised"] if not f.startswith("(")}),
        "facts_exercised_properly_valid": sorted({f for r in valid for f in r["proper"]}),
        "oracle_unsound": [r["test"] for r in REVIEW if not r["oracle_sound"]],
        "invalid": [r["test"] for r in REVIEW if not r["valid"]]}, indent=1))


if __name__ == "__main__":
    main()
