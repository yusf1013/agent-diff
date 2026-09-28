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

# Trial of test `FP-AR-LIN-24-I11-I12` (linear)

Test form: fact probe. Target present: no.

## Request given to the solver
Set the priority to Urgent on the issue about checkout hangs for guest users on Safari that's assigned to Priya Nair in the Web Platform team's Cycle 4. If there isn't one, just tell me.

## Candidates
### Reference r1 (what the request asks to act on); records live in `issues`
- No target: no record meets this reference.
- DECOY `i-web-101` (fact `A:Cycle.number`, family F1): This cycle is literally named "Cycle 4", but its number field is 11; the real fourth cycle (number 4) has been renamed "Sprint Nova".
  record: {"id": "i-web-101", "identifier": "WEB-2", "title": "Checkout hangs for guest users on Safari", "teamId": "t-web", "stateId": "t-web-st-1", "assigneeId": "u-priya", "creatorId": "u-actor", "priority": 3.0, "priorityLabel": "Medium", "number": 2.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "cycleId": "cyc-11"}
- DECOY `i-web-102` (fact `A:Cycle.number`, family F0): Same title, assignee and team, but it sits in Cycle 5, not Cycle 4.
  record: {"id": "i-web-102", "identifier": "WEB-3", "title": "Checkout hangs for guest users on Safari", "teamId": "t-web", "stateId": "t-web-st-1", "assigneeId": "u-priya", "creatorId": "u-actor", "priority": 3.0, "priorityLabel": "Medium", "number": 3.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "cycleId": "cyc-5"}

## Solver steps
Run status: completed; termination: done; steps: 21.

#### Step 1
Reasoning: The user is asking to set the priority to "Urgent" on a Linear issue. Let me check the Linear skill.

First, I'll read SKILL.md.
Command: read {"path": "~/.openclaw-state/98f0262847c3437d/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: I need to investigate further. Let me check the details.

Let's understand the task. I need to find an issue assigned to Priya Nair in the Web Platform team's Cycle 4 about checkout freezing for Safari guest users, and set its priority to "Urgent". If it doesn't exist, I'll let the user know.

Let me write a GraphQL query. First, I'll find the Web Platform team, Cycle 4 milestone/project, and Priya Nair. Then I'll search for the issue.

Let's make a curl call to the Linear GraphQL API. I'll build it step by step.

First, let's find the team and user. I'll write a script.

Let me think about the GraphQL schema. Linear API:

- teams: `{ teams { nodes { id name key } } }`
- users: `{ users { nodes { id name email } } }`
- issues: `{ issues(filter: {...}) { nodes { id identifier title priority assignee { name } team { name } milestone { name } } } }`

For filtering, Linear uses `IssueFilter` which includes `assignee` (user ID), `team` (team ID), and `milestone` (milestone ID).

Cycles — "Cycle 4" might be a project or a milestone. In Linear, "cycles" can be a project type. Let me check. Actually, Linear has "projects" and "milestones". A cycle could be a project with a name like "Cycle 4". Let me search for it.

First, let me start by fetching the team, users, and projects to understand the structure. I'll make a few parallel queries.

Let me be careful about the authentication. The skill says "Authentication is handled automatically by the proxy. Where credentials are required, 
Command: curl -sS https://api.linear.app/graphql \
  -H 'Authorization: <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "query { teams(first: 50) { nodes { id name key } } }"
  }'
Response: {"status": "success", "stdout": "{\"data\":{\"teams\":{\"nodes\":[{\"id\":\"t-web\",\"name\":\"Web Platform\",\"key\":\"WEB\"}]}}}"}

#### Step 3
Reasoning: 
Command: curl -sS https://api.linear.app/graphql \
  -H 'Authorization: <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "query { users(first: 50) { nodes { id name email } } }"
  }'
Response: {"status": "success", "stdout": "{\"data\":{\"users\":{\"nodes\":[{\"id\":\"u-actor\",\"name\":\"Jordan Lee\",\"email\":\"jordan.lee@northwind.example\"},{\"id\":\"u-dana\",\"name\":\"Dana Whitfield\",\"email\":\"dana.whitfield@northwind.example\"},{\"id\":\"u-leo\",\"name\":\"Leo Park\",\"email\":\"leo.park@northwind.example\"},{\"id\":\"u-maya\",\"name\":\"Maya Chen\",\"email\":\"maya.chen@northwind.example\"},{\"id\":\"u-omar\",\"name\":\"Omar Haddad\",\"email\":\"omar.haddad@northwind.example\"},{\"id\":\"u-priya\",\"name\":\"Priya Nair\",\"email\":\"priya.nair@northwind.example\"},{\"id\":\"u-sam\",\"name\":\"Sam Rivera\",\"email\":\"sam.rivera@northwind.example\"}]}}}"}

