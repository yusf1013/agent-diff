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

# Trial of test `AT-G4-LIN-28-I13-I14` (linear)

Test form: absence twin (no target; the request presupposes one, with no escape clause). Target present: no.

## Request given to the solver
Set the estimate to 3 on the issue in the Web team's Done state that was completed on September 18 and whose description mentions the offline cache rollback.

## Candidates
### Reference r1 (what the request asks to act on); records live in `issues`
- No target: no record meets this reference.
- DECOY `9a3181b9-b92c-4e82-8797-a7d742139006` (fact `A:Issue.description`, family F1): Its title mentions the offline cache rollback, but its description does not.
  record: {"id": "9a3181b9-b92c-4e82-8797-a7d742139006", "identifier": "WEB-4", "title": "Offline cache rollback for kiosk mode", "description": "Kiosk layout refresh for the home screen; no backend changes.", "teamId": "6b427556-b29e-460f-a177-995587b19d54", "stateId": "49cb8ea5-1014-45ef-bf45-0a122e277a6d", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 4.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "dueDate": "2026-09-25", "completedAt": "2026-09-18T14:00:00Z"}
- DECOY `56dcfe98-5040-4222-83b7-aca46be57709` (fact `A:Issue.description`, family F2): A comment on the issue mentions the offline cache rollback, but the issue description does not.
  record: {"id": "56dcfe98-5040-4222-83b7-aca46be57709", "identifier": "WEB-5", "title": "Receipt email duplicates", "description": "Dedupe logic for receipt emails after retry.", "teamId": "6b427556-b29e-460f-a177-995587b19d54", "stateId": "49cb8ea5-1014-45ef-bf45-0a122e277a6d", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 5.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "dueDate": "2026-09-26", "completedAt": "2026-09-18T16:00:00Z"}

## Solver steps
Run status: completed; termination: done; steps: 18.

#### Step 1
Reasoning: I need to investigate this further. Let me check the details.

The user wants to work in Linear. I should read Linear's SKILL.md first.
Command: read {"path": "~/.openclaw-state/1ffdf92fbcee43f0/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: The skill says authentication is handled automatically via proxy, and to use placeholder tokens like `<TOKEN>`. Let me query the Linear GraphQL API to find the issue.

What I need to do:
1. Find the Web team (a team with a key like "WEB", or one whose name is "Web")
2. Find its "Done" workflow state
3. Find issues in that state whose completedAt is September 18, 2026
4. Among those, find the one whose description mentions a rollback of the offline cache
5. Set the estimate to 3

Let me write a GraphQL query. First, find the team and states, then find the issues.

I can do it in one query: fetch the teams, and for the Web team fetch the Done state and issues filtered by completedAt.

Linear GraphQL schema:
- `teams(filter: {name: {eq: "Web"}})`
- `workflowStates`
- `issues(filter: {state: {id: {eq: ...}}, completedAt: {eq: ...}, description: {contains: ...}})`

Actually I can use `issue.filter.completionState` or state. For completed issues, Linear has a `completedAt` filter field. Let me use `completedAt: {gte: "2026-09-18", lt: "2026-09-19"}`.

Description filter: `description: {contains: "offline cache rollback"}` — but the exact phrase in the description might be different. It might be better to search first, then check. Let me do a staged query:

1. Query the Web team: `teams { nodes { id name key } }`
2. Query the workflow states for that team: `workflowStates(includeArchived: false) { nodes { id name type teamId } }` — better to filter with `teamId`.
3. Query issues in 
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"query { teams(first: 50) { nodes { id name key } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"teams\":{\"nodes\":[{\"id\":\"6b427556-b29e-460f-a177-995587b19d54\",\"name\":\"Web\",\"key\":\"WEB\"},{\"id\":\"ad2e455d-c823-447b-b5f6-8231c7d37722\",\"name\":\"Mobile\",\"key\":\"MOB\"}]}}}"}

