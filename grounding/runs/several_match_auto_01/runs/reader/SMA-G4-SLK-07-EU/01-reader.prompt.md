You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Slack workspace:

    "Set the topic of every private channel with Diego Alvarez's message about the gateway rollback to Post-release monitoring."

The user is Agent Bot. Below is every Slack channel in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "C_REL",
  "channel_id": "C_REL",
  "channel_name": "release-ops",
  "topic_text": "Release coordination",
  "is_private": true,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "release-ops",
  "private": true,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00",
  "messages": [
   {
    "message_id": "1789992600.000001",
    "channel_id": "C_REL",
    "user_id": "U_DIEGO",
    "message_text": "Gateway rollback finished on prod, the error rate is back to baseline.",
    "ts": "1789992600.000001",
    "created_at": "2026-09-21T12:10:00Z",
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
    "message_id": "1789993500.000002",
    "channel_id": "C_REL",
    "user_id": "U_MAYA",
    "message_text": "Thanks, I will update the incident notes.",
    "ts": "1789993500.000002",
    "created_at": "2026-09-21T12:25:00Z",
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
  "id": "C_DEP",
  "channel_id": "C_DEP",
  "channel_name": "deploy-queue",
  "topic_text": "Release coordination",
  "is_private": true,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "deploy-queue",
  "private": true,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00",
  "messages": [
   {
    "message_id": "1789990800.000003",
    "channel_id": "C_DEP",
    "user_id": "U_DIEGO",
    "message_text": "The checklist for Friday's deploy is pinned, please review it before noon.",
    "ts": "1789990800.000003",
    "created_at": "2026-09-21T11:40:00Z",
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
    "message_id": "1789991700.000004",
    "channel_id": "C_DEP",
    "user_id": "U_LEO",
    "message_text": "The gateway rollback runbook still needs a second reviewer before Friday.",
    "ts": "1789991700.000004",
    "created_at": "2026-09-21T11:55:00Z",
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
  "id": "C_GEN",
  "channel_id": "C_GEN",
  "channel_name": "general",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "general",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00",
  "messages": [
   {
    "message_id": "1789992300.000005",
    "channel_id": "C_GEN",
    "user_id": "U_MAYA",
    "message_text": "Team lunch is at noon in the main kitchen.",
    "ts": "1789992300.000005",
    "created_at": "2026-09-21T12:05:00Z",
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
  "id": "C_SOC",
  "channel_id": "C_SOC",
  "channel_name": "social",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "social",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00",
  "messages": [
   {
    "message_id": "1789992900.000006",
    "channel_id": "C_SOC",
    "user_id": "U_LEO",
    "message_text": "Photos from yesterday's offsite are in the shared drive.",
    "ts": "1789992900.000006",
    "created_at": "2026-09-21T12:15:00Z",
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
  "id": "C_REL-sm5",
  "channel_id": "C_REL-sm5",
  "channel_name": "deploy-ops",
  "topic_text": "Release coordination",
  "is_private": true,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "deploy-ops",
  "private": true,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00",
  "messages": [
   {
    "message_id": "1789992600.900006",
    "channel_id": "C_REL-sm5",
    "user_id": "U_DIEGO",
    "message_text": "Gateway rollback finished on prod, the error rate is back to baseline.",
    "ts": "1789992600.900006",
    "created_at": "2026-09-21T12:10:00Z",
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
    "message_id": "1789993500.900007",
    "channel_id": "C_REL-sm5",
    "user_id": "U_MAYA",
    "message_text": "Thanks, I will update the incident notes.",
    "ts": "1789993500.900007",
    "created_at": "2026-09-21T12:25:00Z",
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
  "id": "C_REL-sm8",
  "channel_id": "C_REL-sm8",
  "channel_name": "release-sync",
  "topic_text": "Release coordination",
  "is_private": true,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "release-sync",
  "private": true,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00",
  "messages": [
   {
    "message_id": "1789992600.900009",
    "channel_id": "C_REL-sm8",
    "user_id": "U_DIEGO",
    "message_text": "Gateway rollback finished on prod, the error rate is back to baseline.",
    "ts": "1789992600.900009",
    "created_at": "2026-09-21T12:10:00Z",
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
    "message_id": "1789993500.900010",
    "channel_id": "C_REL-sm8",
    "user_id": "U_MAYA",
    "message_text": "Thanks, I will update the incident notes.",
    "ts": "1789993500.900010",
    "created_at": "2026-09-21T12:25:00Z",
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
