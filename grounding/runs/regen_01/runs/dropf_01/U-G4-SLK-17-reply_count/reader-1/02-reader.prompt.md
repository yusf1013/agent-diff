Step 2. These are all the records in the service:

### channel_members (15)
{"channel_id": "C_OUT", "user_id": "U01AGENBOT9", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_OUT", "user_id": "U_NADIA", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_OUT", "user_id": "U_FELIX", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_OUT", "user_id": "U_SOFIA", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_OUT", "user_id": "U_MARCUS", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_OUT", "user_id": "U_HANNAH", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_OUT", "user_id": "U_DIEGO", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_OUT", "user_id": "U_OMAR", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_OUT", "user_id": "U_AISHA", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_OTHER", "user_id": "U01AGENBOT9", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_OTHER", "user_id": "U_SOFIA", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_OTHER", "user_id": "U_DIEGO", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_OTHER", "user_id": "U_OMAR", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_FOLLOW", "user_id": "U01AGENBOT9", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_FOLLOW", "user_id": "U_DIEGO", "joined_at": "2026-01-05T09:05:00Z"}
### channels (3)
{"channel_id": "C_OUT", "channel_name": "outages", "team_id": "T1", "is_private": false, "is_dm": false, "is_gc": false, "created_at": "2026-01-05T09:00:00Z", "is_archived": false}
{"channel_id": "C_OTHER", "channel_name": "deploys", "team_id": "T1", "is_private": false, "is_dm": false, "is_gc": false, "created_at": "2026-01-05T09:00:00Z", "is_archived": false}
{"channel_id": "C_FOLLOW", "channel_name": "followups", "team_id": "T1", "is_private": false, "is_dm": false, "is_gc": false, "created_at": "2026-01-05T09:00:00Z", "is_archived": false}
### messages (19)
{"message_id": "1789992600.000001", "channel_id": "C_OUT", "user_id": "U_NADIA", "message_text": "Heads up: lattice outage in eu-west, failover started, tracking here.", "type": "message", "ts": "1789992600.000001", "created_at": "2026-09-21T12:10:00Z"}
{"message_id": "1789992900.000002", "channel_id": "C_OUT", "user_id": "U_NADIA", "message_text": "Adding context: failover is underway.", "type": "message", "ts": "1789992900.000002", "created_at": "2026-09-21T12:15:00Z", "parent_id": "1789992600.000001"}
{"message_id": "1789993200.000003", "channel_id": "C_OUT", "user_id": "U_NADIA", "message_text": "Update: paging the secondary now.", "type": "message", "ts": "1789993200.000003", "created_at": "2026-09-21T12:20:00Z", "parent_id": "1789992600.000001"}
{"message_id": "1789993800.000004", "channel_id": "C_OUT", "user_id": "U_FELIX", "message_text": "Morning standup notes are up, please review before noon.", "type": "message", "ts": "1789993800.000004", "created_at": "2026-09-21T12:30:00Z", "blocks": [{"type": "section", "text": {"type": "mrkdwn", "text": "Lattice outage retro notes attached, see thread."}}]}
{"message_id": "1789993980.000005", "channel_id": "C_OUT", "user_id": "U_FELIX", "message_text": "Got it, reviewing now.", "type": "message", "ts": "1789993980.000005", "created_at": "2026-09-21T12:33:00Z", "parent_id": "1789993800.000004"}
{"message_id": "1789994160.000006", "channel_id": "C_OUT", "user_id": "U_FELIX", "message_text": "Left comments on the doc.", "type": "message", "ts": "1789994160.000006", "created_at": "2026-09-21T12:36:00Z", "parent_id": "1789993800.000004"}
{"message_id": "1789990800.000007", "channel_id": "C_OUT", "user_id": "U_SOFIA", "message_text": "Deploys are green today, no action needed.", "type": "message", "ts": "1789990800.000007", "created_at": "2026-09-21T11:40:00Z"}
{"message_id": "1789991100.000008", "channel_id": "C_OUT", "user_id": "U_SOFIA", "message_text": "Great, thanks for checking.", "type": "message", "ts": "1789991100.000008", "created_at": "2026-09-21T11:45:00Z", "parent_id": "1789990800.000007"}
{"message_id": "1789991400.000009", "channel_id": "C_OUT", "user_id": "U_SOFIA", "message_text": "Green here too.", "type": "message", "ts": "1789991400.000009", "created_at": "2026-09-21T11:50:00Z", "parent_id": "1789990800.000007"}
{"message_id": "1789994700.000010", "channel_id": "C_OTHER", "user_id": "U_SOFIA", "message_text": "Update: lattice outage in eu-west, failover started.", "type": "message", "ts": "1789994700.000010", "created_at": "2026-09-21T12:45:00Z"}
{"message_id": "1789994880.000011", "channel_id": "C_OTHER", "user_id": "U_SOFIA", "message_text": "Seeing the same from my side.", "type": "message", "ts": "1789994880.000011", "created_at": "2026-09-21T12:48:00Z", "parent_id": "1789994700.000010"}
{"message_id": "1789995120.000012", "channel_id": "C_OTHER", "user_id": "U_SOFIA", "message_text": "Joining the call now.", "type": "message", "ts": "1789995120.000012", "created_at": "2026-09-21T12:52:00Z", "parent_id": "1789994700.000010"}
{"message_id": "1789992300.000013", "channel_id": "C_OUT", "user_id": "U_MARCUS", "message_text": "Heads up: lattice outage in eu-west, failover started, tracking here.", "type": "message", "ts": "1789992300.000013", "created_at": "2026-09-21T12:05:00Z"}
{"message_id": "1789992360.000014", "channel_id": "C_OUT", "user_id": "U_MARCUS", "message_text": "Ack.", "type": "message", "ts": "1789992360.000014", "created_at": "2026-09-21T12:06:00Z", "parent_id": "1789992300.000013"}
{"message_id": "1789992420.000015", "channel_id": "C_OUT", "user_id": "U_MARCUS", "message_text": "Looking at graphs.", "type": "message", "ts": "1789992420.000015", "created_at": "2026-09-21T12:07:00Z", "parent_id": "1789992300.000013"}
{"message_id": "1789992480.000016", "channel_id": "C_OUT", "user_id": "U_MARCUS", "message_text": "Paging the secondary.", "type": "message", "ts": "1789992480.000016", "created_at": "2026-09-21T12:08:00Z", "parent_id": "1789992300.000013"}
{"message_id": "1789995000.000017", "channel_id": "C_OUT", "user_id": "U_HANNAH", "message_text": "Heads up: lattice outage in eu-west, failover started.", "type": "message", "ts": "1789995000.000017", "created_at": "2026-09-21T12:50:00Z"}
{"message_id": "1789995300.000018", "channel_id": "C_OUT", "user_id": "U_HANNAH", "message_text": "Ack, on my way.", "type": "message", "ts": "1789995300.000018", "created_at": "2026-09-21T12:55:00Z", "parent_id": "1789995000.000017"}
{"message_id": "1789905600.000019", "channel_id": "C_OTHER", "user_id": "U_DIEGO", "message_text": "Anyone for lunch at noon?", "type": "message", "ts": "1789905600.000019", "created_at": "2026-09-20T12:00:00Z"}
### teams (1)
{"team_id": "T1", "team_name": "Northwind", "created_at": "2025-01-01T00:00:00Z"}
### user_teams (12)
{"user_id": "U01AGENBOT9", "team_id": "T1", "role": "admin"}
{"user_id": "U_PRIYA", "team_id": "T1", "role": "member"}
{"user_id": "U_DIEGO", "team_id": "T1", "role": "member"}
{"user_id": "U_LEO", "team_id": "T1", "role": "member"}
{"user_id": "U_OMAR", "team_id": "T1", "role": "member"}
{"user_id": "U_AISHA", "team_id": "T1", "role": "member"}
{"user_id": "U_MAYA", "team_id": "T1", "role": "member"}
{"user_id": "U_NADIA", "team_id": "T1", "role": "member"}
{"user_id": "U_FELIX", "team_id": "T1", "role": "member"}
{"user_id": "U_SOFIA", "team_id": "T1", "role": "member"}
{"user_id": "U_MARCUS", "team_id": "T1", "role": "member"}
{"user_id": "U_HANNAH", "team_id": "T1", "role": "member"}
### users (12)
{"user_id": "U01AGENBOT9", "username": "agentbot", "email": "agentbot@northwind.example", "real_name": "Agent Bot", "display_name": "AgentBot", "created_at": "2025-01-01T00:05:00Z", "is_bot": true, "is_active": true}
{"user_id": "U_PRIYA", "username": "priya.sharma", "email": "priya.sharma@northwind.example", "real_name": "Priya Sharma", "display_name": "Priya", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}
{"user_id": "U_DIEGO", "username": "diego.alvarez", "email": "diego.alvarez@northwind.example", "real_name": "Diego Alvarez", "display_name": "Diego", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}
{"user_id": "U_LEO", "username": "leo.park", "email": "leo.park@northwind.example", "real_name": "Leo Park", "display_name": "Leo", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}
{"user_id": "U_OMAR", "username": "omar.haddad", "email": "omar.haddad@northwind.example", "real_name": "Omar Haddad", "display_name": "Omar", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}
{"user_id": "U_AISHA", "username": "aisha.khan", "email": "aisha.khan@northwind.example", "real_name": "Aisha Khan", "display_name": "Aisha", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}
{"user_id": "U_MAYA", "username": "maya.chen", "email": "maya.chen@northwind.example", "real_name": "Maya Chen", "display_name": "Maya", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}
{"user_id": "U_NADIA", "username": "nadia.rahman", "email": "nadia.rahman@northwind.example", "real_name": "Nadia Rahman", "display_name": "Nadia", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}
{"user_id": "U_FELIX", "username": "felix.nguyen", "email": "felix.nguyen@northwind.example", "real_name": "Felix Nguyen", "display_name": "Felix", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}
{"user_id": "U_SOFIA", "username": "sofia.reyes", "email": "sofia.reyes@northwind.example", "real_name": "Sofia Reyes", "display_name": "Sofia", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}
{"user_id": "U_MARCUS", "username": "marcus.webb", "email": "marcus.webb@northwind.example", "real_name": "Marcus Webb", "display_name": "Marcus", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}
{"user_id": "U_HANNAH", "username": "hannah.kim", "email": "hannah.kim@northwind.example", "real_name": "Hannah Kim", "display_name": "Hannah", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}

Use your own conditions from step 1 as the author's conditions, with these ids:
- r1: is a Slack user who authored a post/message (the invitee is the author)
- r2: that post/message is about the lattice outage
- r3: that post/message was posted in the #outages channel
- r4: that same user is the one to be invited to the #followups channel

The candidate records are the rows of `users`: U01AGENBOT9, U_PRIYA, U_DIEGO, U_LEO, U_OMAR, U_AISHA, U_MAYA, U_NADIA, U_FELIX, U_SOFIA, U_MARCUS, U_HANNAH.
For every candidate, give the ids of the conditions it fails under the careful reading (an empty list if it meets all of them), whether a careful colleague could still argue that it meets the request (contestable), and a short note. Then say whether the conditions faithfully capture the request as you read it in step 1 (and what differs). For each ambiguity you listed, say whether a careful reader would genuinely be unsure which reading was meant, and whether the readings select different candidates. Say whether the request reads like something a real user would write, without hints that only a test would contain. Finally, say whether the request refers to one specific record, as "the ..." does (asks_for_one: true), as opposed to allowing any record of a kind ("a ...") or asking for several (asks_for_one: false), and why.