#### Step 3
Reasoning: The Web team's id is 6b427556-b29e-460f-a177-995587b19d54. Next, I need to find the workflow state named "Done" for that team, and then find issues in that state that were completed on September 18 and whose description mentions a rollback of the offline cache.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"query { workflowStates(teamId: \"6b427556-b29e-460f-a177-995587b19d54\") { nodes { id name type } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Unknown argument 'teamId' on field 'Query.workflowStates'.\",\"locations\":[{\"line\":1,\"column\":24}]}]}"}

#### Step 4
Reasoning: Let's check the schema for the arguments of workflowStates.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ __type(name: \"Query\") { fields { name args { name type { name kind ofType { name } } } } } }"}' | python3 -c "import json,sys; d=json.load(sys.stdin); [print(f['name'], [a['name'] for a in f['args']]) for f in d['data']['__type']['fields'] if f['name'] in ('workflowStates','issues')]"
Response: {"status": "success", "stdout": "issues ['after', 'before', 'filter', 'first', 'includeArchived', 'last', 'orderBy', 'sort']\nworkflowStates ['after', 'before', 'filter', 'first', 'includeArchived', 'last', 'orderBy']"}

#### Step 5
Reasoning: Use filter on workflowStates. Let's check the filter type of WorkflowStates... I could introspect, or I could just try `filter: { teamId: { eq: ... } }`.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"query { workflowStates(filter: { teamId: { eq: \"6b427556-b29e-460f-a177-995587b19d54\" } }) { nodes { id name type } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Field 'teamId' is not defined by type 'WorkflowStateFilter'. Did you mean 'team'?\",\"locations\":[{\"line\":1,\"column\":34}]}]}"}

#### Step 6
Reasoning: (Thinking: The filter for workflowState is `team`. Let me check the structure of WorkflowStateFilter.)
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ __type(name: \"WorkflowStateFilter\") { inputFields { name type { name kind ofType { name kind } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"inputFields\":[{\"name\":\"and\",\"type\":{\"name\":null,\"kind\":\"LIST\",\"ofType\":{\"name\":null,\"kind\":\"NON_NULL\"}}},{\"name\":\"createdAt\",\"type\":{\"name\":\"DateComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"description\",\"type\":{\"name\":\"StringComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"id\",\"type\":{\"name\":\"IDComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"issues\",\"type\":{\"name\":\"IssueCollectionFilter\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"name\",\"type\":{\"name\":\"StringComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"or\",\"type\":{\"name\":null,\"kind\":\"LIST\",\"ofType\":{\"name\":null,\"kind\":\"NON_NULL\"}}},{\"name\":\"position\",\"type\":{\"name\":\"NumberComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"team\",\"type\":{\"name\":\"TeamFilter\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"type\",\"type\":{\"name\":\"StringComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"updatedAt\",\"type\":{\"name\":\"DateComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}}]}}}"}

#### Step 7
Reasoning: The filter uses `team: { id: { eq: ... } }` (probably a TeamFilter with id). Let's try that.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"query { workflowStates(filter: { team: { id: { eq: \"6b427556-b29e-460f-a177-995587b19d54\" } } }) { nodes { id name type } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"workflowStates\":{\"nodes\":[{\"id\":\"0c434939-9671-48cd-9f5a-551cf77d606c\",\"name\":\"Todo\",\"type\":\"unstarted\"},{\"id\":\"49cb8ea5-1014-45ef-bf45-0a122e277a6d\",\"name\":\"Done\",\"type\":\"completed\"},{\"id\":\"4e12cac5-a870-437a-98df-943f0e63416a\",\"name\":\"Canceled\",\"type\":\"canceled\"},{\"id\":\"74da11dc-78dc-4b5e-8f79-049f24ca0bb9\",\"name\":\"In Progress\",\"type\":\"started\"},{\"id\":\"7fe92f22-6cda-4c02-8c76-ad16d2edcb1d\",\"name\":\"In Review\",\"type\":\"started\"},{\"id\":\"f52619ae-943e-4cb3-bf12-4dfed15ced6a\",\"name\":\"Backlog\",\"type\":\"backlog\"}]}}}"}

