You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Linear workspace:

    "Set the description of all the high-priority at-risk projects with the Meridian milestone due December 2, 2026 to 'Pivoting to usage-based pricing'."

The user is Jordan Lee. Below is every Linear project in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "p-atlas",
  "name": "Atlas",
  "description": "Mobile checkout revamp",
  "creatorId": "u-actor (Jordan Lee)",
  "state": "started",
  "priority": 2.0,
  "priorityLabel": "High",
  "color": "#5e6ad2",
  "slugId": "p-atlas",
  "progress": 0.0,
  "scope": 0.0,
  "frequencyResolution": "weekly",
  "slackIssueComments": false,
  "slackIssueStatuses": false,
  "slackNewIssue": false,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "health": "atRisk",
  "project_milestones": [
   {
    "id": "m-ms1",
    "projectId": "p-atlas",
    "name": "Meridian",
    "targetDate": "2026-12-02",
    "status": "unstarted",
    "progress": 0.0,
    "createdAt": "2026-06-01T09:00:00",
    "updatedAt": "2026-06-01T09:00:00"
   }
  ]
 },
 {
  "id": "p-beacon",
  "name": "Beacon Refresh",
  "description": "Notification preferences",
  "creatorId": "u-actor (Jordan Lee)",
  "state": "started",
  "priority": 2.0,
  "priorityLabel": "High",
  "color": "#5e6ad2",
  "slugId": "p-beacon",
  "progress": 0.0,
  "scope": 0.0,
  "frequencyResolution": "weekly",
  "slackIssueComments": false,
  "slackIssueStatuses": false,
  "slackNewIssue": false,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "health": "atRisk",
  "project_milestones": [
   {
    "id": "m-beacon1",
    "projectId": "p-beacon",
    "name": "Meridian Phase 2",
    "targetDate": "2026-12-02",
    "status": "unstarted",
    "progress": 0.0,
    "createdAt": "2026-06-01T09:00:00",
    "updatedAt": "2026-06-01T09:00:00"
   }
  ]
 },
 {
  "id": "p-harbor",
  "name": "Harbor Mobile",
  "description": "Offline mode",
  "creatorId": "u-actor (Jordan Lee)",
  "state": "started",
  "priority": 2.0,
  "priorityLabel": "High",
  "color": "#5e6ad2",
  "slugId": "p-harbor",
  "progress": 0.0,
  "scope": 0.0,
  "frequencyResolution": "weekly",
  "slackIssueComments": false,
  "slackIssueStatuses": false,
  "slackNewIssue": false,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "health": "atRisk",
  "project_milestones": [
   {
    "id": "m-harbor1",
    "projectId": "p-harbor",
    "name": "Meridian",
    "targetDate": "2027-01-15",
    "status": "unstarted",
    "progress": 0.0,
    "createdAt": "2026-06-01T09:00:00",
    "updatedAt": "2026-06-01T09:00:00"
   },
   {
    "id": "m-harbor2",
    "projectId": "p-harbor",
    "name": "Harbor Launch",
    "targetDate": "2026-12-02",
    "status": "unstarted",
    "progress": 0.0,
    "createdAt": "2026-06-01T09:00:00",
    "updatedAt": "2026-06-01T09:00:00"
   }
  ]
 },
 {
  "id": "p-canyon",
  "name": "Canyon Web",
  "description": "Site search tuning",
  "creatorId": "u-actor (Jordan Lee)",
  "state": "started",
  "priority": 2.0,
  "priorityLabel": "High",
  "color": "#5e6ad2",
  "slugId": "p-canyon",
  "progress": 0.0,
  "scope": 0.0,
  "frequencyResolution": "weekly",
  "slackIssueComments": false,
  "slackIssueStatuses": false,
  "slackNewIssue": false,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "health": "atRisk",
  "project_milestones": [
   {
    "id": "m-canyon1",
    "projectId": "p-canyon",
    "name": "Canyon GA",
    "targetDate": "2026-11-10",
    "status": "unstarted",
    "progress": 0.0,
    "createdAt": "2026-06-01T09:00:00",
    "updatedAt": "2026-06-01T09:00:00"
   }
  ]
 },
 {
  "id": "p-drift",
  "name": "Driftwood",
  "description": "Legacy migration",
  "creatorId": "u-actor (Jordan Lee)",
  "state": "started",
  "priority": 4.0,
  "priorityLabel": "Low",
  "color": "#5e6ad2",
  "slugId": "p-drift",
  "progress": 0.0,
  "scope": 0.0,
  "frequencyResolution": "weekly",
  "slackIssueComments": false,
  "slackIssueStatuses": false,
  "slackNewIssue": false,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "health": "onTrack",
  "project_milestones": [
   {
    "id": "m-drift1",
    "projectId": "p-drift",
    "name": "Driftwood Beta",
    "targetDate": "2026-10-01",
    "status": "unstarted",
    "progress": 0.0,
    "createdAt": "2026-06-01T09:00:00",
    "updatedAt": "2026-06-01T09:00:00"
   }
  ]
 },
 {
  "id": "p-echo",
  "name": "Echo",
  "description": "Help center refresh",
  "creatorId": "u-actor (Jordan Lee)",
  "state": "started",
  "priority": 2.0,
  "priorityLabel": "High",
  "color": "#5e6ad2",
  "slugId": "p-echo",
  "progress": 0.0,
  "scope": 0.0,
  "frequencyResolution": "weekly",
  "slackIssueComments": false,
  "slackIssueStatuses": false,
  "slackNewIssue": false,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "health": "onTrack",
  "project_milestones": [
   {
    "id": "m-echo1",
    "projectId": "p-echo",
    "name": "Meridian",
    "targetDate": "2026-10-05",
    "status": "unstarted",
    "progress": 0.0,
    "createdAt": "2026-06-01T09:00:00",
    "updatedAt": "2026-06-01T09:00:00"
   }
  ]
 },
 {
  "id": "p-atlas-sm743",
  "name": "Beacon",
  "description": "Mobile checkout revamp",
  "creatorId": "u-actor (Jordan Lee)",
  "state": "started",
  "priority": 2.0,
  "priorityLabel": "High",
  "color": "#5e6ad2",
  "slugId": "p-atlas",
  "progress": 0.0,
  "scope": 0.0,
  "frequencyResolution": "weekly",
  "slackIssueComments": false,
  "slackIssueStatuses": false,
  "slackNewIssue": false,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "health": "atRisk",
  "project_milestones": [
   {
    "id": "m-ms1-sm743",
    "projectId": "p-atlas-sm743",
    "name": "Meridian",
    "targetDate": "2026-12-02",
    "status": "unstarted",
    "progress": 0.0,
    "createdAt": "2026-06-01T09:00:00",
    "updatedAt": "2026-06-01T09:00:00"
   }
  ]
 },
 {
  "id": "p-atlas-sm744",
  "name": "Vega",
  "description": "Mobile checkout revamp",
  "creatorId": "u-actor (Jordan Lee)",
  "state": "started",
  "priority": 2.0,
  "priorityLabel": "High",
  "color": "#5e6ad2",
  "slugId": "p-atlas",
  "progress": 0.0,
  "scope": 0.0,
  "frequencyResolution": "weekly",
  "slackIssueComments": false,
  "slackIssueStatuses": false,
  "slackNewIssue": false,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "health": "atRisk",
  "project_milestones": [
   {
    "id": "m-ms1-sm744",
    "projectId": "p-atlas-sm744",
    "name": "Meridian",
    "targetDate": "2026-12-02",
    "status": "unstarted",
    "progress": 0.0,
    "createdAt": "2026-06-01T09:00:00",
    "updatedAt": "2026-06-01T09:00:00"
   }
  ]
 }
]
