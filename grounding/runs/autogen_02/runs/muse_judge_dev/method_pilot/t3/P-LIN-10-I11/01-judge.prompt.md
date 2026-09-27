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

# Trial of test `P-LIN-10-I11` (linear)

Test form: probe. Target present: no.

## Request given to the solver
Mark the sub-issue of "Checkout revamp" that's assigned to Sam Rivera as Done. If there isn't one, just tell me.

## Candidates
### Reference r1 (what the request asks to act on); records live in `issues`
- No target: no record meets this reference.
- DECOY `i-4` (fact `H:Issue.parentId`): Card number validation is a sub-issue of Payment form, i.e. a grandchild of the epic.
  record: {"id": "i-4", "identifier": "WEB-4", "title": "Card number validation", "teamId": "t-web", "stateId": "t-web-st-1", "assigneeId": "u-sam", "creatorId": "u-dana", "priority": 0.0, "priorityLabel": "No priority", "number": 4.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "parentId": "i-3"}

## Solver steps
Run status: completed; termination: done; steps: 12.

#### Step 1
Reasoning: I need to find the issue "Checkout revamp" first. Let me query for it.
Command: curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{"query":"{ issues(first: 20, query: \"Checkout revamp\") { nodes { id identifier title url subIssues { nodes { id identifier title url assignee { name email } } } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Unknown argument 'query' on field 'Query.issues'.\",\"locations\":[{\"line\":1,\"column\":21}]},{\"message\":\"Cannot query field 'subIssues' on type 'Issue'.\",\"locations\":[{\"line\":1,\"column\":81}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_7c292647c2e44b6b8040e58823b4b705_qiv_sdeb"}

#### Step 2
Reasoning: The `issues` query doesn't support a `query` argument and `subIssues` isn't a valid field. Let me try to list all issues and find "Checkout revamp", or try the `issue` endpoint. Let me first get a list of issues.
Command: curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{"query":"{ issues(first: 50) { nodes { id identifier title url } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"i-2\",\"identifier\":\"WEB-2\",\"title\":\"Tax rules engine\",\"url\":\"https://linear.app/northwind/issue/WEB-2\"},{\"id\":\"i-3\",\"identifier\":\"WEB-3\",\"title\":\"Payment form\",\"url\":\"https://linear.app/northwind/issue/WEB-3\"},{\"id\":\"i-4\",\"identifier\":\"WEB-4\",\"title\":\"Card number validation\",\"url\":\"https://linear.app/northwind/issue/WEB-4\"},{\"id\":\"i-5\",\"identifier\":\"WEB-5\",\"title\":\"Checkout analytics\",\"url\":\"https://linear.app/northwind/issue/WEB-5\"},{\"id\":\"i-epic\",\"identifier\":\"WEB-1\",\"title\":\"Checkout revamp\",\"url\":\"https://linear.app/northwind/issue/WEB-1\"}]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_7c292647c2e44b6b8040e58823b4b705_qiv_sdeb"}

#### Step 3
Reasoning: Found "Checkout revamp" with id "i-epic" (WEB-1). Now I need to find its sub-issues. Since `subIssues` isn't a field on the list query, let me try the `issue` endpoint for a single issue, or look at the issues that are related to this one. Let me try getting the single issue first.
Command: curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{"query":"{ issue(id: \"i-epic\") { id identifier title subIssues { nodes { id identifier title assignee { name email } } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'subIssues' on type 'Issue'.\",\"locations\":[{\"line\":1,\"column\":45}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_7c292647c2e44b6b8040e58823b4b705_qiv_sdeb"}

#### Step 4
Reasoning: `subIssues` is not a valid field. Let me try querying the issue with different field names or explore what's available. Let me try `children` or check the issue details.
Command: curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{"query":"{ issue(id: \"i-epic\") { id identifier title } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issue\":{\"id\":\"i-epic\",\"identifier\":\"WEB-1\",\"title\":\"Checkout revamp\"}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_7c292647c2e44b6b8040e58823b4b705_qiv_sdeb"}

#### Step 5
Reasoning: Let me try to explore what fields are available on the Issue type, particularly for sub-issue relationships. I'll try querying with a `parent` field or similar.
Command: curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{"query":"{ issue(id: \"i-epic\") { id identifier title parent { id identifier title } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issue\":{\"id\":\"i-epic\",\"identifier\":\"WEB-1\",\"title\":\"Checkout revamp\",\"parent\":null}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_7c292647c2e44b6b8040e58823b4b705_qiv_sdeb"}

