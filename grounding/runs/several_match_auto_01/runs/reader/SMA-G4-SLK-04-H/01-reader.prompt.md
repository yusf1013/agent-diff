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
  "id": "1789974600.000702",
  "message_id": "1789974600.000702",
  "channel_id": "C_LAUNCH",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Launch checklist — card below lists the rollback steps.",
  "ts": "1789974600.000702",
  "created_at": "2026-09-21T07:10:00Z",
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
  "posted (UTC)": "2026-09-21T07:10:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:10:00-07:00",
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
  "id": "1789974728.000703",
  "message_id": "1789974728.000703",
  "ts": "1789974728.000703",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 1 passed.",
  "created_at": "2026-09-21T07:12:08Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:12:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:12:08-07:00",
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
  "id": "1789974857.000704",
  "message_id": "1789974857.000704",
  "ts": "1789974857.000704",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 2 passed.",
  "created_at": "2026-09-21T07:14:17Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:14:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:14:17-07:00",
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
  "id": "1789974985.000705",
  "message_id": "1789974985.000705",
  "ts": "1789974985.000705",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 3 passed.",
  "created_at": "2026-09-21T07:16:25Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:16:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:16:25-07:00",
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
  "id": "1789975114.000706",
  "message_id": "1789975114.000706",
  "ts": "1789975114.000706",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 4 passed.",
  "created_at": "2026-09-21T07:18:34Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:18:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:18:34-07:00",
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
  "id": "1789975242.000707",
  "message_id": "1789975242.000707",
  "ts": "1789975242.000707",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 5 passed.",
  "created_at": "2026-09-21T07:20:42Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:20:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:20:42-07:00",
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
  "id": "1789975371.000708",
  "message_id": "1789975371.000708",
  "ts": "1789975371.000708",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 6 passed.",
  "created_at": "2026-09-21T07:22:51Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:22:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:22:51-07:00",
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
  "id": "1789975500.000709",
  "message_id": "1789975500.000709",
  "ts": "1789975500.000709",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 7 passed.",
  "created_at": "2026-09-21T07:25:00Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:25:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:25:00-07:00",
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
  "id": "1789975628.000710",
  "message_id": "1789975628.000710",
  "ts": "1789975628.000710",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 8 passed.",
  "created_at": "2026-09-21T07:27:08Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:27:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:27:08-07:00",
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
  "id": "1789975757.000711",
  "message_id": "1789975757.000711",
  "ts": "1789975757.000711",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 9 passed.",
  "created_at": "2026-09-21T07:29:17Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:29:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:29:17-07:00",
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
  "id": "1789975885.000712",
  "message_id": "1789975885.000712",
  "ts": "1789975885.000712",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 10 passed.",
  "created_at": "2026-09-21T07:31:25Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:31:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:31:25-07:00",
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
  "id": "1789976014.000713",
  "message_id": "1789976014.000713",
  "ts": "1789976014.000713",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 11 passed.",
  "created_at": "2026-09-21T07:33:34Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:33:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:33:34-07:00",
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
  "id": "1789976142.000714",
  "message_id": "1789976142.000714",
  "ts": "1789976142.000714",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 12 passed.",
  "created_at": "2026-09-21T07:35:42Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:35:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:35:42-07:00",
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
  "id": "1789976271.000715",
  "message_id": "1789976271.000715",
  "ts": "1789976271.000715",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 13 passed.",
  "created_at": "2026-09-21T07:37:51Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:37:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:37:51-07:00",
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
  "id": "1789976400.000716",
  "message_id": "1789976400.000716",
  "ts": "1789976400.000716",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 14 passed.",
  "created_at": "2026-09-21T07:40:00Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:40:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:40:00-07:00",
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
  "id": "1789976528.000717",
  "message_id": "1789976528.000717",
  "ts": "1789976528.000717",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 15 passed.",
  "created_at": "2026-09-21T07:42:08Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:42:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:42:08-07:00",
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
  "id": "1789976657.000718",
  "message_id": "1789976657.000718",
  "ts": "1789976657.000718",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 16 passed.",
  "created_at": "2026-09-21T07:44:17Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:44:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:44:17-07:00",
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
  "id": "1789976785.000719",
  "message_id": "1789976785.000719",
  "ts": "1789976785.000719",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 17 passed.",
  "created_at": "2026-09-21T07:46:25Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:46:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:46:25-07:00",
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
  "id": "1789976914.000720",
  "message_id": "1789976914.000720",
  "ts": "1789976914.000720",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 18 passed.",
  "created_at": "2026-09-21T07:48:34Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:48:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:48:34-07:00",
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
  "id": "1789977042.000721",
  "message_id": "1789977042.000721",
  "ts": "1789977042.000721",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 19 passed.",
  "created_at": "2026-09-21T07:50:42Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:50:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:50:42-07:00",
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
  "id": "1789977171.000722",
  "message_id": "1789977171.000722",
  "ts": "1789977171.000722",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 20 passed.",
  "created_at": "2026-09-21T07:52:51Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:52:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:52:51-07:00",
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
  "id": "1789977300.000723",
  "message_id": "1789977300.000723",
  "ts": "1789977300.000723",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 21 passed.",
  "created_at": "2026-09-21T07:55:00Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:55:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:55:00-07:00",
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
  "id": "1789977428.000724",
  "message_id": "1789977428.000724",
  "ts": "1789977428.000724",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 22 passed.",
  "created_at": "2026-09-21T07:57:08Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:57:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:57:08-07:00",
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
  "id": "1789977557.000725",
  "message_id": "1789977557.000725",
  "ts": "1789977557.000725",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 23 passed.",
  "created_at": "2026-09-21T07:59:17Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T07:59:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T00:59:17-07:00",
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
  "id": "1789977685.000726",
  "message_id": "1789977685.000726",
  "ts": "1789977685.000726",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 24 passed.",
  "created_at": "2026-09-21T08:01:25Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:01:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:01:25-07:00",
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
  "id": "1789977814.000727",
  "message_id": "1789977814.000727",
  "ts": "1789977814.000727",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 25 passed.",
  "created_at": "2026-09-21T08:03:34Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:03:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:03:34-07:00",
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
  "id": "1789977942.000728",
  "message_id": "1789977942.000728",
  "ts": "1789977942.000728",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 26 passed.",
  "created_at": "2026-09-21T08:05:42Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:05:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:05:42-07:00",
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
  "id": "1789978071.000729",
  "message_id": "1789978071.000729",
  "ts": "1789978071.000729",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 27 passed.",
  "created_at": "2026-09-21T08:07:51Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:07:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:07:51-07:00",
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
  "id": "1789978200.000730",
  "message_id": "1789978200.000730",
  "ts": "1789978200.000730",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 28 passed.",
  "created_at": "2026-09-21T08:10:00Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:10:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:10:00-07:00",
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
  "id": "1789978328.000731",
  "message_id": "1789978328.000731",
  "ts": "1789978328.000731",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 29 passed.",
  "created_at": "2026-09-21T08:12:08Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:12:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:12:08-07:00",
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
  "id": "1789978457.000732",
  "message_id": "1789978457.000732",
  "ts": "1789978457.000732",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 30 passed.",
  "created_at": "2026-09-21T08:14:17Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:14:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:14:17-07:00",
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
  "id": "1789978585.000733",
  "message_id": "1789978585.000733",
  "ts": "1789978585.000733",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 31 passed.",
  "created_at": "2026-09-21T08:16:25Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:16:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:16:25-07:00",
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
  "id": "1789978714.000734",
  "message_id": "1789978714.000734",
  "ts": "1789978714.000734",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 32 passed.",
  "created_at": "2026-09-21T08:18:34Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:18:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:18:34-07:00",
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
  "id": "1789978842.000735",
  "message_id": "1789978842.000735",
  "ts": "1789978842.000735",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 33 passed.",
  "created_at": "2026-09-21T08:20:42Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:20:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:20:42-07:00",
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
  "id": "1789978971.000736",
  "message_id": "1789978971.000736",
  "ts": "1789978971.000736",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 34 passed.",
  "created_at": "2026-09-21T08:22:51Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:22:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:22:51-07:00",
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
  "id": "1789979100.000737",
  "message_id": "1789979100.000737",
  "ts": "1789979100.000737",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 35 passed.",
  "created_at": "2026-09-21T08:25:00Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:25:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:25:00-07:00",
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
  "id": "1789979228.000738",
  "message_id": "1789979228.000738",
  "ts": "1789979228.000738",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 36 passed.",
  "created_at": "2026-09-21T08:27:08Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:27:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:27:08-07:00",
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
  "id": "1789979357.000739",
  "message_id": "1789979357.000739",
  "ts": "1789979357.000739",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 37 passed.",
  "created_at": "2026-09-21T08:29:17Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:29:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:29:17-07:00",
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
  "id": "1789979485.000740",
  "message_id": "1789979485.000740",
  "ts": "1789979485.000740",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 38 passed.",
  "created_at": "2026-09-21T08:31:25Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:31:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:31:25-07:00",
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
  "id": "1789979614.000741",
  "message_id": "1789979614.000741",
  "ts": "1789979614.000741",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 39 passed.",
  "created_at": "2026-09-21T08:33:34Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:33:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:33:34-07:00",
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
  "id": "1789979742.000742",
  "message_id": "1789979742.000742",
  "ts": "1789979742.000742",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 40 passed.",
  "created_at": "2026-09-21T08:35:42Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:35:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:35:42-07:00",
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
  "id": "1789979871.000743",
  "message_id": "1789979871.000743",
  "ts": "1789979871.000743",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 41 passed.",
  "created_at": "2026-09-21T08:37:51Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:37:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:37:51-07:00",
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
  "id": "1789980000.000744",
  "message_id": "1789980000.000744",
  "ts": "1789980000.000744",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 42 passed.",
  "created_at": "2026-09-21T08:40:00Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:40:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:40:00-07:00",
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
  "id": "1789980128.000745",
  "message_id": "1789980128.000745",
  "ts": "1789980128.000745",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 43 passed.",
  "created_at": "2026-09-21T08:42:08Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:42:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:42:08-07:00",
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
  "id": "1789980257.000746",
  "message_id": "1789980257.000746",
  "ts": "1789980257.000746",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 44 passed.",
  "created_at": "2026-09-21T08:44:17Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:44:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:44:17-07:00",
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
  "id": "1789980385.000747",
  "message_id": "1789980385.000747",
  "ts": "1789980385.000747",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 45 passed.",
  "created_at": "2026-09-21T08:46:25Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:46:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:46:25-07:00",
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
  "id": "1789980514.000748",
  "message_id": "1789980514.000748",
  "ts": "1789980514.000748",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 46 passed.",
  "created_at": "2026-09-21T08:48:34Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:48:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:48:34-07:00",
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
  "id": "1789980642.000749",
  "message_id": "1789980642.000749",
  "ts": "1789980642.000749",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 47 passed.",
  "created_at": "2026-09-21T08:50:42Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:50:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:50:42-07:00",
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
  "id": "1789980771.000750",
  "message_id": "1789980771.000750",
  "ts": "1789980771.000750",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 48 passed.",
  "created_at": "2026-09-21T08:52:51Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:52:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:52:51-07:00",
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
  "id": "1789980900.000751",
  "message_id": "1789980900.000751",
  "ts": "1789980900.000751",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 49 passed.",
  "created_at": "2026-09-21T08:55:00Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:55:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:55:00-07:00",
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
  "id": "1789981028.000752",
  "message_id": "1789981028.000752",
  "ts": "1789981028.000752",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 50 passed.",
  "created_at": "2026-09-21T08:57:08Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:57:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:57:08-07:00",
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
  "id": "1789981157.000753",
  "message_id": "1789981157.000753",
  "ts": "1789981157.000753",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 51 passed.",
  "created_at": "2026-09-21T08:59:17Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T08:59:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T01:59:17-07:00",
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
  "id": "1789981285.000754",
  "message_id": "1789981285.000754",
  "ts": "1789981285.000754",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 52 passed.",
  "created_at": "2026-09-21T09:01:25Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:01:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:01:25-07:00",
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
  "id": "1789981414.000755",
  "message_id": "1789981414.000755",
  "ts": "1789981414.000755",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 53 passed.",
  "created_at": "2026-09-21T09:03:34Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:03:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:03:34-07:00",
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
  "id": "1789981542.000756",
  "message_id": "1789981542.000756",
  "ts": "1789981542.000756",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 54 passed.",
  "created_at": "2026-09-21T09:05:42Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:05:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:05:42-07:00",
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
  "id": "1789981671.000757",
  "message_id": "1789981671.000757",
  "ts": "1789981671.000757",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 55 passed.",
  "created_at": "2026-09-21T09:07:51Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:07:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:07:51-07:00",
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
  "id": "1789981800.000758",
  "message_id": "1789981800.000758",
  "ts": "1789981800.000758",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 56 passed.",
  "created_at": "2026-09-21T09:10:00Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:10:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:10:00-07:00",
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
  "id": "1789981928.000759",
  "message_id": "1789981928.000759",
  "ts": "1789981928.000759",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 57 passed.",
  "created_at": "2026-09-21T09:12:08Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:12:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:12:08-07:00",
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
  "id": "1789982057.000760",
  "message_id": "1789982057.000760",
  "ts": "1789982057.000760",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 58 passed.",
  "created_at": "2026-09-21T09:14:17Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:14:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:14:17-07:00",
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
  "id": "1789982185.000761",
  "message_id": "1789982185.000761",
  "ts": "1789982185.000761",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 59 passed.",
  "created_at": "2026-09-21T09:16:25Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:16:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:16:25-07:00",
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
  "id": "1789982314.000762",
  "message_id": "1789982314.000762",
  "ts": "1789982314.000762",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 60 passed.",
  "created_at": "2026-09-21T09:18:34Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:18:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:18:34-07:00",
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
  "id": "1789982442.000763",
  "message_id": "1789982442.000763",
  "ts": "1789982442.000763",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 61 passed.",
  "created_at": "2026-09-21T09:20:42Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:20:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:20:42-07:00",
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
  "id": "1789982571.000764",
  "message_id": "1789982571.000764",
  "ts": "1789982571.000764",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 62 passed.",
  "created_at": "2026-09-21T09:22:51Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:22:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:22:51-07:00",
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
  "id": "1789982700.000765",
  "message_id": "1789982700.000765",
  "ts": "1789982700.000765",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 63 passed.",
  "created_at": "2026-09-21T09:25:00Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:25:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:25:00-07:00",
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
  "id": "1789982828.000766",
  "message_id": "1789982828.000766",
  "ts": "1789982828.000766",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 64 passed.",
  "created_at": "2026-09-21T09:27:08Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:27:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:27:08-07:00",
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
  "id": "1789982957.000767",
  "message_id": "1789982957.000767",
  "ts": "1789982957.000767",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 65 passed.",
  "created_at": "2026-09-21T09:29:17Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:29:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:29:17-07:00",
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
  "id": "1789983085.000768",
  "message_id": "1789983085.000768",
  "ts": "1789983085.000768",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 66 passed.",
  "created_at": "2026-09-21T09:31:25Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:31:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:31:25-07:00",
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
  "id": "1789983214.000769",
  "message_id": "1789983214.000769",
  "ts": "1789983214.000769",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 67 passed.",
  "created_at": "2026-09-21T09:33:34Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:33:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:33:34-07:00",
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
  "id": "1789983342.000770",
  "message_id": "1789983342.000770",
  "ts": "1789983342.000770",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 68 passed.",
  "created_at": "2026-09-21T09:35:42Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:35:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:35:42-07:00",
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
  "id": "1789983471.000771",
  "message_id": "1789983471.000771",
  "ts": "1789983471.000771",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 69 passed.",
  "created_at": "2026-09-21T09:37:51Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:37:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:37:51-07:00",
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
  "id": "1789983600.000772",
  "message_id": "1789983600.000772",
  "ts": "1789983600.000772",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 70 passed.",
  "created_at": "2026-09-21T09:40:00Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:40:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:40:00-07:00",
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
  "id": "1789983728.000773",
  "message_id": "1789983728.000773",
  "ts": "1789983728.000773",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 71 passed.",
  "created_at": "2026-09-21T09:42:08Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:42:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:42:08-07:00",
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
  "id": "1789983857.000774",
  "message_id": "1789983857.000774",
  "ts": "1789983857.000774",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 72 passed.",
  "created_at": "2026-09-21T09:44:17Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:44:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:44:17-07:00",
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
  "id": "1789983985.000775",
  "message_id": "1789983985.000775",
  "ts": "1789983985.000775",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 73 passed.",
  "created_at": "2026-09-21T09:46:25Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:46:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:46:25-07:00",
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
  "id": "1789984114.000776",
  "message_id": "1789984114.000776",
  "ts": "1789984114.000776",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 74 passed.",
  "created_at": "2026-09-21T09:48:34Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:48:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:48:34-07:00",
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
  "id": "1789984242.000777",
  "message_id": "1789984242.000777",
  "ts": "1789984242.000777",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 75 passed.",
  "created_at": "2026-09-21T09:50:42Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:50:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:50:42-07:00",
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
  "id": "1789984371.000778",
  "message_id": "1789984371.000778",
  "ts": "1789984371.000778",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 76 passed.",
  "created_at": "2026-09-21T09:52:51Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:52:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:52:51-07:00",
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
  "id": "1789984500.000779",
  "message_id": "1789984500.000779",
  "ts": "1789984500.000779",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 77 passed.",
  "created_at": "2026-09-21T09:55:00Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:55:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:55:00-07:00",
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
  "id": "1789984628.000780",
  "message_id": "1789984628.000780",
  "ts": "1789984628.000780",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 78 passed.",
  "created_at": "2026-09-21T09:57:08Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:57:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:57:08-07:00",
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
  "id": "1789984757.000781",
  "message_id": "1789984757.000781",
  "ts": "1789984757.000781",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 79 passed.",
  "created_at": "2026-09-21T09:59:17Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T09:59:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T02:59:17-07:00",
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
  "id": "1789984885.000782",
  "message_id": "1789984885.000782",
  "ts": "1789984885.000782",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 80 passed.",
  "created_at": "2026-09-21T10:01:25Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:01:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:01:25-07:00",
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
  "id": "1789985014.000783",
  "message_id": "1789985014.000783",
  "ts": "1789985014.000783",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 81 passed.",
  "created_at": "2026-09-21T10:03:34Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:03:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:03:34-07:00",
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
  "id": "1789985142.000784",
  "message_id": "1789985142.000784",
  "ts": "1789985142.000784",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 82 passed.",
  "created_at": "2026-09-21T10:05:42Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:05:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:05:42-07:00",
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
  "id": "1789985271.000785",
  "message_id": "1789985271.000785",
  "ts": "1789985271.000785",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 83 passed.",
  "created_at": "2026-09-21T10:07:51Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:07:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:07:51-07:00",
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
  "id": "1789985400.000786",
  "message_id": "1789985400.000786",
  "ts": "1789985400.000786",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 84 passed.",
  "created_at": "2026-09-21T10:10:00Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:10:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:10:00-07:00",
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
  "id": "1789985528.000787",
  "message_id": "1789985528.000787",
  "ts": "1789985528.000787",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 85 passed.",
  "created_at": "2026-09-21T10:12:08Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:12:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:12:08-07:00",
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
  "id": "1789985657.000788",
  "message_id": "1789985657.000788",
  "ts": "1789985657.000788",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 86 passed.",
  "created_at": "2026-09-21T10:14:17Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:14:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:14:17-07:00",
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
  "id": "1789985785.000789",
  "message_id": "1789985785.000789",
  "ts": "1789985785.000789",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 87 passed.",
  "created_at": "2026-09-21T10:16:25Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:16:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:16:25-07:00",
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
  "id": "1789985914.000790",
  "message_id": "1789985914.000790",
  "ts": "1789985914.000790",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 88 passed.",
  "created_at": "2026-09-21T10:18:34Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:18:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:18:34-07:00",
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
  "id": "1789986042.000791",
  "message_id": "1789986042.000791",
  "ts": "1789986042.000791",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 89 passed.",
  "created_at": "2026-09-21T10:20:42Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:20:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:20:42-07:00",
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
  "id": "1789986171.000792",
  "message_id": "1789986171.000792",
  "ts": "1789986171.000792",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 90 passed.",
  "created_at": "2026-09-21T10:22:51Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:22:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:22:51-07:00",
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
  "id": "1789986300.000793",
  "message_id": "1789986300.000793",
  "ts": "1789986300.000793",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 91 passed.",
  "created_at": "2026-09-21T10:25:00Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:25:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:25:00-07:00",
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
  "id": "1789986428.000794",
  "message_id": "1789986428.000794",
  "ts": "1789986428.000794",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 92 passed.",
  "created_at": "2026-09-21T10:27:08Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:27:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:27:08-07:00",
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
  "id": "1789986557.000795",
  "message_id": "1789986557.000795",
  "ts": "1789986557.000795",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 93 passed.",
  "created_at": "2026-09-21T10:29:17Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:29:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:29:17-07:00",
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
  "id": "1789986685.000796",
  "message_id": "1789986685.000796",
  "ts": "1789986685.000796",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 94 passed.",
  "created_at": "2026-09-21T10:31:25Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:31:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:31:25-07:00",
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
  "id": "1789986814.000797",
  "message_id": "1789986814.000797",
  "ts": "1789986814.000797",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 95 passed.",
  "created_at": "2026-09-21T10:33:34Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:33:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:33:34-07:00",
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
  "id": "1789986942.000798",
  "message_id": "1789986942.000798",
  "ts": "1789986942.000798",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 96 passed.",
  "created_at": "2026-09-21T10:35:42Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:35:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:35:42-07:00",
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
  "id": "1789987071.000799",
  "message_id": "1789987071.000799",
  "ts": "1789987071.000799",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 97 passed.",
  "created_at": "2026-09-21T10:37:51Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:37:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:37:51-07:00",
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
  "id": "1789987200.000800",
  "message_id": "1789987200.000800",
  "ts": "1789987200.000800",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 98 passed.",
  "created_at": "2026-09-21T10:40:00Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:40:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:40:00-07:00",
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
  "id": "1789987328.000801",
  "message_id": "1789987328.000801",
  "ts": "1789987328.000801",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 99 passed.",
  "created_at": "2026-09-21T10:42:08Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:42:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:42:08-07:00",
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
  "id": "1789987457.000802",
  "message_id": "1789987457.000802",
  "ts": "1789987457.000802",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 100 passed.",
  "created_at": "2026-09-21T10:44:17Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:44:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:44:17-07:00",
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
  "id": "1789987585.000803",
  "message_id": "1789987585.000803",
  "ts": "1789987585.000803",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 101 passed.",
  "created_at": "2026-09-21T10:46:25Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:46:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:46:25-07:00",
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
  "id": "1789987714.000804",
  "message_id": "1789987714.000804",
  "ts": "1789987714.000804",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 102 passed.",
  "created_at": "2026-09-21T10:48:34Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:48:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:48:34-07:00",
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
  "id": "1789987842.000805",
  "message_id": "1789987842.000805",
  "ts": "1789987842.000805",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 103 passed.",
  "created_at": "2026-09-21T10:50:42Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:50:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:50:42-07:00",
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
  "id": "1789987971.000806",
  "message_id": "1789987971.000806",
  "ts": "1789987971.000806",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 104 passed.",
  "created_at": "2026-09-21T10:52:51Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:52:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:52:51-07:00",
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
  "id": "1789988100.000807",
  "message_id": "1789988100.000807",
  "ts": "1789988100.000807",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 105 passed.",
  "created_at": "2026-09-21T10:55:00Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:55:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:55:00-07:00",
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
  "id": "1789988228.000808",
  "message_id": "1789988228.000808",
  "ts": "1789988228.000808",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 106 passed.",
  "created_at": "2026-09-21T10:57:08Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:57:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:57:08-07:00",
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
  "id": "1789988357.000809",
  "message_id": "1789988357.000809",
  "ts": "1789988357.000809",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 107 passed.",
  "created_at": "2026-09-21T10:59:17Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T10:59:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T03:59:17-07:00",
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
  "id": "1789988485.000810",
  "message_id": "1789988485.000810",
  "ts": "1789988485.000810",
  "channel_id": "C_LAUNCH",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Launch checklist check 108 passed.",
  "created_at": "2026-09-21T11:01:25Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:01:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:01:25-07:00",
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
  "id": "1789988614.000811",
  "message_id": "1789988614.000811",
  "ts": "1789988614.000811",
  "channel_id": "C_LAUNCH",
  "user_id": "U01AGENBOT9 (Agent Bot)",
  "message_text": "Launch checklist check 109 passed.",
  "created_at": "2026-09-21T11:03:34Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:03:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:03:34-07:00",
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
  "id": "1789988742.000812",
  "message_id": "1789988742.000812",
  "ts": "1789988742.000812",
  "channel_id": "C_LAUNCH",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Launch checklist check 110 passed.",
  "created_at": "2026-09-21T11:05:42Z",
  "channel": "launch-readiness",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-21T11:05:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-21T04:05:42-07:00",
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
 }
]
