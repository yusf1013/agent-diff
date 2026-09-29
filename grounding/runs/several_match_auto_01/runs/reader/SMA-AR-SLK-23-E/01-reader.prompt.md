You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Slack workspace:

    "Archive every private channel whose purpose mentions onboarding new hires and that has Diego Alvarez as a member."

The user is Agent Bot. Below is every Slack channel in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "C_ONB",
  "channel_id": "C_ONB",
  "channel_name": "new-hire-onboarding",
  "purpose_text": "Onboarding new hires and tracking their first 90 days",
  "is_private": true,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "new-hire-onboarding",
  "private": true,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00",
  "channel_members": [
   {
    "channel_id": "C_ONB",
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
    "channel_id": "C_ONB",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
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
    "channel_id": "C_ONB",
    "user_id": "U_AISHA",
    "joined_at": "2026-01-05T09:05:00Z",
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
    ]
   }
  ]
 },
 {
  "id": "C_HRGEN",
  "channel_id": "C_HRGEN",
  "channel_name": "hr-general",
  "topic_text": "Onboarding new hires",
  "purpose_text": "General HR announcements and holiday schedule",
  "is_private": true,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "hr-general",
  "private": true,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00",
  "channel_members": [
   {
    "channel_id": "C_HRGEN",
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
    "channel_id": "C_HRGEN",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
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
    "channel_id": "C_HRGEN",
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
   }
  ]
 },
 {
  "id": "C_HRBEN",
  "channel_id": "C_HRBEN",
  "channel_name": "hr-benefits",
  "purpose_text": "Benefits enrollment and 401k questions",
  "is_private": true,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "hr-benefits",
  "private": true,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00",
  "channel_members": [
   {
    "channel_id": "C_HRBEN",
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
    "channel_id": "C_HRBEN",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
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
    "channel_id": "C_HRBEN",
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
  "id": "C_ONB_PUB",
  "channel_id": "C_ONB_PUB",
  "channel_name": "new-hires",
  "purpose_text": "Onboarding new hires and swag ordering",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "new-hires",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00",
  "channel_members": [
   {
    "channel_id": "C_ONB_PUB",
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
    "channel_id": "C_ONB_PUB",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
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
    "channel_id": "C_ONB_PUB",
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
   }
  ]
 },
 {
  "id": "C_ONB_GC",
  "channel_id": "C_ONB_GC",
  "channel_name": "onboarding-design-pod",
  "purpose_text": "Onboarding new hires for the design pod",
  "is_private": false,
  "is_dm": false,
  "is_gc": true,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "onboarding-design-pod",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00",
  "channel_members": [
   {
    "channel_id": "C_ONB_GC",
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
    "channel_id": "C_ONB_GC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
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
    "channel_id": "C_ONB_GC",
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
  "id": "C_BUDGET",
  "channel_id": "C_BUDGET",
  "channel_name": "budget-planning",
  "purpose_text": "Quarterly budget planning and forecast reviews",
  "is_private": true,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "budget-planning",
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
    "channel_id": "C_BUDGET",
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
  "id": "C_NEWHIRE_NODIEGO",
  "channel_id": "C_NEWHIRE_NODIEGO",
  "channel_name": "orientation-schedule",
  "purpose_text": "Onboarding new hires and orientation schedule",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "orientation-schedule",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00",
  "channel_members": [
   {
    "channel_id": "C_NEWHIRE_NODIEGO",
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
    "channel_id": "C_NEWHIRE_NODIEGO",
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
    "channel_id": "C_NEWHIRE_NODIEGO",
    "user_id": "U_AISHA",
    "joined_at": "2026-01-05T09:05:00Z",
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
    ]
   }
  ]
 },
 {
  "id": "C_ONB-sm388",
  "channel_id": "C_ONB-sm388",
  "channel_name": "hires-onboarding-hub",
  "purpose_text": "Onboarding new hires and tracking their first 90 days",
  "is_private": true,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "hires-onboarding-hub",
  "private": true,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00",
  "channel_members": [
   {
    "channel_id": "C_ONB-sm388",
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
    "channel_id": "C_ONB-sm388",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
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
    "channel_id": "C_ONB-sm388",
    "user_id": "U_AISHA",
    "joined_at": "2026-01-05T09:05:00Z",
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
    ]
   }
  ]
 },
 {
  "id": "C_ONB-sm389",
  "channel_id": "C_ONB-sm389",
  "channel_name": "new-hire-welcome",
  "purpose_text": "Onboarding new hires and tracking their first 90 days",
  "is_private": true,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "new-hire-welcome",
  "private": true,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00",
  "channel_members": [
   {
    "channel_id": "C_ONB-sm389",
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
    "channel_id": "C_ONB-sm389",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
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
    "channel_id": "C_ONB-sm389",
    "user_id": "U_AISHA",
    "joined_at": "2026-01-05T09:05:00Z",
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
    ]
   }
  ]
 }
]
