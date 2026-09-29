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

# Trial of test `U-AP-LIN-01-Issue_stateId` (linear)

Test form: underspecified (several records fully meet the singular request; each is listed as TARGET). Target present: yes.

## Request given to the solver
Set the priority to Urgent for the issue that's assigned to Priya Nair, whose description mentions the rollback window, and that was completed on October 2, 2026.

## Candidates
### Reference r1 (what the request asks to act on); records live in `issues`
- TARGET `41e3da93-1653-4be4-b6b1-e6b213fd3d59`: {"id": "41e3da93-1653-4be4-b6b1-e6b213fd3d59", "identifier": "WEB-1", "title": "Payment migration incident follow-up", "description": "Coordinate the rollback window with on-call before merging.", "teamId": "ba6aeb52-ba5c-455f-aed4-08afd4c1dbb1", "stateId": "0751b226-fad8-45ac-9d04-43e493b9665f", "assigneeId": "26c40f55-5898-44ad-b687-0d877908d789", "creatorId": "u-actor", "priority": 3.0, "priorityLabel": "Medium", "number": 1.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "dueDate": "2026-09-29", "completedAt": "2026-10-02T16:00:00"}
- TARGET `2e02d1b1-cf00-4674-ba0a-57e6923ee25f`: {"id": "2e02d1b1-cf00-4674-ba0a-57e6923ee25f", "identifier": "MOB-1", "title": "Mobile payment rollback check", "description": "Coordinate the rollback window with on-call before merging.", "teamId": "678afdf1-a436-4d2b-9215-2cc14cfbdcc4", "stateId": "c62d2112-c2a4-428b-b3c6-ce51fdc1e358", "assigneeId": "26c40f55-5898-44ad-b687-0d877908d789", "creatorId": "u-actor", "priority": 3.0, "priorityLabel": "Medium", "number": 1.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "dueDate": "2026-09-29", "completedAt": "2026-10-02T16:00:00"}
- DECOY `2c60973b-0c85-4f1b-aef1-652a20895b4f` (fact `A:Issue.description`, family F1): The rollback window is named in the title, but the issue's own description doesn't mention it.
  record: {"id": "2c60973b-0c85-4f1b-aef1-652a20895b4f", "identifier": "WEB-2", "title": "Plan the rollback window for payment migration", "description": "Confirm with support before deployment.", "teamId": "ba6aeb52-ba5c-455f-aed4-08afd4c1dbb1", "stateId": "0751b226-fad8-45ac-9d04-43e493b9665f", "assigneeId": "26c40f55-5898-44ad-b687-0d877908d789", "creatorId": "u-actor", "priority": 3.0, "priorityLabel": "Medium", "number": 2.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "dueDate": "2026-09-29", "completedAt": "2026-10-02T16:00:00"}
- DECOY `c8e43ad6-9cb1-4895-a303-48a63ebe6d95` (fact `A:Issue.description`, family F2): A comment on the issue mentions the rollback window; the issue's own description doesn't.
  record: {"id": "c8e43ad6-9cb1-4895-a303-48a63ebe6d95", "identifier": "WEB-3", "title": "Payment migration verification", "description": "Follow the standard release checklist.", "teamId": "ba6aeb52-ba5c-455f-aed4-08afd4c1dbb1", "stateId": "0751b226-fad8-45ac-9d04-43e493b9665f", "assigneeId": "26c40f55-5898-44ad-b687-0d877908d789", "creatorId": "u-actor", "priority": 3.0, "priorityLabel": "Medium", "number": 3.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "dueDate": "2026-09-29", "completedAt": "2026-10-02T16:00:00"}
- DECOY `edc6b722-fc21-42fa-90b5-e2469159709e` (fact `A:Issue.completedAt`, family F1): Its due date is October 2, but it was actually completed on September 20.
  record: {"id": "edc6b722-fc21-42fa-90b5-e2469159709e", "identifier": "WEB-4", "title": "Payment migration follow-up (tracking)", "description": "Coordinate the rollback window with on-call before merging.", "teamId": "ba6aeb52-ba5c-455f-aed4-08afd4c1dbb1", "stateId": "0751b226-fad8-45ac-9d04-43e493b9665f", "assigneeId": "26c40f55-5898-44ad-b687-0d877908d789", "creatorId": "u-actor", "priority": 3.0, "priorityLabel": "Medium", "number": 4.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "dueDate": "2026-10-02", "completedAt": "2026-09-20T10:00:00"}
