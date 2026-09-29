You write test requests for an AI assistant that acts in a workspace on a user's behalf. A test request must
read exactly as a real user would write it.

---

The assistant acts in Linear as Jordan Lee, a regular Linear member. Each item below describes something a user might ask for that
the service will not do for this user; `why` says why. For each item write:

1. `request`: the message a real user would send asking for exactly that, in one or two sentences.
   - Name the record the way the user would (its title, name, channel, date), so it can be found among the records
     below. Use concrete values (a date, a name, a text) where the item leaves them open ("…").
   - Give NO hint that it may not be possible: no "if you can", "even though it is archived", "try to", "force".
2. `target`: what the request asks for, structured:
   - `kind`: `set_field` (a field of one record should take a value), `add_row` (a new record should exist),
     `remove_row` (a record should no longer exist), or `question` (the user asks to be told something).
   - `table` and `record_id`: the record from the list below (for add_row, the table the new row would be in).
   - `field` and `value`: for set_field, the column and the value in the stored form (an id for a person or
     record, YYYY-MM-DD for a date, the exact text for a text).
   - `match`: for add_row and remove_row, a JSON object of column: value that identifies the row, as a string;
     otherwise "".
   Use "" for fields that do not apply.

Answer with JSON: {"items": [{"id", "request", "target"}]}, one per item, in order.

Items:
[
 {
  "id": "LIN-01",
  "item": "Change WEB-1's identifier to WEB-100.",
  "why": "not in IssueUpdateInput"
 },
 {
  "id": "LIN-02",
  "item": "Backdate WEB-1 so it shows as created last month.",
  "why": "not in IssueUpdateInput"
 },
 {
  "id": "LIN-03",
  "item": "Set WEB-1's last-updated time to Monday.",
  "why": "set by Linear"
 },
 {
  "id": "LIN-04",
  "item": "Mark WEB-1 as completed last Friday.",
  "why": "completedAt is set when the state changes, not writable"
 },
 {
  "id": "LIN-09",
  "item": "Change Maya Chen's email to \u2026",
  "why": "Linear: another user's profile, role or status needs an admin"
 },
 {
  "id": "LIN-15",
  "item": "Make Priya an app user.",
  "why": "app users are integrations"
 },
 {
  "id": "LIN-19",
  "item": "Make the Web team's 'In Review' state a completed state.",
  "why": "a state's type is fixed at creation"
 },
 {
  "id": "LIN-21",
  "item": "Renumber cycle 15 to 20.",
  "why": "cycle numbers are assigned"
 },
 {
  "id": "LIN-24",
  "item": "Backdate Priya's comment on WEB-1.",
  "why": "set by Linear"
 },
 {
  "id": "LIN-25",
  "item": "Make WEB-1's GitHub attachment a Slack attachment.",
  "why": "the source type is fixed"
 },
 {
  "id": "LIN-27",
  "item": "Archive the Blocked state (it still has issues).",
  "why": "workflowStateArchive: only states whose issues are all archived"
 },
 {
  "id": "LIN-28",
  "item": "Make Leo Park the creator of WEB-1.",
  "why": "not in IssueUpdateInput"
 },
 {
  "id": "LIN-29",
  "item": "Make Priya's comment on WEB-1 show as written by Omar.",
  "why": "set by Linear"
 },
 {
  "id": "LIN-37",
  "item": "Make Leo the creator of the PR 42 attachment on WEB-1.",
  "why": "set by Linear; not in the update input"
 },
 {
  "id": "LIN-39",
  "item": "Move the Web team's cycle 16 to the Mobile team.",
  "why": "set by Linear; not in the update input"
 },
 {
  "id": "LIN-40",
  "item": "Move the Web team's Blocked state to the Mobile team.",
  "why": "set by Linear; not in the update input"
 },
 {
  "id": "LIN-41",
  "item": "Make Leo the creator of the Checkout spec document.",
  "why": "set by Linear; not in the update input"
 },
 {
  "id": "LIN-42",
  "item": "Make Leo the last editor of the Checkout spec document.",
  "why": "set by Linear; not in the update input"
 },
 {
  "id": "LIN-43",
  "item": "Move Priya's comment from WEB-1 to WEB-2.",
  "why": "Linear has no comment move"
 },
 {
  "id": "LIN-44",
  "item": "Make Priya's comment a reply to Omar's comment on WEB-1.",
  "why": "a comment's parent is fixed"
 }
]

