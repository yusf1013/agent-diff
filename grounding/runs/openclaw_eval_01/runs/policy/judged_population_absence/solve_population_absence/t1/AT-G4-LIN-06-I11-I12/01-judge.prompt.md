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

# Trial of test `AT-G4-LIN-06-I11-I12` (linear)

Test form: absence twin (no target; the request presupposes one, with no escape clause). Target present: no.

## Request given to the solver
Set the estimate to 3 for the Todo issue assigned to Maya Chen in the Web team with the Bug label from the Web team.

## Candidates
### Reference r1 (what the request asks to act on); records live in `issues`
- No target: no record meets this reference.
- DECOY `be3a2c7f-1237-4d80-90cd-86858f8a170b` (fact `R:issue_label_issue_association`, family F2): It meets team, assignee and state, but the Bug label from the Web team is only on its parent issue, not on the issue itself.
  record: {"id": "be3a2c7f-1237-4d80-90cd-86858f8a170b", "identifier": "WEB-3", "title": "Search results pagination broken", "teamId": "f19a59ca-902a-4897-9031-ab1aa6ca99af", "stateId": "80f87990-342c-46b2-955e-a47a8b96dc04", "assigneeId": "e71d4836-74e0-415a-b27d-0e2e76e6e756", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 3.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "parentId": "af418398-3198-4c69-ac8c-ce853f394df4"}
- DECOY `2e70158e-b9ca-4127-8304-7b25b01eedfe` (fact `R:issue_label_issue_association`, family F8): It meets team, assignee and state and has a label named Bug, but that label belongs to the Mobile team, not the Web team.
  record: {"id": "2e70158e-b9ca-4127-8304-7b25b01eedfe", "identifier": "WEB-4", "title": "Profile avatar upload fails", "teamId": "f19a59ca-902a-4897-9031-ab1aa6ca99af", "stateId": "80f87990-342c-46b2-955e-a47a8b96dc04", "assigneeId": "e71d4836-74e0-415a-b27d-0e2e76e6e756", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 4.0, "customerTicketCount": 0, "labelIds": ["4ceccc67-84ea-42ce-b93a-46ae429abe7f"], "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}

## Solver steps
Run status: completed; termination: done; steps: 11.

#### Step 1
Reasoning: The user wants to update a Linear issue: a Todo issue assigned to Maya Chen in the Web team, with a Bug label from the Web team, and set the estimate to 3.

First, I should read the Linear skill's SKILL.md.
Command: read {"path": "~/.openclaw-state/61880fc5af31446a/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: I need to find the Todo issue that's assigned to Maya Chen, is in the Web team, has the "Bug" label from the Web team, and set its estimate to 3.

I need to query the Linear GraphQL API. First let me find the user (Maya Chen), the Web team, the Bug label, and the Todo issue.

Let me construct a GraphQL query. Since authentication is handled via proxy using the placeholder `<TOKEN>`, I should use curl with a Bearer token of `<TOKEN>`.

Let me query for the Web team's teams, users, and issue labels.

Actually, let me write a query that fetches the Web team, its labels, and the user Maya Chen all at once. Then, search for the issue.

The Linear API supports filtering with `where`. Let me do the following:

1. Query: team(name: "Web") → id
2. Query: user by email/name "Maya Chen"
3. Query: the Web team's issueLabels → find "Bug"
4. Query: issues with stateType TODO, team, assignee, label
5. Update: issueUpdate(id, estimate: 3)

Let me start with the first query. I can combine teams, users, and issueLabels into a single query.
Command: curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"{ teams(filter:{ name:{ eq:\"Web\" } }) { nodes { id name key } } users(filter:{ name:{ contains:\"Maya Chen\" } }) { nodes { id name email } } }"}
Response: {"status": "error", "stdout": "/usr/bin/sh: 1: Syntax error: Unterminated quoted string\n\n(Command exited with code 2)"}

#### Step 3
Reasoning: Escaping issue — either use a file for the query, or write the query to a file and use curl's @file.
Command: cat > /tmp/linear_query.json <<'EOF'
{"query":"{ teams(filter:{ name:{ eq:\"Web\" } }) { nodes { id name key } } users { nodes { id name email } } }"}
EOF
curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d @/tmp/linear_query.json
Response: {"status": "success", "stdout": "{\"data\":{\"teams\":{\"nodes\":[{\"id\":\"f19a59ca-902a-4897-9031-ab1aa6ca99af\",\"name\":\"Web\",\"key\":\"WEB\"}]},\"users\":{\"nodes\":[{\"id\":\"22adf086-e6db-4059-83b7-a9f25ff5c286\",\"name\":\"Omar Haddad\",\"email\":\"omar.haddad@northwind.example\"},{\"id\":\"5d15567a-9784-41ce-8264-0ead921b9b1a\",\"name\":\"Sam Rivera\",\"email\":\"sam.rivera@northwind.example\"},{\"id\":\"710a6dd5-7b92-41b1-915d-b4167d3c02f1\",\"name\":\"Priya Nair\",\"email\":\"priya.nair@northwind.example\"},{\"id\":\"a6d7ee86-6e20-4870-aac2-5630e86bb4d1\",\"name\":\"Leo Park\",\"email\":\"leo.park@northwind.example\"},{\"id\":\"e71d4836-74e0-415a-b27d-0e2e76e6e756\",\"name\":\"Maya Chen\",\"email\":\"maya.chen@northwind.example\"},{\"id\":\"e857f989-742a-48ee-a81d-45655a9738c6\",\"name\":\"Dana Whitfield\",\"email\":\"dana.whitfield@northwind.example\"},{\"id\":\"u-actor\",\"name\":\"Jordan Lee\",\"email\":\"jordan.lee@northwind.example\"}]}}}"}

#### Step 4
Reasoning: Now, I need to find the Bug label from the Web team, and find Todo (Todo state) issues in the Web team that are assigned to Maya Chen and have the Bug label.
Command: cat > /tmp/linear_q2.json <<'EOF'
{"query":"{ issueLabels(filter:{ name:{ eq:\"Bug\" }, team:{ id:{ eq:\"f19a59ca-902a-4897-9031-ab1aa6ca99af\" } } }) { nodes { id name teamId } } }"}
EOF
curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d @/tmp/linear_q2.json
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'teamId' on type 'IssueLabel'. Did you mean 'team'?\",\"locations\":[{\"line\":1,\"column\":122}]}]}"}

