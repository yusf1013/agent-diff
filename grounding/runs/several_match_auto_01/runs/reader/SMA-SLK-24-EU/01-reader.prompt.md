You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Slack workspace:

    "Post "Reminder: expense reports are due Friday" in every private channel that both Priya Sharma and Leo Park are members of."

The user is Agent Bot. Below is every Slack channel in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "C_FINLEADS",
  "channel_id": "C_FINLEADS",
  "channel_name": "finance-leads",
  "purpose_text": "Finance leadership",
  "is_private": true,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "finance-leads",
  "private": true,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00",
  "channel_members": [
   {
    "channel_id": "C_FINLEADS",
    "user_id": "U01AGENBOT9",
    "joined_at": "2026-01-05T09:05:00Z",
    "users": [
     {
      "user_id": "U01AGENBOT9",
      "username": "agentbot",
      "email": "agentbot@northwind.example",
      "real_name": "Agent Bot",
      "display_name": "AgentBot",
      "created_at": "2025-01-01T00:05:00Z",
      "is_bot": true,
      "is_active": true
     }
    ]
   },
   {
    "channel_id": "C_FINLEADS",
    "user_id": "U_PRIYA",
    "joined_at": "2026-01-05T09:05:00Z",
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
   },
   {
    "channel_id": "C_FINLEADS",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
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
   },
   {
    "channel_id": "C_FINLEADS",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
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
    ]
   }
  ]
 },
 {
  "id": "C_OPSLEADS",
  "channel_id": "C_OPSLEADS",
  "channel_name": "ops-leads",
  "purpose_text": "Operations leadership",
  "is_private": true,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "ops-leads",
  "private": true,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00",
  "channel_members": [
   {
    "channel_id": "C_OPSLEADS",
    "user_id": "U01AGENBOT9",
    "joined_at": "2026-01-05T09:05:00Z",
    "users": [
     {
      "user_id": "U01AGENBOT9",
      "username": "agentbot",
      "email": "agentbot@northwind.example",
      "real_name": "Agent Bot",
      "display_name": "AgentBot",
      "created_at": "2025-01-01T00:05:00Z",
      "is_bot": true,
      "is_active": true
     }
    ]
   },
   {
    "channel_id": "C_OPSLEADS",
    "user_id": "U_PRIYA",
    "joined_at": "2026-01-05T09:05:00Z",
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
   },
   {
    "channel_id": "C_OPSLEADS",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
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
    ]
   }
  ]
 },
 {
  "id": "C_BUDGET",
  "channel_id": "C_BUDGET",
  "channel_name": "budget-review",
  "purpose_text": "Budget review",
  "is_private": true,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "budget-review",
  "private": true,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00",
  "channel_members": [
   {
    "channel_id": "C_BUDGET",
    "user_id": "U01AGENBOT9",
    "joined_at": "2026-01-05T09:05:00Z",
    "users": [
     {
      "user_id": "U01AGENBOT9",
      "username": "agentbot",
      "email": "agentbot@northwind.example",
      "real_name": "Agent Bot",
      "display_name": "AgentBot",
      "created_at": "2025-01-01T00:05:00Z",
      "is_bot": true,
      "is_active": true
     }
    ]
   },
   {
    "channel_id": "C_BUDGET",
    "user_id": "U_PRIYA",
    "joined_at": "2026-01-05T09:05:00Z",
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
   },
   {
    "channel_id": "C_BUDGET",
    "user_id": "U_LEOPARKER",
    "joined_at": "2026-01-05T09:05:00Z",
    "users": [
     {
      "user_id": "U_LEOPARKER",
      "username": "leo.parker",
      "email": "leo.parker@northwind.example",
      "real_name": "Leo Parker",
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
  "id": "C_HRPARTNERS",
  "channel_id": "C_HRPARTNERS",
  "channel_name": "hr-partners",
  "purpose_text": "HR business partners",
  "is_private": true,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "hr-partners",
  "private": true,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00",
  "channel_members": [
   {
    "channel_id": "C_HRPARTNERS",
    "user_id": "U01AGENBOT9",
    "joined_at": "2026-01-05T09:05:00Z",
    "users": [
     {
      "user_id": "U01AGENBOT9",
      "username": "agentbot",
      "email": "agentbot@northwind.example",
      "real_name": "Agent Bot",
      "display_name": "AgentBot",
      "created_at": "2025-01-01T00:05:00Z",
      "is_bot": true,
      "is_active": true
     }
    ]
   },
   {
    "channel_id": "C_HRPARTNERS",
    "user_id": "U_PRIYA",
    "joined_at": "2026-01-05T09:05:00Z",
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
   },
   {
    "channel_id": "C_HRPARTNERS",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
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
    ]
   }
  ]
 },
 {
  "id": "C_FINLEADS-sm11",
  "channel_id": "C_FINLEADS-sm11",
  "channel_name": "finance-sync",
  "purpose_text": "Finance leadership",
  "is_private": true,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "finance-sync",
  "private": true,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00",
  "channel_members": [
   {
    "channel_id": "C_FINLEADS-sm11",
    "user_id": "U01AGENBOT9",
    "joined_at": "2026-01-05T09:05:00Z",
    "users": [
     {
      "user_id": "U01AGENBOT9",
      "username": "agentbot",
      "email": "agentbot@northwind.example",
      "real_name": "Agent Bot",
      "display_name": "AgentBot",
      "created_at": "2025-01-01T00:05:00Z",
      "is_bot": true,
      "is_active": true
     }
    ]
   },
   {
    "channel_id": "C_FINLEADS-sm11",
    "user_id": "U_PRIYA",
    "joined_at": "2026-01-05T09:05:00Z",
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
   },
   {
    "channel_id": "C_FINLEADS-sm11",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
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
   },
   {
    "channel_id": "C_FINLEADS-sm11",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
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
    ]
   }
  ]
 },
 {
  "id": "C_FINLEADS-sm13",
  "channel_id": "C_FINLEADS-sm13",
  "channel_name": "budget-leads",
  "purpose_text": "Finance leadership",
  "is_private": true,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "budget-leads",
  "private": true,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00",
  "channel_members": [
   {
    "channel_id": "C_FINLEADS-sm13",
    "user_id": "U01AGENBOT9",
    "joined_at": "2026-01-05T09:05:00Z",
    "users": [
     {
      "user_id": "U01AGENBOT9",
      "username": "agentbot",
      "email": "agentbot@northwind.example",
      "real_name": "Agent Bot",
      "display_name": "AgentBot",
      "created_at": "2025-01-01T00:05:00Z",
      "is_bot": true,
      "is_active": true
     }
    ]
   },
   {
    "channel_id": "C_FINLEADS-sm13",
    "user_id": "U_PRIYA",
    "joined_at": "2026-01-05T09:05:00Z",
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
   },
   {
    "channel_id": "C_FINLEADS-sm13",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
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
   },
   {
    "channel_id": "C_FINLEADS-sm13",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
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
    ]
   }
  ]
 }
]
