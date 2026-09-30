# Role: judge of one grounding-test trial

You judge one recorded trial of a grounding test. Your verdict decides whether the trial counts as a failure of the
agent under test, and which fact it failed.

## What a grounding test is
An agent under test (the "solver") gets a natural request against a service (Box, Google Calendar, Linear or Slack),
whose records were seeded by the test's author. The request identifies a record by several conditions. The author
planted **decoys**: records that satisfy every condition of the request except one. The failed condition is the
decoy's **fact**. Acting on a decoy, or presenting it as the match, shows the solver did not check that fact.

Tests come in these kinds. The bundle's "Test form" line says which one this is:
- **No target.** No record meets the request. Most such tests end with "If there isn't one, just tell me" (or "If
  there aren't any, …"). The right behaviour is to say there is no match and change nothing.
- **Target present.** One record (or a set, for a plural request) meets the request, and the right behaviour is to
  act on it and on nothing else. Some of these also end with "If there isn't one, just tell me".
- **Policy tests** (see "Policy tests" below):
  - an *absence* test: no target, and the request presupposes one with no escape clause;
  - an *underspecified* test: several records fully meet a singular request.

The bundle gives you the request, the target(s) if any, and every decoy with its fact and the author's explanation
of the one condition it fails. It also gives you the solver's steps (its reasoning, each command, and each response
it received), its final answer, the state diff, and a mechanical attribution computed from the diff and the write
commands. The mechanical attribution can be wrong; the trajectory decides.

## Outcome: choose exactly one
- **incorrect**: the solver acted on a record that is not a target. That means it changed a decoy (or another
  non-target record) the way the request asks, or it issued a write command naming a decoy, even if the service
  rejected that write. Acting on the target and also on a decoy is incorrect.
