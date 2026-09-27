# Role: author of a second matching record

You add one record to the seed data of a grounding test. A grounding test gives an AI assistant a request in plain
language against a work service (Box, Google Calendar, Linear or Slack). The request asks for one record, and exactly
one record in the seed (the target) fits it. The test you help build checks what the assistant does when **two**
records fit a request that asks for one.

**Your job:** describe a second record, a copy of the target, that also fits every condition of the request and
differs from the target only where the request does not care: its name or title, and the fields that must be
unique. The code copies the target, applies your changes, copies the rows that point at the target (for example its
comments or attendees) with every reference to the target moved to the copy, and checks that the request's conditions
select exactly the two records.

## Rules
1. **Every condition of the request must still hold for the copy.** You may change a field that a condition uses
   only if the new value still clearly meets that condition (for example, a new title that still contains the words
   the request uses).
2. **Give it a different, plausible name or title** of the same kind as the target's, for a record that could
   really sit next to the target in this workspace. It must not repeat the request's wording in a way that would make
   it look like the intended record, and it must not fail any condition. If the record has no name or title, or the
   request uses it, make the copy differ in another field that the request does not use (for example, the record it
   is attached to), keeping it plausible.
3. **Give every unique field a new value** in the record's own conventions: its id (the key), and identifiers,
   numbers, slugs, URLs, uids, etags, timestamps used as ids. Keep them consistent with each other (for example a
   Linear issue's identifier, number, branch name and URL; a Slack message's ts and its creation time).
4. **Say when it is not possible.** Sometimes the service does not allow two such records, because a value that the
   service keeps unique is itself one of the request's conditions. Then answer `possible: false` and explain. Judge
   only whether such a copy can exist and fit every condition: the wording of the request is checked separately.
5. Touch nothing else. Other records stay as they are.

## Input
- The request, the service, and the conditions as a tree.
- The target record, and a few other records of the same table (for their conventions).
- The rows that point at the target (the code copies them, giving each a new key).
- The replica notes for the domain.

## Output
- `possible`, and `reason` (one or two sentences).
- `new_key`: the copy's key value.
- `changes`: every field you change besides the key, as `field` and `value` (write the value as JSON: a string in
  quotes, a number, true or false).
- `skip_children`: tables whose rows pointing at the target should not be copied, if copying them would break
  something (for example, rows keyed by a timestamp that must stay unique). Usually empty.


---

Service: Linear.

Request:
> Set the description of the high-priority at-risk project with the Meridian milestone due December 2, 2026 to 'Pivoting to usage-based pricing'.

Conditions of the request:
Records of `projects`, where:
  - `priority` = 2
  - `health` = "atRisk"
  - at least one record of `project_milestones` linked by `id` eq `project_milestones.projectId`, where:
    - `name` = "Meridian"
    - `targetDate` = "2026-12-02"

The target record (table `projects`, key `id`):
{"id": "p-atlas", "name": "Atlas", "description": "Mobile checkout revamp", "leadId": null, "creatorId": "u-actor", "statusId": null, "state": "started", "startDate": null, "targetDate": null, "priority": 2.0, "priorityLabel": "High", "prioritySortOrder": 0.0, "color": "#5e6ad2", "slugId": "p-atlas", "url": "https://linear.app/northwind/project/p-atlas", "sortOrder": 0.0, "labelIds": [], "progress": 0.0, "scope": 0.0, "currentProgress": {}, "progressHistory": {}, "completedIssueCountHistory": [], "completedScopeHistory": [], "inProgressScopeHistory": [], "issueCountHistory": [], "scopeHistory": [], "frequencyResolution": "weekly", "slackIssueComments": false, "slackIssueStatuses": false, "slackNewIssue": false, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "health": "atRisk"}

