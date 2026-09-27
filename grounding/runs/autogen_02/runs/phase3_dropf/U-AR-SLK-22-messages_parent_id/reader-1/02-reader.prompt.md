Step 2. These are all the records in the service:

### channel_members (5)
{"channel_id": "C_LAUNCH", "user_id": "U01AGENBOT9", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_LAUNCH", "user_id": "U_LEO", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_LAUNCH", "user_id": "U_DIEGO", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_LAUNCH", "user_id": "U_OMAR", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_LAUNCH", "user_id": "U_AISHA", "joined_at": "2026-01-05T09:05:00Z"}
### channels (1)
{"channel_id": "C_LAUNCH", "channel_name": "launch-prep", "team_id": "T1", "is_private": false, "is_dm": false, "is_gc": false, "created_at": "2026-01-05T09:00:00Z", "is_archived": false}
### message_reactions (1)
{"message_id": "1790078880.000004", "user_id": "U_LEO", "reaction_type": "clap", "created_at": "2026-09-22T12:09:00Z"}
### messages (5)
{"message_id": "1790077800.000001", "channel_id": "C_LAUNCH", "user_id": "U_DIEGO", "message_text": "Anyone want tacos for lunch?", "type": "message", "ts": "1790077800.000001", "created_at": "2026-09-22T11:50:00Z"}
{"message_id": "1790078700.000002", "channel_id": "C_LAUNCH", "user_id": "U_DIEGO", "message_text": "Reply here once you've signed off on tonight's payments launch checklist.", "type": "message", "ts": "1790078700.000002", "created_at": "2026-09-22T12:05:00Z"}
{"message_id": "1790078760.000003", "channel_id": "C_LAUNCH", "user_id": "U_LEO", "message_text": "Reminder: payments launch checklist review starts at 6pm tonight.", "type": "message", "ts": "1790078760.000003", "created_at": "2026-09-22T12:06:00Z"}
{"message_id": "1790078880.000004", "channel_id": "C_LAUNCH", "user_id": "U_OMAR", "message_text": "Signed off on my end, checklist looks good.", "type": "message", "ts": "1790078880.000004", "created_at": "2026-09-22T12:08:00Z", "parent_id": "1790078700.000002"}
{"message_id": "1790079120.000005", "channel_id": "C_LAUNCH", "user_id": "U_LEO", "message_text": "All checklists are in, we're clear to ship.", "type": "message", "ts": "1790079120.000005", "created_at": "2026-09-22T12:12:00Z", "parent_id": "1790078700.000002"}
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
- r1: The record is a message in the channel #launch-prep
- r2: The message was authored by Leo Park
- r3: The reaction to be added is the rocket emoji (:rocket:)

The candidate records are the rows of `messages`: 1790077800.000001, 1790078700.000002, 1790078760.000003, 1790078880.000004, 1790079120.000005.
For every candidate, give the ids of the conditions it fails under the careful reading (an empty list if it meets all of them), whether a careful colleague could still argue that it meets the request (contestable), and a short note. Then say whether the conditions faithfully capture the request as you read it in step 1 (and what differs). For each ambiguity you listed, say whether a careful reader would genuinely be unsure which reading was meant, and whether the readings select different candidates. Say whether the request reads like something a real user would write, without hints that only a test would contain. Finally, say whether the request refers to one specific record, as "the ..." does (asks_for_one: true), as opposed to allowing any record of a kind ("a ...") or asking for several (asks_for_one: false), and why.