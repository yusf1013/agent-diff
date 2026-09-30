The replica pre-checks found these problems:
- Replica install or read failed: IntegrityError: (psycopg2.errors.UniqueViolation) duplicate key value violates unique constraint "users_pkey"
DETAIL:  Key (user_id)=(U_PRIYA) already exists.

[SQL: INSERT INTO "slack_campaign_94c2fe49ca0d484684fa42ca184a8a64"."users" ("user_id", "username", "email", "real_name", "display_name", "created_at", "is_bot", "is_active") VALUES (%(v0)s, %(v1)s, %(v2)s, %(v3)s, %(v4)s, %(v5)s, %(v6)s, %(v7)s)]
[parameters: {'v0': 'U_PRIYA', 'v1': 'priya.sharma', 'v2': 'priya.sharma@northwind.example', 'v3': 'Priya Sharma', 'v4': 'Priya', 'v5': datetime.datetime(2025, 1, 1, 0, 5), 'v6': False, 'v7': True}]
(Background on this error at: https://sqlalche.me/e/20/gkpj)

Fix scenario.json (edit it in place), then reply with a short summary of what you changed.