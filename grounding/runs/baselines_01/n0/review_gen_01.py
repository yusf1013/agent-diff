"""My hand review of N0's 48 tests (run gen_01), written 2026-09-28 before any agent ran them, by review_rules.md.

    python3 grounding/runs/baselines_01/n0/review_gen_01.py     # writes runs/gen_01/review.json and prints totals

Per test: its form; the catalog facts its conditions rest on; its near misses (one condition failed) with fact and
family; far competitors; the facts it exercises properly (a near miss of family F1 to F8 in a fact-sensitive form);
validity with a cause per flaw; whether its own assertions check what `expected` says.

Families are judged as for our writer's decoys (autogen_01/kit/docs/method.md): F8 when the competitor's name or
identifier shares part of the requested value; F7 for the nearest value on the wrong side of an ordered condition;
F0 for simply another value.

Checks of the replica behind some verdicts (read in the code, not run):
- Slack `chat.delete` refuses to delete another user's message (`cant_delete_message`), as Slack does for a
  non-admin; the acting bot authors no seeded message.
- Slack reads never show `user_mentions`, and the seed builder does not write the mention into the text.
- Box `DELETE /files/{id}` moves the file to the trash (an update, `item_status` "trashed"), as Box does; the row is
  not removed.
- Calendar `events.list` leaves out cancelled events unless `showDeleted` is set.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "runs" / "gen_01" / "review.json"


def t(test, form, facts, near=(), far=(), proper=(), flaws=(), quality=(), oracle_ok=True, oracle_note=""):
    return {"test": test, "form": form, "facts_exercised": list(facts),
            "near_misses": [dict(zip(("record", "fact", "family", "note"), n)) for n in near],
            "far": list(far), "proper": list(proper),
            "valid": not flaws, "flaws": [dict(zip(("cause", "note"), f)) for f in flaws],
            "quality": list(quality), "oracle_sound": oracle_ok, "oracle_note": oracle_note}


REVIEW = [
    # ------------------------------------------------------------------ Box
    t("N0-BOX-T01", "present", ["A:File.name", "R:File.parent_id", "A:Folder.name"],
      near=[("8111", "R:File.parent_id", "F0", "same file name in another folder (Templates)")]),
    t("N0-BOX-T02", "present", ["A:File.name", "A:File.description"],
      near=[("8211", "A:File.description", "F0", "same name, description 'marketing draft'")],
      quality=["the request names the competitor to avoid: '(not the marketing draft)'"]),
    t("N0-BOX-T03", "absence_presupposed", ["A:File.name", "R:File.parent_id", "A:Folder.name"],
      near=[("8310", "A:File.name", "F0", "Acme MSA.pdf for Globex MSA.pdf")]),
    t("N0-BOX-T04", "present", ["A:Folder.name", "A:Folder.description"],
      near=[("8401", "A:Folder.description", "F0", "same name, description 'marketing assets'")]),
    t("N0-BOX-T05", "present", ["R:File.owned_by_id", "A:User.name", "A:File.name", "A:File.extension"],
      near=[("8511", "R:File.owned_by_id", "F8",
             "owned by Maya Lopez for Maya Chen: the default people of seed_ops.md hold this pair")],
      proper=["R:File.owned_by_id"]),
    t("N0-BOX-T06", "present", ["R:Comment.created_by_id", "A:Comment.message", "R:Comment.file_id", "A:File.name"],
      far=["8611: Priya's comment fails the author and the topic"]),
    t("N0-BOX-T07", "present", ["A:Hub.title", "A:Hub.description", "A:File.name"],
      near=[("8721", "A:Hub.description", "F0", "same hub title, description '2024 pilot'")]),
    t("N0-BOX-T08", "present", ["A:File.name", "A:File.description"],
      near=[("8811", "A:File.description", "F0", "same name, description 'superseded 2023'")]),
    t("N0-BOX-T09", "present", ["A:Folder.name", "A:Folder.description", "A:File.name"],
      near=[("8901", "A:Folder.description", "F0", "same folder name, description 'receivable, sales-owned'")],
      quality=["'(finance-owned)' can be read as the owner; both folders are owned by the actor, and only the "
               "description says finance"]),
    t("N0-BOX-T10", "set", ["A:File.tags"],
      near=[("9012", "A:File.tags", "F0", "tagged 'social'")]),
    t("N0-BOX-T11", "present", ["A:File.name", "A:File.extension"],
      near=[("9110", "A:File.extension", "F0", "the PDF of the same name")],
      quality=["the request names the file exactly and says to keep the PDF"],
      oracle_ok=False, oracle_note="expects the file row removed; Box trashes a deleted file (an update), so the "
                                   "assertion fails a correct deletion"),
    t("N0-BOX-T12", "absence_presupposed", ["A:File.name", "A:File.tags"],
      near=[("9210", "A:File.tags", "F0", "tagged draft"), ("9211", "A:File.tags", "F0", "tagged reviewed")]),
    # ------------------------------------------------------------------ Calendar
    t("N0-CAL-T01", "present", ["A:Event.summary", "A:EventAttendee.email", "A:Event.start"],
      near=[("ev_lunch1", "A:Event.start", "F0", "the same lunch three days earlier")]),
    t("N0-CAL-T02", "present", ["A:Event.summary", "A:Event.start"],
      near=[("ev_sync_m", "A:Event.start", "F0", "the same 1:1 in the morning")]),
    t("N0-CAL-T03", "present", ["A:Event.summary", "A:Event.location"],
      near=[("ev_board_a", "A:Event.location", "F0", "Room A for Room B")]),
    t("N0-CAL-T04", "present", ["A:Event.summary", "A:EventAttendee.email"],
      near=[("ev_kick_o", "A:EventAttendee.email", "F0", "Omar attends instead of Maya")]),
    t("N0-CAL-T05", "present", ["A:Event.summary", "A:Event.organizer_email"],
      near=[("ev_des_p", "A:Event.organizer_email", "F0", "organized by Priya instead of Omar")]),
    t("N0-CAL-T06", "present", ["A:Event.summary", "R:Event.calendar_id", "A:Calendar.summary"],
      near=[("ev_sp_p", "R:Event.calendar_id", "F0", "the same event on the primary calendar")]),
    t("N0-CAL-T07", "present", ["A:Event.summary"],
      near=[("ev_dr_f", "A:Event.summary", "F8", "'Design review follow-up' contains 'Design review'")],
      proper=["A:Event.summary"]),
    t("N0-CAL-T08", "present", ["A:Event.summary", "A:Event.start", "A:Event.status"],
      near=[("ev_dent_c", "A:Event.status", "F0", "the cancelled copy; the condition is implicit")],
      quality=["events.list hides cancelled events by default, so the competitor is usually invisible"]),
    t("N0-CAL-T09", "present", ["A:Calendar.summary", "A:AclRule.role", "A:AclRule.scope_value"],
      near=[("engarch@northwind.example", "A:Calendar.summary", "F8", "'Engineering archive' contains 'Engineering'")],
      proper=["A:Calendar.summary"],
      oracle_note="checks the role and the calendar, not that the rule is for Omar"),
    t("N0-CAL-T10", "set", ["A:Event.summary"],
      near=[("ev_fe", "A:Event.summary", "F0", "'Frontend interview' for 'Backend interview'")]),
    t("N0-CAL-T11", "absence_presupposed", ["A:Event.summary", "A:EventAttendee.email", "A:Event.start"],
      near=[("ev_din", "A:Event.start", "F0", "the same dinner a week earlier")]),
    t("N0-CAL-T12", "absence_presupposed", ["A:Event.summary", "R:Event.calendar_id", "A:Calendar.summary"],
      near=[("ev_sp", "R:Event.calendar_id", "F0", "the event on Engineering; the named Sales calendar does not "
                                                     "exist")]),
    # ------------------------------------------------------------------ Linear
    t("N0-LIN-T01", "present", ["A:Issue.title"],
      near=[("i-search", "A:Issue.title", "F0", "an unrelated issue (one-condition request)"),
            ("d-checkout", "(outside the catalog: record type)", "F0", "a document with the same title")]),
    t("N0-LIN-T02", "present", ["A:Issue.title", "R:Issue.teamId", "A:Team.name"],
      near=[("i-mob-push", "R:Issue.teamId", "F0", "the same issue title in the Mobile team")]),
    t("N0-LIN-T03", "present", ["A:Issue.title", "R:Issue.assigneeId", "A:User.name"],
      near=[("i-login-leo", "R:Issue.assigneeId", "F0", "the same title assigned to Leo")]),
    t("N0-LIN-T04", "present", ["A:Issue.title", "R:issue_label_issue_association", "A:IssueLabel.name"],
      near=[("i-exp-feat", "R:issue_label_issue_association", "F0", "the same title labelled Feature")]),
    t("N0-LIN-T05", "present", ["A:Issue.identifier"],
      near=[("i-a1", "A:Issue.identifier", "F8", "API-1 for API-2"), ("i-a3", "A:Issue.identifier", "F8",
                                                                    "API-3 for API-2")],
      proper=["A:Issue.identifier"],
      quality=["a lookup by exact identifier"]),
    t("N0-LIN-T06", "absence_presupposed", ["A:Issue.title"],
      near=[("i-dark", "A:Issue.title", "F0", "unrelated issue (one-condition request)"),
            ("i-slow", "A:Issue.title", "F0", "unrelated issue (one-condition request)")]),
    t("N0-LIN-T07", "present", ["A:Issue.title", "R:Comment.issueId", "R:Comment.userId", "A:Comment.body"],
      far=["c-leo: Leo's comment fails the author and the text"]),
    t("N0-LIN-T08", "present", ["A:IssueLabel.name", "R:IssueLabel.teamId", "A:Team.name"],
      near=[("lb-api", "R:IssueLabel.teamId", "F0", "a Bug label of the API team")]),
    t("N0-LIN-T09", "present", ["A:Issue.title", "R:Issue.cycleId", "A:Cycle.number"],
      near=[("c4", "A:Cycle.number", "F0", "Cycle 4, the issue's current cycle, for Cycle 5 (input reference)")],
      quality=["the issue itself has no competitor"]),
    t("N0-LIN-T10", "present", ["A:Issue.title", "R:Issue.projectId", "A:Project.name"],
      near=[("p-web", "A:Project.name", "F8", "'Mobile Web' for 'Mobile App' (input reference; shares a word)")],
      far=["i-badge: another issue, another title"],
      proper=["A:Project.name"]),
    t("N0-LIN-T11", "present", ["A:Team.name", "R:TeamMembership", "A:User.name"],
      near=[("t-and", "A:Team.name", "F0", "Android for iOS")]),
    t("N0-LIN-T12", "absence_presupposed", ["A:Issue.title", "R:Issue.assigneeId", "A:User.name"],
      near=[("i-c1", "R:Issue.assigneeId", "F0", "checkout issue assigned to Maya"),
            ("i-c2", "R:Issue.assigneeId", "F0", "checkout issue assigned to Leo"),
            ("i-r1", "A:Issue.title", "F0", "Omar's issue is about refunds")]),
    # ------------------------------------------------------------------ Slack
    t("N0-SLK-T01", "present", ["A:Conversation.channel_name"],
      near=[("C_LPS", "A:Conversation.channel_name", "F8", "#launch-plans contains 'launch-plan'")],
      proper=["A:Conversation.channel_name"]),
    t("N0-SLK-T02", "present", ["A:Conversation.channel_name", "A:Conversation.topic_text"],
      far=["C_PAB: #project-atlas-web fails the exact name and the topic (its name contains the requested one)"]),
    t("N0-SLK-T03", "absence_presupposed", ["A:Conversation.channel_name"],
      far=["C_TEAM: #team-ops, unrelated"]),
    t("N0-SLK-T04", "present", ["A:User.real_name", "R:channel_members", "A:Conversation.channel_name"],
      near=[("U_MAYAR", "A:User.real_name", "F8", "Maya Rossi for Maya Chen")],
      proper=["A:User.real_name"],
      oracle_note="counts any one new member, and only rules out Maya Rossi"),
    t("N0-SLK-T05", "present", ["R:messages.user_id", "A:Message.message_text", "R:messages.channel_id"],
      near=[("leomsg", "R:messages.user_id", "F0", "Leo's identical message")],
      flaws=[("a", "the bot cannot delete another user's message (cant_delete_message, as in Slack); the "
                   "expected deletion is impossible")]),
    t("N0-SLK-T06", "present", ["R:messages.user_id", "A:Message.message_text", "R:messages.channel_id"],
      near=[("diammsg", "R:messages.user_id", "F0", "Diego's identical message")],
      oracle_ok=False, oracle_note="requires white_check_mark; 'a check mark reaction' also fits "
                                   "heavy_check_mark or ballot_box_with_check"),
    t("N0-SLK-T07", "present", ["R:messages.user_id", "D:latest_message", "A:Message.message_text",
                                "R:messages.channel_id"],
      near=[("oldupdate", "D:latest_message", "F7", "Leo's previous standup message")],
      proper=["D:latest_message"],
      flaws=[("a", "the bot cannot delete another user's message (cant_delete_message, as in Slack)")]),
    t("N0-SLK-T08", "present", ["A:Message.message_text", "H:messages.parent_id", "R:messages.channel_id"],
      near=[("other", "A:Message.message_text", "F0", "an unrelated message in the channel")]),
    t("N0-SLK-T09", "absence_presupposed", ["A:Message.message_text", "R:messages.channel_id"],
      far=["lunch, holiday: unrelated messages"]),
    t("N0-SLK-T10", "absence_presupposed", ["A:User.real_name", "R:channel_members"],
      far=["no person resembles Sam Rivera"]),
    t("N0-SLK-T11", "set", ["A:Message.message_text", "R:messages.channel_id"],
      near=[("lunch", "A:Message.message_text", "F0", "the lunch poll")]),
    t("N0-SLK-T12", "present", ["A:Message.message_text", "(outside the catalog: mentions)", "R:messages.channel_id"],
      near=[("notea", "(outside the catalog: mentions)", "F0", "the identical draft without the mention")],
      flaws=[("f", "the mention exists only in user_mentions; the text shows none and no read returns it, so "
                   "the two drafts look identical")]),
]


def main():
    OUT.write_text(json.dumps(REVIEW, indent=1) + "\n")
    forms = Counter(r["form"] for r in REVIEW)
    fams = Counter(n["family"] for r in REVIEW for n in r["near_misses"])
    proper = sorted({f for r in REVIEW for f in r["proper"]})
    exercised = sorted({f for r in REVIEW for f in r["facts_exercised"] if not f.startswith("(")})
    flawed = [r["test"] for r in REVIEW if not r["valid"]]
    print(json.dumps({"tests": len(REVIEW), "forms": forms, "near_miss_families": fams,
                      "tests_with_a_near_miss": sum(1 for r in REVIEW if r["near_misses"]),
                      "tests_with_proper_credit": sum(1 for r in REVIEW if r["proper"]),
                      "facts_exercised": len(exercised), "facts_exercised_properly": len(proper),
                      "proper": proper, "invalid": flawed,
                      "oracle_unsound": [r["test"] for r in REVIEW if not r["oracle_sound"]]}, indent=1))


if __name__ == "__main__":
    main()
