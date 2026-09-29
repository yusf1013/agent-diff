You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Slack workspace:

    "React with :eyes: to every message Leo Park posted in #incidents on Tuesday."

The user is Agent Bot. Below is every Slack message in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "1790079000.000001",
  "message_id": "1790079000.000001",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rolled back the payment gateway config after the spike.",
  "ts": "1790079000.000001",
  "created_at": "2026-09-22T12:10:00Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T12:10:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T05:10:00-07:00",
  "users": [
   {
    "user_id": "U_LEO",
    "username": "leo.park",
    "email": "leo.park@northwind.example",
    "real_name": "Leo Park",
    "display_name": "Leo",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790076600.000002",
  "message_id": "1790076600.000002",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Anyone seeing elevated latency on checkout?",
  "ts": "1790076600.000002",
  "created_at": "2026-09-22T11:30:00Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:30:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:30:00-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790080800.000003",
  "message_id": "1790080800.000003",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "I'm looking into the DB connection pool now.",
  "ts": "1790080800.000003",
  "created_at": "2026-09-22T12:40:00Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T12:40:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T05:40:00-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790078400.000004",
  "message_id": "1790078400.000004",
  "channel_id": "C_ENG",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Standup notes: sprint burndown looks good.",
  "ts": "1790078400.000004",
  "created_at": "2026-09-22T12:00:00Z",
  "channel": "eng-standup",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T12:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T05:00:00-07:00",
  "users": [
   {
    "user_id": "U_LEO",
    "username": "leo.park",
    "email": "leo.park@northwind.example",
    "real_name": "Leo Park",
    "display_name": "Leo",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_ENG",
    "channel_name": "eng-standup",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790079600.000005",
  "message_id": "1790079600.000005",
  "channel_id": "C_WAR",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Escalating this to the payments team.",
  "ts": "1790079600.000005",
  "created_at": "2026-09-22T12:20:00Z",
  "channel": "war-room",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T12:20:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T05:20:00-07:00",
  "users": [
   {
    "user_id": "U_LEO",
    "username": "leo.park",
    "email": "leo.park@northwind.example",
    "real_name": "Leo Park",
    "display_name": "Leo",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_WAR",
    "channel_name": "war-room",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790164800.000006",
  "message_id": "1790164800.000006",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Wrapping up the post-incident review doc.",
  "ts": "1790164800.000006",
  "created_at": "2026-09-23T12:00:00Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T12:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T05:00:00-07:00",
  "users": [
   {
    "user_id": "U_LEO",
    "username": "leo.park",
    "email": "leo.park@northwind.example",
    "real_name": "Leo Park",
    "display_name": "Leo",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1789992000.000007",
  "message_id": "1789992000.000007",
  "channel_id": "C_ENG",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Sprint planning notes for next week.",
  "ts": "1789992000.000007",
  "created_at": "2026-09-21T12:00:00Z",
  "channel": "eng-standup",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:00:00-07:00",
  "users": [
   {
    "user_id": "U_PRIYA",
    "username": "priya.sharma",
    "email": "priya.sharma@northwind.example",
    "real_name": "Priya Sharma",
    "display_name": "Priya",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_ENG",
    "channel_name": "eng-standup",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790251200.000008",
  "message_id": "1790251200.000008",
  "channel_id": "C_WAR",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Scheduling the next deployment window.",
  "ts": "1790251200.000008",
  "created_at": "2026-09-24T12:00:00Z",
  "channel": "war-room",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T12:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T05:00:00-07:00",
  "users": [
   {
    "user_id": "U_MAYA",
    "username": "maya.chen",
    "email": "maya.chen@northwind.example",
    "real_name": "Maya Chen",
    "display_name": "Maya",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_WAR",
    "channel_name": "war-room",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790079060.000701",
  "message_id": "1790079060.000701",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Restarted the payment gateway workers after the errors.",
  "ts": "1790079060.000701",
  "created_at": "2026-09-22T12:11:00Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T12:11:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T05:11:00-07:00",
  "users": [
   {
    "user_id": "U_LEO",
    "username": "leo.park",
    "email": "leo.park@northwind.example",
    "real_name": "Leo Park",
    "display_name": "Leo",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790061000.000702",
  "message_id": "1790061000.000702",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Restarted the payment gateway workers after the errors.",
  "ts": "1790061000.000702",
  "created_at": "2026-09-22T07:10:00Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:10:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:10:00-07:00",
  "users": [
   {
    "user_id": "U_LEO",
    "username": "leo.park",
    "email": "leo.park@northwind.example",
    "real_name": "Leo Park",
    "display_name": "Leo",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790061160.000703",
  "message_id": "1790061160.000703",
  "ts": "1790061160.000703",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 1 passed.",
  "created_at": "2026-09-22T07:12:40Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:12:40+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:12:40-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790061321.000704",
  "message_id": "1790061321.000704",
  "ts": "1790061321.000704",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 2 passed.",
  "created_at": "2026-09-22T07:15:21Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:15:21+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:15:21-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790061482.000705",
  "message_id": "1790061482.000705",
  "ts": "1790061482.000705",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 3 passed.",
  "created_at": "2026-09-22T07:18:02Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:18:02+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:18:02-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790061642.000706",
  "message_id": "1790061642.000706",
  "ts": "1790061642.000706",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 4 passed.",
  "created_at": "2026-09-22T07:20:42Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:20:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:20:42-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790061803.000707",
  "message_id": "1790061803.000707",
  "ts": "1790061803.000707",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 5 passed.",
  "created_at": "2026-09-22T07:23:23Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:23:23+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:23:23-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790061964.000708",
  "message_id": "1790061964.000708",
  "ts": "1790061964.000708",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 6 passed.",
  "created_at": "2026-09-22T07:26:04Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:26:04+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:26:04-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790062125.000709",
  "message_id": "1790062125.000709",
  "ts": "1790062125.000709",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 7 passed.",
  "created_at": "2026-09-22T07:28:45Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:28:45+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:28:45-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790062285.000710",
  "message_id": "1790062285.000710",
  "ts": "1790062285.000710",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 8 passed.",
  "created_at": "2026-09-22T07:31:25Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:31:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:31:25-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790062446.000711",
  "message_id": "1790062446.000711",
  "ts": "1790062446.000711",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 9 passed.",
  "created_at": "2026-09-22T07:34:06Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:34:06+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:34:06-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790062607.000712",
  "message_id": "1790062607.000712",
  "ts": "1790062607.000712",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 10 passed.",
  "created_at": "2026-09-22T07:36:47Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:36:47+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:36:47-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790062767.000713",
  "message_id": "1790062767.000713",
  "ts": "1790062767.000713",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 11 passed.",
  "created_at": "2026-09-22T07:39:27Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:39:27+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:39:27-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790062928.000714",
  "message_id": "1790062928.000714",
  "ts": "1790062928.000714",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 12 passed.",
  "created_at": "2026-09-22T07:42:08Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:42:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:42:08-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790063089.000715",
  "message_id": "1790063089.000715",
  "ts": "1790063089.000715",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 13 passed.",
  "created_at": "2026-09-22T07:44:49Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:44:49+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:44:49-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790063250.000716",
  "message_id": "1790063250.000716",
  "ts": "1790063250.000716",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 14 passed.",
  "created_at": "2026-09-22T07:47:30Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:47:30+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:47:30-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790063410.000717",
  "message_id": "1790063410.000717",
  "ts": "1790063410.000717",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 15 passed.",
  "created_at": "2026-09-22T07:50:10Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:50:10+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:50:10-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790063571.000718",
  "message_id": "1790063571.000718",
  "ts": "1790063571.000718",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 16 passed.",
  "created_at": "2026-09-22T07:52:51Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:52:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:52:51-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790063732.000719",
  "message_id": "1790063732.000719",
  "ts": "1790063732.000719",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 17 passed.",
  "created_at": "2026-09-22T07:55:32Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:55:32+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:55:32-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790063892.000720",
  "message_id": "1790063892.000720",
  "ts": "1790063892.000720",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 18 passed.",
  "created_at": "2026-09-22T07:58:12Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:58:12+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:58:12-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790064053.000721",
  "message_id": "1790064053.000721",
  "ts": "1790064053.000721",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 19 passed.",
  "created_at": "2026-09-22T08:00:53Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:00:53+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:00:53-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790064214.000722",
  "message_id": "1790064214.000722",
  "ts": "1790064214.000722",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 20 passed.",
  "created_at": "2026-09-22T08:03:34Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:03:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:03:34-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790064375.000723",
  "message_id": "1790064375.000723",
  "ts": "1790064375.000723",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 21 passed.",
  "created_at": "2026-09-22T08:06:15Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:06:15+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:06:15-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790064535.000724",
  "message_id": "1790064535.000724",
  "ts": "1790064535.000724",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 22 passed.",
  "created_at": "2026-09-22T08:08:55Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:08:55+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:08:55-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790064696.000725",
  "message_id": "1790064696.000725",
  "ts": "1790064696.000725",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 23 passed.",
  "created_at": "2026-09-22T08:11:36Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:11:36+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:11:36-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790064857.000726",
  "message_id": "1790064857.000726",
  "ts": "1790064857.000726",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 24 passed.",
  "created_at": "2026-09-22T08:14:17Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:14:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:14:17-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790065017.000727",
  "message_id": "1790065017.000727",
  "ts": "1790065017.000727",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 25 passed.",
  "created_at": "2026-09-22T08:16:57Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:16:57+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:16:57-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790065178.000728",
  "message_id": "1790065178.000728",
  "ts": "1790065178.000728",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 26 passed.",
  "created_at": "2026-09-22T08:19:38Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:19:38+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:19:38-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790065339.000729",
  "message_id": "1790065339.000729",
  "ts": "1790065339.000729",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 27 passed.",
  "created_at": "2026-09-22T08:22:19Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:22:19+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:22:19-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790065500.000730",
  "message_id": "1790065500.000730",
  "ts": "1790065500.000730",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 28 passed.",
  "created_at": "2026-09-22T08:25:00Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:25:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:25:00-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790065660.000731",
  "message_id": "1790065660.000731",
  "ts": "1790065660.000731",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 29 passed.",
  "created_at": "2026-09-22T08:27:40Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:27:40+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:27:40-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790065821.000732",
  "message_id": "1790065821.000732",
  "ts": "1790065821.000732",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 30 passed.",
  "created_at": "2026-09-22T08:30:21Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:30:21+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:30:21-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790065982.000733",
  "message_id": "1790065982.000733",
  "ts": "1790065982.000733",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 31 passed.",
  "created_at": "2026-09-22T08:33:02Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:33:02+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:33:02-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790066142.000734",
  "message_id": "1790066142.000734",
  "ts": "1790066142.000734",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 32 passed.",
  "created_at": "2026-09-22T08:35:42Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:35:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:35:42-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790066303.000735",
  "message_id": "1790066303.000735",
  "ts": "1790066303.000735",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 33 passed.",
  "created_at": "2026-09-22T08:38:23Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:38:23+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:38:23-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790066464.000736",
  "message_id": "1790066464.000736",
  "ts": "1790066464.000736",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 34 passed.",
  "created_at": "2026-09-22T08:41:04Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:41:04+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:41:04-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790066625.000737",
  "message_id": "1790066625.000737",
  "ts": "1790066625.000737",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 35 passed.",
  "created_at": "2026-09-22T08:43:45Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:43:45+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:43:45-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790066785.000738",
  "message_id": "1790066785.000738",
  "ts": "1790066785.000738",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 36 passed.",
  "created_at": "2026-09-22T08:46:25Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:46:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:46:25-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790066946.000739",
  "message_id": "1790066946.000739",
  "ts": "1790066946.000739",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 37 passed.",
  "created_at": "2026-09-22T08:49:06Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:49:06+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:49:06-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790067107.000740",
  "message_id": "1790067107.000740",
  "ts": "1790067107.000740",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 38 passed.",
  "created_at": "2026-09-22T08:51:47Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:51:47+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:51:47-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790067267.000741",
  "message_id": "1790067267.000741",
  "ts": "1790067267.000741",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 39 passed.",
  "created_at": "2026-09-22T08:54:27Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:54:27+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:54:27-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790067428.000742",
  "message_id": "1790067428.000742",
  "ts": "1790067428.000742",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 40 passed.",
  "created_at": "2026-09-22T08:57:08Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:57:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:57:08-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790067589.000743",
  "message_id": "1790067589.000743",
  "ts": "1790067589.000743",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 41 passed.",
  "created_at": "2026-09-22T08:59:49Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:59:49+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:59:49-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790067750.000744",
  "message_id": "1790067750.000744",
  "ts": "1790067750.000744",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 42 passed.",
  "created_at": "2026-09-22T09:02:30Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:02:30+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:02:30-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790067910.000745",
  "message_id": "1790067910.000745",
  "ts": "1790067910.000745",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 43 passed.",
  "created_at": "2026-09-22T09:05:10Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:05:10+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:05:10-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790068071.000746",
  "message_id": "1790068071.000746",
  "ts": "1790068071.000746",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 44 passed.",
  "created_at": "2026-09-22T09:07:51Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:07:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:07:51-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790068232.000747",
  "message_id": "1790068232.000747",
  "ts": "1790068232.000747",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 45 passed.",
  "created_at": "2026-09-22T09:10:32Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:10:32+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:10:32-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790068392.000748",
  "message_id": "1790068392.000748",
  "ts": "1790068392.000748",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 46 passed.",
  "created_at": "2026-09-22T09:13:12Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:13:12+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:13:12-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790068553.000749",
  "message_id": "1790068553.000749",
  "ts": "1790068553.000749",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 47 passed.",
  "created_at": "2026-09-22T09:15:53Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:15:53+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:15:53-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790068714.000750",
  "message_id": "1790068714.000750",
  "ts": "1790068714.000750",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 48 passed.",
  "created_at": "2026-09-22T09:18:34Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:18:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:18:34-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790068875.000751",
  "message_id": "1790068875.000751",
  "ts": "1790068875.000751",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 49 passed.",
  "created_at": "2026-09-22T09:21:15Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:21:15+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:21:15-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790069035.000752",
  "message_id": "1790069035.000752",
  "ts": "1790069035.000752",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 50 passed.",
  "created_at": "2026-09-22T09:23:55Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:23:55+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:23:55-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790069196.000753",
  "message_id": "1790069196.000753",
  "ts": "1790069196.000753",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 51 passed.",
  "created_at": "2026-09-22T09:26:36Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:26:36+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:26:36-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790069357.000754",
  "message_id": "1790069357.000754",
  "ts": "1790069357.000754",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 52 passed.",
  "created_at": "2026-09-22T09:29:17Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:29:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:29:17-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790069517.000755",
  "message_id": "1790069517.000755",
  "ts": "1790069517.000755",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 53 passed.",
  "created_at": "2026-09-22T09:31:57Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:31:57+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:31:57-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790069678.000756",
  "message_id": "1790069678.000756",
  "ts": "1790069678.000756",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 54 passed.",
  "created_at": "2026-09-22T09:34:38Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:34:38+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:34:38-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790069839.000757",
  "message_id": "1790069839.000757",
  "ts": "1790069839.000757",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 55 passed.",
  "created_at": "2026-09-22T09:37:19Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:37:19+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:37:19-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790070000.000758",
  "message_id": "1790070000.000758",
  "ts": "1790070000.000758",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 56 passed.",
  "created_at": "2026-09-22T09:40:00Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:40:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:40:00-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790070160.000759",
  "message_id": "1790070160.000759",
  "ts": "1790070160.000759",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 57 passed.",
  "created_at": "2026-09-22T09:42:40Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:42:40+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:42:40-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790070321.000760",
  "message_id": "1790070321.000760",
  "ts": "1790070321.000760",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 58 passed.",
  "created_at": "2026-09-22T09:45:21Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:45:21+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:45:21-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790070482.000761",
  "message_id": "1790070482.000761",
  "ts": "1790070482.000761",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 59 passed.",
  "created_at": "2026-09-22T09:48:02Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:48:02+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:48:02-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790070642.000762",
  "message_id": "1790070642.000762",
  "ts": "1790070642.000762",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 60 passed.",
  "created_at": "2026-09-22T09:50:42Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:50:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:50:42-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790070803.000763",
  "message_id": "1790070803.000763",
  "ts": "1790070803.000763",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 61 passed.",
  "created_at": "2026-09-22T09:53:23Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:53:23+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:53:23-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790070964.000764",
  "message_id": "1790070964.000764",
  "ts": "1790070964.000764",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 62 passed.",
  "created_at": "2026-09-22T09:56:04Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:56:04+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:56:04-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790071125.000765",
  "message_id": "1790071125.000765",
  "ts": "1790071125.000765",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 63 passed.",
  "created_at": "2026-09-22T09:58:45Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:58:45+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:58:45-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790071285.000766",
  "message_id": "1790071285.000766",
  "ts": "1790071285.000766",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 64 passed.",
  "created_at": "2026-09-22T10:01:25Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:01:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:01:25-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790071446.000767",
  "message_id": "1790071446.000767",
  "ts": "1790071446.000767",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 65 passed.",
  "created_at": "2026-09-22T10:04:06Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:04:06+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:04:06-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790071607.000768",
  "message_id": "1790071607.000768",
  "ts": "1790071607.000768",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 66 passed.",
  "created_at": "2026-09-22T10:06:47Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:06:47+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:06:47-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790071767.000769",
  "message_id": "1790071767.000769",
  "ts": "1790071767.000769",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 67 passed.",
  "created_at": "2026-09-22T10:09:27Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:09:27+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:09:27-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790071928.000770",
  "message_id": "1790071928.000770",
  "ts": "1790071928.000770",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 68 passed.",
  "created_at": "2026-09-22T10:12:08Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:12:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:12:08-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790072089.000771",
  "message_id": "1790072089.000771",
  "ts": "1790072089.000771",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 69 passed.",
  "created_at": "2026-09-22T10:14:49Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:14:49+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:14:49-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790072250.000772",
  "message_id": "1790072250.000772",
  "ts": "1790072250.000772",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 70 passed.",
  "created_at": "2026-09-22T10:17:30Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:17:30+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:17:30-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790072410.000773",
  "message_id": "1790072410.000773",
  "ts": "1790072410.000773",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 71 passed.",
  "created_at": "2026-09-22T10:20:10Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:20:10+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:20:10-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790072571.000774",
  "message_id": "1790072571.000774",
  "ts": "1790072571.000774",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 72 passed.",
  "created_at": "2026-09-22T10:22:51Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:22:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:22:51-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790072732.000775",
  "message_id": "1790072732.000775",
  "ts": "1790072732.000775",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 73 passed.",
  "created_at": "2026-09-22T10:25:32Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:25:32+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:25:32-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790072892.000776",
  "message_id": "1790072892.000776",
  "ts": "1790072892.000776",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 74 passed.",
  "created_at": "2026-09-22T10:28:12Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:28:12+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:28:12-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790073053.000777",
  "message_id": "1790073053.000777",
  "ts": "1790073053.000777",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 75 passed.",
  "created_at": "2026-09-22T10:30:53Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:30:53+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:30:53-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790073214.000778",
  "message_id": "1790073214.000778",
  "ts": "1790073214.000778",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 76 passed.",
  "created_at": "2026-09-22T10:33:34Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:33:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:33:34-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790073375.000779",
  "message_id": "1790073375.000779",
  "ts": "1790073375.000779",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 77 passed.",
  "created_at": "2026-09-22T10:36:15Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:36:15+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:36:15-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790073535.000780",
  "message_id": "1790073535.000780",
  "ts": "1790073535.000780",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 78 passed.",
  "created_at": "2026-09-22T10:38:55Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:38:55+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:38:55-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790073696.000781",
  "message_id": "1790073696.000781",
  "ts": "1790073696.000781",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 79 passed.",
  "created_at": "2026-09-22T10:41:36Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:41:36+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:41:36-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790073857.000782",
  "message_id": "1790073857.000782",
  "ts": "1790073857.000782",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 80 passed.",
  "created_at": "2026-09-22T10:44:17Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:44:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:44:17-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790074017.000783",
  "message_id": "1790074017.000783",
  "ts": "1790074017.000783",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 81 passed.",
  "created_at": "2026-09-22T10:46:57Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:46:57+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:46:57-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790074178.000784",
  "message_id": "1790074178.000784",
  "ts": "1790074178.000784",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 82 passed.",
  "created_at": "2026-09-22T10:49:38Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:49:38+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:49:38-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790074339.000785",
  "message_id": "1790074339.000785",
  "ts": "1790074339.000785",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 83 passed.",
  "created_at": "2026-09-22T10:52:19Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:52:19+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:52:19-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790074500.000786",
  "message_id": "1790074500.000786",
  "ts": "1790074500.000786",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 84 passed.",
  "created_at": "2026-09-22T10:55:00Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:55:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:55:00-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790074660.000787",
  "message_id": "1790074660.000787",
  "ts": "1790074660.000787",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 85 passed.",
  "created_at": "2026-09-22T10:57:40Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:57:40+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:57:40-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790074821.000788",
  "message_id": "1790074821.000788",
  "ts": "1790074821.000788",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 86 passed.",
  "created_at": "2026-09-22T11:00:21Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:00:21+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:00:21-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790074982.000789",
  "message_id": "1790074982.000789",
  "ts": "1790074982.000789",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 87 passed.",
  "created_at": "2026-09-22T11:03:02Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:03:02+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:03:02-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790075142.000790",
  "message_id": "1790075142.000790",
  "ts": "1790075142.000790",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 88 passed.",
  "created_at": "2026-09-22T11:05:42Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:05:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:05:42-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790075303.000791",
  "message_id": "1790075303.000791",
  "ts": "1790075303.000791",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 89 passed.",
  "created_at": "2026-09-22T11:08:23Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:08:23+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:08:23-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790075464.000792",
  "message_id": "1790075464.000792",
  "ts": "1790075464.000792",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 90 passed.",
  "created_at": "2026-09-22T11:11:04Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:11:04+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:11:04-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790075625.000793",
  "message_id": "1790075625.000793",
  "ts": "1790075625.000793",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 91 passed.",
  "created_at": "2026-09-22T11:13:45Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:13:45+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:13:45-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790075785.000794",
  "message_id": "1790075785.000794",
  "ts": "1790075785.000794",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 92 passed.",
  "created_at": "2026-09-22T11:16:25Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:16:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:16:25-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790075946.000795",
  "message_id": "1790075946.000795",
  "ts": "1790075946.000795",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 93 passed.",
  "created_at": "2026-09-22T11:19:06Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:19:06+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:19:06-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790076107.000796",
  "message_id": "1790076107.000796",
  "ts": "1790076107.000796",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 94 passed.",
  "created_at": "2026-09-22T11:21:47Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:21:47+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:21:47-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790076267.000797",
  "message_id": "1790076267.000797",
  "ts": "1790076267.000797",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 95 passed.",
  "created_at": "2026-09-22T11:24:27Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:24:27+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:24:27-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790076428.000798",
  "message_id": "1790076428.000798",
  "ts": "1790076428.000798",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 96 passed.",
  "created_at": "2026-09-22T11:27:08Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:27:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:27:08-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790076589.000799",
  "message_id": "1790076589.000799",
  "ts": "1790076589.000799",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 97 passed.",
  "created_at": "2026-09-22T11:29:49Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:29:49+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:29:49-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790076750.000800",
  "message_id": "1790076750.000800",
  "ts": "1790076750.000800",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 98 passed.",
  "created_at": "2026-09-22T11:32:30Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:32:30+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:32:30-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790076910.000801",
  "message_id": "1790076910.000801",
  "ts": "1790076910.000801",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 99 passed.",
  "created_at": "2026-09-22T11:35:10Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:35:10+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:35:10-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790077071.000802",
  "message_id": "1790077071.000802",
  "ts": "1790077071.000802",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 100 passed.",
  "created_at": "2026-09-22T11:37:51Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:37:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:37:51-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790077232.000803",
  "message_id": "1790077232.000803",
  "ts": "1790077232.000803",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 101 passed.",
  "created_at": "2026-09-22T11:40:32Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:40:32+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:40:32-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790077392.000804",
  "message_id": "1790077392.000804",
  "ts": "1790077392.000804",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 102 passed.",
  "created_at": "2026-09-22T11:43:12Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:43:12+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:43:12-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790077553.000805",
  "message_id": "1790077553.000805",
  "ts": "1790077553.000805",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 103 passed.",
  "created_at": "2026-09-22T11:45:53Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:45:53+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:45:53-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790077714.000806",
  "message_id": "1790077714.000806",
  "ts": "1790077714.000806",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 104 passed.",
  "created_at": "2026-09-22T11:48:34Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:48:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:48:34-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790077875.000807",
  "message_id": "1790077875.000807",
  "ts": "1790077875.000807",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 105 passed.",
  "created_at": "2026-09-22T11:51:15Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:51:15+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:51:15-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790078035.000808",
  "message_id": "1790078035.000808",
  "ts": "1790078035.000808",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 106 passed.",
  "created_at": "2026-09-22T11:53:55Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:53:55+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:53:55-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790078196.000809",
  "message_id": "1790078196.000809",
  "ts": "1790078196.000809",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 107 passed.",
  "created_at": "2026-09-22T11:56:36Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:56:36+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:56:36-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790078357.000810",
  "message_id": "1790078357.000810",
  "ts": "1790078357.000810",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway check 108 passed.",
  "created_at": "2026-09-22T11:59:17Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:59:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:59:17-07:00",
  "users": [
   {
    "user_id": "U_OMAR",
    "username": "omar.haddad",
    "email": "omar.haddad@northwind.example",
    "real_name": "Omar Haddad",
    "display_name": "Omar",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790078517.000811",
  "message_id": "1790078517.000811",
  "ts": "1790078517.000811",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payment gateway check 109 passed.",
  "created_at": "2026-09-22T12:01:57Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T12:01:57+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T05:01:57-07:00",
  "users": [
   {
    "user_id": "U01AGENBOT9",
    "username": "agentbot",
    "email": "agentbot@northwind.example",
    "real_name": "Agent Bot",
    "display_name": "AgentBot",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": true,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790078678.000812",
  "message_id": "1790078678.000812",
  "ts": "1790078678.000812",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway check 110 passed.",
  "created_at": "2026-09-22T12:04:38Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T12:04:38+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T05:04:38-07:00",
  "users": [
   {
    "user_id": "U_DIEGO",
    "username": "diego.alvarez",
    "email": "diego.alvarez@northwind.example",
    "real_name": "Diego Alvarez",
    "display_name": "Diego",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 }
]
