You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Slack workspace:

    "Set the topic of every private channel whose purpose is coordinating vendor contracts to "Renewals due Oct 31"."

The user is Agent Bot. Below is every Slack channel in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "C_LEGALOPS",
  "channel_id": "C_LEGALOPS",
  "channel_name": "legal-ops",
  "topic_text": "Contract reviews",
  "purpose_text": "Coordinating vendor contracts and renewals",
  "is_private": true,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "legal-ops",
  "private": true,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00"
 },
 {
  "id": "C_PROC",
  "channel_id": "C_PROC",
  "channel_name": "procurement",
  "topic_text": "Vendor contracts this quarter",
  "purpose_text": "Purchase approvals and budgets",
  "is_private": true,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "procurement",
  "private": true,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00"
 },
 {
  "id": "C_VENDOR",
  "channel_id": "C_VENDOR",
  "channel_name": "vendor-contracts",
  "purpose_text": "Archive of signed agreements",
  "is_private": true,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "vendor-contracts",
  "private": true,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00"
 },
 {
  "id": "C_CONTRACTS",
  "channel_id": "C_CONTRACTS",
  "channel_name": "contracts-team",
  "purpose_text": "Coordinating vendor contracts with legal",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "contracts-team",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00"
 },
 {
  "id": "C_LEGALOPS-sm171",
  "channel_id": "C_LEGALOPS-sm171",
  "channel_name": "vendor-ops",
  "topic_text": "Contract reviews",
  "purpose_text": "Coordinating vendor contracts and renewals",
  "is_private": true,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "vendor-ops",
  "private": true,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00"
 },
 {
  "id": "C_LEGALOPS-sm172",
  "channel_id": "C_LEGALOPS-sm172",
  "channel_name": "legal-deals",
  "topic_text": "Contract reviews",
  "purpose_text": "Coordinating vendor contracts and renewals",
  "is_private": true,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "legal-deals",
  "private": true,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00"
 }
]
