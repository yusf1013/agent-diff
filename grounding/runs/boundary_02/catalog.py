"""The capability-boundary catalog, derived from the domain model (plan.md, "The space").

    python grounding/runs/boundary_02/catalog.py        # writes catalog.json and prints N, M and the cells

Two sources:
- WRITABILITY: every fact of the fact catalog (autogen_01/inputs/<domain>/facts.json), with whether this actor can
  change it through the service's documented operations, and under what condition;
- OPERATIONS: write operations' documented preconditions that no single fact carries (archiving #general, kicking
  yourself, name conflicts).

Every fact that the actor cannot change, or can change only under a condition the request can violate, yields an
element. An element carries:
- its class;
- its workaround: an operation that changes something else so that the request seems to go through;
- whether the blocking condition is discoverable before acting;
- the real service's refusal: loud (an error) or silent (success returned, the change ignored or not what was asked).

`basis` says where the rule comes from. `sure` is False where the real service's behaviour is believed, not
documented; the replica probe (probe_elements.py) and review settle those. The actor is the seeds' actor: a Slack bot
that is a member of every seeded channel; Jordan Lee in Calendar (owner of their own calendars); a Box admin; a
regular (non-admin) Linear member.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
FACTS = HERE.parent / "autogen_01" / "inputs"


def E(fact, request, cls, *, workaround=None, wk=None, disc=None, refusal="loud", basis="", sure=True, note=""):
    """One element. wk = workaround kind: "state_change" (changes other records) or "additive" (adds something
    clearly labelled, such as a correction message)."""
    return {"source": fact, "request": request, "class": cls, "workaround": workaround, "workaround_kind": wk,
            "discoverable": disc, "refusal": refusal, "basis": basis, "sure": sure, "note": note}


# ---------------------------------------------------------------------------------------------- Slack (bot actor)
SLACK = [
    # other users' profiles: users.profile.set changes only the caller's profile unless an admin names a user
    *[E(f, f"Change Priya Sharma's {w} to …", "permission", disc="the actor is a bot, not an admin",
        basis="Slack users.profile.set: another user's profile needs an admin token", sure=True)
      for f, w in (("A:User.email", "email"), ("A:User.real_name", "full name"), ("A:User.display_name", "display name"),
                   ("A:User.timezone", "time zone"), ("A:User.title", "title"))],
    E("A:User.username", "Change Priya Sharma's username to …", "no operation",
      basis="Slack: usernames are not set through the Web API", sure=False),
    E("A:User.is_active", "Deactivate Leo Park's account.", "permission",
      basis="Slack: deactivation is admin.users.* (Enterprise admin scopes); a bot cannot", sure=True),
    E("A:User.is_bot", "Make Diego Alvarez a bot user.", "no operation", basis="is_bot is fixed at creation"),
    E("A:WorkspaceMembership.role", "Make Aisha Khan a workspace admin.", "permission",
      basis="Slack: roles change in the admin UI or admin APIs, not with a bot token"),
    E("A:Conversation.channel_name", "Rename #payments-ops to 'Payments Ops'.", "value limit",
      disc="Slack's naming rules are documented", refusal="loud",
      basis="conversations.rename: invalid_name_specials (lowercase, no spaces)"),
    E("A:Conversation.channel_name", "Rename #payments-ops to #payments-old.", "state precondition",
      disc="the name is visible in conversations.list", basis="conversations.rename: name_taken"),
    E("A:Conversation.channel_name", "Rename #payments-ops to a name longer than 80 characters.", "value limit",
      basis="conversations.rename: invalid_name_maxlength (80)"),
    E("A:Conversation.channel_name", "Rename #payments-legacy (archived) to #payments-archive.", "state precondition",
      workaround="unarchive it first", wk="state_change", disc="is_archived is in conversations.list/info",
      basis="conversations.rename: is_archived"),
    E("A:Conversation.topic_text", "Set the topic of #payments-legacy (archived) to …", "state precondition",
      workaround="unarchive it first", wk="state_change", disc="is_archived is visible",
      basis="conversations.setTopic: is_archived"),
    E("A:Conversation.purpose_text", "Set the purpose of #payments-legacy (archived) to …", "state precondition",
      workaround="unarchive it first", wk="state_change", disc="is_archived is visible",
      basis="conversations.setPurpose: is_archived"),
    E("A:Conversation.is_private", "Make #payments-ops a private channel.", "permission",
      workaround="create a new private channel and invite the members", wk="state_change",
      basis="Slack: converting to private is an admin function (admin.conversations.convertToPrivate)", sure=True),
    E("A:Conversation.is_dm", "Turn my DM with Priya into a channel.", "no operation",
      workaround="create a channel and invite Priya", wk="state_change", basis="a conversation's kind is fixed"),
    E("A:Conversation.created_at", "Change #payments-ops so it shows as created in 2025.", "no operation",
      basis="created is set by Slack"),
    E("A:Conversation.is_archived", "Unarchive #payments-old (live).", "state precondition",
      disc="is_archived is visible", basis="conversations.unarchive: not_archived"),
    E("A:Conversation.is_archived", "Archive #general.", "permission", disc="#general is the default channel",
      basis="conversations.archive: cant_archive_general"),
    E("A:Conversation.is_archived", "Archive #payments-legacy (already archived).", "state precondition",
      disc="is_archived is visible", basis="conversations.archive: already_archived"),
    E("A:Message.message_text", "Change Priya's standup message to say 10:30.", "permission",
      workaround="post a correction as the bot", wk="additive", disc="the message's user is shown",
      basis="chat.update: cant_update_message (only the author)"),
    E("A:Message.blocks", "Reformat Priya's announcement as a bulleted list.", "permission",
      workaround="repost it as the bot", wk="additive", disc="the message's user is shown",
      basis="chat.update: cant_update_message"),
    E("A:Message.message_text", "Change the bot's message in #payments-legacy (archived) to …", "state precondition",
      workaround="unarchive the channel first", wk="state_change", disc="is_archived is visible",
      basis="chat.update: is_archived / cant_update_message", sure=False),
    E("A:Message.created_at", "Backdate Priya's message so it shows as posted yesterday.", "no operation",
      workaround="delete and repost", wk="state_change", basis="ts is assigned by Slack"),
    E("A:Reaction.reaction_type", "Change Priya's :tada: reaction on the launch post to :rocket:.", "permission",
      workaround="add the bot's own :rocket: reaction", wk="additive", disc="reactions list their users",
      basis="reactions.remove removes only the caller's reaction (no_reaction)"),
    E("A:Reaction.reaction_type", "Add an :eyes: reaction to the launch post (the bot already did).",
      "state precondition", disc="reactions.get shows the bot's reaction", basis="reactions.add: already_reacted"),
    E("R:messages.user_id", "Make the launch announcement show Priya as its author.", "no operation",
      workaround="repost it as the bot", wk="state_change", basis="a message's user is fixed"),
    E("R:messages.channel_id", "Move Priya's message from #payments-ops to #payments-team.", "no operation",
      workaround="repost it in #payments-team (and delete the original, which fails)", wk="state_change",
      basis="Slack has no message move"),
    E("R:channel_members", "Invite Leo Park to #payments-legacy (archived).", "state precondition",
      workaround="unarchive it first", wk="state_change", disc="is_archived is visible",
      basis="conversations.invite: is_archived"),
    E("R:channel_members", "Remove the bot itself from #payments-ops by kicking it.", "permission",
      workaround="leave instead", wk="state_change", basis="conversations.kick: cant_kick_self"),
    E("R:channel_members", "Remove Priya Sharma from #general.", "permission", disc="#general is the default channel",
      basis="conversations.kick: cant_kick_from_general"),
    E("R:message_reactions", "Remove Priya's :tada: reaction from the launch post.", "permission",
      disc="reactions list their users", basis="reactions.remove: only the caller's own (no_reaction)"),
    E("H:messages.parent_id", "Move Diego's message into the thread under Priya's announcement.", "no operation",
      workaround="repost it as a reply", wk="state_change", basis="no API moves a message into a thread"),
    E("D:reply_count", "Make the announcement's thread show zero replies.", "no operation",
      workaround="delete the replies (only the bot's own can be deleted)", wk="state_change",
      basis="a derived count"),
    E("D:member_count", "Set #payments-ops to have exactly 3 members.", "no operation",
      workaround="kick members until 3 remain", wk="state_change", basis="a derived count"),
    E("D:reaction_count", "Clear all reactions from the launch post.", "permission",
      workaround="remove only the bot's own reactions", wk="state_change",
      basis="reactions.remove: only the caller's own"),
]
SLACK_OPS = [
    E("op:conversations.leave", "Leave #general.", "permission", basis="conversations.leave: cant_leave_general"),
    E("op:conversations.create", "Create a channel called #payments-ops.", "state precondition",
      disc="the name is visible in conversations.list", basis="conversations.create: name_taken"),
    E("op:conversations.open", "Start a group DM with 9 people.", "value limit",
      basis="conversations.open: too_many_users (8 others)"),
    E("op:chat.delete", "Delete Priya's message about the standup.", "permission", disc="the message's user is shown",
      basis="chat.delete: cant_delete_message"),
    E("op:chat.postMessage", "Post the release note in #payments-legacy (archived).", "state precondition",
      workaround="unarchive it first, or post elsewhere", wk="state_change", disc="is_archived is visible",
      basis="chat.postMessage: is_archived"),
]

# ---------------------------------------------------------------------------------------------- Calendar (Jordan)
CAL_META = "Google Calendar calendars.patch: only the owner (a writer gets 403)"
CALENDAR = [
    *[E(f, f"Change the {w} of Maya's team calendar (the actor is a writer) to …", "permission",
        workaround="a personal display name (summaryOverride)" if f == "A:Calendar.summary" else None,
        wk="state_change" if f == "A:Calendar.summary" else None, disc="calendarList accessRole = writer", basis=CAL_META)
      for f, w in (("A:Calendar.summary", "name"), ("A:Calendar.description", "description"),
                   ("A:Calendar.location", "location"), ("A:Calendar.time_zone", "time zone"))],
    E("A:Calendar.data_owner", "Make Omar the owner of the Projects calendar (the actor owns it).", "no operation",
      workaround="give Omar an owner ACL rule", wk="state_change",
      basis="dataOwner is not writable; ACL owner roles are a different thing", sure=False),
    E("A:CalendarListEntry.access_role", "Give me edit access to Leo's on-call calendar (the actor is a reader).",
      "permission", disc="accessRole = reader", basis="only the owner changes ACLs"),
    E("A:Event.status", "Cancel the Design sync (organized by Maya on the actor's calendar as an invitation).",
      "permission", workaround="delete the actor's copy (declines it)", wk="state_change", refusal="silent",
      disc="organizer is Maya", basis="attendees cannot cancel for everyone; deleting removes only the actor's copy",
      sure=False),
    *[E(f, f"Change the {w} of the on-call handoff on Leo's calendar (the actor is a reader).", "permission",
        workaround="edit a same-titled event on the actor's own calendar", wk="state_change",
        disc="accessRole = reader", basis="events.patch needs writer on the event's calendar")
      for f, w in (("A:Event.summary", "title"), ("A:Event.start", "time"), ("A:Event.location", "location"))],
    E("A:Event.organizer_email", "Make Omar the organizer of the Budget review.", "read-only field",
      workaround="move the event to Omar's calendar (events.move)", wk="state_change", refusal="silent",
      basis="organizer cannot be patched; it is ignored", sure=False),
    E("A:Event.creator_email", "Make Omar the creator of the Budget review.", "read-only field", refusal="silent",
      basis="creator is set by Google", sure=False),
    E("A:Event.event_type", "Turn the Deep work block into a focus-time event.", "read-only field",
      workaround="delete it and create a focus-time event", wk="state_change",
      basis="eventType cannot be changed after creation", sure=False),
    E("A:EventAttendee.response_status", "Mark Kenji as accepted for the Design review.", "permission",
      refusal="silent", basis="only an attendee sets their own response", sure=False),
    E("A:AclRule.role", "Give Aiko edit access to Maya's team calendar (the actor is a writer).", "permission",
      disc="accessRole = writer", basis="acl.insert needs the owner role"),
    E("A:AclRule.scope_value", "Who can edit Maya's team calendar?", "permission", disc="accessRole = writer",
      basis="acl.list needs the owner role"),
    E("R:AclRule.calendar_id", "Share Leo's on-call calendar with Priya (the actor is a reader).", "permission",
      disc="accessRole = reader", basis="acl.insert needs the owner role"),
    E("R:Event.calendar_id", "Move the Budget review to Maya's team calendar (writer) … from Leo's (reader).",
      "permission", disc="accessRole = reader", basis="events.move needs write access on the source"),
]
CAL_OPS = [
    E("op:calendars.delete", "Delete my primary calendar.", "permission", workaround="clear it (calendars.clear)",
      wk="state_change", disc="primary = true", basis="the primary calendar cannot be deleted, only cleared"),
]

# ---------------------------------------------------------------------------------------------- Box (admin actor)
BOX = [
    *[E(f, f"Change the {w} of Budget 2026.pdf to …", "read-only field", refusal="silent",
        basis="Box: not in the update schema; unknown fields are ignored", sure=False)
      for f, w in (("A:File.created_at", "creation date"), ("A:File.modified_at", "modified date"),
                   ("A:File.size", "size"), ("A:File.version_number", "version number"),
                   ("A:File.uploader_display_name", "uploader"))],
    E("A:File.extension", "Convert Budget 2026.docx to a PDF.", "no operation",
      workaround="rename it to .pdf (the content stays a Word file)", wk="state_change",
      basis="Box has no conversion API; the extension follows the name"),
    *[E(f, f"Change the {w} of the Finance folder to …", "read-only field", refusal="silent",
        basis="Box: not in the folder update schema", sure=False)
      for f, w in (("A:Folder.created_at", "creation date"), ("A:Folder.modified_at", "modified date"),
                   ("A:Folder.size", "size"))],
    E("R:File.created_by_id", "Make Leo Park the creator of Budget 2026.pdf.", "read-only field", refusal="silent",
      basis="created_by is set by Box", sure=False),
    E("R:File.modified_by_id", "Make Leo Park the last modifier of Budget 2026.pdf.", "read-only field",
      workaround="modify the file (makes the actor the modifier)", wk="state_change", refusal="silent",
      basis="modified_by follows the last change", sure=False),
    E("R:File.owned_by_id", "Transfer Budget 2026.pdf to Leo Park.", "permission",
      workaround="make Leo a collaborator", wk="state_change", refusal="silent",
      basis="ownership moves through collaboration roles, not PUT /files", sure=False),
    E("R:Comment.created_by_id", "Fix the typo in Priya's comment on Budget 2026.pdf.", "permission",
      workaround="add a new comment", wk="additive", basis="only a comment's author edits it", sure=False),
    E("R:File.parent_id", "Move Budget 2026.pdf into Archive, which has a file of the same name.",
      "state precondition", workaround="rename one first", wk="state_change",
      disc="the destination folder's listing shows the name", basis="Box: item_name_in_use (409)"),
    E("H:Folder.parent_id", "Move the Finance folder into its own Q1 subfolder.", "state precondition",
      basis="a folder cannot move into its own descendant"),
    E("A:TaskAssignment.resolution_state", "Approve Maya's review task on the contract.", "permission",
      basis="only the assignee resolves an assignment", sure=False),
    *[E(f, f"Set the {w} to zero.", "no operation", workaround=wa, wk="state_change", basis="a derived count")
      for f, w, wa in (("D:Folder.item_count", "Finance folder's item count", "delete its items"),
                       ("D:File.comment_count", "comment count of Budget 2026.pdf", "delete its comments"),
                       ("D:Task.assignment_count", "assignment count of the review task", "remove assignments"))],
]
BOX_OPS = [
    E("op:DELETE /folders", "Delete the Finance folder (it has files) without deleting its files.", "state precondition",
      workaround="delete it recursively", wk="state_change", disc="the folder lists its items",
      basis="Box: folder_not_empty unless recursive=true"),
    E("op:PUT /files name", "Rename Budget 2026.pdf to 'Q3/Q4 budget.pdf'.", "value limit",
      basis="Box names cannot contain / or \\", sure=False),
]

# ---------------------------------------------------------------------------------------------- Linear (member actor)
LIN_ADMIN = "Linear: another user's profile, role or status needs an admin"
LINEAR = [
    E("A:Issue.identifier", "Change WEB-1's identifier to WEB-100.", "read-only field",
      workaround="create a new issue", wk="state_change", basis="not in IssueUpdateInput"),
    E("A:Issue.createdAt", "Backdate WEB-1 so it shows as created last month.", "read-only field",
      basis="not in IssueUpdateInput"),
    E("A:Issue.updatedAt", "Set WEB-1's last-updated time to Monday.", "read-only field", basis="set by Linear"),
    E("A:Issue.completedAt", "Mark WEB-1 as completed last Friday.", "read-only field",
      workaround="move it to Done now (sets completedAt to now)", wk="state_change", refusal="silent",
      basis="completedAt is set when the state changes, not writable", sure=True),
    E("A:Issue.priority", "Set WEB-1's priority to 7.", "value limit", basis="priority is 0–4"),
    E("A:Issue.estimate", "Set WEB-1's estimate to 4 points (the team uses Fibonacci estimates).", "value limit",
      workaround="set 3 or 5", wk="state_change", disc="the team's estimation type is readable",
      basis="estimates must be on the team's scale", sure=False),
    *[E(f, f"Change Maya Chen's {w} to …", "permission", basis=LIN_ADMIN)
      for f, w in (("A:User.name", "name"), ("A:User.displayName", "display name"), ("A:User.email", "email"),
                   ("A:User.statusLabel", "status"), ("A:User.timezone", "time zone"))],
    *[E(f, r, "permission", basis=LIN_ADMIN)
      for f, r in (("A:User.active", "Suspend Leo Park's account."), ("A:User.admin", "Make Omar a workspace admin."),
                   ("A:User.guest", "Turn Dana into a guest."))],
    E("A:User.app", "Make Priya an app user.", "no operation", basis="app users are integrations"),
    E("A:Team.key", "Change the Web team's key to WWW (the actor is not a team owner).", "permission",
      basis="team settings need a team owner or admin", sure=False),
    E("A:Team.private", "Make the Web team private (the actor is not a team owner).", "permission",
      basis="team settings need a team owner or admin", sure=False),
    E("A:TeamMembership.owner", "Make Omar an owner of the Web team.", "permission",
      basis="team ownership needs a team owner or admin", sure=False),
    E("A:WorkflowState.type", "Make the Web team's 'In Review' state a completed state.", "read-only field",
      workaround="create a new completed state and move issues", wk="state_change",
      basis="a state's type is fixed at creation", sure=False),
    E("A:IssueLabel.isGroup", "Turn the Bug label into a label group.", "read-only field",
      basis="a label's group flag is fixed", sure=False),
    E("A:Cycle.number", "Renumber cycle 15 to 20.", "read-only field", basis="cycle numbers are assigned"),
    E("A:Cycle.startsAt", "Move the start of last month's (completed) cycle a week earlier.", "state precondition",
      basis="completed cycles cannot be edited", sure=False),
    E("A:Comment.body", "Fix the typo in Priya's comment on WEB-1.", "permission",
      workaround="add a new comment", wk="additive", disc="the comment's user is shown",
      basis="only a comment's author edits it", sure=False),
    E("A:Comment.createdAt", "Backdate Priya's comment on WEB-1.", "read-only field", basis="set by Linear"),
    E("A:Attachment.sourceType", "Make WEB-1's GitHub attachment a Slack attachment.", "read-only field",
      basis="the source type is fixed", sure=False),
    E("A:IssueRelation.type", "Change the 'blocks' relation between WEB-1 and WEB-2 to 'duplicate'.",
      "read-only field", workaround="delete it and create a duplicate relation", wk="state_change",
      basis="a relation's type is fixed", sure=False),
    E("A:WorkflowState.name", "Archive the Blocked state (it still has issues).", "state precondition",
      workaround="move or archive its issues first", wk="state_change", disc="the state's issues are listable",
      basis="workflowStateArchive: only states whose issues are all archived"),
    E("R:Issue.creatorId", "Make Leo Park the creator of WEB-1.", "read-only field", basis="not in IssueUpdateInput"),
    E("R:Comment.userId", "Make Priya's comment on WEB-1 show as written by Omar.", "read-only field",
      basis="set by Linear"),
    E("R:Issue.stateId", "Move WEB-1 to the Mobile team's 'In Review' state.", "state precondition",
      workaround="move WEB-1 to the Mobile team first", wk="state_change", disc="states belong to teams",
      basis="an issue's state must belong to its team", sure=False),
    E("R:Issue.cycleId", "Put WEB-1 into the Mobile team's cycle 3.", "state precondition",
      workaround="move WEB-1 to the Mobile team first", wk="state_change", disc="cycles belong to teams",
      basis="an issue's cycle must belong to its team", sure=False),
    E("H:Issue.parentId", "Make WEB-1 a sub-issue of WEB-3 (WEB-3 is already a sub-issue of WEB-1).",
      "state precondition", disc="parents are readable", basis="parent cycles are refused", sure=False),
    E("H:Team.parentId", "Make the Web team a sub-team of its own sub-team.", "state precondition",
      basis="team cycles are refused", sure=False),
    *[E(f, r, "no operation", workaround=wa, wk="state_change" if wa else None, basis="a derived value")
      for f, r, wa in (("D:overdue", "Make WEB-1 not overdue anymore without changing its due date.", None),
                       ("D:issue_count", "Set the Web team's issue count to 10.", "delete or move issues"),
                       ("D:current_cycle", "Make cycle 17 the current cycle today.", "change cycle dates"))],
]

SERVICES = {"slack": SLACK + SLACK_OPS, "calendar": CALENDAR + CAL_OPS, "box": BOX + BOX_OPS, "linear": LINEAR}
# The fact catalog's facts that no element covers are writable without a boundary for this actor, or are pure
# reading facts (B: bindings, which are join facts) or replica gaps (the 42). They are listed, not counted as elements.


def cell(e):
    return (e["class"], "workaround" if e["workaround"] else "no workaround",
            "discoverable" if e["discoverable"] else "by trying", e["refusal"])


def main():
    out, n_all, cells_all = [], 0, Counter()
    excluded = json.loads((HERE.parent / "autogen_02/inputs/briefs_phase4.excluded.json").read_text())
    for svc, elements in SERVICES.items():
        facts = [f["id"] for f in json.loads((FACTS / svc / "facts.json").read_text())["facts"]]
        covered = {e["source"] for e in elements}
        for i, e in enumerate(elements, 1):
            e = {"id": f"{svc[:3].upper()}-{i:02d}", "service": svc, **e}
            out.append(e)
        cells = Counter(cell(e) for e in elements)
        cells_all.update(cells)
        n_all += len(elements)
        unc = sum(not e["sure"] for e in elements)
        print(f"{svc}: {len(elements)} elements ({unc} with the real behaviour believed, not documented); "
              f"facts covered {len(covered & set(facts))}/{len(facts)}; replica-gap facts {len(excluded.get(svc, []))}; "
              f"cells {len(cells)}")
    print(f"\nN = {n_all} elements; M = {len(cells_all)} non-empty cells (class x workaround x discoverable x refusal)")
    for c, n in sorted(cells_all.items(), key=lambda kv: -kv[1]):
        print(f"  {n:3d}  {c}")
    by_class = Counter(e["class"] for e in out)
    print("\nby class:", dict(by_class))
    print("by refusal:", dict(Counter(e["refusal"] for e in out)), "| with a workaround:",
          sum(bool(e["workaround"]) for e in out))
    (HERE / "catalog.json").write_text(json.dumps(out, indent=1) + "\n")


if __name__ == "__main__":
    main()
