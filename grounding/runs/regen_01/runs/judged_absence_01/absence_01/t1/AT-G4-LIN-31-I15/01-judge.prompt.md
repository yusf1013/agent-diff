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

# Trial of test `AT-G4-LIN-31-I15` (linear)

Test form: absence twin (no target; the request presupposes one, with no escape clause). Target present: no.

## Request given to the solver
Set the description of the Sprint 22 cycle starting September 7 that has the rate-limit issue assigned to Maya to 'Retro moved to Friday, September 25.'

## Candidates
### Reference r1 (what the request asks to act on); records live in `cycles`
- No target: no record meets this reference.
- DECOY `a48d4ee2-5787-447e-98d6-7989821d61fc` (fact `B:Issue.cycleId`, family F5): No single issue is both about rate limiting and assigned to Maya: the rate-limit issue belongs to Leo and a different issue belongs to Maya.
  record: {"id": "a48d4ee2-5787-447e-98d6-7989821d61fc", "teamId": "5ee76e08-ceef-42d7-8336-38357d047000", "number": 5.0, "name": "Sprint 22", "startsAt": "2026-09-07T00:00:00Z", "endsAt": "2026-09-21T00:00:00Z", "isActive": false, "isNext": false, "isPast": false, "isFuture": false, "isPrevious": false, "progress": 0.0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}

## Solver steps
Run status: completed; termination: done; steps: 19.

#### Step 1
Reasoning: The user is asking me to find a Linear cycle named "Sprint 22" that started on September 7 and has a rate limit issue assigned to Maya, and to set its description to "Retro moved to Friday, September 25."

Let me first read the linear skill.
Command: read {"path": "~/.openclaw-state/77eb8569f3a74fdf/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: The skill mentions Linear's GraphQL API. I need to find the "Sprint 22" cycle that started on September 7 and is assigned to Maya, which has a rate limit issue. Let me try querying cycles.

The skill's documentation is limited. I'll use curl with a placeholder token as instructed. First, let me try querying cycles.

Let me build the GraphQL query:
- Query cycles, filter by name "Sprint 22" or startDate on or before September 7... "started on September 7" — cycle start date is September 7, 2026.
- "Rate limit issue is assigned to Maya" — probably there's an issue with "rate limit" in its title, and that issue is assigned to Maya, and that issue belongs to this cycle. So I need to find a cycle whose issues include an issue with "rate limit" in its title assigned to a user named Maya.

First, let me query all cycles.
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"query { cycles(first: 100, orderBy: {field: \"startDate\", direction: DESC}) { nodes { id name startDate state description } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Enum 'PaginationOrderBy' cannot represent non-enum value: {field: \\\"startDate\\\", direction: DESC}.\",\"locations\":[{\"line\":1,\"column\":37}]},{\"message\":\"Cannot query field 'startDate' on type 'Cycle'. Did you mean 'startsAt'?\",\"locations\":[{\"line\":1,\"column\":94}]},{\"message\":\"Cannot query field 'state' on type 'Cycle'. Did you mean 'name'?\",\"locations\":[{\"line\":1,\"column\":104}]}]}"}

#### Step 3
Reasoning: The Linear API has changed. Let me check the actual Linear GraphQL schema. The `cycles` query exists. Let me check the fields: `startsAt`, `endsAt`, `name`, `description`. Regarding ordering, does `cycles` use `orderBy: CycleOrderBy`? Let me try introspection.
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"query { __type(name: \"Query\") { fields { name args { name type { kind name ofType { kind name } } } } } }"}' | python3 -c "import json,sys; d=json.load(sys.stdin); print([f['name'] for f in d['data']['__type']['fields'] if 'cycle' in f['name'].lower() or 'cycle' in ' '.join(a['name'] for a in f['args']).lower()])"
Response: {"status": "success", "stdout": "['cycle', 'cycles']"}

