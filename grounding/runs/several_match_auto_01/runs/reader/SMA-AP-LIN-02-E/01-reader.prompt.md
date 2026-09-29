You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Linear workspace:

    "Bump the priority of all the security review tickets assigned to Priya Chen, our guest reviewer from vendorworks.example, to Urgent."

The user is Jordan Lee. Below is every Linear issue in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "i-sec-payments",
  "identifier": "GRC-1",
  "title": "Security review: Payments API",
  "teamId": "t-grc",
  "stateId": "t-grc-st-1",
  "assigneeId": "u-priya_guest (Priya Chen)",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 3.0,
  "priorityLabel": "Medium",
  "number": 1.0,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "team": "Governance & Compliance",
  "state": "Todo",
  "users": [
   {
    "id": "u-priya_guest",
    "email": "priya.chen@vendorworks.example",
    "name": "Priya Chen",
    "displayName": "priya",
    "active": true,
    "admin": false,
    "app": false,
    "avatarBackgroundColor": "#3B82F6",
    "canAccessAnyPublicTeam": true,
    "createdAt": "2025-01-01T00:00:00",
    "updatedAt": "2025-01-01T00:00:00",
    "createdIssueCount": 0,
    "guest": true,
    "initials": "PC",
    "inviteHash": "inv-priya_guest",
    "isAssignable": true,
    "isMe": false,
    "isMentionable": true,
    "lastSeen": "2025-01-01T00:00:00",
    "timezone": "America/Los_Angeles"
   }
  ]
 },
 {
  "id": "i-sec-admin",
  "identifier": "GRC-2",
  "title": "Security review: Admin console",
  "teamId": "t-grc",
  "stateId": "t-grc-st-1",
  "assigneeId": "u-priya_employee (Priya Chen)",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 3.0,
  "priorityLabel": "Medium",
  "number": 2.0,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "team": "Governance & Compliance",
  "state": "Todo",
  "users": [
   {
    "id": "u-priya_employee",
    "email": "p.chen@vendorworks.example",
    "name": "Priya Chen",
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
    "initials": "PC",
    "inviteHash": "inv-priya_employee",
    "isAssignable": true,
    "isMe": false,
    "isMentionable": true,
    "lastSeen": "2025-01-01T00:00:00",
    "timezone": "America/Los_Angeles"
   }
  ]
 },
 {
  "id": "i-sec-mobile",
  "identifier": "GRC-3",
  "title": "Security review: Mobile app",
  "teamId": "t-grc",
  "stateId": "t-grc-st-1",
  "assigneeId": "u-priyanka_guest (Priyanka Chen)",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 3.0,
  "priorityLabel": "Medium",
  "number": 3.0,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "team": "Governance & Compliance",
  "state": "Todo",
  "users": [
   {
    "id": "u-priyanka_guest",
    "email": "priyanka.chen@vendorworks.example",
    "name": "Priyanka Chen",
    "displayName": "priyanka",
    "active": true,
    "admin": false,
    "app": false,
    "avatarBackgroundColor": "#3B82F6",
    "canAccessAnyPublicTeam": true,
    "createdAt": "2025-01-01T00:00:00",
    "updatedAt": "2025-01-01T00:00:00",
    "createdIssueCount": 0,
    "guest": true,
    "initials": "PC",
    "inviteHash": "inv-priyanka_guest",
    "isAssignable": true,
    "isMe": false,
    "isMentionable": true,
    "lastSeen": "2025-01-01T00:00:00",
    "timezone": "America/Los_Angeles"
   }
  ]
 },
 {
  "id": "i-sec-billing",
  "identifier": "GRC-4",
  "title": "Security review: Billing service",
  "teamId": "t-grc",
  "stateId": "t-grc-st-1",
  "assigneeId": "u-priya_vendorstaff (Priya Chen)",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 3.0,
  "priorityLabel": "Medium",
  "number": 4.0,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "team": "Governance & Compliance",
  "state": "Todo",
  "users": [
   {
    "id": "u-priya_vendorstaff",
    "email": "priya.chen@vendorstaff.example",
    "name": "Priya Chen",
    "displayName": "priya",
    "active": true,
    "admin": false,
    "app": false,
    "avatarBackgroundColor": "#3B82F6",
    "canAccessAnyPublicTeam": true,
    "createdAt": "2025-01-01T00:00:00",
    "updatedAt": "2025-01-01T00:00:00",
    "createdIssueCount": 0,
    "guest": true,
    "initials": "PC",
    "inviteHash": "inv-priya_vendorstaff",
    "isAssignable": true,
    "isMe": false,
    "isMentionable": true,
    "lastSeen": "2025-01-01T00:00:00",
    "timezone": "America/Los_Angeles"
   }
  ]
 },
 {
  "id": "i-sec-network",
  "identifier": "GRC-5",
  "title": "Security review: Network access",
  "teamId": "t-grc",
  "stateId": "t-grc-st-1",
  "assigneeId": "u-dana (Dana Whitfield)",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 2.0,
  "priorityLabel": "High",
  "number": 5.0,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "team": "Governance & Compliance",
  "state": "Todo",
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
  "id": "i-okr",
  "identifier": "GRC-6",
  "title": "Quarterly OKR review",
  "teamId": "t-grc",
  "stateId": "t-grc-st-1",
  "assigneeId": "u-leo (Leo Park)",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 2.0,
  "priorityLabel": "High",
  "number": 6.0,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "team": "Governance & Compliance",
  "state": "Todo",
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
 },
 {
  "id": "i-sec-payments-sm0-v",
  "identifier": "GRC-7",
  "title": "Security review: Auth service",
  "teamId": "t-grc",
  "stateId": "t-grc-st-1",
  "assigneeId": "u-priya_guest (Priya Chen)",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 3.0,
  "priorityLabel": "Medium",
  "number": 7.0,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "team": "Governance & Compliance",
  "state": "Todo",
  "users": [
   {
    "id": "u-priya_guest",
    "email": "priya.chen@vendorworks.example",
    "name": "Priya Chen",
    "displayName": "priya",
    "active": true,
    "admin": false,
    "app": false,
    "avatarBackgroundColor": "#3B82F6",
    "canAccessAnyPublicTeam": true,
    "createdAt": "2025-01-01T00:00:00",
    "updatedAt": "2025-01-01T00:00:00",
    "createdIssueCount": 0,
    "guest": true,
    "initials": "PC",
    "inviteHash": "inv-priya_guest",
    "isAssignable": true,
    "isMe": false,
    "isMentionable": true,
    "lastSeen": "2025-01-01T00:00:00",
    "timezone": "America/Los_Angeles"
   }
  ]
 },
 {
  "id": "i-sec-payments-sm1-v",
  "identifier": "GRC-8",
  "title": "Security review: Checkout flow",
  "teamId": "t-grc",
  "stateId": "t-grc-st-1",
  "assigneeId": "u-priya_guest (Priya Chen)",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 3.0,
  "priorityLabel": "Medium",
  "number": 8.0,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "team": "Governance & Compliance",
  "state": "Todo",
  "users": [
   {
    "id": "u-priya_guest",
    "email": "priya.chen@vendorworks.example",
    "name": "Priya Chen",
    "displayName": "priya",
    "active": true,
    "admin": false,
    "app": false,
    "avatarBackgroundColor": "#3B82F6",
    "canAccessAnyPublicTeam": true,
    "createdAt": "2025-01-01T00:00:00",
    "updatedAt": "2025-01-01T00:00:00",
    "createdIssueCount": 0,
    "guest": true,
    "initials": "PC",
    "inviteHash": "inv-priya_guest",
    "isAssignable": true,
    "isMe": false,
    "isMentionable": true,
    "lastSeen": "2025-01-01T00:00:00",
    "timezone": "America/Los_Angeles"
   }
  ]
 }
]
