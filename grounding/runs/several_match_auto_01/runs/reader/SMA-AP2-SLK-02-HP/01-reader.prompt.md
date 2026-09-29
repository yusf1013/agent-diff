You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Slack workspace:

    "Invite Aisha Khan to every channel with 'incident' in its name, whose Topic mentions postmortems, and that hasn't been archived yet."

The user is Agent Bot. Below is every Slack channel in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "C_INCRESP",
  "channel_id": "C_INCRESP",
  "channel_name": "incident-response",
  "topic_text": "Postmortems and outage retros for live incidents",
  "purpose_text": "Coordinate incident response",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "incident-response",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00"
 },
 {
  "id": "C_INCRESP_ARCH",
  "channel_id": "C_INCRESP_ARCH",
  "channel_name": "incident-response-archive",
  "topic_text": "Postmortems and outage retros for closed incidents",
  "purpose_text": "Archive of past incident retros",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": true,
  "channel": "incident-response-archive",
  "private": false,
  "archived": true,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00"
 },
 {
  "id": "C_INCCOMMS",
  "channel_id": "C_INCCOMMS",
  "channel_name": "incident-comms",
  "topic_text": "Live incident chatter and status updates",
  "purpose_text": "Coordinate postmortems and retro scheduling",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "incident-comms",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00"
 },
 {
  "id": "C_POSTMORTEMS",
  "channel_id": "C_POSTMORTEMS",
  "channel_name": "postmortems-hub",
  "topic_text": "Incident retros and postmortems recap channel",
  "purpose_text": "Central hub for postmortem write-ups",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "postmortems-hub",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00"
 },
 {
  "id": "C_ENG",
  "channel_id": "C_ENG",
  "channel_name": "engineering",
  "topic_text": "Roadmap planning and architecture discussions",
  "purpose_text": "Engineering team home",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "engineering",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00"
 },
 {
  "id": "C_OLDINC",
  "channel_id": "C_OLDINC",
  "channel_name": "incident-2019-retro",
  "topic_text": "Archived project artifacts",
  "purpose_text": "N/A",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": true,
  "channel": "incident-2019-retro",
  "private": false,
  "archived": true,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00"
 },
 {
  "id": "C_INCRESP-sm200",
  "channel_id": "C_INCRESP-sm200",
  "channel_name": "incident-review",
  "topic_text": "Postmortems and outage retros for live incidents",
  "purpose_text": "Coordinate incident response",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "incident-review",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00"
 },
 {
  "id": "C_INCRESP-sm201",
  "channel_id": "C_INCRESP-sm201",
  "channel_name": "incident-followup",
  "topic_text": "Postmortems and outage retros for live incidents",
  "purpose_text": "Coordinate incident response",
  "is_private": true,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "incident-followup",
  "private": true,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00"
 }
]