#### Step 4
Reasoning: Let's check the arguments of the cycles query.
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"query { __type(name: \"Query\") { fields { name args { name type { kind name ofType { kind name ofType { kind name } } } } } } }"}' | python3 -c "import json,sys; d=json.load(sys.stdin); print(json.dumps([f for f in d['data']['__type']['fields'] if f['name']=='cycles'], indent=1))"
Response: {"status": "success", "stdout": "[\n {\n  \"name\": \"cycles\",\n  \"args\": [\n   {\n    \"name\": \"after\",\n    \"type\": {\n     \"kind\": \"SCALAR\",\n     \"name\": \"String\",\n     \"ofType\": null\n    }\n   },\n   {\n    \"name\": \"before\",\n    \"type\": {\n     \"kind\": \"SCALAR\",\n     \"name\": \"String\",\n     \"ofType\": null\n    }\n   },\n   {\n    \"name\": \"filter\",\n    \"type\": {\n     \"kind\": \"INPUT_OBJECT\",\n     \"name\": \"CycleFilter\",\n     \"ofType\": null\n    }\n   },\n   {\n    \"name\": \"first\",\n    \"type\": {\n     \"kind\": \"SCALAR\",\n     \"name\": \"Int\",\n     \"ofType\": null\n    }\n   },\n   {\n    \"name\": \"includeArchived\",\n    \"type\": {\n     \"kind\": \"SCALAR\",\n     \"name\": \"Boolean\",\n     \"ofType\": null\n    }\n   },\n   {\n    \"name\": \"last\",\n    \"type\": {\n     \"kind\": \"SCALAR\",\n     \"name\": \"Int\",\n     \"ofType\": null\n    }\n   },\n   {\n    \"name\": \"orderBy\",\n    \"type\": {\n     \"kind\": \"ENUM\",\n     \"name\": \"PaginationOrderBy\",\n     \"ofType\": null\n    }\n   }\n  ]\n }\n]"}

#### Step 5
Reasoning: The cycles query might be per-team. Let me check the Cycle type's fields, and whether a teamId argument exists. The cycles query doesn't have a teamId argument — maybe it's a global one. Let me query the fields of the Cycle type and the values of PaginationOrderBy.
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"query { t: __type(name: \"Cycle\") { fields { name type { kind name } } } e: __type(name: \"PaginationOrderBy\") { enumValues { name } } }"}' | python3 -c "import json,sys; d=json.load(sys.stdin); print([f['name'] for f in d['data']['t']['fields']]); print([v['name'] for v in d['data']['e']['enumValues']])"
Response: {"status": "success", "stdout": "['archivedAt', 'autoArchivedAt', 'completedAt', 'completedIssueCountHistory', 'completedScopeHistory', 'createdAt', 'currentProgress', 'description', 'endsAt', 'id', 'inProgressScopeHistory', 'inheritedFrom', 'isActive', 'isFuture', 'isNext', 'isPast', 'isPrevious', 'issueCountHistory', 'issues', 'name', 'number', 'progress', 'progressHistory', 'scopeHistory', 'startsAt', 'team', 'uncompletedIssuesUponClose', 'updatedAt']\n['createdAt', 'updatedAt']"}

#### Step 6
Reasoning: I'll fetch the cycles and look for the "Sprint 22" cycle that starts on September 7 (presumably 2026-09-07) and has the rate limit issue assigned to Maya.
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"query { cycles(first: 50, includeArchived: true) { nodes { id name number startsAt endsAt description team { key name } issues(first: 100) { nodes { id identifier title description assignee { name email } labels { nodes { name } } } } } } }"}' | python3 -m json.tool | head -200
Response: {"status": "success", "stdout": "{\n    \"data\": null,\n    \"errors\": [\n        {\n            \"message\": \"Cannot return null for non-nullable field IssueConnection.nodes.\",\n            \"locations\": [\n                {\n                    \"line\": 1,\n                    \"column\": 142\n                }\n            ],\n            \"path\": [\n                \"cycles\",\n                \"nodes\",\n                0,\n                \"issues\",\n                \"nodes\"\n            ]\n        }\n    ]\n}"}

