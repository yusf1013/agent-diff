The replica pre-checks found these problems:
- Replica install or read failed: IntegrityError: (psycopg2.errors.ForeignKeyViolation) insert or update on table "comments" violates foreign key constraint "comments_documentId_fkey"
DETAIL:  Key (documentId)=(doc-content-comment) is not present in table "documents".

[SQL: INSERT INTO "linear_campaign_bc242c5810d64dcd932621b3efb5f793"."comments" ("id", "documentId", "userId", "body", "bodyData", "createdAt", "reactionData", "updatedAt", "url") VALUES (%(id)s, %(documentId)s, %(userId)s, %(body)s, %(bodyData)s, %(createdAt)s, %(reactionData)s, %(updatedAt)s, %(url)s)]
[parameters: {'id': 'c-content-comment', 'documentId': 'doc-content-comment', 'userId': 'u-leo', 'body': 'Great writeup, can we fold the Q3 churn analysis numbers in here too?', 'bodyData': '', 'createdAt': '2026-06-01T09:00:00+00:00', 'reactionData': '{}', 'updatedAt': '20

Fix scenario.json (edit it in place), then reply with a short summary of what you changed.