You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Slack workspace:

    "Add an eyes reaction to every release checklist message that Maya Chen posted in #launch-plan and that Diego Alvarez reacted to with thumbsup."

The user is Agent Bot. Below is every Slack message in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "1789992120.000001",
  "message_id": "1789992120.000001",
  "channel_id": "C_LAUNCH",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "The release checklist is final, all items signed off for Thursday's deploy.",
  "ts": "1789992120.000001",
  "created_at": "2026-09-21T12:02:00Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:02:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:02:00-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": [
   {
    "message_id": "1789992120.000001",
    "user_id": "U_DIEGO",
    "reaction_type": "thumbsup",
    "created_at": "2026-09-01T12:00:00Z",
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
    ]
   }
  ]
 },
 {
  "id": "1789992600.000002",
  "message_id": "1789992600.000002",
  "channel_id": "C_LAUNCH",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Reminder: the release checklist for Thursday is pinned above, please review it.",
  "ts": "1789992600.000002",
  "created_at": "2026-09-21T12:10:00Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:10:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:10:00-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": [
   {
    "message_id": "1789992600.000002",
    "user_id": "U_DIEGO",
    "reaction_type": "tada",
    "created_at": "2026-09-01T12:00:00Z",
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
    ]
   },
   {
    "message_id": "1789992600.000002",
    "user_id": "U_LEO",
    "reaction_type": "thumbsup",
    "created_at": "2026-09-01T12:00:00Z",
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
    ]
   }
  ]
 },
 {
  "id": "1789992960.000003",
  "message_id": "1789992960.000003",
  "channel_id": "C_LAUNCH",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Updated the release checklist with the rollback steps.",
  "ts": "1789992960.000003",
  "created_at": "2026-09-21T12:16:00Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:16:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:16:00-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": [
   {
    "message_id": "1789992960.000003",
    "user_id": "U_DIEGO",
    "reaction_type": "thumbsdown",
    "created_at": "2026-09-01T12:00:00Z",
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
    ]
   }
  ]
 },
 {
  "id": "1789993200.000004",
  "message_id": "1789993200.000004",
  "channel_id": "C_RANDOM",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Cross-posting the release checklist for Thursday's deploy.",
  "ts": "1789993200.000004",
  "created_at": "2026-09-21T12:20:00Z",
  "channel": "random",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:20:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:20:00-07:00",
  "channels": [
   {
    "channel_id": "C_RANDOM",
    "channel_name": "random",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": [
   {
    "message_id": "1789993200.000004",
    "user_id": "U_DIEGO",
    "reaction_type": "thumbsup",
    "created_at": "2026-09-01T12:00:00Z",
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
    ]
   }
  ]
 },
 {
  "id": "1789993440.000005",
  "message_id": "1789993440.000005",
  "channel_id": "C_LAUNCH",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Team lunch rota for next week is up, add your preferences.",
  "ts": "1789993440.000005",
  "created_at": "2026-09-21T12:24:00Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:24:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:24:00-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": [
   {
    "message_id": "1789993440.000005",
    "user_id": "U_PRIYA",
    "reaction_type": "fire",
    "created_at": "2026-09-01T12:00:00Z",
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
    ]
   }
  ]
 },
 {
  "id": "1789993680.000006",
  "message_id": "1789993680.000006",
  "channel_id": "C_LAUNCH",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "My copy of the release checklist for Thursday, working through it now.",
  "ts": "1789993680.000006",
  "created_at": "2026-09-21T12:28:00Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:28:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:28:00-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": [
   {
    "message_id": "1789993680.000006",
    "user_id": "U_DIEGO",
    "reaction_type": "clap",
    "created_at": "2026-09-01T12:00:00Z",
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
    ]
   }
  ]
 },
 {
  "id": "1789992180.000701",
  "message_id": "1789992180.000701",
  "channel_id": "C_LAUNCH",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "The release checklist is done, all items approved for Friday's deploy.",
  "ts": "1789992180.000701",
  "created_at": "2026-09-21T12:03:00Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:03:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:03:00-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": [
   {
    "message_id": "1789992180.000701",
    "user_id": "U_DIEGO",
    "reaction_type": "thumbsup",
    "created_at": "2026-09-01T12:00:00Z",
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
    ]
   }
  ]
 },
 {
  "id": "1789974600.000702",
  "message_id": "1789974600.000702",
  "channel_id": "C_LAUNCH",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "The release checklist is done, all items approved for Friday's deploy.",
  "ts": "1789974600.000702",
  "created_at": "2026-09-21T07:10:00Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:10:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:10:00-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": [
   {
    "message_id": "1789974600.000702",
    "user_id": "U_DIEGO",
    "reaction_type": "thumbsup",
    "created_at": "2026-09-01T12:00:00Z",
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
    ]
   }
  ]
 },
 {
  "id": "1789974756.000703",
  "message_id": "1789974756.000703",
  "ts": "1789974756.000703",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 1 passed.",
  "created_at": "2026-09-21T07:12:36Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:12:36+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:12:36-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789974912.000704",
  "message_id": "1789974912.000704",
  "ts": "1789974912.000704",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 2 passed.",
  "created_at": "2026-09-21T07:15:12Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:15:12+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:15:12-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789975069.000705",
  "message_id": "1789975069.000705",
  "ts": "1789975069.000705",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Release checklist check 3 passed.",
  "created_at": "2026-09-21T07:17:49Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:17:49+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:17:49-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789975225.000706",
  "message_id": "1789975225.000706",
  "ts": "1789975225.000706",
  "channel_id": "C_LAUNCH",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Release checklist check 4 passed.",
  "created_at": "2026-09-21T07:20:25Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:20:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:20:25-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789975382.000707",
  "message_id": "1789975382.000707",
  "ts": "1789975382.000707",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 5 passed.",
  "created_at": "2026-09-21T07:23:02Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:23:02+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:23:02-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789975538.000708",
  "message_id": "1789975538.000708",
  "ts": "1789975538.000708",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 6 passed.",
  "created_at": "2026-09-21T07:25:38Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:25:38+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:25:38-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789975694.000709",
  "message_id": "1789975694.000709",
  "ts": "1789975694.000709",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Release checklist check 7 passed.",
  "created_at": "2026-09-21T07:28:14Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:28:14+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:28:14-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789975851.000710",
  "message_id": "1789975851.000710",
  "ts": "1789975851.000710",
  "channel_id": "C_LAUNCH",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Release checklist check 8 passed.",
  "created_at": "2026-09-21T07:30:51Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:30:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:30:51-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789976007.000711",
  "message_id": "1789976007.000711",
  "ts": "1789976007.000711",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 9 passed.",
  "created_at": "2026-09-21T07:33:27Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:33:27+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:33:27-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789976164.000712",
  "message_id": "1789976164.000712",
  "ts": "1789976164.000712",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 10 passed.",
  "created_at": "2026-09-21T07:36:04Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:36:04+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:36:04-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789976320.000713",
  "message_id": "1789976320.000713",
  "ts": "1789976320.000713",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Release checklist check 11 passed.",
  "created_at": "2026-09-21T07:38:40Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:38:40+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:38:40-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789976477.000714",
  "message_id": "1789976477.000714",
  "ts": "1789976477.000714",
  "channel_id": "C_LAUNCH",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Release checklist check 12 passed.",
  "created_at": "2026-09-21T07:41:17Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:41:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:41:17-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789976633.000715",
  "message_id": "1789976633.000715",
  "ts": "1789976633.000715",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 13 passed.",
  "created_at": "2026-09-21T07:43:53Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:43:53+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:43:53-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789976789.000716",
  "message_id": "1789976789.000716",
  "ts": "1789976789.000716",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 14 passed.",
  "created_at": "2026-09-21T07:46:29Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:46:29+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:46:29-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789976946.000717",
  "message_id": "1789976946.000717",
  "ts": "1789976946.000717",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Release checklist check 15 passed.",
  "created_at": "2026-09-21T07:49:06Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:49:06+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:49:06-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789977102.000718",
  "message_id": "1789977102.000718",
  "ts": "1789977102.000718",
  "channel_id": "C_LAUNCH",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Release checklist check 16 passed.",
  "created_at": "2026-09-21T07:51:42Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:51:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:51:42-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789977259.000719",
  "message_id": "1789977259.000719",
  "ts": "1789977259.000719",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 17 passed.",
  "created_at": "2026-09-21T07:54:19Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:54:19+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:54:19-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789977415.000720",
  "message_id": "1789977415.000720",
  "ts": "1789977415.000720",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 18 passed.",
  "created_at": "2026-09-21T07:56:55Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:56:55+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:56:55-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789977572.000721",
  "message_id": "1789977572.000721",
  "ts": "1789977572.000721",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Release checklist check 19 passed.",
  "created_at": "2026-09-21T07:59:32Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:59:32+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:59:32-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789977728.000722",
  "message_id": "1789977728.000722",
  "ts": "1789977728.000722",
  "channel_id": "C_LAUNCH",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Release checklist check 20 passed.",
  "created_at": "2026-09-21T08:02:08Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:02:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:02:08-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789977884.000723",
  "message_id": "1789977884.000723",
  "ts": "1789977884.000723",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 21 passed.",
  "created_at": "2026-09-21T08:04:44Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:04:44+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:04:44-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789978041.000724",
  "message_id": "1789978041.000724",
  "ts": "1789978041.000724",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 22 passed.",
  "created_at": "2026-09-21T08:07:21Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:07:21+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:07:21-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789978197.000725",
  "message_id": "1789978197.000725",
  "ts": "1789978197.000725",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Release checklist check 23 passed.",
  "created_at": "2026-09-21T08:09:57Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:09:57+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:09:57-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789978354.000726",
  "message_id": "1789978354.000726",
  "ts": "1789978354.000726",
  "channel_id": "C_LAUNCH",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Release checklist check 24 passed.",
  "created_at": "2026-09-21T08:12:34Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:12:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:12:34-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789978510.000727",
  "message_id": "1789978510.000727",
  "ts": "1789978510.000727",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 25 passed.",
  "created_at": "2026-09-21T08:15:10Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:15:10+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:15:10-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789978667.000728",
  "message_id": "1789978667.000728",
  "ts": "1789978667.000728",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 26 passed.",
  "created_at": "2026-09-21T08:17:47Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:17:47+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:17:47-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789978823.000729",
  "message_id": "1789978823.000729",
  "ts": "1789978823.000729",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Release checklist check 27 passed.",
  "created_at": "2026-09-21T08:20:23Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:20:23+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:20:23-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789978979.000730",
  "message_id": "1789978979.000730",
  "ts": "1789978979.000730",
  "channel_id": "C_LAUNCH",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Release checklist check 28 passed.",
  "created_at": "2026-09-21T08:22:59Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:22:59+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:22:59-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789979136.000731",
  "message_id": "1789979136.000731",
  "ts": "1789979136.000731",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 29 passed.",
  "created_at": "2026-09-21T08:25:36Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:25:36+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:25:36-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789979292.000732",
  "message_id": "1789979292.000732",
  "ts": "1789979292.000732",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 30 passed.",
  "created_at": "2026-09-21T08:28:12Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:28:12+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:28:12-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789979449.000733",
  "message_id": "1789979449.000733",
  "ts": "1789979449.000733",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Release checklist check 31 passed.",
  "created_at": "2026-09-21T08:30:49Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:30:49+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:30:49-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789979605.000734",
  "message_id": "1789979605.000734",
  "ts": "1789979605.000734",
  "channel_id": "C_LAUNCH",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Release checklist check 32 passed.",
  "created_at": "2026-09-21T08:33:25Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:33:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:33:25-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789979762.000735",
  "message_id": "1789979762.000735",
  "ts": "1789979762.000735",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 33 passed.",
  "created_at": "2026-09-21T08:36:02Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:36:02+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:36:02-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789979918.000736",
  "message_id": "1789979918.000736",
  "ts": "1789979918.000736",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 34 passed.",
  "created_at": "2026-09-21T08:38:38Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:38:38+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:38:38-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789980074.000737",
  "message_id": "1789980074.000737",
  "ts": "1789980074.000737",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Release checklist check 35 passed.",
  "created_at": "2026-09-21T08:41:14Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:41:14+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:41:14-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789980231.000738",
  "message_id": "1789980231.000738",
  "ts": "1789980231.000738",
  "channel_id": "C_LAUNCH",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Release checklist check 36 passed.",
  "created_at": "2026-09-21T08:43:51Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:43:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:43:51-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789980387.000739",
  "message_id": "1789980387.000739",
  "ts": "1789980387.000739",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 37 passed.",
  "created_at": "2026-09-21T08:46:27Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:46:27+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:46:27-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789980544.000740",
  "message_id": "1789980544.000740",
  "ts": "1789980544.000740",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 38 passed.",
  "created_at": "2026-09-21T08:49:04Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:49:04+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:49:04-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789980700.000741",
  "message_id": "1789980700.000741",
  "ts": "1789980700.000741",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Release checklist check 39 passed.",
  "created_at": "2026-09-21T08:51:40Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:51:40+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:51:40-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789980857.000742",
  "message_id": "1789980857.000742",
  "ts": "1789980857.000742",
  "channel_id": "C_LAUNCH",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Release checklist check 40 passed.",
  "created_at": "2026-09-21T08:54:17Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:54:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:54:17-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789981013.000743",
  "message_id": "1789981013.000743",
  "ts": "1789981013.000743",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 41 passed.",
  "created_at": "2026-09-21T08:56:53Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:56:53+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:56:53-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789981169.000744",
  "message_id": "1789981169.000744",
  "ts": "1789981169.000744",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 42 passed.",
  "created_at": "2026-09-21T08:59:29Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:59:29+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:59:29-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789981326.000745",
  "message_id": "1789981326.000745",
  "ts": "1789981326.000745",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Release checklist check 43 passed.",
  "created_at": "2026-09-21T09:02:06Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:02:06+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:02:06-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789981482.000746",
  "message_id": "1789981482.000746",
  "ts": "1789981482.000746",
  "channel_id": "C_LAUNCH",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Release checklist check 44 passed.",
  "created_at": "2026-09-21T09:04:42Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:04:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:04:42-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789981639.000747",
  "message_id": "1789981639.000747",
  "ts": "1789981639.000747",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 45 passed.",
  "created_at": "2026-09-21T09:07:19Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:07:19+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:07:19-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789981795.000748",
  "message_id": "1789981795.000748",
  "ts": "1789981795.000748",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 46 passed.",
  "created_at": "2026-09-21T09:09:55Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:09:55+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:09:55-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789981952.000749",
  "message_id": "1789981952.000749",
  "ts": "1789981952.000749",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Release checklist check 47 passed.",
  "created_at": "2026-09-21T09:12:32Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:12:32+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:12:32-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789982108.000750",
  "message_id": "1789982108.000750",
  "ts": "1789982108.000750",
  "channel_id": "C_LAUNCH",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Release checklist check 48 passed.",
  "created_at": "2026-09-21T09:15:08Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:15:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:15:08-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789982264.000751",
  "message_id": "1789982264.000751",
  "ts": "1789982264.000751",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 49 passed.",
  "created_at": "2026-09-21T09:17:44Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:17:44+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:17:44-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789982421.000752",
  "message_id": "1789982421.000752",
  "ts": "1789982421.000752",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 50 passed.",
  "created_at": "2026-09-21T09:20:21Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:20:21+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:20:21-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789982577.000753",
  "message_id": "1789982577.000753",
  "ts": "1789982577.000753",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Release checklist check 51 passed.",
  "created_at": "2026-09-21T09:22:57Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:22:57+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:22:57-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789982734.000754",
  "message_id": "1789982734.000754",
  "ts": "1789982734.000754",
  "channel_id": "C_LAUNCH",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Release checklist check 52 passed.",
  "created_at": "2026-09-21T09:25:34Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:25:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:25:34-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789982890.000755",
  "message_id": "1789982890.000755",
  "ts": "1789982890.000755",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 53 passed.",
  "created_at": "2026-09-21T09:28:10Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:28:10+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:28:10-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789983047.000756",
  "message_id": "1789983047.000756",
  "ts": "1789983047.000756",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 54 passed.",
  "created_at": "2026-09-21T09:30:47Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:30:47+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:30:47-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789983203.000757",
  "message_id": "1789983203.000757",
  "ts": "1789983203.000757",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Release checklist check 55 passed.",
  "created_at": "2026-09-21T09:33:23Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:33:23+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:33:23-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789983359.000758",
  "message_id": "1789983359.000758",
  "ts": "1789983359.000758",
  "channel_id": "C_LAUNCH",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Release checklist check 56 passed.",
  "created_at": "2026-09-21T09:35:59Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:35:59+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:35:59-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789983516.000759",
  "message_id": "1789983516.000759",
  "ts": "1789983516.000759",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 57 passed.",
  "created_at": "2026-09-21T09:38:36Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:38:36+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:38:36-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789983672.000760",
  "message_id": "1789983672.000760",
  "ts": "1789983672.000760",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 58 passed.",
  "created_at": "2026-09-21T09:41:12Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:41:12+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:41:12-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789983829.000761",
  "message_id": "1789983829.000761",
  "ts": "1789983829.000761",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Release checklist check 59 passed.",
  "created_at": "2026-09-21T09:43:49Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:43:49+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:43:49-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789983985.000762",
  "message_id": "1789983985.000762",
  "ts": "1789983985.000762",
  "channel_id": "C_LAUNCH",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Release checklist check 60 passed.",
  "created_at": "2026-09-21T09:46:25Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:46:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:46:25-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789984142.000763",
  "message_id": "1789984142.000763",
  "ts": "1789984142.000763",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 61 passed.",
  "created_at": "2026-09-21T09:49:02Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:49:02+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:49:02-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789984298.000764",
  "message_id": "1789984298.000764",
  "ts": "1789984298.000764",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 62 passed.",
  "created_at": "2026-09-21T09:51:38Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:51:38+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:51:38-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789984454.000765",
  "message_id": "1789984454.000765",
  "ts": "1789984454.000765",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Release checklist check 63 passed.",
  "created_at": "2026-09-21T09:54:14Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:54:14+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:54:14-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789984611.000766",
  "message_id": "1789984611.000766",
  "ts": "1789984611.000766",
  "channel_id": "C_LAUNCH",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Release checklist check 64 passed.",
  "created_at": "2026-09-21T09:56:51Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:56:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:56:51-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789984767.000767",
  "message_id": "1789984767.000767",
  "ts": "1789984767.000767",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 65 passed.",
  "created_at": "2026-09-21T09:59:27Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:59:27+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:59:27-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789984924.000768",
  "message_id": "1789984924.000768",
  "ts": "1789984924.000768",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 66 passed.",
  "created_at": "2026-09-21T10:02:04Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:02:04+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:02:04-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789985080.000769",
  "message_id": "1789985080.000769",
  "ts": "1789985080.000769",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Release checklist check 67 passed.",
  "created_at": "2026-09-21T10:04:40Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:04:40+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:04:40-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789985237.000770",
  "message_id": "1789985237.000770",
  "ts": "1789985237.000770",
  "channel_id": "C_LAUNCH",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Release checklist check 68 passed.",
  "created_at": "2026-09-21T10:07:17Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:07:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:07:17-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789985393.000771",
  "message_id": "1789985393.000771",
  "ts": "1789985393.000771",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 69 passed.",
  "created_at": "2026-09-21T10:09:53Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:09:53+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:09:53-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789985549.000772",
  "message_id": "1789985549.000772",
  "ts": "1789985549.000772",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 70 passed.",
  "created_at": "2026-09-21T10:12:29Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:12:29+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:12:29-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789985706.000773",
  "message_id": "1789985706.000773",
  "ts": "1789985706.000773",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Release checklist check 71 passed.",
  "created_at": "2026-09-21T10:15:06Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:15:06+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:15:06-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789985862.000774",
  "message_id": "1789985862.000774",
  "ts": "1789985862.000774",
  "channel_id": "C_LAUNCH",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Release checklist check 72 passed.",
  "created_at": "2026-09-21T10:17:42Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:17:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:17:42-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789986019.000775",
  "message_id": "1789986019.000775",
  "ts": "1789986019.000775",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 73 passed.",
  "created_at": "2026-09-21T10:20:19Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:20:19+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:20:19-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789986175.000776",
  "message_id": "1789986175.000776",
  "ts": "1789986175.000776",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 74 passed.",
  "created_at": "2026-09-21T10:22:55Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:22:55+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:22:55-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789986332.000777",
  "message_id": "1789986332.000777",
  "ts": "1789986332.000777",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Release checklist check 75 passed.",
  "created_at": "2026-09-21T10:25:32Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:25:32+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:25:32-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789986488.000778",
  "message_id": "1789986488.000778",
  "ts": "1789986488.000778",
  "channel_id": "C_LAUNCH",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Release checklist check 76 passed.",
  "created_at": "2026-09-21T10:28:08Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:28:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:28:08-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789986644.000779",
  "message_id": "1789986644.000779",
  "ts": "1789986644.000779",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 77 passed.",
  "created_at": "2026-09-21T10:30:44Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:30:44+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:30:44-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789986801.000780",
  "message_id": "1789986801.000780",
  "ts": "1789986801.000780",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 78 passed.",
  "created_at": "2026-09-21T10:33:21Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:33:21+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:33:21-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789986957.000781",
  "message_id": "1789986957.000781",
  "ts": "1789986957.000781",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Release checklist check 79 passed.",
  "created_at": "2026-09-21T10:35:57Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:35:57+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:35:57-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789987114.000782",
  "message_id": "1789987114.000782",
  "ts": "1789987114.000782",
  "channel_id": "C_LAUNCH",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Release checklist check 80 passed.",
  "created_at": "2026-09-21T10:38:34Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:38:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:38:34-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789987270.000783",
  "message_id": "1789987270.000783",
  "ts": "1789987270.000783",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 81 passed.",
  "created_at": "2026-09-21T10:41:10Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:41:10+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:41:10-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789987427.000784",
  "message_id": "1789987427.000784",
  "ts": "1789987427.000784",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 82 passed.",
  "created_at": "2026-09-21T10:43:47Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:43:47+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:43:47-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789987583.000785",
  "message_id": "1789987583.000785",
  "ts": "1789987583.000785",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Release checklist check 83 passed.",
  "created_at": "2026-09-21T10:46:23Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:46:23+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:46:23-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789987739.000786",
  "message_id": "1789987739.000786",
  "ts": "1789987739.000786",
  "channel_id": "C_LAUNCH",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Release checklist check 84 passed.",
  "created_at": "2026-09-21T10:48:59Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:48:59+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:48:59-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789987896.000787",
  "message_id": "1789987896.000787",
  "ts": "1789987896.000787",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 85 passed.",
  "created_at": "2026-09-21T10:51:36Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:51:36+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:51:36-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789988052.000788",
  "message_id": "1789988052.000788",
  "ts": "1789988052.000788",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 86 passed.",
  "created_at": "2026-09-21T10:54:12Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:54:12+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:54:12-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789988209.000789",
  "message_id": "1789988209.000789",
  "ts": "1789988209.000789",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Release checklist check 87 passed.",
  "created_at": "2026-09-21T10:56:49Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:56:49+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:56:49-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789988365.000790",
  "message_id": "1789988365.000790",
  "ts": "1789988365.000790",
  "channel_id": "C_LAUNCH",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Release checklist check 88 passed.",
  "created_at": "2026-09-21T10:59:25Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:59:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:59:25-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789988522.000791",
  "message_id": "1789988522.000791",
  "ts": "1789988522.000791",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 89 passed.",
  "created_at": "2026-09-21T11:02:02Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:02:02+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:02:02-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789988678.000792",
  "message_id": "1789988678.000792",
  "ts": "1789988678.000792",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 90 passed.",
  "created_at": "2026-09-21T11:04:38Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:04:38+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:04:38-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789988834.000793",
  "message_id": "1789988834.000793",
  "ts": "1789988834.000793",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Release checklist check 91 passed.",
  "created_at": "2026-09-21T11:07:14Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:07:14+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:07:14-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789988991.000794",
  "message_id": "1789988991.000794",
  "ts": "1789988991.000794",
  "channel_id": "C_LAUNCH",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Release checklist check 92 passed.",
  "created_at": "2026-09-21T11:09:51Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:09:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:09:51-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789989147.000795",
  "message_id": "1789989147.000795",
  "ts": "1789989147.000795",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 93 passed.",
  "created_at": "2026-09-21T11:12:27Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:12:27+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:12:27-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789989304.000796",
  "message_id": "1789989304.000796",
  "ts": "1789989304.000796",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 94 passed.",
  "created_at": "2026-09-21T11:15:04Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:15:04+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:15:04-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789989460.000797",
  "message_id": "1789989460.000797",
  "ts": "1789989460.000797",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Release checklist check 95 passed.",
  "created_at": "2026-09-21T11:17:40Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:17:40+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:17:40-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789989617.000798",
  "message_id": "1789989617.000798",
  "ts": "1789989617.000798",
  "channel_id": "C_LAUNCH",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Release checklist check 96 passed.",
  "created_at": "2026-09-21T11:20:17Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:20:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:20:17-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789989773.000799",
  "message_id": "1789989773.000799",
  "ts": "1789989773.000799",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 97 passed.",
  "created_at": "2026-09-21T11:22:53Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:22:53+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:22:53-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789989929.000800",
  "message_id": "1789989929.000800",
  "ts": "1789989929.000800",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 98 passed.",
  "created_at": "2026-09-21T11:25:29Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:25:29+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:25:29-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789990086.000801",
  "message_id": "1789990086.000801",
  "ts": "1789990086.000801",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Release checklist check 99 passed.",
  "created_at": "2026-09-21T11:28:06Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:28:06+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:28:06-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789990242.000802",
  "message_id": "1789990242.000802",
  "ts": "1789990242.000802",
  "channel_id": "C_LAUNCH",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Release checklist check 100 passed.",
  "created_at": "2026-09-21T11:30:42Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:30:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:30:42-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789990399.000803",
  "message_id": "1789990399.000803",
  "ts": "1789990399.000803",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 101 passed.",
  "created_at": "2026-09-21T11:33:19Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:33:19+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:33:19-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789990555.000804",
  "message_id": "1789990555.000804",
  "ts": "1789990555.000804",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 102 passed.",
  "created_at": "2026-09-21T11:35:55Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:35:55+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:35:55-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789990712.000805",
  "message_id": "1789990712.000805",
  "ts": "1789990712.000805",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Release checklist check 103 passed.",
  "created_at": "2026-09-21T11:38:32Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:38:32+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:38:32-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789990868.000806",
  "message_id": "1789990868.000806",
  "ts": "1789990868.000806",
  "channel_id": "C_LAUNCH",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Release checklist check 104 passed.",
  "created_at": "2026-09-21T11:41:08Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:41:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:41:08-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789991024.000807",
  "message_id": "1789991024.000807",
  "ts": "1789991024.000807",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 105 passed.",
  "created_at": "2026-09-21T11:43:44Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:43:44+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:43:44-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789991181.000808",
  "message_id": "1789991181.000808",
  "ts": "1789991181.000808",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 106 passed.",
  "created_at": "2026-09-21T11:46:21Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:46:21+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:46:21-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789991337.000809",
  "message_id": "1789991337.000809",
  "ts": "1789991337.000809",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Release checklist check 107 passed.",
  "created_at": "2026-09-21T11:48:57Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:48:57+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:48:57-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789991494.000810",
  "message_id": "1789991494.000810",
  "ts": "1789991494.000810",
  "channel_id": "C_LAUNCH",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Release checklist check 108 passed.",
  "created_at": "2026-09-21T11:51:34Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:51:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:51:34-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789991650.000811",
  "message_id": "1789991650.000811",
  "ts": "1789991650.000811",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Release checklist check 109 passed.",
  "created_at": "2026-09-21T11:54:10Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:54:10+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:54:10-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 },
 {
  "id": "1789991807.000812",
  "message_id": "1789991807.000812",
  "ts": "1789991807.000812",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Release checklist check 110 passed.",
  "created_at": "2026-09-21T11:56:47Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:56:47+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:56:47-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-plan",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
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
  "message_reactions": []
 }
]