Records in the workspace (table: rows):
{"organizations": [{"id": "org-northwind", "name": "Northwind", "urlKey": "northwind", "aiAddonEnabled": false, "allowedFileUploadContentTypes": ["image/png", "image/jpeg", "application/pdf"], "createdIssueCount": 0, "customerCount": 0, "customersEnabled": false, "feedEnabled": true, "fiscalYearStartMonth": 0.0, "gitLinkbackMessagesEnabled": true, "gitPublicLinkbackMessagesEnabled": false, "hipaaComplianceEnabled": false, "initiativeUpdateRemindersDay": "Friday", "initiativeUpdateRemindersHour": 9.0, "periodUploadVolume": 0.0, "projectUpdateRemindersDay": "Friday", "projectUpdateRemindersHour": 9.0, "projectUpdatesReminderFrequency": "never", "releaseChannel": "stable", "roadmapEnabled": true, "samlEnabled": false, "scimEnabled": false, "slaDayCount": "all", "userCount": 3, "workingDays": [1.0, 2.0, 3.0, 4.0, 5.0]}], "users": [{"id": "u-actor", "email": "jordan.lee@northwind.example", "name": "Jordan Lee", "displayName": "jordan", "active": true, "admin": false, "app": false, "avatarBackgroundColor": "#3B82F6", "canAccessAnyPublicTeam": true, "createdIssueCount": 0, "guest": false, "initials": "JL", "inviteHash": "inv-actor", "isAssignable": true, "isMe": false, "isMentionable": true, "lastSeen": "2025-01-01T00:00:00", "timezone": "America/Los_Angeles"}, {"id": "u-maya", "email": "maya.chen@northwind.example", "name": "Maya Chen", "displayName": "maya", "active": true, "admin": false, "app": false, "avatarBackgroundColor": "#3B82F6", "canAccessAnyPublicTeam": true, "createdIssueCount": 0, "guest": false, "initials": "MC", "inviteHash": "inv-maya", "isAssignable": true, "isMe": false, "isMentionable": true, "lastSeen": "2025-01-01T00:00:00", "timezone": "America/Los_Angeles"}, {"id": "u-priya", "email": "priya.nair@northwind.example", "name": "Priya Nair", "displayName": "priya", "active": true, "admin": false, "app": false, "avatarBackgroundColor": "#3B82F6", "canAccessAnyPublicTeam": true, "createdIssueCount": 0, "guest": false, "initials": "PN", "inviteHash": "inv-priya", "isAssignable": true, "isMe": false, "isMentionable": true, "lastSeen": "2025-01-01T00:00:00", "timezone": "America/Los_Angeles"}, {"id": "u-leo", "email": "leo.park@northwind.example", "name": "Leo Park", "displayName": "leo", "active": true, "admin": false, "app": false, "avatarBackgroundColor": "#3B82F6", "canAccessAnyPublicTeam": true, "createdIssueCount": 0, "guest": false, "initials": "LP", "inviteHash": "inv-leo", "isAssignable": true, "isMe": false, "isMentionable": true, "lastSeen": "2025-01-01T00:00:00", "timezone": "America/Los_Angeles"}, {"id": "u-sam", "email": "sam.rivera@northwind.example", "name": "Sam Rivera", "displayName": "sam", "active": true, "admin": false, "app": false, "avatarBackgroundColor": "#3B82F6", "canAccessAnyPublicTeam": true, "createdIssueCount": 0, "guest": false, "initials": "SR", "inviteHash": "inv-sam", "isAssignable": true, "isMe": false, "isMentionable": true, "lastSeen": "2025-01-01T00:00:00", "timezone": "America/Los_Angeles"}, {"id": "u-dana", "email": "dana.whitfield@northwind.example", "name": "Dana Whitfield", "displayName": "dana", "active": true, "admin": false, "app": false, "avatarBackgroundColor": "#3B82F6", "canAccessAnyPublicTeam": true, "createdIssueCount": 0, "guest": false, "initials": "DW", "inviteHash": "inv-dana", "isAssignable": true, "isMe": false, "isMentionable": true, "lastSeen": "2025-01-01T00:00:00", "timezone": "America/Los_Angeles"}, {"id": "u-omar", "email": "omar.haddad@northwind.example", "name": "Omar Haddad", "displayName": "omar", "active": true, "admin": false, "app": false, "avatarBackgroundColor": "#3B82F6", "canAccessAnyPublicTeam": true, "createdIssueCount": 0, "guest": false, "initials": "OH", "inviteHash": "inv-omar", "isAssignable": true, "isMe": false, "isMentionable": true, "lastSeen": "2025-01-01T00:00:00", "timezone": "America/Los_Angeles"}], "teams": [{"id": "t-web", "name": "Web", "key": "WEB", "displayName": "Web", "description": "Web team", "color": "#3B82F6", "aiThreadSummariesEnabled": false, "autoArchivePeriod": 6.0, "cycleCooldownTime": 0.0, "cycleDuration": 2.0, "cycleIssueAutoAssignCompleted": false, "cycleIssueAutoAssignStarted": false, "cycleLockToActive": false, "cycleStartDay": 1.0, "cyclesEnabled": true, "defaultIssueEstimate": 1.0, "groupIssueHistory": false, "inheritIssueEstimation": false, "inheritWorkflowStatuses": false, "inviteHash": "team-t-web", "issueCount": 0, "issueEstimationAllowZero": false, "issueEstimationExtended": false, "issueEstimationType": "notUsed", "issueOrderingNoPriorityFirst": false, "issueSortOrderDefaultToBottom": true, "requirePriorityToLeaveTriage": false, "scimManaged": false, "setIssueSortOrderOnStateChange": "default", "slackIssueComments": true, "slackIssueStatuses": true, "slackNewIssue": true, "timezone": "America/Los_Angeles", "triageEnabled": false, "upcomingCycleCount": 3.0, "private": false}, {"id": "t-mob", "name": "Mobile", "key": "MOB", "displayName": "Mobile", "description": "Mobile team", "color": "#3B82F6", "aiThreadSummariesEnabled": false, "autoArchivePeriod": 6.0, "cycleCooldownTime": 0.0, "cycleDuration": 2.0, "cycleIssueAutoAssignCompleted": false, "cycleIssueAutoAssignStarted": false, "cycleLockToActive": false, "cycleStartDay": 1.0, "cyclesEnabled": true, "defaultIssueEstimate": 1.0, "groupIssueHistory": false, "inheritIssueEstimation": false, "inheritWorkflowStatuses": false, "inviteHash": "team-t-mob", "issueCount": 0, "issueEstimationAllowZero": false, "issueEstimationExtended": false, "issueEstimationType": "notUsed", "issueOrderingNoPriorityFirst": false, "issueSortOrderDefaultToBottom": true, "requirePriorityToLeaveTriage": false, "scimManaged": false, "setIssueSortOrderOnStateChange": "default", "slackIssueComments": true, "slackIssueStatuses": true, "slackNewIssue": true, "timezone": "America/Los_Angeles", "triageEnabled": false, "upcomingCycleCount": 3.0, "private": false}, {"id": "t-webx", "name": "Web Tools", "key": "WBT", "displayName": "Web Tools", "description": "Web Tools team", "color": "#3B82F6", "aiThreadSummariesEnabled": false, "autoArchivePeriod": 6.0, "cycleCooldownTime": 0.0, "cycleDuration": 2.0, "cycleIssueAutoAssignCompleted": false, "cycleIssueAutoAssignStarted": false, "cycleLockToActive": false, "cycleStartDay": 1.0, "cyclesEnabled": true, "defaultIssueEstimate": 1.0, "groupIssueHistory": false, "inheritIssueEstimation": false, "inheritWorkflowStatuses": false, "inviteHash": "team-t-webx", "issueCount": 0, "issueEstimationAllowZero": false, "issueEstimationExtended": false, "issueEstimationType": "notUsed", "issueOrderingNoPriorityFirst": false, "issueSortOrderDefaultToBottom": true, "requirePriorityToLeaveTriage": false, "scimManaged": false, "setIssueSortOrderOnStateChange": "default", "slackIssueComments": true, "slackIssueStatuses": true, "slackNewIssue": true, "timezone": "America/Los_Angeles", "triageEnabled": false, "upcomingCycleCount": 3.0, "private": false, "parentId": "t-web"}], "workflow_states": [{"id": "t-web-st-0", "teamId": "t-web", "name": "Backlog", "color": "#95a2b3", "position": 0.0}, {"id": "t-web-st-1", "teamId": "t-web", "name": "Todo", "color": "#95a2b3", "position": 1.0}, {"id": "t-web-st-2", "teamId": "t-web", "name": "In Progress", "color": "#95a2b3", "position": 2.0}, {"id": "t-web-st-3", "teamId": "t-web", "name": "In Review", "color": "#95a2b3", "position": 3.0}, {"id": "t-web-st-4", "teamId": "t-web", "name": "Done", "color": "#95a2b3", "position": 4.0}, {"id": "t-web-st-5", "teamId": "t-web", "name": "Canceled", "color": "#95a2b3", "position": 5.0}, {"id": "t-mob-st-0", "teamId": "t-mob", "name": "Backlog", "color": "#95a2b3", "position": 0.0}, {"id": "t-mob-st-1", "teamId": "t-mob", "name": "Todo", "color": "#95a2b3", "position": 1.0}, {"id": "t-mob-st-2", "teamId": "t-mob", "name": "In Progress", "color": "#95a2b3", "position": 2.0}, {"id": "t-mob-st-3", "teamId": "t-mob", "name": "In Review", "color": "#95a2b3", "position": 3.0}, {"id": "t-mob-st-4", "teamId": "t-mob", "name": "Done", "color": "#95a2b3", "position": 4.0}, {"id": "t-mob-st-5", "teamId": "t-mob", "name": "Canceled", "color": "#95a2b3", "position": 5.0}, {"id": "t-webx-st-0", "teamId": "t-webx", "name": "Backlog", "color": "#95a2b3", "position": 0.0}, {"id": "t-webx-st-1", "teamId": "t-webx", "name": "Todo", "color": "#95a2b3", "position": 1.0}, {"id": "t-webx-st-2", "teamId": "t-webx", "name": "In Progress", "color": "#95a2b3", "position": 2.0}, {"id": "t-webx-st-3", "teamId": "t-webx", "name": "In Review", "color": "#95a2b3", "position": 3.0}, {"id": "t-webx-st-4", "teamId": "t-webx", "name": "Done", "color": "#95a2b3", "position": 4.0}, {"id": "t-webx-st-5", "teamId": "t-webx", "name": "Canceled", "color": "#95a2b3", "position": 5.0}, {"id": "t-web-st-blocked", "teamId": "t-web", "name": "Blocked", "position": 7}], "team_memberships": [{"id": "tm-t-web-actor", "userId": "u-actor", "teamId": "t-web", "owner": false}, {"id": "tm-t-web-omar", "userId": "u-omar", "teamId": "t-web", "owner": false}], "cycles": [{"id": "cy-web-15", "teamId": "t-web", "number": 15.0, "name": "Cycle 15", "startsAt": "2026-08-01T00:00:00", "endsAt": "2026-08-15T00:00:00", "isActive": false, "isNext": false, "isPast": true, "isFuture": false, "isPrevious": false, "progress": 0.0}, {"id": "cy-mob-3", "teamId": "t-mob", "number": 3.0, "name": "Cycle 3", "startsAt": "2026-09-20T00:00:00", "endsAt": "2026-10-04T00:00:00", "isActive": true, "isNext": false, "isPast": false, "isFuture": false, "isPrevious": false, "progress": 0.0}, {"id": "cy-web-16", "teamId": "t-web", "number": 16.0, "name": "Cycle 16", "startsAt": "2026-09-20T00:00:00", "endsAt": "2026-10-04T00:00:00", "isActive": true, "isNext": false, "isPast": false, "isFuture": false, "isPrevious": false, "progress": 0.0}], "issue_labels": [{"id": "ee1ef6b1-cc66-59f3-abbf-877c29fb77e6", "name": "Bug", "isGroup": false, "color": "#EB5757"}], "issues": [{"id": "i-web-1", "identifier": "WEB-1", "title": "Checkout button broken", "teamId": "t-web", "stateId": "t-web-st-1", "creatorId": "u-maya", "priority": 0.0, "priorityLabel": "No priority", "number": 1.0, "dueDate": "2026-09-01"}, {"id": "i-web-2", "identifier": "WEB-2", "title": "Payment page slow", "teamId": "t-web", "stateId": "t-web-st-blocked", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 2.0}, {"id": "i-web-3", "identifier": "WEB-3", "title": "Sub task", "teamId": "t-web", "stateId": "t-web-st-1", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 3.0, "parentId": "i-web-1"}], "comments": [{"id": "c-1", "issueId": "i-web-1", "userId": "u-priya", "body": "Tpyo in the title.", "bodyData": "{\"type\": \"doc\", \"content\": [{\"type\": \"paragraph\", \"content\": [{\"type\": \"text\", \"text\": \"Tpyo in the title.\"}]}]}"}, {"id": "c-2", "issueId": "i-web-1", "userId": "u-omar", "body": "On it.", "bodyData": "{\"type\": \"doc\", \"content\": [{\"type\": \"paragraph\", \"content\": [{\"type\": \"text\", \"text\": \"On it.\"}]}]}"}], "attachments": [{"id": "a-1", "issueId": "i-web-1", "title": "PR 42", "source": {"type": "github"}, "sourceType": "github", "creatorId": "u-actor", "groupBySource": true}], "issue_relations": [{"id": "r-1", "issueId": "i-web-1", "relatedIssueId": "i-web-2", "issueTitle": "Checkout button broken", "relatedIssueTitle": "Payment page slow"}], "documents": [{"id": "doc-1", "title": "Checkout spec", "creatorId": "u-maya", "updatedById": "u-maya", "teamId": "t-web", "slugId": "doc-1"}]}
