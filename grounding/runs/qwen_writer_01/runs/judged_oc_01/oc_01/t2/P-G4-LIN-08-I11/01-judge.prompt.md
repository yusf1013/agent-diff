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

# Trial of test `P-G4-LIN-08-I11` (linear)

Test form: no-target test with all of the scenario's decoys. Target present: no.

## Request given to the solver
Bump the priority of the ENG issue that's due Friday, October 2, is estimated at 3 points, and is assigned to Priya Nair to Urgent. If there isn't one, just tell me.

## Candidates
### Reference r1 (what the request asks to act on); records live in `issues`
- No target: no record meets this reference.
- DECOY `47c50000-7316-4e1f-a987-f87e67c4f295` (fact `A:Issue.dueDate`, family F7): Same team, 3-point estimate and assignee, but it is due the day before, on Thursday October 1.
  record: {"id": "47c50000-7316-4e1f-a987-f87e67c4f295", "identifier": "ENG-16", "title": "Checkout: tax line missing for EU orders", "teamId": "e660af85-ece8-48d1-ad31-b3e400f08a4a", "stateId": "f4c268b8-3895-46fb-b72e-690b5baf6246", "assigneeId": "caa1ea16-4ec3-4909-9884-4e0da8f29b40", "creatorId": "u-actor", "priority": 2.0, "priorityLabel": "High", "number": 16.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "estimate": 3, "dueDate": "2026-10-01"}

## Solver steps
Run status: completed; termination: done; steps: 11.

#### Step 1
Reasoning: The user wants to update the priority of an issue in Linear. I should read the Linear skill first.
Command: read {"path": "~/.openclaw-state/3faad27a020a429d/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: Let me find the issue in question. I need to query Linear's GraphQL API to find ENG issues that are due on Friday, October 2, 2026, have an estimate of 3 points, and are assigned to Priya Nair.

Let me construct the query. First I need to identify Priya Nair's user ID and the ENG team. Let me run a query to find the issue.

I'll write a GraphQL query to find the user and the issue.

I'll query Linear to find that specific issue. Let me start by identifying Priya Nair and the ENG team, then find the matching issue.
Command: curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: <TOKEN>" \
  -H "Content-Type: application/json" \
  --data '{
    "query": "query {
      users(orderBy: name, first: 100) {
        nodes { id name email }
      }
      teams(first: 100) {
        nodes { id name key }
      }
    }"
  }'
Response: {"status": "success", "stdout": "Request body is not a valid JSON"}

#### Step 3
Reasoning: The request body wasn't valid JSON. The issue is probably that the multi-line query contains some weird characters. Let me try writing the query to a file and using that.

Let me try a cleaner approach with a query file:
Command: write {"path": "/tmp/linear_users_teams.json", "content": "{\n  \"query\": \"query { users(first: 100) { nodes { id name email } } teams(first: 100) { nodes { id name key } } }\"\n}\n"}
Response: {"status": "success", "stdout": "Successfully wrote 117 bytes to /tmp/linear_users_teams.json"}

#### Step 4
Reasoning: Let me try sending this using a file.
Command: curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: <TOKEN>" \
  -H "Content-Type: application/json" \
  --data @/tmp/linear_users_teams.json
Response: {"status": "success", "stdout": "{\"data\":{\"users\":{\"nodes\":[{\"id\":\"267ac6da-46f8-4203-b440-330fc7515fc9\",\"name\":\"Leo Park\",\"email\":\"leo.park@northwind.example\"},{\"id\":\"3ada5040-c357-4575-b53b-667e20a7e6f4\",\"name\":\"Dana Whitfield\",\"email\":\"dana.whitfield@northwind.example\"},{\"id\":\"40f77d87-b0bb-41a0-a206-8dbb1dabc76b\",\"name\":\"Sam Rivera\",\"email\":\"sam.rivera@northwind.example\"},{\"id\":\"ae4044ff-920d-460a-830c-34c04993e11e\",\"name\":\"Omar Haddad\",\"email\":\"omar.haddad@northwind.example\"},{\"id\":\"caa1ea16-4ec3-4909-9884-4e0da8f29b40\",\"name\":\"Priya Nair\",\"email\":\"priya.nair@northwind.example\"},{\"id\":\"e16bd282-6a02-4dcf-a67c-7a36cfe92103\",\"name\":\"Maya Chen\",\"email\":\"maya.chen@northwind.example\"},{\"id\":\"u-actor\",\"name\":\"Jordan Lee\",\"email\":\"jordan.lee@northwind.example\"}]},\"teams\":{\"nodes\":[{\"id\":\"0576069f-f49a-4be2-80ab-fad2bfc741eb\",\"name\":\"Mobile\",\"key\":\"MOB\"},{\"id\":\"e660af85-ece8-48d1-ad31-b3e400f08a4a\",\"name\":\"Engineering\",\"key\":\"ENG\"}]}}}"}

