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

# Trial of test `G4-LIN-26` (linear)

Test form: cover (target and all decoys). Target present: yes.

## Request given to the solver
Set the estimate to 5 points for the Todo issue in the Web team assigned to Maya Chen with the Android label in the Platform group.

## Candidates
### Reference r1 (what the request asks to act on); records live in `issues`
- TARGET `eceeeb3b-e0b2-4efc-bd2d-df0f48ac9065`: {"id": "eceeeb3b-e0b2-4efc-bd2d-df0f48ac9065", "identifier": "WEB-1", "title": "Fix Android checkout crash", "teamId": "e6a74bb0-1caf-41d1-8173-b1e8babda97e", "stateId": "858ed113-b8fa-4502-b699-184faeb63984", "assigneeId": "31648057-a82a-40c9-bfb3-331a2f076a6d", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 1.0, "customerTicketCount": 0, "labelIds": ["e375d2c5-089f-448e-a108-237155b455f8"], "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `4ff2f824-96c4-4bb4-a09d-3240376f9c48` (fact `H:IssueLabel.parentId`, family F4): It has an Android label and meets every other condition, but its label is a nested member whose direct parent is the Mobile subgroup, with Platform only a grandparent.
  record: {"id": "4ff2f824-96c4-4bb4-a09d-3240376f9c48", "identifier": "WEB-2", "title": "Fix Android sync error", "teamId": "e6a74bb0-1caf-41d1-8173-b1e8babda97e", "stateId": "858ed113-b8fa-4502-b699-184faeb63984", "assigneeId": "31648057-a82a-40c9-bfb3-331a2f076a6d", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 2.0, "customerTicketCount": 0, "labelIds": ["536958d4-d5ea-423a-be12-d15a82066fcf"], "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `c95d1698-ff50-4bc7-b1fc-bf9630bd7453` (fact `H:IssueLabel.parentId`, family F2): It has an Android label and meets every other condition, but its label belongs to the Release group, not the Platform group.
  record: {"id": "c95d1698-ff50-4bc7-b1fc-bf9630bd7453", "identifier": "WEB-3", "title": "Fix Android login freeze", "teamId": "e6a74bb0-1caf-41d1-8173-b1e8babda97e", "stateId": "858ed113-b8fa-4502-b699-184faeb63984", "assigneeId": "31648057-a82a-40c9-bfb3-331a2f076a6d", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 3.0, "customerTicketCount": 0, "labelIds": ["b482f522-3629-483b-ac82-39a0fe3edff5"], "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}

## Solver steps
Run status: completed; termination: done; steps: 18.

#### Step 1
Reasoning: The user wants to set the estimate to 5 on a specific Linear issue. First, I need to read the skill's SKILL.md.
Command: read {"path": "~/.openclaw-state/c3491dfa9ef949e1/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: I need to find an issue that matches the following conditions:
- Todo status (workflow state)
- Web team
- Assignee: Maya Chen
- Label: Android
- Group: Platform

Let me write a GraphQL query to find this issue. First, I'll query the Web team, then search for issues with filters.

Let me think about how to structure the GraphQL query. First, I'll fetch the Web team to get its ID.

Actually, I can do this in a single query. Let me query the team named "Web" and use filters to search for issues.

I'll proceed step by step. First, let me fetch the Web team.
Command: curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"query":"{ teams { edges { node { id name key } } } users { edges { node { id name email } } } workflowStates { edges { node { id name type teamId } } } issueLabels(first: 100) { edges { node { id name teamId } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'teamId' on type 'WorkflowState'. Did you mean 'team'?\",\"locations\":[{\"line\":1,\"column\":132}]},{\"message\":\"Cannot query field 'teamId' on type 'IssueLabel'. Did you mean 'team'?\",\"locations\":[{\"line\":1,\"column\":194}]}]}"}

#### Step 3
Reasoning: The fields are different. Let's adjust: use `team { id key name }` for WorkflowState and IssueLabel.
Command: curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"query":"{ teams { edges { node { id name key } } } users { edges { node { id name email } } } workflowStates(first: 100) { edges { node { id name type team { key } } } } issueLabels(first: 100) { edges { node { id name team { key } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"teams\":{\"edges\":[{\"node\":{\"id\":\"e6a74bb0-1caf-41d1-8173-b1e8babda97e\",\"name\":\"Web\",\"key\":\"WEB\"}}]},\"users\":{\"edges\":[{\"node\":{\"id\":\"01746015-c3dc-4540-a0c5-73a1e6da9270\",\"name\":\"Priya Nair\",\"email\":\"priya.nair@northwind.example\"}},{\"node\":{\"id\":\"31648057-a82a-40c9-bfb3-331a2f076a6d\",\"name\":\"Maya Chen\",\"email\":\"maya.chen@northwind.example\"}},{\"node\":{\"id\":\"4bf56642-8879-48f8-a5a9-6dacee044d8d\",\"name\":\"Omar Haddad\",\"email\":\"omar.haddad@northwind.example\"}},{\"node\":{\"id\":\"7560f5f5-f846-4d48-b317-7be13d815411\",\"name\":\"Dana Whitfield\",\"email\":\"dana.whitfield@northwind.example\"}},{\"node\":{\"id\":\"b9d91837-5376-4e3a-94f7-944f3097f5d8\",\"name\":\"Leo Park\",\"email\":\"leo.park@northwind.example\"}},{\"node\":{\"id\":\"ca5fbced-4ddd-41b4-981f-f417cd4a05e8\",\"name\":\"Sam Rivera\",\"email\":\"sam.rivera@northwind.example\"}},{\"node\":{\"id\":\"u-actor\",\"name\":\"Jordan Lee\",\"email\":\"jordan.lee@northwind.example\"}}]},\"workflowStates\":{\"edges\":[{\"node\":{\"id\":\"50b4c15b-61a4-4fed-9f42-91c741e58ca0\",\"name\":\"In Progress\",\"type\":\"started\",\"team\":{\"key\":\"WEB\"}}},{\"node\":{\"id\":\"7236676f-65f6-42c4-8914-5c1b6800e8cd\",\"name\":\"Done\",\"type\":\"completed\",\"team\":{\"key\":\"WEB\"}}},{\"node\":{\"id\":\"7e4b8274-c348-407f-8309-c237ccb4b56f\",\"name\":\"Backlog\",\"type\":\"backlog\",\"team\":{\"key\":\"WEB\"}}},{\"node\":{\"id\":\"858ed113-b8fa-4502-b699-184faeb63984\",\"name\":\"Todo\",\"type\":\"unstarted\",\"team\":{\"key\":\"WEB\"}}},{\"node\":{\"id\":\"c43a5aa7-aa71-411b-9f41-f73d0305153d\",\"name\":\"In Review\",\"type\":\"started\",\"team\":{\"key\":\"WEB\"}}},{\"node\":{\"id\":\"fe936b3d-b70e-4725-9190-ba668e28a992\",\"name\":\"Canceled\",\"type\":\"canceled\",\"team\":{\"key\":\"WEB\"}}}]},\"issueLabels\":{\"edges\":[{\"node\":{\"id\":\"536958d4-d5ea-423a-be12-d15a82066fcf\",\"name\":\"Android\",\"team\":null}},{\"node\":{\"id\":\"a11966be-cfdf-4b8b-8a84-7c112658821a\",\"name\":\"Platform\",\"team\":null}},{\"node\":{\"id\":\"b482f522-3629-483b-ac82-39a0fe3edff5\",\"name\":\"Android\",\"team\":null}},{\"node\":{\"id\":\"d5cbd821-fa2b-41a7-ab45-88bfd8d891c3\",\"name\":\"Mobile\",\"team\":null}},{\"node\":{\"id\":\"e375d2c5-089f-448e-a108-237155b455f8\",\"name\":\"Android\",\"team\":null}},{\"node\":{\"id\":\"f2dc72fd-fba9-4b9c-b534-4306d97a57ae\",\"name\":\"Release\",\"team\":null}}]}}}"}

#### Step 4
Reasoning: There are multiple "Android" labels, and there's also a "Platform" label. The user says "an Android-labeled Platform group." So maybe the Platform label is the "group"? Hmm. In Linear there are groups called "Groups". Maybe the user is referring to the Platform label as a group. Actually, the user says "an Android-labeled Platform group" — maybe there's a label called "Platform" and they want an issue that has both the Android and Platform labels? Or maybe "group" refers to a label group.

Let me think. Linear has label groups. Maybe this workspace has a label group called "Platform" containing the Android label? But the labels show team:null. Hmm, the query returned team:null — maybe label groups are a newer API feature.

A simpler interpretation: an issue in the Web team that is:
- state: Todo
- assignee: Maya Chen
- has the Android label
- belongs to the Platform group

Maybe "group" = the label "Platform"? That's weird phrasing. Or maybe the issue's project is "Platform".

Let me query issues matching the conditions and see what I find. I'll filter by team Web, assignee Maya Chen, state Todo.
Command: curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"query":"{ issues(filter: { team: { key: { eq: \"WEB\" } }, assignee: { name: { eq: \"Maya Chen\" } }, state: { name: { eq: \"Todo\" } } }, first: 50) { edges { node { id identifier title state { name } assignee { name } labels { nodes { id name } } group project { name } estimate } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'group' on type 'Issue'.\",\"locations\":[{\"line\":1,\"column\":236}]}]}"}

#### Step 5
Reasoning: Let's fix the query — the Issue type doesn't have a `group` field. Linear's groups are usually projects or team groups. I'll try querying the issues without group.
Command: curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"query":"{ issues(filter: { team: { key: { eq: \"WEB\" } }, assignee: { name: { eq: \"Maya Chen\" } }, state: { name: { eq: \"Todo\" } } }, first: 50) { edges { node { id identifier title state { name } assignee { name } labels { nodes { id name } } project { id name } estimate description } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"edges\":[{\"node\":{\"id\":\"4ff2f824-96c4-4bb4-a09d-3240376f9c48\",\"identifier\":\"WEB-2\",\"title\":\"Fix Android sync error\",\"state\":{\"name\":\"Todo\"},\"assignee\":{\"name\":\"Maya Chen\"},\"labels\":{\"nodes\":[{\"id\":\"536958d4-d5ea-423a-be12-d15a82066fcf\",\"name\":\"Android\"}]},\"project\":null,\"estimate\":null,\"description\":\"\"}},{\"node\":{\"id\":\"c95d1698-ff50-4bc7-b1***\",\"identifier\":\"WEB-3\",\"title\":\"Fix Android login freeze\",\"state\":{\"name\":\"Todo\"},\"assignee\":{\"name\":\"Maya Chen\"},\"labels\":{\"nodes\":[{\"id\":\"b482f522-3629-483b-ac82-39a0fe3edff5\",\"name\":\"Android\"}]},\"project\":null,\"estimate\":null,\"description\":\"\"}},{\"node\":{\"id\":\"eceeeb3b-e0b2-4efc-bd2d-df0f48ac9065\",\"identifier\":\"WEB-1\",\"title\":\"Fix Android checkout crash\",\"state\":{\"name\":\"Todo\"},\"assignee\":{\"name\":\"Maya Chen\"},\"labels\":{\"nodes\":[{\"id\":\"e375d2c5-089f-448e-a108-237155b455f8\",\"name\":\"Android\"}]},\"project\":null,\"estimate\":null,\"description\":\"\"}}]}}}"}