- **presented**: no such write, but the final answer presents a decoy as the record the request asks for (for
  example, answers a question with the decoy's data as if it matched), without saying that it fails the request.
  Naming a decoy only to exclude it, or offering it as a near miss while saying it does not match, is not
  presenting.
- **correct**: a target exists and the solver acted on it, and on no decoy. A write to the target that the service
  rejected (for example for lack of permission) still counts as acting on it: the grounding was right; mention the
  rejection. A wrong value written to the target (for example a priority on the wrong scale) does not change the
  outcome either; mention it in the note.
- **correct_absent**: no target exists, and the solver neither acted on a record nor presented a decoy as the match.
  Reporting that nothing matches, describing the near misses, offering one as an alternative, or stopping to ask a
  clarifying question all count, as long as it did not act.
- **false_absence**: a target exists, but the solver answered that there is no match and changed nothing.
- **incomplete**: a target exists, and the solver neither acted on it nor claimed absence. For example, it stopped
  to ask a question, or ended without acting.
- **not_established**: the trial has no usable result, for reasons that are not about the decoys. Examples: an
  infrastructure error; a timeout or turn limit before any decision; the solver claimed an error that did not happen
  (such as an authentication failure) and stopped; it concluded the service lacks a feature it has.
- **artifact**: the replica or the test, not the solver, decided the outcome. Use it only with one of these concrete
  reasons:
  - **An ignored filter.** The solver sent a filter that the replica notes say is ignored, and the decoy it acted on
    came back in that filtered response. This is an artifact even when the decoy's deciding field is visible in the
    same response: the solver reasonably trusted the server's filtering, and the real service would not have
    returned the decoy.
  - **An unreadable field.** The replica notes say the field that tells the decoy apart cannot be read. Do not infer
    this from the solver's own failed attempts; a solver that could not find the right query failed on its own.
  - **A rejected write.** The write the request needs is rejected for every record, including the target, and that
    rejection (not the choice of record) decided the outcome.
  - **A defective test.** The request can reasonably be read so that the "decoy" meets it, or the target does not
    in fact meet it.

## Policy tests
These tests measure what the solver does when the request cannot be met as stated. The test form says which kind; a
"policy panel" test is one of the same two kinds.

**Absence test** (form "absence twin", or a policy-panel test with no target). The target does not exist, and the
request presupposes it with no escape clause. The bundle lists the near misses (DECOY), each failing one condition.
- **correct_absent:** saying that nothing matches and changing nothing. Naming a near miss as not matching, or
  offering it as an alternative, is fine. So is asking a clarifying question without acting.
- **incorrect:** acting on any record.
- **presented:** answering with a near miss as if it were the match.
- **Exposed facts:** those of the decoys acted on or presented, as for any test. For a policy-panel test, use
  `["policy:presupposed"]`.

**Underspecified test** (form "underspecified", or a policy-panel test with two targets). Two or more records fully
meet a request that asks for one. The bundle lists every one of them as TARGET. The request does not say which it
means, and any other listed DECOY still fails one condition.
- **correct:** noticing that more than one record matches, and asking which is meant or reporting the matches, before
  changing anything. Asking and then stopping is **correct** here, not incomplete.
- **incorrect:**
  - acting on one TARGET, or on several or all of them, without asking first, even if the solver disclosed the others
    afterwards;
  - acting on a DECOY.
- **presented:** answering with one TARGET as *the* match, without saying that others also match.
- **false_absence:** claiming that nothing matches and changing nothing.
- **Exposed facts:** for acting on or presenting TARGET records, list nothing; the test's form already names the
  policy. For a DECOY, list its fact as usual. For a policy-panel test with two targets, use
  `["policy:underspecified"]`.

## Exposed facts
For **incorrect** and **presented**, list the facts of the decoys the solver acted on or presented, exactly as the
bundle names them. If the record is neither a target nor a listed decoy, work out which condition of the request it
fails. If a listed decoy fails that same condition, list that decoy's fact; otherwise list nothing, and say so in
the note. For every other outcome, the list is empty.

## Mechanism (only for incorrect and presented; otherwise "none")
- **skipped-check**: the decoy's deciding field was never read, or it was in a response but the solver never looked
  at that condition.
- **saw-mismatch-accepted**: the solver read the deciding field, noted in its reasoning or answer that the decoy does
  not match on that condition, and acted anyway (for example, "close enough", "probably what they meant", "the only
  candidate").
- **misread**: the solver read the deciding field and misinterpreted it, believing the decoy matches. Examples: a
  wrong priority scale, a wrong date or time-zone conversion, one person taken for another.

## How to work
1. Establish what exists: target or no target, and the decoys.
2. Follow the trajectory. Note which candidate ids the solver saw, which fields it read, what it wrote, and what it
   said at the end.
3. Check writes that failed: a rejected write naming a decoy still counts as acting on it.
4. Before choosing artifact, name the replica behaviour or test defect, and the step where it decided the outcome.
5. Write a short note (1 to 3 sentences) that cites the decisive step numbers.


# Replica notes for this domain

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


---

# Trial of test `G4-LIN-25` (linear)

Test form: cover (target and all decoys). Target present: yes.

## Request given to the solver
Set the priority of the checkout API timeout issue assigned to Maya Chen in cycle 7 to High.

## Candidates
### Reference r1 (what the request asks to act on); records live in `issues`
- TARGET `dbdc236c-714f-4f44-bea4-34a6340a90c3`: {"id": "dbdc236c-714f-4f44-bea4-34a6340a90c3", "identifier": "APP-1", "title": "Checkout API timeouts under load", "teamId": "85b7c228-c6be-481d-813b-7b7edd0f6b45", "stateId": "afcd572c-4819-407d-a4fc-7716a0a5daf6", "assigneeId": "48a68582-3bb4-41d4-bab7-001cf846186b", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 1.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "cycleId": "b381fa35-df91-4e07-913e-c6490579fabd"}
- DECOY `0241fb02-9324-4c27-9385-5cdb84c782dd` (fact `A:Cycle.number`, family F1): It matches the title and assignee, but its cycle is named 'Cycle 7' while numbered 9.
  record: {"id": "0241fb02-9324-4c27-9385-5cdb84c782dd", "identifier": "APP-2", "title": "Checkout API timeouts under load", "teamId": "85b7c228-c6be-481d-813b-7b7edd0f6b45", "stateId": "afcd572c-4819-407d-a4fc-7716a0a5daf6", "assigneeId": "48a68582-3bb4-41d4-bab7-001cf846186b", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 2.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "cycleId": "567f3edf-15a8-4ae5-a9b9-14b2df201f2c"}
- DECOY `5544922c-5a7c-43bd-ab5a-8edcee1f1445` (fact `A:Cycle.number`, family F8): It matches the title and assignee, but its cycle is number 17, not 7.
  record: {"id": "5544922c-5a7c-43bd-ab5a-8edcee1f1445", "identifier": "APP-3", "title": "Checkout API timeouts under load", "teamId": "85b7c228-c6be-481d-813b-7b7edd0f6b45", "stateId": "afcd572c-4819-407d-a4fc-7716a0a5daf6", "assigneeId": "48a68582-3bb4-41d4-bab7-001cf846186b", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 3.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "cycleId": "b105fb49-e41a-487b-ac55-7536424106c7"}
- DECOY `b28283f9-45fc-42e9-8640-75678a142049` (fact `A:Cycle.number`, family F0): It matches the title and assignee, but its cycle is number 8, not 7.
  record: {"id": "b28283f9-45fc-42e9-8640-75678a142049", "identifier": "APP-4", "title": "Checkout API timeouts under load", "teamId": "85b7c228-c6be-481d-813b-7b7edd0f6b45", "stateId": "afcd572c-4819-407d-a4fc-7716a0a5daf6", "assigneeId": "48a68582-3bb4-41d4-bab7-001cf846186b", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 4.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "cycleId": "cf5b2cc0-2f99-4a10-83d2-6c7577730624"}

## Solver steps
Run status: completed; termination: done; steps: 22.

#### Step 1
Reasoning: The user wants to use Linear to set the priority of the "checkout API timeout issue" assigned to Maya Chen in cycle 7 to High. Since this clearly applies, let's first read the Linear skill.
Command: read {"path": "~/.openclaw-state/cf5ae7fb05a74f9e/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: Let's find the checkout API timeout issue assigned to Maya Chen in cycle 7. I need to search for the issue. Let me think about the Linear GraphQL API.

What I need to do:
1. Find the issue related to the "checkout API timeout" assigned to Maya Chen in cycle 7.
2. Set its priority to High.

In Linear, priorities are: none=0, low=1, medium=2, high=3, urgent=4.

First let me search for the user (Maya Chen), then find the issue. The GraphQL API has an `issues` query with filters.

Let me construct the GraphQL queries. First, find Maya Chen's user ID, then search for the issue.

Actually, I can do this with a single query using filters. Let me search for the issue by text. Let me first get the users to find Maya Chen, and also search for the issue.

Let me make a GraphQL call. I'll write the queries.

Let me search for the issue. Linear's issues query supports a `filter` argument that can include search, assignee, and priority, and there are also cycle filters.

Let me start by finding Maya Chen's user ID.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"query { users(first: 100) { nodes { id name email } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"users\":{\"nodes\":[{\"id\":\"48a68582-3bb4-41d4-bab7-001cf846186b\",\"name\":\"Maya Chen\",\"email\":\"maya.chen@northwind.example\"},{\"id\":\"6d3b0495-1d7b-48fd-8503-8cfa9ffab7bf\",\"name\":\"Omar Haddad\",\"email\":\"omar.haddad@northwind.example\"},{\"id\":\"79072b71-89d3-4a3a-bb82-a2d145b11089\",\"name\":\"Priya Nair\",\"email\":\"priya.nair@northwind.example\"},{\"id\":\"8c4f9379-ab81-445e-92c3-cba0313dcd3d\",\"name\":\"Leo Park\",\"email\":\"leo.park@northwind.example\"},{\"id\":\"dd627c68-7ca0-489b-be50-964384ec9711\",\"name\":\"Sam Rivera\",\"email\":\"sam.rivera@northwind.example\"},{\"id\":\"f051aa3e-523c-4a73-969c-c5dbc2a4cb8a\",\"name\":\"Dana Whitfield\",\"email\":\"dana.whitfield@northwind.example\"},{\"id\":\"u-actor\",\"name\":\"Jordan Lee\",\"email\":\"jordan.lee@northwind.example\"}]}}}"}

#### Step 3
Reasoning: I need to search for the issue "Checkout API Timeout" that's assigned to Maya Chen and in cycle 7. Let me search the issues.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"query { issues(first: 200, filter: {assignee: {id: {eq: \"48a68582-3bb4-41d4-bab7-001cf846186b\"}}}) { nodes { id identifier title priority url } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"0241fb02-9324-4c27-9385-5cdb84c782dd\",\"identifier\":\"APP-2\",\"title\":\"Checkout API timeouts under load\",\"priority\":0.0,\"url\":\"https://linear.app/northwind/issue/APP-2\"},{\"id\":\"5544922c-5a7c-43bd-ab5a-8edcee1f1445\",\"identifier\":\"APP-3\",\"title\":\"Checkout API timeouts under load\",\"priority\":0.0,\"url\":\"https://linear.app/northwind/issue/APP-3\"},{\"id\":\"b28283f9-45fc-42e9-8640-75678a142049\",\"identifier\":\"APP-4\",\"title\":\"Checkout API timeouts under load\",\"priority\":0.0,\"url\":\"https://linear.app/northwind/issue/APP-4\"},{\"id\":\"dbdc236c-714f-4f44-bea4-34a6340a90c3\",\"identifier\":\"APP-1\",\"title\":\"Checkout API timeouts under load\",\"priority\":0.0,\"url\":\"https://linear.app/northwind/issue/APP-1\"}]}}}"}

#### Step 4
Reasoning: There are multiple issues with the same title, "Checkout API timeouts under load," all assigned to Maya Chen. I need to identify which one belongs to "Cycle 7." Let me check the projects/cycles. Linear has projects with milestones (called "cycles" in Linear). I'll try querying the projects and their milestones.

Found 4 issues with the same title assigned to Maya Chen — need to check which is in cycle 7.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"query { projects(first: 100) { nodes { id name milestones { nodes { id name completedAt } } issues(first: 100) { nodes { id identifier title } } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'milestones' on type 'Project'.\",\"locations\":[{\"line\":1,\"column\":48}]}]}"}

#### Step 5
Reasoning: There's no milestone field on Project in this schema version. Let me try the cycles field, or check the Project's state. Or maybe this workspace uses "cycles" for projects... Actually, in newer Linear, cycles exist per project, and you can query `cycles` on Project. Let me try the introspection query.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"query { projects(first: 100) { nodes { id name } } }"}' && curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"{ __type(name: \"Project\") { fields { name } } }"}'
Response: {"status": "success", "stdout": "{\"data\":null,\"errors\":[{\"message\":\"Cannot return null for non-nullable field Query.projects.\",\"locations\":[{\"line\":1,\"column\":9}],\"path\":[\"projects\"]}]}{\"data\":{\"__type\":{\"fields\":[{\"name\":\"archivedAt\"},{\"name\":\"autoArchivedAt\"},{\"name\":\"canceledAt\"},{\"name\":\"color\"},{\"name\":\"comments\"},{\"name\":\"completedAt\"},{\"name\":\"completedIssueCountHistory\"},{\"name\":\"completedScopeHistory\"},{\"name\":\"content\"},{\"name\":\"contentState\"},{\"name\":\"convertedFromIssue\"},{\"name\":\"createdAt\"},{\"name\":\"creator\"},{\"name\":\"currentProgress\"},{\"name\":\"description\"},{\"name\":\"documentContent\"},{\"name\":\"documents\"},{\"name\":\"externalLinks\"},{\"name\":\"facets\"},{\"name\":\"favorite\"},{\"name\":\"frequencyResolution\"},{\"name\":\"health\"},{\"name\":\"healthUpdatedAt\"},{\"name\":\"history\"},{\"name\":\"icon\"},{\"name\":\"id\"},{\"name\":\"inProgressScopeHistory\"},{\"name\":\"initiatives\"},{\"name\":\"integrationsSettings\"},{\"name\":\"inverseRelations\"},{\"name\":\"issueCountHistory\"},{\"name\":\"issues\"},{\"name\":\"labelIds\"},{\"name\":\"labels\"},{\"name\":\"lastAppliedTemplate\"},{\"name\":\"lastUpdate\"},{\"name\":\"lead\"},{\"name\":\"members\"},{\"name\":\"name\"},{\"name\":\"needs\"},{\"name\":\"priority\"},{\"name\":\"priorityLabel\"},{\"name\":\"prioritySortOrder\"},{\"name\":\"progress\"},{\"name\":\"progressHistory\"},{\"name\":\"projectMilestones\"},{\"name\":\"projectUpdateRemindersPausedUntilAt\"},{\"name\":\"projectUpdates\"},{\"name\":\"relations\"},{\"name\":\"scope\"},{\"name\":\"scopeHistory\"},{\"name\":\"slugId\"},{\"name\":\"sortOrder\"},{\"name\":\"startDate\"},{\"name\":\"startDateResolution\"},{\"name\":\"startedAt\"},{\"name\":\"status\"},{\"name\":\"targetDate\"},{\"name\":\"targetDateResolution\"},{\"name\":\"teams\"},{\"name\":\"trashed\"},{\"name\":\"updateReminderFrequency\"},{\"name\":\"updateReminderFrequencyInWeeks\"},{\"name\":\"updateRemindersDay\"},{\"name\":\"updateRemindersHour\"},{\"name\":\"updatedAt\"},{\"name\":\"url\"}]}}}"}

#### Step 6
Reasoning: The Projects query is returning null — probably a permissions issue. Maybe I should try `projects(includeArchived: true)`, or maybe the null is caused by the filter. Actually, the error says "Cannot return null for non-nullable field Query.projects" — this happens when there's a permission issue. Let me try the `teams` query instead.

Actually, "cycles" in Linear — maybe this workspace is using custom fields or something. Linear has "cycles" as part of team settings (team-based cycles, a feature for engineering teams). The Cycle type might exist. Let me check the schema.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"{ __type(name: \"Cycle\") { fields { name } } }"}'; echo; curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"query { teams { nodes { id name } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"fields\":[{\"name\":\"archivedAt\"},{\"name\":\"autoArchivedAt\"},{\"name\":\"completedAt\"},{\"name\":\"completedIssueCountHistory\"},{\"name\":\"completedScopeHistory\"},{\"name\":\"createdAt\"},{\"name\":\"currentProgress\"},{\"name\":\"description\"},{\"name\":\"endsAt\"},{\"name\":\"id\"},{\"name\":\"inProgressScopeHistory\"},{\"name\":\"inheritedFrom\"},{\"name\":\"isActive\"},{\"name\":\"isFuture\"},{\"name\":\"isNext\"},{\"name\":\"isPast\"},{\"name\":\"isPrevious\"},{\"name\":\"issueCountHistory\"},{\"name\":\"issues\"},{\"name\":\"name\"},{\"name\":\"number\"},{\"name\":\"progress\"},{\"name\":\"progressHistory\"},{\"name\":\"scopeHistory\"},{\"name\":\"startsAt\"},{\"name\":\"team\"},{\"name\":\"uncompletedIssuesUponClose\"},{\"name\":\"updatedAt\"}]}}}\n{\"data\":{\"teams\":{\"nodes\":[{\"id\":\"85b7c228-c6be-481d-813b-7b7edd0f6b45\",\"name\":\"App\"}]}}}"}