#### Step 5
Reasoning: What I found:
- Priya Nair: id `caa1ea16-4ec3-4909-9884-4e0da8f29b40`
- ENG team (Engineering): id `e660af85-ece8-48d1-ad31-b3e400f08a4a`

Now, I'll search for issues that satisfy the following conditions:
- Assigned to Priya Nair
- Team = ENG
- Due date = 2026-10-02 (Friday)
- Estimate = 3 points

I'll query these issues. The "Urgent" priority in Linear is the "urgent" priority model. First, let's fetch the issues that match the conditions, and then update the priority.

Query:
```graphql
query {
  issues(
    first: 50,
    filter: {
      assignee: { id: { eq: "caa1ea16-4ec3-4909-9884-4e0da8f29b40" } },
      team: { id: { eq: "e660af85-ece8-48d1-ad31-b3e400f08a4a" } },
      dueDate: { eq: "2026-10-02" },
      estimate: { eq: 3 }
    }
  ) {
    nodes { id identifier title priority priorityName estimate dueDate state { name } assignee { name } }
  }
}
```

Note: "3faad27a020a429d" looks like a hash. I'll ignore it.

Wait, in the user list there's "u-actor" Jordan Lee, who is probably the current user. No problem.

Let me run the query.

Found Priya Nair (id: `caa1ea16...`) and the ENG team (Engineering, `e660af85...`). Now searching for the matching issue:
Command: write {"content": "{\n  \"query\": \"query {\n    issues(\n      first: 50,\n      filter: {\n        assignee: { id: { eq: \\\"caa1ea16-4ec3-4909-9884-4e0da8f29b40\\\" } },\n        team: { id: { eq: \\\"e660af85-ece8-48d1-ad31-b3e400f08a4a\\\" } },\n        dueDate: { eq: \\\"2026-10-02\\\" },\n        estimate: { eq: 3 }\n      }\n    ) {\n      nodes {\n        id\n        identifier\n        title\n        priority\n        estimate\n        dueDate\n        state { name }\n        assignee { name }\n      }\n    }\n  }\"\n}\n", "path": "/tmp/linear_find_issue.json"}
Response: {"status": "success", "stdout": "Successfully wrote 478 bytes to /tmp/linear_find_issue.json"}

#### Step 6
Reasoning: The user asked about issues whose deadline is Friday, October 2nd. Let me check what day of the week October 2nd, 2026 actually is. The message says "due Friday, October 2nd," and the current date is Wednesday, September 30, 2026. So, is October 2, 2026 a Friday? Let me verify: September 30, 2026 is a Wednesday (as stated in the message). So October 1 is Thursday, and October 2 is Friday. Yes, that checks out.

Let's run the query.
Command: curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: <TOKEN>" \
  -H "Content-Type: application/json" \
  --data @/tmp/linear_find_issue.json
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[]}}}"}

#### Step 7
Reasoning: No issues found with that exact filter. Let me broaden the search — maybe dueDate is in a different range, or the estimate/dueDate filters are using the wrong format. I'll check all issues assigned to Priya on the ENG team and verify manually.

No exact match on those filters. Let me broaden the search to see all ENG issues assigned to Priya and check the criteria manually:
Command: write {"content": "{\n  \"query\": \"query {\n    issues(\n      first: 100,\n      filter: {\n        assignee: { id: { eq: \\\"caa1ea16-4ec3-4909-9884-4e0da8f29b40\\\" } },\n        team: { id: { eq: \\\"e660af85-ece8-48d1-ad31-b3e400f08a4a\\\" } }\n      }\n    ) {\n      nodes {\n        id\n        identifier\n        title\n        priority\n        estimate\n        dueDate\n        state { name }\n      }\n    }\n  }\"\n}\n", "path": "/tmp/linear_priya_issues.json"}
Response: {"status": "success", "stdout": "Successfully wrote 383 bytes to /tmp/linear_priya_issues.json"}