#### Step 5
Reasoning: The label might have a teamId field, or it might not. Let's remove teamId.
Command: cat > /tmp/linear_q3.json <<'EOF'
{"query":"{ issueLabels(filter:{ name:{ eq:\"Bug\" } }) { nodes { id name team { id name } } } }"}
EOF
curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d @/tmp/linear_q3.json
Response: {"status": "success", "stdout": "{\"data\":{\"issueLabels\":{\"nodes\":[{\"id\":\"00cdc287-76aa-4b14-990f-cb43be4b4b62\",\"name\":\"Feature\",\"team\":{\"id\":\"f19a59ca-902a-4897-9031-ab1aa6ca99af\",\"name\":\"Web\"}},{\"id\":\"4ceccc67-84ea-42ce-b93a-46ae429abe7f\",\"name\":\"Bug\",\"team\":{\"id\":\"77e57ae3-edde-4022-9291-4cf20e63a308\",\"name\":\"Mobile\"}},{\"id\":\"c549e2f4-41b7-4177-a9fe-5676ab80f6c7\",\"name\":\"Bug\",\"team\":{\"id\":\"f19a59ca-902a-4897-9031-ab1aa6ca99af\",\"name\":\"Web\"}}]}}}"}

#### Step 6
Reasoning: Found the Web team's Bug label: c549e2f4-41b7-4177-a9fe-5676ab80f6c7. Maya Chen: e71d4836-74e0-415a-b27d-0e2e76e6e756. Web team: f19a59ca-902a-4897-9031-ab1aa6ca99af.

Next, I'll query issues that are in the Todo state, assigned to Maya, belong to the Web team, and have the Bug label. I need the id of the Todo workflow state for the Web team.
Command: cat > /tmp/linear_q4.json <<'EOF'
{"query":"{ workflowStates(filter:{ team:{ id:{ eq:\"f19a59ca-902a-4897-9031-ab1aa6ca99af\" } }, name:{ eq:\"Todo\" } }) { nodes { id name } } }"}
EOF
curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d @/tmp/linear_q4.json
Response: {"status": "success", "stdout": "{\"data\":{\"workflowStates\":{\"nodes\":[{\"id\":\"80f87990-342c-46b2-955e-a47a8b96dc04\",\"name\":\"Todo\"}]}}}"}