#### Step 8
Reasoning: The "Done" state in the web team: id `49cb8ea5-1014-45ef-bf45-0a122e277a6d`. Next, I'll search for issues within that state that were completed on September 18 (2026) and whose description mentions a rollback of the offline cache.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"query { issues(filter: { team: { id: { eq: \"6b427556-b29e-460f-a177-995587b19d54\" } }, state: { id: { eq: \"49cb8ea5-1014-45ef-bf45-0a122e277a6d\" } }, completedAt: { between: [\"2026-09-18T00:00:00\", \"2026-09-18T23:59:59\"] }, description: { contains: \"offline cache\" } }, first: 20) { nodes { id identifier title description state { name } completedAt estimate } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Field 'between' is not defined by type 'NullableDateComparator'.\",\"locations\":[{\"line\":1,\"column\":166}]}]}"}

#### Step 9
Reasoning: Let's check the fields of DateComparator.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ __type(name: \"NullableDateComparator\") { inputFields { name } } __type2: __type(name: \"DateComparator\") { inputFields { name } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"inputFields\":[{\"name\":\"eq\"},{\"name\":\"gt\"},{\"name\":\"gte\"},{\"name\":\"in\"},{\"name\":\"lt\"},{\"name\":\"lte\"},{\"name\":\"neq\"},{\"name\":\"nin\"},{\"name\":\"null\"}]},\"__type2\":{\"inputFields\":[{\"name\":\"eq\"},{\"name\":\"gt\"},{\"name\":\"gte\"},{\"name\":\"in\"},{\"name\":\"lt\"},{\"name\":\"lte\"},{\"name\":\"neq\"},{\"name\":\"nin\"}]}}}"}

#### Step 10
Reasoning: Use gte/lt against completedAt. September 18, 2026 — the date completed in that day's local time (EDT, UTC-4). gte 2026-09-18T00:00:00Z lt 2026-09-19T00:00:00Z roughly covers the UTC day. For the EDT day, it would be 2026-09-18T04:00:00Z to 2026-09-19T04:00:00Z. Let's widen the range a bit: gte 2026-09-18T00:00:00 lt 2026-09-19T00:00:00. Actually, for safety, let's just grab all the completed issues in the Done state and check the dates.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"query { issues(filter: { team: { id: { eq: \"6b427556-b29e-460f-a177-995587b19d54\" } }, state: { id: { eq: \"49cb8ea5-1014-45ef-bf45-0a122e277a6d\" } }, completedAt: { gte: \"2026-09-18T00:00:00\", lt: \"2026-09-19T00:00:00\" } }, first: 50) { nodes { id identifier title description state { name } completedAt estimate } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"56dcfe98-5040-4222-83b7-aca46be57709\",\"identifier\":\"WEB-5\",\"title\":\"Receipt email duplicates\",\"description\":\"Dedupe logic for receipt emails after retry.\",\"state\":{\"name\":\"Done\"},\"completedAt\":\"2026-09-18T16:00:00\",\"estimate\":null},{\"id\":\"9a3181b9-b92c-4e82-8797-a7d742139006\",\"identifier\":\"WEB-4\",\"title\":\"Offline cache rollback for kiosk mode\",\"description\":\"Kiosk layout refresh for the home screen; no backend changes.\",\"state\":{\"name\":\"Done\"},\"completedAt\":\"2026-09-18T14:00:00\",\"estimate\":null}]}}}"}

#### Step 11
Reasoning: Two issues were completed on September 18. One of them has "Offline cache rollback for kiosk mode" written in the title, but its description is "Update of the kiosk layout for the home screen. No changes to the backend."

