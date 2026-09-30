Step 2. These are all the records in the service:

### channel_members (14)
{"channel_id": "D_PRIYA", "user_id": "U01AGENBOT9", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "D_PRIYA", "user_id": "U_PRIYA", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "G_PO", "user_id": "U01AGENBOT9"}
{"channel_id": "G_PO", "user_id": "U_PRIYA"}
{"channel_id": "G_PO", "user_id": "U_OMAR"}
{"channel_id": "C_BILL", "user_id": "U01AGENBOT9", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_BILL", "user_id": "U_PRIYA", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_BILL", "user_id": "U_DIEGO", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_BILL", "user_id": "U_LEO", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "D_OMAR", "user_id": "U01AGENBOT9", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "D_OMAR", "user_id": "U_OMAR", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_GEN", "user_id": "U01AGENBOT9", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_GEN", "user_id": "U_DIEGO", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_GEN", "user_id": "U_OMAR", "joined_at": "2026-01-05T09:05:00Z"}
### channels (5)
{"channel_id": "D_PRIYA", "channel_name": "D_PRIYA", "team_id": "T1", "is_private": true, "is_dm": true, "is_gc": false, "created_at": "2026-01-05T09:00:00Z", "is_archived": false}
{"channel_id": "G_PO", "is_dm": false, "is_gc": true, "is_private": true}
{"channel_id": "C_BILL", "channel_name": "billing", "team_id": "T1", "is_private": false, "is_dm": false, "is_gc": false, "created_at": "2026-01-05T09:00:00Z", "is_archived": false}
{"channel_id": "D_OMAR", "channel_name": "D_OMAR", "team_id": "T1", "is_private": true, "is_dm": true, "is_gc": false, "created_at": "2026-01-05T09:00:00Z", "is_archived": false}
{"channel_id": "C_GEN", "channel_name": "general", "team_id": "T1", "is_private": false, "is_dm": false, "is_gc": false, "created_at": "2026-01-05T09:00:00Z", "is_archived": false}
### messages (7)
{"message_id": "1790683500.000001", "channel_id": "D_PRIYA", "user_id": "U_PRIYA", "message_text": "The billing migration is live in prod. All charges now route to the new service.", "type": "message", "ts": "1790683500.000001", "created_at": "2026-09-29T12:05:00Z"}
{"message_id": "1790682000.000002", "channel_id": "G_PO", "user_id": "U_PRIYA", "message_text": "The billing migration is live now. Omar, can you verify the EU region too?", "type": "message", "ts": "1790682000.000002", "created_at": "2026-09-29T11:40:00Z"}
{"message_id": "1790682300.000003", "channel_id": "G_PO", "user_id": "U_OMAR", "message_text": "On it. Checking the EU region now.", "type": "message", "ts": "1790682300.000003", "created_at": "2026-09-29T11:45:00Z"}
{"message_id": "1790680800.000004", "channel_id": "C_BILL", "user_id": "U_PRIYA", "message_text": "Billing migration is live across all tiers. Please report any regressions here.", "type": "message", "ts": "1790680800.000004", "created_at": "2026-09-29T11:20:00Z"}
{"message_id": "1790681400.000005", "channel_id": "C_BILL", "user_id": "U_DIEGO", "message_text": "Confirming, all green on our side.", "type": "message", "ts": "1790681400.000005", "created_at": "2026-09-29T11:30:00Z"}
{"message_id": "1790673000.000006", "channel_id": "D_OMAR", "user_id": "U_OMAR", "message_text": "Hey, did the standup notes go out this morning?", "type": "message", "ts": "1790673000.000006", "created_at": "2026-09-29T09:10:00Z"}
{"message_id": "1790676000.000007", "channel_id": "C_GEN", "user_id": "U_DIEGO", "message_text": "Lunch on Friday at the usual place?", "type": "message", "ts": "1790676000.000007", "created_at": "2026-09-29T10:00:00Z"}
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

The author lists these conditions of the request:
- c1: in your DM with her
- c2: the message Priya Sharma sent
- c3: that says the billing migration is live

The candidate records are the rows of `messages`: 1790683500.000001, 1790682000.000002, 1790682300.000003, 1790680800.000004, 1790681400.000005, 1790673000.000006, 1790676000.000007.
For every candidate, give the ids of the author's conditions it fails under the careful reading (an empty list if it meets all of them), whether a careful colleague could still argue that it meets the request (contestable), and a short note. Then say whether the author's conditions faithfully capture the request as you read it in step 1 (and what differs). For each ambiguity you listed, say whether a careful reader would genuinely be unsure which reading was meant, and whether the readings select different candidates. Finally, say whether the request reads like something a real user would write, without hints that only a test would contain.