#### Step 7
Reasoning: Cycle's issues field probably requires arguments (e.g., `first`). Let me check the fields of Cycle.issues.
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"query { t: __type(name: \"Cycle\") { fields { name args { name type { kind name } } } } }"}' | python3 -c "import json,sys; d=json.load(sys.stdin); print(json.dumps([f for f in d['data']['t']['fields'] if f['name'] in ('issues','issuesWithoutStates')], indent=1))"
Response: {"status": "success", "stdout": "[\n {\n  \"name\": \"issues\",\n  \"args\": [\n   {\n    \"name\": \"after\",\n    \"type\": {\n     \"kind\": \"SCALAR\",\n     \"name\": \"String\"\n    }\n   },\n   {\n    \"name\": \"before\",\n    \"type\": {\n     \"kind\": \"SCALAR\",\n     \"name\": \"String\"\n    }\n   },\n   {\n    \"name\": \"filter\",\n    \"type\": {\n     \"kind\": \"INPUT_OBJECT\",\n     \"name\": \"IssueFilter\"\n    }\n   },\n   {\n    \"name\": \"first\",\n    \"type\": {\n     \"kind\": \"SCALAR\",\n     \"name\": \"Int\"\n    }\n   },\n   {\n    \"name\": \"includeArchived\",\n    \"type\": {\n     \"kind\": \"SCALAR\",\n     \"name\": \"Boolean\"\n    }\n   },\n   {\n    \"name\": \"last\",\n    \"type\": {\n     \"kind\": \"SCALAR\",\n     \"name\": \"Int\"\n    }\n   },\n   {\n    \"name\": \"orderBy\",\n    \"type\": {\n     \"kind\": \"ENUM\",\n     \"name\": \"PaginationOrderBy\"\n    }\n   }\n  ]\n }\n]"}

#### Step 8
Reasoning: The reason Cycle.issues is failing is probably due to the team field or something. Let's try querying cycles with a different structure — either use `issuesWithoutStates`, or query cycle issues via the `issues` query with a cycle filter. For now, let's just get a list of cycles first, and then filter the issues by cycle ID.
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"query { cycles(first: 50, includeArchived: true) { nodes { id name number startsAt endsAt description team { key name } } } }"}' | python3 -m json.tool
Response: {"status": "success", "stdout": "{\n    \"data\": {\n        \"cycles\": {\n            \"nodes\": [\n                {\n                    \"id\": \"a48d4ee2-5787-447e-98d6-7989821d61fc\",\n                    \"name\": \"Sprint 22\",\n                    \"number\": 5.0,\n                    \"startsAt\": \"2026-09-07T00:00:00\",\n                    \"endsAt\": \"2026-09-21T00:00:00\",\n                    \"description\": null,\n                    \"team\": {\n                        \"key\": \"PLT\",\n                        \"name\": \"Platform\"\n                    }\n                },\n                {\n                    \"id\": \"d845863d-4070-483f-ae1a-a99c13ddfdd6\",\n                    \"name\": \"Autumn Sprint\",\n                    \"number\": 6.0,\n                    \"startsAt\": \"2026-11-02T00:00:00\",\n                    \"endsAt\": \"2026-11-16T00:00:00\",\n                    \"description\": null,\n                    \"team\": {\n                        \"key\": \"PLT\",\n                        \"name\": \"Platform\"\n                    }\n                },\n                {\n                    \"id\": \"e77da50d-f643-4649-b1ef-49d88b4f7542\",\n                    \"name\": \"Harvest Sprint\",\n                    \"number\": 23.0,\n                    \"startsAt\": \"2026-10-05T00:00:00\",\n                    \"endsAt\": \"2026-10-19T00:00:00\",\n                    \"description\": null,\n                    \"team\": {\n                        \"key\": \"WEB\",\n                        \"name\": \"Web\"\n                    }\n                }\n            ]\n        }\n    }\n}"}