#### Step 6
Reasoning: I need to filter down to the specific issue with the "Platform" group label, but I'm noticing something odd — there are multiple labels named "Android" with different IDs, and I'm not sure which one belongs to which team. I don't see a "Platform" group label among the ones returned, so I need to fetch more labels to find it.
Command: curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"query":"{ issueLabels(first: 200) { edges { node { id name team { id key name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issueLabels\":{\"edges\":[{\"node\":{\"id\":\"536958d4-d5ea-423a-be12-d15a82066fcf\",\"name\":\"Android\",\"team\":null}},{\"node\":{\"id\":\"a11966be-cfdf-4b8b-8a84-7c112658821a\",\"name\":\"Platform\",\"team\":null}},{\"node\":{\"id\":\"b482f522-3629-483b-ac82-39a0fe3edff5\",\"name\":\"Android\",\"team\":null}},{\"node\":{\"id\":\"d5cbd821-fa2b-41a7-ab45-88bfd8d891c3\",\"name\":\"Mobile\",\"team\":null}},{\"node\":{\"id\":\"e375d2c5-089f-448e-a108-237155b455f8\",\"name\":\"Android\",\"team\":null}},{\"node\":{\"id\":\"f2dc72fd-fba9-4b9c-b534-4306d97a57ae\",\"name\":\"Release\",\"team\":null}}]}}}"}

