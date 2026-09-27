The replica pre-checks found these problems:
- Replica install or read failed: IntegrityError: (psycopg2.errors.UniqueViolation) duplicate key value violates unique constraint "uq_team_org_key"
DETAIL:  Key ("organizationId", key)=(org-northwind, ENG) already exists.

[SQL: INSERT INTO "linear_campaign_0b6001699a334ba797e894be4d943886"."teams" ("id", "name", "key", "displayName", "organizationId", "description", "color", "createdAt", "updatedAt", "aiThreadSummariesEnabled", "autoArchivePeriod", "currentProgress", "cycleCalenderUrl", "cycleCooldownTime", "cycleDuration", "cycleIssueAutoAssignCompleted", "cycleIssueAutoAssignStarted", "cycleLockToActive", "cycleStartDay", "cyclesEnabled", "defaultIssueEstimate", "groupIssueHistory", "icon", "inheritIssueEstimation", "inheritWorkflowStatuses", "inviteHash", "issueCount", "issueEstimationAllowZero", "issueEstimationExtended", "issueEsti

Fix scenario.json (edit it in place), then reply with a short summary of what you changed.