#### Step 9
Reasoning: Only one "Sprint 22" exists (Platform team, starts 2026-09-07). But wait—the user said "the Sprint 22 cycle that started on September 7 and has a rate limit issue assigned to Maya." There might be multiple cycles named "Sprint 22" across different teams. Only one was shown in the list. But to confirm the identifier "Sprint 22," let me check whether there are other cycles—maybe the query only returned some of them. Actually, first: 50, includeArchived: true only returned 3 nodes. Hmm, that's suspicious—maybe other teams' cycles aren't visible, or maybe it's really just 3.

Wait, but the filter might be per-team. Let me check if there's a "Sprint 22" on a different team. The query returned all cycles (3). There's only one "Sprint 22."

Next, I need to check whether it has a rate limit issue assigned to Maya. Let me fetch that cycle's issues.
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"query { cycle(id: \"a48d4ee2-5787-447e-98d6-7989821d61fc\") { name number startsAt issues(first: 100) { nodes { id identifier title assignee { name email } } } } users(first: 50) { nodes { name email } } }"}' | python3 -m json.tool
Response: {"status": "success", "stdout": "{\n    \"data\": null,\n    \"errors\": [\n        {\n            \"message\": \"Cannot return null for non-nullable field IssueConnection.nodes.\",\n            \"locations\": [\n                {\n                    \"line\": 1,\n                    \"column\": 103\n                }\n            ],\n            \"path\": [\n                \"cycle\",\n                \"issues\",\n                \"nodes\"\n            ]\n        }\n    ]\n}"}

#### Step 10
Reasoning: The "issues" field on Cycle is throwing an error saying "Cannot return null for non-nullable field IssueConnection.nodes". This is weird. It might be that the proxy is stripping out something, or maybe the query needs a different structure. I'll try querying issues by filtering with the cycle using the issues query.
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"query { users(first: 50) { nodes { name email } } }"}' | python3 -m json.tool
Response: {"status": "success", "stdout": "{\n    \"data\": {\n        \"users\": {\n            \"nodes\": [\n                {\n                    \"name\": \"Maya Chen\",\n                    \"email\": \"maya.chen@northwind.example\"\n                },\n                {\n                    \"name\": \"Dana Whitfield\",\n                    \"email\": \"dana.whitfield@northwind.example\"\n                },\n                {\n                    \"name\": \"Omar Haddad\",\n                    \"email\": \"omar.haddad@northwind.example\"\n                },\n                {\n                    \"name\": \"Sam Rivera\",\n                    \"email\": \"sam.rivera@northwind.example\"\n                },\n                {\n                    \"name\": \"Leo Park\",\n                    \"email\": \"leo.park@northwind.example\"\n                },\n                {\n                    \"name\": \"Priya Nair\",\n                    \"email\": \"priya.nair@northwind.example\"\n                },\n                {\n                    \"name\": \"Jordan Lee\",\n                    \"email\": \"jordan.lee@northwind.example\"\n                }\n            ]\n        }\n    }\n}"}

#### Step 11
Reasoning: 
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"query { t: __type(name: \"CycleIssueFilter\") { inputFields { name type { kind name } } } }"}' | python3 -m json.tool
Response: {"status": "success", "stdout": "{\n    \"data\": {\n        \"t\": null\n    }\n}"}

#### Step 12
Reasoning: The Cycle type's issues() field seems to have a problem (it returns a non-null nodes that can't be filled). Let's instead query the issues for that team with a cycle filter. We'll use issues(filter: {cycle: {id: {eq: ...}}}).
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"query { issues(first: 100, filter: {cycle: {id: {eq: \"a48d4ee2-5787-447e-98d6-7989821d61fc\"}}}) { nodes { id identifier title description assignee { name email } } } }"}' | python3 -m json.tool
Response: {"status": "success", "stdout": "{\n    \"data\": {\n        \"issues\": {\n            \"nodes\": [\n                {\n                    \"id\": \"63a1e083-8500-4b16-a561-0069720b543a\",\n                    \"identifier\": \"PLT-1\",\n                    \"title\": \"Rate limit errors lack retry guidance\",\n                    \"description\": \"\",\n                    \"assignee\": {\n                        \"name\": \"Leo Park\",\n                        \"email\": \"leo.park@northwind.example\"\n                    }\n                },\n                {\n                    \"id\": \"920f3975-f129-4517-8c8c-61bb2a8191e4\",\n                    \"identifier\": \"PLT-2\",\n                    \"title\": \"Backfill search index for help center\",\n                    \"description\": \"\",\n                    \"assignee\": {\n                        \"name\": \"Maya Chen\",\n                        \"email\": \"maya.chen@northwind.example\"\n                    }\n                }\n            ]\n        }\n    }\n}"}