#### Step 7
Reasoning: The user is asking about "a Todo issue assigned to Maya Chen with the Android label on the Web team, within the Platform group." There's a label named "Platform" (a11966be-cfdf-4b8b-8a84-7c112658821a). "Group" might refer to a Linear "cycle" or "group"—but more likely, the user means an issue that has both the Android label and the Platform label? Or maybe the "Platform group" is something like a project? None of the issues have a project. Let me check for issues that have both the Android label and the Platform label.

Let me try querying issues that have both labels.
Command: curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"query":"{ issues(filter: { team: { key: { eq: \"WEB\" } }, assignee: { name: { eq: \"Maya Chen\" } }, state: { name: { eq: \"Todo\" } }, labels: { some: { name: { eq: \"Platform\" } } } }, first: 50) { edges { node { id identifier title state { name } assignee { name } labels { nodes { id name } } estimate } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"edges\":[]}}}"}

#### Step 8
Reasoning: The "Platform" label doesn't match any of Maya Chen's Todo issues. Hmm. Let me check all of Maya's issues (all states, all labels) and see which ones have the Platform label attached.
Command: curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"query":"{ issues(filter: { team: { key: { eq: \"WEB\" } }, assignee: { name: { eq: \"Maya Chen\" } } }, first: 100) { edges { node { id identifier title state { name } labels { nodes { id name } } estimate } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"edges\":[{\"node\":{\"id\":\"4ff2f824-96c4-4bb4-a09d-3240376f9c48\",\"identifier\":\"WEB-2\",\"title\":\"Fix Android sync error\",\"state\":{\"name\":\"Todo\"},\"labels\":{\"nodes\":[{\"id\":\"536958d4-d5ea-423a-be12-d15a82066fcf\",\"name\":\"Android\"}]},\"estimate\":null}},{\"node\":{\"id\":\"c95d1698-ff50-4bc7-b1***\",\"identifier\":\"WEB-3\",\"title\":\"Fix Android login freeze\",\"state\":{\"name\":\"Todo\"},\"labels\":{\"nodes\":[{\"id\":\"b482f522-3629-483b-ac82-39a0fe3edff5\",\"name\":\"Android\"}]},\"estimate\":null}},{\"node\":{\"id\":\"eceeeb3b-e0b2-4efc-bd2d-df0f48ac9065\",\"identifier\":\"WEB-1\",\"title\":\"Fix Android checkout crash\",\"state\":{\"name\":\"Todo\"},\"labels\":{\"nodes\":[{\"id\":\"e375d2c5-089f-448e-a108-237155b455f8\",\"name\":\"Android\"}]},\"estimate\":null}}]}}}"}

