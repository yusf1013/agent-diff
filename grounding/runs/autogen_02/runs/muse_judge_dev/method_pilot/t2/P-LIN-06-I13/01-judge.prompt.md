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

# Trial of test `P-LIN-06-I13` (linear)

Test form: probe. Target present: no.

## Request given to the solver
Which active admins are owners of the Design team itself (not its sub-teams)? Just list their names. If there aren't any, just tell me.

## Candidates
### Reference r1 (another record the request names); records live in `users`
- No target: no record meets this reference.
- DECOY `u-mia` (fact `A:TeamMembership.owner`): Mia is a Design member, not an owner.
  record: {"id": "u-mia", "email": "mia.wong@northwind.example", "name": "Mia Wong", "displayName": "mia", "organizationId": "org-northwind", "active": true, "admin": true, "app": false, "avatarBackgroundColor": "#3B82F6", "canAccessAnyPublicTeam": true, "createdAt": "2025-01-01T00:00:00", "updatedAt": "2025-01-01T00:00:00", "createdIssueCount": 0, "guest": false, "initials": "MW", "isAssignable": true, "isMe": false, "isMentionable": true, "lastSeen": "2025-01-01T00:00:00", "timezone": "America/Los_Angeles"}

## Solver steps
Run status: completed; termination: done; steps: 12.

