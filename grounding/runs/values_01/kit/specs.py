"""The requested value of every written field, per scenario: written by hand from each request's wording (manual
work, 2026-09-30). The cases carry no structured requested value; their references name the written fields only.

A scenario's policy units and probes keep its parent's value phrase (checked over the 395 distinct requests), so one
specification per scenario covers all its executions.

Kinds (the comparator each field needs):
- `tag_add`: Box tags. The requested tag is added; existing tags stay; nothing else is added.
- `priority`: Linear priority by name. Linear's scale (and the replica's `priorityLabel`): 0 No priority, 1 Urgent,
  2 High, 3 Medium, 4 Low.
- `number`: an exact number (Linear estimate).
- `reaction`: a Slack reaction name. `accept` lists the names the request can mean *among the names the replica
  accepts* (`COMMON_REACTIONS` in the Slack replica: it has `thumbsup` and `+1`, and `check` as its only check mark).
- `bool`, `null`: a state (archived, hidden) or cleared fields (a reopened thread).
- `date`: a calendar date without a year in the request. `year` is the year the seed's world implies; a write in
  another year is kept apart (the run date can suggest the next occurrence).
- `text`: a quoted or literal replacement text, compared exactly, then after normalization.
- `append`: text added to existing text (the old text must stay; `position: end` where the request says "at the
  end").
- `semantic`: a paraphrasable instruction ("to say that ..."); keywords are checked mechanically, fidelity needs a
  reader.
- `enum`: a value from a fixed set (`accept`), with `near` for values a reader might defend.
- `ref_input`: a record named by the request as the value (the case's `input` reference holds its ids).
- `ref_name`: a record named by the request as the value, looked up by name in the case's seed.
"""
from __future__ import annotations

T = "tag_add"


def tag(table: str, value: str, phrase: str) -> dict:
    return {"field": f"{table}.tags", "kind": T, "value": value, "phrase": phrase}


def prio(value: str, phrase: str) -> dict:
    return {"field": "issues.priority", "kind": "priority", "value": value, "phrase": phrase}


def est(value: float, phrase: str) -> dict:
    return {"field": "issues.estimate", "kind": "number", "value": float(value), "phrase": phrase}


def react(value: str, phrase: str, accept=None) -> dict:
    return {"field": "message_reactions.reaction_type", "kind": "reaction", "value": value,
            "accept": accept or [value], "phrase": phrase}


def loc(value: str, phrase: str) -> dict:
    return {"field": "calendar_events.location", "kind": "text", "value": value, "phrase": phrase}


HIDE = {"field": "calendar_list_entries.hidden", "kind": "bool", "value": True, "phrase": "hide"}
ARCHIVE = {"field": "channels.is_archived", "kind": "bool", "value": True, "phrase": "Archive"}