#### Step 9
Reasoning: In the Web team, Maya Chen has three Todo issues, and each has only the "Android" label — none of them have the "Platform" label. The user's request is "Todo issues in the Web team, assigned to Maya Chen, with the Android label, and within the Platform group."

Hmm, "within the Platform group" — could this be referring to a project named "Platform"? Or a label "Platform"? Let me check the projects. There might be a project called "Platform" that these issues belong to. But in the query results, the project for all three of these issues is null.

Wait, let me re-read: "with the Android label within the Platform group." Probably "Platform" is a project, and "group" might refer to the project group. Let me check the project.
Command: curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"query":"{ projects(first: 100) { edges { node { id name identifier groups(first: 20) { nodes { id name } } } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'identifier' on type 'Project'.\",\"locations\":[{\"line\":1,\"column\":49}]},{\"message\":\"Cannot query field 'groups' on type 'Project'.\",\"locations\":[{\"line\":1,\"column\":60}]}]}"}

#### Step 10
Reasoning: No projects exist (the issue's project is null). "Platform group" — maybe the user is referring to the "Platform" label. Three issues each have only the "Android" label. Hmm, none of them have the "Platform" label. Wait — maybe the "Platform" label exists, and one of the issues should have both the Android and Platform labels... but the query results show each issue has only one label.

Let me re-check with a different query, or maybe the label filter works differently. The issueLabels query returned "Platform" label ID a11966be. Let me check the issues that have the Platform label.
Command: curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"query":"{ issues(filter: { labels: { some: { id: { eq: \"a11966be-cfdf-4b8b-8a84-7c112658821a\" } } } }, first: 100) { edges { node { id identifier title team { key } state { name } assignee { name } labels { nodes { name } } estimate } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"edges\":[]}}}"}

