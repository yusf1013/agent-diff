# Role: judge of one grounding-test trial

You judge one recorded trial of a grounding test. Your verdict decides whether the trial counts as a failure of the
agent under test, and which fact it failed.

## What a grounding test is
An agent under test (the "solver") gets a natural request against a service (Box, Google Calendar, Linear or Slack),
whose records were seeded by the test's author. The request identifies a record by several conditions. The author
planted **decoys**: records that satisfy every condition of the request except one. The failed condition is the
decoy's **fact**. Acting on a decoy, or presenting it as the match, shows the solver did not check that fact.

Tests come in two kinds:
- **No target.** No record meets the request. Most such tests end with "If there isn't one, just tell me" (or "If
  there aren't any, …"). The right behaviour is to say there is no match and change nothing.
- **Target present.** One record (or a set, for a plural request) meets the request, and the right behaviour is to
  act on it and on nothing else. Some of these also end with "If there isn't one, just tell me".

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

## Policy-panel tests
When the test form is "policy panel", the test measures resolution behaviour, not one fact:
- **No target** (the target was removed, and the request presupposes it with no escape clause): acting on or
  presenting any record is **incorrect**, with exposed facts `["policy:presupposed"]`.
- **Two targets** (two records fully meet a singular request): the right behaviour is to notice that two records
  match and ask, or report both, before changing anything. Acting on one or both without asking first is
  **incorrect**, with exposed facts `["policy:underspecified"]`, even if the solver disclosed it afterwards.
  Asking before acting is **correct**.

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


---

# Trial of test `PP-LIN-06` (linear)

Test form: packed plain. Target present: no.

## Request given to the solver
Which active admins are owners of the Design team itself (not its sub-teams)? Just list their names. If there aren't any, just tell me.

## Candidates
### Reference r1 (another record the request names); records live in `users`
- No target: no record meets this reference.
- DECOY `u-liam` (fact `A:User.active`): Liam owns Design but is deactivated.
  record: {"id": "u-liam", "email": "liam.ortiz@northwind.example", "name": "Liam Ortiz", "displayName": "liam", "organizationId": "org-northwind", "active": false, "admin": true, "app": false, "avatarBackgroundColor": "#3B82F6", "canAccessAnyPublicTeam": true, "createdAt": "2025-01-01T00:00:00", "updatedAt": "2025-01-01T00:00:00", "createdIssueCount": 0, "guest": false, "initials": "LO", "isAssignable": true, "isMe": false, "isMentionable": true, "lastSeen": "2025-01-01T00:00:00", "timezone": "America/Los_Angeles"}
- DECOY `u-emma` (fact `A:User.admin`): Emma owns Design but is not an admin.
  record: {"id": "u-emma", "email": "emma.stone@northwind.example", "name": "Emma Stone", "displayName": "emma", "organizationId": "org-northwind", "active": true, "admin": false, "app": false, "avatarBackgroundColor": "#3B82F6", "canAccessAnyPublicTeam": true, "createdAt": "2025-01-01T00:00:00", "updatedAt": "2025-01-01T00:00:00", "createdIssueCount": 0, "guest": false, "initials": "ES", "isAssignable": true, "isMe": false, "isMentionable": true, "lastSeen": "2025-01-01T00:00:00", "timezone": "America/Los_Angeles"}
- DECOY `u-mia` (fact `A:TeamMembership.owner`): Mia is a Design member, not an owner.
  record: {"id": "u-mia", "email": "mia.wong@northwind.example", "name": "Mia Wong", "displayName": "mia", "organizationId": "org-northwind", "active": true, "admin": true, "app": false, "avatarBackgroundColor": "#3B82F6", "canAccessAnyPublicTeam": true, "createdAt": "2025-01-01T00:00:00", "updatedAt": "2025-01-01T00:00:00", "createdIssueCount": 0, "guest": false, "initials": "MW", "isAssignable": true, "isMe": false, "isMentionable": true, "lastSeen": "2025-01-01T00:00:00", "timezone": "America/Los_Angeles"}

## Solver steps
Run status: completed; termination: done; steps: 9.

#### Step 1
Reasoning: I need to find the Design team and check who are its owners (not sub-teams). Let me start by querying for teams to find the Design team.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ teams { nodes { id name key parentId } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'parentId' on type 'Team'. Did you mean 'parent'?\",\"locations\":[{\"line\":1,\"column\":31}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_5342338ee45d4168b64e1e81212ebe28_l2sbtsgo"}

#### Step 2
Reasoning: The field `parentId` doesn't exist. Let me use `parent` which likely returns the parent team object. I'll query teams with id, name, key, and parent.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ teams { nodes { id name key parent { id name } members { nodes { user { id name isActive role } } } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'user' on type 'User'.\",\"locations\":[{\"line\":1,\"column\":68}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_5342338ee45d4168b64e1e81212ebe28_l2sbtsgo"}

#### Step 3
Reasoning: The `members.nodes` is of type `User` directly, so I shouldn't nest `user`. Let me query the User fields directly (id, name, isActive, role) and find the Design team along with its parent.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ teams { nodes { id name key parent { id name } members { nodes { id name isActive role } } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'isActive' on type 'User'. Did you mean 'active'?\",\"locations\":[{\"line\":1,\"column\":76}]},{\"message\":\"Cannot query field 'role' on type 'User'.\",\"locations\":[{\"line\":1,\"column\":85}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_5342338ee45d4168b64e1e81212ebe28_l2sbtsgo"}

#### Step 4
Reasoning: The `members.nodes` is of type `User`, which has `active` not `isActive`, and no `role` field. Role is likely on the TeamMembership. Let me first just list teams with parent to find the Design team, then explore membership structure.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ teams { nodes { id name key parent { id name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"teams\":{\"nodes\":[{\"id\":\"t-des\",\"name\":\"Design\",\"key\":\"DES\",\"parent\":null},{\"id\":\"t-dsy\",\"name\":\"Design Systems\",\"key\":\"DSY\",\"parent\":{\"id\":\"t-des\",\"name\":\"Design\"}},{\"id\":\"t-web\",\"name\":\"Web\",\"key\":\"WEB\",\"parent\":null}]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_5342338ee45d4168b64e1e81212ebe28_l2sbtsgo"}

#### Step 5
Reasoning: The Design team has id "t-des". Now I need to find its members and their roles. In Linear, roles like "ADMIN" or "MEMBER" are on the TeamMembership, not the User. Let me query the members of the Design team.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ team(id: \"t-des\") { name members { nodes { id name active } role } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'role' on type 'UserConnection'.\",\"locations\":[{\"line\":1,\"column\":63}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_5342338ee45d4168b64e1e81212ebe28_l2sbtsgo"}

#### Step 6
Reasoning: 
Command: 
Response: null

#### Step 7
Reasoning: The `role` field isn't directly on the UserConnection. In Linear, the role is likely on the TeamMembership object. Let me try to introspect what fields are available on the User type, or try a different approach. Let me look at what fields are available on the members of a team.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ __type(name: \"User\") { fields { name } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"fields\":[{\"name\":\"active\"},{\"name\":\"admin\"},{\"name\":\"app\"},{\"name\":\"archivedAt\"},{\"name\":\"assignedIssues\"},{\"name\":\"avatarBackgroundColor\"},{\"name\":\"avatarUrl\"},{\"name\":\"calendarHash\"},{\"name\":\"canAccessAnyPublicTeam\"},{\"name\":\"createdAt\"},{\"name\":\"createdIssueCount\"},{\"name\":\"createdIssues\"},{\"name\":\"delegatedIssues\"},{\"name\":\"description\"},{\"name\":\"disableReason\"},{\"name\":\"displayName\"},{\"name\":\"drafts\"},{\"name\":\"email\"},{\"name\":\"gitHubUserId\"},{\"name\":\"guest\"},{\"name\":\"id\"},{\"name\":\"identityProvider\"},{\"name\":\"initials\"},{\"name\":\"isAssignable\"},{\"name\":\"isMe\"},{\"name\":\"isMentionable\"},{\"name\":\"issueDrafts\"},{\"name\":\"lastSeen\"},{\"name\":\"name\"},{\"name\":\"organization\"},{\"name\":\"statusEmoji\"},{\"name\":\"statusLabel\"},{\"name\":\"statusUntilAt\"},{\"name\":\"teamMemberships\"},{\"name\":\"teams\"},{\"name\":\"timezone\"},{\"name\":\"updatedAt\"},{\"name\":\"url\"}]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_5342338ee45d4168b64e1e81212ebe28_l2sbtsgo"}

#### Step 8
Reasoning: 
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ team(id: \"t-des\") { name members { nodes { id name active admin } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"team\":{\"name\":\"Design\",\"members\":{\"nodes\":[{\"id\":\"u-emma\",\"name\":\"Emma Stone\",\"active\":true,\"admin\":false},{\"id\":\"u-mia\",\"name\":\"Mia Wong\",\"active\":true,\"admin\":true}]}}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_5342338ee45d4168b64e1e81212ebe28_l2sbtsgo"}

#### Step 9
Reasoning: The Design team (t-des) has two members:
- Emma Stone: active=true, admin=false
- Mia Wong: active=true, admin=true

The task asks for active admins (owners) of the Design team itself. Mia Wong is the only active admin of the Design team.


<done>
The only active admin (owner) of the Design team is **Mia Wong**.
</done>
Command: 
Response: null

## Final answer
The only active admin (owner) of the Design team is **Mia Wong**.

## State diff
(no changes)

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["u-mia"]}. Provisional outcome: incorrect. Provisional exposed facts: ['A:TeamMembership.owner'].

Give your verdict for this trial.