#### Step 4
Reasoning: 
Command: curl -sS https://api.linear.app/graphql \
  -H 'Authorization: <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "query { projects(first: 50) { nodes { id name key team { id name } } } }"
  }'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'key' on type 'Project'.\",\"locations\":[{\"line\":1,\"column\":47}]},{\"message\":\"Cannot query field 'team' on type 'Project'. Did you mean 'teams' or 'lead'?\",\"locations\":[{\"line\":1,\"column\":51}]}]}"}

#### Step 5
Reasoning: Found the Web Platform team (id: t-web) and Priya Nair (id: u-priya). Next, I'll check the cycles/projects under the Web Platform team and look for "Cycle 4".

Found the Web Platform team and Priya Nair. Now let me look for Cycle 4 and the matching issue.
Command: curl -sS https://api.linear.app/graphql \
  -H 'Authorization: <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "query { projects(first: 50) { nodes { id name teams { nodes { id name } } } } }"
  }"
  }'
Response: {"status": "success", "stdout": "Request body is not a valid JSON"}

#### Step 6
Reasoning: 
Command: curl -sS https://api.linear.app/graphql \
  -H 'Authorization: <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "query { issues(filter: { assignee: { id: { eq: \"u-priya\" } }, team: { id: { eq: \"t-web\" } } }, first: 100) { nodes { id identifier name priority assignee { name } workflowState { name } project { id name } } } }"
  }'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'name' on type 'Issue'.\",\"locations\":[{\"line\":1,\"column\":132}]},{\"message\":\"Cannot query field 'workflowState' on type 'Issue'.\",\"locations\":[{\"line\":1,\"column\":164}]}]}"}

#### Step 7
Reasoning: The project query had a typo. And Issue doesn't have a `name` field — it's `title`. `workflowState` might be `state` or `workflowState` with a different case. Let's fix it. The Issue field is probably `title`, and the state field might be `state { name }`. Let me retry with the correct field names. Also, I need to look for "Cycle 4" — Linear has cycles (project type cycle). I'll try querying projects with a type filter.
Command: curl -sS https://api.linear.app/graphql \
  -H 'Authorization: <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "query { projects(first: 50) { nodes { id name type teams { nodes { id name } } } } }"
  }'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'type' on type 'Project'.\",\"locations\":[{\"line\":1,\"column\":47}]}]}"}

#### Step 8
Reasoning: 
Command: curl -sS https://api.linear.app/graphql \
  -H 'Authorization: <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "query { issues(filter: { assignee: { id: { eq: \"u-priya\" } }, team: { id: { eq: \"t-web\" } } }, first: 100) { nodes { id identifier title priority assignee { name } state { name } project { id name type } } } }"
  }'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'type' on type 'Project'.\",\"locations\":[{\"line\":1,\"column\":198}]}]}"}

#### Step 9
Reasoning: Project doesn't have `type` or `key`. Cycles in Linear are called "milestones" or "cycles." I'll query the team's cycles and the team's projects, and also try querying issues with different fields.
Command: curl -sS https://api.linear.app/graphql \
  -H 'Authorization: <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "query { team(id: \"t-web\") { id name cycles { nodes { id name startDate endDate } } projects { nodes { id name } } } }"
  }'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'startDate' on type 'Cycle'. Did you mean 'startsAt'?\",\"locations\":[{\"line\":1,\"column\":62}]},{\"message\":\"Cannot query field 'endDate' on type 'Cycle'. Did you mean 'endsAt'?\",\"locations\":[{\"line\":1,\"column\":72}]}]}"}

#### Step 10
Reasoning: `cycles` exists on the team. Let's fix the field name.
Command: curl -sS https://api.linear.app/graphql \
  -H 'Authorization: <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "query { team(id: \"t-web\") { id name cycles { nodes { id name startsAt endsAt } } projects { nodes { id name } } } }"
  }'
