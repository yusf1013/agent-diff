You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Slack workspace:

    "Archive every channel that our workspace owner belongs to, that was created before March 2026, and that only has 5 members."

The user is Agent Bot. Below is every Slack channel in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "C_ATLAS",
  "channel_id": "C_ATLAS",
  "channel_name": "proj-atlas",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-02-10T12:00:00Z",
  "is_archived": false,
  "channel": "proj-atlas",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-02-10T12:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-02-10T04:00:00-08:00",
  "channel_members": [
   {
    "channel_id": "C_ATLAS",
    "user_id": "U01AGENBOT9",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_ATLAS",
    "user_id": "U_VICTOR",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_ATLAS",
    "user_id": "U_NINA",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_ATLAS",
    "user_id": "U_SAM",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_ATLAS",
    "user_id": "U_TARIQ",
    "joined_at": "2026-01-05T09:05:00Z"
   }
  ]
 },
 {
  "id": "C_FOUR",
  "channel_id": "C_FOUR",
  "channel_name": "proj-nova",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-02-05T12:00:00Z",
  "is_archived": false,
  "channel": "proj-nova",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-02-05T12:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-02-05T04:00:00-08:00",
  "channel_members": [
   {
    "channel_id": "C_FOUR",
    "user_id": "U01AGENBOT9",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_FOUR",
    "user_id": "U_VICTOR",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_FOUR",
    "user_id": "U_NINA",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_FOUR",
    "user_id": "U_SAM",
    "joined_at": "2026-01-05T09:05:00Z"
   }
  ]
 },
 {
  "id": "C_POSTERS",
  "channel_id": "C_POSTERS",
  "channel_name": "proj-comet",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-02-12T12:00:00Z",
  "is_archived": false,
  "channel": "proj-comet",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-02-12T12:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-02-12T04:00:00-08:00",
  "channel_members": [
   {
    "channel_id": "C_POSTERS",
    "user_id": "U01AGENBOT9",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_POSTERS",
    "user_id": "U_VICTOR",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_POSTERS",
    "user_id": "U_NINA",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_POSTERS",
    "user_id": "U_SAM",
    "joined_at": "2026-01-05T09:05:00Z"
   }
  ]
 },
 {
  "id": "C_LATE",
  "channel_id": "C_LATE",
  "channel_name": "proj-orion",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-03-04T12:00:00Z",
  "is_archived": false,
  "channel": "proj-orion",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-03-04T12:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-03-04T04:00:00-08:00",
  "channel_members": [
   {
    "channel_id": "C_LATE",
    "user_id": "U01AGENBOT9",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_LATE",
    "user_id": "U_VICTOR",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_LATE",
    "user_id": "U_NINA",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_LATE",
    "user_id": "U_SAM",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_LATE",
    "user_id": "U_TARIQ",
    "joined_at": "2026-01-05T09:05:00Z"
   }
  ]
 },
 {
  "id": "C_ADMIN",
  "channel_id": "C_ADMIN",
  "channel_name": "proj-vega",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-02-08T12:00:00Z",
  "is_archived": false,
  "channel": "proj-vega",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-02-08T12:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-02-08T04:00:00-08:00",
  "channel_members": [
   {
    "channel_id": "C_ADMIN",
    "user_id": "U01AGENBOT9",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_ADMIN",
    "user_id": "U_AMARA",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_ADMIN",
    "user_id": "U_NINA",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_ADMIN",
    "user_id": "U_SAM",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_ADMIN",
    "user_id": "U_TARIQ",
    "joined_at": "2026-01-05T09:05:00Z"
   }
  ]
 },
 {
  "id": "C_PLAIN",
  "channel_id": "C_PLAIN",
  "channel_name": "proj-lyra",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-02-15T12:00:00Z",
  "is_archived": false,
  "channel": "proj-lyra",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-02-15T12:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-02-15T04:00:00-08:00",
  "channel_members": [
   {
    "channel_id": "C_PLAIN",
    "user_id": "U01AGENBOT9",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_PLAIN",
    "user_id": "U_NINA",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_PLAIN",
    "user_id": "U_SAM",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_PLAIN",
    "user_id": "U_TARIQ",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_PLAIN",
    "user_id": "U_ELENA",
    "joined_at": "2026-01-05T09:05:00Z"
   }
  ]
 },
 {
  "id": "C_GENERAL",
  "channel_id": "C_GENERAL",
  "channel_name": "general",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-04-01T12:00:00Z",
  "is_archived": false,
  "channel": "general",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-04-01T12:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-04-01T05:00:00-07:00",
  "channel_members": [
   {
    "channel_id": "C_GENERAL",
    "user_id": "U01AGENBOT9",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_GENERAL",
    "user_id": "U_AMARA",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_GENERAL",
    "user_id": "U_ELENA",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_GENERAL",
    "user_id": "U_SAM",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_GENERAL",
    "user_id": "U_TARIQ",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_GENERAL",
    "user_id": "U_NINA",
    "joined_at": "2026-01-05T09:05:00Z"
   }
  ]
 },
 {
  "id": "C_RANDOM",
  "channel_id": "C_RANDOM",
  "channel_name": "watercooler",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-01T12:00:00Z",
  "is_archived": false,
  "channel": "watercooler",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-01T12:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-01T04:00:00-08:00",
  "channel_members": [
   {
    "channel_id": "C_RANDOM",
    "user_id": "U01AGENBOT9",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_RANDOM",
    "user_id": "U_ELENA",
    "joined_at": "2026-01-05T09:05:00Z"
   }
  ]
 },
 {
  "id": "C_ATLAS-sm1",
  "channel_id": "C_ATLAS-sm1",
  "channel_name": "proj-atlas",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-02-10T12:00:00Z",
  "is_archived": false,
  "channel": "proj-atlas",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-02-10T12:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-02-10T04:00:00-08:00",
  "channel_members": [
   {
    "channel_id": "C_ATLAS-sm1",
    "user_id": "U01AGENBOT9",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_ATLAS-sm1",
    "user_id": "U_VICTOR",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_ATLAS-sm1",
    "user_id": "U_NINA",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_ATLAS-sm1",
    "user_id": "U_SAM",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_ATLAS-sm1",
    "user_id": "U_TARIQ",
    "joined_at": "2026-01-05T09:05:00Z"
   }
  ]
 },
 {
  "id": "C_ATLAS-sm2",
  "channel_id": "C_ATLAS-sm2",
  "channel_name": "proj-atlas",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-02-10T12:00:00Z",
  "is_archived": false,
  "channel": "proj-atlas",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-02-10T12:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-02-10T04:00:00-08:00",
  "channel_members": [
   {
    "channel_id": "C_ATLAS-sm2",
    "user_id": "U01AGENBOT9",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_ATLAS-sm2",
    "user_id": "U_VICTOR",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_ATLAS-sm2",
    "user_id": "U_NINA",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_ATLAS-sm2",
    "user_id": "U_SAM",
    "joined_at": "2026-01-05T09:05:00Z"
   },
   {
    "channel_id": "C_ATLAS-sm2",
    "user_id": "U_TARIQ",
    "joined_at": "2026-01-05T09:05:00Z"
   }
  ]
 }
]
