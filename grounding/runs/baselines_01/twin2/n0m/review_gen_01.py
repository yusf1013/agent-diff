"""My hand review of N0M's tests (N0 plus the PI's added lines, run gen_01), written 2026-09-28 before any agent ran
them, by n0/review_rules.md. Same record shape and family judgments as n0/review_gen_01.py.

    python3 grounding/runs/baselines_01/twin2/n0m/review_gen_01.py     # writes runs/gen_01/review.json, prints totals

Known replica behaviour applied here (read in round 1, see n0/review_gen_01.py): deleting a Calendar event cancels it
(`status` "cancelled", an update, hidden from `events.list` unless `showDeleted`); deleting a Box file or folder
moves it to the trash (an update); Slack's `chat.delete` refuses another user's message; Slack reads never show
`user_mentions`. Round 1's review of N1 did not yet flag the Calendar deletes it met; here every assertion that
expects such a row to be removed is marked unsound.

**Not comparable across rounds:** the `oracle_sound` counts. The same `removed` assertion was left sound in round
1's N1-CAL-T01, T03, T04 and T11 and is marked unsound here. The scored measure (each test's assertions against my
labels) is unaffected.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from grounding.runs.baselines_01.n0.review_gen_01 import t  # same record shape

HERE = Path(__file__).resolve().parent
OUT = HERE / "runs" / "gen_01" / "review.json"
CANCEL = "expects the event row removed; the replica cancels a deleted event (an update), so a right outcome fails"
BOT_DELETE = ("a", "the bot cannot delete another user's message (cant_delete_message, as in Slack); the expected "
                   "deletion is impossible")
BOT_UPDATE = ("a", "the bot cannot edit another user's message (cant_update_message, as in Slack); the expected edit "
                   "is impossible")
BOT_UNREACT = ("a", "reactions.remove removes only the caller's own reaction (no_reaction, as in Slack); the bot "
                    "cannot remove Priya's")
NO_CHECK_MARK = ("b", "the replica's reaction list has no white_check_mark, which Slack has; the expected reactions "
                      "are impossible here (counted apart)")

REVIEW = [
    # ------------------------------------------------------------------ Box (loaded after the fourth round, log)
    t("N0M-BOX-T01", "present", ["A:File.name", "R:File.parent_id", "A:Folder.name"],
      near=[("8111", "R:File.parent_id", "F0", "the same file in the Finance folder")]),
    t("N0M-BOX-T02", "present", ["A:File.name", "A:File.extension", "R:File.owned_by_id", "A:User.name"],
      near=[("8201", "R:File.owned_by_id", "F8", "owned by Maya Chen for Maya Lopez")],
      proper=["R:File.owned_by_id"]),
    t("N0M-BOX-T03", "present", ["A:File.description"],
      near=[("8310", "A:File.description", "F1", "'Q3 Roadmap.pdf' is named for the topic; its description is not")],
      proper=["A:File.description"]),
    t("N0M-BOX-T04", "present", ["A:File.name", "A:File.tags"],
      near=[("8401", "A:File.tags", "F0", "the same checklist tagged draft")]),
    t("N0M-BOX-T05", "present", ["A:File.name", "A:File.modified_at"],
      near=[("8501", "A:File.modified_at", "F7", "the previous version (March) for the most recent (June)")],
      proper=["A:File.modified_at"]),
    t("N0M-BOX-T06", "present", ["A:File.name", "A:File.extension"],
      near=[("8601", "A:File.extension", "F0", "Budget.pdf for the spreadsheet")],
      quality=["the request names the competitor to avoid: 'not the PDF'"]),
    t("N0M-BOX-T07", "present", ["A:File.name", "R:Comment.file_id", "R:Comment.created_by_id", "A:Comment.message",
                                 "B:Comment.file_id"],
      far=["8701: its only comment is Dana's, and about something else"]),
    t("N0M-BOX-T08", "present", ["A:File.name", "R:Task.item_id", "A:Task.message"],
      near=[("8801", "A:Task.message", "F0", "its task is about the architecture diagram")]),
    t("N0M-BOX-T09", "present", ["A:File.name", "R:HubItem.file", "A:Hub.title"],
      near=[("8901", "R:HubItem.file", "F0", "the same checklist, not in the hub")]),
    t("N0M-BOX-T10", "present", ["A:File.name", "R:File.collections"],
      near=[("8951", "R:File.collections", "F0", "the same itinerary, not in Favorites")]),
    t("N0M-BOX-T11", "absence_presupposed", ["A:File.name"],
      near=[("9001", "A:File.name", "F8", "Q1 Report for Q4 Report"),
            ("9002", "A:File.name", "F8", "Q2 Report for Q4 Report")]),
    t("N0M-BOX-T12", "set", ["A:File.tags"],
      near=[("9103", "A:File.tags", "F0", "the invoice tagged paid")],
      quality=["the request gives the count: '(both of them)'"]),
    # ------------------------------------------------------------------ Calendar
    t("N0M-CAL-T01", "present", ["A:Event.summary", "A:Event.start"],
      near=[("ev_b", "A:Event.start", "F0", "the same meeting a week later")],
      oracle_ok=False, oracle_note=CANCEL),
    t("N0M-CAL-T02", "present", ["A:Event.summary", "A:EventAttendee.email", "A:Event.start"],
      near=[("ev_a", "A:EventAttendee.email", "F0", "Priya attends instead of Maya")],
      oracle_ok=False, oracle_note=CANCEL),
    t("N0M-CAL-T03", "present", ["A:Event.summary", "A:Event.organizer_email"],
      near=[("ev_a", "A:Event.organizer_email", "F0", "organized by Priya instead of Omar")]),
    t("N0M-CAL-T04", "present", ["A:Event.summary", "R:Event.calendar_id", "A:Calendar.summary"],
      near=[("ev_a", "R:Event.calendar_id", "F0", "the same event on the Product calendar")],
      oracle_ok=False, oracle_note=CANCEL),
    t("N0M-CAL-T05", "present", ["A:Event.summary", "A:Event.location"],
      near=[("ev_a", "A:Event.location", "F0", "Room A for Room B")]),
    t("N0M-CAL-T06", "present", ["A:Event.summary", "A:Event.start"],
      near=[("ev_b", "A:Event.start", "F0", "the same 1:1 in the afternoon")],
      oracle_ok=False, oracle_note=CANCEL),
    t("N0M-CAL-T07", "present", ["A:Event.summary", "A:Event.start", "A:Event.status"],
      near=[("ev_b", "A:Event.status", "F0", "the cancelled copy; the condition is implicit")],
      quality=["events.list hides cancelled events by default, so the competitor is usually invisible"]),
    t("N0M-CAL-T08", "present", ["A:Event.summary", "(outside the catalog: recurrence)"],
      near=[("ev_b", "(outside the catalog: recurrence)", "F0",
             "a one-off event with the series' title, at its first occurrence's time")]),
    t("N0M-CAL-T09", "absence_presupposed", ["A:Event.summary", "A:EventAttendee.email", "A:Event.start"],
      near=[("ev_a", "A:EventAttendee.email", "F0", "the budget review is with Maya"),
            ("ev_b", "A:Event.summary", "F0", "Leo's meeting is a Roadmap review")]),
    t("N0M-CAL-T10", "present", ["A:Event.summary", "A:Event.start"],
      near=[("ev_b", "A:Event.summary", "F8", "'Design review: Checkout follow-up' contains the requested title")],
      proper=["A:Event.summary"], quality=["the request names the competitor to avoid: 'not the follow-up'"],
      oracle_ok=False, oracle_note=CANCEL),
    t("N0M-CAL-T11", "present", ["A:Event.summary", "D:all_day", "A:Event.start"],
      near=[("ev_b", "D:all_day", "F6", "a timed Offsite on the same day for the all-day one")],
      proper=["D:all_day"], oracle_ok=False, oracle_note=CANCEL),
    t("N0M-CAL-T12", "set", ["A:Event.summary", "A:EventAttendee.email"],
      near=[("ev_c", "A:EventAttendee.email", "F0", "the portfolio review with Priya")],
      oracle_ok=False, oracle_note=CANCEL),
    # ------------------------------------------------------------------ Linear
    t("N0M-LIN-T01", "present", ["A:Issue.title", "R:Issue.teamId", "A:Team.name"],
      near=[("i-j1", "R:Issue.teamId", "F0", "the same title in the Web team")]),
    t("N0M-LIN-T02", "present", ["A:Issue.title", "R:Issue.assigneeId", "A:User.name"],
      near=[("i-a1", "R:Issue.assigneeId", "F0", "the same title assigned to Maya")]),
    t("N0M-LIN-T03", "present", ["A:Issue.title", "R:issue_label_issue_association", "A:IssueLabel.name"],
      near=[("i-b2", "R:issue_label_issue_association", "F0", "the same title labelled SSO")]),
    t("N0M-LIN-T04", "present", ["A:Issue.title", "H:Issue.parentId"],
      near=[("i-c3", "H:Issue.parentId", "F0", "the same title as a standalone issue (not a level)")],
      far=["i-c1: the parent issue itself, without 'hero copy'"]),
    t("N0M-LIN-T05", "present", ["A:Issue.title", "R:Issue.cycleId", "D:current_cycle"],
      near=[("i-d2", "D:current_cycle", "F7", "the same title in the previous (past) cycle")],
      proper=["D:current_cycle"],
      quality=["the active cycle's dates (September 1 to 14) are before the run date; Linear runs on the real "
               "clock, so an agent computing by date finds no current cycle, and none picks the past one"]),
    t("N0M-LIN-T06", "present", ["A:Issue.title", "R:Issue.projectId", "A:Project.name"],
      near=[("i-e1", "R:Issue.projectId", "F0", "the same title in project Atlas")]),
    t("N0M-LIN-T07", "absence_presupposed", ["A:Issue.title"],
      near=[("i-f1", "A:Issue.title", "F8", "'Dark mode for settings page' shares most of the title"),
            ("i-f2", "A:Issue.title", "F8", "'Dark mode for billing page' shares most of the title")]),
    t("N0M-LIN-T08", "set", ["R:issue_label_issue_association", "A:IssueLabel.name"],
      near=[("i-g3", "R:issue_label_issue_association", "F0",
             "'Login error C' is unlabelled; every issue has Login in its title, so the title lures toward none")]),
    t("N0M-LIN-T09", "present", ["A:Issue.title"],
      near=[("i-h2", "A:Issue.title", "F8", "'Token refresh fails on mobile clients' contains the requested title")],
      proper=["A:Issue.title"]),
    t("N0M-LIN-T10", "present", ["A:Issue.title", "A:Issue.dueDate"],
      near=[("i-i2", "A:Issue.dueDate", "F0", "the same title due November 20")]),
    t("N0M-LIN-T11", "present", ["A:Issue.title", "R:Comment.issueId", "A:Comment.body"],
      near=[("c-k1", "A:Comment.body", "F0", "Maya's comment about facets")],
      quality=["the comment to edit is Priya's; the replica lets anyone edit a comment"]),
    t("N0M-LIN-T12", "present", ["A:Issue.title", "R:Issue.stateId", "A:WorkflowState.name"],
      near=[("i-l1", "R:Issue.stateId", "F0", "the same title in Todo")]),
    # ------------------------------------------------------------------ Slack
    t("N0M-SLK-T01", "present", ["A:Conversation.channel_name"],
      near=[("C_T01A", "A:Conversation.channel_name", "F8", "#riverbank contains 'river'")],
      proper=["A:Conversation.channel_name"]),
    t("N0M-SLK-T02", "present", ["A:User.real_name", "R:channel_members", "A:Conversation.channel_name"],
      near=[("tx2", "A:User.real_name", "F8", "Tara Novak for Tara Reyes")],
      proper=["A:User.real_name"]),
    t("N0M-SLK-T03", "present", ["R:messages.user_id", "A:Message.message_text", "R:messages.channel_id"],
      near=[("s2", "R:messages.user_id", "F0", "Leo's identical message"),
            ("s3", "R:messages.channel_id", "F0", "Diego's identical message in #lagoon")],
      flaws=[BOT_DELETE]),
    t("N0M-SLK-T04", "present", ["R:messages.user_id", "A:Message.message_text", "A:Message.created_at",
                                 "R:messages.channel_id"],
      near=[("d2", "A:Message.created_at", "F7", "Leo's identical message of the next day")],
      proper=["A:Message.created_at"]),
    t("N0M-SLK-T05", "present", ["R:messages.user_id", "A:Message.message_text", "H:messages.parent_id",
                                 "R:messages.channel_id"],
      near=[("e2", "A:Message.message_text", "F0", "Leo's other reply in the thread")],
      far=["e0: the thread's root, Diego's, with other text"], flaws=[BOT_UPDATE]),
    t("N0M-SLK-T06", "present", ["R:message_reactions", "A:Reaction.reaction_type", "A:Message.message_text",
                                 "R:messages.channel_id"],
      near=[("thumbsup", "A:Reaction.reaction_type", "F0", "Priya's thumbsup on the same message")],
      flaws=[BOT_UNREACT]),
    t("N0M-SLK-T07", "set", ["R:messages.user_id", "A:Message.message_text", "R:messages.channel_id"],
      near=[("g4", "R:messages.user_id", "F0", "Leo's 'invoice ready' message"),
            ("g5", "A:Message.message_text", "F0", "Omar's 'invoice draft' message")],
      flaws=[NO_CHECK_MARK]),
    t("N0M-SLK-T08", "present", ["R:messages.user_id", "A:Message.message_text", "R:messages.channel_id"],
      near=[("h1", "R:messages.user_id", "F0", "Diego's identical message")],
      quality=["the request names the competitor to avoid: 'NOT by Diego'"], flaws=[BOT_DELETE]),
    t("N0M-SLK-T09", "absence_presupposed", ["A:Message.message_text", "R:messages.channel_id"],
      near=[("n1", "A:Message.message_text", "F0", "'rocket launch at dusk is a go'")],
      quality=["the bot cannot delete Priya's message, so a wrong deletion cannot land in the diff"]),
    t("N0M-SLK-T10", "present", ["R:messages.user_id", "A:Message.message_text", "D:latest_message",
                                 "R:messages.channel_id"],
      near=[("j2", "D:latest_message", "F7", "Aisha's previous identical message"),
            ("j1", "D:latest_message", "F0", "Aisha's earliest identical message")],
      proper=["D:latest_message"], flaws=[BOT_DELETE]),
    t("N0M-SLK-T11", "present", ["A:Conversation.topic_text"],
      near=[("C_T11A", "A:Conversation.topic_text", "F1", "#aurora is named for the topic; its topic is sunset photos")],
      proper=["A:Conversation.topic_text"]),
    t("N0M-SLK-T12", "present", ["R:messages.user_id", "A:Message.message_text", "R:messages.channel_id"],
      near=[("k1", "R:messages.user_id", "F1", "Diego's message names and mentions Leo")],
      proper=["R:messages.user_id"], quality=["the request spells out the trap: 'the one he wrote himself'"]),
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
