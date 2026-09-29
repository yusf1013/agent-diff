You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Linear workspace:

    "Set the priority to Urgent on all the issues where Priya commented about the API timeout, in a comment thread posted on September 22 that Leo has already resolved."

The user is Jordan Lee. Below is every Linear issue in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "i-web-20",
  "identifier": "WEB-1",
  "title": "Improve payment retry queue",
  "teamId": "t-web",
  "stateId": "t-web-st-2",
  "assigneeId": "u-sam (Sam Rivera)",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 3.0,
  "priorityLabel": "Medium",
  "number": 1.0,
  "createdAt": "2026-09-01T09:00:00",
  "updatedAt": "2026-09-01T09:00:00",
  "team": "Web",
  "state": "In Progress",
  "comments": [
   {
    "id": "c-target",
    "issueId": "i-web-20",
    "userId": "u-priya",
    "body": "We keep seeing an API timeout during retries; let's add exponential backoff.",
    "bodyData": "{\"type\": \"doc\", \"content\": [{\"type\": \"paragraph\", \"content\": [{\"type\": \"text\", \"text\": \"We keep seeing an API timeout during retries; let's add exponential backoff.\"}]}]}",
    "resolvingUserId": "u-leo",
    "resolvedAt": "2026-09-22T15:00:00",
    "createdAt": "2026-09-22T10:00:00",
    "updatedAt": "2026-09-22T10:00:00",
    "users": [
     {
      "id": "u-priya",
      "email": "priya.nair@northwind.example",
      "name": "Priya Nair",
      "displayName": "priya",
      "active": true,
      "admin": false,
      "app": false,
      "avatarBackgroundColor": "#3B82F6",
      "canAccessAnyPublicTeam": true,
      "createdAt": "2025-01-01T00:00:00",
      "updatedAt": "2025-01-01T00:00:00",
      "createdIssueCount": 0,
      "guest": false,
      "initials": "PN",
      "inviteHash": "inv-priya",
      "isAssignable": true,
      "isMe": false,
      "isMentionable": true,
      "lastSeen": "2025-01-01T00:00:00",
      "timezone": "America/Los_Angeles"
     }
    ]
   },
   {
    "id": "c-chatter",
    "issueId": "i-web-20",
    "userId": "u-dana",
    "body": "Nice catch, thanks for flagging.",
    "bodyData": "{\"type\": \"doc\", \"content\": [{\"type\": \"paragraph\", \"content\": [{\"type\": \"text\", \"text\": \"Nice catch, thanks for flagging.\"}]}]}",
    "createdAt": "2026-09-23T09:00:00",
    "updatedAt": "2026-09-23T09:00:00",
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
   }
  ]
 },
 {
  "id": "i-web-21",
  "identifier": "WEB-2",
  "title": "Investigate flaky checkout tests",
  "teamId": "t-web",
  "stateId": "t-web-st-1",
  "assigneeId": "u-leo (Leo Park)",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 2.0,
  "priorityLabel": "High",
  "number": 2.0,
  "createdAt": "2026-09-01T09:00:00",
  "updatedAt": "2026-09-01T09:00:00",
  "team": "Web",
  "state": "Todo",
  "comments": [
   {
    "id": "c-split-author",
    "issueId": "i-web-21",
    "userId": "u-priya",
    "body": "Can we rename this ticket to reflect the current scope?",
    "bodyData": "{\"type\": \"doc\", \"content\": [{\"type\": \"paragraph\", \"content\": [{\"type\": \"text\", \"text\": \"Can we rename this ticket to reflect the current scope?\"}]}]}",
    "createdAt": "2026-09-22T09:00:00",
    "updatedAt": "2026-09-22T09:00:00",
    "users": [
     {
      "id": "u-priya",
      "email": "priya.nair@northwind.example",
      "name": "Priya Nair",
      "displayName": "priya",
      "active": true,
      "admin": false,
      "app": false,
      "avatarBackgroundColor": "#3B82F6",
      "canAccessAnyPublicTeam": true,
      "createdAt": "2025-01-01T00:00:00",
      "updatedAt": "2025-01-01T00:00:00",
      "createdIssueCount": 0,
      "guest": false,
      "initials": "PN",
      "inviteHash": "inv-priya",
      "isAssignable": true,
      "isMe": false,
      "isMentionable": true,
      "lastSeen": "2025-01-01T00:00:00",
      "timezone": "America/Los_Angeles"
     }
    ]
   },
   {
    "id": "c-split-topic",
    "issueId": "i-web-21",
    "userId": "u-leo",
    "body": "Seeing the same API timeout in the staging logs too.",
    "bodyData": "{\"type\": \"doc\", \"content\": [{\"type\": \"paragraph\", \"content\": [{\"type\": \"text\", \"text\": \"Seeing the same API timeout in the staging logs too.\"}]}]}",
    "resolvingUserId": "u-leo",
    "resolvedAt": "2026-09-22T16:00:00",
    "createdAt": "2026-09-22T11:00:00",
    "updatedAt": "2026-09-22T11:00:00",
    "users": [
     {
      "id": "u-leo",
      "email": "leo.park@northwind.example",
      "name": "Leo Park",
      "displayName": "leo",
      "active": true,
      "admin": false,
      "app": false,
      "avatarBackgroundColor": "#3B82F6",
      "canAccessAnyPublicTeam": true,
      "createdAt": "2025-01-01T00:00:00",
      "updatedAt": "2025-01-01T00:00:00",
      "createdIssueCount": 0,
      "guest": false,
      "initials": "LP",
      "inviteHash": "inv-leo",
      "isAssignable": true,
      "isMe": false,
      "isMentionable": true,
      "lastSeen": "2025-01-01T00:00:00",
      "timezone": "America/Los_Angeles"
     }
    ]
   }
  ]
 },
 {
  "id": "i-web-22",
  "identifier": "WEB-3",
  "title": "Reduce webhook latency",
  "teamId": "t-web",
  "stateId": "t-web-st-1",
  "assigneeId": "u-maya (Maya Chen)",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 2.0,
  "priorityLabel": "High",
  "number": 3.0,
  "createdAt": "2026-09-01T09:00:00",
  "updatedAt": "2026-09-01T09:00:00",
  "team": "Web",
  "state": "Todo",
  "comments": [
   {
    "id": "c-f7",
    "issueId": "i-web-22",
    "userId": "u-priya",
    "body": "The API timeout happens whenever latency spikes above 2 seconds.",
    "bodyData": "{\"type\": \"doc\", \"content\": [{\"type\": \"paragraph\", \"content\": [{\"type\": \"text\", \"text\": \"The API timeout happens whenever latency spikes above 2 seconds.\"}]}]}",
    "resolvingUserId": "u-leo",
    "resolvedAt": "2026-09-21T14:00:00",
    "createdAt": "2026-09-21T10:00:00",
    "updatedAt": "2026-09-21T10:00:00",
    "users": [
     {
      "id": "u-priya",
      "email": "priya.nair@northwind.example",
      "name": "Priya Nair",
      "displayName": "priya",
      "active": true,
      "admin": false,
      "app": false,
      "avatarBackgroundColor": "#3B82F6",
      "canAccessAnyPublicTeam": true,
      "createdAt": "2025-01-01T00:00:00",
      "updatedAt": "2025-01-01T00:00:00",
      "createdIssueCount": 0,
      "guest": false,
      "initials": "PN",
      "inviteHash": "inv-priya",
      "isAssignable": true,
      "isMe": false,
      "isMentionable": true,
      "lastSeen": "2025-01-01T00:00:00",
      "timezone": "America/Los_Angeles"
     }
    ]
   }
  ]
 },
 {
  "id": "i-web-23",
  "identifier": "WEB-4",
  "title": "Fix webhook signature verification",
  "teamId": "t-web",
  "stateId": "t-web-st-1",
  "assigneeId": "u-dana (Dana Whitfield)",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 2.0,
  "priorityLabel": "High",
  "number": 4.0,
  "createdAt": "2026-09-01T09:00:00",
  "updatedAt": "2026-09-01T09:00:00",
  "team": "Web",
  "state": "Todo",
  "comments": [
   {
    "id": "c-f1",
    "issueId": "i-web-23",
    "userId": "u-priya",
    "body": "This API timeout also shows up on the staging webhook endpoint.",
    "bodyData": "{\"type\": \"doc\", \"content\": [{\"type\": \"paragraph\", \"content\": [{\"type\": \"text\", \"text\": \"This API timeout also shows up on the staging webhook endpoint.\"}]}]}",
    "resolvingUserId": "u-leo",
    "resolvedAt": "2026-09-22T09:30:00",
    "createdAt": "2026-09-20T09:00:00",
    "updatedAt": "2026-09-20T09:00:00",
    "users": [
     {
      "id": "u-priya",
      "email": "priya.nair@northwind.example",
      "name": "Priya Nair",
      "displayName": "priya",
      "active": true,
      "admin": false,
      "app": false,
      "avatarBackgroundColor": "#3B82F6",
      "canAccessAnyPublicTeam": true,
      "createdAt": "2025-01-01T00:00:00",
      "updatedAt": "2025-01-01T00:00:00",
      "createdIssueCount": 0,
      "guest": false,
      "initials": "PN",
      "inviteHash": "inv-priya",
      "isAssignable": true,
      "isMe": false,
      "isMentionable": true,
      "lastSeen": "2025-01-01T00:00:00",
      "timezone": "America/Los_Angeles"
     }
    ]
   }
  ]
 },
 {
  "id": "i-web-24",
  "identifier": "WEB-5",
  "title": "Optimize database queries for reports",
  "teamId": "t-web",
  "stateId": "t-web-st-1",
  "assigneeId": "u-omar (Omar Haddad)",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 2.0,
  "priorityLabel": "High",
  "number": 5.0,
  "createdAt": "2026-09-01T09:00:00",
  "updatedAt": "2026-09-01T09:00:00",
  "team": "Web",
  "state": "Todo",
  "comments": [
   {
    "id": "c-f0",
    "issueId": "i-web-24",
    "userId": "u-priya",
    "body": "There's an API timeout when exporting large reports.",
    "bodyData": "{\"type\": \"doc\", \"content\": [{\"type\": \"paragraph\", \"content\": [{\"type\": \"text\", \"text\": \"There's an API timeout when exporting large reports.\"}]}]}",
    "createdAt": "2026-09-22T08:00:00",
    "updatedAt": "2026-09-22T08:00:00",
    "users": [
     {
      "id": "u-priya",
      "email": "priya.nair@northwind.example",
      "name": "Priya Nair",
      "displayName": "priya",
      "active": true,
      "admin": false,
      "app": false,
      "avatarBackgroundColor": "#3B82F6",
      "canAccessAnyPublicTeam": true,
      "createdAt": "2025-01-01T00:00:00",
      "updatedAt": "2025-01-01T00:00:00",
      "createdIssueCount": 0,
      "guest": false,
      "initials": "PN",
      "inviteHash": "inv-priya",
      "isAssignable": true,
      "isMe": false,
      "isMentionable": true,
      "lastSeen": "2025-01-01T00:00:00",
      "timezone": "America/Los_Angeles"
     }
    ]
   }
  ]
 },
 {
  "id": "i-web-25",
  "identifier": "WEB-6",
  "title": "Update onboarding email copy",
  "teamId": "t-web",
  "stateId": "t-web-st-1",
  "assigneeId": "u-sam (Sam Rivera)",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 1.0,
  "priorityLabel": "Urgent",
  "number": 6.0,
  "createdAt": "2026-09-01T09:00:00",
  "updatedAt": "2026-09-01T09:00:00",
  "team": "Web",
  "state": "Todo",
  "comments": [
   {
    "id": "c-bg",
    "issueId": "i-web-25",
    "userId": "u-sam",
    "body": "Let's tweak the subject line for clarity.",
    "bodyData": "{\"type\": \"doc\", \"content\": [{\"type\": \"paragraph\", \"content\": [{\"type\": \"text\", \"text\": \"Let's tweak the subject line for clarity.\"}]}]}",
    "resolvingUserId": "u-leo",
    "resolvedAt": "2026-09-15T12:00:00",
    "createdAt": "2026-09-15T09:00:00",
    "updatedAt": "2026-09-15T09:00:00",
    "users": [
     {
      "id": "u-sam",
      "email": "sam.rivera@northwind.example",
      "name": "Sam Rivera",
      "displayName": "sam",
      "active": true,
      "admin": false,
      "app": false,
      "avatarBackgroundColor": "#3B82F6",
      "canAccessAnyPublicTeam": true,
      "createdAt": "2025-01-01T00:00:00",
      "updatedAt": "2025-01-01T00:00:00",
      "createdIssueCount": 0,
      "guest": false,
      "initials": "SR",
      "inviteHash": "inv-sam",
      "isAssignable": true,
      "isMe": false,
      "isMentionable": true,
      "lastSeen": "2025-01-01T00:00:00",
      "timezone": "America/Los_Angeles"
     }
    ]
   }
  ]
 },
 {
  "id": "i-web-20-sm0-v",
  "identifier": "WEB-7",
  "title": "Fix checkout latency spikes",
  "teamId": "t-web",
  "stateId": "t-web-st-2",
  "assigneeId": "u-sam (Sam Rivera)",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 3.0,
  "priorityLabel": "Medium",
  "number": 7.0,
  "createdAt": "2026-09-01T09:00:00",
  "updatedAt": "2026-09-01T09:00:00",
  "team": "Web",
  "state": "In Progress",
  "comments": [
   {
    "id": "c-target-sm645",
    "issueId": "i-web-20-sm0-v",
    "userId": "u-priya",
    "body": "We keep seeing an API timeout during retries; let's add exponential backoff.",
    "bodyData": "{\"type\": \"doc\", \"content\": [{\"type\": \"paragraph\", \"content\": [{\"type\": \"text\", \"text\": \"We keep seeing an API timeout during retries; let's add exponential backoff.\"}]}]}",
    "resolvingUserId": "u-leo",
    "resolvedAt": "2026-09-22T15:00:00",
    "createdAt": "2026-09-22T10:00:00",
    "updatedAt": "2026-09-22T10:00:00",
    "users": [
     {
      "id": "u-priya",
      "email": "priya.nair@northwind.example",
      "name": "Priya Nair",
      "displayName": "priya",
      "active": true,
      "admin": false,
      "app": false,
      "avatarBackgroundColor": "#3B82F6",
      "canAccessAnyPublicTeam": true,
      "createdAt": "2025-01-01T00:00:00",
      "updatedAt": "2025-01-01T00:00:00",
      "createdIssueCount": 0,
      "guest": false,
      "initials": "PN",
      "inviteHash": "inv-priya",
      "isAssignable": true,
      "isMe": false,
      "isMentionable": true,
      "lastSeen": "2025-01-01T00:00:00",
      "timezone": "America/Los_Angeles"
     }
    ]
   },
   {
    "id": "c-chatter-sm645",
    "issueId": "i-web-20-sm0-v",
    "userId": "u-dana",
    "body": "Nice catch, thanks for flagging.",
    "bodyData": "{\"type\": \"doc\", \"content\": [{\"type\": \"paragraph\", \"content\": [{\"type\": \"text\", \"text\": \"Nice catch, thanks for flagging.\"}]}]}",
    "createdAt": "2026-09-23T09:00:00",
    "updatedAt": "2026-09-23T09:00:00",
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
   }
  ]
 },
 {
  "id": "i-web-20-sm1-v",
  "identifier": "WEB-8",
  "title": "Stabilize refund webhook queue",
  "teamId": "t-web",
  "stateId": "t-web-st-2",
  "assigneeId": "u-sam (Sam Rivera)",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 3.0,
  "priorityLabel": "Medium",
  "number": 8.0,
  "createdAt": "2026-09-01T09:00:00",
  "updatedAt": "2026-09-01T09:00:00",
  "team": "Web",
  "state": "In Progress",
  "comments": [
   {
    "id": "c-target-sm646",
    "issueId": "i-web-20-sm1-v",
    "userId": "u-priya",
    "body": "We keep seeing an API timeout during retries; let's add exponential backoff.",
    "bodyData": "{\"type\": \"doc\", \"content\": [{\"type\": \"paragraph\", \"content\": [{\"type\": \"text\", \"text\": \"We keep seeing an API timeout during retries; let's add exponential backoff.\"}]}]}",
    "resolvingUserId": "u-leo",
    "resolvedAt": "2026-09-22T15:00:00",
    "createdAt": "2026-09-22T10:00:00",
    "updatedAt": "2026-09-22T10:00:00",
    "users": [
     {
      "id": "u-priya",
      "email": "priya.nair@northwind.example",
      "name": "Priya Nair",
      "displayName": "priya",
      "active": true,
      "admin": false,
      "app": false,
      "avatarBackgroundColor": "#3B82F6",
      "canAccessAnyPublicTeam": true,
      "createdAt": "2025-01-01T00:00:00",
      "updatedAt": "2025-01-01T00:00:00",
      "createdIssueCount": 0,
      "guest": false,
      "initials": "PN",
      "inviteHash": "inv-priya",
      "isAssignable": true,
      "isMe": false,
      "isMentionable": true,
      "lastSeen": "2025-01-01T00:00:00",
      "timezone": "America/Los_Angeles"
     }
    ]
   },
   {
    "id": "c-chatter-sm646",
    "issueId": "i-web-20-sm1-v",
    "userId": "u-dana",
    "body": "Nice catch, thanks for flagging.",
    "bodyData": "{\"type\": \"doc\", \"content\": [{\"type\": \"paragraph\", \"content\": [{\"type\": \"text\", \"text\": \"Nice catch, thanks for flagging.\"}]}]}",
    "createdAt": "2026-09-23T09:00:00",
    "updatedAt": "2026-09-23T09:00:00",
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
   }
  ]
 }
]