The user was looking for an issue whose *description* refers to the offline cache rollback. Let me check the descriptions of both. Neither of these descriptions refers to the offline cache rollback. Hmm. Maybe there are more issues — completedAt might be a date, but the user might be interpreting "completed on September 18" differently. Let me check more broadly: for issues in the Done state, let me look at the completedAt values and descriptions for all issues.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"query { issues(filter: { team: { id: { eq: \"6b427556-b29e-460f-a177-995587b19d54\" } }, state: { id: { eq: \"49cb8ea5-1014-45ef-bf45-0a122e277a6d\" } } }, first: 100) { nodes { id identifier title description state { name } completedAt estimate } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"56dcfe98-5040-4222-83b7-aca46be57709\",\"identifier\":\"WEB-5\",\"title\":\"Receipt email duplicates\",\"description\":\"Dedupe logic for receipt emails after retry.\",\"state\":{\"name\":\"Done\"},\"completedAt\":\"2026-09-18T16:00:00\",\"estimate\":null},{\"id\":\"9a3181b9-b92c-4e82-8797-a7d742139006\",\"identifier\":\"WEB-4\",\"title\":\"Offline cache rollback for kiosk mode\",\"description\":\"Kiosk layout refresh for the home screen; no backend changes.\",\"state\":{\"name\":\"Done\"},\"completedAt\":\"2026-09-18T14:00:00\",\"estimate\":null}]}}}"}

#### Step 12
Reasoning: Interesting — there are only two issues in the "Done" state, both completed on September 18. The user said "the description mentions the offline cache rollback." WEB-4's *title* is "Offline cache rollback for kiosk mode," but its description is "Kiosk layout refresh for the home screen; no backend changes." Hmm — the description doesn't mention the offline cache rollback. WEB-5's description: "Dedupe logic for receipt emails after retry." That doesn't mention it either.

Wait, there might be other issues — there could be archived issues or other Done issues. The filter only returned 2 issues. Hmm. Maybe the description contains the mention in a way that my query didn't capture? Let me double-check: could there be other "Done" states? There's only one "Done" state.

Hmm, wait — WEB-4's description says "Kiosk layout refresh for the home screen; no backend changes." That doesn't mention the offline cache rollback. So neither matches "the description mentions the offline cache rollback"?

Wait, maybe I should re-check with a broader search — perhaps the description field I fetched is truncated, or there's more. Actually, let me search all issues (regardless of state) whose description contains "offline cache" to see what comes up.

The description fields don't obviously match, so let me search more broadly to make sure I'm not missing an issue.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"query { issues(filter: { description: { contains: \"offline cache\" } }, first: 50, includeArchived: true) { nodes { id identifier title description state { name } completedAt team { key } estimate } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[]}}}"}

#### Step 13
Reasoning: A search on "offline cache" in the description field returns nothing. However, WEB-4's title contains "Offline cache rollback". The description "Kiosk layout refresh for the home screen; no backend changes." doesn't mention offline cache rollback.

Hmm, this might be a trap/test. The user's request is: "the issue in the Web team's Done state, that was completed on September 18, and whose description mentions the offline cache rollback."

There are two issues completed on September 18 in Done:
- WEB-5: "Receipt email duplicates" — description: "Dedupe logic for receipt emails after retry."
- WEB-4: "Offline cache rollback for kiosk mode" — description: "Kiosk layout refresh for the home screen; no backend changes."

Neither description mentions offline cache rollback. The only one that mentions it is the title (WEB-4).

Let me double-check — maybe the description field has a different value, or perhaps there's a difference in how the filter's contains works (case sensitivity?). A contains search for "offline cache" across all issues including archived returned nothing. That's strange since WEB-4's title contains it — but we're filtering on description, not title, so that's as expected.

Just to be safe, let me also try a contains search for "rollback" in the description.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"query { issues(filter: { description: { contains: \"rollback\" } }, first: 50, includeArchived: true) { nodes { id identifier title description state { name } completedAt team { key } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[]}}}"}

