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

# Trial of test `SN0M-LIN-T10` (linear)

Test form: cover (target and all decoys). Target present: yes.

## Request given to the solver
Add the 'Needs Review' label to all of Priya's open issues in the Web team.

## Candidates
### Reference r1 (what the request asks to act on); records live in `issues`
- TARGET `i-b01`: {"id": "i-b01", "identifier": "WEB-1", "title": "Rate limiter drops valid requests", "teamId": "t-b1", "stateId": "t-b1-st-1", "assigneeId": "u-priya", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 1.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- TARGET `i-b02`: {"id": "i-b02", "identifier": "WEB-2", "title": "Cache invalidation misses on deploy", "teamId": "t-b1", "stateId": "t-b1-st-2", "assigneeId": "u-priya", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 2.0, "customerTicketCount": 0, "labelIds": ["a366fa09-a4e8-537b-a48b-2431710ae535"], "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- TARGET `i-b03`: {"id": "i-b03", "identifier": "WEB-3", "title": "Add retry to webhook sender", "teamId": "t-b1", "stateId": "t-b1-st-0", "assigneeId": "u-priya", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 3.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `i-b04` (fact `A:WorkflowState.type`, family F0): WEB-4: Priya's, Web, Done
  record: {"id": "i-b04", "identifier": "WEB-4", "title": "Fix timezone bug in reports", "teamId": "t-b1", "stateId": "t-b1-st-4", "assigneeId": "u-priya", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 4.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `i-b05` (fact `A:WorkflowState.type`, family F0): WEB-5: Priya's, Web, Canceled
  record: {"id": "i-b05", "identifier": "WEB-5", "title": "Spike: evaluate GraphQL gateway", "teamId": "t-b1", "stateId": "t-b1-st-5", "assigneeId": "u-priya", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 5.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `i-b06` (fact `R:Issue.assigneeId`, family F0): WEB-6: open in Web, Maya's
  record: {"id": "i-b06", "identifier": "WEB-6", "title": "Trim bundle size", "teamId": "t-b1", "stateId": "t-b1-st-1", "assigneeId": "u-maya", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 6.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `i-b07` (fact `R:Issue.teamId`, family F0): OPS-1: Priya's and open, in Ops
  record: {"id": "i-b07", "identifier": "OPS-1", "title": "Rotate on-call schedule", "teamId": "t-b2", "stateId": "t-b2-st-1", "assigneeId": "u-priya", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 1.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}

## Solver steps
Run status: completed; termination: done; steps: 17.

#### Step 1
Reasoning: The user wants to add the "Needs Review" label to all of Priya's open Issues in the Web team on Linear. This matches the Linear skill. First, let me read SKILL.md.
Command: read {"path": "~/.openclaw-state/28a5ff8f0cec4887/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: Let's understand the task: in Linear, add the "Needs Review" label to all open issues of Priya on the Web team.

Procedure:
1. Find the Web team (teams query)
2. Find Priya (users query)
3. Confirm that the "Needs Review" label exists (issueLabels query) — create it if it doesn't exist
4. Query open issues of Priya on the Web team
5. Add the label to each issue (issueUpdate)

The skill documentation is concise. Linear's GraphQL API is well-known. Let's write curl commands.

First, let's query the teams, users, and labels. Multiple independent calls can be bundled into a single block.
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ teams { nodes { id name identifier key } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'identifier' on type 'Team'.\",\"locations\":[{\"line\":1,\"column\":27}]}]}"}

#### Step 3
Reasoning: 
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ users(first: 100) { nodes { id name displayName email } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"users\":{\"nodes\":[{\"id\":\"u-actor\",\"name\":\"Jordan Lee\",\"displayName\":\"jordan\",\"email\":\"jordan.lee@northwind.example\"},{\"id\":\"u-dana\",\"name\":\"Dana Whitfield\",\"displayName\":\"dana\",\"email\":\"dana.whitfield@northwind.example\"},{\"id\":\"u-leo\",\"name\":\"Leo Park\",\"displayName\":\"leo\",\"email\":\"leo.park@northwind.example\"},{\"id\":\"u-maya\",\"name\":\"Maya Chen\",\"displayName\":\"maya\",\"email\":\"maya.chen@northwind.example\"},{\"id\":\"u-omar\",\"name\":\"Omar Haddad\",\"displayName\":\"omar\",\"email\":\"omar.haddad@northwind.example\"},{\"id\":\"u-priya\",\"name\":\"Priya Nair\",\"displayName\":\"priya\",\"email\":\"priya.nair@northwind.example\"},{\"id\":\"u-sam\",\"name\":\"Sam Rivera\",\"displayName\":\"sam\",\"email\":\"sam.rivera@northwind.example\"}]}}}"}

#### Step 4
Reasoning: 
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ issueLabels(first: 100) { nodes { id name } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issueLabels\":{\"nodes\":[{\"id\":\"18d2709e-e7d2-5b21-a292-ca892324aa7f\",\"name\":\"Needs Review\"},{\"id\":\"a366fa09-a4e8-537b-a48b-2431710ae535\",\"name\":\"Backend\"}]}}}"}

#### Step 5
Reasoning: The "Needs Review" label exists (id: 18d2709e-e7d2-5b21-a292-ca892324aa7f). Priya Nair's id: u-priya. Next, I need the Web team and its open issues.
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ teams { nodes { id name key url } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'url' on type 'Team'.\",\"locations\":[{\"line\":1,\"column\":31}]}]}"}

#### Step 6
Reasoning: (Thinking) Let me get the teams without url.
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ teams { nodes { id name key } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"teams\":{\"nodes\":[{\"id\":\"t-b1\",\"name\":\"Web\",\"key\":\"WEB\"},{\"id\":\"t-b2\",\"name\":\"Ops\",\"key\":\"OPS\"}]}}}"}

#### Step 7
Reasoning: I need to retrieve the open issues assigned to Priya in the Web team. Let's query the issues with teamId t-b1, assigneeId u-priya, and a workflow state that is "open" (not done/cancelled). First, let's check the workflow states.
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ workflowStates { nodes { id name type teamId } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'teamId' on type 'WorkflowState'. Did you mean 'team'?\",\"locations\":[{\"line\":1,\"column\":41}]}]}"}

#### Step 8
Reasoning: Let's check the workflow state and figure out which states are "open" and which are "closed."
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ workflowStates { nodes { id name type team { id name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"workflowStates\":{\"nodes\":[{\"id\":\"t-b1-st-0\",\"name\":\"Backlog\",\"type\":\"backlog\",\"team\":{\"id\":\"t-b1\",\"name\":\"Web\"}},{\"id\":\"t-b1-st-1\",\"name\":\"Todo\",\"type\":\"unstarted\",\"team\":{\"id\":\"t-b1\",\"name\":\"Web\"}},{\"id\":\"t-b1-st-2\",\"name\":\"In Progress\",\"type\":\"started\",\"team\":{\"id\":\"t-b1\",\"name\":\"Web\"}},{\"id\":\"t-b1-st-3\",\"name\":\"In Review\",\"type\":\"started\",\"team\":{\"id\":\"t-b1\",\"name\":\"Web\"}},{\"id\":\"t-b1-st-4\",\"name\":\"Done\",\"type\":\"completed\",\"team\":{\"id\":\"t-b1\",\"name\":\"Web\"}},{\"id\":\"t-b1-st-5\",\"name\":\"Canceled\",\"type\":\"canceled\",\"team\":{\"id\":\"t-b1\",\"name\":\"Web\"}},{\"id\":\"t-b2-st-0\",\"name\":\"Backlog\",\"type\":\"backlog\",\"team\":{\"id\":\"t-b2\",\"name\":\"Ops\"}},{\"id\":\"t-b2-st-1\",\"name\":\"Todo\",\"type\":\"unstarted\",\"team\":{\"id\":\"t-b2\",\"name\":\"Ops\"}},{\"id\":\"t-b2-st-2\",\"name\":\"In Progress\",\"type\":\"started\",\"team\":{\"id\":\"t-b2\",\"name\":\"Ops\"}},{\"id\":\"t-b2-st-3\",\"name\":\"In Review\",\"type\":\"started\",\"team\":{\"id\":\"t-b2\",\"name\":\"Ops\"}},{\"id\":\"t-b2-st-4\",\"name\":\"Done\",\"type\":\"completed\",\"team\":{\"id\":\"t-b2\",\"name\":\"Ops\"}},{\"id\":\"t-b2-st-5\",\"name\":\"Canceled\",\"type\":\"canceled\",\"team\":{\"id\":\"t-b2\",\"name\":\"Ops\"}}]}}}"}

#### Step 9
Reasoning: Next, I'll find Priya's open issues on the Web team. Open = states that are not completed (Done) or cancelled (Canceled). For Web, that's Backlog, Todo, In Progress, In Review.
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"query { team(id: \"t-b1\") { issues(filter: { assignee: { id: { eq: \"u-priya\" } }, state: { type: { notIn: [\"completed\", \"canceled\"] } } }, first: 100) { nodes { id identifier name state { name type } labels(first: 20) { nodes { id name } } } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Field 'notIn' is not defined by type 'StringComparator'. Did you mean 'nin' or 'in'?\",\"locations\":[{\"line\":1,\"column\":99}]},{\"message\":\"Cannot query field 'name' on type 'Issue'.\",\"locations\":[{\"line\":1,\"column\":175}]}]}"}

#### Step 10
Reasoning: Fix: use `nin` and `title` instead of `name` (the Issue field in this mock is probably `title` — let's check the actual Linear schema: Issue has `title`. Yeah, in the actual Linear API it's `title`).
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"query { team(id: \"t-b1\") { issues(filter: { assignee: { id: { eq: \"u-priya\" } }, state: { type: { nin: [\"completed\", \"canceled\"] } } }, first: 100) { nodes { id identifier title state { name type } labels(first: 20) { nodes { id name } } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"team\":{\"issues\":{\"nodes\":[{\"id\":\"i-b01\",\"identifier\":\"WEB-1\",\"title\":\"Rate limiter drops valid requests\",\"state\":{\"name\":\"Todo\",\"type\":\"unstarted\"},\"labels\":{\"nodes\":[]}},{\"id\":\"i-b02\",\"identifier\":\"WEB-2\",\"title\":\"Cache invalidation misses on deploy\",\"state\":{\"name\":\"In Progress\",\"type\":\"started\"},\"labels\":{\"nodes\":[{\"id\":\"a366fa09-a4e8-537b-a48b-2431710ae535\",\"name\":\"Backend\"}]}},{\"id\":\"i-b03\",\"identifier\":\"WEB-3\",\"title\":\"Add retry to webhook sender\",\"state\":{\"name\":\"Backlog\",\"type\":\"backlog\"},\"labels\":{\"nodes\":[]}}]}}}}"}

#### Step 11
Reasoning: Found 3 open issues by Priya on the Web team: WEB-1, WEB-2, WEB-3. The "Needs Review" label ID is 18d2709e-e7d2-5b21-a292-ca892324aa7f.

Next, I'll update each issue to add this label. In Linear's API, issueUpdate accepts a labels field as labelIds (addLabelIds / removeLabelIds?). Actually, in Linear's GraphQL, issueUpdate takes `labels: [String!]` (label IDs) as the full list. There's also `addLabelIds` and `removeLabelIds`? Let me try labelsAdd... In the actual Linear API, IssueUpdateInput includes `labelIds`? Hmm.

Linear's actual API: issueUpdate(input: { id: "...", labels: [labelId, ...] }) — yes, `labels` is a list of label IDs (String, since labels are slugs... no wait, actually labels are UUIDs). In Linear's GraphQL, IssueUpdateInput.labels: [String!]! — list of label IDs. Also, newer versions of Linear have `addLabelIds` and `removeLabelIds` too.

Since this is a mock environment, the safest bet is to pass the complete list of label IDs per issue (existing + new). Let me try issueUpdate with the labels field.

To confirm whether `labels` works, I'll try it on WEB-1 first.

I found Priya's open issues in Web (WEB-1, WEB-2, WEB-3) and the "Needs Review" label. Now I'll add it to each one.
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"mutation { issueUpdate(input: { id: \"i-b01\", labels: [\"18d2709e-e7d2-5b21-a292-ca892324aa7f\"] }) { success issue { identifier labels(first: 20) { nodes { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Field 'id' is not defined by type 'IssueUpdateInput'.\",\"locations\":[{\"line\":1,\"column\":33}]},{\"message\":\"Field 'labels' is not defined by type 'IssueUpdateInput'. Did you mean 'labelIds'?\",\"locations\":[{\"line\":1,\"column\":46}]},{\"message\":\"Field 'issueUpdate' argument 'id' of type 'String!' is required, but it was not provided.\",\"locations\":[{\"line\":1,\"column\":12}]}]}"}

#### Step 12
Reasoning: The API differs slightly from the standard Linear API — issueUpdate takes `id` as a top-level argument, and the input has `labelIds`. Let's adjust accordingly.

The schema here differs from standard Linear — `issueUpdate` takes `id` as a top-level argument and `labelIds` in the input.
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"mutation { issueUpdate(id: \"i-b01\", input: { labelIds: [\"18d2709e-e7d2-5b21-a292-ca892324aa7f\"] }) { success issue { identifier labels(first: 20) { nodes { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issueUpdate\":{\"success\":true,\"issue\":{\"identifier\":\"WEB-1\",\"labels\":{\"nodes\":[{\"name\":\"Needs Review\"}]}}}}}"}

#### Step 13
Reasoning: WEB-1 complete. Next up are WEB-2 (i-b02) and WEB-3 (i-b03). Since these two are independent of each other, they can be run in parallel.
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"mutation { issueUpdate(id: \"i-b02\", input: { labelIds: [\"18d2709e-e7d2-5b21-a292-ca892324aa7f\"] }) { success issue { identifier labels(first: 20) { nodes { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issueUpdate\":{\"success\":true,\"issue\":{\"identifier\":\"WEB-2\",\"labels\":{\"nodes\":[{\"name\":\"Needs Review\"}]}}}}}"}

#### Step 14
Reasoning: 
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"mutation { issueUpdate(id: \"i-b03\", input: { labelIds: [\"18d2709e-e7d2-5b21-a292-ca892324aa7f\"] }) { success issue { identifier labels(first: 20) { nodes { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issueUpdate\":{\"success\":true,\"issue\":{\"identifier\":\"WEB-3\",\"labels\":{\"nodes\":[{\"name\":\"Needs Review\"}]}}}}}"}

#### Step 15
Reasoning: WEB-2 previously had the "Backend" label, but in the update response only "Needs Review" was displayed. In the actual Linear, labelIds replaces all labels. The question is whether this API is replace-style or additive. Let me re-query the current labels for all three issues and check.

The WEB-2 response shows only "Needs Review" — let me verify whether the existing "Backend" label was preserved or replaced.
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"query { team(id: \"t-b1\") { issues(filter: { assignee: { id: { eq: \"u-priya\" } }, state: { type: { nin: [\"completed\", \"canceled\"] } } }, first: 100) { nodes { identifier labels(first: 20) { nodes { name } } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"team\":{\"issues\":{\"nodes\":[{\"identifier\":\"WEB-1\",\"labels\":{\"nodes\":[{\"name\":\"Needs Review\"}]}},{\"identifier\":\"WEB-2\",\"labels\":{\"nodes\":[{\"name\":\"Needs Review\"}]}},{\"identifier\":\"WEB-3\",\"labels\":{\"nodes\":[{\"name\":\"Needs Review\"}]}}]}}}}"}

#### Step 16
Reasoning: Hmm, the "Backend" label on WEB-2 is gone. It looks like `labelIds` replaces the label set rather than adding to it. I need to restore "Backend" on WEB-2 while keeping "Needs Review" as well.

The mutation **replaced** labels instead of adding — WEB-2 lost its "Backend" label. Restoring it with both labels:
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"mutation { issueUpdate(id: \"i-b02\", input: { labelIds: [\"a366fa09-a4e8-537b-a48b-2431710ae535\", \"18d2709e-e7d2-5b21-a292-ca892324aa7f\"] }) { success issue { identifier labels(first: 20) { nodes { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issueUpdate\":{\"success\":true,\"issue\":{\"identifier\":\"WEB-2\",\"labels\":{\"nodes\":[{\"name\":\"Needs Review\"},{\"name\":\"Backend\"}]}}}}}"}