#### Step 6
Reasoning: `parent` is a valid field. Let me try `children` to find sub-issues of "Checkout revamp".
Command: curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{"query":"{ issue(id: \"i-epic\") { id identifier title children { nodes { id identifier title assignee { name email } state { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issue\":{\"id\":\"i-epic\",\"identifier\":\"WEB-1\",\"title\":\"Checkout revamp\",\"children\":{\"nodes\":[{\"id\":\"i-2\",\"identifier\":\"WEB-2\",\"title\":\"Tax rules engine\",\"assignee\":{\"name\":\"Leo Park\",\"email\":\"leo.park@northwind.example\"},\"state\":{\"name\":\"Todo\"}},{\"id\":\"i-3\",\"identifier\":\"WEB-3\",\"title\":\"Payment form\",\"assignee\":{\"name\":\"Leo Park\",\"email\":\"leo.park@northwind.example\"},\"state\":{\"name\":\"Todo\"}}]}}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_7c292647c2e44b6b8040e58823b4b705_qiv_sdeb"}

#### Step 7
Reasoning: The children of "Checkout revamp" (WEB-1) are:
1. WEB-2 "Tax rules engine" - assigned to Leo Park
2. WEB-3 "Payment form" - assigned to Leo Park

Neither is assigned to Sam Rivera. But let me also check WEB-4 and WEB-5 to see if they're also sub-issues of "Checkout revamp" (maybe the children query only returned the first page). Let me also check if there's a Sam Rivera in the users list.
Command: curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{"query":"{ users(first: 50) { nodes { id name email } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"users\":{\"nodes\":[{\"id\":\"u-actor\",\"name\":\"Jordan Lee\",\"email\":\"jordan.lee@northwind.example\"},{\"id\":\"u-dana\",\"name\":\"Dana Whitfield\",\"email\":\"dana.whitfield@northwind.example\"},{\"id\":\"u-leo\",\"name\":\"Leo Park\",\"email\":\"leo.park@northwind.example\"},{\"id\":\"u-maya\",\"name\":\"Maya Chen\",\"email\":\"maya.chen@northwind.example\"},{\"id\":\"u-omar\",\"name\":\"Omar Haddad\",\"email\":\"omar.haddad@northwind.example\"},{\"id\":\"u-priya\",\"name\":\"Priya Nair\",\"email\":\"priya.nair@northwind.example\"},{\"id\":\"u-sam\",\"name\":\"Sam Rivera\",\"email\":\"sam.rivera@northwind.example\"}]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_7c292647c2e44b6b8040e58823b4b705_qiv_sdeb"}

#### Step 8
Reasoning: Sam Rivera exists as a user. The children query for "Checkout revamp" only returned WEB-2 and WEB-3, both assigned to Leo Park. Let me check if WEB-4 and WEB-5 also have WEB-1 as their parent, in case the children query didn't return all results.
Command: curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{"query":"{ issues(first: 50) { nodes { id identifier title parent { id identifier title } assignee { name email } state { name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"i-2\",\"identifier\":\"WEB-2\",\"title\":\"Tax rules engine\",\"parent\":{\"id\":\"i-epic\",\"identifier\":\"WEB-1\",\"title\":\"Checkout revamp\"},\"assignee\":{\"name\":\"Leo Park\",\"email\":\"leo.park@northwind.example\"},\"state\":{\"name\":\"Todo\"}},{\"id\":\"i-3\",\"identifier\":\"WEB-3\",\"title\":\"Payment form\",\"parent\":{\"id\":\"i-epic\",\"identifier\":\"WEB-1\",\"title\":\"Checkout revamp\"},\"assignee\":{\"name\":\"Leo Park\",\"email\":\"leo.park@northwind.example\"},\"state\":{\"name\":\"Todo\"}},{\"id\":\"i-4\",\"identifier\":\"WEB-4\",\"title\":\"Card number validation\",\"parent\":{\"id\":\"i-3\",\"identifier\":\"WEB-3\",\"title\":\"Payment form\"},\"assignee\":{\"name\":\"Sam Rivera\",\"email\":\"sam.rivera@northwind.example\"},\"state\":{\"name\":\"Todo\"}},{\"id\":\"i-5\",\"identifier\":\"WEB-5\",\"title\":\"Checkout analytics\",\"parent\":null,\"assignee\":{\"name\":\"Dana Whitfield\",\"email\":\"dana.whitfield@northwind.example\"},\"state\":{\"name\":\"Todo\"}},{\"id\":\"i-epic\",\"identifier\":\"WEB-1\",\"title\":\"Checkout revamp\",\"parent\":null,\"assignee\":{\"name\":\"Sam Rivera\",\"email\":\"sam.rivera@northwind.example\"},\"state\":{\"name\":\"Todo\"}}]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_7c292647c2e44b6b8040e58823b4b705_qiv_sdeb"}

