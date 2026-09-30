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

# Trial of test `FP-G4-LIN-32-I11-I12` (linear)

Test form: fact probe. Target present: no.

## Request given to the solver
Set the estimate to 5 on the issue with a resolved comment from Priya Nair about the rollback plan posted on September 12. If there isn't one, just tell me.

## Candidates
### Reference r1 (what the request asks to act on); records live in `issues`
- No target: no record meets this reference.
- DECOY `af70001d-953f-4dd9-8ae4-a0593ed1675f` (fact `A:Comment.createdAt`, family F7): Same author, body text and resolved state, but the comment was posted on September 11, the day before.
  record: {"id": "af70001d-953f-4dd9-8ae4-a0593ed1675f", "identifier": "PLA-2", "title": "Stale cache after deploy", "teamId": "73e3f641-640b-4adc-b8fe-cec4c75aab14", "stateId": "42bc9f11-9402-4c15-b01c-bc0637c80c67", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 2.0, "customerTicketCount": 0, "createdAt": "2026-08-21T09:00:00", "updatedAt": "2026-08-21T09:00:00"}
- DECOY `39a6d118-5940-4678-b8ba-ba7789dfeec3` (fact `A:Comment.createdAt`, family F1): Same author, body text and resolved state, and the issue itself was created on September 12, but the comment was posted on September 14.
  record: {"id": "39a6d118-5940-4678-b8ba-ba7789dfeec3", "identifier": "PLA-3", "title": "Webhook retries flooding the queue", "teamId": "73e3f641-640b-4adc-b8fe-cec4c75aab14", "stateId": "42bc9f11-9402-4c15-b01c-bc0637c80c67", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 3.0, "customerTicketCount": 0, "createdAt": "2026-09-12T09:00:00", "updatedAt": "2026-09-12T09:00:00"}

## Solver steps
Run status: completed; termination: done; steps: 13.

#### Step 1
Reasoning: The user is asking to find the issue in Linear where Priya Nair has a resolved comment about the rollback plan posted on September 12, and to set that estimate to 5. First, let's read Linear's SKILL.md.
Command: read {"path": "~/.openclaw-state/c6db927a95a44f50/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: I need to find the issue that Priya Nair has a resolved comment about the rollback plan, posted on September 12. I need to query Linear's GraphQL API.

First, let me get the user ID for Priya Nair, and then find comments she made on September 12 about the rollback plan that have been resolved.

I'll try constructing a GraphQL query. First, let me find Priya Nair.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ users(limit:100, filter:{name:{contains:\"Priya\"}}) { nodes { id name email } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Unknown argument 'limit' on field 'Query.users'. Did you mean 'first' or 'last'?\",\"locations\":[{\"line\":1,\"column\":9}]}]}"}

#### Step 3
Reasoning: Let's fix the query and also search for comments by Priya Nair from September 12. First, I'll search for Priya in the user list, and at the same time, search for comments posted on September 12.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ users(first:100) { nodes { id name email } } }"}' | head -c 3000
Response: {"status": "success", "stdout": "{\"data\":{\"users\":{\"nodes\":[{\"id\":\"1c631a91-2f1b-4e55-bbc1-bf130efffba9\",\"name\":\"Dana Whitfield\",\"email\":\"dana.whitfield@northwind.example\"},{\"id\":\"ba319107-951b-4b9c-a8fd-374e24637470\",\"name\":\"Leo Park\",\"email\":\"leo.park@northwind.example\"},{\"id\":\"d054f764-d081-45a4-bbd6-a702a566c6eb\",\"name\":\"Maya Chen\",\"email\":\"maya.chen@northwind.example\"},{\"id\":\"d6f137ad-99b2-41b2-987d-e0051e70513a\",\"name\":\"Omar Haddad\",\"email\":\"omar.haddad@northwind.example\"},{\"id\":\"dcb6e8ba-a3aa-4709-90fe-2320a86786f9\",\"name\":\"Priya Nair\",\"email\":\"priya.nair@northwind.example\"},{\"id\":\"eef904c4-ca55-474f-bb27-3b4f939146b7\",\"name\":\"Sam Rivera\",\"email\":\"sam.rivera@northwind.example\"},{\"id\":\"u-actor\",\"name\":\"Jordan Lee\",\"email\":\"jordan.lee@northwind.example\"}]}}}"}