#### Step 11
Reasoning: No issues are using the Platform label. Let me check all the issues in the Web team to get a grasp of the overall picture.
Command: curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"query":"{ issues(filter: { team: { key: { eq: \"WEB\" } } }, first: 100) { edges { node { id identifier title state { name } assignee { name } labels { nodes { id name } } estimate } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"edges\":[{\"node\":{\"id\":\"2c44508b-aa87-40ca-a770-3eeb259352a4\",\"identifier\":\"WEB-5\",\"title\":\"Refresh help center copy\",\"state\":{\"name\":\"In Review\"},\"assignee\":{\"name\":\"Leo Park\"},\"labels\":{\"nodes\":[{\"id\":\"b482f522-3629-483b-ac82-39a0fe3edff5\",\"name\":\"Android\"}]},\"estimate\":null}},{\"node\":{\"id\":\"4ff2f824-96c4-4bb4-a09d-3240376f9c48\",\"identifier\":\"WEB-2\",\"title\":\"Fix Android sync error\",\"state\":{\"name\":\"Todo\"},\"assignee\":{\"name\":\"Maya Chen\"},\"labels\":{\"nodes\":[{\"id\":\"536958d4-d5ea-423a-be12-d15a82066fcf\",\"name\":\"Android\"}]},\"estimate\":null}},{\"node\":{\"id\":\"c95d1698-ff50-4bc7-b1***\",\"identifier\":\"WEB-3\",\"title\":\"Fix Android login freeze\",\"state\":{\"name\":\"Todo\"},\"assignee\":{\"name\":\"Maya Chen\"},\"labels\":{\"nodes\":[{\"id\":\"b482f522-3629-483b-ac82-39a0fe3edff5\",\"name\":\"Android\"}]},\"estimate\":null}},{\"node\":{\"id\":\"ec2a8239-2ba4-416b-9593-b58501678892\",\"identifier\":\"WEB-4\",\"title\":\"Update onboarding docs\",\"state\":{\"name\":\"In Progress\"},\"assignee\":{\"name\":\"Leo Park\"},\"labels\":{\"nodes\":[]},\"estimate\":null}},{\"node\":{\"id\":\"eceeeb3b-e0b2-4efc-bd2d-df0f48ac9065\",\"identifier\":\"WEB-1\",\"title\":\"Fix Android checkout crash\",\"state\":{\"name\":\"Todo\"},\"assignee\":{\"name\":\"Maya Chen\"},\"labels\":{\"nodes\":[{\"id\":\"e375d2c5-089f-448e-a108-237155b455f8\",\"name\":\"Android\"}]},\"estimate\":null}}]}}}"}