#### Step 1
Reasoning: I need to find the Design team first, then identify its owners who are active admins. Let me start by querying all teams to find the Design team.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ teams { nodes { id name identifier parent { id name } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'identifier' on type 'Team'.\",\"locations\":[{\"line\":1,\"column\":27}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_1548dfa81e7c4153a68122a27be98548_mf4yybh1"}

#### Step 2
Reasoning: 
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ teams { nodes { id name parent { id name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"teams\":{\"nodes\":[{\"id\":\"t-des\",\"name\":\"Design\",\"parent\":null},{\"id\":\"t-dsy\",\"name\":\"Design Systems\",\"parent\":{\"id\":\"t-des\",\"name\":\"Design\"}},{\"id\":\"t-web\",\"name\":\"Web\",\"parent\":null}]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_1548dfa81e7c4153a68122a27be98548_mf4yybh1"}

#### Step 3
Reasoning: I found the Design team with id "t-des". Now I need to find the members of this team specifically, check their role (owner), and whether they are active admins. Let me query the team's members with their permissions and user info.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ team(id: \"t-des\") { id name members { nodes { permission role user { id name active isAdmin } } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'permission' on type 'User'.\",\"locations\":[{\"line\":1,\"column\":49}]},{\"message\":\"Cannot query field 'role' on type 'User'.\",\"locations\":[{\"line\":1,\"column\":60}]},{\"message\":\"Cannot query field 'user' on type 'User'.\",\"locations\":[{\"line\":1,\"column\":65}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_1548dfa81e7c4153a68122a27be98548_mf4yybh1"}

#### Step 4
Reasoning: 
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ team(id: \"t-des\") { id name members { nodes { id name active isAdmin } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'isAdmin' on type 'User'. Did you mean 'admin'?\",\"locations\":[{\"line\":1,\"column\":64}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_1548dfa81e7c4153a68122a27be98548_mf4yybh1"}

#### Step 5
Reasoning: 
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ team(id: \"t-des\") { id name members { nodes { id name active admin } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"team\":{\"id\":\"t-des\",\"name\":\"Design\",\"members\":{\"nodes\":[{\"id\":\"u-mia\",\"name\":\"Mia Wong\",\"active\":true,\"admin\":true}]}}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_1548dfa81e7c4153a68122a27be98548_mf4yybh1"}

#### Step 6
Reasoning: 
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ team(id: \"t-des\") { id name members { nodes { id name active admin } } } teamMemberships { nodes { team { id name } user { id name active admin } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"team\":{\"id\":\"t-des\",\"name\":\"Design\",\"members\":{\"nodes\":[{\"id\":\"u-mia\",\"name\":\"Mia Wong\",\"active\":true,\"admin\":true}]}},\"teamMemberships\":{\"nodes\":[{\"team\":{\"id\":\"t-des\",\"name\":\"Design\"},\"user\":{\"id\":\"u-mia\",\"name\":\"Mia Wong\",\"active\":true,\"admin\":true}}]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_1548dfa81e7c4153a68122a27be98548_mf4yybh1"}

#### Step 7
Reasoning: 
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ __type(name: \"Team\") { fields { name } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"fields\":[{\"name\":\"activeCycle\"},{\"name\":\"aiThreadSummariesEnabled\"},{\"name\":\"archivedAt\"},{\"name\":\"autoArchivePeriod\"},{\"name\":\"autoCloseChildIssues\"},{\"name\":\"autoCloseParentIssues\"},{\"name\":\"autoClosePeriod\"},{\"name\":\"autoCloseStateId\"},{\"name\":\"children\"},{\"name\":\"color\"},{\"name\":\"createdAt\"},{\"name\":\"currentProgress\"},{\"name\":\"cycleCalenderUrl\"},{\"name\":\"cycleCooldownTime\"},{\"name\":\"cycleDuration\"},{\"name\":\"cycleIssueAutoAssignCompleted\"},{\"name\":\"cycleIssueAutoAssignStarted\"},{\"name\":\"cycleLockToActive\"},{\"name\":\"cycleStartDay\"},{\"name\":\"cycles\"},{\"name\":\"cyclesEnabled\"},{\"name\":\"defaultIssueEstimate\"},{\"name\":\"defaultIssueState\"},{\"name\":\"defaultProjectTemplate\"},{\"name\":\"defaultTemplateForMembers\"},{\"name\":\"defaultTemplateForNonMembers\"},{\"name\":\"description\"},{\"name\":\"displayName\"},{\"name\":\"facets\"},{\"name\":\"gitAutomationStates\"},{\"name\":\"groupIssueHistory\"},{\"name\":\"icon\"},{\"name\":\"id\"},{\"name\":\"inheritIssueEstimation\"},{\"name\":\"inheritWorkflowStatuses\"},{\"name\":\"integrationsSettings\"},{\"name\":\"inviteHash\"},{\"name\":\"issueCount\"},{\"name\":\"issueEstimationAllowZero\"},{\"name\":\"issueEstimationExtended\"},{\"name\":\"issueEstimationType\"},{\"name\":\"issues\"},{\"name\":\"joinByDefault\"},{\"name\":\"key\"},{\"name\":\"labels\"},{\"name\":\"markedAsDuplicateWorkflowState\"},{\"name\":\"members\"},{\"name\":\"membership\"},{\"name\":\"memberships\"},{\"name\":\"name\"},{\"name\":\"organization\"},{\"name\":\"parent\"},{\"name\":\"posts\"},{\"name\":\"private\"},{\"name\":\"progressHistory\"},{\"name\":\"projects\"},{\"name\":\"requirePriorityToLeaveTriage\"},{\"name\":\"scimGroupName\"},{\"name\":\"scimManaged\"},{\"name\":\"setIssueSortOrderOnStateChange\"},{\"name\":\"states\"},{\"name\":\"templates\"},{\"name\":\"timezone\"},{\"name\":\"triageEnabled\"},{\"name\":\"triageIssueState\"},{\"name\":\"triageResponsibility\"},{\"name\":\"upcomingCycleCount\"},{\"name\":\"updatedAt\"},{\"name\":\"webhooks\"}]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_1548dfa81e7c4153a68122a27be98548_mf4yybh1"}

#### Step 8
Reasoning: 
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ __type(name: \"Team\") { fields { name type { name kind ofType { name } } } } }"}' | python3 -c "
import json, sys
data = json.load(sys.stdin)
for f in data['data']['__type']['fields']:
    if f['name'] in ['members', 'memberships', 'membership']:
        print(f['name'], f['type'])
"
Response: {"status": "success", "stdout": "members {'name': None, 'kind': 'NON_NULL', 'ofType': {'name': 'UserConnection'}}\nmembership {'name': 'TeamMembership', 'kind': 'OBJECT', 'ofType': None}\nmemberships {'name': None, 'kind': 'NON_NULL', 'ofType': {'name': 'TeamMembershipConnection'}}\n", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_1548dfa81e7c4153a68122a27be98548_mf4yybh1"}

#### Step 9
Reasoning: 
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ __type(name: \"TeamMembership\") { fields { name type { name kind ofType { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"fields\":[{\"name\":\"archivedAt\",\"type\":{\"name\":\"DateTime\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"createdAt\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"DateTime\"}}},{\"name\":\"id\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"ID\"}}},{\"name\":\"owner\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"Boolean\"}}},{\"name\":\"sortOrder\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"Float\"}}},{\"name\":\"team\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"Team\"}}},{\"name\":\"updatedAt\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"DateTime\"}}},{\"name\":\"user\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"User\"}}}]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_1548dfa81e7c4153a68122a27be98548_mf4yybh1"}

#### Step 10
Reasoning: 
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ team(id: \"t-des\") { id name memberships { nodes { id owner user { id name active admin } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":null,\"errors\":[{\"message\":\"Cannot return null for non-nullable field TeamMembershipConnection.nodes.\",\"locations\":[{\"line\":1,\"column\":45}],\"path\":[\"team\",\"memberships\",\"nodes\"]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_1548dfa81e7c4153a68122a27be98548_mf4yybh1"}

#### Step 11
Reasoning: 
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ teamMemberships { nodes { id owner team { id name } user { id name active admin } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"teamMemberships\":{\"nodes\":[{\"id\":\"tm-t-des-mia\",\"owner\":false,\"team\":{\"id\":\"t-des\",\"name\":\"Design\"},\"user\":{\"id\":\"u-mia\",\"name\":\"Mia Wong\",\"active\":true,\"admin\":true}}]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_1548dfa81e7c4153a68122a27be98548_mf4yybh1"}

#### Step 12
Reasoning: I queried all team memberships and found that the only membership for the Design team (t-des) is Mia Wong, who has `owner: false`. Although she is active and an admin, she is not an owner of the Design team. There are no other memberships for this team. So there are no active admins who are owners of the Design team itself.


<done>
There are no active admins who are owners of the Design team itself. The only member of the Design team is Mia Wong (active admin), but she is not an owner of that team.
</done>
Command: 
Response: null

## Final answer
There are no active admins who are owners of the Design team itself. The only member of the Design team is Mia Wong (active admin), but she is not an owner of that team.

## State diff
(no changes)

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["u-mia"]}. Provisional outcome: incorrect. Provisional exposed facts: ['A:TeamMembership.owner'].

Give your verdict for this trial.