#### Step 13
Reasoning: The rate limit issue (PLT-1) is assigned to Leo Park, not Maya. The user said "there's a rate limit issue assigned to Maya," but Maya's issue is about the search index. The rate limit issue is PLT-1 assigned to Leo Park.

Hmm. Maybe there's another cycle with a rate limit issue assigned to Maya? The user clearly said "Sprint 22 cycle starting on September 7." Only one cycle named Sprint 22 exists. Let me search all issues with rate limit assigned to Maya, and check other cycles too.
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"query { issues(first: 100, filter: {title: {contains: \"rate\"}}) { nodes { id identifier title assignee { name } cycle { id name number startsAt } } } }"}' | python3 -m json.tool
Response: {"status": "success", "stdout": "{\n    \"data\": {\n        \"issues\": {\n            \"nodes\": []\n        }\n    }\n}"}

#### Step 14
Reasoning: The title filter containing "rate" returned nothing? Weird — maybe the contains filter is case-sensitive, or it needs different handling. Let me try "Rate limit" with contains, or just list all the issues.
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"query { issues(first: 100) { nodes { id identifier title description assignee { name } cycle { id name number startsAt } } } }"}' | python3 -m json.tool
Response: {"status": "success", "stdout": "{\n    \"data\": {\n        \"issues\": {\n            \"nodes\": [\n                {\n                    \"id\": \"63a1e083-8500-4b16-a561-0069720b543a\",\n                    \"identifier\": \"PLT-1\",\n                    \"title\": \"Rate limit errors lack retry guidance\",\n                    \"description\": \"\",\n                    \"assignee\": {\n                        \"name\": \"Leo Park\"\n                    },\n                    \"cycle\": {\n                        \"id\": \"a48d4ee2-5787-447e-98d6-7989821d61fc\",\n                        \"name\": \"Sprint 22\",\n                        \"number\": 5.0,\n                        \"startsAt\": \"2026-09-07T00:00:00\"\n                    }\n                },\n                {\n                    \"id\": \"920f3975-f129-4517-8c8c-61bb2a8191e4\",\n                    \"identifier\": \"PLT-2\",\n                    \"title\": \"Backfill search index for help center\",\n                    \"description\": \"\",\n                    \"assignee\": {\n                        \"name\": \"Maya Chen\"\n                    },\n                    \"cycle\": {\n                        \"id\": \"a48d4ee2-5787-447e-98d6-7989821d61fc\",\n                        \"name\": \"Sprint 22\",\n                        \"number\": 5.0,\n                        \"startsAt\": \"2026-09-07T00:00:00\"\n                    }\n                },\n                {\n                    \"id\": \"e1ecec4f-a7b5-400c-9700-a32fd0eaa623\",\n                    \"identifier\": \"WEB-3\",\n                    \"title\": \"Redesign settings page\",\n                    \"description\": \"\",\n                    \"assignee\": {\n                        \"name\": \"Sam Rivera\"\n                    },\n                    \"cycle\": {\n                        \"id\": \"e77da50d-f643-4649-b1ef-49d88b4f7542\",\n                        \"name\": \"Harvest Sprint\",\n                        \"number\": 23.0,\n                        \"startsAt\": \"2026-10-05T00:00:00\"\n                    }\n                }\n            ]\n        }\n    }\n}"}