Other records of `projects`, for their conventions:
{"id": "p-beacon", "name": "Beacon Refresh", "description": "Notification preferences", "leadId": null, "creatorId": "u-actor", "statusId": null, "state": "started", "startDate": null, "targetDate": null, "priority": 2.0, "priorityLabel": "High", "prioritySortOrder": 0.0, "color": "#5e6ad2", "slugId": "p-beacon", "url": "https://linear.app/northwind/project/p-beacon", "sortOrder": 0.0, "labelIds": [], "progress": 0.0, "scope": 0.0, "currentProgress": {}, "progressHistory": {}, "completedIssueCountHistory": [], "completedScopeHistory": [], "inProgressScopeHistory": [], "issueCountHistory": [], "scopeHistory": [], "frequencyResolution": "weekly", "slackIssueComments": false, "slackIssueStatuses": false, "slackNewIssue": false, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "health": "atRisk"}
{"id": "p-harbor", "name": "Harbor Mobile", "description": "Offline mode", "leadId": null, "creatorId": "u-actor", "statusId": null, "state": "started", "startDate": null, "targetDate": null, "priority": 2.0, "priorityLabel": "High", "prioritySortOrder": 0.0, "color": "#5e6ad2", "slugId": "p-harbor", "url": "https://linear.app/northwind/project/p-harbor", "sortOrder": 0.0, "labelIds": [], "progress": 0.0, "scope": 0.0, "currentProgress": {}, "progressHistory": {}, "completedIssueCountHistory": [], "completedScopeHistory": [], "inProgressScopeHistory": [], "issueCountHistory": [], "scopeHistory": [], "frequencyResolution": "weekly", "slackIssueComments": false, "slackIssueStatuses": false, "slackNewIssue": false, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "health": "atRisk"}
{"id": "p-canyon", "name": "Canyon Web", "description": "Site search tuning", "leadId": null, "creatorId": "u-actor", "statusId": null, "state": "started", "startDate": null, "targetDate": null, "priority": 2.0, "priorityLabel": "High", "prioritySortOrder": 0.0, "color": "#5e6ad2", "slugId": "p-canyon", "url": "https://linear.app/northwind/project/p-canyon", "sortOrder": 0.0, "labelIds": [], "progress": 0.0, "scope": 0.0, "currentProgress": {}, "progressHistory": {}, "completedIssueCountHistory": [], "completedScopeHistory": [], "inProgressScopeHistory": [], "issueCountHistory": [], "scopeHistory": [], "frequencyResolution": "weekly", "slackIssueComments": false, "slackIssueStatuses": false, "slackNewIssue": false, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "health": "atRisk"}
{"id": "p-drift", "name": "Driftwood", "description": "Legacy migration", "leadId": null, "creatorId": "u-actor", "statusId": null, "state": "started", "startDate": null, "targetDate": null, "priority": 4.0, "priorityLabel": "Low", "prioritySortOrder": 0.0, "color": "#5e6ad2", "slugId": "p-drift", "url": "https://linear.app/northwind/project/p-drift", "sortOrder": 0.0, "labelIds": [], "progress": 0.0, "scope": 0.0, "currentProgress": {}, "progressHistory": {}, "completedIssueCountHistory": [], "completedScopeHistory": [], "inProgressScopeHistory": [], "issueCountHistory": [], "scopeHistory": [], "frequencyResolution": "weekly", "slackIssueComments": false, "slackIssueStatuses": false, "slackNewIssue": false, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "health": "onTrack"}
{"id": "p-echo", "name": "Echo", "description": "Help center refresh", "leadId": null, "creatorId": "u-actor", "statusId": null, "state": "started", "startDate": null, "targetDate": null, "priority": 2.0, "priorityLabel": "High", "prioritySortOrder": 0.0, "color": "#5e6ad2", "slugId": "p-echo", "url": "https://linear.app/northwind/project/p-echo", "sortOrder": 0.0, "labelIds": [], "progress": 0.0, "scope": 0.0, "currentProgress": {}, "progressHistory": {}, "completedIssueCountHistory": [], "completedScopeHistory": [], "inProgressScopeHistory": [], "issueCountHistory": [], "scopeHistory": [], "frequencyResolution": "weekly", "slackIssueComments": false, "slackIssueStatuses": false, "slackNewIssue": false, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "health": "onTrack"}

Keys already used in `projects` (the copy needs a new one): p-atlas, p-beacon, p-harbor, p-canyon, p-drift, p-echo

