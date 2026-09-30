The replica pre-checks found these problems:
- Replica install or read failed: IntegrityError: (psycopg2.errors.UniqueViolation) duplicate key value violates unique constraint "calendar_acl_rules_pkey"
DETAIL:  Key (id)=(user:jordan.lee@northwind.example) already exists.

[SQL: INSERT INTO "calendar_campaign_04d1b19a85c74ab2b9dbbbab54d7a9c1"."calendar_acl_rules" ("id", "calendar_id", "role", "scope_type", "scope_value", "etag", "deleted", "created_at", "updated_at") VALUES (%(id)s, %(calendar_id)s, %(role)s, %(scope_type)s, %(scope_value)s, %(etag)s, %(deleted)s, %(created_at)s, %(updated_at)s)]
[parameters: {'id': 'user:jordan.lee@northwind.example', 'calendar_id': 'berlin-trip-family@northwind.example', 'role': 'owner', 'scope_type': 'user', 'scope_value': 'jordan.lee@northwind.example', 'etag': '"etag_user:jordan.lee@northwind.example"', 'deleted': False, 'created_at': '2018-01-0

Fix scenario.json (edit it in place), then reply with a short summary of what you changed.