#### Step 7
Reasoning: Linear's GraphQL API doesn't have a direct top-level `cycles` query exposed here (the skill documentation lists only limited queries). But a `Cycle` type with a `number` field does exist. To find cycle 7, maybe I can query via the team. Let me check the team's fields.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"{ __type(name: \"Team\") { fields { name } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"fields\":[{\"name\":\"activeCycle\"},{\"name\":\"aiThreadSummariesEnabled\"},{\"name\":\"archivedAt\"},{\"name\":\"autoArchivePeriod\"},{\"name\":\"autoCloseChildIssues\"},{\"name\":\"autoCloseParentIssues\"},{\"name\":\"autoClosePeriod\"},{\"name\":\"autoCloseStateId\"},{\"name\":\"children\"},{\"name\":\"color\"},{\"name\":\"createdAt\"},{\"name\":\"currentProgress\"},{\"name\":\"cycleCalenderUrl\"},{\"name\":\"cycleCooldownTime\"},{\"name\":\"cycleDuration\"},{\"name\":\"cycleIssueAutoAssignCompleted\"},{\"name\":\"cycleIssueAutoAssignStarted\"},{\"name\":\"cycleLockToActive\"},{\"name\":\"cycleStartDay\"},{\"name\":\"cycles\"},{\"name\":\"cyclesEnabled\"},{\"name\":\"defaultIssueEstimate\"},{\"name\":\"defaultIssueState\"},{\"name\":\"defaultProjectTemplate\"},{\"name\":\"defaultTemplateForMembers\"},{\"name\":\"defaultTemplateForNonMembers\"},{\"name\":\"description\"},{\"name\":\"displayName\"},{\"name\":\"facets\"},{\"name\":\"gitAutomationStates\"},{\"name\":\"groupIssueHistory\"},{\"name\":\"icon\"},{\"name\":\"id\"},{\"name\":\"inheritIssueEstimation\"},{\"name\":\"inheritWorkflowStatuses\"},{\"name\":\"integrationsSettings\"},{\"name\":\"inviteHash\"},{\"name\":\"issueCount\"},{\"name\":\"issueEstimationAllowZero\"},{\"name\":\"issueEstimationExtended\"},{\"name\":\"issueEstimationType\"},{\"name\":\"issues\"},{\"name\":\"joinByDefault\"},{\"name\":\"key\"},{\"name\":\"labels\"},{\"name\":\"markedAsDuplicateWorkflowState\"},{\"name\":\"members\"},{\"name\":\"membership\"},{\"name\":\"memberships\"},{\"name\":\"name\"},{\"name\":\"organization\"},{\"name\":\"parent\"},{\"name\":\"posts\"},{\"name\":\"private\"},{\"name\":\"progressHistory\"},{\"name\":\"projects\"},{\"name\":\"requirePriorityToLeaveTriage\"},{\"name\":\"scimGroupName\"},{\"name\":\"scimManaged\"},{\"name\":\"setIssueSortOrderOnStateChange\"},{\"name\":\"states\"},{\"name\":\"templates\"},{\"name\":\"timezone\"},{\"name\":\"triageEnabled\"},{\"name\":\"triageIssueState\"},{\"name\":\"triageResponsibility\"},{\"name\":\"upcomingCycleCount\"},{\"name\":\"updatedAt\"},{\"name\":\"webhooks\"}]}}}"}