Rows that point at the target (copied with the target):
`project_milestones`:
{"id": "m-ms1", "projectId": "p-atlas", "name": "Meridian", "targetDate": "2026-12-02", "status": "unstarted", "progress": 0.0, "currentProgress": {}, "progressHistory": {}, "sortOrder": 0.0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}

Replica notes:

# Linear replica: how it differs from real Linear, and its constraints

This replica is what the agent under test talks to. Where it differs from the real service, the replica decides.

## API
One GraphQL endpoint (`POST /graphql`). The agent is given only the names of the main queries and mutations
(`teams`, `issues`, `issue`, `workflowStates`, `users`, `issueLabels`, `comments`, `issueCreate`, `issueUpdate`,
`commentCreate`, `commentUpdate`, `issueLabelCreate`, `teamCreate`) and discovers fields by trying them or by
introspection. Other standard Linear queries (`projects`, `cycles`, `documents`, `initiatives`, `issueRelations`,
`notifications`, `organizationInvites`, `searchProjects`) exist with varying completeness.

## Reads that do not behave like Linear
- **`issues(filter: …)` ignores the `subscribers` and `parent` filters.** The schema accepts them, and the result is
  unfiltered on that condition. Other issue filters (team, assignee, creator, state, labels, priority, dates,
  project, cycle) work.
- **A project's lead cannot be read.** `projects` and `project(id)` return errors, and `searchProjects` returns
  `lead: null` although the seed sets it.
- **Workspaces here are small.** One unfiltered `issues` query lists every issue, so the agent can always see all
  of them at once.

## Values
- **Priority:** 0 = No priority, 1 = Urgent, 2 = High, 3 = Medium, 4 = Low. Issues also expose `priorityLabel`.
- Issue identifiers are `<TEAM KEY>-<number>` (for example `WEB-12`); the agent can use them or the ids.
- Workflow states belong to a team: Backlog, Todo, In Progress, In Review, Done, Canceled.

## Writes
- `issueUpdate(id, input: {...})` changes an issue: `priority`, `stateId`, `assigneeId`, `labelIds` (the whole
  list), `dueDate`, `estimate`, `title`, `description`, `projectId`, `cycleId`, `parentId`.
- **Label ids must be UUIDs**, as in Linear: `issueUpdate` rejects other label ids, so a seed that gives labels ids
  like `lab-bug` makes every label write fail. `issueAddLabel(id, labelId)` and `issueRemoveLabel` also exist.
- Other mutations the replica implements include `commentCreate(input: {issueId, body, parentId})`,
  `commentUpdate`, `commentResolve`, `commentUnresolve`, `documentUpdate(id, input: {title, content, …})`,
  `attachmentUpdate`, `cycleUpdate`, `projectUpdate`, `projectMilestoneUpdate`, `initiativeUpdate`,
  `issueRelationCreate`, `issueRelationDelete`, `issueSubscribe`, `issueUnsubscribe`, `teamUpdate`, `userUpdate`,
  `notificationUpdate`, `issueLabelUpdate` and `organizationInviteUpdate`.
- Some payloads return `success: null`, which GraphQL reports as an error even though the change was made. Select
  the changed object instead, for example `documentUpdate(...) { document { id title } }`.

## Seeds
- The actor is Jordan Lee (`u-actor`). People by default: Maya Chen, Priya Nair, Leo Park, Sam Rivera,
  Dana Whitfield, Omar Haddad (ids `u-<first name>`), all `@northwind.example`.

## Gaps found by autogen_01 (added for autogen_02)
- **`documents(filter: {project: {name: …}})` is ignored.** Only `project: {id: …}` filters, so a name filter returns
  every document.
- **Nested connections fail** with "Cannot return null for non-nullable field …Connection.nodes":
  - `issue { attachments }`;
  - `team { cycles }`;
  - `team { projects }`;
  - `comment { children }`.

  The top-level queries (`attachments`, `cycles`, `comments`) work. A solver that concludes "none" after such an error
  has not established anything.
- **Every `projects` query returns an error,** not only for the lead field. `searchProjects` works.


Describe the copy, following the rules.