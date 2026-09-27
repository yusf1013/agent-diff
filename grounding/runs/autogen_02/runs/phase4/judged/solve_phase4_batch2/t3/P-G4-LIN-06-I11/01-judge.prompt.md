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

# Trial of test `P-G4-LIN-06-I11` (linear)

Test form: probe. Target present: no.

## Request given to the solver
Set the estimate to 3 for the Todo issue assigned to Maya Chen in the Web team with the Bug label from the Web team. If there isn't one, just tell me.

## Candidates
### Reference r1 (what the request asks to act on); records live in `issues`
- No target: no record meets this reference.
- DECOY `i-d1` (fact `R:issue_label_issue_association`, family F2): It meets team, assignee and state, but the Bug label from the Web team is only on its parent issue, not on the issue itself.
  record: {"id": "i-d1", "identifier": "WEB-3", "title": "Search results pagination broken", "teamId": "t-web", "stateId": "t-web-st-1", "assigneeId": "u-maya", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 3.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "parentId": "i-parent"}

## Solver steps
Run status: completed; termination: done; steps: 9.

#### Step 1
Reasoning: I need to find a specific issue with these criteria:
- Workflow state: "Todo"
- Assigned to: Maya Chen
- Team: Web
- Label: Bug (from the Web team)

Let me start by querying for the Web team, Maya Chen, and the Todo state to get their IDs.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{
  "query": "{
    teams { nodes { id name key } }
    users { nodes { id name email } }
  }"
}'
Response: {"status": "success", "stdout": "Request body is not a valid JSON", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_e400e297ea0c44359001609aca104afa_uhkasnxj"}

#### Step 2
Reasoning: I had a JSON syntax error - missing a closing brace. Let me fix that.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ teams { nodes { id name key } } users { nodes { id name email } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"teams\":{\"nodes\":[{\"id\":\"t-mob\",\"name\":\"Mobile\",\"key\":\"MOB\"},{\"id\":\"t-web\",\"name\":\"Web\",\"key\":\"WEB\"}]},\"users\":{\"nodes\":[{\"id\":\"u-actor\",\"name\":\"Jordan Lee\",\"email\":\"jordan.lee@northwind.example\"},{\"id\":\"u-dana\",\"name\":\"Dana Whitfield\",\"email\":\"dana.whitfield@northwind.example\"},{\"id\":\"u-leo\",\"name\":\"Leo Park\",\"email\":\"leo.park@northwind.example\"},{\"id\":\"u-maya\",\"name\":\"Maya Chen\",\"email\":\"maya.chen@northwind.example\"},{\"id\":\"u-omar\",\"name\":\"Omar Haddad\",\"email\":\"omar.haddad@northwind.example\"},{\"id\":\"u-priya\",\"name\":\"Priya Nair\",\"email\":\"priya.nair@northwind.example\"},{\"id\":\"u-sam\",\"name\":\"Sam Rivera\",\"email\":\"sam.rivera@northwind.example\"}]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_e400e297ea0c44359001609aca104afa_uhkasnxj"}

#### Step 3
Reasoning: I have the Web team ID (t-web) and Maya Chen's user ID (u-maya). Now I need to find the "Todo" workflow state and the "Bug" label from the Web team.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ workflowStates { nodes { id name teamId } } issueLabels { nodes { id name teamId } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'teamId' on type 'WorkflowState'. Did you mean 'team'?\",\"locations\":[{\"line\":1,\"column\":36}]},{\"message\":\"Cannot query field 'teamId' on type 'IssueLabel'. Did you mean 'team'?\",\"locations\":[{\"line\":1,\"column\":77}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_e400e297ea0c44359001609aca104afa_uhkasnxj"}

#### Step 4
Reasoning: The fields are nested under `team` rather than being `teamId` directly. Let me fix the query.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ workflowStates { nodes { id name team { id } } } issueLabels { nodes { id name team { id } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"workflowStates\":{\"nodes\":[{\"id\":\"t-mob-st-0\",\"name\":\"Backlog\",\"team\":{\"id\":\"t-mob\"}},{\"id\":\"t-mob-st-1\",\"name\":\"Todo\",\"team\":{\"id\":\"t-mob\"}},{\"id\":\"t-mob-st-2\",\"name\":\"In Progress\",\"team\":{\"id\":\"t-mob\"}},{\"id\":\"t-mob-st-3\",\"name\":\"In Review\",\"team\":{\"id\":\"t-mob\"}},{\"id\":\"t-mob-st-4\",\"name\":\"Done\",\"team\":{\"id\":\"t-mob\"}},{\"id\":\"t-mob-st-5\",\"name\":\"Canceled\",\"team\":{\"id\":\"t-mob\"}},{\"id\":\"t-web-st-0\",\"name\":\"Backlog\",\"team\":{\"id\":\"t-web\"}},{\"id\":\"t-web-st-1\",\"name\":\"Todo\",\"team\":{\"id\":\"t-web\"}},{\"id\":\"t-web-st-2\",\"name\":\"In Progress\",\"team\":{\"id\":\"t-web\"}},{\"id\":\"t-web-st-3\",\"name\":\"In Review\",\"team\":{\"id\":\"t-web\"}},{\"id\":\"t-web-st-4\",\"name\":\"Done\",\"team\":{\"id\":\"t-web\"}},{\"id\":\"t-web-st-5\",\"name\":\"Canceled\",\"team\":{\"id\":\"t-web\"}}]},\"issueLabels\":{\"nodes\":[{\"id\":\"2d294ae9-6079-5fa9-8704-8177f6e12778\",\"name\":\"Bug\",\"team\":{\"id\":\"t-web\"}},{\"id\":\"90cff729-4331-52ca-bb49-8039cc0ee33b\",\"name\":\"Feature\",\"team\":{\"id\":\"t-web\"}},{\"id\":\"eefe992a-946f-536d-90ea-2cdc686d165f\",\"name\":\"Bug\",\"team\":{\"id\":\"t-mob\"}}]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_e400e297ea0c44359001609aca104afa_uhkasnxj"}

#### Step 5
Reasoning: Now I have all the IDs:
- Web team: t-web
- Maya Chen: u-maya
- Todo state (Web team): t-web-st-1
- Bug label (Web team): 2d294ae9-6079-5fa9-8704-8177f6e12778

Let me query for issues matching all these criteria.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ issues(filter: { state: { id: { eq: \"t-web-st-1\" } }, assignee: { id: { eq: \"u-maya\" } }, team: { id: { eq: \"t-web\" } }, labels: { id: { eq: \"2d294ae9-6079-5fa9-8704-8177f6e12778\" } } }) { nodes { id identifier title estimate state { name } assignee { name } team { name } labels { nodes { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_e400e297ea0c44359001609aca104afa_uhkasnxj"}

#### Step 6
Reasoning: No issues found with all four criteria. Let me broaden the search to verify - let me check if there are any issues assigned to Maya Chen in the Web team with the Bug label (without the state filter), to confirm the filter is working and just the combination doesn't exist.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ issues(filter: { assignee: { id: { eq: \"u-maya\" } }, team: { id: { eq: \"t-web\" } }, labels: { id: { eq: \"2d294ae9-6079-5fa9-8704-8177f6e12778\" } } }) { nodes { id identifier title estimate state { name } assignee { name } team { name } labels { nodes { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_e400e297ea0c44359001609aca104afa_uhkasnxj"}

#### Step 7
Reasoning: Still no results even without the state filter. Let me check if Maya Chen has any issues in the Web team at all, to be thorough.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ issues(filter: { assignee: { id: { eq: \"u-maya\" } }, team: { id: { eq: \"t-web\" } } }) { nodes { id identifier title estimate state { name } assignee { name } team { name } labels { nodes { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"i-d1\",\"identifier\":\"WEB-3\",\"title\":\"Search results pagination broken\",\"estimate\":null,\"state\":{\"name\":\"Todo\"},\"assignee\":{\"name\":\"Maya Chen\"},\"team\":{\"name\":\"Web\"},\"labels\":{\"nodes\":[]}}]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_e400e297ea0c44359001609aca104afa_uhkasnxj"}

#### Step 8
Reasoning: Maya Chen has one issue in the Web team: WEB-3 "Search results pagination broken" which is in the "Todo" state, but it has no labels - so it doesn't have the "Bug" label from the Web team.

Let me also check if there are any Web team issues in Todo state with the Bug label to confirm.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ issues(filter: { state: { id: { eq: \"t-web-st-1\" } }, team: { id: { eq: \"t-web\" } }, labels: { id: { eq: \"2d294ae9-6079-5fa9-8704-8177f6e12778\" } } }) { nodes { id identifier title estimate state { name } assignee { name } team { name } labels { nodes { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_e400e297ea0c44359001609aca104afa_uhkasnxj"}

#### Step 9
Reasoning: I've thoroughly checked and confirmed that there is no issue matching all the specified criteria:
- State: Todo ✓ (WEB-3 is in Todo)
- Assigned to: Maya Chen ✓ (WEB-3 is assigned to Maya Chen)
- Team: Web ✓ (WEB-3 is in the Web team)
- Label: Bug (Web team) ✗ (WEB-3 has NO labels)

The only issue Maya Chen has in the Web team is WEB-3 "Search results pagination broken", which is in the Todo state but does not have the "Bug" label. No Web team issue in the Todo state has the Bug label at all.

So I should inform the user that no such issue exists.


<done>
There is no issue that matches all the specified criteria. The only issue assigned to Maya Chen in the Web team is **WEB-3** ("Search results pagination broken"), which is in the "Todo" state but has **no labels** — so it does not carry the "Bug" label from the Web team. There are also no other Web team issues in the "Todo" state with the "Bug" label. No estimate was updated.
</done>
Command: 
Response: null

## Final answer
There is no issue that matches all the specified criteria. The only issue assigned to Maya Chen in the Web team is **WEB-3** ("Search results pagination broken"), which is in the "Todo" state but has **no labels** — so it does not carry the "Bug" label from the Web team. There are also no other Web team issues in the "Todo" state with the "Bug" label. No estimate was updated.

## State diff
(no changes)

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": []}. Provisional outcome: correct_absent. Provisional exposed facts: [].

Give your verdict for this trial.