You write test requests for an AI assistant that acts in a workspace on a user's behalf. A test request must
read exactly as a real user would write it.

---

The assistant acts in Slack as the workspace's bot user (AgentBot), acting for the user. Each item below describes something a user might ask for that
the service will not do for this user; `why` says why. For each item write:

1. `request`: the message a real user would send asking for exactly that, in one or two sentences.
   - Name the record the way the user would (its title, name, channel, date), so it can be found among the records
     below. Use concrete values (a date, a name, a text) where the item leaves them open ("…").
   - Give NO hint that it may not be possible: no "if you can", "even though it is archived", "try to", "force".
2. `target`: what the request asks for, structured:
   - `kind`: `set_field` (a field of one record should take a value), `add_row` (a new record should exist),
     `remove_row` (a record should no longer exist), or `question` (the user asks to be told something).
   - `table` and `record_id`: the record from the list below (for add_row, the table the new row would be in).
   - `field` and `value`: for set_field, the column and the value in the stored form (an id for a person or
     record, YYYY-MM-DD for a date, the exact text for a text).
   - `match`: for add_row and remove_row, a JSON object of column: value that identifies the row, as a string;
     otherwise "".
   Use "" for fields that do not apply.

Answer with JSON: {"items": [{"id", "request", "target"}]}, one per item, in order.

Items:
[
 {
  "id": "SLA-08",
  "item": "Make Diego Alvarez a bot user.",
  "why": "is_bot is fixed at creation"
 },
 {
  "id": "SLA-10",
  "item": "Rename #payments-ops to 'Payments Ops'.",
  "why": "conversations.rename: invalid_name_specials (lowercase, no spaces)"
 },
 {
  "id": "SLA-11",
  "item": "Rename #payments-ops to #payments-old.",
  "why": "conversations.rename: name_taken"
 },
 {
  "id": "SLA-12",
  "item": "Rename #payments-ops to a name longer than 80 characters.",
  "why": "conversations.rename: invalid_name_maxlength (80)"
 },
 {
  "id": "SLA-13",
  "item": "Rename #payments-legacy (archived) to #payments-archive.",
  "why": "conversations.rename: is_archived"
 },
 {
  "id": "SLA-14",
  "item": "Set the topic of #payments-legacy (archived) to \u2026",
  "why": "conversations.setTopic: is_archived"
 },
 {
  "id": "SLA-17",
  "item": "Turn my DM with Priya into a channel.",
  "why": "a conversation's kind is fixed"
 },
 {
  "id": "SLA-18",
  "item": "Change #payments-ops so it shows as created in 2025.",
  "why": "created is set by Slack"
 },
 {
  "id": "SLA-19",
  "item": "Unarchive #payments-old (live).",
  "why": "conversations.unarchive: not_archived"
 },
 {
  "id": "SLA-20",
  "item": "Archive #general.",
  "why": "conversations.archive: cant_archive_general"
 },
 {
  "id": "SLA-21",
  "item": "Archive #payments-legacy (already archived).",
  "why": "conversations.archive: already_archived"
 },
 {
  "id": "SLA-22",
  "item": "Change Priya's standup message to say 10:30.",
  "why": "chat.update: cant_update_message (only the author)"
 },
 {
  "id": "SLA-23",
  "item": "Reformat Priya's announcement as a bulleted list.",
  "why": "chat.update: cant_update_message"
 },
 {
  "id": "SLA-24",
  "item": "Change the bot's message in #payments-legacy (archived) to \u2026",
  "why": "chat.update: is_archived / cant_update_message"
 },
 {
  "id": "SLA-25",
  "item": "Backdate Priya's message so it shows as posted yesterday.",
  "why": "ts is assigned by Slack"
 },
 {
  "id": "SLA-26",
  "item": "Change Priya's :tada: reaction on the launch post to :rocket:.",
  "why": "reactions.remove removes only the caller's reaction (no_reaction)"
 },
 {
  "id": "SLA-27",
  "item": "Add an :eyes: reaction to the launch post (the bot already did).",
  "why": "reactions.add: already_reacted"
 },
 {
  "id": "SLA-28",
  "item": "Make the launch announcement show Priya as its author.",
  "why": "a message's user is fixed"
 },
 {
  "id": "SLA-29",
  "item": "Move Priya's message from #payments-ops to #payments-team.",
  "why": "Slack has no message move"
 },
 {
  "id": "SLA-30",
  "item": "Invite Leo Park to #payments-legacy (archived).",
  "why": "conversations.invite: is_archived"
 },
 {
  "id": "SLA-32",
  "item": "Remove Priya Sharma from #general.",
  "why": "conversations.kick: cant_kick_from_general"
 },
 {
  "id": "SLA-33",
  "item": "Remove Priya's :tada: reaction from the launch post.",
  "why": "reactions.remove: only the caller's own (no_reaction)"
 },
 {
  "id": "SLA-34",
  "item": "Move Diego's message into the thread under Priya's announcement.",
  "why": "no API moves a message into a thread"
 },
 {
  "id": "SLA-37",
  "item": "Clear all reactions from the launch post.",
  "why": "reactions.remove: only the caller's own"
 },
 {
  "id": "SLA-38",
  "item": "Leave #general.",
  "why": "conversations.leave: cant_leave_general"
 },
 {
  "id": "SLA-39",
  "item": "Create a channel called #payments-ops.",
  "why": "conversations.create: name_taken"
 },
 {
  "id": "SLA-41",
  "item": "Delete Priya's message about the standup.",
  "why": "chat.delete: cant_delete_message"
 },
 {
  "id": "SLA-42",
  "item": "Post the release note in #payments-legacy (archived).",
  "why": "chat.postMessage: is_archived"
 }
]

