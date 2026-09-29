You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Slack workspace:

    "Add the eyes reaction to all of Maya Chen's messages about the deploy checklist in my direct message with Maya Chen."

The user is Agent Bot. Below is every Slack message in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "1789992300.000001",
  "message_id": "1789992300.000001",
  "channel_id": "D_MAYA",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Deploy checklist for Friday is ready: env, flags, rollback plan.",
  "ts": "1789992300.000001",
  "created_at": "2026-09-21T12:05:00Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T12:05:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:05:00-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789993200.000002",
  "message_id": "1789993200.000002",
  "channel_id": "C_DEPLOY",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Deploy checklist for Friday is ready: env, flags, rollback plan. Flagging for the room.",
  "ts": "1789993200.000002",
  "created_at": "2026-09-21T12:20:00Z",
  "channel": "deployments",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:20:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:20:00-07:00",
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
    "channel_id": "C_DEPLOY",
    "channel_name": "deployments",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "C_DEPLOY",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "C_DEPLOY",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "C_DEPLOY",
      "user_id": "U_LEO",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "C_DEPLOY",
      "user_id": "U_DIEGO",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789993800.000003",
  "message_id": "1789993800.000003",
  "channel_id": "G_MAYALEO",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Deploy checklist for Friday is ready: env, flags, rollback plan. Leo looping you in.",
  "ts": "1789993800.000003",
  "created_at": "2026-09-21T12:30:00Z",
  "channel": "maya-leo-group",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:30:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:30:00-07:00",
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
    "channel_id": "G_MAYALEO",
    "channel_name": "maya-leo-group",
    "is_private": false,
    "is_dm": false,
    "is_gc": true,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "G_MAYALEO",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "G_MAYALEO",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "G_MAYALEO",
      "user_id": "U_LEO",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789994400.000004",
  "message_id": "1789994400.000004",
  "channel_id": "C_DEPLOY",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Deploy checklist looks good to me, will help verify on Friday.",
  "ts": "1789994400.000004",
  "created_at": "2026-09-21T12:40:00Z",
  "channel": "deployments",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:40:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:40:00-07:00",
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
    "channel_id": "C_DEPLOY",
    "channel_name": "deployments",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "C_DEPLOY",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "C_DEPLOY",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "C_DEPLOY",
      "user_id": "U_LEO",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "C_DEPLOY",
      "user_id": "U_DIEGO",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789995000.000005",
  "message_id": "1789995000.000005",
  "channel_id": "C_RANDOM",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Anyone up for lunch at noon?",
  "ts": "1789995000.000005",
  "created_at": "2026-09-21T12:50:00Z",
  "channel": "random",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:50:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:50:00-07:00",
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
    "channel_id": "C_RANDOM",
    "channel_name": "random",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "C_RANDOM",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "C_RANDOM",
      "user_id": "U_LEO",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "C_RANDOM",
      "user_id": "U_DIEGO",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789992360.000701",
  "message_id": "1789992360.000701",
  "channel_id": "D_MAYA",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Deploy checklist for Thursday is ready: env, flags, rollback.",
  "ts": "1789992360.000701",
  "created_at": "2026-09-21T12:06:00Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T12:06:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:06:00-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789974600.000702",
  "message_id": "1789974600.000702",
  "channel_id": "D_MAYA",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Deploy checklist for Thursday is ready: env, flags, rollback.",
  "ts": "1789974600.000702",
  "created_at": "2026-09-21T07:10:00Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T07:10:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:10:00-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789974758.000703",
  "message_id": "1789974758.000703",
  "ts": "1789974758.000703",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 1 passed.",
  "created_at": "2026-09-21T07:12:38Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T07:12:38+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:12:38-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789974916.000704",
  "message_id": "1789974916.000704",
  "ts": "1789974916.000704",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 2 passed.",
  "created_at": "2026-09-21T07:15:16Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T07:15:16+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:15:16-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789975074.000705",
  "message_id": "1789975074.000705",
  "ts": "1789975074.000705",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 3 passed.",
  "created_at": "2026-09-21T07:17:54Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T07:17:54+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:17:54-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789975232.000706",
  "message_id": "1789975232.000706",
  "ts": "1789975232.000706",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 4 passed.",
  "created_at": "2026-09-21T07:20:32Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T07:20:32+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:20:32-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789975390.000707",
  "message_id": "1789975390.000707",
  "ts": "1789975390.000707",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 5 passed.",
  "created_at": "2026-09-21T07:23:10Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T07:23:10+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:23:10-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789975548.000708",
  "message_id": "1789975548.000708",
  "ts": "1789975548.000708",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 6 passed.",
  "created_at": "2026-09-21T07:25:48Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T07:25:48+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:25:48-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789975706.000709",
  "message_id": "1789975706.000709",
  "ts": "1789975706.000709",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 7 passed.",
  "created_at": "2026-09-21T07:28:26Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T07:28:26+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:28:26-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789975864.000710",
  "message_id": "1789975864.000710",
  "ts": "1789975864.000710",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 8 passed.",
  "created_at": "2026-09-21T07:31:04Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T07:31:04+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:31:04-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789976022.000711",
  "message_id": "1789976022.000711",
  "ts": "1789976022.000711",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 9 passed.",
  "created_at": "2026-09-21T07:33:42Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T07:33:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:33:42-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789976180.000712",
  "message_id": "1789976180.000712",
  "ts": "1789976180.000712",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 10 passed.",
  "created_at": "2026-09-21T07:36:20Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T07:36:20+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:36:20-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789976338.000713",
  "message_id": "1789976338.000713",
  "ts": "1789976338.000713",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 11 passed.",
  "created_at": "2026-09-21T07:38:58Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T07:38:58+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:38:58-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789976496.000714",
  "message_id": "1789976496.000714",
  "ts": "1789976496.000714",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 12 passed.",
  "created_at": "2026-09-21T07:41:36Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T07:41:36+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:41:36-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789976654.000715",
  "message_id": "1789976654.000715",
  "ts": "1789976654.000715",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 13 passed.",
  "created_at": "2026-09-21T07:44:14Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T07:44:14+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:44:14-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789976812.000716",
  "message_id": "1789976812.000716",
  "ts": "1789976812.000716",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 14 passed.",
  "created_at": "2026-09-21T07:46:52Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T07:46:52+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:46:52-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789976970.000717",
  "message_id": "1789976970.000717",
  "ts": "1789976970.000717",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 15 passed.",
  "created_at": "2026-09-21T07:49:30Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T07:49:30+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:49:30-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789977128.000718",
  "message_id": "1789977128.000718",
  "ts": "1789977128.000718",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 16 passed.",
  "created_at": "2026-09-21T07:52:08Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T07:52:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:52:08-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789977286.000719",
  "message_id": "1789977286.000719",
  "ts": "1789977286.000719",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 17 passed.",
  "created_at": "2026-09-21T07:54:46Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T07:54:46+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:54:46-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789977444.000720",
  "message_id": "1789977444.000720",
  "ts": "1789977444.000720",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 18 passed.",
  "created_at": "2026-09-21T07:57:24Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T07:57:24+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:57:24-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789977602.000721",
  "message_id": "1789977602.000721",
  "ts": "1789977602.000721",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 19 passed.",
  "created_at": "2026-09-21T08:00:02Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T08:00:02+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:00:02-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789977760.000722",
  "message_id": "1789977760.000722",
  "ts": "1789977760.000722",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 20 passed.",
  "created_at": "2026-09-21T08:02:40Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T08:02:40+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:02:40-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789977918.000723",
  "message_id": "1789977918.000723",
  "ts": "1789977918.000723",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 21 passed.",
  "created_at": "2026-09-21T08:05:18Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T08:05:18+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:05:18-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789978076.000724",
  "message_id": "1789978076.000724",
  "ts": "1789978076.000724",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 22 passed.",
  "created_at": "2026-09-21T08:07:56Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T08:07:56+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:07:56-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789978234.000725",
  "message_id": "1789978234.000725",
  "ts": "1789978234.000725",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 23 passed.",
  "created_at": "2026-09-21T08:10:34Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T08:10:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:10:34-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789978392.000726",
  "message_id": "1789978392.000726",
  "ts": "1789978392.000726",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 24 passed.",
  "created_at": "2026-09-21T08:13:12Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T08:13:12+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:13:12-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789978550.000727",
  "message_id": "1789978550.000727",
  "ts": "1789978550.000727",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 25 passed.",
  "created_at": "2026-09-21T08:15:50Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T08:15:50+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:15:50-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789978708.000728",
  "message_id": "1789978708.000728",
  "ts": "1789978708.000728",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 26 passed.",
  "created_at": "2026-09-21T08:18:28Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T08:18:28+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:18:28-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789978866.000729",
  "message_id": "1789978866.000729",
  "ts": "1789978866.000729",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 27 passed.",
  "created_at": "2026-09-21T08:21:06Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T08:21:06+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:21:06-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789979024.000730",
  "message_id": "1789979024.000730",
  "ts": "1789979024.000730",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 28 passed.",
  "created_at": "2026-09-21T08:23:44Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T08:23:44+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:23:44-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789979183.000731",
  "message_id": "1789979183.000731",
  "ts": "1789979183.000731",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 29 passed.",
  "created_at": "2026-09-21T08:26:23Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T08:26:23+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:26:23-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789979341.000732",
  "message_id": "1789979341.000732",
  "ts": "1789979341.000732",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 30 passed.",
  "created_at": "2026-09-21T08:29:01Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T08:29:01+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:29:01-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789979499.000733",
  "message_id": "1789979499.000733",
  "ts": "1789979499.000733",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 31 passed.",
  "created_at": "2026-09-21T08:31:39Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T08:31:39+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:31:39-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789979657.000734",
  "message_id": "1789979657.000734",
  "ts": "1789979657.000734",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 32 passed.",
  "created_at": "2026-09-21T08:34:17Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T08:34:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:34:17-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789979815.000735",
  "message_id": "1789979815.000735",
  "ts": "1789979815.000735",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 33 passed.",
  "created_at": "2026-09-21T08:36:55Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T08:36:55+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:36:55-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789979973.000736",
  "message_id": "1789979973.000736",
  "ts": "1789979973.000736",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 34 passed.",
  "created_at": "2026-09-21T08:39:33Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T08:39:33+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:39:33-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789980131.000737",
  "message_id": "1789980131.000737",
  "ts": "1789980131.000737",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 35 passed.",
  "created_at": "2026-09-21T08:42:11Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T08:42:11+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:42:11-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789980289.000738",
  "message_id": "1789980289.000738",
  "ts": "1789980289.000738",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 36 passed.",
  "created_at": "2026-09-21T08:44:49Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T08:44:49+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:44:49-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789980447.000739",
  "message_id": "1789980447.000739",
  "ts": "1789980447.000739",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 37 passed.",
  "created_at": "2026-09-21T08:47:27Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T08:47:27+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:47:27-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789980605.000740",
  "message_id": "1789980605.000740",
  "ts": "1789980605.000740",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 38 passed.",
  "created_at": "2026-09-21T08:50:05Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T08:50:05+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:50:05-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789980763.000741",
  "message_id": "1789980763.000741",
  "ts": "1789980763.000741",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 39 passed.",
  "created_at": "2026-09-21T08:52:43Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T08:52:43+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:52:43-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789980921.000742",
  "message_id": "1789980921.000742",
  "ts": "1789980921.000742",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 40 passed.",
  "created_at": "2026-09-21T08:55:21Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T08:55:21+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:55:21-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789981079.000743",
  "message_id": "1789981079.000743",
  "ts": "1789981079.000743",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 41 passed.",
  "created_at": "2026-09-21T08:57:59Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T08:57:59+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:57:59-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789981237.000744",
  "message_id": "1789981237.000744",
  "ts": "1789981237.000744",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 42 passed.",
  "created_at": "2026-09-21T09:00:37Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T09:00:37+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:00:37-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789981395.000745",
  "message_id": "1789981395.000745",
  "ts": "1789981395.000745",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 43 passed.",
  "created_at": "2026-09-21T09:03:15Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T09:03:15+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:03:15-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789981553.000746",
  "message_id": "1789981553.000746",
  "ts": "1789981553.000746",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 44 passed.",
  "created_at": "2026-09-21T09:05:53Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T09:05:53+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:05:53-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789981711.000747",
  "message_id": "1789981711.000747",
  "ts": "1789981711.000747",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 45 passed.",
  "created_at": "2026-09-21T09:08:31Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T09:08:31+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:08:31-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789981869.000748",
  "message_id": "1789981869.000748",
  "ts": "1789981869.000748",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 46 passed.",
  "created_at": "2026-09-21T09:11:09Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T09:11:09+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:11:09-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789982027.000749",
  "message_id": "1789982027.000749",
  "ts": "1789982027.000749",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 47 passed.",
  "created_at": "2026-09-21T09:13:47Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T09:13:47+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:13:47-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789982185.000750",
  "message_id": "1789982185.000750",
  "ts": "1789982185.000750",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 48 passed.",
  "created_at": "2026-09-21T09:16:25Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T09:16:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:16:25-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789982343.000751",
  "message_id": "1789982343.000751",
  "ts": "1789982343.000751",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 49 passed.",
  "created_at": "2026-09-21T09:19:03Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T09:19:03+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:19:03-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789982501.000752",
  "message_id": "1789982501.000752",
  "ts": "1789982501.000752",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 50 passed.",
  "created_at": "2026-09-21T09:21:41Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T09:21:41+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:21:41-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789982659.000753",
  "message_id": "1789982659.000753",
  "ts": "1789982659.000753",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 51 passed.",
  "created_at": "2026-09-21T09:24:19Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T09:24:19+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:24:19-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789982817.000754",
  "message_id": "1789982817.000754",
  "ts": "1789982817.000754",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 52 passed.",
  "created_at": "2026-09-21T09:26:57Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T09:26:57+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:26:57-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789982975.000755",
  "message_id": "1789982975.000755",
  "ts": "1789982975.000755",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 53 passed.",
  "created_at": "2026-09-21T09:29:35Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T09:29:35+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:29:35-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789983133.000756",
  "message_id": "1789983133.000756",
  "ts": "1789983133.000756",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 54 passed.",
  "created_at": "2026-09-21T09:32:13Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T09:32:13+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:32:13-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789983291.000757",
  "message_id": "1789983291.000757",
  "ts": "1789983291.000757",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 55 passed.",
  "created_at": "2026-09-21T09:34:51Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T09:34:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:34:51-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789983449.000758",
  "message_id": "1789983449.000758",
  "ts": "1789983449.000758",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 56 passed.",
  "created_at": "2026-09-21T09:37:29Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T09:37:29+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:37:29-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789983608.000759",
  "message_id": "1789983608.000759",
  "ts": "1789983608.000759",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 57 passed.",
  "created_at": "2026-09-21T09:40:08Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T09:40:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:40:08-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789983766.000760",
  "message_id": "1789983766.000760",
  "ts": "1789983766.000760",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 58 passed.",
  "created_at": "2026-09-21T09:42:46Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T09:42:46+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:42:46-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789983924.000761",
  "message_id": "1789983924.000761",
  "ts": "1789983924.000761",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 59 passed.",
  "created_at": "2026-09-21T09:45:24Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T09:45:24+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:45:24-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789984082.000762",
  "message_id": "1789984082.000762",
  "ts": "1789984082.000762",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 60 passed.",
  "created_at": "2026-09-21T09:48:02Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T09:48:02+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:48:02-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789984240.000763",
  "message_id": "1789984240.000763",
  "ts": "1789984240.000763",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 61 passed.",
  "created_at": "2026-09-21T09:50:40Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T09:50:40+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:50:40-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789984398.000764",
  "message_id": "1789984398.000764",
  "ts": "1789984398.000764",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 62 passed.",
  "created_at": "2026-09-21T09:53:18Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T09:53:18+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:53:18-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789984556.000765",
  "message_id": "1789984556.000765",
  "ts": "1789984556.000765",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 63 passed.",
  "created_at": "2026-09-21T09:55:56Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T09:55:56+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:55:56-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789984714.000766",
  "message_id": "1789984714.000766",
  "ts": "1789984714.000766",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 64 passed.",
  "created_at": "2026-09-21T09:58:34Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T09:58:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:58:34-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789984872.000767",
  "message_id": "1789984872.000767",
  "ts": "1789984872.000767",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 65 passed.",
  "created_at": "2026-09-21T10:01:12Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T10:01:12+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:01:12-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789985030.000768",
  "message_id": "1789985030.000768",
  "ts": "1789985030.000768",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 66 passed.",
  "created_at": "2026-09-21T10:03:50Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T10:03:50+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:03:50-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789985188.000769",
  "message_id": "1789985188.000769",
  "ts": "1789985188.000769",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 67 passed.",
  "created_at": "2026-09-21T10:06:28Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T10:06:28+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:06:28-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789985346.000770",
  "message_id": "1789985346.000770",
  "ts": "1789985346.000770",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 68 passed.",
  "created_at": "2026-09-21T10:09:06Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T10:09:06+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:09:06-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789985504.000771",
  "message_id": "1789985504.000771",
  "ts": "1789985504.000771",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 69 passed.",
  "created_at": "2026-09-21T10:11:44Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T10:11:44+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:11:44-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789985662.000772",
  "message_id": "1789985662.000772",
  "ts": "1789985662.000772",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 70 passed.",
  "created_at": "2026-09-21T10:14:22Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T10:14:22+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:14:22-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789985820.000773",
  "message_id": "1789985820.000773",
  "ts": "1789985820.000773",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 71 passed.",
  "created_at": "2026-09-21T10:17:00Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T10:17:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:17:00-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789985978.000774",
  "message_id": "1789985978.000774",
  "ts": "1789985978.000774",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 72 passed.",
  "created_at": "2026-09-21T10:19:38Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T10:19:38+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:19:38-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789986136.000775",
  "message_id": "1789986136.000775",
  "ts": "1789986136.000775",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 73 passed.",
  "created_at": "2026-09-21T10:22:16Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T10:22:16+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:22:16-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789986294.000776",
  "message_id": "1789986294.000776",
  "ts": "1789986294.000776",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 74 passed.",
  "created_at": "2026-09-21T10:24:54Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T10:24:54+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:24:54-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789986452.000777",
  "message_id": "1789986452.000777",
  "ts": "1789986452.000777",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 75 passed.",
  "created_at": "2026-09-21T10:27:32Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T10:27:32+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:27:32-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789986610.000778",
  "message_id": "1789986610.000778",
  "ts": "1789986610.000778",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 76 passed.",
  "created_at": "2026-09-21T10:30:10Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T10:30:10+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:30:10-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789986768.000779",
  "message_id": "1789986768.000779",
  "ts": "1789986768.000779",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 77 passed.",
  "created_at": "2026-09-21T10:32:48Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T10:32:48+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:32:48-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789986926.000780",
  "message_id": "1789986926.000780",
  "ts": "1789986926.000780",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 78 passed.",
  "created_at": "2026-09-21T10:35:26Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T10:35:26+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:35:26-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789987084.000781",
  "message_id": "1789987084.000781",
  "ts": "1789987084.000781",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 79 passed.",
  "created_at": "2026-09-21T10:38:04Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T10:38:04+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:38:04-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789987242.000782",
  "message_id": "1789987242.000782",
  "ts": "1789987242.000782",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 80 passed.",
  "created_at": "2026-09-21T10:40:42Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T10:40:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:40:42-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789987400.000783",
  "message_id": "1789987400.000783",
  "ts": "1789987400.000783",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 81 passed.",
  "created_at": "2026-09-21T10:43:20Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T10:43:20+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:43:20-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789987558.000784",
  "message_id": "1789987558.000784",
  "ts": "1789987558.000784",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 82 passed.",
  "created_at": "2026-09-21T10:45:58Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T10:45:58+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:45:58-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789987716.000785",
  "message_id": "1789987716.000785",
  "ts": "1789987716.000785",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 83 passed.",
  "created_at": "2026-09-21T10:48:36Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T10:48:36+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:48:36-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789987874.000786",
  "message_id": "1789987874.000786",
  "ts": "1789987874.000786",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 84 passed.",
  "created_at": "2026-09-21T10:51:14Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T10:51:14+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:51:14-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789988033.000787",
  "message_id": "1789988033.000787",
  "ts": "1789988033.000787",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 85 passed.",
  "created_at": "2026-09-21T10:53:53Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T10:53:53+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:53:53-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789988191.000788",
  "message_id": "1789988191.000788",
  "ts": "1789988191.000788",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 86 passed.",
  "created_at": "2026-09-21T10:56:31Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T10:56:31+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:56:31-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789988349.000789",
  "message_id": "1789988349.000789",
  "ts": "1789988349.000789",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 87 passed.",
  "created_at": "2026-09-21T10:59:09Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T10:59:09+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:59:09-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789988507.000790",
  "message_id": "1789988507.000790",
  "ts": "1789988507.000790",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 88 passed.",
  "created_at": "2026-09-21T11:01:47Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T11:01:47+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:01:47-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789988665.000791",
  "message_id": "1789988665.000791",
  "ts": "1789988665.000791",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 89 passed.",
  "created_at": "2026-09-21T11:04:25Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T11:04:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:04:25-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789988823.000792",
  "message_id": "1789988823.000792",
  "ts": "1789988823.000792",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 90 passed.",
  "created_at": "2026-09-21T11:07:03Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T11:07:03+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:07:03-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789988981.000793",
  "message_id": "1789988981.000793",
  "ts": "1789988981.000793",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 91 passed.",
  "created_at": "2026-09-21T11:09:41Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T11:09:41+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:09:41-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789989139.000794",
  "message_id": "1789989139.000794",
  "ts": "1789989139.000794",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 92 passed.",
  "created_at": "2026-09-21T11:12:19Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T11:12:19+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:12:19-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789989297.000795",
  "message_id": "1789989297.000795",
  "ts": "1789989297.000795",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 93 passed.",
  "created_at": "2026-09-21T11:14:57Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T11:14:57+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:14:57-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789989455.000796",
  "message_id": "1789989455.000796",
  "ts": "1789989455.000796",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 94 passed.",
  "created_at": "2026-09-21T11:17:35Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T11:17:35+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:17:35-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789989613.000797",
  "message_id": "1789989613.000797",
  "ts": "1789989613.000797",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 95 passed.",
  "created_at": "2026-09-21T11:20:13Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T11:20:13+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:20:13-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789989771.000798",
  "message_id": "1789989771.000798",
  "ts": "1789989771.000798",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 96 passed.",
  "created_at": "2026-09-21T11:22:51Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T11:22:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:22:51-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789989929.000799",
  "message_id": "1789989929.000799",
  "ts": "1789989929.000799",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 97 passed.",
  "created_at": "2026-09-21T11:25:29Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T11:25:29+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:25:29-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789990087.000800",
  "message_id": "1789990087.000800",
  "ts": "1789990087.000800",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 98 passed.",
  "created_at": "2026-09-21T11:28:07Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T11:28:07+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:28:07-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789990245.000801",
  "message_id": "1789990245.000801",
  "ts": "1789990245.000801",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 99 passed.",
  "created_at": "2026-09-21T11:30:45Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T11:30:45+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:30:45-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789990403.000802",
  "message_id": "1789990403.000802",
  "ts": "1789990403.000802",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 100 passed.",
  "created_at": "2026-09-21T11:33:23Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T11:33:23+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:33:23-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789990561.000803",
  "message_id": "1789990561.000803",
  "ts": "1789990561.000803",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 101 passed.",
  "created_at": "2026-09-21T11:36:01Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T11:36:01+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:36:01-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789990719.000804",
  "message_id": "1789990719.000804",
  "ts": "1789990719.000804",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 102 passed.",
  "created_at": "2026-09-21T11:38:39Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T11:38:39+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:38:39-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789990877.000805",
  "message_id": "1789990877.000805",
  "ts": "1789990877.000805",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 103 passed.",
  "created_at": "2026-09-21T11:41:17Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T11:41:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:41:17-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789991035.000806",
  "message_id": "1789991035.000806",
  "ts": "1789991035.000806",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 104 passed.",
  "created_at": "2026-09-21T11:43:55Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T11:43:55+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:43:55-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789991193.000807",
  "message_id": "1789991193.000807",
  "ts": "1789991193.000807",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 105 passed.",
  "created_at": "2026-09-21T11:46:33Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T11:46:33+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:46:33-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789991351.000808",
  "message_id": "1789991351.000808",
  "ts": "1789991351.000808",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 106 passed.",
  "created_at": "2026-09-21T11:49:11Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T11:49:11+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:49:11-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789991509.000809",
  "message_id": "1789991509.000809",
  "ts": "1789991509.000809",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 107 passed.",
  "created_at": "2026-09-21T11:51:49Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T11:51:49+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:51:49-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789991667.000810",
  "message_id": "1789991667.000810",
  "ts": "1789991667.000810",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 108 passed.",
  "created_at": "2026-09-21T11:54:27Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T11:54:27+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:54:27-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789991825.000811",
  "message_id": "1789991825.000811",
  "ts": "1789991825.000811",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 109 passed.",
  "created_at": "2026-09-21T11:57:05Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T11:57:05+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:57:05-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "1789991983.000812",
  "message_id": "1789991983.000812",
  "ts": "1789991983.000812",
  "channel_id": "D_MAYA",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Deploy checklist check 110 passed.",
  "created_at": "2026-09-21T11:59:43Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T11:59:43+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:59:43-07:00",
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
    "channel_id": "D_MAYA",
    "channel_name": "D_MAYA",
    "is_private": true,
    "is_dm": true,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false,
    "channel_members": [
     {
      "channel_id": "D_MAYA",
      "user_id": "U01AGENBOT9",
      "joined_at": "2026-01-05T09:05:00Z"
     },
     {
      "channel_id": "D_MAYA",
      "user_id": "U_MAYA",
      "joined_at": "2026-01-05T09:05:00Z"
     }
    ]
   }
  ]
 }
]