#### Step 14
Reasoning: The description filter with "contains" returns nothing, even though the description of WEB-4 "Kiosk layout refresh for the home screen; no backend changes." clearly doesn't contain "rollback" — wait, no, the title does contain "rollback" but the description doesn't. Hmm, but the user is saying "the description mentions rolling back the offline cache." Let me check the actual description more carefully. The descriptions shown are:

- WEB-5: "Dedupe logic for receipt emails after retry."
- WEB-4: "Kiosk layout refresh for the home screen; no backend changes."

Neither mentions "rolling back the offline cache." Interesting. Maybe the description field is being truncated in the response? No, it's short.

Maybe there are more issues — including archived ones, or ones from other teams. Let me query all issues without a team filter and look at everything. Also, it's possible the "contains" filter on description is broken (in the first query where I used a description filter combined with a date filter, the error was only about "between"… then I removed the description filter). Let me check all issues in the Web team regardless of state, and also do a global search for "offline" and "cache".
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"query { issues(first: 100, includeArchived: true) { nodes { id identifier title description state { name } completedAt team { key } } } }"}' | python3 -m json.tool
Response: {"status": "success", "stdout": "{\n    \"data\": {\n        \"issues\": {\n            \"nodes\": [\n                {\n                    \"id\": \"56dcfe98-5040-4222-83b7-aca46be57709\",\n                    \"identifier\": \"WEB-5\",\n                    \"title\": \"Receipt email duplicates\",\n                    \"description\": \"Dedupe logic for receipt emails after retry.\",\n                    \"state\": {\n                        \"name\": \"Done\"\n                    },\n                    \"completedAt\": \"2026-09-18T16:00:00\",\n                    \"team\": {\n                        \"key\": \"WEB\"\n                    }\n                },\n                {\n                    \"id\": \"9a3181b9-b92c-4e82-8797-a7d742139006\",\n                    \"identifier\": \"WEB-4\",\n                    \"title\": \"Offline cache rollback for kiosk mode\",\n                    \"description\": \"Kiosk layout refresh for the home screen; no backend changes.\",\n                    \"state\": {\n                        \"name\": \"Done\"\n                    },\n                    \"completedAt\": \"2026-09-18T14:00:00\",\n                    \"team\": {\n                        \"key\": \"WEB\"\n                    }\n                },\n                {\n                    \"id\": \"9e9c9b05-c0f3-418b-ab52-7f6b401a34b6\",\n                    \"identifier\": \"MOB-2\",\n                    \"title\": \"Onboarding tooltip copy\",\n                    \"description\": \"Rewrite the onboarding tooltips.\",\n                    \"state\": {\n                        \"name\": \"In Progress\"\n                    },\n                    \"completedAt\": null,\n                    \"team\": {\n                        \"key\": \"MOB\"\n                    }\n                },\n                {\n                    \"id\": \"b670ca2c-c888-4fad-baa3-dfbbfefb671b\",\n                    \"identifier\": \"WEB-6\",\n                    \"title\": \"Footer link updates\",\n                    \"description\": \"Update the footer links for the help center.\",\n                    \"state\": {\n                        \"name\": \"Todo\"\n                    },\n                    \"completedAt\": null,\n                    \"team\": {\n                        \"key\": \"WEB\"\n                    }\n                }\n            ]\n        }\n    }\n}"}

#### Step 15
Reasoning: The full list of all issues contains only 4 issues. The only one that matches "Web team, Done state, completed on September 18, related to the offline cache rollback" is WEB-4 "Offline cache rollback for kiosk mode". Its description reads "Kiosk layout refresh for the home screen. No backend changes", and while it doesn't literally contain the phrase "offline cache rollback", the title does. The user said "the description states offline cache rollback" — hmm. There might be comments, or the description might be different. But the only issue that matches all the other conditions (Web team, Done, completed 9/18, offline cache rollback theme) is WEB-4. WEB-5 also matches team/state/date, but has nothing to do with the offline cache rollback.