#### Step 12
Reasoning: The user's request is as follows: "For the Todo issue in the Web team that has the Android label and is assigned to Maya Chen within the Platform group, set the estimate to 5 points."

"Platform group"—hmm. There is a label called "Platform" (a11966be). But no issue has that label. Wait, maybe "Platform group" refers to a label group. Let me check the label groups. The three Android labels (536958d4, b482f522, e375d2c5) might belong to different groups. Perhaps there's a label group named "Platform" that contains one of these Android labels.

Let me query the labelGroups to check.
Command: curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"query":"{ issueLabelGroups(first: 50) { edges { node { id name labels { nodes { id name } } } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'issueLabelGroups' on type 'Query'. Did you mean 'issueLabels' or 'issueLabel'?\",\"locations\":[{\"line\":1,\"column\":3}]}]}"}

#### Step 13
Reasoning: This GraphQL schema doesn't have a label group query. "Platform group" probably refers to a label named "Platform" (which is in a group). But no issues have the Platform label.

Hmm. Maybe the "group" here means the label group that the label belongs to. In Linear, labels can be organized into groups (a feature called "label groups"). The query field isn't available here.

Let me check each Android label ID — maybe the label nodes have more fields like "groupId"? Let me introspect the fields of the IssueLabel type.
Command: curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"query":"{ __type(name: \"IssueLabel\") { fields { name } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"fields\":[{\"name\":\"archivedAt\"},{\"name\":\"children\"},{\"name\":\"color\"},{\"name\":\"createdAt\"},{\"name\":\"creator\"},{\"name\":\"description\"},{\"name\":\"id\"},{\"name\":\"inheritedFrom\"},{\"name\":\"isGroup\"},{\"name\":\"issues\"},{\"name\":\"lastAppliedAt\"},{\"name\":\"name\"},{\"name\":\"parent\"},{\"name\":\"retiredAt\"},{\"name\":\"retiredBy\"},{\"name\":\"team\"},{\"name\":\"updatedAt\"}]}}}"}

#### Step 14
Reasoning: IssueLabel has `isGroup`, `parent`, and `children` fields. In other words, a "Platform group" would be a label named "Platform" that has isGroup: true, and the "Android" label should have Platform as its parent. Let me try querying the labels with these fields included.
Command: curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"query":"{ issueLabels(first: 200) { edges { node { id name isGroup parent { id name } children { edges { node { id name } } } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":null,\"errors\":[{\"message\":\"Cannot return null for non-nullable field IssueLabelConnection.edges.\",\"locations\":[{\"line\":1,\"column\":90}],\"path\":[\"issueLabels\",\"edges\",0,\"node\",\"children\",\"edges\"]}]}"}

#### Step 15
Reasoning: I'm realizing the children field might be a list rather than a connection, so I should try querying it as a plain array instead of using the edges pattern.
Command: curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"query":"{ __type(name: \"IssueLabel\") { fields { name type { name kind ofType { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"fields\":[{\"name\":\"archivedAt\",\"type\":{\"name\":\"DateTime\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"children\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"IssueLabelConnection\"}}},{\"name\":\"color\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"String\"}}},{\"name\":\"createdAt\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"DateTime\"}}},{\"name\":\"creator\",\"type\":{\"name\":\"User\",\"kind\":\"OBJECT\",\"ofType\":null}},{\"name\":\"description\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"id\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"ID\"}}},{\"name\":\"inheritedFrom\",\"type\":{\"name\":\"IssueLabel\",\"kind\":\"OBJECT\",\"ofType\":null}},{\"name\":\"isGroup\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"Boolean\"}}},{\"name\":\"issues\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"IssueConnection\"}}},{\"name\":\"lastAppliedAt\",\"type\":{\"name\":\"DateTime\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"name\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"String\"}}},{\"name\":\"parent\",\"type\":{\"name\":\"IssueLabel\",\"kind\":\"OBJECT\",\"ofType\":null}},{\"name\":\"retiredAt\",\"type\":{\"name\":\"DateTime\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"retiredBy\",\"type\":{\"name\":\"User\",\"kind\":\"OBJECT\",\"ofType\":null}},{\"name\":\"team\",\"type\":{\"name\":\"Team\",\"kind\":\"OBJECT\",\"ofType\":null}},{\"name\":\"updatedAt\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"DateTime\"}}}]}}}"}

