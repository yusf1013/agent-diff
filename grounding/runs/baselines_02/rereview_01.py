"""My re-review of the cross-check draw `runs/rereview_01` (5 N0M, 5 N1M and 5 N1 tests of baselines_01, under ids
X01...), by the same rules and helpers as my pool review (`review_pool_01.py`), written before `compare` read the
manifest or the other session's review.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.baselines_02.rereview_01   # writes the JSON
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from grounding.runs.baselines_02.review_pool_01 import ins, r, upd

HERE = Path(__file__).resolve().parent
OUT = HERE / "runs" / "rereview_01" / "review.json"
DELETE = {"table": "messages", "key": ["message_id"], "changes": ["delete", "update"]}

REVIEW = [
    r("X01", "present", ["A:Folder.name", "R:Folder.owned_by_id"],
      target=["8500"], table="box_folders", effect=upd("box_folders"),
      near=[("8501", "R:Folder.owned_by_id", "F8", "the Contracts folder Maya Lopez owns")],
      proper=["R:Folder.owned_by_id"]),
    r("X02", "present", ["A:File.name", "A:File.shared_link"],
      target=["8202"], table="box_files", effect=ins("box_comments", "file_id"),
      near=[("8201", "A:File.shared_link", "F0", "the other Launch Plan.pdf, no shared link")]),
    r("X03", "absence_presupposed", ["D:latest_message", "A:Conversation.channel_name"],
      table="messages", effect=DELETE,
      note="#empty has no message at all: no competitor"),
    r("X04", "present", ["A:File.name", "R:Comment.created_by_id", "A:Comment.message", "B:Comment.file_id"],
      target=["8810"], table="box_files", effect=ins("box_tasks", "item_id"),
      near=[("8820", "B:Comment.file_id", "F5",
             "the Launch Brief in Briefs Archive: Maya Chen wrote 'Needs more data', Omar 'Approved for launch'")],
      proper=["B:Comment.file_id"]),
    r("X05", "absence_presupposed", ["A:Message.message_text", "A:Conversation.channel_name"],
      table="messages", effect=DELETE,
      near=[("1789992180.000001", "A:Message.message_text", "F0", "Priya's 'rocket launch at dusk is a go'")]),
    r("X06", "present", ["A:Issue.title", "A:WorkflowState.name"],
      target=["i-l2"], table="issues", effect=upd("issues"),
      near=[("i-l1", "A:WorkflowState.name", "F0", "the same title in Todo")]),
    r("X07", "present", ["A:Calendar.summary", "A:Calendar.data_owner", "A:CalendarListEntry.access_role"],
      target=["cal-a@northwind.example"], table="calendars", effect=upd("calendars"),
      near=[("cal-c@northwind.example", "A:CalendarListEntry.access_role", "F7", "Kenji's, but Jordan only reads it"),
            ("cal-b@northwind.example", "A:Calendar.data_owner", "F0", "Jordan's own Budget review calendar")],
      oracle_ok=False, oracle_note="expects the calendar row removed; the replica marks a deleted calendar `deleted`",
      flaws=[("a", "only a calendar's owner can delete it (Google Calendar; the replica's `calendars_delete` checks "
                   "the owner too): Jordan, a writer, cannot delete Kenji's calendar, so the expected deletion is "
                   "impossible")]),
    r("X08", "present", ["A:File.name", "A:Comment.message", "R:Comment.file_id"],
      target=["8601"], table="box_files", effect=ins("box_tasks", "item_id"),
      near=[("8602", "A:Comment.message", "F0",
             "the other Project Notes: the legal review comment, but 'Timeline shifted' instead of the budget one")]),
    r("X09", "present", ["A:Event.summary", "A:Event.organizer_email"],
      target=["ev_b"], table="calendar_events", effect=upd("calendar_events"),
      near=[("ev_a", "A:Event.organizer_email", "F0", "the Design sync Priya organizes")]),
    r("X10", "present", ["A:Event.summary", "A:Event.location", "A:Event.start"],
      target=["ev_roomb"], table="calendar_events", effect=upd("calendar_events"),
      near=[("ev_rooma", "A:Event.location", "F0", "the Sprint demo in Room A at the same time")],
      oracle_ok=False, oracle_note="expects the event row removed; the replica cancels a deleted event (an update), "
                                   "so a right outcome fails; `unchanged` is not an assertion type the engine takes"),
    r("X11", "absence_presupposed", ["A:Issue.title"],
      table="issues", effect=upd("issues"),
      near=[("i-f1", "A:Issue.title", "F8", "Dark mode for settings page"),
            ("i-f2", "A:Issue.title", "F8", "Dark mode for billing page")]),
    r("X12", "absence_presupposed", ["A:Event.summary", "A:Event.start", "A:EventAttendee.email"],
      table="calendar_events", effect=upd("calendar_events"),
      near=[("ev-b", "A:EventAttendee.email", "F0", "the Budget sync on June 22 with Sam")],
      far=["ev-a: June 20, with Priya"]),
    r("X13", "present", ["A:File.name", "A:Task.message", "R:Task.item_id"],
      target=["8802"], table="box_files", effect=ins("box_comments", "file_id"),
      near=[("8801", "A:Task.message", "F0", "the other Migration Plan, whose task is about the architecture diagram")]),
    r("X14", "present", ["R:Comment.created_by_id", "H:Comment.item_id:comment", "A:File.name"],
      target=["8912"], table="box_comments", effect=ins("box_comments", "item_id"),
      near=[("8913", "H:Comment.item_id:comment", "F4", "Omar's identical top-level comment")],
      far=["8911: Maya's review comment itself (the thread's root)"],
      proper=["H:Comment.item_id:comment"],
      quality=["a reply placed in Maya's thread (on 8911) would read as closing the thread too; the request names "
               "Omar's reply, which the replica accepts as a reply's parent"]),
    r("X15", "present", ["D:dm_with"],
      target=["D_H2"], table="channels", effect=ins("messages", "channel_id", key=("message_id",)),
      near=[("D_H1", "D:dm_with", "F0", "the DM with Diego")]),
]


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(REVIEW, indent=1, ensure_ascii=False) + "\n")
    print(json.dumps({"reviewed": len(REVIEW), "valid": sum(x["valid"] for x in REVIEW),
                      "forms": Counter(x["form"] for x in REVIEW)}))


if __name__ == "__main__":
    main()