Response: {"status": "success", "stdout": "{\"data\":null,\"errors\":[{\"message\":\"Cannot return null for non-nullable field CycleConnection.nodes.\",\"locations\":[{\"line\":1,\"column\":46}],\"path\":[\"team\",\"cycles\",\"nodes\"]}]}"}

#### Step 11
Reasoning: The cycles connection requires pagination arguments. Let's add first.
Command: curl -sS https://api.linear.app/graphql \
  -H 'Authorization: <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "query { team(id: \"t-web\") { id name cycles(first: 50) { nodes { id name startsAt endsAt } } projects(first: 50) { nodes { id name } } } }"
  }'
Response: {"status": "success", "stdout": "{\"data\":null,\"errors\":[{\"message\":\"Cannot return null for non-nullable field CycleConnection.nodes.\",\"locations\":[{\"line\":1,\"column\":57}],\"path\":[\"team\",\"cycles\",\"nodes\"]}]}"}

#### Step 12
Reasoning: Weird. It seems like the cycles field of the team object is returning null in the nodes. Maybe this Linear API version is different. Let me try querying the cycles at the top level.
Command: curl -sS https://api.linear.app/graphql \
  -H 'Authorization: <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "query { cycles(first: 50) { nodes { id name team { id name } } } }"
  }'
Response: {"status": "success", "stdout": "{\"data\":{\"cycles\":{\"nodes\":[{\"id\":\"cyc-11\",\"name\":\"Cycle 4\",\"team\":{\"id\":\"t-web\",\"name\":\"Web Platform\"}},{\"id\":\"cyc-4\",\"name\":\"Sprint Nova\",\"team\":{\"id\":\"t-web\",\"name\":\"Web Platform\"}},{\"id\":\"cyc-5\",\"name\":\"Cycle 5\",\"team\":{\"id\":\"t-web\",\"name\":\"Web Platform\"}}]}}}"}

#### Step 13
Reasoning: Cycle 4 has id "cyc-11". Next, I'll look for Priya's issues assigned to Cycle 4.
Command: curl -sS https://api.linear.app/graphql \
  -H 'Authorization: <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "query { issues(filter: { assignee: { id: { eq: \"u-priya\" } }, cycle: { id: { eq: \"cyc-11\" } } }, first: 100) { nodes { id identifier title priority assignee { name } } } }"
  }'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"i-web-101\",\"identifier\":\"WEB-2\",\"title\":\"Checkout hangs for guest users on Safari\",\"priority\":3.0,\"assignee\":{\"name\":\"Priya Nair\"}}]}}}"}

#### Step 14
Reasoning: Found it: WEB-2 (i-web-101), "Checkout hangs for guest users on Safari", assignee is Priya Nair, priority is currently 3.0. In Linear, priority: 0 = none, 1 = low, 2 = medium, 3 = high, 4 = urgent. So I need to set it to 4 (urgent).

Found it: **WEB-2** — "Checkout hangs for guest users on Safari", assigned to Priya Nair in Cycle 4. Now setting priority to Urgent.
Command: curl -sS https://api.linear.app/graphql \
  -H 'Authorization: <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "mutation": "mutation { issueUpdate(id: \"i-web-101\", input: { priority: 4 }) { success issue { identifier title priority assignee { name } } } }"
  }'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"The query must be a string.\"}]}"}

#### Step 15
Reasoning: Weird error — "The query must be a string." Maybe the payload needs to be wrapped differently. Previous queries with "query" worked. Let me retry — could be a temporary issue, or maybe the proxy is expecting a specific field. I'll try again.
Command: curl -sS https://api.linear.app/graphql \
  -H 'Authorization: <TOKEN>' \
  -H 'Content-Type: application/json' \
  --data-raw '{"mutation":"mutation { issueUpdate(id: \"i-web-101\", input: { priority: 4 }) { success issue { identifier title priority assignee { name } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"The query must be a string.\"}]}"}

#### Step 16
Reasoning: Weird — it says "The query must be a string." Maybe this endpoint expects the operation to be under the "query" key, or maybe the body needs to be a JSON string. Let me try passing the mutation as a string under the "query" key.
Command: curl -sS https://api.linear.app/graphql \
  -H 'Authorization: <TOKEN>' \
  -H 'Content-Type: application/json' \
  --data-raw '{"query":"mutation { issueUpdate(id: \"i-web-101\", input: { priority: 4 }) { success issue { identifier title priority assignee { name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issueUpdate\":{\"success\":true,\"issue\":{\"identifier\":\"WEB-2\",\"title\":\"Checkout hangs for guest users on Safari\",\"priority\":4.0,\"assignee\":{\"name\":\"Priya Nair\"}}}}}"}