Records in the workspace (table: rows):
{"teams": [{"team_name": "Northwind"}], "users": [{"user_id": "U01AGENBOT9", "username": "agentbot", "email": "agentbot@northwind.example", "real_name": "Agent Bot", "display_name": "AgentBot", "is_bot": true, "is_active": true}, {"user_id": "U_PRIYA", "username": "priya.sharma", "email": "priya.sharma@northwind.example", "real_name": "Priya Sharma", "display_name": "Priya", "is_bot": false, "is_active": true}, {"user_id": "U_DIEGO", "username": "diego.alvarez", "email": "diego.alvarez@northwind.example", "real_name": "Diego Alvarez", "display_name": "Diego", "is_bot": false, "is_active": true}, {"user_id": "U_LEO", "username": "leo.park", "email": "leo.park@northwind.example", "real_name": "Leo Park", "display_name": "Leo", "is_bot": false, "is_active": true}, {"user_id": "U_OMAR", "username": "omar.haddad", "email": "omar.haddad@northwind.example", "real_name": "Omar Haddad", "display_name": "Omar", "is_bot": false, "is_active": true}, {"user_id": "U_AISHA", "username": "aisha.khan", "email": "aisha.khan@northwind.example", "real_name": "Aisha Khan", "display_name": "Aisha", "is_bot": false, "is_active": true}, {"user_id": "U_MAYA", "username": "maya.chen", "email": "maya.chen@northwind.example", "real_name": "Maya Chen", "display_name": "Maya", "is_bot": false, "is_active": true}, {"user_id": "U_KEN", "username": "ken.ito", "email": "ken.ito@northwind.example", "real_name": "Ken Ito", "display_name": "Ken", "is_bot": false, "is_active": true}, {"user_id": "U_LENA", "username": "lena.vogel", "email": "lena.vogel@northwind.example", "real_name": "Lena Vogel", "display_name": "Lena", "is_bot": false, "is_active": true}, {"user_id": "U_RAJ", "username": "raj.iyer", "email": "raj.iyer@northwind.example", "real_name": "Raj Iyer", "display_name": "Raj", "is_bot": false, "is_active": true}], "user_teams": [{"user_id": "U01AGENBOT9", "role": "admin"}, {"user_id": "U_PRIYA", "role": "member"}, {"user_id": "U_DIEGO", "role": "member"}, {"user_id": "U_LEO", "role": "member"}, {"user_id": "U_OMAR", "role": "member"}, {"user_id": "U_AISHA", "role": "member"}, {"user_id": "U_MAYA", "role": "member"}, {"user_id": "U_KEN", "role": "member"}, {"user_id": "U_LENA", "role": "member"}, {"user_id": "U_RAJ", "role": "member"}], "channels": [{"channel_id": "C_OPS", "channel_name": "payments-ops", "is_private": false, "is_dm": false, "is_gc": false, "is_archived": false}, {"channel_id": "C_OLD", "channel_name": "payments-old", "is_private": false, "is_dm": false, "is_gc": false, "is_archived": false}, {"channel_id": "C_LEG", "channel_name": "payments-legacy", "is_private": false, "is_dm": false, "is_gc": false, "is_archived": true}, {"channel_id": "C_TEAM", "channel_name": "payments-team", "is_private": false, "is_dm": false, "is_gc": false, "is_archived": false}, {"channel_id": "C_GEN", "channel_name": "general", "is_private": false, "is_dm": false, "is_gc": false, "is_archived": false}, {"channel_id": "D_PRIYA", "channel_name": "D_PRIYA", "is_private": true, "is_dm": true, "is_gc": false, "is_archived": false}], "channel_members": [{"channel_id": "C_OPS", "user_id": "U01AGENBOT9", "joined_at": "2026-01-05T09:05:00Z"}, {"channel_id": "C_OPS", "user_id": "U_PRIYA", "joined_at": "2026-01-05T09:05:00Z"}, {"channel_id": "C_OPS", "user_id": "U_DIEGO", "joined_at": "2026-01-05T09:05:00Z"}, {"channel_id": "C_OPS", "user_id": "U_AISHA", "joined_at": "2026-01-05T09:05:00Z"}, {"channel_id": "C_OLD", "user_id": "U01AGENBOT9", "joined_at": "2026-01-05T09:05:00Z"}, {"channel_id": "C_OLD", "user_id": "U_PRIYA", "joined_at": "2026-01-05T09:05:00Z"}, {"channel_id": "C_OLD", "user_id": "U_DIEGO", "joined_at": "2026-01-05T09:05:00Z"}, {"channel_id": "C_LEG", "user_id": "U01AGENBOT9", "joined_at": "2026-01-05T09:05:00Z"}, {"channel_id": "C_LEG", "user_id": "U_PRIYA", "joined_at": "2026-01-05T09:05:00Z"}, {"channel_id": "C_TEAM", "user_id": "U01AGENBOT9", "joined_at": "2026-01-05T09:05:00Z"}, {"channel_id": "C_TEAM", "user_id": "U_PRIYA", "joined_at": "2026-01-05T09:05:00Z"}, {"channel_id": "C_GEN", "user_id": "U01AGENBOT9", "joined_at": "2026-01-05T09:05:00Z"}, {"channel_id": "C_GEN", "user_id": "U_PRIYA", "joined_at": "2026-01-05T09:05:00Z"}, {"channel_id": "C_GEN", "user_id": "U_DIEGO", "joined_at": "2026-01-05T09:05:00Z"}, {"channel_id": "C_GEN", "user_id": "U_AISHA", "joined_at": "2026-01-05T09:05:00Z"}, {"channel_id": "C_GEN", "user_id": "U_LEO", "joined_at": "2026-01-05T09:05:00Z"}, {"channel_id": "D_PRIYA", "user_id": "U01AGENBOT9", "joined_at": "2026-01-05T09:05:00Z"}, {"channel_id": "D_PRIYA", "user_id": "U_PRIYA", "joined_at": "2026-01-05T09:05:00Z"}], "messages": [{"message_id": "1789992000.000001", "channel_id": "C_OPS", "user_id": "U_PRIYA", "message_text": "Standup moves to 10:00 tomorrow.", "ts": "1789992000.000001"}, {"message_id": "1789992600.000002", "channel_id": "C_OPS", "user_id": "U01AGENBOT9", "message_text": "Reminder: freeze starts Friday.", "ts": "1789992600.000002"}, {"message_id": "1789993200.000003", "channel_id": "C_OPS", "user_id": "U_PRIYA", "message_text": "Launch day!", "ts": "1789993200.000003"}, {"message_id": "1789993800.000004", "channel_id": "C_OPS", "user_id": "U01AGENBOT9", "message_text": "Congrats!", "ts": "1789993800.000004", "parent_id": "1789993200.000003"}, {"message_id": "1785585600.000005", "channel_id": "C_LEG", "user_id": "U01AGENBOT9", "message_text": "Old note.", "ts": "1785585600.000005"}, {"message_id": "1790067600.000006", "channel_id": "D_PRIYA", "user_id": "U_PRIYA", "message_text": "Can you share the launch checklist?", "ts": "1790067600.000006"}], "message_reactions": [{"message_id": "1789993200.000003", "user_id": "U_PRIYA", "reaction_type": "tada"}, {"message_id": "1789993200.000003", "user_id": "U01AGENBOT9", "reaction_type": "eyes"}]}