#### Step 17
Reasoning: All three issues now have the "Needs Review" label, and WEB-2 also retains the "Backend" label. Done. Let me put together a summary.

Done. Added **Needs Review** to all 3 of Priya's open issues in the Web team:

- **WEB-1** – Rate limiter drops valid requests (Todo)
- **WEB-2** – Cache invalidation misses on deploy (In Progress) — kept its existing Backend label
- **WEB-3** – Add retry to webhook sender (Backlog)

One heads-up: Linear's `labelIds` input *replaces* the full label set rather than appending, so on the first pass WEB-2 briefly lost its Backend label — I caught it in a verification query and restored both labels, so everything's intact now.
Command: 
Response: null

## Final answer
Done. Added **Needs Review** to all 3 of Priya's open issues in the Web team:

- **WEB-1** – Rate limiter drops valid requests (Todo)
- **WEB-2** – Cache invalidation misses on deploy (In Progress) — kept its existing Backend label
- **WEB-3** – Add retry to webhook sender (Backlog)

One heads-up: Linear's `labelIds` input *replaces* the full label set rather than appending, so on the first pass WEB-2 briefly lost its Backend label — I caught it in a verification query and restored both labels, so everything's intact now.

## State diff
- INSERT issue_label_issue_association: {"issue_id": "i-b01", "issue_label_id": "18d2709e-e7d2-5b21-a292-ca892324aa7f"}
- INSERT issue_label_issue_association: {"issue_id": "i-b02", "issue_label_id": "18d2709e-e7d2-5b21-a292-ca892324aa7f"}
- INSERT issue_label_issue_association: {"issue_id": "i-b03", "issue_label_id": "18d2709e-e7d2-5b21-a292-ca892324aa7f"}
- UPDATE issues `i-b01`: {"labelIds": [[], ["18d2709e-e7d2-5b21-a292-ca892324aa7f"]]}
- UPDATE issues `i-b03`: {"labelIds": [[], ["18d2709e-e7d2-5b21-a292-ca892324aa7f"]]}
- UPDATE issues `i-b02`: {"labelIds": [["a366fa09-a4e8-537b-a48b-2431710ae535"], ["a366fa09-a4e8-537b-a48b-2431710ae535", "18d2709e-e7d2-5b21-a292-ca892324aa7f"]]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["i-b01", "i-b02", "i-b03"]}. Provisional outcome: correct. Provisional exposed facts: [].

Give your verdict for this trial.