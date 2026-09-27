The replica pre-checks found these problems:
- Replica install or read failed: IntegrityError: (psycopg2.errors.ForeignKeyViolation) insert or update on table "comments" violates foreign key constraint "comments_documentId_fkey"
DETAIL:  Key (documentId)=(d-content-f2) is not present in table "documents".

[SQL: INSERT INTO "linear_campaign_bf6867f61f144a6cbf9885d05c7149f9"."comments" ("id", "documentId", "userId", "body", "createdAt", "bodyData", "reactionData", "updatedAt", "url") VALUES (%(id)s, %(documentId)s, %(userId)s, %(body)s, %(createdAt)s, %(bodyData)s, %(reactionData)s, %(updatedAt)s, %(url)s)]
[parameters: {'id': 'cm-referral-mention', 'documentId': 'd-content-f2', 'userId': 'u-leo', 'body': "Let's make sure this also covers the referral program pilot.", 'createdAt': '2026-06-02T10:00:00', 'bodyData': '', 'reactionData': '{}', 'updatedAt': '2026-06-01T09:00:00+00:00', '

Fix scenario.json (edit it in place), then reply with a short summary of what you changed.