You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Slack workspace:

    "Add an eyes reaction to all of Maya Chen's launch checklist cards in #launch-readiness that list the rollback steps."

The user is Agent Bot. Below is every Slack message in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "1789989000.000001",
  "message_id": "1789989000.000001",
  "channel_id": "C_LAUNCH",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Launch readiness — card below with the final sequence.",
  "ts": "1789989000.000001",
  "created_at": "2026-09-21T11:10:00Z",
  "blocks": [
   {
    "type": "section",
    "text": {
     "type": "mrkdwn",
     "text": "Launch checklist card: rollback steps — 1) halt deploys 2) restore snapshot 3) verify health"
    }
   }
  ],
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:10:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:10:00-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-readiness",
    "topic_text": "Q3 launch — rollback steps draft parked here",
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
  ]
 },
 {
  "id": "1789989900.000002",
  "message_id": "1789989900.000002",
  "channel_id": "C_LAUNCH",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Launch checklist: rollback steps — 1) halt deploys 2) restore snapshot 3) verify health",
  "ts": "1789989900.000002",
  "created_at": "2026-09-21T11:25:00Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:25:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:25:00-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-readiness",
    "topic_text": "Q3 launch — rollback steps draft parked here",
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
  ]
 },
 {
  "id": "1789990800.000003",
  "message_id": "1789990800.000003",
  "channel_id": "C_LAUNCH",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Launch readiness — verification card below.",
  "ts": "1789990800.000003",
  "created_at": "2026-09-21T11:40:00Z",
  "blocks": [
   {
    "type": "section",
    "text": {
     "type": "mrkdwn",
     "text": "Follow-up card: verification checklist — 1) confirm monitors 2) note owners"
    }
   }
  ],
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:40:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:40:00-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-readiness",
    "topic_text": "Q3 launch — rollback steps draft parked here",
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
  ]
 },
 {
  "id": "1789992300.000004",
  "message_id": "1789992300.000004",
  "channel_id": "C_LAUNCH",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Launch readiness — card below with the final sequence.",
  "ts": "1789992300.000004",
  "created_at": "2026-09-21T12:05:00Z",
  "blocks": [
   {
    "type": "section",
    "text": {
     "type": "mrkdwn",
     "text": "Launch checklist card: rollout steps — 1) open flags 2) ramp traffic 3) monitor errors"
    }
   }
  ],
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T12:05:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T05:05:00-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-readiness",
    "topic_text": "Q3 launch — rollback steps draft parked here",
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
  ]
 },
 {
  "id": "1789991400.000005",
  "message_id": "1789991400.000005",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch readiness — card below.",
  "ts": "1789991400.000005",
  "created_at": "2026-09-21T11:50:00Z",
  "blocks": [
   {
    "type": "section",
    "text": {
     "type": "mrkdwn",
     "text": "Launch checklist card: cleanup steps — 1) close flags 2) file notes"
    }
   }
  ],
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:50:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:50:00-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-readiness",
    "topic_text": "Q3 launch — rollback steps draft parked here",
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
  ]
 },
 {
  "id": "1789991700.000006",
  "message_id": "1789991700.000006",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch readiness — card below.",
  "ts": "1789991700.000006",
  "created_at": "2026-09-21T11:55:00Z",
  "blocks": [
   {
    "type": "section",
    "text": {
     "type": "mrkdwn",
     "text": "Launch checklist card: handoff notes — 1) page owner 2) link dashboard"
    }
   }
  ],
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:55:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:55:00-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-readiness",
    "topic_text": "Q3 launch — rollback steps draft parked here",
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
  ]
 },
 {
  "id": "1789989060.000701",
  "message_id": "1789989060.000701",
  "channel_id": "C_LAUNCH",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Launch checklist — card below lists the rollback steps.",
  "ts": "1789989060.000701",
  "created_at": "2026-09-21T11:11:00Z",
  "blocks": [
   {
    "type": "section",
    "text": {
     "type": "mrkdwn",
     "text": "Launch checklist card: rollback steps — 1) halt deploys 2) restore snapshot 3) verify health"
    }
   }
  ],
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:11:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:11:00-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-readiness",
    "topic_text": "Q3 launch — rollback steps draft parked here",
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
  ]
 },
 {
  "id": "1789989120.000702",
  "message_id": "1789989120.000702",
  "channel_id": "C_LAUNCH",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Launch readiness — card with rollback steps is below.",
  "ts": "1789989120.000702",
  "created_at": "2026-09-21T11:12:00Z",
  "blocks": [
   {
    "type": "section",
    "text": {
     "type": "mrkdwn",
     "text": "Launch checklist card: rollback steps — 1) halt deploys 2) restore snapshot 3) verify health"
    }
   }
  ],
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:12:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:12:00-07:00",
  "channels": [
   {
    "channel_id": "C_LAUNCH",
    "channel_name": "launch-readiness",
    "topic_text": "Q3 launch — rollback steps draft parked here",
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
  ]
 }
]