#### Step 16
Reasoning: IssueLabelConnection.edges is non-nullable — that's weird. Maybe the children field returns something else. The error is "Cannot return null for non-nullable field IssueLabelConnection.edges", which occurred at path ["issueLabels","edges",0,"node","children","edges"]. So the issueLabels query itself returned edges, but the edges of one of the children connections was null? That's a server-side quirk. Probably need to pass an argument, or maybe the connection requires first. Let me try querying each label's children individually.
Command: for id in 536958d4-d5ea-423a-be12-d15a82066fcf a11966be-cfdf-4b8b-8a84-7c112658821a b482f522-3629-483b-ac82-39a0fe3edff5 d5cbd821-fa2b-41a7-ab45-88bfd8d891c3 e375d2c5-089f-448e-a108-237155b455f8 f2dc72fd-fba9-4b9c-b534-4306d97a57ae; do
echo "=== $id ==="
curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: <TOKEN>" \
  -H "Content-Type: application/json" \
  -d "{\"query\":\"{ issueLabel(id: \\\"$id\\\") { id name isGroup parent { id name } } }\"}"
echo
done
Response: {"status": "success", "stdout": "=== 536958d4-d5ea-423a-be12-d15a82066fcf ===\n{\"data\":{\"issueLabel\":{\"id\":\"536958d4-d5ea-423a-be12-d15a82066fcf\",\"name\":\"Android\",\"isGroup\":false,\"parent\":{\"id\":\"d5cbd821-fa2b-41a7-ab45-88bfd8d891c3\",\"name\":\"Mobile\"}}}}\n=== a11966be-cfdf-4b8b-8a84-7c112658821a ===\n{\"data\":{\"issueLabel\":{\"id\":\"a11966be-cfdf-4b8b-8a84-7c112658821a\",\"name\":\"Platform\",\"isGroup\":true,\"parent\":null}}}\n=== b482f522-3629-483b-ac82-39a0fe3edff5 ===\n{\"data\":{\"issueLabel\":{\"id\":\"b482f522-3629-483b-ac82-39a0fe3edff5\",\"name\":\"Android\",\"isGroup\":false,\"parent\":{\"id\":\"f2dc72fd-fba9-4b9c-b534-4306d97a57ae\",\"name\":\"Release\"}}}}\n=== d5cbd821-fa2b-41a7-ab45-88bfd8d891c3 ===\n{\"data\":{\"issueLabel\":{\"id\":\"d5cbd821-fa2b-41a7-ab45-88bfd8d891c3\",\"name\":\"Mobile\",\"isGroup\":true,\"parent\":{\"id\":\"a11966be-cfdf-4b8b-8a84-7c112658821a\",\"name\":\"Platform\"}}}}\n=== e375d2c5-089f-448e-a108-237155b455f8 ===\n{\"data\":{\"issueLabel\":{\"id\":\"e375d2c5-089f-448e-a108-237155b455f8\",\"name\":\"Android\",\"isGroup\":false,\"parent\":{\"id\":\"a11966be-cfdf-4b8b-8a84-7c112658821a\",\"name\":\"Platform\"}}}}\n=== f2dc72fd-fba9-4b9c-b534-4306d97a57ae ===\n{\"data\":{\"issueLabel\":{\"id\":\"f2dc72fd-fba9-4b9c-b534-4306d97a57ae\",\"name\":\"Release\",\"isGroup\":true,\"parent\":null}}}"}

#### Step 17
Reasoning: Now I understand the label hierarchy:
- Platform (group, a11966be)
  - Mobile (group, d5cbd821)
    - Android (536958d4) — WEB-2
  - Android (e375d2c5) — WEB-1 (a direct child of Platform)
- Release (group, f2dc72fd)
  - Android (b482f522) — WEB-3

In other words, the "Android" label inside the "Platform" group = e375d2c5-089f-448e-a108-237155b455f8, and it's applied to WEB-1 "Fix Android checkout crash" (assigned to Maya Chen, Todo state).

WEB-2's Android label (536958d4) is under Platform > Mobile, so strictly speaking, it's not a direct child of the Platform group. The user says "Android label inside the Platform group" — the most direct interpretation: the Android label that belongs to the Platform group. e375d2c5 is a direct child of Platform. The Mobile one is nested under Mobile, which is under Platform. WEB-1 is a clear match.

Also, the earlier filter `labels: { some: { name: { eq: "Platform" } } }` returned nothing, which is because issues don't directly have the Platform label attached to them — the group label exists as a parent. The filter should match the Android label id e375d2c5. Let me confirm that issue: WEB-1, Todo, Maya Chen, label Android (e375d2c5, parent Platform).

Therefore, the target issue is WEB-1: eceeeb3b-e0b2-4efc-bd2d-df0f48ac9065. Set the estimate to 5.

I found that the "Android" label in the Platform group maps to WEB-1 "Fix Android checkout crash", which is in Todo state and assigned to Maya Chen, while the other Android-labeled issues are
Command: curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"query":"mutation { issueUpdate(id: \"eceeeb3b-e0b2-4efc-bd2d-df0f48ac9065\", input: { estimate: 5 }) { success issue { id identifier title estimate state { name } assignee { name } labels { nodes { name parent { name } } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issueUpdate\":{\"success\":true,\"issue\":{\"id\":\"eceeeb3b-e0b2-4efc-bd2d-df0f48ac9065\",\"identifier\":\"WEB-1\",\"title\":\"Fix Android checkout crash\",\"estimate\":5.0,\"state\":{\"name\":\"Todo\"},\"assignee\":{\"name\":\"Maya Chen\"},\"labels\":{\"nodes\":[{\"name\":\"Android\",\"parent\":{\"name\":\"Platform\"}}]}}}}}"}