The description filter for "rollback" returned nothing — that's strange. The title contains "rollback" but the description doesn't. So the `contains` filter is probably only searching the description, and this description doesn't contain it. The user may be loosely saying "the description states...". WEB-4 is the only candidate that matches. Given the constraints, WEB-4 is clearly the intended issue.

Just to be safe, should I check WEB-4's comments to see if "offline cache rollback" is mentioned? Actually, the user's condition is "the description states offline cache rollback" — the title says exactly that. In this test environment, the intent is clearly WEB-4. I'll proceed with updating WEB-4's estimate to 3.

I found the issue WEB-4 "Off
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"mutation { issueUpdate(id: \"9a3181b9-b92c-4e82-8797-a7d742139006\", input: { estimate: 3 }) { id identifier title estimate } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'id' on type 'IssuePayload'.\",\"locations\":[{\"line\":1,\"column\":94}]},{\"message\":\"Cannot query field 'identifier' on type 'IssuePayload'.\",\"locations\":[{\"line\":1,\"column\":97}]},{\"message\":\"Cannot query field 'title' on type 'IssuePayload'.\",\"locations\":[{\"line\":1,\"column\":108}]},{\"message\":\"Cannot query field 'estimate' on type 'IssuePayload'.\",\"locations\":[{\"line\":1,\"column\":114}]}]}"}

#### Step 16
Reasoning: I'm trying to figure out what the IssuePayload return type structure looks like for the issueUpdate mutation.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ __type(name: \"IssuePayload\") { fields { name } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"fields\":[{\"name\":\"issue\"},{\"name\":\"lastSyncId\"},{\"name\":\"success\"}]}}}"}

#### Step 17
Reasoning: The mutation's selection should be `issue { ... }`, not direct fields. I'll retry.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"mutation { issueUpdate(id: \"9a3181b9-b92c-4e82-8797-a7d742139006\", input: { estimate: 3 }) { success issue { id identifier title estimate } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issueUpdate\":{\"success\":true,\"issue\":{\"id\":\"9a3181b9-b92c-4e82-8797-a7d742139006\",\"identifier\":\"WEB-4\",\"title\":\"Offline cache rollback for kiosk mode\",\"estimate\":3.0}}}}"}

#### Step 18
Reasoning: Done. Note: The description of this issue ("Refresh the kiosk layout on the home screen. No backend changes.") actually does not mention a rollback of the offline cache — it's included in the *title*. However, since this is the only Web Done issue that was completed on September 18 and relates to a rollback of the offline cache, WEB-4 is clearly the intended one. It's worth briefly noting this point.

Done — set **WEB-4 "Offline cache rollback for kiosk mode"** (Web team, Done, completed Sep 18 at 2:00 PM) to an estimate of **3**.

One note: the "offline cache rollback" mention is in that issue's *title*; its description text ("Kiosk layout refresh for the home screen…") doesn't actually reference it. It's the only Web Done issue from Sep 18 matching, so I'm confident it's the right one — but flagging in case you meant something else.
Command: 
Response: null

## Final answer
Done — set **WEB-4 "Offline cache rollback for kiosk mode"** (Web team, Done, completed Sep 18 at 2:00 PM) to an estimate of **3**.

One note: the "offline cache rollback" mention is in that issue's *title*; its description text ("Kiosk layout refresh for the home screen…") doesn't actually reference it. It's the only Web Done issue from Sep 18 matching, so I'm confident it's the right one — but flagging in case you meant something else.

## State diff
- UPDATE issues `9a3181b9-b92c-4e82-8797-a7d742139006`: {"estimate": [null, 3.0]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["9a3181b9-b92c-4e82-8797-a7d742139006"]}. Provisional outcome: incorrect. Provisional exposed facts: ['A:Issue.description'].

Give your verdict for this trial.