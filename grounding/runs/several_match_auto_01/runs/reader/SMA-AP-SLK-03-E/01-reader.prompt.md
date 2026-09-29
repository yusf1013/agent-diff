You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Slack workspace:

    "Add a rocket reaction to every message about the rollout timeline in #eng-updates that Priya reacted to with eyes."

The user is Agent Bot. Below is every Slack message in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "1789916400.000001",
  "message_id": "1789916400.000001",
  "channel_id": "C_ENG",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollout timeline: shipping to prod Friday 3pm.",
  "ts": "1789916400.000001",
  "created_at": "2026-09-20T15:00:00Z",
  "channel": "eng-updates",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-20T15:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-20T08:00:00-07:00",
  "channels": [
   {
    "channel_id": "C_ENG",
    "channel_name": "eng-updates",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "message_reactions": [
   {
    "message_id": "1789916400.000001",
    "user_id": "U_PRIYA",
    "reaction_type": "eyes",
    "created_at": "2026-09-20T15:05:00Z",
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
    "message_id": "1789916400.000001",
    "user_id": "U_DIEGO",
    "reaction_type": "thumbsup",
    "created_at": "2026-09-20T15:06:00Z",
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
  "id": "1789920000.000002",
  "message_id": "1789920000.000002",
  "channel_id": "C_ENG",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Updated rollout timeline: prod push moved to Thursday.",
  "ts": "1789920000.000002",
  "created_at": "2026-09-20T16:00:00Z",
  "channel": "eng-updates",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-20T16:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-20T09:00:00-07:00",
  "channels": [
   {
    "channel_id": "C_ENG",
    "channel_name": "eng-updates",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "message_reactions": [
   {
    "message_id": "1789920000.000002",
    "user_id": "U_PRIYA",
    "reaction_type": "thumbsup",
    "created_at": "2026-09-20T16:05:00Z",
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
  "id": "1789923600.000003",
  "message_id": "1789923600.000003",
  "channel_id": "C_ENG",
  "user_id": "U_PRIYA (Priya Sharma)",
  "message_text": "Rollout timeline slipped by one day, more soon.",
  "ts": "1789923600.000003",
  "created_at": "2026-09-20T17:00:00Z",
  "channel": "eng-updates",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-20T17:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-20T10:00:00-07:00",
  "channels": [
   {
    "channel_id": "C_ENG",
    "channel_name": "eng-updates",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "message_reactions": [
   {
    "message_id": "1789923600.000003",
    "user_id": "U_OMAR",
    "reaction_type": "eyes",
    "created_at": "2026-09-20T17:05:00Z",
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
  "id": "1789927200.000004",
  "message_id": "1789927200.000004",
  "channel_id": "C_ENG",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Rollout timeline: no changes, still Friday 3pm.",
  "ts": "1789927200.000004",
  "created_at": "2026-09-20T18:00:00Z",
  "channel": "eng-updates",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-20T18:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-20T11:00:00-07:00",
  "channels": [
   {
    "channel_id": "C_ENG",
    "channel_name": "eng-updates",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "message_reactions": [
   {
    "message_id": "1789927200.000004",
    "user_id": "U_LEO",
    "reaction_type": "tada",
    "created_at": "2026-09-20T18:05:00Z",
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
  "id": "1789905600.000005",
  "message_id": "1789905600.000005",
  "channel_id": "C_ENG",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Lunch at noon?",
  "ts": "1789905600.000005",
  "created_at": "2026-09-20T12:00:00Z",
  "channel": "eng-updates",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-20T12:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-20T05:00:00-07:00",
  "channels": [
   {
    "channel_id": "C_ENG",
    "channel_name": "eng-updates",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "message_reactions": [
   {
    "message_id": "1789905600.000005",
    "user_id": "U_PRIYA",
    "reaction_type": "eyes",
    "created_at": "2026-09-20T12:05:00Z",
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
  "id": "1789930800.000006",
  "message_id": "1789930800.000006",
  "channel_id": "C_ENG",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Rollout timeline confirmed for Friday, see thread.",
  "ts": "1789930800.000006",
  "created_at": "2026-09-20T19:00:00Z",
  "channel": "eng-updates",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-20T19:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-20T12:00:00-07:00",
  "channels": [
   {
    "channel_id": "C_ENG",
    "channel_name": "eng-updates",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "message_reactions": [
   {
    "message_id": "1789930800.000006",
    "user_id": "U_PRIYA",
    "reaction_type": "thumbsup",
    "created_at": "2026-09-20T19:05:00Z",
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
    "message_id": "1789930800.000006",
    "user_id": "U_LEO",
    "reaction_type": "eyes",
    "created_at": "2026-09-20T19:06:00Z",
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
  "id": "1789894800.000007",
  "message_id": "1789894800.000007",
  "channel_id": "C_ENG",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Standup at 9am tomorrow.",
  "ts": "1789894800.000007",
  "created_at": "2026-09-20T09:00:00Z",
  "channel": "eng-updates",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-20T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-20T02:00:00-07:00",
  "channels": [
   {
    "channel_id": "C_ENG",
    "channel_name": "eng-updates",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "message_reactions": []
 },
 {
  "id": "1789916460.000701",
  "message_id": "1789916460.000701",
  "channel_id": "C_ENG",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollout timeline: releasing to prod Monday 10am.",
  "ts": "1789916460.000701",
  "created_at": "2026-09-20T15:01:00Z",
  "channel": "eng-updates",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-20T15:01:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-20T08:01:00-07:00",
  "channels": [
   {
    "channel_id": "C_ENG",
    "channel_name": "eng-updates",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "message_reactions": [
   {
    "message_id": "1789916460.000701",
    "user_id": "U_PRIYA",
    "reaction_type": "eyes",
    "created_at": "2026-09-20T15:05:00Z",
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
    "message_id": "1789916460.000701",
    "user_id": "U_DIEGO",
    "reaction_type": "thumbsup",
    "created_at": "2026-09-20T15:06:00Z",
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
  "id": "1789916520.000702",
  "message_id": "1789916520.000702",
  "channel_id": "C_ENG",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Rollout timeline: deploy to prod Thursday noon.",
  "ts": "1789916520.000702",
  "created_at": "2026-09-20T15:02:00Z",
  "channel": "eng-updates",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-20T15:02:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-20T08:02:00-07:00",
  "channels": [
   {
    "channel_id": "C_ENG",
    "channel_name": "eng-updates",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "message_reactions": [
   {
    "message_id": "1789916520.000702",
    "user_id": "U_PRIYA",
    "reaction_type": "eyes",
    "created_at": "2026-09-20T15:05:00Z",
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
    "message_id": "1789916520.000702",
    "user_id": "U_DIEGO",
    "reaction_type": "thumbsup",
    "created_at": "2026-09-20T15:06:00Z",
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