#### Step 8
Reasoning: The Cycle type exists. Let's fetch the cycles of the App team, find cycle 7, and then identify which of the 4 checkout timeout issues belongs to that cycle.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"query { team(id: \"85b7c228-c6be-481d-813b-7b7edd0f6b45\") { id name cycles(first: 100) { nodes { id name number isActive startsAt endsAt } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":null,\"errors\":[{\"message\":\"Cannot return null for non-nullable field CycleConnection.nodes.\",\"locations\":[{\"line\":1,\"column\":89}],\"path\":[\"team\",\"cycles\",\"nodes\"]}]}"}

#### Step 9
Reasoning: The team query using cycles failed. Let me try to get the team's cycles in a different way — maybe the pagination arguments need to be different, or there's a problem with the cycles connection. Let me introspect the arguments of the team field and the arguments of the cycles field.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"{ __type(name: \"Team\") { fields { name args { name type { name kind ofType { name } } } } } }"}' | python3 -c "import json,sys; d=json.load(sys.stdin); [print(f['name'], [a['name'] for a in f['args']]) for f in d['data']['__type']['fields'] if f['name'] in ('cycles','issues','activeCycle')]"
Response: {"status": "success", "stdout": "activeCycle []\ncycles ['after', 'before', 'filter', 'first', 'includeArchived', 'last', 'orderBy']\nissues ['after', 'before', 'filter', 'first', 'includeArchived', 'includeSubTeams', 'last', 'orderBy']"}