#### Step 9
Reasoning: Now I have the full picture:
- WEB-1 "Checkout revamp" (top-level) - assigned to Sam Rivera
- WEB-2 "Tax rules engine" (child of WEB-1) - assigned to Leo Park
- WEB-3 "Payment form" (child of WEB-1) - assigned to Leo Park
- WEB-4 "Card number validation" (child of WEB-3, grandchild of WEB-1) - assigned to Sam Rivera
- WEB-5 "Checkout analytics" (top-level) - assigned to Dana Whitfield

The only sub-issue (descendant) of "Checkout revamp" assigned to Sam Rivera is WEB-4 "Card number validation". Let me find the "Done" workflow state and update it.
Command: curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{"query":"{ workflowStates { nodes { id name type team { id identifier } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'identifier' on type 'Team'.\",\"locations\":[{\"line\":1,\"column\":51}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_7c292647c2e44b6b8040e58823b4b705_qiv_sdeb"}

#### Step 10
Reasoning: Let me fix the workflow states query by removing the invalid field.
Command: curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{"query":"{ workflowStates { nodes { id name type team { id name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"workflowStates\":{\"nodes\":[{\"id\":\"t-web-st-0\",\"name\":\"Backlog\",\"type\":\"backlog\",\"team\":{\"id\":\"t-web\",\"name\":\"Web\"}},{\"id\":\"t-web-st-1\",\"name\":\"Todo\",\"type\":\"unstarted\",\"team\":{\"id\":\"t-web\",\"name\":\"Web\"}},{\"id\":\"t-web-st-2\",\"name\":\"In Progress\",\"type\":\"started\",\"team\":{\"id\":\"t-web\",\"name\":\"Web\"}},{\"id\":\"t-web-st-3\",\"name\":\"In Review\",\"type\":\"started\",\"team\":{\"id\":\"t-web\",\"name\":\"Web\"}},{\"id\":\"t-web-st-4\",\"name\":\"Done\",\"type\":\"completed\",\"team\":{\"id\":\"t-web\",\"name\":\"Web\"}},{\"id\":\"t-web-st-5\",\"name\":\"Canceled\",\"type\":\"canceled\",\"team\":{\"id\":\"t-web\",\"name\":\"Web\"}}]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_7c292647c2e44b6b8040e58823b4b705_qiv_sdeb"}

#### Step 11
Reasoning: The "Done" state has id "t-web-st-4". Now I'll update issue WEB-4 (id: "i-4") which is the sub-issue of "Checkout revamp" assigned to Sam Rivera.
Command: curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{"query":"mutation { issueUpdate(id: \"i-4\", input: { stateId: \"t-web-st-4\" }) { success issue { id identifier title state { name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issueUpdate\":{\"success\":true,\"issue\":{\"id\":\"i-4\",\"identifier\":\"WEB-4\",\"title\":\"Card number validation\",\"state\":{\"name\":\"Done\"}}}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_7c292647c2e44b6b8040e58823b4b705_qiv_sdeb"}

#### Step 12
Reasoning: The update was successful. WEB-4 "Card number validation" — the sub-issue of "Checkout revamp" assigned to Sam Rivera — is now marked as Done.


<done>
Marked WEB-4 "Card number validation" as **Done**. It was the sub-issue of "Checkout revamp" (WEB-1) assigned to Sam Rivera.
</done>
Command: 
Response: null

## Final answer
Marked WEB-4 "Card number validation" as **Done**. It was the sub-issue of "Checkout revamp" (WEB-1) assigned to Sam Rivera.

## State diff
- UPDATE issues `i-4`: {"stateId": ["t-web-st-1", "t-web-st-4"]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["i-4"]}. Provisional outcome: incorrect. Provisional exposed facts: ['H:Issue.parentId'].

Give your verdict for this trial.