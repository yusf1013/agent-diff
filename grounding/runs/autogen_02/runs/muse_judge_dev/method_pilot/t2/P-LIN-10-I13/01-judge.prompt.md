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

# Trial of test `P-LIN-10-I13` (linear)

Test form: probe. Target present: no.

## Request given to the solver
Mark the sub-issue of "Checkout revamp" that's assigned to Sam Rivera as Done. If there isn't one, just tell me.

## Candidates
### Reference r1 (what the request asks to act on); records live in `issues`
- No target: no record meets this reference.
- DECOY `i-6` (fact `A:Issue.title`): Sam's sub-issue of Checkout analytics.
  record: {"id": "i-6", "identifier": "WEB-6", "title": "Funnel dashboard", "teamId": "t-web", "stateId": "t-web-st-1", "assigneeId": "u-sam", "creatorId": "u-dana", "priority": 0.0, "priorityLabel": "No priority", "number": 6.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "parentId": "i-5"}

## Solver steps
Run status: completed; termination: done; steps: 10.

#### Step 1
Reasoning: I need to find the "Checkout revamp" issue and its sub-issues, identify the one assigned to Sam Rivera, and mark it as Done. Let me start by searching for the "Checkout revamp" issue and also get Sam Rivera's user info.
Command: curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "query { issues(filter: { title: { contains: \"Checkout revamp\" } }) { nodes { id identifier title subIssues { nodes { id identifier title assignee { name id } workflowState { name id } } } } } users(filter: { name: { contains: \"Sam Rivera\" } }) { nodes { id name } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'subIssues' on type 'Issue'.\",\"locations\":[{\"line\":1,\"column\":98}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_4caa2322524a42968cd91f8954656c3c_izen4a9w"}

#### Step 2
Reasoning: The `subIssues` field doesn't exist on the Issue type. In Linear, sub-issues are typically linked via a `parentIssue` field. Let me first find the "Checkout revamp" issue, then query for issues that have it as their parent.
Command: curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "query { issues(filter: { title: { contains: \"Checkout revamp\" } }) { nodes { id identifier title } } users(filter: { name: { contains: \"Sam Rivera\" } }) { nodes { id name } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"i-epic\",\"identifier\":\"WEB-1\",\"title\":\"Checkout revamp\"}]},\"users\":{\"nodes\":[{\"id\":\"u-sam\",\"name\":\"Sam Rivera\"}]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_4caa2322524a42968cd91f8954656c3c_izen4a9w"}

#### Step 3
Reasoning: I found the "Checkout revamp" issue (ID: "i-epic") and Sam Rivera (ID: "u-sam"). Now I need to find issues that are sub-issues (children) of this epic, specifically the one assigned to Sam Rivera. In Linear, sub-issues are linked via the `parentIssue` field.
Command: curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "query { issues(filter: { parent: { id: { eq: \"i-epic\" } }, assignee: { id: { eq: \"u-sam\" } } }) { nodes { id identifier title workflowState { id name } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'workflowState' on type 'Issue'.\",\"locations\":[{\"line\":1,\"column\":127}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_4caa2322524a42968cd91f8954656c3c_izen4a9w"}

#### Step 4
Reasoning: The field on Issue is likely `state` not `workflowState`. Let me fix the query.
Command: curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "query { issues(filter: { parent: { id: { eq: \"i-epic\" } }, assignee: { id: { eq: \"u-sam\" } } }) { nodes { id identifier title state { id name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"i-6\",\"identifier\":\"WEB-6\",\"title\":\"Funnel dashboard\",\"state\":{\"id\":\"t-web-st-1\",\"name\":\"Todo\"}},{\"id\":\"i-epic\",\"identifier\":\"WEB-1\",\"title\":\"Checkout revamp\",\"state\":{\"id\":\"t-web-st-1\",\"name\":\"Todo\"}}]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_4caa2322524a42968cd91f8954656c3c_izen4a9w"}