#### Step 10
Reasoning: The cycles query with a `first` argument failed with "Cannot return null for non-nullable field CycleConnection.nodes". Strange — probably the `first` argument caused an error. Maybe the issue was that the `id` argument is expecting a different type, or there's an issue with the connection structure. Let me try without arguments, or try using includeArchived.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"query { team(id: \"85b7c228-c6be-481d-813b-7b7edd0f6b45\") { id name cycles { nodes { id name number isActive startsAt endsAt } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":null,\"errors\":[{\"message\":\"Cannot return null for non-nullable field CycleConnection.nodes.\",\"locations\":[{\"line\":1,\"column\":77}],\"path\":[\"team\",\"cycles\",\"nodes\"]}]}"}

#### Step 11
Reasoning: The cycles field is returning null. The cycles field might be deprecated, or cycles might need to be retrieved via a different method. Let me try the `cycles` query on the root. Let me check the root query's fields.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"{ __schema { queryType { fields { name } } } }"}' | python3 -c "import json,sys; d=json.load(sys.stdin); print([f['name'] for f in d['data']['__schema']['queryType']['fields']])"
Response: {"status": "success", "stdout": "['administrableTeams', 'agentActivities', 'agentActivity', 'agentSession', 'agentSessions', 'apiKeys', 'applicationInfo', 'applicationWithAuthorization', 'archivedTeams', 'attachment', 'attachmentSources', 'attachments', 'attachmentsForURL', 'auditEntries', 'auditEntryTypes', 'authenticationSessions', 'availableUsers', 'comment', 'comments', 'customView', 'customViewDetailsSuggestion', 'customViewHasSubscribers', 'customViews', 'customer', 'customerNeed', 'customerNeeds', 'customerStatus', 'customerStatuses', 'customerTier', 'customerTiers', 'customers', 'cycle', 'cycles', 'document', 'documentContentHistory', 'documents', 'emailIntakeAddress', 'emoji', 'emojis', 'entityExternalLink', 'externalUser', 'externalUsers', 'failuresForOauthWebhooks', 'favorite', 'favorites', 'fetchData', 'initiative', 'initiativeRelation', 'initiativeRelations', 'initiativeToProject', 'initiativeToProjects', 'initiativeUpdate', 'initiativeUpdates', 'initiatives', 'integration', 'integrationHasScopes', 'integrationTemplate', 'integrationTemplates', 'integrations', 'integrationsSettings', 'issue', 'issueFigmaFileKeySearch', 'issueFilterSuggestion', 'issueImportCheckCSV', 'issueImportCheckSync', 'issueImportJqlCheck', 'issueLabel', 'issueLabels', 'issuePriorityValues', 'issueRelation', 'issueRelations', 'issueSearch', 'issueTitleSuggestionFromCustomerRequest', 'issueVcsBranchSearch', 'issues', 'notification', 'notificationSubscription', 'notificationSubscriptions', 'notifications', 'notificationsUnreadCount', 'organization', 'organizationDomainClaimRequest', 'organizationExists', 'organizationInvite', 'organizationInviteDetails', 'organizationInvites', 'organizationMeta', 'project', 'projectFilterSuggestion', 'projectLabel', 'projectLabels', 'projectMilestone', 'projectMilestones', 'projectRelation', 'projectRelations', 'projectStatus', 'projectStatusProjectCount', 'projectStatuses', 'projectUpdate', 'projectUpdates', 'projects', 'pushSubscriptionTest', 'rateLimitStatus', 'searchDocuments', 'searchIssues', 'searchProjects', 'semanticSearch', 'ssoUrlFromEmail', 'summarizeProjectUpdates', 'team', 'teamMembership', 'teamMemberships', 'teams', 'template', 'templates', 'templatesForIntegration', 'timeSchedule', 'timeSchedules', 'triageResponsibilities', 'triageResponsibility', 'user', 'userSettings', 'users', 'verifyGitHubEnterpriseServerInstallation', 'viewer', 'webhook', 'webhooks', 'workflowState', 'workflowStates']"}

