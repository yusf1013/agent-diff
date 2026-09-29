You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Slack workspace:

    "Add an :eyes: reaction to all of Diego Alvarez's replies in the #incidents thread about the checkout outage."

The user is Agent Bot. Below is every Slack message in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "1789999560.000001",
  "message_id": "1789999560.000001",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage: 502s on /pay since 14:05 UTC.",
  "ts": "1789999560.000001",
  "created_at": "2026-09-21T14:06:00Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T14:06:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T07:06:00-07:00",
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
  "messages": [],
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
  "id": "1790000400.000002",
  "message_id": "1790000400.000002",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Rolled back the gateway config; watching the error rate.",
  "ts": "1790000400.000002",
  "created_at": "2026-09-21T14:20:00Z",
  "parent_id": "1789999560.000001",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T14:20:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T07:20:00-07:00",
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
  "messages": [
   {
    "message_id": "1789999560.000001",
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "message_text": "Checkout outage: 502s on /pay since 14:05 UTC.",
    "ts": "1789999560.000001",
    "created_at": "2026-09-21T14:06:00Z"
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
  "id": "1790000700.000003",
  "message_id": "1790000700.000003",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments dashboards look normal again.",
  "ts": "1790000700.000003",
  "created_at": "2026-09-21T14:25:00Z",
  "parent_id": "1789999560.000001",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T14:25:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T07:25:00-07:00",
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
  "messages": [
   {
    "message_id": "1789999560.000001",
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "message_text": "Checkout outage: 502s on /pay since 14:05 UTC.",
    "ts": "1789999560.000001",
    "created_at": "2026-09-21T14:06:00Z"
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
  "id": "1790071200.000004",
  "message_id": "1790071200.000004",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "The postmortem for the checkout outage is on Friday.",
  "ts": "1790071200.000004",
  "created_at": "2026-09-22T10:00:00Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:00:00-07:00",
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
  "messages": [],
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
  "id": "1790092800.000005",
  "message_id": "1790092800.000005",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Search latency spike on the product pages.",
  "ts": "1790092800.000005",
  "created_at": "2026-09-22T16:00:00Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T16:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T09:00:00-07:00",
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
  "messages": [],
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
  "id": "1790093400.000006",
  "message_id": "1790093400.000006",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Might be the same config push as the checkout outage.",
  "ts": "1790093400.000006",
  "created_at": "2026-09-22T16:10:00Z",
  "parent_id": "1790092800.000005",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T16:10:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T09:10:00-07:00",
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
  "messages": [
   {
    "message_id": "1790092800.000005",
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "message_text": "Search latency spike on the product pages.",
    "ts": "1790092800.000005",
    "created_at": "2026-09-22T16:00:00Z"
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
  "id": "1790000460.000701",
  "message_id": "1790000460.000701",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Reverted the gateway config; monitoring checkout recovery now.",
  "ts": "1790000460.000701",
  "created_at": "2026-09-21T14:21:00Z",
  "parent_id": "1789999560.000001",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T14:21:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T07:21:00-07:00",
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
  "messages": [
   {
    "message_id": "1789999560.000001",
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "message_text": "Checkout outage: 502s on /pay since 14:05 UTC.",
    "ts": "1789999560.000001",
    "created_at": "2026-09-21T14:06:00Z"
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
  "id": "1789974600.000702",
  "message_id": "1789974600.000702",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Reverted the gateway config; monitoring checkout recovery now.",
  "ts": "1789974600.000702",
  "created_at": "2026-09-21T07:10:00Z",
  "parent_id": "1789999560.000001",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:10:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:10:00-07:00",
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
  "messages": [
   {
    "message_id": "1789999560.000001",
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "message_text": "Checkout outage: 502s on /pay since 14:05 UTC.",
    "ts": "1789999560.000001",
    "created_at": "2026-09-21T14:06:00Z"
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
  "id": "1789974830.000703",
  "message_id": "1789974830.000703",
  "ts": "1789974830.000703",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 1 passed.",
  "created_at": "2026-09-21T07:13:50Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:13:50+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:13:50-07:00",
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
  "messages": [],
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
  "id": "1789975060.000704",
  "message_id": "1789975060.000704",
  "ts": "1789975060.000704",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 2 passed.",
  "created_at": "2026-09-21T07:17:40Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:17:40+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:17:40-07:00",
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
  "messages": [],
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
  "id": "1789975291.000705",
  "message_id": "1789975291.000705",
  "ts": "1789975291.000705",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 3 passed.",
  "created_at": "2026-09-21T07:21:31Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:21:31+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:21:31-07:00",
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
  "messages": [],
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
  "id": "1789975521.000706",
  "message_id": "1789975521.000706",
  "ts": "1789975521.000706",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 4 passed.",
  "created_at": "2026-09-21T07:25:21Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:25:21+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:25:21-07:00",
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
  "messages": [],
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
  "id": "1789975751.000707",
  "message_id": "1789975751.000707",
  "ts": "1789975751.000707",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 5 passed.",
  "created_at": "2026-09-21T07:29:11Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:29:11+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:29:11-07:00",
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
  "messages": [],
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
  "id": "1789975982.000708",
  "message_id": "1789975982.000708",
  "ts": "1789975982.000708",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 6 passed.",
  "created_at": "2026-09-21T07:33:02Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:33:02+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:33:02-07:00",
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
  "messages": [],
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
  "id": "1789976212.000709",
  "message_id": "1789976212.000709",
  "ts": "1789976212.000709",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 7 passed.",
  "created_at": "2026-09-21T07:36:52Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:36:52+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:36:52-07:00",
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
  "messages": [],
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
  "id": "1789976442.000710",
  "message_id": "1789976442.000710",
  "ts": "1789976442.000710",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 8 passed.",
  "created_at": "2026-09-21T07:40:42Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:40:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:40:42-07:00",
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
  "messages": [],
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
  "id": "1789976673.000711",
  "message_id": "1789976673.000711",
  "ts": "1789976673.000711",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 9 passed.",
  "created_at": "2026-09-21T07:44:33Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:44:33+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:44:33-07:00",
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
  "messages": [],
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
  "id": "1789976903.000712",
  "message_id": "1789976903.000712",
  "ts": "1789976903.000712",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 10 passed.",
  "created_at": "2026-09-21T07:48:23Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:48:23+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:48:23-07:00",
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
  "messages": [],
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
  "id": "1789977133.000713",
  "message_id": "1789977133.000713",
  "ts": "1789977133.000713",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 11 passed.",
  "created_at": "2026-09-21T07:52:13Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:52:13+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:52:13-07:00",
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
  "messages": [],
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
  "id": "1789977364.000714",
  "message_id": "1789977364.000714",
  "ts": "1789977364.000714",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 12 passed.",
  "created_at": "2026-09-21T07:56:04Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:56:04+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:56:04-07:00",
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
  "messages": [],
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
  "id": "1789977594.000715",
  "message_id": "1789977594.000715",
  "ts": "1789977594.000715",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 13 passed.",
  "created_at": "2026-09-21T07:59:54Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:59:54+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:59:54-07:00",
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
  "messages": [],
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
  "id": "1789977825.000716",
  "message_id": "1789977825.000716",
  "ts": "1789977825.000716",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 14 passed.",
  "created_at": "2026-09-21T08:03:45Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:03:45+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:03:45-07:00",
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
  "messages": [],
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
  "id": "1789978055.000717",
  "message_id": "1789978055.000717",
  "ts": "1789978055.000717",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 15 passed.",
  "created_at": "2026-09-21T08:07:35Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:07:35+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:07:35-07:00",
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
  "messages": [],
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
  "id": "1789978285.000718",
  "message_id": "1789978285.000718",
  "ts": "1789978285.000718",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 16 passed.",
  "created_at": "2026-09-21T08:11:25Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:11:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:11:25-07:00",
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
  "messages": [],
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
  "id": "1789978516.000719",
  "message_id": "1789978516.000719",
  "ts": "1789978516.000719",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 17 passed.",
  "created_at": "2026-09-21T08:15:16Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:15:16+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:15:16-07:00",
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
  "messages": [],
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
  "id": "1789978746.000720",
  "message_id": "1789978746.000720",
  "ts": "1789978746.000720",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 18 passed.",
  "created_at": "2026-09-21T08:19:06Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:19:06+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:19:06-07:00",
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
  "messages": [],
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
  "id": "1789978976.000721",
  "message_id": "1789978976.000721",
  "ts": "1789978976.000721",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 19 passed.",
  "created_at": "2026-09-21T08:22:56Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:22:56+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:22:56-07:00",
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
  "messages": [],
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
  "id": "1789979207.000722",
  "message_id": "1789979207.000722",
  "ts": "1789979207.000722",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 20 passed.",
  "created_at": "2026-09-21T08:26:47Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:26:47+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:26:47-07:00",
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
  "messages": [],
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
  "id": "1789979437.000723",
  "message_id": "1789979437.000723",
  "ts": "1789979437.000723",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 21 passed.",
  "created_at": "2026-09-21T08:30:37Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:30:37+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:30:37-07:00",
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
  "messages": [],
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
  "id": "1789979667.000724",
  "message_id": "1789979667.000724",
  "ts": "1789979667.000724",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 22 passed.",
  "created_at": "2026-09-21T08:34:27Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:34:27+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:34:27-07:00",
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
  "messages": [],
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
  "id": "1789979898.000725",
  "message_id": "1789979898.000725",
  "ts": "1789979898.000725",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 23 passed.",
  "created_at": "2026-09-21T08:38:18Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:38:18+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:38:18-07:00",
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
  "messages": [],
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
  "id": "1789980128.000726",
  "message_id": "1789980128.000726",
  "ts": "1789980128.000726",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 24 passed.",
  "created_at": "2026-09-21T08:42:08Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:42:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:42:08-07:00",
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
  "messages": [],
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
  "id": "1789980358.000727",
  "message_id": "1789980358.000727",
  "ts": "1789980358.000727",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 25 passed.",
  "created_at": "2026-09-21T08:45:58Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:45:58+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:45:58-07:00",
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
  "messages": [],
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
  "id": "1789980589.000728",
  "message_id": "1789980589.000728",
  "ts": "1789980589.000728",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 26 passed.",
  "created_at": "2026-09-21T08:49:49Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:49:49+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:49:49-07:00",
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
  "messages": [],
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
  "id": "1789980819.000729",
  "message_id": "1789980819.000729",
  "ts": "1789980819.000729",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 27 passed.",
  "created_at": "2026-09-21T08:53:39Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:53:39+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:53:39-07:00",
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
  "messages": [],
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
  "id": "1789981050.000730",
  "message_id": "1789981050.000730",
  "ts": "1789981050.000730",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 28 passed.",
  "created_at": "2026-09-21T08:57:30Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:57:30+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:57:30-07:00",
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
  "messages": [],
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
  "id": "1789981280.000731",
  "message_id": "1789981280.000731",
  "ts": "1789981280.000731",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 29 passed.",
  "created_at": "2026-09-21T09:01:20Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:01:20+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:01:20-07:00",
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
  "messages": [],
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
  "id": "1789981510.000732",
  "message_id": "1789981510.000732",
  "ts": "1789981510.000732",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 30 passed.",
  "created_at": "2026-09-21T09:05:10Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:05:10+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:05:10-07:00",
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
  "messages": [],
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
  "id": "1789981741.000733",
  "message_id": "1789981741.000733",
  "ts": "1789981741.000733",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 31 passed.",
  "created_at": "2026-09-21T09:09:01Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:09:01+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:09:01-07:00",
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
  "messages": [],
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
  "id": "1789981971.000734",
  "message_id": "1789981971.000734",
  "ts": "1789981971.000734",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 32 passed.",
  "created_at": "2026-09-21T09:12:51Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:12:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:12:51-07:00",
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
  "messages": [],
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
  "id": "1789982201.000735",
  "message_id": "1789982201.000735",
  "ts": "1789982201.000735",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 33 passed.",
  "created_at": "2026-09-21T09:16:41Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:16:41+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:16:41-07:00",
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
  "messages": [],
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
  "id": "1789982432.000736",
  "message_id": "1789982432.000736",
  "ts": "1789982432.000736",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 34 passed.",
  "created_at": "2026-09-21T09:20:32Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:20:32+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:20:32-07:00",
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
  "messages": [],
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
  "id": "1789982662.000737",
  "message_id": "1789982662.000737",
  "ts": "1789982662.000737",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 35 passed.",
  "created_at": "2026-09-21T09:24:22Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:24:22+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:24:22-07:00",
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
  "messages": [],
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
  "id": "1789982892.000738",
  "message_id": "1789982892.000738",
  "ts": "1789982892.000738",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 36 passed.",
  "created_at": "2026-09-21T09:28:12Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:28:12+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:28:12-07:00",
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
  "messages": [],
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
  "id": "1789983123.000739",
  "message_id": "1789983123.000739",
  "ts": "1789983123.000739",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 37 passed.",
  "created_at": "2026-09-21T09:32:03Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:32:03+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:32:03-07:00",
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
  "messages": [],
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
  "id": "1789983353.000740",
  "message_id": "1789983353.000740",
  "ts": "1789983353.000740",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 38 passed.",
  "created_at": "2026-09-21T09:35:53Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:35:53+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:35:53-07:00",
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
  "messages": [],
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
  "id": "1789983583.000741",
  "message_id": "1789983583.000741",
  "ts": "1789983583.000741",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 39 passed.",
  "created_at": "2026-09-21T09:39:43Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:39:43+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:39:43-07:00",
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
  "messages": [],
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
  "id": "1789983814.000742",
  "message_id": "1789983814.000742",
  "ts": "1789983814.000742",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 40 passed.",
  "created_at": "2026-09-21T09:43:34Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:43:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:43:34-07:00",
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
  "messages": [],
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
  "id": "1789984044.000743",
  "message_id": "1789984044.000743",
  "ts": "1789984044.000743",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 41 passed.",
  "created_at": "2026-09-21T09:47:24Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:47:24+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:47:24-07:00",
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
  "messages": [],
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
  "id": "1789984275.000744",
  "message_id": "1789984275.000744",
  "ts": "1789984275.000744",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 42 passed.",
  "created_at": "2026-09-21T09:51:15Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:51:15+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:51:15-07:00",
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
  "messages": [],
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
  "id": "1789984505.000745",
  "message_id": "1789984505.000745",
  "ts": "1789984505.000745",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 43 passed.",
  "created_at": "2026-09-21T09:55:05Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:55:05+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:55:05-07:00",
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
  "messages": [],
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
  "id": "1789984735.000746",
  "message_id": "1789984735.000746",
  "ts": "1789984735.000746",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 44 passed.",
  "created_at": "2026-09-21T09:58:55Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:58:55+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:58:55-07:00",
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
  "messages": [],
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
  "id": "1789984966.000747",
  "message_id": "1789984966.000747",
  "ts": "1789984966.000747",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 45 passed.",
  "created_at": "2026-09-21T10:02:46Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:02:46+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:02:46-07:00",
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
  "messages": [],
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
  "id": "1789985196.000748",
  "message_id": "1789985196.000748",
  "ts": "1789985196.000748",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 46 passed.",
  "created_at": "2026-09-21T10:06:36Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:06:36+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:06:36-07:00",
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
  "messages": [],
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
  "id": "1789985426.000749",
  "message_id": "1789985426.000749",
  "ts": "1789985426.000749",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 47 passed.",
  "created_at": "2026-09-21T10:10:26Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:10:26+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:10:26-07:00",
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
  "messages": [],
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
  "id": "1789985657.000750",
  "message_id": "1789985657.000750",
  "ts": "1789985657.000750",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 48 passed.",
  "created_at": "2026-09-21T10:14:17Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:14:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:14:17-07:00",
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
  "messages": [],
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
  "id": "1789985887.000751",
  "message_id": "1789985887.000751",
  "ts": "1789985887.000751",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 49 passed.",
  "created_at": "2026-09-21T10:18:07Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:18:07+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:18:07-07:00",
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
  "messages": [],
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
  "id": "1789986117.000752",
  "message_id": "1789986117.000752",
  "ts": "1789986117.000752",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 50 passed.",
  "created_at": "2026-09-21T10:21:57Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:21:57+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:21:57-07:00",
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
  "messages": [],
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
  "id": "1789986348.000753",
  "message_id": "1789986348.000753",
  "ts": "1789986348.000753",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 51 passed.",
  "created_at": "2026-09-21T10:25:48Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:25:48+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:25:48-07:00",
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
  "messages": [],
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
  "id": "1789986578.000754",
  "message_id": "1789986578.000754",
  "ts": "1789986578.000754",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 52 passed.",
  "created_at": "2026-09-21T10:29:38Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:29:38+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:29:38-07:00",
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
  "messages": [],
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
  "id": "1789986808.000755",
  "message_id": "1789986808.000755",
  "ts": "1789986808.000755",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 53 passed.",
  "created_at": "2026-09-21T10:33:28Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:33:28+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:33:28-07:00",
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
  "messages": [],
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
  "id": "1789987039.000756",
  "message_id": "1789987039.000756",
  "ts": "1789987039.000756",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 54 passed.",
  "created_at": "2026-09-21T10:37:19Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:37:19+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:37:19-07:00",
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
  "messages": [],
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
  "id": "1789987269.000757",
  "message_id": "1789987269.000757",
  "ts": "1789987269.000757",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 55 passed.",
  "created_at": "2026-09-21T10:41:09Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:41:09+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:41:09-07:00",
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
  "messages": [],
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
  "id": "1789987500.000758",
  "message_id": "1789987500.000758",
  "ts": "1789987500.000758",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 56 passed.",
  "created_at": "2026-09-21T10:45:00Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:45:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:45:00-07:00",
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
  "messages": [],
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
  "id": "1789987730.000759",
  "message_id": "1789987730.000759",
  "ts": "1789987730.000759",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 57 passed.",
  "created_at": "2026-09-21T10:48:50Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:48:50+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:48:50-07:00",
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
  "messages": [],
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
  "id": "1789987960.000760",
  "message_id": "1789987960.000760",
  "ts": "1789987960.000760",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 58 passed.",
  "created_at": "2026-09-21T10:52:40Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:52:40+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:52:40-07:00",
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
  "messages": [],
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
  "id": "1789988191.000761",
  "message_id": "1789988191.000761",
  "ts": "1789988191.000761",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 59 passed.",
  "created_at": "2026-09-21T10:56:31Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:56:31+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:56:31-07:00",
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
  "messages": [],
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
  "id": "1789988421.000762",
  "message_id": "1789988421.000762",
  "ts": "1789988421.000762",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 60 passed.",
  "created_at": "2026-09-21T11:00:21Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:00:21+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:00:21-07:00",
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
  "messages": [],
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
  "id": "1789988651.000763",
  "message_id": "1789988651.000763",
  "ts": "1789988651.000763",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 61 passed.",
  "created_at": "2026-09-21T11:04:11Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:04:11+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:04:11-07:00",
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
  "messages": [],
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
  "id": "1789988882.000764",
  "message_id": "1789988882.000764",
  "ts": "1789988882.000764",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 62 passed.",
  "created_at": "2026-09-21T11:08:02Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:08:02+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:08:02-07:00",
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
  "messages": [],
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
  "id": "1789989112.000765",
  "message_id": "1789989112.000765",
  "ts": "1789989112.000765",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 63 passed.",
  "created_at": "2026-09-21T11:11:52Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:11:52+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:11:52-07:00",
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
  "messages": [],
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
  "id": "1789989342.000766",
  "message_id": "1789989342.000766",
  "ts": "1789989342.000766",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 64 passed.",
  "created_at": "2026-09-21T11:15:42Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:15:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:15:42-07:00",
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
  "messages": [],
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
  "id": "1789989573.000767",
  "message_id": "1789989573.000767",
  "ts": "1789989573.000767",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 65 passed.",
  "created_at": "2026-09-21T11:19:33Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:19:33+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:19:33-07:00",
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
  "messages": [],
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
  "id": "1789989803.000768",
  "message_id": "1789989803.000768",
  "ts": "1789989803.000768",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 66 passed.",
  "created_at": "2026-09-21T11:23:23Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:23:23+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:23:23-07:00",
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
  "messages": [],
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
  "id": "1789990033.000769",
  "message_id": "1789990033.000769",
  "ts": "1789990033.000769",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 67 passed.",
  "created_at": "2026-09-21T11:27:13Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:27:13+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:27:13-07:00",
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
  "messages": [],
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
  "id": "1789990264.000770",
  "message_id": "1789990264.000770",
  "ts": "1789990264.000770",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 68 passed.",
  "created_at": "2026-09-21T11:31:04Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:31:04+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:31:04-07:00",
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
  "messages": [],
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
  "id": "1789990494.000771",
  "message_id": "1789990494.000771",
  "ts": "1789990494.000771",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 69 passed.",
  "created_at": "2026-09-21T11:34:54Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:34:54+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:34:54-07:00",
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
  "messages": [],
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
  "id": "1789990725.000772",
  "message_id": "1789990725.000772",
  "ts": "1789990725.000772",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 70 passed.",
  "created_at": "2026-09-21T11:38:45Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:38:45+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:38:45-07:00",
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
  "messages": [],
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
  "id": "1789990955.000773",
  "message_id": "1789990955.000773",
  "ts": "1789990955.000773",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 71 passed.",
  "created_at": "2026-09-21T11:42:35Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:42:35+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:42:35-07:00",
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
  "messages": [],
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
  "id": "1789991185.000774",
  "message_id": "1789991185.000774",
  "ts": "1789991185.000774",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 72 passed.",
  "created_at": "2026-09-21T11:46:25Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:46:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:46:25-07:00",
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
  "messages": [],
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
  "id": "1789991416.000775",
  "message_id": "1789991416.000775",
  "ts": "1789991416.000775",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 73 passed.",
  "created_at": "2026-09-21T11:50:16Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:50:16+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:50:16-07:00",
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
  "messages": [],
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
  "id": "1789991646.000776",
  "message_id": "1789991646.000776",
  "ts": "1789991646.000776",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 74 passed.",
  "created_at": "2026-09-21T11:54:06Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:54:06+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:54:06-07:00",
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
  "messages": [],
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
  "id": "1789991876.000777",
  "message_id": "1789991876.000777",
  "ts": "1789991876.000777",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 75 passed.",
  "created_at": "2026-09-21T11:57:56Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:57:56+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:57:56-07:00",
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
  "messages": [],
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
  "id": "1789992107.000778",
  "message_id": "1789992107.000778",
  "ts": "1789992107.000778",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 76 passed.",
  "created_at": "2026-09-21T12:01:47Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:01:47+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:01:47-07:00",
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
  "messages": [],
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
  "id": "1789992337.000779",
  "message_id": "1789992337.000779",
  "ts": "1789992337.000779",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 77 passed.",
  "created_at": "2026-09-21T12:05:37Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:05:37+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:05:37-07:00",
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
  "messages": [],
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
  "id": "1789992567.000780",
  "message_id": "1789992567.000780",
  "ts": "1789992567.000780",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 78 passed.",
  "created_at": "2026-09-21T12:09:27Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:09:27+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:09:27-07:00",
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
  "messages": [],
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
  "id": "1789992798.000781",
  "message_id": "1789992798.000781",
  "ts": "1789992798.000781",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 79 passed.",
  "created_at": "2026-09-21T12:13:18Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:13:18+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:13:18-07:00",
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
  "messages": [],
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
  "id": "1789993028.000782",
  "message_id": "1789993028.000782",
  "ts": "1789993028.000782",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 80 passed.",
  "created_at": "2026-09-21T12:17:08Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:17:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:17:08-07:00",
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
  "messages": [],
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
  "id": "1789993258.000783",
  "message_id": "1789993258.000783",
  "ts": "1789993258.000783",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 81 passed.",
  "created_at": "2026-09-21T12:20:58Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:20:58+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:20:58-07:00",
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
  "messages": [],
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
  "id": "1789993489.000784",
  "message_id": "1789993489.000784",
  "ts": "1789993489.000784",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 82 passed.",
  "created_at": "2026-09-21T12:24:49Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:24:49+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:24:49-07:00",
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
  "messages": [],
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
  "id": "1789993719.000785",
  "message_id": "1789993719.000785",
  "ts": "1789993719.000785",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 83 passed.",
  "created_at": "2026-09-21T12:28:39Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:28:39+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:28:39-07:00",
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
  "messages": [],
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
  "id": "1789993950.000786",
  "message_id": "1789993950.000786",
  "ts": "1789993950.000786",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 84 passed.",
  "created_at": "2026-09-21T12:32:30Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:32:30+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:32:30-07:00",
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
  "messages": [],
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
  "id": "1789994180.000787",
  "message_id": "1789994180.000787",
  "ts": "1789994180.000787",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 85 passed.",
  "created_at": "2026-09-21T12:36:20Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:36:20+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:36:20-07:00",
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
  "messages": [],
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
  "id": "1789994410.000788",
  "message_id": "1789994410.000788",
  "ts": "1789994410.000788",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 86 passed.",
  "created_at": "2026-09-21T12:40:10Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:40:10+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:40:10-07:00",
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
  "messages": [],
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
  "id": "1789994641.000789",
  "message_id": "1789994641.000789",
  "ts": "1789994641.000789",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 87 passed.",
  "created_at": "2026-09-21T12:44:01Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:44:01+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:44:01-07:00",
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
  "messages": [],
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
  "id": "1789994871.000790",
  "message_id": "1789994871.000790",
  "ts": "1789994871.000790",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 88 passed.",
  "created_at": "2026-09-21T12:47:51Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:47:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:47:51-07:00",
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
  "messages": [],
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
  "id": "1789995101.000791",
  "message_id": "1789995101.000791",
  "ts": "1789995101.000791",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 89 passed.",
  "created_at": "2026-09-21T12:51:41Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:51:41+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:51:41-07:00",
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
  "messages": [],
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
  "id": "1789995332.000792",
  "message_id": "1789995332.000792",
  "ts": "1789995332.000792",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 90 passed.",
  "created_at": "2026-09-21T12:55:32Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:55:32+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:55:32-07:00",
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
  "messages": [],
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
  "id": "1789995562.000793",
  "message_id": "1789995562.000793",
  "ts": "1789995562.000793",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 91 passed.",
  "created_at": "2026-09-21T12:59:22Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:59:22+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:59:22-07:00",
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
  "messages": [],
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
  "id": "1789995792.000794",
  "message_id": "1789995792.000794",
  "ts": "1789995792.000794",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 92 passed.",
  "created_at": "2026-09-21T13:03:12Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T13:03:12+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T06:03:12-07:00",
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
  "messages": [],
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
  "id": "1789996023.000795",
  "message_id": "1789996023.000795",
  "ts": "1789996023.000795",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 93 passed.",
  "created_at": "2026-09-21T13:07:03Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T13:07:03+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T06:07:03-07:00",
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
  "messages": [],
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
  "id": "1789996253.000796",
  "message_id": "1789996253.000796",
  "ts": "1789996253.000796",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 94 passed.",
  "created_at": "2026-09-21T13:10:53Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T13:10:53+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T06:10:53-07:00",
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
  "messages": [],
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
  "id": "1789996483.000797",
  "message_id": "1789996483.000797",
  "ts": "1789996483.000797",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 95 passed.",
  "created_at": "2026-09-21T13:14:43Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T13:14:43+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T06:14:43-07:00",
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
  "messages": [],
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
  "id": "1789996714.000798",
  "message_id": "1789996714.000798",
  "ts": "1789996714.000798",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 96 passed.",
  "created_at": "2026-09-21T13:18:34Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T13:18:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T06:18:34-07:00",
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
  "messages": [],
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
  "id": "1789996944.000799",
  "message_id": "1789996944.000799",
  "ts": "1789996944.000799",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 97 passed.",
  "created_at": "2026-09-21T13:22:24Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T13:22:24+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T06:22:24-07:00",
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
  "messages": [],
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
  "id": "1789997175.000800",
  "message_id": "1789997175.000800",
  "ts": "1789997175.000800",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 98 passed.",
  "created_at": "2026-09-21T13:26:15Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T13:26:15+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T06:26:15-07:00",
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
  "messages": [],
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
  "id": "1789997405.000801",
  "message_id": "1789997405.000801",
  "ts": "1789997405.000801",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 99 passed.",
  "created_at": "2026-09-21T13:30:05Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T13:30:05+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T06:30:05-07:00",
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
  "messages": [],
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
  "id": "1789997635.000802",
  "message_id": "1789997635.000802",
  "ts": "1789997635.000802",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 100 passed.",
  "created_at": "2026-09-21T13:33:55Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T13:33:55+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T06:33:55-07:00",
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
  "messages": [],
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
  "id": "1789997866.000803",
  "message_id": "1789997866.000803",
  "ts": "1789997866.000803",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 101 passed.",
  "created_at": "2026-09-21T13:37:46Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T13:37:46+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T06:37:46-07:00",
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
  "messages": [],
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
  "id": "1789998096.000804",
  "message_id": "1789998096.000804",
  "ts": "1789998096.000804",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 102 passed.",
  "created_at": "2026-09-21T13:41:36Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T13:41:36+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T06:41:36-07:00",
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
  "messages": [],
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
  "id": "1789998326.000805",
  "message_id": "1789998326.000805",
  "ts": "1789998326.000805",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 103 passed.",
  "created_at": "2026-09-21T13:45:26Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T13:45:26+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T06:45:26-07:00",
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
  "messages": [],
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
  "id": "1789998557.000806",
  "message_id": "1789998557.000806",
  "ts": "1789998557.000806",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 104 passed.",
  "created_at": "2026-09-21T13:49:17Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T13:49:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T06:49:17-07:00",
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
  "messages": [],
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
  "id": "1789998787.000807",
  "message_id": "1789998787.000807",
  "ts": "1789998787.000807",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 105 passed.",
  "created_at": "2026-09-21T13:53:07Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T13:53:07+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T06:53:07-07:00",
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
  "messages": [],
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
  "id": "1789999017.000808",
  "message_id": "1789999017.000808",
  "ts": "1789999017.000808",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 106 passed.",
  "created_at": "2026-09-21T13:56:57Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T13:56:57+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T06:56:57-07:00",
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
  "messages": [],
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
  "id": "1789999248.000809",
  "message_id": "1789999248.000809",
  "ts": "1789999248.000809",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 107 passed.",
  "created_at": "2026-09-21T14:00:48Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T14:00:48+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T07:00:48-07:00",
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
  "messages": [],
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
  "id": "1789999478.000810",
  "message_id": "1789999478.000810",
  "ts": "1789999478.000810",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Checkout outage check 108 passed.",
  "created_at": "2026-09-21T14:04:38Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T14:04:38+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T07:04:38-07:00",
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
  "messages": [],
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
  "id": "1789999708.000811",
  "message_id": "1789999708.000811",
  "ts": "1789999708.000811",
  "channel_id": "C_INC",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Checkout outage check 109 passed.",
  "created_at": "2026-09-21T14:08:28Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T14:08:28+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T07:08:28-07:00",
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
  "messages": [],
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
  "id": "1789999939.000812",
  "message_id": "1789999939.000812",
  "ts": "1789999939.000812",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Checkout outage check 110 passed.",
  "created_at": "2026-09-21T14:12:19Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T14:12:19+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T07:12:19-07:00",
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
  "messages": [],
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
