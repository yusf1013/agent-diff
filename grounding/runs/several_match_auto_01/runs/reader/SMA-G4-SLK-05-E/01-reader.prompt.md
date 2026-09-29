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
  "id": "1789992420.000702",
  "message_id": "1789992420.000702",
  "channel_id": "D_MAYA",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Deploy checklist for Monday is set: config, flags, rollback plan.",
  "ts": "1789992420.000702",
  "created_at": "2026-09-21T12:07:00Z",
  "channel": "D_MAYA",
  "private": true,
  "archived": false,
  "direct message": true,
  "posted (UTC)": "2026-09-21T12:07:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:07:00-07:00",
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
 }
]