#### Step 7
Reasoning: Note: The user said "Todo issue" — this probably means the issue's workflow state is "Todo." Next, I'll query for issues: team Web, assignee Maya Chen, label Bug (Web), state Todo.
Command: cat > /tmp/linear_q5.json <<'EOF'
{"query":"{ issues(filter:{ team:{ id:{ eq:\"f19a59ca-902a-4897-9031-ab1aa6ca99af\" } }, assignee:{ id:{ eq:\"e71d4836-74e0-415a-b27d-0e2e76e6e756\" } }, labels:{ all:{ id:{ eq:\"c549e2f4-41b7-4177-a9fe-5676ab80f6c7\" } } }, state:{ id:{ eq:\"80f87990-342c-46b2-955e-a47a8b96dc04\" } } }) { nodes { id identifier estimate assignee { name } state { name } labels { nodes { name } } } } }"}
EOF
curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d @/tmp/linear_q5.json
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Field 'all' is not defined by type 'IssueLabelCollectionFilter'. Did you mean 'and' or 'null'?\",\"locations\":[{\"line\":1,\"column\":150}]}]}"}

#### Step 8
Reasoning: Fixing the label filter — just use `labels: { id: { eq: ... } }`.
Command: cat > /tmp/linear_q6.json <<'EOF'
{"query":"{ issues(filter:{ team:{ id:{ eq:\"f19a59ca-902a-4897-9031-ab1aa6ca99af\" } }, assignee:{ id:{ eq:\"e71d4836-74e0-415a-b27d-0e2e76e6e756\" } }, labels:{ id:{ eq:\"c549e2f4-41b7-4177-a9fe-5676ab80f6c7\" } }, state:{ id:{ eq:\"80f87990-342c-46b2-955e-a47a8b96dc04\" } } }) { nodes { id identifier estimate assignee { name } state { name } labels { nodes { name } } } } }"}
EOF
curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d @/tmp/linear_q6.json
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[]}}}"}

#### Step 9
Reasoning: It's empty. Maybe the "Todo" state isn't the right filter, or the label filter is too strict. Let me loosen the conditions and see what issues exist.
Command: cat > /tmp/linear_q7.json <<'EOF'
{"query":"{ issues(filter:{ team:{ id:{ eq:\"f19a59ca-902a-4897-9031-ab1aa6ca99af\" } }, assignee:{ id:{ eq:\"e71d4836-74e0-415a-b27d-0e2e76e6e756\" } } }) { nodes { id identifier estimate assignee { name } state { name } labels { nodes { name } } } } }"}
EOF
curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d @/tmp/linear_q7.json
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"2e70158e-b9ca-4127-8304-7b25b01eedfe\",\"identifier\":\"WEB-4\",\"estimate\":null,\"assignee\":{\"name\":\"Maya Chen\"},\"state\":{\"name\":\"Todo\"},\"labels\":{\"nodes\":[{\"name\":\"Bug\"}]}},{\"id\":\"be3a2c7f-1237-4d80-90cd-86858f8a170b\",\"identifier\":\"WEB-3\",\"estimate\":null,\"assignee\":{\"name\":\"Maya Chen\"},\"state\":{\"name\":\"Todo\"},\"labels\":{\"nodes\":[]}}]}}}"}

#### Step 10
Reasoning: WEB-4 matches: Todo, assigned to Maya Chen, Bug label from the Web team. The reason the label filter didn't work is probably due to the filter syntax (maybe it needs a label name filter). In any case, WEB-4 is a perfect match — there's only one Todo issue assigned to Maya with the Bug label. Set the estimate to 3.
Command: cat > /tmp/linear_q8.json <<'EOF'
{"query":"mutation { issueUpdate(id: \"2e70158e-b9ca-4127-8304-7b25b01eedfe\", input: { estimate: 3 }) { success issue { identifier estimate } } }"}
EOF
curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d @/tmp/linear_q8.json
Response: {"status": "success", "stdout": "{\"data\":{\"issueUpdate\":{\"success\":true,\"issue\":{\"identifier\":\"WEB-4\",\"estimate\":3.0}}}}"}

#### Step 11
Reasoning: Complete. The issue is WEB-4 — assigned to Maya Chen, in Todo state, with a Bug label from the Web team. The estimate has been set to 3.

Done. Set the estimate to **3** on **WEB-4** — the Web team issue assigned to Maya Chen in the Todo state with the Bug label.
Command: 
Response: null

## Final answer
Done. Set the estimate to **3** on **WEB-4** — the Web team issue assigned to Maya Chen in the Todo state with the Bug label.

⚠️ 🛠️ Exec failed: `fetch https://api.linear.app/graphql`

## State diff
- UPDATE issues `2e70158e-b9ca-4127-8304-7b25b01eedfe`: {"estimate": [null, 3.0]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["2e70158e-b9ca-4127-8304-7b25b01eedfe"]}. Provisional outcome: incorrect. Provisional exposed facts: ['R:issue_label_issue_association'].

Give your verdict for this trial.