SPECS: dict[str, list[dict]] = {
    # Box
    "AP-BOX-01": [tag("box_folders", "ready-for-review", "Add the tag ready-for-review")],
    "AP-BOX-02": [tag("box_files", "needs-legal-review", "Add the tag needs-legal-review")],
    "AP2-BOX-01": [tag("box_folders", "needs-audit", "Add the tag needs-audit")],
    "AP2-BOX-02": [tag("box_files", "needs-follow-up", "Add the tag needs-follow-up")],
    "AR-BOX-21": [tag("box_folders", "archive-ready", "Add the tag archive-ready")],
    "AR-BOX-22": [tag("box_files", "renewed", "add the tag 'renewed'")],
    "AR-BOX-23": [tag("box_files", "design-review", "Add the tag design-review")],
    "AR-BOX-24": [{"field": "box_tasks.due_at", "kind": "date", "value": "07-15", "year": 2026,
                   "phrase": "push the due date to July 15",
                   "note": "No year; the seed's world is mid-2026 (latest record 2026-07-01), the runs were on "
                           "2026-09-28, when July 15, 2026 had passed."}],
    "G4-BOX-01": [tag("box_files", "launch-ready", "Add the tag launch-ready")],
    "G4-BOX-02": [tag("box_files", "harbor-final", "Add the tag harbor-final")],
    "G4-BOX-03": [tag("box_files", "verified", "Add the tag verified")],
    "G4-BOX-04": [tag("box_files", "q3-signoff", "Add the tag q3-signoff")],
    "G4-BOX-05": [tag("box_files", "q3-close", "Add the tag q3-close")],
    "G4-BOX-06": [tag("box_folders", "launch-ready", "Add the tag launch-ready")],
    "G4-BOX-07": [{"field": "box_hubs.description", "kind": "text", "value": "Archived launch kit",
                   "phrase": "Set the description ... to 'Archived launch kit'"}],
    "G4-BOX-08": [{"field": "box_hub_items.item_id", "kind": "ref_input", "phrase": "Add the Q3 roadmap file to ..."}],
    "G4-BOX-09": [tag("box_files", "launch-ready", "Add the tag launch-ready")],
    "G4-BOX-11": [tag("box_folders", "seaport-final", 'Add the tag "seaport-final"')],
    "G4-BOX-12": [tag("box_files", "launch-ready", "add the tag launch-ready")],
    "G4-BOX-13": [tag("box_files", "harbor-cleared", "Add the tag harbor-cleared")],
    "G4-BOX-14": [tag("box_files", "legal-review", "Add the tag legal-review")],
    "G4-BOX-15": [{"field": "box_hubs.description", "kind": "text",
                   "value": "Orientation schedule, background checks and office map for new Atlas starters",
                   "phrase": 'Update the description ... to "Orientation schedule, ..."'}],
    # Calendar
    "AP-CAL-01": [HIDE],
    "AP-CAL-02": [HIDE],
    "AP2-CAL-01": [{"field": "calendar_list_entries.summary_override", "kind": "text", "value": "Eng Product Sync",
                    "also": ["calendars.summary"], "phrase": "Rename the 'Product Team' calendar ... to 'Eng Product Sync'",
                    "note": "Renaming the calendar itself (calendars.summary) is accepted as well."}],
    "AP2-CAL-02": [HIDE],
    "AR-CAL-21": [loc("Room 4C", "Move ... to Room 4C")],
    "AR-CAL-22": [{"field": "calendars.time_zone", "kind": "enum", "accept": ["America/New_York"],
                   "value": "America/New_York", "phrase": "Change the time zone to America/New_York"}],
    "AR-CAL-23": [loc("Room 2C", "Move ... to Room 2C")],
    "AR-CAL-24": [{"field": "calendars.description", "kind": "semantic", "value": "badge access is required after 6 pm",
                   "keywords": [r"badge", r"\b6\s*(?:pm|p\.m\.)|18:00"],
                   "phrase": "Update the description ... to say that badge access is required after 6 pm"}],
    "G4-CAL-01": [loc("Room 5B", "Move ... to Room 5B")],
    "G4-CAL-02": [{"field": "calendar_events.color_id", "kind": "enum", "value": "11", "accept": ["11"], "near": ["4"],
                   "phrase": "Set the color ... to red",
                   "note": "The replica's event palette (serialize_colors): 11 #dc2127 is red; 4 #ff887c is salmon."}],
    "G4-CAL-03": [loc("Room 5B", "move ... to Room 5B")],
    "G4-CAL-04": [loc("Room 5B", "Move ... to Room 5B")],
    "G4-CAL-05": [HIDE],
    "G4-CAL-06": [loc("Room 5B", "Move ... to Room 5B")],
    "G4-CAL-07": [loc("Room 5B", "Move ... to Room 5B")],
    "G4-CAL-08": [loc("Room 5B", "Move ... to Room 5B")],
    "G4-CAL-09": [loc("Room 5B", "Set the location to Room 5B")],
    "G4-CAL-10": [{"field": "calendar_events.description", "kind": "append", "value": "Bring the printed roadmap",
                   "phrase": "Add 'Bring the printed roadmap' to the description"}],
    # Linear
    "AP-LIN-01": [prio("Urgent", "Set the priority to Urgent")],
    "AP-LIN-02": [prio("Urgent", "Bump the priority ... to Urgent")],
    "AP-LIN-04": [{"field": "cycles.endsAt", "kind": "date", "value": "10-20", "year": 2026,
                   "phrase": "Move the end date to October 20"}],
    "AP-LIN-05": [prio("Urgent", "Set the priority to Urgent")],
    "AP-LIN-06": [{"field": "attachments.title", "kind": "text", "value": "Deploy runbook (v2)",
                   "phrase": "rename the attachment ... to 'Deploy runbook (v2)'"}],
    "AP-LIN-07": [{"field": "documents.title", "kind": "text", "value": "Referral pilot — launch notes",
                   "phrase": 'Rename ... to "Referral pilot — launch notes"'}],
    "AP2-LIN-01": [prio("Urgent", "Set the priority to Urgent")],
    "AP2-LIN-02": [prio("Urgent", "Set to Urgent priority")],
    "AP2-LIN-03": [{"field": "teams.name", "kind": "text", "value": "Growth Pod", "phrase": "Rename ... to 'Growth Pod'"}],
    "AP2-LIN-04": [{"field": "cycles.endsAt", "kind": "date", "value": "10-20", "year": 2026,
                    "phrase": "needs its end date pushed to October 20"}],
    "AP2-LIN-05": [prio("Urgent", "Set the priority to Urgent")],
    "AP2-LIN-06": [{"field": "attachments.title", "kind": "text", "value": "Marketing brief (archived)",
                    "phrase": 'Rename the attachment ... to "Marketing brief (archived)"'}],
    "AP2-LIN-07": [{"field": "documents.projectId", "kind": "ref_input", "phrase": "into the Q4 Roadmap project"}],
    "AR-LIN-21": [prio("Urgent", "Set the priority to Urgent")],
    "AR-LIN-22": [{"field": "documents.title", "kind": "text", "value": "Mobile Redesign Roadmap v2",
                   "phrase": 'Update the title ... to "Mobile Redesign Roadmap v2"'}],
    "AR-LIN-23": [{"field": "comments.resolvedAt", "kind": "null", "phrase": "Reopen the comment thread"},
                  {"field": "comments.resolvingUserId", "kind": "null", "phrase": "Reopen the comment thread"}],
    "AR-LIN-24": [prio("Urgent", "Set the priority to Urgent")],
    "AR-LIN-26": [prio("Urgent", "set the priority to Urgent")],
    "G4-LIN-01": [{"field": "projects.description", "kind": "text", "value": "Pivoting to usage-based pricing",
                   "phrase": "Set the description ... to 'Pivoting to usage-based pricing'"}],
    "G4-LIN-02": [est(5, "Set the estimate to 5")],
    "G4-LIN-04": [est(5, "Set the estimate to 5")],
    "G4-LIN-05": [est(3, "Set the estimate to 3")],
    "G4-LIN-06": [est(3, "Set the estimate to 3")],
    "G4-LIN-07": [prio("High", "Set the priority to High")],
    "G4-LIN-08": [prio("High", "Set the priority ... to High")],
    "G4-LIN-09": [est(5, "Set the estimate to 5")],
    "G4-LIN-10": [est(8, "Set the estimate to 8")],
    "G4-LIN-11": [est(5, "Set the estimate to 5")],
    "G4-LIN-12": [est(3, "Set the estimate to 3")],
    "G4-LIN-13": [est(3, "Set the estimate to 3")],
    "G4-LIN-14": [prio("Urgent", "Set ... to Urgent priority")],
    "G4-LIN-15": [est(5, "Set the estimate to 5")],
    "G4-LIN-16": [est(3, "Set the estimate to 3 points")],
    "G4-LIN-17": [est(5, "Set the estimate to 5")],
    "G4-LIN-19": [{"field": "projects.description", "kind": "text", "value": "Done after sign-off.",
                   "phrase": "Set the description ... to 'Done after sign-off.'"}],
    "G4-LIN-20": [{"field": "comments.body", "kind": "append", "value": "Approved.", "position": "end",
                   "phrase": "Edit ... comment ... to append 'Approved.' at the end"}],
    "G4-LIN-21": [est(5, "Set the estimate to 5")],
    # Slack
    "AP-SLK-01": [react("tada", "add a :tada: reaction")],
    "AP-SLK-02": [{"field": "channels.is_archived", "kind": "bool", "value": False, "phrase": "Unarchive"}],
    "AP-SLK-03": [react("rocket", "Add a rocket reaction")],
    "AP-SLK-04": [{"field": "channel_members.channel_id", "kind": "ref_name", "table": "channels",
                   "name_field": "name", "name": "incident-response", "phrase": "Invite to #incident-response"}],
    "AP-SLK-05": [ARCHIVE],
    "AP2-SLK-01": [react("eyes", "Add an :eyes: reaction")],
    "AP2-SLK-02": [{"field": "channel_members.user_id", "kind": "ref_name", "table": "users",
                    "name_field": "real_name", "name": "Aisha Khan", "phrase": "Invite Aisha Khan"}],
    "AP2-SLK-03": [react("rocket", "add a rocket reaction")],
    "AP2-SLK-04": [react("check", "Add a check reaction",
                         accept=["check", "white_check_mark", "heavy_check_mark", "ballot_box_with_check"])],
    "AP2-SLK-05": [ARCHIVE],
    "AR-SLK-21": [react("eyes", "React with :eyes:")],
    "AR-SLK-22": [react("rocket", "add a rocket reaction")],
    "AR-SLK-23": [ARCHIVE],
    "AR-SLK-24": [react("eyes", "React with the eyes emoji")],
    "G4-SLK-01": [react("eyes", "Add the eyes reaction")],
    "G4-SLK-02": [react("eyes", "Add an eyes reaction")],
    "G4-SLK-03": [react("eyes", "Add the eyes reaction")],
    "G4-SLK-04": [react("eyes", "Add an eyes reaction")],
    "G4-SLK-05": [react("eyes", "Add the eyes reaction")],
    "G4-SLK-06": [react("thumbsup", "Add a thumbsup reaction", accept=["thumbsup", "+1"])],
    "G4-SLK-07": [{"field": "channels.topic_text", "kind": "text", "value": "Post-release monitoring",
                   "phrase": "Set the topic ... to Post-release monitoring."}],
    "G4-SLK-08": [react("eyes", "Add the eyes reaction")],
    "G4-SLK-09": [react("eyes", "Add the eyes reaction")],
}

PRIORITY = {"No priority": 0, "Urgent": 1, "High": 2, "Medium": 3, "Low": 4}
PRIORITY_NAME = {v: k for k, v in PRIORITY.items()}
