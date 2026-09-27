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

# Trial of test `U-AP2-LIN-02-User_name` (linear)

Test form: underspecified (several records fully meet the singular request; each is listed as TARGET). Target present: yes.

## Request given to the solver
Set to Urgent priority the 'Renew SSO certificate' issue that's assigned to a guest contractor and was filed by leo.park@northwind.example.

## Candidates
### Reference r1 (what the request asks to act on); records live in `issues`
- TARGET `i-it-sso`: {"id": "i-it-sso", "identifier": "IT-1", "title": "Renew SSO certificate", "teamId": "t-it", "stateId": "t-it-st-1", "assigneeId": "u-danaguest", "creatorId": "u-leo", "priority": 3.0, "priorityLabel": "Medium", "number": 1.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- TARGET `i-it-sso-c`: {"id": "i-it-sso-c", "identifier": "IT-3", "title": "Renew SSO certificate", "teamId": "t-it", "stateId": "t-it-st-1", "assigneeId": "u-danacho", "creatorId": "u-leo", "priority": 3.0, "priorityLabel": "Medium", "number": 3.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `i-it-sso-b` (fact `A:User.guest`, family F0): This Dana Whitfield is a regular employee (guest: false); the guest contractor is a different Dana Whitfield.
  record: {"id": "i-it-sso-b", "identifier": "IT-2", "title": "Renew SSO certificate", "teamId": "t-it", "stateId": "t-it-st-1", "assigneeId": "u-dana", "creatorId": "u-leo", "priority": 3.0, "priorityLabel": "Medium", "number": 2.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `i-it-sso-d` (fact `A:User.email`, family F8): Filed by Leo Parkinson (leo.parkinson@northwind.example), not Leo Park (leo.park@northwind.example).
  record: {"id": "i-it-sso-d", "identifier": "IT-4", "title": "Renew SSO certificate", "teamId": "t-it", "stateId": "t-it-st-1", "assigneeId": "u-danaguest", "creatorId": "u-leoparkinson", "priority": 3.0, "priorityLabel": "Medium", "number": 4.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}

## Solver steps
Run status: completed; termination: done; steps: 6.

#### Step 1
Reasoning: I need to find the 'Renew SSO certificate' issue. Let me first search for issues with that name.
Command: curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{"query": "query { issues(first: 20, filter: {title: {contains: \"Renew SSO certificate\"}}) { nodes { id identifier title priority assignee { id name email type } creator { id name email } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Syntax Error: Expected Name, found <EOF>.\",\"locations\":[{\"line\":1,\"column\":181}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_020629e57c474426a52c3c6a9c3cbd59_6u9qk1er"}

#### Step 2
Reasoning: The query had a syntax error. Let me fix it by removing the `type` field from assignee which might not be valid, and ensure proper formatting.
Command: curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{
    "query": "query { issues(first: 20, filter: {title: {contains: \"Renew SSO certificate\"}}) { nodes { id identifier title priority assignee { id name email } creator { id name email } } } }"
  }'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"i-it-sso\",\"identifier\":\"IT-1\",\"title\":\"Renew SSO certificate\",\"priority\":3.0,\"assignee\":{\"id\":\"u-danaguest\",\"name\":\"Dana Whitfield\",\"email\":\"dana.whitfield.ext@northwind.example\"},\"creator\":{\"id\":\"u-leo\",\"name\":\"Leo Park\",\"email\":\"leo.park@northwind.example\"}},{\"id\":\"i-it-sso-b\",\"identifier\":\"IT-2\",\"title\":\"Renew SSO certificate\",\"priority\":3.0,\"assignee\":{\"id\":\"u-dana\",\"name\":\"Dana Whitfield\",\"email\":\"dana.whitfield@northwind.example\"},\"creator\":{\"id\":\"u-leo\",\"name\":\"Leo Park\",\"email\":\"leo.park@northwind.example\"}},{\"id\":\"i-it-sso-c\",\"identifier\":\"IT-3\",\"title\":\"Renew SSO certificate\",\"priority\":3.0,\"assignee\":{\"id\":\"u-danacho\",\"name\":\"Dana Cho\",\"email\":\"dana.cho@northwind.example\"},\"creator\":{\"id\":\"u-leo\",\"name\":\"Leo Park\",\"email\":\"leo.park@northwind.example\"}},{\"id\":\"i-it-sso-d\",\"identifier\":\"IT-4\",\"title\":\"Renew SSO certificate\",\"priority\":3.0,\"assignee\":{\"id\":\"u-danaguest\",\"name\":\"Dana Whitfield\",\"email\":\"dana.whitfield.ext@northwind.example\"},\"creator\":{\"id\":\"u-leoparkinson\",\"name\":\"Leo Parkinson\",\"email\":\"leo.parkinson@northwind.example\"}}]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_020629e57c474426a52c3c6a9c3cbd59_6u9qk1er"}

#### Step 3
Reasoning: I found 4 issues with the title "Renew SSO certificate". Let me identify the correct one:

- **IT-1** (`i-it-sso`): Assignee Dana Whitfield `dana.whitfield.ext@northwind.example` (`.ext` = guest/external contractor), Creator Leo Park `leo.park@northwind.example` ✓
- **IT-2** (`i-it-sso-b`): Assignee Dana Whitfield `dana.whitfield@northwind.example` (internal, no `.ext`), Creator Leo Park `leo.park@northwind.example`
- **IT-3** (`i-it-sso-c`): Assignee Dana Cho `dana.cho@northwind.example` (internal), Creator Leo Park `leo.park@northwind.example`
- **IT-4** (`i-it-sso-d`): Assignee Dana Whitfield `dana.whitfield.ext@northwind.example` (guest), but Creator is Leo Parkinson `leo.parkinson@northwind.example` (not the right person)

The matching issue is **IT-1** (`i-it-sso`):
- Guest contractor: `dana.whitfield.ext@northwind.example` (the `.ext` suffix indicates external/guest)
- Filed by: `leo.park@northwind.example`

Now I need to set its priority to Urgent (priority value 1 in Linear).
Command: curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{
    "query": "mutation { issueUpdate(id: \"i-it-sso\", priority: 1) { id identifier title priority success } }"
  }'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Unknown argument 'priority' on field 'Mutation.issueUpdate'.\",\"locations\":[{\"line\":1,\"column\":40}]},{\"message\":\"Cannot query field 'id' on type 'IssuePayload'.\",\"locations\":[{\"line\":1,\"column\":55}]},{\"message\":\"Cannot query field 'identifier' on type 'IssuePayload'.\",\"locations\":[{\"line\":1,\"column\":58}]},{\"message\":\"Cannot query field 'title' on type 'IssuePayload'.\",\"locations\":[{\"line\":1,\"column\":69}]},{\"message\":\"Cannot query field 'priority' on type 'IssuePayload'.\",\"locations\":[{\"line\":1,\"column\":75}]},{\"message\":\"Field 'issueUpdate' argument 'input' of type 'IssueUpdateInput!' is required, but it was not provided.\",\"locations\":[{\"line\":1,\"column\":12}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_020629e57c474426a52c3c6a9c3cbd59_6u9qk1er"}

#### Step 4
Reasoning: The issueUpdate mutation requires an `input` argument of type `IssueUpdateInput`. I need to restructure the query to wrap the arguments inside an `input` object. Let me also check what fields are available on `IssuePayload`.
Command: curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{
    "query": "mutation { issueUpdate(input: {id: \"i-it-sso\", priority: 1}) { success issue { id identifier title priority } } }"
  }'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Field 'id' is not defined by type 'IssueUpdateInput'.\",\"locations\":[{\"line\":1,\"column\":32}]},{\"message\":\"Field 'issueUpdate' argument 'id' of type 'String!' is required, but it was not provided.\",\"locations\":[{\"line\":1,\"column\":12}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_020629e57c474426a52c3c6a9c3cbd59_6u9qk1er"}

#### Step 5
Reasoning: The `id` is a top-level argument of `issueUpdate`, separate from the `input` object. Let me restructure.
Command: curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{
    "query": "mutation { issueUpdate(id: \"i-it-sso\", input: {priority: 1}) { success issue { id identifier title priority } } }"
  }'
Response: {"status": "success", "stdout": "{\"data\":{\"issueUpdate\":{\"success\":true,\"issue\":{\"id\":\"i-it-sso\",\"identifier\":\"IT-1\",\"title\":\"Renew SSO certificate\",\"priority\":1.0}}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_020629e57c474426a52c3c6a9c3cbd59_6u9qk1er"}

#### Step 6
Reasoning: The mutation succeeded. Issue IT-1 "Renew SSO certificate" (assigned to guest contractor Dana Whitfield `dana.whitfield.ext@northwind.example`, filed by Leo Park `leo.park@northwind.example`) has been updated to priority 1.0 (Urgent). The task is complete.


<done>
Successfully set the 'Renew SSO certificate' issue (IT-1) to Urgent priority. This was the issue assigned to guest contractor Dana Whitfield (dana.whitfield.ext@northwind.example) and filed by leo.park@northwind.example. The priority was updated from 3.0 (Medium) to 1.0 (Urgent) and the API confirmed the change.
</done>
Command: 
Response: null

## Final answer
Successfully set the 'Renew SSO certificate' issue (IT-1) to Urgent priority. This was the issue assigned to guest contractor Dana Whitfield (dana.whitfield.ext@northwind.example) and filed by leo.park@northwind.example. The priority was updated from 3.0 (Medium) to 1.0 (Urgent) and the API confirmed the change.

## State diff
- UPDATE issues `i-it-sso`: {"priorityLabel": ["Medium", "Urgent"], "priority": [3.0, 1.0]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["i-it-sso"]}. Provisional outcome: incomplete. Provisional exposed facts: [].

Give your verdict for this trial.