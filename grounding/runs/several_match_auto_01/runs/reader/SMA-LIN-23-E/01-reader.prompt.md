You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Linear workspace:

    "Reopen all the comment threads on WEB-5 that Maya Chen resolved."

The user is Jordan Lee. Below is every Linear comment in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "c-21",
  "issueId": "i-w5",
  "userId": "u-sam",
  "body": "The retry wrapper hides the real failure.",
  "bodyData": "{\"type\": \"doc\", \"content\": [{\"type\": \"paragraph\", \"content\": [{\"type\": \"text\", \"text\": \"The retry wrapper hides the real failure.\"}]}]}",
  "resolvingUserId": "u-maya",
  "resolvedAt": "2026-06-01T09:00:00",
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "issues": [
   {
    "id": "i-w5",
    "identifier": "WEB-5",
    "title": "Flaky checkout test",
    "teamId": "t-web",
    "stateId": "t-web-st-1",
    "creatorId": "u-actor",
    "priority": 0.0,
    "priorityLabel": "No priority",
    "number": 5.0,
    "createdAt": "2026-06-01T09:00:00",
    "updatedAt": "2026-06-01T09:00:00"
   }
  ],
  "users": [
   {
    "id": "u-maya",
    "email": "maya.chen@northwind.example",
    "name": "Maya Chen",
    "displayName": "maya",
    "active": true,
    "admin": false,
    "app": false,
    "avatarBackgroundColor": "#3B82F6",
    "canAccessAnyPublicTeam": true,
    "createdAt": "2025-01-01T00:00:00",
    "updatedAt": "2025-01-01T00:00:00",
    "createdIssueCount": 0,
    "guest": false,
    "initials": "MC",
    "inviteHash": "inv-maya",
    "isAssignable": true,
    "isMe": false,
    "isMentionable": true,
    "lastSeen": "2025-01-01T00:00:00",
    "timezone": "America/Los_Angeles"
   }
  ]
 },
 {
  "id": "c-22",
  "issueId": "i-w5",
  "userId": "u-maya",
  "body": "Can we pin the browser version?",
  "bodyData": "{\"type\": \"doc\", \"content\": [{\"type\": \"paragraph\", \"content\": [{\"type\": \"text\", \"text\": \"Can we pin the browser version?\"}]}]}",
  "resolvingUserId": "u-dana",
  "resolvedAt": "2026-06-01T09:00:00",
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "issues": [
   {
    "id": "i-w5",
    "identifier": "WEB-5",
    "title": "Flaky checkout test",
    "teamId": "t-web",
    "stateId": "t-web-st-1",
    "creatorId": "u-actor",
    "priority": 0.0,
    "priorityLabel": "No priority",
    "number": 5.0,
    "createdAt": "2026-06-01T09:00:00",
    "updatedAt": "2026-06-01T09:00:00"
   }
  ],
  "users": [
   {
    "id": "u-dana",
    "email": "dana.whitfield@northwind.example",
    "name": "Dana Whitfield",
    "displayName": "dana",
    "active": true,
    "admin": false,
    "app": false,
    "avatarBackgroundColor": "#3B82F6",
    "canAccessAnyPublicTeam": true,
    "createdAt": "2025-01-01T00:00:00",
    "updatedAt": "2025-01-01T00:00:00",
    "createdIssueCount": 0,
    "guest": false,
    "initials": "DW",
    "inviteHash": "inv-dana",
    "isAssignable": true,
    "isMe": false,
    "isMentionable": true,
    "lastSeen": "2025-01-01T00:00:00",
    "timezone": "America/Los_Angeles"
   }
  ]
 },
 {
  "id": "c-25",
  "issueId": "i-w5",
  "userId": "u-sam",
  "body": "Timeouts are too short on CI.",
  "bodyData": "{\"type\": \"doc\", \"content\": [{\"type\": \"paragraph\", \"content\": [{\"type\": \"text\", \"text\": \"Timeouts are too short on CI.\"}]}]}",
  "resolvingUserId": "u-dana",
  "resolvedAt": "2026-06-01T09:00:00",
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "issues": [
   {
    "id": "i-w5",
    "identifier": "WEB-5",
    "title": "Flaky checkout test",
    "teamId": "t-web",
    "stateId": "t-web-st-1",
    "creatorId": "u-actor",
    "priority": 0.0,
    "priorityLabel": "No priority",
    "number": 5.0,
    "createdAt": "2026-06-01T09:00:00",
    "updatedAt": "2026-06-01T09:00:00"
   }
  ],
  "users": [
   {
    "id": "u-dana",
    "email": "dana.whitfield@northwind.example",
    "name": "Dana Whitfield",
    "displayName": "dana",
    "active": true,
    "admin": false,
    "app": false,
    "avatarBackgroundColor": "#3B82F6",
    "canAccessAnyPublicTeam": true,
    "createdAt": "2025-01-01T00:00:00",
    "updatedAt": "2025-01-01T00:00:00",
    "createdIssueCount": 0,
    "guest": false,
    "initials": "DW",
    "inviteHash": "inv-dana",
    "isAssignable": true,
    "isMe": false,
    "isMentionable": true,
    "lastSeen": "2025-01-01T00:00:00",
    "timezone": "America/Los_Angeles"
   }
  ]
 },
 {
  "id": "c-21-sm111",
  "issueId": "i-w5",
  "userId": "u-sam",
  "body": "The cache layer masks the real error.",
  "bodyData": "{\"type\": \"doc\", \"content\": [{\"type\": \"paragraph\", \"content\": [{\"type\": \"text\", \"text\": \"The retry wrapper hides the real failure.\"}]}]}",
  "resolvingUserId": "u-maya",
  "resolvedAt": "2026-06-01T09:00:00",
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "issues": [
   {
    "id": "i-w5",
    "identifier": "WEB-5",
    "title": "Flaky checkout test",
    "teamId": "t-web",
    "stateId": "t-web-st-1",
    "creatorId": "u-actor",
    "priority": 0.0,
    "priorityLabel": "No priority",
    "number": 5.0,
    "createdAt": "2026-06-01T09:00:00",
    "updatedAt": "2026-06-01T09:00:00"
   }
  ],
  "users": [
   {
    "id": "u-maya",
    "email": "maya.chen@northwind.example",
    "name": "Maya Chen",
    "displayName": "maya",
    "active": true,
    "admin": false,
    "app": false,
    "avatarBackgroundColor": "#3B82F6",
    "canAccessAnyPublicTeam": true,
    "createdAt": "2025-01-01T00:00:00",
    "updatedAt": "2025-01-01T00:00:00",
    "createdIssueCount": 0,
    "guest": false,
    "initials": "MC",
    "inviteHash": "inv-maya",
    "isAssignable": true,
    "isMe": false,
    "isMentionable": true,
    "lastSeen": "2025-01-01T00:00:00",
    "timezone": "America/Los_Angeles"
   }
  ]
 },
 {
  "id": "c-21-sm112",
  "issueId": "i-w5",
  "userId": "u-sam",
  "body": "The helper function swallows the actual exception.",
  "bodyData": "{\"type\": \"doc\", \"content\": [{\"type\": \"paragraph\", \"content\": [{\"type\": \"text\", \"text\": \"The retry wrapper hides the real failure.\"}]}]}",
  "resolvingUserId": "u-maya",
  "resolvedAt": "2026-06-01T09:00:00",
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "issues": [
   {
    "id": "i-w5",
    "identifier": "WEB-5",
    "title": "Flaky checkout test",
    "teamId": "t-web",
    "stateId": "t-web-st-1",
    "creatorId": "u-actor",
    "priority": 0.0,
    "priorityLabel": "No priority",
    "number": 5.0,
    "createdAt": "2026-06-01T09:00:00",
    "updatedAt": "2026-06-01T09:00:00"
   }
  ],
  "users": [
   {
    "id": "u-maya",
    "email": "maya.chen@northwind.example",
    "name": "Maya Chen",
    "displayName": "maya",
    "active": true,
    "admin": false,
    "app": false,
    "avatarBackgroundColor": "#3B82F6",
    "canAccessAnyPublicTeam": true,
    "createdAt": "2025-01-01T00:00:00",
    "updatedAt": "2025-01-01T00:00:00",
    "createdIssueCount": 0,
    "guest": false,
    "initials": "MC",
    "inviteHash": "inv-maya",
    "isAssignable": true,
    "isMe": false,
    "isMentionable": true,
    "lastSeen": "2025-01-01T00:00:00",
    "timezone": "America/Los_Angeles"
   }
  ]
 }
]