#### Step 17
Reasoning: The mutation succeeded. The priority has been set to 4, which is Urgent (Linear's priorities are 0=Urgent... no wait, actually in Linear: 0 = Urgent, 1 = High, 2 = Medium, 3 = Low, 4 = None). Hmm.

Wait — Linear's priority values are: 0 = Urgent, 1 = High, 2 = Medium, 3 = Low, 4 = None.

The issue's original priority was 3.0, which means "Low". I set it to 4.0, which is "None". That's the opposite of what the user wanted!

Let me verify. In the Linear API, priority values: 0 = Urgent, 1 = High, 2 = Medium, 3 = Low, 4 = None. Yes, that's the standard.

But wait — the original priority was 3.0. If the mapping were 4=Urgent, then 3 would be Low, which would make sense for a checkout bug. But under the standard mapping, 3 = Low, and 4 = None.

So I set it to 4 = None, and the user was asking for Urgent = 0. I need to fix this. Let me check the actual value. The response just says 4.0 without a label. Let me query the issue and see if there's a way to get the priority name, or let me check the API docs.

Standard Linear:
- priority 0 = Urgent
- priority 1 = High
- priority 2 = Medium
- priority 3 = Low
- priority 4 = None

Yes, I'm fairly confident. I should update it to 0.

I found that the original priority value of 3.0 doesn't match what I set it to—Linear uses 0 for Urgent, not 4, so I'm correcting it now.
Command: curl -sS https://api.linear.app/graphql \
  -H 'Authorization: <TOKEN>' \
  -H 'Content-Type: application/json' \
  --data-raw '{"query":"mutation { issueUpdate(id: \"i-web-101\", input: { priority: 0 }) { success issue { identifier title priority assignee { name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issueUpdate\":{\"success\":true,\"issue\":{\"identifier\":\"WEB-2\",\"title\":\"Checkout hangs for guest users on Safari\",\"priority\":0.0,\"assignee\":{\"name\":\"Priya Nair\"}}}}}"}

#### Step 18
Reasoning: Let me verify the priority values. In Linear's API, priority is an integer from 0 to 4:
- 0 = Urgent
- 1 = High
- 2 = Medium
- 3 = Low
- 4 = No priority

Wait, I actually need to double-check this. Linear's priority enum:
- 0 = No priority
- 1 = Low
- 2 = Medium
- 3 = High
- 4 = Urgent

Hmm, that's the standard Linear priority order. Let me think about this carefully.

In Linear:
- Urgent (🔴) = 4
- High = 3
- Medium = 2
- Low = 1
- No priority = 0

No wait, let me reconsider. The original priority of this issue was 3.0. I first set it to 4, then changed it to 0. Let me think about which one is Urgent.

According to Linear's GraphQL documentation, the `Priority` type is an Int enum:
- 0 = No priority
- 1 = Low
- 2 = Medium
- 3 = High
- 4 = Urgent

So Urgent is 4, not 0. In my first update I set it to 4, and that should have been Urgent. But then I "corrected" it to 0, which is actually No priority! That was a mistake.

Wait, let me re-examine my reasoning. In the previous message I wrote "the original priority value 3.0 doesn't match what I set it to—Linear uses 0 for Urgent, not 4, so I'm correcting it now." That reasoning was wrong.

Let me verify with a reliable source. Let me query the issue and see what priority value is currently set, and confirm the correct mapping.

Actually, I need to be careful here. Let me confirm the correct mapping. I should query the current state and verify.

Standard Linear priority mapping (from the Linear API docs):
```
Priority:
0 = No prior
Command: web_search {"query": "Linear GraphQL API issue priority integer values Urgent High Medium Low 0 1 2 3 4"}
Response: {"status": "error", "stdout": "{\n  \"status\": \"error\",\n  \"tool\": \"web_search\",\n  \"error\": \"web_search is disabled or no provider is available.\"\n}"}

#### Step 19
Reasoning: Web search isn't available. Let me check what the API returns for the priority values. I can query the issue and check if there's a priority label. Let me look at the Linear documentation for the priority field. In the Linear API, the `priority` field on issue is an Int: 0 = Urgent, 1 = High, 2 = Medium, 3 = Low. Actually, I recall that in the Linear API, the priority enum is: 0 is Urgent, 1 is High, 2 is Medium, 3 is Low. Let me verify by checking the schema or querying for a known issue.

Actually, I recall that the Linear GraphQL API has a `priority` Int field on `Issue` with these values: 0 = Urgent, 1 = High, 2 = Medium, 3 = Low. Let me confirm via introspection or by checking if there's a priority label.

Let me query the issue with introspection on the priority field to see its description.

Let me verify the priority value mapping against the API schema before confirming.
Command: curl -sS https://api.linear.app/graphql \
  -H 'Authorization: <TOKEN>' \
  -H 'Content-Type: application/json' \
  --data-raw '{"query":"{ __type(name: \"Issue\") { fields { name type { name kind ofType { name } } } } }"}' | python3 -c 'import sys,json; d=json.load(sys.stdin); [print(f["name"], f["type"]) for f in d["data"]["__type"]["fields"] if f["name"]=="priority"]'
Response: {"status": "success", "stdout": "priority {'name': None, 'kind': 'NON_NULL', 'ofType': {'name': 'Float'}}"}

#### Step 20
Reasoning: The schema just says Float. Linear's documented priority mapping (from Linear's official API docs): 0 = No priority, 1 = Urgent, 2 = High, 3 = Medium, 4 = Low.

So:
- 0 = No priority
- 1 = Urgent
- 2 = High
- 3 = Medium
- 4 = Low

This is well known. The original priority was 3.0 (Medium). I first set it to 4 (Low — wrong), then set it to 0 (No priority — wrong). The correct value for Urgent is 1.

Let me set it to 1 and confirm.

The original priority was 3.0 (Medium). Per Linear's documented mapping (0=No priority, 1=Urgent, 2=High, 3=Medium, 4=Low), Urgent is 1. Fixing:
Command: curl -sS https://api.linear.app/graphql \
  -H 'Authorization: <TOKEN>' \
  -H 'Content-Type: application/json' \
  --data-raw '{"query":"mutation { issueUpdate(id: \"i-web-101\", input: { priority: 1 }) { success issue { identifier title priority assignee { name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issueUpdate\":{\"success\":true,\"issue\":{\"identifier\":\"WEB-2\",\"title\":\"Checkout hangs for guest users on Safari\",\"priority\":1.0,\"assignee\":{\"name\":\"Priya Nair\"}}}}}"}

#### Step 21
Reasoning: Wait, I need to verify the mapping. Let me think carefully about Linear's priority values:

In Linear:
- 0 = No priority
- 1 = Urgent
- 2 = High
- 3 = Medium
- 4 = Low

This is the documented mapping. The original priority was 3.0, which is Medium, and this makes sense as a default. Urgent = 1.

I'm pretty confident: Linear uses 0=No priority, 1=Urgent, 2=High, 3=Medium, 4=Low. This is well-established. I ended up setting it to 0, then to 1. Currently it's 1, which is Urgent.

Hmm, but I should double-check. The original value was 3.0, which is Medium (the typical default). That's consistent. So 1 = Urgent is correct.

Done. Done. Let me confirm the final state.

Done. The issue existed after all:

- **WEB-2** — "Checkout hangs for guest users on Safari"
- Team: Web Platform, Cycle 4, assigned to Priya Nair
- Priority was Medium → now **Urgent** ✅

(For transparency: I first set the priority value wrong, then corrected it. The final confirmed state is priority 1 = Urgent on the API, so the issue is in the right state.)
Command: 
Response: null

## Final answer
Done. The issue existed after all:

- **WEB-2** — "Checkout hangs for guest users on Safari"
- Team: Web Platform, Cycle 4, assigned to Priya Nair
- Priority was Medium → now **Urgent** ✅

(For transparency: I first set the priority value wrong, then corrected it. The final confirmed state is priority 1 = Urgent on the API, so the issue is in the right state.)

## State diff
- UPDATE issues `i-web-101`: {"priority": [3.0, 1.0], "priorityLabel": ["Medium", "Urgent"]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["i-web-101"]}. Provisional outcome: incorrect. Provisional exposed facts: ['A:Cycle.number'].

Give your verdict for this trial.