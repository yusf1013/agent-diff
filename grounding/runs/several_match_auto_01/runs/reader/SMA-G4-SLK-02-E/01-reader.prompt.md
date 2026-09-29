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
  "id": "1789992240.000702",
  "message_id": "1789992240.000702",
  "channel_id": "C_LAUNCH",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "The release checklist is locked, all owners signed off for Tuesday's push.",
  "ts": "1789992240.000702",
  "created_at": "2026-09-21T12:04:00Z",
  "channel": "launch-plan",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:04:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:04:00-07:00",
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
    "message_id": "1789992240.000702",
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
 }
]