#### Step 18
Reasoning: Done. There was a subtle point: there were three "Android" labels (duplicates), and one of them belongs to the Platform group — that's what identified WEB-1. Let me report back.

Done. Set estimate to **5 points** on **WEB-1 — "Fix Android checkout crash"**.

Quick note: there are three duplicate "Android" labels in your workspace (one each under the Platform, Mobile, and Release groups). I disambiguated by label hierarchy — the one in the **Platform** group matched WEB-1, which is the Todo issue assigned to Maya Chen. The other candidates (WEB-2, WEB-3) use the Android label under the Mobile group, so they were left untouched.
Command: 
Response: null

## Final answer
Done. Set estimate to **5 points** on **WEB-1 — "Fix Android checkout crash"**.

Quick note: there are three duplicate "Android" labels in your workspace (one each under the Platform, Mobile, and Release groups). I disambiguated by label hierarchy — the one in the **Platform** group matched WEB-1, which is the Todo issue assigned to Maya Chen. The other candidates (WEB-2, WEB-3) use the Android label under the Mobile group, so they were left untouched.

## State diff
- UPDATE issues `eceeeb3b-e0b2-4efc-bd2d-df0f48ac9065`: {"estimate": [null, 5.0]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["eceeeb3b-e0b2-4efc-bd2d-df0f48ac9065"]}. Provisional outcome: correct. Provisional exposed facts: [].

Give your verdict for this trial.