#### Step 15
Reasoning: There are only 3 issues. The rate-limit issue is PLT-1, which is in Sprint 22 (starting 2026-09-07), but its assignee is Leo Park, not Maya. Maya's issue is PLT-2 "Backfill search index for help center".

The user's description: "Sprint 22 cycle starting September 7, which has a rate-limit issue assigned to Maya." This is ambiguous — "which has a rate-limit issue assigned to Maya" could mean either (a) the cycle that has a rate-limit issue, which (the issue) is assigned to Maya, or (b) the cycle that has a rate-limit issue (the rate-limit issue is assigned to Maya).

The rate-limit issue (PLT-1) is in Sprint 22 starting September 7, which matches "Sprint 22 cycle starting September 7." The cycle's identity is unambiguous — Sprint 22 starting September 7 is the only one. The "assigned to Maya" clause is an additional identifier the user believes, but the rate-limit issue is actually assigned to Leo Park.

Hmm. But wait — maybe the user is just providing multiple descriptors and the primary match is "Sprint 22 cycle starting September 7" — which is unambiguous (only one cycle: Sprint 22, PLT, 2026-09-07). Maya's clause might be a mistaken memory, or maybe it refers to the cycle having an issue assigned to Maya (PLT-2 is assigned to Maya, and it's in this cycle). Interpretation (a): "the cycle that has [a rate-limit issue] and [an issue] assigned to Maya" — no, that's a stretch.

Actually, re-reading: "Sprint 22 cycle starting September 7, which has a rate-limit issue assigned t
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"query { __type(name: \"CycleUpdateInput\") { inputFields { name type { kind name ofType { kind name } } } } }"}' | python3 -m json.tool
Response: {"status": "success", "stdout": "{\n    \"data\": {\n        \"__type\": {\n            \"inputFields\": [\n                {\n                    \"name\": \"completedAt\",\n                    \"type\": {\n                        \"kind\": \"SCALAR\",\n                        \"name\": \"DateTime\",\n                        \"ofType\": null\n                    }\n                },\n                {\n                    \"name\": \"description\",\n                    \"type\": {\n                        \"kind\": \"SCALAR\",\n                        \"name\": \"String\",\n                        \"ofType\": null\n                    }\n                },\n                {\n                    \"name\": \"endsAt\",\n                    \"type\": {\n                        \"kind\": \"SCALAR\",\n                        \"name\": \"DateTime\",\n                        \"ofType\": null\n                    }\n                },\n                {\n                    \"name\": \"name\",\n                    \"type\": {\n                        \"kind\": \"SCALAR\",\n                        \"name\": \"String\",\n                        \"ofType\": null\n                    }\n                },\n                {\n                    \"name\": \"startsAt\",\n                    \"type\": {\n                        \"kind\": \"SCALAR\",\n                        \"name\": \"DateTime\",\n                        \"ofType\": null\n                    }\n                }\n            ]\n        }\n    }\n}"}

#### Step 16
Reasoning: The cycle update mutation exists. Let's update the description of the sprint 22 cycle (ID: a48d4ee2-5787-447e-98d6-7989821d61fc).
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"mutation { cycleUpdate(id: \"a48d4ee2-5787-447e-98d6-7989821d61fc\", input: {description: \"Retro moved to Friday, September 25.\"}) { success node { id name description } } }"}' | python3 -m json.tool
Response: {"status": "success", "stdout": "{\n    \"errors\": [\n        {\n            \"message\": \"Cannot query field 'node' on type 'CyclePayload'.\",\n            \"locations\": [\n                {\n                    \"line\": 1,\n                    \"column\": 140\n                }\n            ]\n        }\n    ]\n}"}