#### Step 5
Reasoning: I found the sub-issue: "Funnel dashboard" (WEB-6, ID: "i-6") is a sub-issue of "Checkout revamp" and is assigned to Sam Rivera. It's currently in "Todo" state. Now I need to find the "Done" workflow state ID to update this issue.
Command: curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "query { workflowStates(filter: { name: { eq: \"Done\" } }) { nodes { id name teamId } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'teamId' on type 'WorkflowState'. Did you mean 'team'?\",\"locations\":[{\"line\":1,\"column\":76}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_4caa2322524a42968cd91f8954656c3c_izen4a9w"}

#### Step 6
Reasoning: The field should be `team { id }` not `teamId`. Let me fix that.
Command: curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "query { workflowStates(filter: { name: { eq: \"Done\" } }) { nodes { id name team { id } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"workflowStates\":{\"nodes\":[{\"id\":\"t-web-st-4\",\"name\":\"Done\",\"team\":{\"id\":\"t-web\"}}]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_4caa2322524a42968cd91f8954656c3c_izen4a9w"}

#### Step 7
Reasoning: I found the "Done" workflow state (ID: "t-web-st-4") for the WEB team. Now I'll update issue WEB-6 (i-6) to set its state to Done.
Command: curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "mutation { issueUpdate(id: \"i-6\", stateId: \"t-web-st-4\") { success issue { id identifier title state { id name } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Unknown argument 'stateId' on field 'Mutation.issueUpdate'.\",\"locations\":[{\"line\":1,\"column\":35}]},{\"message\":\"Field 'issueUpdate' argument 'input' of type 'IssueUpdateInput!' is required, but it was not provided.\",\"locations\":[{\"line\":1,\"column\":12}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_4caa2322524a42968cd91f8954656c3c_izen4a9w"}

#### Step 8
Reasoning: The issueUpdate mutation requires an `input` argument of type `IssueUpdateInput`. Let me restructure the mutation properly.
Command: curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "mutation { issueUpdate(input: { id: \"i-6\", stateId: \"t-web-st-4\" }) { success issue { id identifier title state { id name } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Field 'id' is not defined by type 'IssueUpdateInput'.\",\"locations\":[{\"line\":1,\"column\":33}]},{\"message\":\"Field 'issueUpdate' argument 'id' of type 'String!' is required, but it was not provided.\",\"locations\":[{\"line\":1,\"column\":12}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_4caa2322524a42968cd91f8954656c3c_izen4a9w"}

#### Step 9
Reasoning: The `id` should be a top-level argument on `issueUpdate`, not inside the `input` object. Let me restructure.
Command: curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "mutation { issueUpdate(id: \"i-6\", input: { stateId: \"t-web-st-4\" }) { success issue { id identifier title state { id name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issueUpdate\":{\"success\":true,\"issue\":{\"id\":\"i-6\",\"identifier\":\"WEB-6\",\"title\":\"Funnel dashboard\",\"state\":{\"id\":\"t-web-st-4\",\"name\":\"Done\"}}}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_4caa2322524a42968cd91f8954656c3c_izen4a9w"}

#### Step 10
Reasoning: The update was successful. The sub-issue "Funnel dashboard" (WEB-6) of "Checkout revamp" that was assigned to Sam Rivera has been marked as Done.


<done>
I found the sub-issue of "Checkout revamp" assigned to Sam Rivera — it's **WEB-6: "Funnel dashboard"** — and successfully marked it as **Done**.
</done>
Command: 
Response: null

## Final answer
I found the sub-issue of "Checkout revamp" assigned to Sam Rivera — it's **WEB-6: "Funnel dashboard"** — and successfully marked it as **Done**.

## State diff
- UPDATE issues `i-6`: {"stateId": ["t-web-st-1", "t-web-st-4"]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["i-6"]}. Provisional outcome: incorrect. Provisional exposed facts: ['A:Issue.title'].

Give your verdict for this trial.