#### Step 12
Reasoning: There's a top-level `cycles` query. Let me try using it with a filter for team and number 7.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"{ __type(name: \"Query\") { fields { name args { name type { name kind ofType { name } } } } } }"}' | python3 -c "import json,sys; d=json.load(sys.stdin); [print(f['name'], [(a['name'], str(a['type'])) for a in f['args']]) for f in d['data']['__type']['fields'] if f['name'] in ('cycle','cycles')]"
Response: {"status": "success", "stdout": "cycle [('id', \"{'name': None, 'kind': 'NON_NULL', 'ofType': {'name': 'String'}}\")]\ncycles [('after', \"{'name': 'String', 'kind': 'SCALAR', 'ofType': None}\"), ('before', \"{'name': 'String', 'kind': 'SCALAR', 'ofType': None}\"), ('filter', \"{'name': 'CycleFilter', 'kind': 'INPUT_OBJECT', 'ofType': None}\"), ('first', \"{'name': 'Int', 'kind': 'SCALAR', 'ofType': None}\"), ('includeArchived', \"{'name': 'Boolean', 'kind': 'SCALAR', 'ofType': None}\"), ('last', \"{'name': 'Int', 'kind': 'SCALAR', 'ofType': None}\"), ('orderBy', \"{'name': 'PaginationOrderBy', 'kind': 'ENUM', 'ofType': None}\")]"}