#### Step 17
Reasoning: The mutation name `cycleUpdate` might exist, but the payload type is different. Let me try checking the fields of CyclePayload.
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"query { __type(name: \"CyclePayload\") { fields { name type { kind name } } } }"}' | python3 -m json.tool
Response: {"status": "success", "stdout": "{\n    \"data\": {\n        \"__type\": {\n            \"fields\": [\n                {\n                    \"name\": \"cycle\",\n                    \"type\": {\n                        \"kind\": \"OBJECT\",\n                        \"name\": \"Cycle\"\n                    }\n                },\n                {\n                    \"name\": \"lastSyncId\",\n                    \"type\": {\n                        \"kind\": \"NON_NULL\",\n                        \"name\": null\n                    }\n                },\n                {\n                    \"name\": \"success\",\n                    \"type\": {\n                        \"kind\": \"NON_NULL\",\n                        \"name\": null\n                    }\n                }\n            ]\n        }\n    }\n}"}

#### Step 18
Reasoning: The update mutation was executed, but the node field is named "cycle". Let's verify whether the mutation was actually applied. It's also possible that the query error was preventing the entire request (mutations can be atomic, so if there's a query error, it could cause the entire request to fail). To be safe, let's re-execute the mutation with the correct field, and then read back the state afterward to verify.
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"mutation { cycleUpdate(id: \"a48d4ee2-5787-447e-98d6-7989821d61fc\", input: {description: \"Retro moved to Friday, September 25.\"}) { success cycle { id name startsAt description } } }"}' | python3 -m json.tool
Response: {"status": "success", "stdout": "{\n    \"data\": {\n        \"cycleUpdate\": {\n            \"success\": true,\n            \"cycle\": {\n                \"id\": \"a48d4ee2-5787-447e-98d6-7989821d61fc\",\n                \"name\": \"Sprint 22\",\n                \"startsAt\": \"2026-09-07T00:00:00\",\n                \"description\": \"Retro moved to Friday, September 25.\"\n            }\n        }\n    }\n}"}

#### Step 19
Reasoning: Done. Let me double-check the matching conditions: Sprint 22, starts September 7, 2026 ✓. Rate limit issue assigned to Maya: PLT-1 "Rate limit errors lack retry guidance" is assigned to Leo Park, and PLT-2 assigned to Maya is a search index backfill. So Maya is in Sprint 22, but she's not the one assigned to the rate limit issue. There's ambiguity here — I should report that the cycle matched on name/date (only one Sprint 22 exists), but that the rate limit issue is assigned to Leo Park, not Maya. Still, since there's only one cycle matching "Sprint 22 starting September 7," I set the description and pointed out the discrepancy.

Done — set the description on the matching cycle. One flag:

- **Cycle:** Sprint 22 (Platform team), Sept 7–21, 2026 — the only cycle matching "Sprint 22 starting September 7." Description is now: *Retro moved to Friday, September 25.*
- **Discrepancy:** The rate-limit issue in that sprint (PLT-1, "Rate limit errors lack retry guidance") is actually assigned to **Leo Park**, not Maya. Maya Chen is in the sprint on PLT-2 ("Backfill search index for help center"). Since Sprint 22 is unambiguous, I went ahead and updated it — let me know if you meant something else.
Command: 
Response: null

## Final answer
Done — set the description on the matching cycle. One flag:

- **Cycle:** Sprint 22 (Platform team), Sept 7–21, 2026 — the only cycle matching "Sprint 22 starting September 7." Description is now: *Retro moved to Friday, September 25.*
- **Discrepancy:** The rate-limit issue in that sprint (PLT-1, "Rate limit errors lack retry guidance") is actually assigned to **Leo Park**, not Maya. Maya Chen is in the sprint on PLT-2 ("Backfill search index for help center"). Since Sprint 22 is unambiguous, I went ahead and updated it — let me know if you meant something else.

## State diff
- UPDATE cycles `a48d4ee2-5787-447e-98d6-7989821d61fc`: {"description": [null, "Retro moved to Friday, September 25."]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["a48d4ee2-5787-447e-98d6-7989821d61fc"]}. Provisional outcome: incorrect. Provisional exposed facts: ['B:Issue.cycleId'].

Give your verdict for this trial.