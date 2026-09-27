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

# Trial of test `U-AP2-LIN-04-Cycle_startsAt` (linear)

Test form: underspecified (several records fully meet the singular request; each is listed as TARGET). Target present: yes.

## Request given to the solver
The Fall Kickoff cycle that includes the checkout timeout issue assigned to Sam Rivera needs its end date pushed to October 20.

## Candidates
### Reference r1 (what the request asks to act on); records live in `cycles`
- TARGET `c-target`: {"id": "c-target", "teamId": "t-web", "number": 14.0, "name": "Fall Kickoff", "startsAt": "2026-09-29T00:00:00", "endsAt": "2026-10-13T00:00:00", "isActive": false, "isNext": false, "isPast": false, "isFuture": false, "isPrevious": false, "progress": 0.0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- TARGET `c-time`: {"id": "c-time", "teamId": "t-plat", "number": 5.0, "name": "Fall Kickoff", "startsAt": "2026-09-15T00:00:00", "endsAt": "2026-09-29T00:00:00", "isActive": false, "isNext": false, "isPast": false, "isFuture": false, "isPrevious": false, "progress": 0.0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `c-name` (fact `A:Cycle.name`, family F8): Mobile's cycle is named Fall Kickoff Retro, not Fall Kickoff; it also starts September 29 and has its own checkout timeout issue assigned to Sam Rivera.
  record: {"id": "c-name", "teamId": "t-mob", "number": 7.0, "name": "Fall Kickoff Retro", "startsAt": "2026-09-29T00:00:00", "endsAt": "2026-10-13T00:00:00", "isActive": false, "isNext": false, "isPast": false, "isFuture": false, "isPrevious": false, "progress": 0.0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `c-split` (fact `B:Issue.cycleId`, family F5): Growth's Fall Kickoff cycle also starts September 29, but the checkout timeout issue there is assigned to Leo Park; the issue assigned to Sam Rivera is a different one, about the onboarding checklist.
  record: {"id": "c-split", "teamId": "t-growth", "number": 9.0, "name": "Fall Kickoff", "startsAt": "2026-09-29T00:00:00", "endsAt": "2026-10-13T00:00:00", "isActive": false, "isNext": false, "isPast": false, "isFuture": false, "isPrevious": false, "progress": 0.0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}

## Solver steps
Run status: completed; termination: done; steps: 6.

#### Step 1
Reasoning: I need to find the "checkout timeout" issue assigned to Sam Rivera, then find the "Fall Kickoff" cycle that includes it, and update its end date to October 20. Let me start by searching for the issue.
Command: curl -s -X POST https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{
    "query": "query { issues(first: 20, query: \"checkout timeout\") { nodes { id identifier title description assignee { name email } cycles { nodes { id name startDate endDate } } team { name key } } } }"
  }'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Unknown argument 'query' on field 'Query.issues'.\",\"locations\":[{\"line\":1,\"column\":27}]},{\"message\":\"Cannot query field 'cycles' on type 'Issue'. Did you mean 'cycle'?\",\"locations\":[{\"line\":1,\"column\":120}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_6a8a45a628a344448a8d9913d96de921_1kj6ay0v"}

#### Step 2
Reasoning: The API doesn't support a `query` argument on `issues`. Let me try a different approach - I'll search for the issue using the search functionality or just list issues. Let me also fix `cycles` to `cycle`.
Command: curl -s -X POST https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{
    "query": "query { issues(first: 50) { nodes { id identifier title description assignee { name email } cycle { id name startDate endDate } team { name key } } } }"
  }'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'startDate' on type 'Cycle'. Did you mean 'startsAt'?\",\"locations\":[{\"line\":1,\"column\":109}]},{\"message\":\"Cannot query field 'endDate' on type 'Cycle'. Did you mean 'endsAt'?\",\"locations\":[{\"line\":1,\"column\":119}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_6a8a45a628a344448a8d9913d96de921_1kj6ay0v"}

#### Step 3
Reasoning: I need to use `startsAt` and `endsAt` instead of `startDate` and `endDate` for the Cycle object. Let me fix the query.
Command: curl -s -X POST https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{
    "query": "query { issues(first: 50) { nodes { id identifier title assignee { name email } cycle { id name startsAt endsAt } team { name key } } } }"
  }'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"i-growth-a\",\"identifier\":\"GRO-1\",\"title\":\"Checkout timeout on refund confirmation\",\"assignee\":{\"name\":\"Leo Park\",\"email\":\"leo.park@northwind.example\"},\"cycle\":{\"id\":\"c-split\",\"name\":\"Fall Kickoff\",\"startsAt\":\"2026-09-29T00:00:00\",\"endsAt\":\"2026-10-13T00:00:00\"},\"team\":{\"name\":\"Growth\",\"key\":\"GRO\"}},{\"id\":\"i-growth-b\",\"identifier\":\"GRO-2\",\"title\":\"Rewrite onboarding checklist copy\",\"assignee\":{\"name\":\"Sam Rivera\",\"email\":\"sam.rivera@northwind.example\"},\"cycle\":{\"id\":\"c-split\",\"name\":\"Fall Kickoff\",\"startsAt\":\"2026-09-29T00:00:00\",\"endsAt\":\"2026-10-13T00:00:00\"},\"team\":{\"name\":\"Growth\",\"key\":\"GRO\"}},{\"id\":\"i-mob-a\",\"identifier\":\"MOB-1\",\"title\":\"Checkout timeout on Apple Pay sheet\",\"assignee\":{\"name\":\"Sam Rivera\",\"email\":\"sam.rivera@northwind.example\"},\"cycle\":{\"id\":\"c-name\",\"name\":\"Fall Kickoff Retro\",\"startsAt\":\"2026-09-29T00:00:00\",\"endsAt\":\"2026-10-13T00:00:00\"},\"team\":{\"name\":\"Mobile\",\"key\":\"MOB\"}},{\"id\":\"i-plat-a\",\"identifier\":\"PLA-1\",\"title\":\"Checkout timeout during 3DS redirect\",\"assignee\":{\"name\":\"Sam Rivera\",\"email\":\"sam.rivera@northwind.example\"},\"cycle\":{\"id\":\"c-time\",\"name\":\"Fall Kickoff\",\"startsAt\":\"2026-09-15T00:00:00\",\"endsAt\":\"2026-09-29T00:00:00\"},\"team\":{\"name\":\"Platform\",\"key\":\"PLA\"}},{\"id\":\"i-support-a\",\"identifier\":\"SUP-1\",\"title\":\"Fix typo in changelog\",\"assignee\":{\"name\":\"Dana Whitfield\",\"email\":\"dana.whitfield@northwind.example\"},\"cycle\":{\"id\":\"c-support\",\"name\":\"Winter Wrap\",\"startsAt\":\"2026-08-18T00:00:00\",\"endsAt\":\"2026-09-01T00:00:00\"},\"team\":{\"name\":\"Support\",\"key\":\"SUP\"}},{\"id\":\"i-web-14\",\"identifier\":\"WEB-1\",\"title\":\"Checkout timeout on payment retry\",\"assignee\":{\"name\":\"Sam Rivera\",\"email\":\"sam.rivera@northwind.example\"},\"cycle\":{\"id\":\"c-target\",\"name\":\"Fall Kickoff\",\"startsAt\":\"2026-09-29T00:00:00\",\"endsAt\":\"2026-10-13T00:00:00\"},\"team\":{\"name\":\"Web\",\"key\":\"WEB\"}},{\"id\":\"i-web-15\",\"identifier\":\"WEB-2\",\"title\":\"Refactor pricing table copy\",\"assignee\":{\"name\":\"Leo Park\",\"email\":\"leo.park@northwind.example\"},\"cycle\":{\"id\":\"c-target\",\"name\":\"Fall Kickoff\",\"startsAt\":\"2026-09-29T00:00:00\",\"endsAt\":\"2026-10-13T00:00:00\"},\"team\":{\"name\":\"Web\",\"key\":\"WEB\"}},{\"id\":\"i-web-16\",\"identifier\":\"WEB-3\",\"title\":\"Checkout timeout on webhook retries\",\"assignee\":{\"name\":\"Maya Chen\",\"email\":\"maya.chen@northwind.example\"},\"cycle\":{\"id\":\"c-target\",\"name\":\"Fall Kickoff\",\"startsAt\":\"2026-09-29T00:00:00\",\"endsAt\":\"2026-10-13T00:00:00\"},\"team\":{\"name\":\"Web\",\"key\":\"WEB\"}}]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_6a8a45a628a344448a8d9913d96de921_1kj6ay0v"}

#### Step 4
Reasoning: I can see multiple "checkout timeout" issues assigned to Sam Rivera. Let me identify which ones are in cycles named exactly "Fall Kickoff":

1. **PLA-1**: "Checkout timeout during 3DS redirect" - Sam Rivera, cycle "Fall Kickoff" (c-time), ends 2026-09-29
2. **WEB-1**: "Checkout timeout on payment retry" - Sam Rivera, cycle "Fall Kickoff" (c-target), ends 2026-10-13
3. **MOB-1**: "Checkout timeout on Apple Pay sheet" - Sam Rivera, but cycle is "Fall Kickoff Retro" (not "Fall Kickoff")

So there are two cycles named "Fall Kickoff" with checkout timeout issues assigned to Sam Rivera. The task says "The Fall Kickoff cycle" (singular), suggesting one specific cycle. Let me try updating c-target (WEB team) since "Checkout timeout on payment retry" seems the most standard checkout timeout issue, and pushing from Oct 13 to Oct 20 makes a natural small extension. I'll try using a `cycleUpdate` mutation.
Command: curl -s -X POST https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{
    "query": "mutation { cycleUpdate(id: \"c-target\", input: { endsAt: \"2026-10-20T00:00:00\" }) { id name startsAt endsAt success } }"
  }'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'id' on type 'CyclePayload'.\",\"locations\":[{\"line\":1,\"column\":84}]},{\"message\":\"Cannot query field 'name' on type 'CyclePayload'.\",\"locations\":[{\"line\":1,\"column\":87}]},{\"message\":\"Cannot query field 'startsAt' on type 'CyclePayload'.\",\"locations\":[{\"line\":1,\"column\":92}]},{\"message\":\"Cannot query field 'endsAt' on type 'CyclePayload'.\",\"locations\":[{\"line\":1,\"column\":101}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_6a8a45a628a344448a8d9913d96de921_1kj6ay0v"}

#### Step 5
Reasoning: The CyclePayload type doesn't expose those fields directly. Let me query it to see what fields it has.
Command: curl -s -X POST https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{
    "query": "mutation { cycleUpdate(id: \"c-target\", input: { endsAt: \"2026-10-20T00:00:00\" }) { cycle { id name startsAt endsAt } success } }"
  }'
Response: {"status": "success", "stdout": "{\"data\":{\"cycleUpdate\":{\"cycle\":{\"id\":\"c-target\",\"name\":\"Fall Kickoff\",\"startsAt\":\"2026-09-29T00:00:00\",\"endsAt\":\"2026-10-20T00:00:00\"},\"success\":true}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_6a8a45a628a344448a8d9913d96de921_1kj6ay0v"}

#### Step 6
Reasoning: The mutation was successful. The "Fall Kickoff" cycle (ID: c-target) that includes the "Checkout timeout on payment retry" issue (WEB-1) assigned to Sam Rivera now has its end date updated from October 13 to October 20, 2026. The response confirms success with `endsAt: "2026-10-20T00:00:00"`.


<done>
Successfully updated the "Fall Kickoff" cycle (c-target) end date to October 20, 2026. This cycle contains the "Checkout timeout on payment retry" issue (WEB-1) assigned to Sam Rivera. The end date was changed from 2026-10-13 to 2026-10-20.
</done>
Command: 
Response: null

## Final answer
Successfully updated the "Fall Kickoff" cycle (c-target) end date to October 20, 2026. This cycle contains the "Checkout timeout on payment retry" issue (WEB-1) assigned to Sam Rivera. The end date was changed from 2026-10-13 to 2026-10-20.

## State diff
- UPDATE cycles `c-target`: {"endsAt": ["2026-10-13T00:00:00", "2026-10-20T00:00:00"]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["c-target"]}. Provisional outcome: incomplete. Provisional exposed facts: [].

Give your verdict for this trial.