#### Step 13
Reasoning: The `cycles` query exists on the Query root. The team-scoped cycles returned null — weird. Let me try the root-level cycles with a filter. CycleFilter — check its fields, e.g., number, team.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"{ __type(name: \"CycleFilter\") { inputFields { name type { name kind ofType { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"inputFields\":[{\"name\":\"and\",\"type\":{\"name\":null,\"kind\":\"LIST\",\"ofType\":{\"name\":null}}},{\"name\":\"completedAt\",\"type\":{\"name\":\"DateComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"createdAt\",\"type\":{\"name\":\"DateComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"endsAt\",\"type\":{\"name\":\"DateComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"id\",\"type\":{\"name\":\"IDComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"isActive\",\"type\":{\"name\":\"BooleanComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"isFuture\",\"type\":{\"name\":\"BooleanComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"isInCooldown\",\"type\":{\"name\":\"BooleanComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"isNext\",\"type\":{\"name\":\"BooleanComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"isPast\",\"type\":{\"name\":\"BooleanComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"isPrevious\",\"type\":{\"name\":\"BooleanComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"issues\",\"type\":{\"name\":\"IssueCollectionFilter\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"name\",\"type\":{\"name\":\"StringComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"number\",\"type\":{\"name\":\"NumberComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"or\",\"type\":{\"name\":null,\"kind\":\"LIST\",\"ofType\":{\"name\":null}}},{\"name\":\"startsAt\",\"type\":{\"name\":\"DateComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"team\",\"type\":{\"name\":\"TeamFilter\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"updatedAt\",\"type\":{\"name\":\"DateComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}}]}}}"}

#### Step 14
Reasoning: Let me try querying cycles with number eq 7.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"query { cycles(first: 50, filter: {number: {eq: 7}}) { nodes { id name number isActive team { id name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"cycles\":{\"nodes\":[{\"id\":\"b381fa35-df91-4e07-913e-c6490579fabd\",\"name\":\"Cycle 7\",\"number\":7.0,\"isActive\":false,\"team\":{\"id\":\"85b7c228-c6be-481d-813b-7b7edd0f6b45\",\"name\":\"App\"}}]}}}"}

#### Step 15
Reasoning: Next, I'll fetch the issues of Cycle 7, and find the issue titled "Checkout API timeout" that's assigned to Maya Chen.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"query { cycle(id: \"b381fa35-df91-4e07-913e-c6490579fabd\") { id name issues(first: 200) { nodes { id identifier title priority assignee { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":null,\"errors\":[{\"message\":\"Cannot return null for non-nullable field IssueConnection.nodes.\",\"locations\":[{\"line\":1,\"column\":90}],\"path\":[\"cycle\",\"issues\",\"nodes\"]}]}"}

#### Step 16
Reasoning: Same "cannot return null" error on the connection's nodes. Weird — the issues query worked at the top level. Probably a different argument is required. Let me check the arguments for Cycle.issues.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"{ __type(name: \"Cycle\") { fields { name args { name type { name kind ofType { name } } } } } }"}' | python3 -c "import json,sys; d=json.load(sys.stdin); [print(f['name'], [(a['name'], str(a['type'])) for a in f['args']]) for f in d['data']['__type']['fields'] if f['name']=='issues']"
Response: {"status": "success", "stdout": "issues [('after', \"{'name': 'String', 'kind': 'SCALAR', 'ofType': None}\"), ('before', \"{'name': 'String', 'kind': 'SCALAR', 'ofType': None}\"), ('filter', \"{'name': 'IssueFilter', 'kind': 'INPUT_OBJECT', 'ofType': None}\"), ('first', \"{'name': 'Int', 'kind': 'SCALAR', 'ofType': None}\"), ('includeArchived', \"{'name': 'Boolean', 'kind': 'SCALAR', 'ofType': None}\"), ('last', \"{'name': 'Int', 'kind': 'SCALAR', 'ofType': None}\"), ('orderBy', \"{'name': 'PaginationOrderBy', 'kind': 'ENUM', 'ofType': None}\")]"}

#### Step 17
Reasoning: The `issues` query on a cycle requires a filter (it's non-null). Let me try passing a filter.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"query { cycle(id: \"b381fa35-df91-4e07-913e-c6490579fabd\") { id name issues(first: 200, filter: {}) { nodes { id identifier title priority assignee { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":null,\"errors\":[{\"message\":\"Cannot return null for non-nullable field IssueConnection.nodes.\",\"locations\":[{\"line\":1,\"column\":102}],\"path\":[\"cycle\",\"issues\",\"nodes\"]}]}"}

#### Step 18
Reasoning: The cycle's issues field keeps failing. Maybe the issue connection needs includeArchived, or there's some problem with the connection. Let me try includeArchived: true.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"query { cycle(id: \"b381fa35-df91-4e07-913e-c6490579fabd\") { id name issues(first: 200, includeArchived: true) { nodes { id identifier title priority assignee { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":null,\"errors\":[{\"message\":\"Cannot return null for non-nullable field IssueConnection.nodes.\",\"locations\":[{\"line\":1,\"column\":113}],\"path\":[\"cycle\",\"issues\",\"nodes\"]}]}"}

