Step 2. These are all the records in the service:

### channel_members (3)
{"channel_id": "C_INC482", "user_id": "U01AGENBOT9", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_INC482", "user_id": "U_DIEGO", "joined_at": "2026-01-05T09:05:00Z"}
{"channel_id": "C_INC482", "user_id": "U_LEO", "joined_at": "2026-01-05T09:05:00Z"}
### channels (1)
{"channel_id": "C_INC482", "channel_name": "incident-482", "team_id": "T1", "topic_text": "Payments checkout outage", "is_private": false, "is_dm": false, "is_gc": false, "created_at": "2026-01-05T09:00:00Z", "is_archived": false}
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
{"user_id": "U_SOFIA", "team_id": "T1", "role": "member"}
{"user_id": "U_MARTA", "team_id": "T1", "role": "member"}
{"user_id": "U_FELIX", "team_id": "T1", "role": "member"}
{"user_id": "U_LUKAS", "team_id": "T1", "role": "member"}
{"user_id": "U_NOAH", "team_id": "T1", "role": "member"}
### users (12)
{"user_id": "U01AGENBOT9", "username": "agentbot", "email": "agentbot@northwind.example", "real_name": "Agent Bot", "display_name": "AgentBot", "created_at": "2025-01-01T00:05:00Z", "is_bot": true, "is_active": true}
{"user_id": "U_PRIYA", "username": "priya.sharma", "email": "priya.sharma@northwind.example", "real_name": "Priya Sharma", "display_name": "Priya", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}
{"user_id": "U_DIEGO", "username": "diego.alvarez", "email": "diego.alvarez@northwind.example", "real_name": "Diego Alvarez", "display_name": "Diego", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}
{"user_id": "U_LEO", "username": "leo.park", "email": "leo.park@northwind.example", "real_name": "Leo Park", "display_name": "Leo", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}
{"user_id": "U_OMAR", "username": "omar.haddad", "email": "omar.haddad@northwind.example", "real_name": "Omar Haddad", "display_name": "Omar", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}
{"user_id": "U_AISHA", "username": "aisha.khan", "email": "aisha.khan@northwind.example", "real_name": "Aisha Khan", "display_name": "Aisha", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}
{"user_id": "U_MAYA", "username": "maya.chen", "email": "maya.chen@northwind.example", "real_name": "Maya Chen", "display_name": "Maya", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}
{"user_id": "U_SOFIA", "username": "sofia.martins", "email": "sofia.martins@northwind.example", "real_name": "Sofia Martins", "display_name": "Sofia", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true, "title": "Site Reliability Engineer", "timezone": "Europe/Berlin"}
{"user_id": "U_MARTA", "username": "marta.silva", "email": "marta.silva@northwind.example", "real_name": "Marta Silva", "display_name": "Marta Silva (Site Reliability Engineer)", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true, "title": "Support Engineer", "timezone": "Europe/Berlin"}
{"user_id": "U_FELIX", "username": "felix.bauer", "email": "felix.bauer@northwind.example", "real_name": "Felix Bauer", "display_name": "Felix", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true, "title": "Platform Engineer", "timezone": "Europe/Berlin"}
{"user_id": "U_LUKAS", "username": "lukas.weber", "email": "lukas.weber@northwind.example", "real_name": "Lukas Weber", "display_name": "Lukas", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true, "title": "Site Reliability Engineer", "timezone": "Europe/London"}
{"user_id": "U_NOAH", "username": "noah.fischer", "email": "noah.fischer@northwind.example", "real_name": "Noah Fischer", "display_name": "Noah", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": false, "title": "Site Reliability Engineer", "timezone": "Europe/Berlin"}

The author lists these conditions of the request:
- c1: active
- c2: Site Reliability Engineer
- c3: based in the Europe/Berlin time zone

The candidate records are the rows of `users`: U01AGENBOT9, U_PRIYA, U_DIEGO, U_LEO, U_OMAR, U_AISHA, U_MAYA, U_SOFIA, U_MARTA, U_FELIX, U_LUKAS, U_NOAH.
For every candidate, give the ids of the author's conditions it fails (an empty list if it meets all of them), with a short note. Then say whether the author's conditions faithfully capture the request as you read it in step 1 (and what differs), whether each ambiguity you listed changes which candidates match, and whether the request reads like something a real user would write.