#### Step 8
Reasoning: Let's try running this broadened search.
Command: curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: <TOKEN>" \
  -H "Content-Type: application/json" \
  --data @/tmp/linear_priya_issues.json
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"47c50000-7316-4e1f-a987-f87e67c4f295\",\"identifier\":\"ENG-16\",\"title\":\"Checkout: tax line missing for EU orders\",\"priority\":2.0,\"estimate\":3.0,\"dueDate\":\"2026-10-01\",\"state\":{\"name\":\"In Progress\"}}]}}}"}

#### Step 9
Reasoning: There's only one ENG issue assigned to Priya: ENG-16, estimate 3 points, but the due date is 2026-10-01 (Thursday), not 2026-10-02 (Friday).

Let's double-check: 2026-10-02 — is that a Friday? Let me verify. 2026-09-30 is stated in the message as Wednesday (Wed 2026-09-30). So October 1 = Thursday, October 2 = Friday. Correct, October 2 is Friday.

ENG-16 is due October 1 (Thursday), not Friday. Estimate matches (3), assignee matches (Priya), team matches (ENG). Only the due date doesn't match.

Let me also confirm I haven't missed anything — perhaps the estimate filter works differently, or the issue might be in a different state (archived?). Let me check all issues with a due date of 2026-10-02 within ENG, regardless of assignee/estimate, to see if there's anything else close. Actually, the strict filter query I ran earlier with all four conditions returned empty. To be safe, let me run one more query: all ENG issues due 2026-10-02, regardless of assignee or estimate.

I found that the only ENG issue assigned to Priya has a due date of Thursday, October 1st, not Friday, so I'll search all ENG issues due Friday to make sure I'm not missing a match.
Command: write {"content": "{\n  \"query\": \"query {\n    issues(\n      first: 100,\n      filter: {\n        team: { id: { eq: \\\"e660af85-ece8-48d1-ad31-b3e400f08a4a\\\" } },\n        dueDate: { eq: \\\"2026-10-02\\\" }\n      }\n    ) {\n      nodes {\n        id\n        identifier\n        title\n        priority\n        estimate\n        dueDate\n        state { name }\n        assignee { name }\n      }\n    }\n  }\"\n}\n", "path": "/tmp/linear_due_friday.json"}
Response: {"status": "success", "stdout": "Successfully wrote 374 bytes to /tmp/linear_due_friday.json"}

#### Step 10
Reasoning: The user is repeating the same request. I was in the middle of verifying. Let me finish the verification — I wrote a query to check all ENG issues due on Friday, October 2, 2026. Let me run it to confirm there's no match before telling the user.

Note: In 2026, October 2 is a Friday. Good.

Let me run the query I wrote.
Command: curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: <TOKEN>" \
  -H "Content-Type: application/json" \
  --data @/tmp/linear_due_friday.json
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[]}}}"}

#### Step 11
Reasoning: Confirmed: There is no ENG issue with a due date of Friday, October 2, 2026. The only ENG issue assigned to Priya Nair is ENG-16, and its due date is Thursday, October 1, 2026 (estimated 3 points, currently in progress, priority 2.0).

In other words, there's no match for all the conditions (Friday Oct 2 + 3 points + Priya). I shouldn't update anything — the user said "if there isn't one, just tell me."

I'll tell them what I found: no ENG issue with a Friday, October 2 due date exists; the closest match is ENG-16 (3 points, Priya, but due Oct 1).

There isn't one. I checked Linear and found no ENG issue matching all your criteria — in fact, no ENG issues are due Friday, October 2 at all.

The closest match: **ENG-16 — "Checkout: tax line missing for EU orders"**, assigned to Priya Nair, estimated at 3 points, currently In Progress — but it's due **Thursday, October 1**, not Friday.

Want me to bump ENG-16 to Urgent instead, or were you thinking of a different date?
Command: 
Response: null

## Final answer
There isn't one. I checked Linear and found no ENG issue matching all your criteria — in fact, no ENG issues are due Friday, October 2 at all.

The closest match: **ENG-16 — "Checkout: tax line missing for EU orders"**, assigned to Priya Nair, estimated at 3 points, currently In Progress — but it's due **Thursday, October 1**, not Friday.

Want me to bump ENG-16 to Urgent instead, or were you thinking of a different date?

## State diff
(no changes)

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": []}. Provisional outcome: correct_absent. Provisional exposed facts: [].

Give your verdict for this trial.