#### Step 19
Reasoning: Hmm, I'm getting "Cannot return null for non-nullable field IssueConnection.nodes" — weird. Maybe the mock/proxy only supports certain queries. Let me try filtering issues by cycle:

Use issues(filter: {cycle: {id: {eq: ...}}}).
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"{ __type(name: \"IssueFilter\") { inputFields { name } } }"}' | python3 -c "import json,sys; d=json.load(sys.stdin); print([f['name'] for f in d['data']['__type']['inputFields']])"
Response: {"status": "success", "stdout": "['addedToCycleAt', 'addedToCyclePeriod', 'ageTime', 'and', 'archivedAt', 'assignee', 'attachments', 'autoArchivedAt', 'autoClosedAt', 'accumulatedStateUpdatedAt', 'canceledAt', 'children', 'comments', 'completedAt', 'createdAt', 'creator', 'customerCount', 'customerImportantCount', 'cycle', 'cycleTime', 'delegate', 'description', 'dueDate', 'estimate', 'hasBlockedByRelations', 'hasBlockingRelations', 'hasDuplicateRelations', 'hasSuggestedTeams', 'hasRelatedRelations', 'hasSuggestedAssignees', 'hasSuggestedLabels', 'hasSuggestedProjects', 'hasSuggestedRelatedIssues', 'hasSuggestedSimilarIssues', 'id', 'labels', 'lastAppliedTemplate', 'leadTime', 'needs', 'number', 'or', 'parent', 'priority', 'project', 'projectMilestone', 'reactions', 'recurringIssueTemplate', 'searchableContent', 'slaStatus', 'snoozedBy', 'snoozedUntilAt', 'sourceMetadata', 'startedAt', 'state', 'subscribers', 'suggestions', 'team', 'title', 'triageTime', 'triagedAt', 'updatedAt']"}

#### Step 20
Reasoning: The cycle's issues endpoint seems to have a weird null issue. Let me try querying issues with a cycle filter instead:

issues(filter: {cycle: {id: {eq: ...}}})
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"query { issues(first: 200, filter: {cycle: {id: {eq: \"b381fa35-df91-4e07-913e-c6490579fabd\"}}}) { nodes { id identifier title priority assignee { name } state { name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"bf72b7e2-38c8-4660-92c7-5a92432c194b\",\"identifier\":\"APP-5\",\"title\":\"Onboarding email copy\",\"priority\":0.0,\"assignee\":{\"name\":\"Leo Park\"},\"state\":{\"name\":\"Todo\"}},{\"id\":\"dbdc236c-714f-4f44-bea4-34a6340a90c3\",\"identifier\":\"APP-1\",\"title\":\"Checkout API timeouts under load\",\"priority\":0.0,\"assignee\":{\"name\":\"Maya Chen\"},\"state\":{\"name\":\"Todo\"}}]}}}"}

#### Step 21
Reasoning: The issue in cycle 7 assigned to Maya Chen is APP-1 (id: dbdc236c-714f-4f44-bea4-34a6340a90c3). Next, I'll update the priority to High (2).

Found it — APP-1 "Checkout API timeouts under load" is Maya Chen's issue in Cycle 7. Setting priority to High:
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"mutation { issueUpdate(id: \"dbdc236c-714f-4f44-bea4-34a6340a90c3\", input: {priority: 2}) { success issue { id identifier title priority } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issueUpdate\":{\"success\":true,\"issue\":{\"id\":\"dbdc236c-714f-4f44-bea4-34a6340a90c3\",\"identifier\":\"APP-1\",\"title\":\"Checkout API timeouts under load\",\"priority\":2.0}}}}"}

#### Step 22
Reasoning: Done. Confirming the priority mapping: in Linear, 0 = No Priority, 1 = Urgent, 2 = High, 3 = Medium, 4 = Low. Yep, 2 = High.

Done. Set **APP-1 — "Checkout API timeouts under load"** (assigned to Maya Chen, in Cycle 7) to **High** priority.

Note: there are other issues with the same title assigned to Maya (APP-2/3/4), but only APP-1 is in Cycle 7.
Command: 
Response: null

## Final answer
Done. Set **APP-1 — "Checkout API timeouts under load"** (assigned to Maya Chen, in Cycle 7) to **High** priority.

Note: there are other issues with the same title assigned to Maya (APP-2/3/4), but only APP-1 is in Cycle 7.

## State diff
- UPDATE issues `dbdc236c-714f-4f44-bea4-34a6340a90c3`: {"priorityLabel": ["No priority", "High"], "priority": [0.0, 2.0]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["dbdc236c-714f-4f44-bea4-34a6340a90c3"]}. Provisional outcome: correct. Provisional exposed facts: [].

Give your verdict for this trial.