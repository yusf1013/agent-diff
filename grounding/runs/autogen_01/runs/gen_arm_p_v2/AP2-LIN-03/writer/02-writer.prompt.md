The replica pre-checks found these problems:
- Replica install or read failed: IntegrityError: (psycopg2.errors.UniqueViolation) duplicate key value violates unique constraint "uq_team_org_key"
DETAIL:  Key ("organizationId", key)=(org-northwind, GRW) already exists.

[SQL: INSERT INTO "linear_campaign_0278a4b5852b4d36af128e1568615a00"."teams" ("id", "name", "key", "displayName", "organizationId", "description", "color", "createdAt", "updatedAt", "aiThreadSummariesEnabled", "autoArchivePeriod", "currentProgress", "cycleCalenderUrl", "cycleCooldownTime", "cycleDuration", "cycleIssueAutoAssignCompleted", "cycleIssueAutoAssignStarted", "cycleLockToActive", "cycleStartDay", "cyclesEnabled", "defaultIssueEstimate", "groupIssueHistory", "icon", "inheritIssueEstimation", "inheritWorkflowStatuses", "inviteHash", "issueCount", "issueEstimationAllowZero", "issueEstimationExtended", "issueEsti

Fix scenario.json (edit it in place), then reply with a short summary of what you changed.