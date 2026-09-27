Step 2. These are all the records in the service:

### channel_members (4)
{"channel_id": "C_LAUNCH", "user_id": "U01AGENBOT9", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_LAUNCH", "user_id": "U_MAYA", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_LAUNCH", "user_id": "U_DIEGO", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_LAUNCH", "user_id": "U_LEO", "joined_at": "2026-01-05T09:05:00Z"}
### channels (1)
{"channel_id": "C_LAUNCH", "channel_name": "launch-readiness", "team_id": "T1", "topic_text": "Q3 launch — rollback steps draft parked here", "is_private": false, "is_dm": false, "is_gc": false, "created_at": "2026-01-05T09:00:00Z", "is_archived": false}
### messages (6)
{"message_id": "1789989000.000001", "channel_id": "C_LAUNCH", "user_id": "U_MAYA", "message_text": "Launch readiness — card below with the final sequence.", "type": "message", "ts": "1789989000.000001", "created_at": "2026-09-21T11:10:00Z", "blocks": [{"type": "section", "text": {"type": "mrkdwn", "text": "Launch checklist card: rollback steps — 1) halt deploys 2) restore snapshot 3) verify health"}}]}
{"message_id": "1789989900.000002", "channel_id": "C_LAUNCH", "user_id": "U_MAYA", "message_text": "Launch checklist: rollback steps — 1) halt deploys 2) restore snapshot 3) verify health", "type": "message", "ts": "1789989900.000002", "created_at": "2026-09-21T11:25:00Z"}
{"message_id": "1789990800.000003", "channel_id": "C_LAUNCH", "user_id": "U_MAYA", "message_text": "Launch readiness — verification card below.", "type": "message", "ts": "1789990800.000003", "created_at": "2026-09-21T11:40:00Z", "blocks": [{"type": "section", "text": {"type": "mrkdwn", "text": "Follow-up card: verification checklist — 1) confirm monitors 2) note owners"}}]}
{"message_id": "1789992300.000004", "channel_id": "C_LAUNCH", "user_id": "U_MAYA", "message_text": "Launch readiness — card below with the final sequence.", "type": "message", "ts": "1789992300.000004", "created_at": "2026-09-21T12:05:00Z", "blocks": [{"type": "section", "text": {"type": "mrkdwn", "text": "Launch checklist card: rollout steps — 1) open flags 2) ramp traffic 3) monitor errors"}}]}
{"message_id": "1789991400.000005", "channel_id": "C_LAUNCH", "user_id": "U_LEO", "message_text": "Launch readiness — card below.", "type": "message", "ts": "1789991400.000005", "created_at": "2026-09-21T11:50:00Z", "blocks": [{"type": "section", "text": {"type": "mrkdwn", "text": "Launch checklist card: cleanup steps — 1) close flags 2) file notes"}}]}
{"message_id": "1789991700.000006", "channel_id": "C_LAUNCH", "user_id": "U_DIEGO", "message_text": "Launch readiness — card below.", "type": "message", "ts": "1789991700.000006", "created_at": "2026-09-21T11:55:00Z", "blocks": [{"type": "section", "text": {"type": "mrkdwn", "text": "Launch checklist card: handoff notes — 1) page owner 2) link dashboard"}}]}
### teams (1)
{"team_id": "T1", "team_name": "Northwind", "created_at": "2025-01-01T00:00:00Z"}
### user_teams (7)
{"user_id": "U01AGENBOT9", "team_id": "T1", "role": "admin"}
{"user_id": "U_PRIYA", "team_id": "T1", "role": "member"}
{"user_id": "U_DIEGO", "team_id": "T1", "role": "member"}
{"user_id": "U_LEO", "team_id": "T1", "role": "member"}
{"user_id": "U_OMAR", "team_id": "T1", "role": "member"}
{"user_id": "U_AISHA", "team_id": "T1", "role": "member"}
{"user_id": "U_MAYA", "team_id": "T1", "role": "member"}
### users (7)
{"user_id": "U01AGENBOT9", "username": "agentbot", "email": "agentbot@northwind.example", "real_name": "Agent Bot", "display_name": "AgentBot", "created_at": "2025-01-01T00:05:00Z", "is_bot": true, "is_active": true}
{"user_id": "U_PRIYA", "username": "priya.sharma", "email": "priya.sharma@northwind.example", "real_name": "Priya Sharma", "display_name": "Priya", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}
{"user_id": "U_DIEGO", "username": "diego.alvarez", "email": "diego.alvarez@northwind.example", "real_name": "Diego Alvarez", "display_name": "Diego", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}
{"user_id": "U_LEO", "username": "leo.park", "email": "leo.park@northwind.example", "real_name": "Leo Park", "display_name": "Leo", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}
{"user_id": "U_OMAR", "username": "omar.haddad", "email": "omar.haddad@northwind.example", "real_name": "Omar Haddad", "display_name": "Omar", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}
{"user_id": "U_AISHA", "username": "aisha.khan", "email": "aisha.khan@northwind.example", "real_name": "Aisha Khan", "display_name": "Aisha", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}
{"user_id": "U_MAYA", "username": "maya.chen", "email": "maya.chen@northwind.example", "real_name": "Maya Chen", "display_name": "Maya", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}

Use your own conditions from step 1 as the author's conditions, with these ids:
- r1: record is a Slack message that can receive a reaction
- r2: the message was authored by the exact person Maya Chen
- r3: the message is in the channel #launch-readiness

The candidate records are the rows of `messages`: 1789989000.000001, 1789989900.000002, 1789990800.000003, 1789992300.000004, 1789991400.000005, 1789991700.000006.
For every candidate, give the ids of the conditions it fails under the careful reading (an empty list if it meets all of them), whether a careful colleague could still argue that it meets the request (contestable), and a short note. Then say whether the conditions faithfully capture the request as you read it in step 1 (and what differs). For each ambiguity you listed, say whether a careful reader would genuinely be unsure which reading was meant, and whether the readings select different candidates. Say whether the request reads like something a real user would write, without hints that only a test would contain. Finally, say whether the request refers to one specific record, as "the ..." does (asks_for_one: true), as opposed to allowing any record of a kind ("a ...") or asking for several (asks_for_one: false), and why.