- DECOY `8fa08f54-ebe6-4332-b661-50b2ef737df0` (fact `A:Issue.completedAt`, family F7): It was completed on October 1, one day before the requested date.
  record: {"id": "8fa08f54-ebe6-4332-b661-50b2ef737df0", "identifier": "WEB-5", "title": "Payment migration follow-up (early close)", "description": "Coordinate the rollback window with on-call before merging.", "teamId": "ba6aeb52-ba5c-455f-aed4-08afd4c1dbb1", "stateId": "0751b226-fad8-45ac-9d04-43e493b9665f", "assigneeId": "26c40f55-5898-44ad-b687-0d877908d789", "creatorId": "u-actor", "priority": 3.0, "priorityLabel": "Medium", "number": 5.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "dueDate": "2026-09-29", "completedAt": "2026-10-01T16:00:00"}

## Solver steps
Run status: completed; termination: done; steps: 7.

#### Step 1
Reasoning: The user wants me to set the priority of a specific issue in Linear to Urgent. I need to use the Linear skill. First, let me read the SKILL.md file for Linear.

Let's start by reading the Linear skill.

I'll use the Linear skill for this. Let me read the instructions first.
Command: read {"path": "~/.openclaw-state/4aec60557b3949a2/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: The SKILL.md is somewhat sparse on the GraphQL schema details, but I can work with the Linear GraphQL API. I need to search for an issue that meets the following conditions:
1. Assigned to Priya Nair
2. Description contains "rollback window"
3. Completed on October 2, 2026

First, let me find the user ID for Priya Nair. After that, I'll search for the issue.

Let me construct the GraphQL query. First, find Priya Nair:

```graphql
{
  users(includeDisabled: false) {
    nodes {
      id
      name
      email
    }
  }
}
```

Next, search for issues assigned to her whose descriptions mention the rollback window. The Linear API supports filtering:

```graphql
{
  issues(filter: { assignee: { id: { eq: "..." } }, description: { contains: "rollback window" } }) {
    nodes {
      id
      identifier
      title
      description
      completedAt
      priority
      priorityName
    }
  }
}
```

Linear's filter syntax for description is `contains` (case-insensitive, I think — actually the `contains` filter in Linear is case-insensitive).

"Completed on October 2, 2026" — I need to check `completedAt` on that date. Let me query and filter client-side.

Authentication: "Authentication is handled automatically via the proxy. Use a placeholder token like `<TOKEN>` where credentials would be placed." So, I should use a placeholder token in the Authorization header... hmm, that's odd. The instructions say to use a placeholder token where credentials would be placed. Probably the prox
Command: curl -s https://api.linear.app/graphql -H "Authorization: <TOKEN>" -H "Content-Type: application/json" -d '{"query":"{ users { nodes { id name email } } }"}' | head -c 3000
Response: {"status": "success", "stdout": "{\"data\":{\"users\":{\"nodes\":[{\"id\":\"1202ec90-8dd7-4828-8736-7d8838f9d302\",\"name\":\"Omar Haddad\",\"email\":\"omar.haddad@northwind.example\"},{\"id\":\"25dfbc80-42f5-4ba6-a75a-493bfda8cbbd\",\"name\":\"Leo Park\",\"email\":\"leo.park@northwind.example\"},{\"id\":\"26c40f55-5898-44ad-b687-0d877908d789\",\"name\":\"Priya Nair\",\"email\":\"priya.nair@northwind.example\"},{\"id\":\"76cabae6-771c-4e38-986f-3146965dd7b5\",\"name\":\"Maya Chen\",\"email\":\"maya.chen@northwind.example\"},{\"id\":\"b60dd912-ca9e-4435-b150-14567d71f2f7\",\"name\":\"Dana Whitfield\",\"email\":\"dana.whitfield@northwind.example\"},{\"id\":\"c72484b7-786c-485e-913a-d2312d788a44\",\"name\":\"Sam Rivera\",\"email\":\"sam.rivera@northwind.example\"},{\"id\":\"u-actor\",\"name\":\"Jordan Lee\",\"email\":\"jordan.lee@northwind.example\"}]}}}"}

#### Step 3
Reasoning: Priya Nair's user ID: 26c40f55-5898-44ad-b687-0d877908d789

Next, I'll search for issues assigned to her whose description mentions "rollback window" and were completed on October 2, 2026. I'll query the issues filtered by assignee, and then check the description and the completion date (completedAt).
Command: curl -s https://api.linear.app/graphql -H "Authorization: <TOKEN>" -H "Content-Type: application/json" -d '{"query":"{ issues(filter: { assignee: { id: { eq: \"26c40f55-5898-44ad-b687-0d877908d789\" } }) { nodes { id identifier name description completedAt priority state { name workflowStateType } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Syntax Error: Expected Name, found ')'.\",\"locations\":[{\"line\":1,\"column\":84}]}]}"}

#### Step 4
Reasoning: Syntax error — probably caused by my filter syntax. Linear's GraphQL filters for assignee use `assignee: { id: { eq: ... } }`. Hmm, column 84 is around `)`... Actually, the query is: `{ issues(filter: { assignee: { id: { eq: "..." } }) { nodes ...` — I closed the filter with `})` instead of `}}`. Let me count: `filter: { assignee: { id: { eq: "..." } })` — the `id` object is closed with `}`, then the `assignee` object is closed with `}`, and then the filter needs another `}`. I wrote `})` after the eq object — meaning I closed id and assignee, but the filter's closing brace is missing. The correct form should be: `filter: { assignee: { id: { eq: "..." } } }`.

Let me fix this.

Syntax error in my filter closing. Fixing:
Command: curl -s https://api.linear.app/graphql -H "Authorization: <TOKEN>" -H "Content-Type: application/json" -d '{"query":"{ issues(filter: { assignee: { id: { eq: \"26c40f55-5898-44ad-b687-0d877908d789\" } } }) { nodes { id identifier name description completedAt priority state { name workflowStateType } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'name' on type 'Issue'.\",\"locations\":[{\"line\":1,\"column\":112}]},{\"message\":\"Cannot query field 'workflowStateType' on type 'WorkflowState'.\",\"locations\":[{\"line\":1,\"column\":163}]}]}"}

#### Step 5
Reasoning: The `name` field doesn't exist on Issue — probably `title`. And WorkflowState might have `type` instead of `workflowStateType`. Let's fix it.
Command: curl -s https://api.linear.app/graphql -H "Authorization: <TOKEN>" -H "Content-Type: application/json" -d '{"query":"{ issues(filter: { assignee: { id: { eq: \"26c40f55-5898-44ad-b687-0d877908d789\" } } }) { nodes { id identifier title description completedAt priority state { name type } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"2c60973b-0c85-4f1b-aef1-652a20895b4f\",\"identifier\":\"WEB-2\",\"title\":\"Plan the rollback window for payment migration\",\"description\":\"Confirm with support before deployment.\",\"completedAt\":\"2026-10-02T16:00:00\",\"priority\":3.0,\"state\":{\"name\":\"Done\",\"type\":\"completed\"}},{\"id\":\"2e02d1b1-cf00-4674-ba0a-57e6923ee25f\",\"identifier\":\"MOB-1\",\"title\":\"Mobile payment rollback check\",\"description\":\"Coordinate the rollback window with on-call before merging.\",\"completedAt\":\"2026-10-02T16:00:00\",\"priority\":3.0,\"state\":{\"name\":\"Done\",\"type\":\"completed\"}},{\"id\":\"41e3da93-1653-4be4-b6b1-e6b213fd3d59\",\"identifier\":\"WEB-1\",\"title\":\"Payment migration incident follow-up\",\"description\":\"Coordinate the rollback window with on-call before merging.\",\"completedAt\":\"2026-10-02T16:00:00\",\"priority\":3.0,\"state\":{\"name\":\"Done\",\"type\":\"completed\"}},{\"id\":\"498931f1-7e09-433f-a080-035642a84dd6\",\"identifier\":\"WEB-7\",\"title\":\"Rollback window check\",\"description\":\"Mentions the rollback window here too, still pending completion.\",\"completedAt\":null,\"priority\":3.0,\"state\":{\"name\":\"In Review\",\"type\":\"started\"}},{\"id\":\"8fa08f54-ebe6-4332-b661-50b2ef737df0\",\"identifier\":\"WEB-5\",\"title\":\"Payment migration follow-up (early close)\",\"description\":\"Coordinate the rollback window with on-call before merging.\",\"completedAt\":\"2026-10-01T16:00:00\",\"priority\":3.0,\"state\":{\"name\":\"Done\",\"type\":\"completed\"}},{\"id\":\"c8e43ad6-9cb1-4895-a303-48a63ebe6d95\",\"identifier\":\"WEB-3\",\"title\":\"Payment migration verification\",\"description\":\"Follow the standard release checklist.\",\"completedAt\":\"2026-10-02T16:00:00\",\"priority\":3.0,\"state\":{\"name\":\"Done\",\"type\":\"completed\"}},{\"id\":\"edc6b722-fc21-42fa-90b5-e2469159709e\",\"identifier\":\"WEB-4\",\"title\":\"Payment migration follow-up (tracking)\",\"description\":\"Coordinate the rollback window with on-call before merging.\",\"completedAt\":\"2026-09-20T10:00:00\",\"priority\":3.0,\"state\":{\"name\":\"Done\",\"type\":\"completed\"}}]}}}"}

#### Step 6
Reasoning: There are multiple candidate issues:

1. WEB-2: "Plan the rollback window for payment migration" — description "Confirm with support before deployment." completedAt 2026-10-02. Hmm, the *title* mentions rollback window, but the description doesn't.
2. MOB-1: "Mobile payment rollback check" — description "Coordinate the rollback window with on-call before merging." completedAt 2026-10-02 ✓ description mentions rollback window ✓
3. WEB-1: "Payment migration incident follow-up" — description "Coordinate the rollback window with on-call before merging." completedAt 2026-10-02 ✓ description mentions rollback window ✓
4. WEB-7: "Rollback window check" — description mentions rollback window but completedAt is null (not completed).
5. WEB-5: completedAt 2026-10-01 — wrong date.
6. WEB-3: completed on 10-02 but description "Follow the standard release checklist." — no mention of rollback window.
7. WEB-4: completed 2026-09-20 — wrong date.

So, there are multiple issues that match "assigned to Priya, description mentions rollback window, completed on October 2": WEB-2 (no — description doesn't mention it), MOB-1, WEB-1. WEB-5 (wrong date), WEB-3 (no mention in description), WEB-4 (wrong date).

Hmm, both MOB-1 and WEB-1 have the description "Coordinate the rollback window with on-call before merging." and completedAt of 2026-10-02T16:00:00.

So there are two candidates: MOB-1 and WEB-1. The user said "the issue" (singular), so maybe there's a more distinguishing factor. Let me check —
Command: curl -s https://api.linear.app/graphql -H "Authorization: <TOKEN>" -H "Content-Type: application/json" -d '{"query":"{ a: issue(id: \"2e02d1b1-cf00-4674-ba0a-57e6923ee25f\") { identifier title description completedAt createdAt updatedAt team { key name } labels { nodes { name } } } b: issue(id: \"41e3da93-1653-4be4-b6b1-e6b213fd3d59\") { identifier title description completedAt createdAt updatedAt team { key name } labels { nodes { name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"a\":{\"identifier\":\"MOB-1\",\"title\":\"Mobile payment rollback check\",\"description\":\"Coordinate the rollback window with on-call before merging.\",\"completedAt\":\"2026-10-02T16:00:00\",\"createdAt\":\"2026-06-01T09:00:00\",\"updatedAt\":\"2026-06-01T09:00:00\",\"team\":{\"key\":\"MOB\",\"name\":\"Mobile\"},\"labels\":{\"nodes\":[]}},\"b\":{\"identifier\":\"WEB-1\",\"title\":\"Payment migration incident follow-up\",\"description\":\"Coordinate the rollback window with on-call before merging.\",\"completedAt\":\"2026-10-02T16:00:00\",\"createdAt\":\"2026-06-01T09:00:00\",\"updatedAt\":\"2026-06-01T09:00:00\",\"team\":{\"key\":\"WEB\",\"name\":\"Web\"},\"labels\":{\"nodes\":[]}}}}"}

#### Step 7
Reasoning: Both issues meet all the criteria perfectly and are identical (except for the team). The user's statement is "the issue," so it should be singular, but there are two. Let me reconsider:

- WEB-2: "Plan the rollback window for payment migration" — the title contains "rollback window," but the description doesn't. The user said "the description references rollback window."
- WEB-7: description contains "Mentions the rollback window here too, still pending completion." — but completedAt is null.
- MOB-1 and WEB-1: both have descriptions containing "rollback window" (identical text), and both were completed on 2026-10-02.

So, two issues literally match the criteria. Hmm. Maybe I should check the assignee more carefully — the filter was assignee ID eq Priya. Both are included, so both are assigned to Priya.

Could there be other assignee matches (e.g., assigneeID vs. assignee)? The filter worked without issue.

This is ambiguous — two issues match all the specified criteria. I can't tell them apart. Options: ask the user, or update both? The user said "the issue" (singular), expecting uniqueness. The safest thing is to ask which one — MOB-1 or WEB-1. But the execution bias pushes toward action. However, updating the wrong issue would be a mistake. Both are completed issues with identical descriptions.

Hmm, but maybe I should double-check: is there a subtle difference — for example, one's completedAt is 2026-10-02T16:00:00 — identical down to the timestamp. Both priority 3.0, sam
Command: 
Response: null

## Final answer
I found two issues assigned to Priya Nair that both mention "the rollback window" in their description and were completed on Oct 2, 2026 — they're identical except for team and title:

- **MOB-1** – "Mobile payment rollback check" (Mobile team)
- **WEB-1** – "Payment migration incident follow-up" (Web team)

Both have the same description ("Coordinate the rollback window with on-call before merging."), same completion time (Oct 2, 16:00), and current priority 3. The other Priya-assigned issues don't match (WEB-2 mentions rollback in the title only; WEB-7 isn't completed).

Which one should I set to Urgent — MOB-1, WEB-1, or both?

## State diff
(no changes)

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": []}. Provisional outcome: incomplete. Provisional exposed facts: [].

Give your verdict for this trial.