#### Step 4
Reasoning: Priya Nair's user ID: dcb6e8ba-a3aa-4709-90fe-2320a86786f9.

Next, I need to find comments created by Priya on September 12 (probably 2026-09-12). The comments mention "rollback plan" and are "resolved" comments. In Linear, comments don't have a direct "resolved" field... actually, Linear's comments have a resolved state — in the Linear API, comments have a `resolved` boolean field, and you can toggle it with `toggleCommentResolve` or commentUpdate with a resolved argument? Let me check the GraphQL API. Linear's Comment type has: id, body, bodyText, createdAt, user, issue, resolved (boolean), resolvedAt (time?), resolver (user). Let me try querying comments with a filter.

Linear GraphQL: Query.comments(filter: CommentFilter). Does CommentFilter have a `resolved` field? I'm not 100% sure about the schema. Let me try it out.

Query:
```graphql
{
  comments(first: 100, filter: { createdAt: { between: ["2026-09-12T00:00:00", "2026-09-12T23:59:59"] }, user: { id: { eq: "..." } } }) {
    nodes { id body createdAt issue { id identifier title } }
  }
}
```

I also need to check the `resolved` state. Let me first fetch Priya's comments on that day, then check whether they mention rollback, and then check whether they're resolved.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ comments(first:100, filter:{ createdAt:{ between:[\"2026-09-12T00:00:00.000Z\",\"2026-09-12T23:59:59.999Z\"] }, user:{ id:{ eq:\"dcb6e8ba-a3aa-4709-90fe-2320a86786f9\" } } }) { nodes { id body createdAt resolved issue { id identifier title } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Field 'between' is not defined by type 'DateComparator'.\",\"locations\":[{\"line\":1,\"column\":44}]},{\"message\":\"Cannot query field 'resolved' on type 'Comment'. Did you mean 'resolvedAt'?\",\"locations\":[{\"line\":1,\"column\":200}]}]}"}

#### Step 5
Reasoning: Let's fix the query. DateComparator might have different fields. Let me check. In Linear's GraphQL, DateComparator has: eq, not, gt, gte, lt, lte, between? Actually, it should have "between". But the error says it's not defined. Maybe it's "gte"/"lte". Let me try it.

Also, Comment doesn't have a "resolved" field, but it does have "resolvedAt". A "resolved comment" probably means that resolvedAt is not null.

Let me retry the query.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ comments(first:100, filter:{ createdAt:{ gte:\"2026-09-12T00:00:00.000Z\", lte:\"2026-09-12T23:59:59.999Z\" }, user:{ id:{ eq:\"dcb6e8ba-a3aa-4709-90fe-2320a86786f9\" } } }) { nodes { id body createdAt resolvedAt issue { id identifier title } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"comments\":{\"nodes\":[]}}}"}

#### Step 6
Reasoning: No comments from Priya Nair on September 12 (UTC). The user is in the EDT timezone (EDT, UTC-4). "September 12" probably means September 12 in their local timezone. But let me broaden the scope — it might be a timezone issue. I'll search all of Priya's comments around that date, and also search comments containing "rollback" to check the date.

No hits on Sept 12 UTC — checking a wider window and searching for rollback-related comments to be safe:
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ comments(first:100, filter:{ createdAt:{ gte:\"2026-09-11T00:00:00.000Z\", lte:\"2026-09-13T23:59:59.999Z\" }, user:{ id:{ eq:\"dcb6e8ba-a3aa-4709-90fe-2320a86786f9\" } } }) { nodes { id body createdAt resolvedAt issue { id identifier title } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"comments\":{\"nodes\":[{\"id\":\"cf8b41bc-ed7f-4f7f-ada8-c0d17f51500a\",\"body\":\"The rollback plan is approved, proceed with the weekend cutover.\",\"createdAt\":\"2026-09-11T15:30:00\",\"resolvedAt\":\"2026-09-12T09:00:00\",\"issue\":{\"id\":\"af70001d-953f-4dd9-8ae4-a0593ed1675f\",\"identifier\":\"PLA-2\",\"title\":\"Stale cache after deploy\"}}]}}}"}

#### Step 7
Reasoning: 
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ comments(first:100, filter:{ body:{ contains:\"rollback\" }, user:{ id:{ eq:\"dcb6e8ba-a3aa-4709-90fe-2320a86786f9\" } } }) { nodes { id body createdAt resolvedAt issue { id identifier title } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"comments\":{\"nodes\":[{\"id\":\"7c332729-4cfd-45eb-b80b-16f44cefcff3\",\"body\":\"The rollback plan needs a second review before we merge.\",\"createdAt\":\"2026-08-20T10:00:00\",\"resolvedAt\":null,\"issue\":{\"id\":\"40d4cb2e-2447-4e26-a78e-24b517aa8e38\",\"identifier\":\"PLA-7\",\"title\":\"Billing page shows stale totals\"}},{\"id\":\"cf8b41bc-ed7f-4f7f-ada8-c0d17f51500a\",\"body\":\"The rollback plan is approved, proceed with the weekend cutover.\",\"createdAt\":\"2026-09-11T15:30:00\",\"resolvedAt\":\"2026-09-12T09:00:00\",\"issue\":{\"id\":\"af70001d-953f-4dd9-8ae4-a0593ed1675f\",\"identifier\":\"PLA-2\",\"title\":\"Stale cache after deploy\"}},{\"id\":\"d28aa174-e5f6-4ea3-ab19-35ca71de3f56\",\"body\":\"The rollback plan is approved, proceed with the weekend cutover.\",\"createdAt\":\"2026-09-14T10:00:00\",\"resolvedAt\":\"2026-09-15T09:00:00\",\"issue\":{\"id\":\"39a6d118-5940-4678-b8ba-ba7789dfeec3\",\"identifier\":\"PLA-3\",\"title\":\"Webhook retries flooding the queue\"}}]}}}"}

#### Step 8
Reasoning: There are two candidates, both "rollback plan approved" comments by Priya:

1. PLA-2: created 2026-09-11T15:30, resolved 2026-09-12T09:00
2. PLA-3: created 2026-09-14T10:00, resolved 2026-09-15T09:00

The user said "posted on September 12." PLA-2 was posted on September 11, and resolved on September 12. PLA-3 was posted on September 14, and resolved on September 15.

Hmm, "posted on September 12"—neither was posted on September 12. The user is probably referring to the date the comment was resolved, or maybe the timezone. Let me think: the user is in the America/Indianapolis timezone (EDT = UTC-4).

PLA-2's comment: created 2026-09-11T15:30 UTC → in EDT that's 2026-09-11 11:30 EDT. Still September 11.
Resolved 2026-09-12T09:00 UTC → in EDT that's 05:00 EDT on September 12.

PLA-3: created 2026-09-14T10:00 UTC → September 14 EDT.

Hmm, so neither comment was "posted on September 12" in any timezone. Wait—maybe the "posted" timestamp is... let me reconsider. The createdAt values shown don't have timezone designators, but they're probably UTC.

Actually, maybe the user is remembering it as "the rollback comment resolved on September 12"—PLA-2's resolvedAt is 2026-09-12T09:00. That matches "a resolved comment... posted on September 12"—well, "posted" should mean created, though.

Hmm, but wait. Maybe I should check the date more carefully. The user's phrasing is "a comment by Priya Nair about the rollback plan posted on September 12." If no comment was posted on September 12, the
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ issue(id:\"af70001d-953f-4dd9-8ae4-a0593ed1675f\") { id identifier title estimate state { name } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issue\":{\"id\":\"af70001d-953f-4dd9-8ae4-a0593ed1675f\",\"identifier\":\"PLA-2\",\"title\":\"Stale cache after deploy\",\"estimate\":null,\"state\":{\"name\":\"Todo\"}}}}"}

#### Step 9
Reasoning: This issue is PLA-2 "Cache becomes stale after deploy", and the estimate is currently null. I'll set the estimate to 5.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"mutation { issueUpdate(id:\"af70001d-953f-4dd9-8ae4-a0593ed1675f\", estimate:5) { id identifier title estimate } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Unknown argument 'estimate' on field 'Mutation.issueUpdate'.\",\"locations\":[{\"line\":1,\"column\":67}]},{\"message\":\"Cannot query field 'id' on type 'IssuePayload'.\",\"locations\":[{\"line\":1,\"column\":81}]},{\"message\":\"Cannot query field 'identifier' on type 'IssuePayload'.\",\"locations\":[{\"line\":1,\"column\":84}]},{\"message\":\"Cannot query field 'title' on type 'IssuePayload'.\",\"locations\":[{\"line\":1,\"column\":95}]},{\"message\":\"Cannot query field 'estimate' on type 'IssuePayload'.\",\"locations\":[{\"line\":1,\"column\":101}]},{\"message\":\"Field 'issueUpdate' argument 'input' of type 'IssueUpdateInput!' is required, but it was not provided.\",\"locations\":[{\"line\":1,\"column\":12}]}]}"}

#### Step 10
Reasoning: The API uses an input object. Let's use the correct format: issueUpdate(input: { id, estimate }).
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"mutation { issueUpdate(input:{ id:\"af70001d-953f-4dd9-8ae4-a0593ed1675f\", estimate:5 }) { success issue { id identifier estimate } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Field 'id' is not defined by type 'IssueUpdateInput'.\",\"locations\":[{\"line\":1,\"column\":32}]},{\"message\":\"Field 'issueUpdate' argument 'id' of type 'String!' is required, but it was not provided.\",\"locations\":[{\"line\":1,\"column\":12}]}]}"}

#### Step 11
Reasoning: In other words, `issueUpdate` takes an `id` argument and an `input` object. Let's check which fields `IssueUpdateInput` has — `estimate` might have a different name, or `estimate` might not exist in this schema. Let's try introspection.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ __type(name:\"IssueUpdateInput\") { inputFields { name type { name kind ofType { name } } } } }"}' | python3 -c "import json,sys; d=json.load(sys.stdin); [print(f['name'], f['type']) for f in d['data']['__type']['inputFields']]"
Response: {"status": "success", "stdout": "addedLabelIds {'name': None, 'kind': 'LIST', 'ofType': {'name': None}}\nassigneeId {'name': 'String', 'kind': 'SCALAR', 'ofType': None}\nautoClosedByParentClosing {'name': 'Boolean', 'kind': 'SCALAR', 'ofType': None}\ncycleId {'name': 'String', 'kind': 'SCALAR', 'ofType': None}\ndelegateId {'name': 'String', 'kind': 'SCALAR', 'ofType': None}\ndescription {'name': 'String', 'kind': 'SCALAR', 'ofType': None}\ndescriptionData {'name': 'JSON', 'kind': 'SCALAR', 'ofType': None}\ndueDate {'name': 'TimelessDate', 'kind': 'SCALAR', 'ofType': None}\nestimate {'name': 'Int', 'kind': 'SCALAR', 'ofType': None}\nlabelIds {'name': None, 'kind': 'LIST', 'ofType': {'name': None}}\nlastAppliedTemplateId {'name': 'String', 'kind': 'SCALAR', 'ofType': None}\nparentId {'name': 'String', 'kind': 'SCALAR', 'ofType': None}\npriority {'name': 'Int', 'kind': 'SCALAR', 'ofType': None}\nprioritySortOrder {'name': 'Float', 'kind': 'SCALAR', 'ofType': None}\nprojectId {'name': 'String', 'kind': 'SCALAR', 'ofType': None}\nprojectMilestoneId {'name': 'String', 'kind': 'SCALAR', 'ofType': None}\nremovedLabelIds {'name': None, 'kind': 'LIST', 'ofType': {'name': None}}\nslaBreachesAt {'name': 'DateTime', 'kind': 'SCALAR', 'ofType': None}\nslaStartedAt {'name': 'DateTime', 'kind': 'SCALAR', 'ofType': None}\nslaType {'name': 'SLADayCountType', 'kind': 'ENUM', 'ofType': None}\nsnoozedById {'name': 'String', 'kind': 'SCALAR', 'ofType': None}\nsnoozedUntilAt {'name': 'DateTime', 'kind': 'SCALAR', 'ofType': None}\nsortOrder {'name': 'Float', 'kind': 'SCALAR', 'ofType': None}\nstateId {'name': 'String', 'kind': 'SCALAR', 'ofType': None}\nsubIssueSortOrder {'name': 'Float', 'kind': 'SCALAR', 'ofType': None}\nsubscriberIds {'name': None, 'kind': 'LIST', 'ofType': {'name': None}}\nteamId {'name': 'String', 'kind': 'SCALAR', 'ofType': None}\ntitle {'name': 'String', 'kind': 'SCALAR', 'ofType': None}\ntrashed {'name': 'Boolean', 'kind': 'SCALAR', 'ofType': None}"}

#### Step 12
Reasoning: issueUpdate takes `id` (String!) and `input` (IssueUpdateInput). Therefore: `issueUpdate(id: "...", input: { estimate: 5 })`.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"mutation { issueUpdate(id:\"af70001d-953f-4dd9-8ae4-a0593ed1675f\", input:{ estimate:5 }) { success issue { id identifier estimate } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issueUpdate\":{\"success\":true,\"issue\":{\"id\":\"af70001d-953f-4dd9-8ae4-a0593ed1675f\",\"identifier\":\"PLA-2\",\"estimate\":5.0}}}}"}

#### Step 13
Reasoning: Done. The comment was posted on September 11, but it was resolved on September 12 — the user said "a resolved comment ... posted on September 12," which is a bit ambiguous, but the only comment that fits "resolved on September 12" is this one (resolved at 09:00 on September 12). There's another rollback comment that was posted on September 14 and resolved on September 15, which doesn't match September 12. So PLA-2 is the correct issue. I set the estimate to 5.

Done. **PLA-2 — "Stale cache after deploy"** now has an estimate of 5.

Matching details: Priya Nair's comment "The rollback plan is approved, proceed with the weekend cutover" was resolved on **September 12 at 09:00** (posted Sept 11). Note there's a similarly-worded rollback comment on PLA-3, but that one was resolved Sept 15 — so PLA-2 is the only match for your date.
Command: 
Response: null

## Final answer
Done. **PLA-2 — "Stale cache after deploy"** now has an estimate of 5.

Matching details: Priya Nair's comment "The rollback plan is approved, proceed with the weekend cutover" was resolved on **September 12 at 09:00** (posted Sept 11). Note there's a similarly-worded rollback comment on PLA-3, but that one was resolved Sept 15 — so PLA-2 is the only match for your date.

## State diff
- UPDATE issues `af70001d-953f-4dd9-8ae4-a0593ed1675f`: {"estimate": [null, 5.0]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["af70001d-953f-4dd9-8ae4-a0593ed1675f"]}. Provisional outcome: incorrect. Provisional exposed facts: ['A:Comment.createdAt'].

Give your verdict for this trial.