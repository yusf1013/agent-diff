You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Slack workspace:

    "In #launch-prep, add a rocket reaction to all of Leo Park's replies in the thread about tonight's payments launch checklist."

The user is Agent Bot. Below is every Slack message in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "1790077800.000001",
  "message_id": "1790077800.000001",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Anyone want tacos for lunch?",
  "ts": "1790077800.000001",
  "created_at": "2026-09-22T11:50:00Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:50:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:50:00-07:00",
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
  "messages": []
 },
 {
  "id": "1790078700.000002",
  "message_id": "1790078700.000002",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Reply here once you've signed off on tonight's payments launch checklist.",
  "ts": "1790078700.000002",
  "created_at": "2026-09-22T12:05:00Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T12:05:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T05:05:00-07:00",
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
  "messages": []
 },
 {
  "id": "1790078760.000003",
  "message_id": "1790078760.000003",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Reminder: payments launch checklist review starts at 6pm tonight.",
  "ts": "1790078760.000003",
  "created_at": "2026-09-22T12:06:00Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T12:06:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T05:06:00-07:00",
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
  "messages": []
 },
 {
  "id": "1790078880.000004",
  "message_id": "1790078880.000004",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Signed off on my end, checklist looks good.",
  "ts": "1790078880.000004",
  "created_at": "2026-09-22T12:08:00Z",
  "parent_id": "1790078700.000002",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T12:08:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T05:08:00-07:00",
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
    "message_id": "1790078700.000002",
    "channel_id": "C_LAUNCH",
    "user_id": "U_DIEGO",
    "message_text": "Reply here once you've signed off on tonight's payments launch checklist.",
    "ts": "1790078700.000002",
    "created_at": "2026-09-22T12:05:00Z"
   }
  ]
 },
 {
  "id": "1790079120.000005",
  "message_id": "1790079120.000005",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "All checklists are in, we're clear to ship.",
  "ts": "1790079120.000005",
  "created_at": "2026-09-22T12:12:00Z",
  "parent_id": "1790078700.000002",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T12:12:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T05:12:00-07:00",
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
  "messages": [
   {
    "message_id": "1790078700.000002",
    "channel_id": "C_LAUNCH",
    "user_id": "U_DIEGO",
    "message_text": "Reply here once you've signed off on tonight's payments launch checklist.",
    "ts": "1790078700.000002",
    "created_at": "2026-09-22T12:05:00Z"
   }
  ]
 },
 {
  "id": "1790079180.000701",
  "message_id": "1790079180.000701",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "All checklists are in, we're clear to ship.",
  "ts": "1790079180.000701",
  "created_at": "2026-09-22T12:13:00Z",
  "parent_id": "1790078700.000002",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T12:13:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T05:13:00-07:00",
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
  "messages": [
   {
    "message_id": "1790078700.000002",
    "channel_id": "C_LAUNCH",
    "user_id": "U_DIEGO",
    "message_text": "Reply here once you've signed off on tonight's payments launch checklist.",
    "ts": "1790078700.000002",
    "created_at": "2026-09-22T12:05:00Z"
   }
  ]
 },
 {
  "id": "1790061000.000702",
  "message_id": "1790061000.000702",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "All checklists are in, we're clear to ship.",
  "ts": "1790061000.000702",
  "created_at": "2026-09-22T07:10:00Z",
  "parent_id": "1790078700.000002",
  "channel": "launch-prep",
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
  "messages": [
   {
    "message_id": "1790078700.000002",
    "channel_id": "C_LAUNCH",
    "user_id": "U_DIEGO",
    "message_text": "Reply here once you've signed off on tonight's payments launch checklist.",
    "ts": "1790078700.000002",
    "created_at": "2026-09-22T12:05:00Z"
   }
  ]
 },
 {
  "id": "1790061161.000703",
  "message_id": "1790061161.000703",
  "ts": "1790061161.000703",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 1 passed.",
  "created_at": "2026-09-22T07:12:41Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:12:41+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:12:41-07:00",
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
  "messages": []
 },
 {
  "id": "1790061323.000704",
  "message_id": "1790061323.000704",
  "ts": "1790061323.000704",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 2 passed.",
  "created_at": "2026-09-22T07:15:23Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:15:23+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:15:23-07:00",
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
  "messages": []
 },
 {
  "id": "1790061485.000705",
  "message_id": "1790061485.000705",
  "ts": "1790061485.000705",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments launch checklist check 3 passed.",
  "created_at": "2026-09-22T07:18:05Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:18:05+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:18:05-07:00",
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
  "messages": []
 },
 {
  "id": "1790061647.000706",
  "message_id": "1790061647.000706",
  "ts": "1790061647.000706",
  "channel_id": "C_LAUNCH",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Payments launch checklist check 4 passed.",
  "created_at": "2026-09-22T07:20:47Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:20:47+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:20:47-07:00",
  "users": [
   {
    "user_id": "U_AISHA",
    "username": "aisha.khan",
    "email": "aisha.khan@northwind.example",
    "real_name": "Aisha Khan",
    "display_name": "Aisha",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "messages": []
 },
 {
  "id": "1790061808.000707",
  "message_id": "1790061808.000707",
  "ts": "1790061808.000707",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 5 passed.",
  "created_at": "2026-09-22T07:23:28Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:23:28+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:23:28-07:00",
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
  "messages": []
 },
 {
  "id": "1790061970.000708",
  "message_id": "1790061970.000708",
  "ts": "1790061970.000708",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 6 passed.",
  "created_at": "2026-09-22T07:26:10Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:26:10+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:26:10-07:00",
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
  "messages": []
 },
 {
  "id": "1790062132.000709",
  "message_id": "1790062132.000709",
  "ts": "1790062132.000709",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments launch checklist check 7 passed.",
  "created_at": "2026-09-22T07:28:52Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:28:52+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:28:52-07:00",
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
  "messages": []
 },
 {
  "id": "1790062294.000710",
  "message_id": "1790062294.000710",
  "ts": "1790062294.000710",
  "channel_id": "C_LAUNCH",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Payments launch checklist check 8 passed.",
  "created_at": "2026-09-22T07:31:34Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:31:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:31:34-07:00",
  "users": [
   {
    "user_id": "U_AISHA",
    "username": "aisha.khan",
    "email": "aisha.khan@northwind.example",
    "real_name": "Aisha Khan",
    "display_name": "Aisha",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "messages": []
 },
 {
  "id": "1790062456.000711",
  "message_id": "1790062456.000711",
  "ts": "1790062456.000711",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 9 passed.",
  "created_at": "2026-09-22T07:34:16Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:34:16+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:34:16-07:00",
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
  "messages": []
 },
 {
  "id": "1790062617.000712",
  "message_id": "1790062617.000712",
  "ts": "1790062617.000712",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 10 passed.",
  "created_at": "2026-09-22T07:36:57Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:36:57+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:36:57-07:00",
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
  "messages": []
 },
 {
  "id": "1790062779.000713",
  "message_id": "1790062779.000713",
  "ts": "1790062779.000713",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments launch checklist check 11 passed.",
  "created_at": "2026-09-22T07:39:39Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:39:39+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:39:39-07:00",
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
  "messages": []
 },
 {
  "id": "1790062941.000714",
  "message_id": "1790062941.000714",
  "ts": "1790062941.000714",
  "channel_id": "C_LAUNCH",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Payments launch checklist check 12 passed.",
  "created_at": "2026-09-22T07:42:21Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:42:21+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:42:21-07:00",
  "users": [
   {
    "user_id": "U_AISHA",
    "username": "aisha.khan",
    "email": "aisha.khan@northwind.example",
    "real_name": "Aisha Khan",
    "display_name": "Aisha",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "messages": []
 },
 {
  "id": "1790063103.000715",
  "message_id": "1790063103.000715",
  "ts": "1790063103.000715",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 13 passed.",
  "created_at": "2026-09-22T07:45:03Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:45:03+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:45:03-07:00",
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
  "messages": []
 },
 {
  "id": "1790063264.000716",
  "message_id": "1790063264.000716",
  "ts": "1790063264.000716",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 14 passed.",
  "created_at": "2026-09-22T07:47:44Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:47:44+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:47:44-07:00",
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
  "messages": []
 },
 {
  "id": "1790063426.000717",
  "message_id": "1790063426.000717",
  "ts": "1790063426.000717",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments launch checklist check 15 passed.",
  "created_at": "2026-09-22T07:50:26Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:50:26+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:50:26-07:00",
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
  "messages": []
 },
 {
  "id": "1790063588.000718",
  "message_id": "1790063588.000718",
  "ts": "1790063588.000718",
  "channel_id": "C_LAUNCH",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Payments launch checklist check 16 passed.",
  "created_at": "2026-09-22T07:53:08Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:53:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:53:08-07:00",
  "users": [
   {
    "user_id": "U_AISHA",
    "username": "aisha.khan",
    "email": "aisha.khan@northwind.example",
    "real_name": "Aisha Khan",
    "display_name": "Aisha",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "messages": []
 },
 {
  "id": "1790063750.000719",
  "message_id": "1790063750.000719",
  "ts": "1790063750.000719",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 17 passed.",
  "created_at": "2026-09-22T07:55:50Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:55:50+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:55:50-07:00",
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
  "messages": []
 },
 {
  "id": "1790063912.000720",
  "message_id": "1790063912.000720",
  "ts": "1790063912.000720",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 18 passed.",
  "created_at": "2026-09-22T07:58:32Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T07:58:32+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T00:58:32-07:00",
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
  "messages": []
 },
 {
  "id": "1790064073.000721",
  "message_id": "1790064073.000721",
  "ts": "1790064073.000721",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments launch checklist check 19 passed.",
  "created_at": "2026-09-22T08:01:13Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:01:13+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:01:13-07:00",
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
  "messages": []
 },
 {
  "id": "1790064235.000722",
  "message_id": "1790064235.000722",
  "ts": "1790064235.000722",
  "channel_id": "C_LAUNCH",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Payments launch checklist check 20 passed.",
  "created_at": "2026-09-22T08:03:55Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:03:55+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:03:55-07:00",
  "users": [
   {
    "user_id": "U_AISHA",
    "username": "aisha.khan",
    "email": "aisha.khan@northwind.example",
    "real_name": "Aisha Khan",
    "display_name": "Aisha",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "messages": []
 },
 {
  "id": "1790064397.000723",
  "message_id": "1790064397.000723",
  "ts": "1790064397.000723",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 21 passed.",
  "created_at": "2026-09-22T08:06:37Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:06:37+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:06:37-07:00",
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
  "messages": []
 },
 {
  "id": "1790064559.000724",
  "message_id": "1790064559.000724",
  "ts": "1790064559.000724",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 22 passed.",
  "created_at": "2026-09-22T08:09:19Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:09:19+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:09:19-07:00",
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
  "messages": []
 },
 {
  "id": "1790064721.000725",
  "message_id": "1790064721.000725",
  "ts": "1790064721.000725",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments launch checklist check 23 passed.",
  "created_at": "2026-09-22T08:12:01Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:12:01+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:12:01-07:00",
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
  "messages": []
 },
 {
  "id": "1790064882.000726",
  "message_id": "1790064882.000726",
  "ts": "1790064882.000726",
  "channel_id": "C_LAUNCH",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Payments launch checklist check 24 passed.",
  "created_at": "2026-09-22T08:14:42Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:14:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:14:42-07:00",
  "users": [
   {
    "user_id": "U_AISHA",
    "username": "aisha.khan",
    "email": "aisha.khan@northwind.example",
    "real_name": "Aisha Khan",
    "display_name": "Aisha",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "messages": []
 },
 {
  "id": "1790065044.000727",
  "message_id": "1790065044.000727",
  "ts": "1790065044.000727",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 25 passed.",
  "created_at": "2026-09-22T08:17:24Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:17:24+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:17:24-07:00",
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
  "messages": []
 },
 {
  "id": "1790065206.000728",
  "message_id": "1790065206.000728",
  "ts": "1790065206.000728",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 26 passed.",
  "created_at": "2026-09-22T08:20:06Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:20:06+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:20:06-07:00",
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
  "messages": []
 },
 {
  "id": "1790065368.000729",
  "message_id": "1790065368.000729",
  "ts": "1790065368.000729",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments launch checklist check 27 passed.",
  "created_at": "2026-09-22T08:22:48Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:22:48+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:22:48-07:00",
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
  "messages": []
 },
 {
  "id": "1790065529.000730",
  "message_id": "1790065529.000730",
  "ts": "1790065529.000730",
  "channel_id": "C_LAUNCH",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Payments launch checklist check 28 passed.",
  "created_at": "2026-09-22T08:25:29Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:25:29+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:25:29-07:00",
  "users": [
   {
    "user_id": "U_AISHA",
    "username": "aisha.khan",
    "email": "aisha.khan@northwind.example",
    "real_name": "Aisha Khan",
    "display_name": "Aisha",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "messages": []
 },
 {
  "id": "1790065691.000731",
  "message_id": "1790065691.000731",
  "ts": "1790065691.000731",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 29 passed.",
  "created_at": "2026-09-22T08:28:11Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:28:11+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:28:11-07:00",
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
  "messages": []
 },
 {
  "id": "1790065853.000732",
  "message_id": "1790065853.000732",
  "ts": "1790065853.000732",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 30 passed.",
  "created_at": "2026-09-22T08:30:53Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:30:53+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:30:53-07:00",
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
  "messages": []
 },
 {
  "id": "1790066015.000733",
  "message_id": "1790066015.000733",
  "ts": "1790066015.000733",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments launch checklist check 31 passed.",
  "created_at": "2026-09-22T08:33:35Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:33:35+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:33:35-07:00",
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
  "messages": []
 },
 {
  "id": "1790066177.000734",
  "message_id": "1790066177.000734",
  "ts": "1790066177.000734",
  "channel_id": "C_LAUNCH",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Payments launch checklist check 32 passed.",
  "created_at": "2026-09-22T08:36:17Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:36:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:36:17-07:00",
  "users": [
   {
    "user_id": "U_AISHA",
    "username": "aisha.khan",
    "email": "aisha.khan@northwind.example",
    "real_name": "Aisha Khan",
    "display_name": "Aisha",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "messages": []
 },
 {
  "id": "1790066338.000735",
  "message_id": "1790066338.000735",
  "ts": "1790066338.000735",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 33 passed.",
  "created_at": "2026-09-22T08:38:58Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:38:58+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:38:58-07:00",
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
  "messages": []
 },
 {
  "id": "1790066500.000736",
  "message_id": "1790066500.000736",
  "ts": "1790066500.000736",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 34 passed.",
  "created_at": "2026-09-22T08:41:40Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:41:40+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:41:40-07:00",
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
  "messages": []
 },
 {
  "id": "1790066662.000737",
  "message_id": "1790066662.000737",
  "ts": "1790066662.000737",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments launch checklist check 35 passed.",
  "created_at": "2026-09-22T08:44:22Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:44:22+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:44:22-07:00",
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
  "messages": []
 },
 {
  "id": "1790066824.000738",
  "message_id": "1790066824.000738",
  "ts": "1790066824.000738",
  "channel_id": "C_LAUNCH",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Payments launch checklist check 36 passed.",
  "created_at": "2026-09-22T08:47:04Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:47:04+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:47:04-07:00",
  "users": [
   {
    "user_id": "U_AISHA",
    "username": "aisha.khan",
    "email": "aisha.khan@northwind.example",
    "real_name": "Aisha Khan",
    "display_name": "Aisha",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "messages": []
 },
 {
  "id": "1790066986.000739",
  "message_id": "1790066986.000739",
  "ts": "1790066986.000739",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 37 passed.",
  "created_at": "2026-09-22T08:49:46Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:49:46+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:49:46-07:00",
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
  "messages": []
 },
 {
  "id": "1790067147.000740",
  "message_id": "1790067147.000740",
  "ts": "1790067147.000740",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 38 passed.",
  "created_at": "2026-09-22T08:52:27Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:52:27+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:52:27-07:00",
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
  "messages": []
 },
 {
  "id": "1790067309.000741",
  "message_id": "1790067309.000741",
  "ts": "1790067309.000741",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments launch checklist check 39 passed.",
  "created_at": "2026-09-22T08:55:09Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:55:09+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:55:09-07:00",
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
  "messages": []
 },
 {
  "id": "1790067471.000742",
  "message_id": "1790067471.000742",
  "ts": "1790067471.000742",
  "channel_id": "C_LAUNCH",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Payments launch checklist check 40 passed.",
  "created_at": "2026-09-22T08:57:51Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T08:57:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T01:57:51-07:00",
  "users": [
   {
    "user_id": "U_AISHA",
    "username": "aisha.khan",
    "email": "aisha.khan@northwind.example",
    "real_name": "Aisha Khan",
    "display_name": "Aisha",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "messages": []
 },
 {
  "id": "1790067633.000743",
  "message_id": "1790067633.000743",
  "ts": "1790067633.000743",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 41 passed.",
  "created_at": "2026-09-22T09:00:33Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:00:33+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:00:33-07:00",
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
  "messages": []
 },
 {
  "id": "1790067794.000744",
  "message_id": "1790067794.000744",
  "ts": "1790067794.000744",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 42 passed.",
  "created_at": "2026-09-22T09:03:14Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:03:14+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:03:14-07:00",
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
  "messages": []
 },
 {
  "id": "1790067956.000745",
  "message_id": "1790067956.000745",
  "ts": "1790067956.000745",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments launch checklist check 43 passed.",
  "created_at": "2026-09-22T09:05:56Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:05:56+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:05:56-07:00",
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
  "messages": []
 },
 {
  "id": "1790068118.000746",
  "message_id": "1790068118.000746",
  "ts": "1790068118.000746",
  "channel_id": "C_LAUNCH",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Payments launch checklist check 44 passed.",
  "created_at": "2026-09-22T09:08:38Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:08:38+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:08:38-07:00",
  "users": [
   {
    "user_id": "U_AISHA",
    "username": "aisha.khan",
    "email": "aisha.khan@northwind.example",
    "real_name": "Aisha Khan",
    "display_name": "Aisha",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "messages": []
 },
 {
  "id": "1790068280.000747",
  "message_id": "1790068280.000747",
  "ts": "1790068280.000747",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 45 passed.",
  "created_at": "2026-09-22T09:11:20Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:11:20+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:11:20-07:00",
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
  "messages": []
 },
 {
  "id": "1790068442.000748",
  "message_id": "1790068442.000748",
  "ts": "1790068442.000748",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 46 passed.",
  "created_at": "2026-09-22T09:14:02Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:14:02+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:14:02-07:00",
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
  "messages": []
 },
 {
  "id": "1790068603.000749",
  "message_id": "1790068603.000749",
  "ts": "1790068603.000749",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments launch checklist check 47 passed.",
  "created_at": "2026-09-22T09:16:43Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:16:43+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:16:43-07:00",
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
  "messages": []
 },
 {
  "id": "1790068765.000750",
  "message_id": "1790068765.000750",
  "ts": "1790068765.000750",
  "channel_id": "C_LAUNCH",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Payments launch checklist check 48 passed.",
  "created_at": "2026-09-22T09:19:25Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:19:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:19:25-07:00",
  "users": [
   {
    "user_id": "U_AISHA",
    "username": "aisha.khan",
    "email": "aisha.khan@northwind.example",
    "real_name": "Aisha Khan",
    "display_name": "Aisha",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "messages": []
 },
 {
  "id": "1790068927.000751",
  "message_id": "1790068927.000751",
  "ts": "1790068927.000751",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 49 passed.",
  "created_at": "2026-09-22T09:22:07Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:22:07+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:22:07-07:00",
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
  "messages": []
 },
 {
  "id": "1790069089.000752",
  "message_id": "1790069089.000752",
  "ts": "1790069089.000752",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 50 passed.",
  "created_at": "2026-09-22T09:24:49Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:24:49+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:24:49-07:00",
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
  "messages": []
 },
 {
  "id": "1790069251.000753",
  "message_id": "1790069251.000753",
  "ts": "1790069251.000753",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments launch checklist check 51 passed.",
  "created_at": "2026-09-22T09:27:31Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:27:31+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:27:31-07:00",
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
  "messages": []
 },
 {
  "id": "1790069412.000754",
  "message_id": "1790069412.000754",
  "ts": "1790069412.000754",
  "channel_id": "C_LAUNCH",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Payments launch checklist check 52 passed.",
  "created_at": "2026-09-22T09:30:12Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:30:12+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:30:12-07:00",
  "users": [
   {
    "user_id": "U_AISHA",
    "username": "aisha.khan",
    "email": "aisha.khan@northwind.example",
    "real_name": "Aisha Khan",
    "display_name": "Aisha",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "messages": []
 },
 {
  "id": "1790069574.000755",
  "message_id": "1790069574.000755",
  "ts": "1790069574.000755",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 53 passed.",
  "created_at": "2026-09-22T09:32:54Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:32:54+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:32:54-07:00",
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
  "messages": []
 },
 {
  "id": "1790069736.000756",
  "message_id": "1790069736.000756",
  "ts": "1790069736.000756",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 54 passed.",
  "created_at": "2026-09-22T09:35:36Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:35:36+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:35:36-07:00",
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
  "messages": []
 },
 {
  "id": "1790069898.000757",
  "message_id": "1790069898.000757",
  "ts": "1790069898.000757",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments launch checklist check 55 passed.",
  "created_at": "2026-09-22T09:38:18Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:38:18+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:38:18-07:00",
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
  "messages": []
 },
 {
  "id": "1790070059.000758",
  "message_id": "1790070059.000758",
  "ts": "1790070059.000758",
  "channel_id": "C_LAUNCH",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Payments launch checklist check 56 passed.",
  "created_at": "2026-09-22T09:40:59Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:40:59+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:40:59-07:00",
  "users": [
   {
    "user_id": "U_AISHA",
    "username": "aisha.khan",
    "email": "aisha.khan@northwind.example",
    "real_name": "Aisha Khan",
    "display_name": "Aisha",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "messages": []
 },
 {
  "id": "1790070221.000759",
  "message_id": "1790070221.000759",
  "ts": "1790070221.000759",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 57 passed.",
  "created_at": "2026-09-22T09:43:41Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:43:41+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:43:41-07:00",
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
  "messages": []
 },
 {
  "id": "1790070383.000760",
  "message_id": "1790070383.000760",
  "ts": "1790070383.000760",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 58 passed.",
  "created_at": "2026-09-22T09:46:23Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:46:23+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:46:23-07:00",
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
  "messages": []
 },
 {
  "id": "1790070545.000761",
  "message_id": "1790070545.000761",
  "ts": "1790070545.000761",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments launch checklist check 59 passed.",
  "created_at": "2026-09-22T09:49:05Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:49:05+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:49:05-07:00",
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
  "messages": []
 },
 {
  "id": "1790070707.000762",
  "message_id": "1790070707.000762",
  "ts": "1790070707.000762",
  "channel_id": "C_LAUNCH",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Payments launch checklist check 60 passed.",
  "created_at": "2026-09-22T09:51:47Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:51:47+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:51:47-07:00",
  "users": [
   {
    "user_id": "U_AISHA",
    "username": "aisha.khan",
    "email": "aisha.khan@northwind.example",
    "real_name": "Aisha Khan",
    "display_name": "Aisha",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "messages": []
 },
 {
  "id": "1790070868.000763",
  "message_id": "1790070868.000763",
  "ts": "1790070868.000763",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 61 passed.",
  "created_at": "2026-09-22T09:54:28Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:54:28+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:54:28-07:00",
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
  "messages": []
 },
 {
  "id": "1790071030.000764",
  "message_id": "1790071030.000764",
  "ts": "1790071030.000764",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 62 passed.",
  "created_at": "2026-09-22T09:57:10Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:57:10+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:57:10-07:00",
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
  "messages": []
 },
 {
  "id": "1790071192.000765",
  "message_id": "1790071192.000765",
  "ts": "1790071192.000765",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments launch checklist check 63 passed.",
  "created_at": "2026-09-22T09:59:52Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T09:59:52+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T02:59:52-07:00",
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
  "messages": []
 },
 {
  "id": "1790071354.000766",
  "message_id": "1790071354.000766",
  "ts": "1790071354.000766",
  "channel_id": "C_LAUNCH",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Payments launch checklist check 64 passed.",
  "created_at": "2026-09-22T10:02:34Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:02:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:02:34-07:00",
  "users": [
   {
    "user_id": "U_AISHA",
    "username": "aisha.khan",
    "email": "aisha.khan@northwind.example",
    "real_name": "Aisha Khan",
    "display_name": "Aisha",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "messages": []
 },
 {
  "id": "1790071516.000767",
  "message_id": "1790071516.000767",
  "ts": "1790071516.000767",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 65 passed.",
  "created_at": "2026-09-22T10:05:16Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:05:16+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:05:16-07:00",
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
  "messages": []
 },
 {
  "id": "1790071677.000768",
  "message_id": "1790071677.000768",
  "ts": "1790071677.000768",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 66 passed.",
  "created_at": "2026-09-22T10:07:57Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:07:57+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:07:57-07:00",
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
  "messages": []
 },
 {
  "id": "1790071839.000769",
  "message_id": "1790071839.000769",
  "ts": "1790071839.000769",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments launch checklist check 67 passed.",
  "created_at": "2026-09-22T10:10:39Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:10:39+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:10:39-07:00",
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
  "messages": []
 },
 {
  "id": "1790072001.000770",
  "message_id": "1790072001.000770",
  "ts": "1790072001.000770",
  "channel_id": "C_LAUNCH",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Payments launch checklist check 68 passed.",
  "created_at": "2026-09-22T10:13:21Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:13:21+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:13:21-07:00",
  "users": [
   {
    "user_id": "U_AISHA",
    "username": "aisha.khan",
    "email": "aisha.khan@northwind.example",
    "real_name": "Aisha Khan",
    "display_name": "Aisha",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "messages": []
 },
 {
  "id": "1790072163.000771",
  "message_id": "1790072163.000771",
  "ts": "1790072163.000771",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 69 passed.",
  "created_at": "2026-09-22T10:16:03Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:16:03+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:16:03-07:00",
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
  "messages": []
 },
 {
  "id": "1790072324.000772",
  "message_id": "1790072324.000772",
  "ts": "1790072324.000772",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 70 passed.",
  "created_at": "2026-09-22T10:18:44Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:18:44+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:18:44-07:00",
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
  "messages": []
 },
 {
  "id": "1790072486.000773",
  "message_id": "1790072486.000773",
  "ts": "1790072486.000773",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments launch checklist check 71 passed.",
  "created_at": "2026-09-22T10:21:26Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:21:26+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:21:26-07:00",
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
  "messages": []
 },
 {
  "id": "1790072648.000774",
  "message_id": "1790072648.000774",
  "ts": "1790072648.000774",
  "channel_id": "C_LAUNCH",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Payments launch checklist check 72 passed.",
  "created_at": "2026-09-22T10:24:08Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:24:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:24:08-07:00",
  "users": [
   {
    "user_id": "U_AISHA",
    "username": "aisha.khan",
    "email": "aisha.khan@northwind.example",
    "real_name": "Aisha Khan",
    "display_name": "Aisha",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "messages": []
 },
 {
  "id": "1790072810.000775",
  "message_id": "1790072810.000775",
  "ts": "1790072810.000775",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 73 passed.",
  "created_at": "2026-09-22T10:26:50Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:26:50+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:26:50-07:00",
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
  "messages": []
 },
 {
  "id": "1790072972.000776",
  "message_id": "1790072972.000776",
  "ts": "1790072972.000776",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 74 passed.",
  "created_at": "2026-09-22T10:29:32Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:29:32+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:29:32-07:00",
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
  "messages": []
 },
 {
  "id": "1790073133.000777",
  "message_id": "1790073133.000777",
  "ts": "1790073133.000777",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments launch checklist check 75 passed.",
  "created_at": "2026-09-22T10:32:13Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:32:13+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:32:13-07:00",
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
  "messages": []
 },
 {
  "id": "1790073295.000778",
  "message_id": "1790073295.000778",
  "ts": "1790073295.000778",
  "channel_id": "C_LAUNCH",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Payments launch checklist check 76 passed.",
  "created_at": "2026-09-22T10:34:55Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:34:55+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:34:55-07:00",
  "users": [
   {
    "user_id": "U_AISHA",
    "username": "aisha.khan",
    "email": "aisha.khan@northwind.example",
    "real_name": "Aisha Khan",
    "display_name": "Aisha",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "messages": []
 },
 {
  "id": "1790073457.000779",
  "message_id": "1790073457.000779",
  "ts": "1790073457.000779",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 77 passed.",
  "created_at": "2026-09-22T10:37:37Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:37:37+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:37:37-07:00",
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
  "messages": []
 },
 {
  "id": "1790073619.000780",
  "message_id": "1790073619.000780",
  "ts": "1790073619.000780",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 78 passed.",
  "created_at": "2026-09-22T10:40:19Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:40:19+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:40:19-07:00",
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
  "messages": []
 },
 {
  "id": "1790073781.000781",
  "message_id": "1790073781.000781",
  "ts": "1790073781.000781",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments launch checklist check 79 passed.",
  "created_at": "2026-09-22T10:43:01Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:43:01+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:43:01-07:00",
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
  "messages": []
 },
 {
  "id": "1790073942.000782",
  "message_id": "1790073942.000782",
  "ts": "1790073942.000782",
  "channel_id": "C_LAUNCH",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Payments launch checklist check 80 passed.",
  "created_at": "2026-09-22T10:45:42Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:45:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:45:42-07:00",
  "users": [
   {
    "user_id": "U_AISHA",
    "username": "aisha.khan",
    "email": "aisha.khan@northwind.example",
    "real_name": "Aisha Khan",
    "display_name": "Aisha",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "messages": []
 },
 {
  "id": "1790074104.000783",
  "message_id": "1790074104.000783",
  "ts": "1790074104.000783",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 81 passed.",
  "created_at": "2026-09-22T10:48:24Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:48:24+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:48:24-07:00",
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
  "messages": []
 },
 {
  "id": "1790074266.000784",
  "message_id": "1790074266.000784",
  "ts": "1790074266.000784",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 82 passed.",
  "created_at": "2026-09-22T10:51:06Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:51:06+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:51:06-07:00",
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
  "messages": []
 },
 {
  "id": "1790074428.000785",
  "message_id": "1790074428.000785",
  "ts": "1790074428.000785",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments launch checklist check 83 passed.",
  "created_at": "2026-09-22T10:53:48Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:53:48+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:53:48-07:00",
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
  "messages": []
 },
 {
  "id": "1790074589.000786",
  "message_id": "1790074589.000786",
  "ts": "1790074589.000786",
  "channel_id": "C_LAUNCH",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Payments launch checklist check 84 passed.",
  "created_at": "2026-09-22T10:56:29Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:56:29+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:56:29-07:00",
  "users": [
   {
    "user_id": "U_AISHA",
    "username": "aisha.khan",
    "email": "aisha.khan@northwind.example",
    "real_name": "Aisha Khan",
    "display_name": "Aisha",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "messages": []
 },
 {
  "id": "1790074751.000787",
  "message_id": "1790074751.000787",
  "ts": "1790074751.000787",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 85 passed.",
  "created_at": "2026-09-22T10:59:11Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T10:59:11+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T03:59:11-07:00",
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
  "messages": []
 },
 {
  "id": "1790074913.000788",
  "message_id": "1790074913.000788",
  "ts": "1790074913.000788",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 86 passed.",
  "created_at": "2026-09-22T11:01:53Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:01:53+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:01:53-07:00",
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
  "messages": []
 },
 {
  "id": "1790075075.000789",
  "message_id": "1790075075.000789",
  "ts": "1790075075.000789",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments launch checklist check 87 passed.",
  "created_at": "2026-09-22T11:04:35Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:04:35+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:04:35-07:00",
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
  "messages": []
 },
 {
  "id": "1790075237.000790",
  "message_id": "1790075237.000790",
  "ts": "1790075237.000790",
  "channel_id": "C_LAUNCH",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Payments launch checklist check 88 passed.",
  "created_at": "2026-09-22T11:07:17Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:07:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:07:17-07:00",
  "users": [
   {
    "user_id": "U_AISHA",
    "username": "aisha.khan",
    "email": "aisha.khan@northwind.example",
    "real_name": "Aisha Khan",
    "display_name": "Aisha",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "messages": []
 },
 {
  "id": "1790075398.000791",
  "message_id": "1790075398.000791",
  "ts": "1790075398.000791",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 89 passed.",
  "created_at": "2026-09-22T11:09:58Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:09:58+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:09:58-07:00",
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
  "messages": []
 },
 {
  "id": "1790075560.000792",
  "message_id": "1790075560.000792",
  "ts": "1790075560.000792",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 90 passed.",
  "created_at": "2026-09-22T11:12:40Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:12:40+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:12:40-07:00",
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
  "messages": []
 },
 {
  "id": "1790075722.000793",
  "message_id": "1790075722.000793",
  "ts": "1790075722.000793",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments launch checklist check 91 passed.",
  "created_at": "2026-09-22T11:15:22Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:15:22+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:15:22-07:00",
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
  "messages": []
 },
 {
  "id": "1790075884.000794",
  "message_id": "1790075884.000794",
  "ts": "1790075884.000794",
  "channel_id": "C_LAUNCH",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Payments launch checklist check 92 passed.",
  "created_at": "2026-09-22T11:18:04Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:18:04+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:18:04-07:00",
  "users": [
   {
    "user_id": "U_AISHA",
    "username": "aisha.khan",
    "email": "aisha.khan@northwind.example",
    "real_name": "Aisha Khan",
    "display_name": "Aisha",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "messages": []
 },
 {
  "id": "1790076046.000795",
  "message_id": "1790076046.000795",
  "ts": "1790076046.000795",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 93 passed.",
  "created_at": "2026-09-22T11:20:46Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:20:46+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:20:46-07:00",
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
  "messages": []
 },
 {
  "id": "1790076207.000796",
  "message_id": "1790076207.000796",
  "ts": "1790076207.000796",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 94 passed.",
  "created_at": "2026-09-22T11:23:27Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:23:27+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:23:27-07:00",
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
  "messages": []
 },
 {
  "id": "1790076369.000797",
  "message_id": "1790076369.000797",
  "ts": "1790076369.000797",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments launch checklist check 95 passed.",
  "created_at": "2026-09-22T11:26:09Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:26:09+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:26:09-07:00",
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
  "messages": []
 },
 {
  "id": "1790076531.000798",
  "message_id": "1790076531.000798",
  "ts": "1790076531.000798",
  "channel_id": "C_LAUNCH",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Payments launch checklist check 96 passed.",
  "created_at": "2026-09-22T11:28:51Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:28:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:28:51-07:00",
  "users": [
   {
    "user_id": "U_AISHA",
    "username": "aisha.khan",
    "email": "aisha.khan@northwind.example",
    "real_name": "Aisha Khan",
    "display_name": "Aisha",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "messages": []
 },
 {
  "id": "1790076693.000799",
  "message_id": "1790076693.000799",
  "ts": "1790076693.000799",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 97 passed.",
  "created_at": "2026-09-22T11:31:33Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:31:33+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:31:33-07:00",
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
  "messages": []
 },
 {
  "id": "1790076854.000800",
  "message_id": "1790076854.000800",
  "ts": "1790076854.000800",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 98 passed.",
  "created_at": "2026-09-22T11:34:14Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:34:14+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:34:14-07:00",
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
  "messages": []
 },
 {
  "id": "1790077016.000801",
  "message_id": "1790077016.000801",
  "ts": "1790077016.000801",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments launch checklist check 99 passed.",
  "created_at": "2026-09-22T11:36:56Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:36:56+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:36:56-07:00",
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
  "messages": []
 },
 {
  "id": "1790077178.000802",
  "message_id": "1790077178.000802",
  "ts": "1790077178.000802",
  "channel_id": "C_LAUNCH",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Payments launch checklist check 100 passed.",
  "created_at": "2026-09-22T11:39:38Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:39:38+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:39:38-07:00",
  "users": [
   {
    "user_id": "U_AISHA",
    "username": "aisha.khan",
    "email": "aisha.khan@northwind.example",
    "real_name": "Aisha Khan",
    "display_name": "Aisha",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "messages": []
 },
 {
  "id": "1790077340.000803",
  "message_id": "1790077340.000803",
  "ts": "1790077340.000803",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 101 passed.",
  "created_at": "2026-09-22T11:42:20Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:42:20+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:42:20-07:00",
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
  "messages": []
 },
 {
  "id": "1790077502.000804",
  "message_id": "1790077502.000804",
  "ts": "1790077502.000804",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 102 passed.",
  "created_at": "2026-09-22T11:45:02Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:45:02+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:45:02-07:00",
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
  "messages": []
 },
 {
  "id": "1790077663.000805",
  "message_id": "1790077663.000805",
  "ts": "1790077663.000805",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments launch checklist check 103 passed.",
  "created_at": "2026-09-22T11:47:43Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:47:43+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:47:43-07:00",
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
  "messages": []
 },
 {
  "id": "1790077825.000806",
  "message_id": "1790077825.000806",
  "ts": "1790077825.000806",
  "channel_id": "C_LAUNCH",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Payments launch checklist check 104 passed.",
  "created_at": "2026-09-22T11:50:25Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:50:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:50:25-07:00",
  "users": [
   {
    "user_id": "U_AISHA",
    "username": "aisha.khan",
    "email": "aisha.khan@northwind.example",
    "real_name": "Aisha Khan",
    "display_name": "Aisha",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "messages": []
 },
 {
  "id": "1790077987.000807",
  "message_id": "1790077987.000807",
  "ts": "1790077987.000807",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 105 passed.",
  "created_at": "2026-09-22T11:53:07Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:53:07+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:53:07-07:00",
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
  "messages": []
 },
 {
  "id": "1790078149.000808",
  "message_id": "1790078149.000808",
  "ts": "1790078149.000808",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 106 passed.",
  "created_at": "2026-09-22T11:55:49Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:55:49+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:55:49-07:00",
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
  "messages": []
 },
 {
  "id": "1790078311.000809",
  "message_id": "1790078311.000809",
  "ts": "1790078311.000809",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payments launch checklist check 107 passed.",
  "created_at": "2026-09-22T11:58:31Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T11:58:31+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T04:58:31-07:00",
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
  "messages": []
 },
 {
  "id": "1790078472.000810",
  "message_id": "1790078472.000810",
  "ts": "1790078472.000810",
  "channel_id": "C_LAUNCH",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Payments launch checklist check 108 passed.",
  "created_at": "2026-09-22T12:01:12Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T12:01:12+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T05:01:12-07:00",
  "users": [
   {
    "user_id": "U_AISHA",
    "username": "aisha.khan",
    "email": "aisha.khan@northwind.example",
    "real_name": "Aisha Khan",
    "display_name": "Aisha",
    "created_at": "2025-01-01T00:05:00Z",
    "is_bot": false,
    "is_active": true
   }
  ],
  "messages": []
 },
 {
  "id": "1790078634.000811",
  "message_id": "1790078634.000811",
  "ts": "1790078634.000811",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Payments launch checklist check 109 passed.",
  "created_at": "2026-09-22T12:03:54Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T12:03:54+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T05:03:54-07:00",
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
  "messages": []
 },
 {
  "id": "1790078796.000812",
  "message_id": "1790078796.000812",
  "ts": "1790078796.000812",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payments launch checklist check 110 passed.",
  "created_at": "2026-09-22T12:06:36Z",
  "channel": "launch-prep",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-22T12:06:36+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-22T05:06:36-07:00",
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
  "messages": []
 }
]
