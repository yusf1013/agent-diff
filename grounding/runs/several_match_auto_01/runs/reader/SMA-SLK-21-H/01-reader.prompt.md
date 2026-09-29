You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Slack workspace:

    "Add a :thumbsup: reaction to every message Priya Sharma posted in #deploys on September 23 about the rollback."

The user is Agent Bot. Below is every Slack message in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "1790154000.000001",
  "message_id": "1790154000.000001",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Deploying web 4.12 to production.",
  "ts": "1790154000.000001",
  "created_at": "2026-09-23T09:00:00Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T02:00:00-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790164800.000002",
  "message_id": "1790164800.000002",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Rollback of payments-api finished; error rates are back to normal.",
  "ts": "1790164800.000002",
  "created_at": "2026-09-23T12:00:00Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T12:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T05:00:00-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790166000.000003",
  "message_id": "1790166000.000003",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "<@U_PRIYA> the search-api rollback is done on my side.",
  "ts": "1790166000.000003",
  "created_at": "2026-09-23T12:20:00Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T12:20:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T05:20:00-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
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
  "channel_id": "C_DEPLOYS",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Rollback plan for the cache migration is ready for review.",
  "ts": "1790078400.000004",
  "created_at": "2026-09-22T12:00:00Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T12:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T05:00:00-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790165400.000005",
  "message_id": "1790165400.000005",
  "channel_id": "C_DEPSTG",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Rollback on staging went through cleanly.",
  "ts": "1790165400.000005",
  "created_at": "2026-09-23T12:10:00Z",
  "channel": "deploys-staging",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T12:10:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T05:10:00-07:00",
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
    "channel_id": "C_DEPSTG",
    "channel_name": "deploys-staging",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790166600.000006",
  "message_id": "1790166600.000006",
  "channel_id": "C_GENERAL",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "FYI: the billing rollback is complete.",
  "ts": "1790166600.000006",
  "created_at": "2026-09-23T12:30:00Z",
  "channel": "general",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T12:30:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T05:30:00-07:00",
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
    "channel_id": "C_GENERAL",
    "channel_name": "general",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790164860.000701",
  "message_id": "1790164860.000701",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Rollback of payments-api done; checkout errors have dropped to normal.",
  "ts": "1790164860.000701",
  "created_at": "2026-09-23T12:01:00Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T12:01:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T05:01:00-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790147400.000702",
  "message_id": "1790147400.000702",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Rollback of payments-api done; checkout errors have dropped to normal.",
  "ts": "1790147400.000702",
  "created_at": "2026-09-23T07:10:00Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T07:10:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T00:10:00-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790147555.000703",
  "message_id": "1790147555.000703",
  "ts": "1790147555.000703",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 1 passed.",
  "created_at": "2026-09-23T07:12:35Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T07:12:35+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T00:12:35-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790147710.000704",
  "message_id": "1790147710.000704",
  "ts": "1790147710.000704",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 2 passed.",
  "created_at": "2026-09-23T07:15:10Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T07:15:10+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T00:15:10-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790147866.000705",
  "message_id": "1790147866.000705",
  "ts": "1790147866.000705",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 3 passed.",
  "created_at": "2026-09-23T07:17:46Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T07:17:46+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T00:17:46-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790148021.000706",
  "message_id": "1790148021.000706",
  "ts": "1790148021.000706",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 4 passed.",
  "created_at": "2026-09-23T07:20:21Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T07:20:21+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T00:20:21-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790148176.000707",
  "message_id": "1790148176.000707",
  "ts": "1790148176.000707",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 5 passed.",
  "created_at": "2026-09-23T07:22:56Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T07:22:56+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T00:22:56-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790148332.000708",
  "message_id": "1790148332.000708",
  "ts": "1790148332.000708",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 6 passed.",
  "created_at": "2026-09-23T07:25:32Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T07:25:32+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T00:25:32-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790148487.000709",
  "message_id": "1790148487.000709",
  "ts": "1790148487.000709",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 7 passed.",
  "created_at": "2026-09-23T07:28:07Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T07:28:07+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T00:28:07-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790148642.000710",
  "message_id": "1790148642.000710",
  "ts": "1790148642.000710",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 8 passed.",
  "created_at": "2026-09-23T07:30:42Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T07:30:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T00:30:42-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790148798.000711",
  "message_id": "1790148798.000711",
  "ts": "1790148798.000711",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 9 passed.",
  "created_at": "2026-09-23T07:33:18Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T07:33:18+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T00:33:18-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790148953.000712",
  "message_id": "1790148953.000712",
  "ts": "1790148953.000712",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 10 passed.",
  "created_at": "2026-09-23T07:35:53Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T07:35:53+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T00:35:53-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790149108.000713",
  "message_id": "1790149108.000713",
  "ts": "1790149108.000713",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 11 passed.",
  "created_at": "2026-09-23T07:38:28Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T07:38:28+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T00:38:28-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790149264.000714",
  "message_id": "1790149264.000714",
  "ts": "1790149264.000714",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 12 passed.",
  "created_at": "2026-09-23T07:41:04Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T07:41:04+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T00:41:04-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790149419.000715",
  "message_id": "1790149419.000715",
  "ts": "1790149419.000715",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 13 passed.",
  "created_at": "2026-09-23T07:43:39Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T07:43:39+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T00:43:39-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790149575.000716",
  "message_id": "1790149575.000716",
  "ts": "1790149575.000716",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 14 passed.",
  "created_at": "2026-09-23T07:46:15Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T07:46:15+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T00:46:15-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790149730.000717",
  "message_id": "1790149730.000717",
  "ts": "1790149730.000717",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 15 passed.",
  "created_at": "2026-09-23T07:48:50Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T07:48:50+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T00:48:50-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790149885.000718",
  "message_id": "1790149885.000718",
  "ts": "1790149885.000718",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 16 passed.",
  "created_at": "2026-09-23T07:51:25Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T07:51:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T00:51:25-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790150041.000719",
  "message_id": "1790150041.000719",
  "ts": "1790150041.000719",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 17 passed.",
  "created_at": "2026-09-23T07:54:01Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T07:54:01+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T00:54:01-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790150196.000720",
  "message_id": "1790150196.000720",
  "ts": "1790150196.000720",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 18 passed.",
  "created_at": "2026-09-23T07:56:36Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T07:56:36+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T00:56:36-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790150351.000721",
  "message_id": "1790150351.000721",
  "ts": "1790150351.000721",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 19 passed.",
  "created_at": "2026-09-23T07:59:11Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T07:59:11+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T00:59:11-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790150507.000722",
  "message_id": "1790150507.000722",
  "ts": "1790150507.000722",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 20 passed.",
  "created_at": "2026-09-23T08:01:47Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T08:01:47+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T01:01:47-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790150662.000723",
  "message_id": "1790150662.000723",
  "ts": "1790150662.000723",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 21 passed.",
  "created_at": "2026-09-23T08:04:22Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T08:04:22+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T01:04:22-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790150817.000724",
  "message_id": "1790150817.000724",
  "ts": "1790150817.000724",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 22 passed.",
  "created_at": "2026-09-23T08:06:57Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T08:06:57+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T01:06:57-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790150973.000725",
  "message_id": "1790150973.000725",
  "ts": "1790150973.000725",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 23 passed.",
  "created_at": "2026-09-23T08:09:33Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T08:09:33+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T01:09:33-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790151128.000726",
  "message_id": "1790151128.000726",
  "ts": "1790151128.000726",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 24 passed.",
  "created_at": "2026-09-23T08:12:08Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T08:12:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T01:12:08-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790151283.000727",
  "message_id": "1790151283.000727",
  "ts": "1790151283.000727",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 25 passed.",
  "created_at": "2026-09-23T08:14:43Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T08:14:43+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T01:14:43-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790151439.000728",
  "message_id": "1790151439.000728",
  "ts": "1790151439.000728",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 26 passed.",
  "created_at": "2026-09-23T08:17:19Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T08:17:19+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T01:17:19-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790151594.000729",
  "message_id": "1790151594.000729",
  "ts": "1790151594.000729",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 27 passed.",
  "created_at": "2026-09-23T08:19:54Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T08:19:54+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T01:19:54-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790151750.000730",
  "message_id": "1790151750.000730",
  "ts": "1790151750.000730",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 28 passed.",
  "created_at": "2026-09-23T08:22:30Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T08:22:30+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T01:22:30-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790151905.000731",
  "message_id": "1790151905.000731",
  "ts": "1790151905.000731",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 29 passed.",
  "created_at": "2026-09-23T08:25:05Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T08:25:05+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T01:25:05-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790152060.000732",
  "message_id": "1790152060.000732",
  "ts": "1790152060.000732",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 30 passed.",
  "created_at": "2026-09-23T08:27:40Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T08:27:40+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T01:27:40-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790152216.000733",
  "message_id": "1790152216.000733",
  "ts": "1790152216.000733",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 31 passed.",
  "created_at": "2026-09-23T08:30:16Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T08:30:16+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T01:30:16-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790152371.000734",
  "message_id": "1790152371.000734",
  "ts": "1790152371.000734",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 32 passed.",
  "created_at": "2026-09-23T08:32:51Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T08:32:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T01:32:51-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790152526.000735",
  "message_id": "1790152526.000735",
  "ts": "1790152526.000735",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 33 passed.",
  "created_at": "2026-09-23T08:35:26Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T08:35:26+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T01:35:26-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790152682.000736",
  "message_id": "1790152682.000736",
  "ts": "1790152682.000736",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 34 passed.",
  "created_at": "2026-09-23T08:38:02Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T08:38:02+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T01:38:02-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790152837.000737",
  "message_id": "1790152837.000737",
  "ts": "1790152837.000737",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 35 passed.",
  "created_at": "2026-09-23T08:40:37Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T08:40:37+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T01:40:37-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790152992.000738",
  "message_id": "1790152992.000738",
  "ts": "1790152992.000738",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 36 passed.",
  "created_at": "2026-09-23T08:43:12Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T08:43:12+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T01:43:12-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790153148.000739",
  "message_id": "1790153148.000739",
  "ts": "1790153148.000739",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 37 passed.",
  "created_at": "2026-09-23T08:45:48Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T08:45:48+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T01:45:48-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790153303.000740",
  "message_id": "1790153303.000740",
  "ts": "1790153303.000740",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 38 passed.",
  "created_at": "2026-09-23T08:48:23Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T08:48:23+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T01:48:23-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790153458.000741",
  "message_id": "1790153458.000741",
  "ts": "1790153458.000741",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 39 passed.",
  "created_at": "2026-09-23T08:50:58Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T08:50:58+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T01:50:58-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790153614.000742",
  "message_id": "1790153614.000742",
  "ts": "1790153614.000742",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 40 passed.",
  "created_at": "2026-09-23T08:53:34Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T08:53:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T01:53:34-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790153769.000743",
  "message_id": "1790153769.000743",
  "ts": "1790153769.000743",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 41 passed.",
  "created_at": "2026-09-23T08:56:09Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T08:56:09+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T01:56:09-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790153925.000744",
  "message_id": "1790153925.000744",
  "ts": "1790153925.000744",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 42 passed.",
  "created_at": "2026-09-23T08:58:45Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T08:58:45+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T01:58:45-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790154080.000745",
  "message_id": "1790154080.000745",
  "ts": "1790154080.000745",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 43 passed.",
  "created_at": "2026-09-23T09:01:20Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T09:01:20+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T02:01:20-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790154235.000746",
  "message_id": "1790154235.000746",
  "ts": "1790154235.000746",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 44 passed.",
  "created_at": "2026-09-23T09:03:55Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T09:03:55+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T02:03:55-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790154391.000747",
  "message_id": "1790154391.000747",
  "ts": "1790154391.000747",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 45 passed.",
  "created_at": "2026-09-23T09:06:31Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T09:06:31+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T02:06:31-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790154546.000748",
  "message_id": "1790154546.000748",
  "ts": "1790154546.000748",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 46 passed.",
  "created_at": "2026-09-23T09:09:06Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T09:09:06+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T02:09:06-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790154701.000749",
  "message_id": "1790154701.000749",
  "ts": "1790154701.000749",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 47 passed.",
  "created_at": "2026-09-23T09:11:41Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T09:11:41+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T02:11:41-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790154857.000750",
  "message_id": "1790154857.000750",
  "ts": "1790154857.000750",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 48 passed.",
  "created_at": "2026-09-23T09:14:17Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T09:14:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T02:14:17-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790155012.000751",
  "message_id": "1790155012.000751",
  "ts": "1790155012.000751",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 49 passed.",
  "created_at": "2026-09-23T09:16:52Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T09:16:52+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T02:16:52-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790155167.000752",
  "message_id": "1790155167.000752",
  "ts": "1790155167.000752",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 50 passed.",
  "created_at": "2026-09-23T09:19:27Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T09:19:27+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T02:19:27-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790155323.000753",
  "message_id": "1790155323.000753",
  "ts": "1790155323.000753",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 51 passed.",
  "created_at": "2026-09-23T09:22:03Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T09:22:03+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T02:22:03-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790155478.000754",
  "message_id": "1790155478.000754",
  "ts": "1790155478.000754",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 52 passed.",
  "created_at": "2026-09-23T09:24:38Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T09:24:38+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T02:24:38-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790155633.000755",
  "message_id": "1790155633.000755",
  "ts": "1790155633.000755",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 53 passed.",
  "created_at": "2026-09-23T09:27:13Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T09:27:13+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T02:27:13-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790155789.000756",
  "message_id": "1790155789.000756",
  "ts": "1790155789.000756",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 54 passed.",
  "created_at": "2026-09-23T09:29:49Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T09:29:49+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T02:29:49-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790155944.000757",
  "message_id": "1790155944.000757",
  "ts": "1790155944.000757",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 55 passed.",
  "created_at": "2026-09-23T09:32:24Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T09:32:24+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T02:32:24-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790156100.000758",
  "message_id": "1790156100.000758",
  "ts": "1790156100.000758",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 56 passed.",
  "created_at": "2026-09-23T09:35:00Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T09:35:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T02:35:00-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790156255.000759",
  "message_id": "1790156255.000759",
  "ts": "1790156255.000759",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 57 passed.",
  "created_at": "2026-09-23T09:37:35Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T09:37:35+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T02:37:35-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790156410.000760",
  "message_id": "1790156410.000760",
  "ts": "1790156410.000760",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 58 passed.",
  "created_at": "2026-09-23T09:40:10Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T09:40:10+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T02:40:10-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790156566.000761",
  "message_id": "1790156566.000761",
  "ts": "1790156566.000761",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 59 passed.",
  "created_at": "2026-09-23T09:42:46Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T09:42:46+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T02:42:46-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790156721.000762",
  "message_id": "1790156721.000762",
  "ts": "1790156721.000762",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 60 passed.",
  "created_at": "2026-09-23T09:45:21Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T09:45:21+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T02:45:21-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790156876.000763",
  "message_id": "1790156876.000763",
  "ts": "1790156876.000763",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 61 passed.",
  "created_at": "2026-09-23T09:47:56Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T09:47:56+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T02:47:56-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790157032.000764",
  "message_id": "1790157032.000764",
  "ts": "1790157032.000764",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 62 passed.",
  "created_at": "2026-09-23T09:50:32Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T09:50:32+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T02:50:32-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790157187.000765",
  "message_id": "1790157187.000765",
  "ts": "1790157187.000765",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 63 passed.",
  "created_at": "2026-09-23T09:53:07Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T09:53:07+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T02:53:07-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790157342.000766",
  "message_id": "1790157342.000766",
  "ts": "1790157342.000766",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 64 passed.",
  "created_at": "2026-09-23T09:55:42Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T09:55:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T02:55:42-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790157498.000767",
  "message_id": "1790157498.000767",
  "ts": "1790157498.000767",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 65 passed.",
  "created_at": "2026-09-23T09:58:18Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T09:58:18+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T02:58:18-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790157653.000768",
  "message_id": "1790157653.000768",
  "ts": "1790157653.000768",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 66 passed.",
  "created_at": "2026-09-23T10:00:53Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T10:00:53+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T03:00:53-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790157808.000769",
  "message_id": "1790157808.000769",
  "ts": "1790157808.000769",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 67 passed.",
  "created_at": "2026-09-23T10:03:28Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T10:03:28+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T03:03:28-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790157964.000770",
  "message_id": "1790157964.000770",
  "ts": "1790157964.000770",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 68 passed.",
  "created_at": "2026-09-23T10:06:04Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T10:06:04+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T03:06:04-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790158119.000771",
  "message_id": "1790158119.000771",
  "ts": "1790158119.000771",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 69 passed.",
  "created_at": "2026-09-23T10:08:39Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T10:08:39+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T03:08:39-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790158275.000772",
  "message_id": "1790158275.000772",
  "ts": "1790158275.000772",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 70 passed.",
  "created_at": "2026-09-23T10:11:15Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T10:11:15+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T03:11:15-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790158430.000773",
  "message_id": "1790158430.000773",
  "ts": "1790158430.000773",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 71 passed.",
  "created_at": "2026-09-23T10:13:50Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T10:13:50+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T03:13:50-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790158585.000774",
  "message_id": "1790158585.000774",
  "ts": "1790158585.000774",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 72 passed.",
  "created_at": "2026-09-23T10:16:25Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T10:16:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T03:16:25-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790158741.000775",
  "message_id": "1790158741.000775",
  "ts": "1790158741.000775",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 73 passed.",
  "created_at": "2026-09-23T10:19:01Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T10:19:01+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T03:19:01-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790158896.000776",
  "message_id": "1790158896.000776",
  "ts": "1790158896.000776",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 74 passed.",
  "created_at": "2026-09-23T10:21:36Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T10:21:36+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T03:21:36-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790159051.000777",
  "message_id": "1790159051.000777",
  "ts": "1790159051.000777",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 75 passed.",
  "created_at": "2026-09-23T10:24:11Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T10:24:11+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T03:24:11-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790159207.000778",
  "message_id": "1790159207.000778",
  "ts": "1790159207.000778",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 76 passed.",
  "created_at": "2026-09-23T10:26:47Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T10:26:47+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T03:26:47-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790159362.000779",
  "message_id": "1790159362.000779",
  "ts": "1790159362.000779",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 77 passed.",
  "created_at": "2026-09-23T10:29:22Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T10:29:22+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T03:29:22-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790159517.000780",
  "message_id": "1790159517.000780",
  "ts": "1790159517.000780",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 78 passed.",
  "created_at": "2026-09-23T10:31:57Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T10:31:57+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T03:31:57-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790159673.000781",
  "message_id": "1790159673.000781",
  "ts": "1790159673.000781",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 79 passed.",
  "created_at": "2026-09-23T10:34:33Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T10:34:33+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T03:34:33-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790159828.000782",
  "message_id": "1790159828.000782",
  "ts": "1790159828.000782",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 80 passed.",
  "created_at": "2026-09-23T10:37:08Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T10:37:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T03:37:08-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790159983.000783",
  "message_id": "1790159983.000783",
  "ts": "1790159983.000783",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 81 passed.",
  "created_at": "2026-09-23T10:39:43Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T10:39:43+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T03:39:43-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790160139.000784",
  "message_id": "1790160139.000784",
  "ts": "1790160139.000784",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 82 passed.",
  "created_at": "2026-09-23T10:42:19Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T10:42:19+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T03:42:19-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790160294.000785",
  "message_id": "1790160294.000785",
  "ts": "1790160294.000785",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 83 passed.",
  "created_at": "2026-09-23T10:44:54Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T10:44:54+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T03:44:54-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790160450.000786",
  "message_id": "1790160450.000786",
  "ts": "1790160450.000786",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 84 passed.",
  "created_at": "2026-09-23T10:47:30Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T10:47:30+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T03:47:30-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790160605.000787",
  "message_id": "1790160605.000787",
  "ts": "1790160605.000787",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 85 passed.",
  "created_at": "2026-09-23T10:50:05Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T10:50:05+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T03:50:05-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790160760.000788",
  "message_id": "1790160760.000788",
  "ts": "1790160760.000788",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 86 passed.",
  "created_at": "2026-09-23T10:52:40Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T10:52:40+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T03:52:40-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790160916.000789",
  "message_id": "1790160916.000789",
  "ts": "1790160916.000789",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 87 passed.",
  "created_at": "2026-09-23T10:55:16Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T10:55:16+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T03:55:16-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790161071.000790",
  "message_id": "1790161071.000790",
  "ts": "1790161071.000790",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 88 passed.",
  "created_at": "2026-09-23T10:57:51Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T10:57:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T03:57:51-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790161226.000791",
  "message_id": "1790161226.000791",
  "ts": "1790161226.000791",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 89 passed.",
  "created_at": "2026-09-23T11:00:26Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T11:00:26+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T04:00:26-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790161382.000792",
  "message_id": "1790161382.000792",
  "ts": "1790161382.000792",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 90 passed.",
  "created_at": "2026-09-23T11:03:02Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T11:03:02+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T04:03:02-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790161537.000793",
  "message_id": "1790161537.000793",
  "ts": "1790161537.000793",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 91 passed.",
  "created_at": "2026-09-23T11:05:37Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T11:05:37+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T04:05:37-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790161692.000794",
  "message_id": "1790161692.000794",
  "ts": "1790161692.000794",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 92 passed.",
  "created_at": "2026-09-23T11:08:12Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T11:08:12+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T04:08:12-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790161848.000795",
  "message_id": "1790161848.000795",
  "ts": "1790161848.000795",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 93 passed.",
  "created_at": "2026-09-23T11:10:48Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T11:10:48+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T04:10:48-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790162003.000796",
  "message_id": "1790162003.000796",
  "ts": "1790162003.000796",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 94 passed.",
  "created_at": "2026-09-23T11:13:23Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T11:13:23+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T04:13:23-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790162158.000797",
  "message_id": "1790162158.000797",
  "ts": "1790162158.000797",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 95 passed.",
  "created_at": "2026-09-23T11:15:58Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T11:15:58+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T04:15:58-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790162314.000798",
  "message_id": "1790162314.000798",
  "ts": "1790162314.000798",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 96 passed.",
  "created_at": "2026-09-23T11:18:34Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T11:18:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T04:18:34-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790162469.000799",
  "message_id": "1790162469.000799",
  "ts": "1790162469.000799",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 97 passed.",
  "created_at": "2026-09-23T11:21:09Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T11:21:09+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T04:21:09-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790162625.000800",
  "message_id": "1790162625.000800",
  "ts": "1790162625.000800",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 98 passed.",
  "created_at": "2026-09-23T11:23:45Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T11:23:45+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T04:23:45-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790162780.000801",
  "message_id": "1790162780.000801",
  "ts": "1790162780.000801",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 99 passed.",
  "created_at": "2026-09-23T11:26:20Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T11:26:20+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T04:26:20-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790162935.000802",
  "message_id": "1790162935.000802",
  "ts": "1790162935.000802",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 100 passed.",
  "created_at": "2026-09-23T11:28:55Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T11:28:55+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T04:28:55-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790163091.000803",
  "message_id": "1790163091.000803",
  "ts": "1790163091.000803",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 101 passed.",
  "created_at": "2026-09-23T11:31:31Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T11:31:31+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T04:31:31-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790163246.000804",
  "message_id": "1790163246.000804",
  "ts": "1790163246.000804",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 102 passed.",
  "created_at": "2026-09-23T11:34:06Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T11:34:06+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T04:34:06-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790163401.000805",
  "message_id": "1790163401.000805",
  "ts": "1790163401.000805",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 103 passed.",
  "created_at": "2026-09-23T11:36:41Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T11:36:41+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T04:36:41-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790163557.000806",
  "message_id": "1790163557.000806",
  "ts": "1790163557.000806",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 104 passed.",
  "created_at": "2026-09-23T11:39:17Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T11:39:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T04:39:17-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790163712.000807",
  "message_id": "1790163712.000807",
  "ts": "1790163712.000807",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 105 passed.",
  "created_at": "2026-09-23T11:41:52Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T11:41:52+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T04:41:52-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790163867.000808",
  "message_id": "1790163867.000808",
  "ts": "1790163867.000808",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 106 passed.",
  "created_at": "2026-09-23T11:44:27Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T11:44:27+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T04:44:27-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790164023.000809",
  "message_id": "1790164023.000809",
  "ts": "1790164023.000809",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 107 passed.",
  "created_at": "2026-09-23T11:47:03Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T11:47:03+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T04:47:03-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790164178.000810",
  "message_id": "1790164178.000810",
  "ts": "1790164178.000810",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollback payments check 108 passed.",
  "created_at": "2026-09-23T11:49:38Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T11:49:38+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T04:49:38-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790164333.000811",
  "message_id": "1790164333.000811",
  "ts": "1790164333.000811",
  "channel_id": "C_DEPLOYS",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Rollback payments check 109 passed.",
  "created_at": "2026-09-23T11:52:13Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T11:52:13+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T04:52:13-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 },
 {
  "id": "1790164489.000812",
  "message_id": "1790164489.000812",
  "ts": "1790164489.000812",
  "channel_id": "C_DEPLOYS",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rollback payments check 110 passed.",
  "created_at": "2026-09-23T11:54:49Z",
  "channel": "deploys",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T11:54:49+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T04:54:49-07:00",
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
    "channel_id": "C_DEPLOYS",
    "channel_name": "deploys",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ]
 }
]
