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

# Trial of test `U-G4-LIN-20-Comment_issueId` (linear)

Test form: underspecified (several records fully meet the singular request; each is listed as TARGET). Target present: yes.

## Request given to the solver
Edit Maya Chen's top-level comment mentioning the rollback plan to append 'Approved.' at the end.

## Candidates
### Reference r1 (what the request asks to act on); records live in `comments`
- TARGET `e2aca69a-30c5-409a-b5c3-85af87ea9f76`: {"id": "e2aca69a-30c5-409a-b5c3-85af87ea9f76", "issueId": "fd686c45-06f0-4ee2-a12b-ac87a9506246", "userId": "95fc7151-f3af-4bfd-82a8-b086e86df272", "body": "The rollback plan is drafted and ready for review.", "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- TARGET `a6cec921-abad-45b5-94bf-f4fde4deaf0f`: {"id": "a6cec921-abad-45b5-94bf-f4fde4deaf0f", "issueId": "faee4c00-7ed2-4308-b39c-3b3263cae283", "userId": "95fc7151-f3af-4bfd-82a8-b086e86df272", "body": "The rollback plan covers the mobile checkout flow as well.", "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `3421051c-619b-4ae1-b0a9-a079c06ab02f` (fact `A:Comment.body`, family F0): Same author, issue and level, but its body never mentions the rollback plan.
  record: {"id": "3421051c-619b-4ae1-b0a9-a079c06ab02f", "issueId": "fd686c45-06f0-4ee2-a12b-ac87a9506246", "userId": "95fc7151-f3af-4bfd-82a8-b086e86df272", "body": "Load test results are in and look good for the release.", "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `ab00b93d-79f4-4ba6-abbb-48ba1df045d4` (fact `A:Comment.body`, family F2): Maya's top-level comment whose body lacks the phrase; only a reply in its thread mentions the rollback plan.
  record: {"id": "ab00b93d-79f4-4ba6-abbb-48ba1df045d4", "issueId": "fd686c45-06f0-4ee2-a12b-ac87a9506246", "userId": "95fc7151-f3af-4bfd-82a8-b086e86df272", "body": "Summarizing today's performance review for the team.", "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `8e3c7e66-ba1c-4b51-92fb-beea6d431288` (fact `R:Comment.userId`, family F1): Maya Chen is only mentioned in its body; Sam Rivera posted it.
  record: {"id": "8e3c7e66-ba1c-4b51-92fb-beea6d431288", "issueId": "fd686c45-06f0-4ee2-a12b-ac87a9506246", "userId": "45767a58-0db8-40a1-b8c8-97034c474a10", "body": "Per Maya Chen's estimate, the rollback plan stays on hold until QA signs off.", "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `ded3b3a6-8200-4ced-959b-56b275044023` (fact `R:Comment.userId`, family F8): Posted by Maya Lopez, not Maya Chen.
  record: {"id": "ded3b3a6-8200-4ced-959b-56b275044023", "issueId": "fd686c45-06f0-4ee2-a12b-ac87a9506246", "userId": "1011b32f-6cda-47a3-b864-343be10fc7b4", "body": "The rollback plan looks solid from my side.", "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `047c2f3a-54e8-4a68-9a8e-f28fc64598b3` (fact `H:Comment.parentId`, family F4): Matches everything except that it is a reply in a thread, not a top-level comment.
  record: {"id": "047c2f3a-54e8-4a68-9a8e-f28fc64598b3", "issueId": "fd686c45-06f0-4ee2-a12b-ac87a9506246", "userId": "95fc7151-f3af-4bfd-82a8-b086e86df272", "body": "The rollback plan is drafted and ready for review.", "parentId": "5bad0ebf-158f-44da-8178-14ecc8bf3102", "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}

## Solver steps
Run status: completed; termination: done; steps: 12.

#### Step 1
Reasoning: The user wants me to work in Linear: edit a top-level comment by Maya Chen that mentions a rollback plan, and append "Approved." to the end of it.

First, let me read Linear's SKILL.md to understand how to use it.
Command: read {"path": "~/.openclaw-state/1556dab10baa44b6/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: The skill's documentation is thin on content. What I need to do is:
1. Find the relevant issue (Maya Chen's comment about the rollback plan)
2. Find the top-level comment (no parentId) that mentions the rollback plan, posted by Maya Chen
3. Edit it to append "Approved." at the end

Let me start by querying the Linear API. First, I need to find the issue and the comment. The user is saying "Maya Chen's top-level comment that mentions the rollback plan," but which issue is it in? It might be a recent issue. Let me search for comments that mention the rollback plan.

First, let me check if there's any existing session environment or proxy setup. The skill says "authentication is handled automatically via the proxy. Use a placeholder token like `<TOKEN>`." So I'll curl using the placeholder token `<TOKEN>`.

Let me query comments that mention the rollback. GraphQL: comments(query: "rollback"). Let me try that first.
Command: curl -sS https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: <TOKEN>" -d '{"query":"query { comments(first: 50, query: \"rollback\") { nodes { id body createdAt updatedAt issue { id identifier title } creator { name } parentId } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Unknown argument 'query' on field 'Query.comments'.\",\"locations\":[{\"line\":1,\"column\":29}]},{\"message\":\"Cannot query field 'creator' on type 'Comment'.\",\"locations\":[{\"line\":1,\"column\":116}]}]}"}

#### Step 3
Reasoning: The comments query does not accept the "query" argument, and "creator" is not a field on Comment. Let me first check the schema.
Command: curl -sS https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: <TOKEN>" -d '{"query":"query { __type(name: \"Comment\") { fields { name } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"fields\":[{\"name\":\"agentSession\"},{\"name\":\"agentSessions\"},{\"name\":\"archivedAt\"},{\"name\":\"body\"},{\"name\":\"bodyData\"},{\"name\":\"botActor\"},{\"name\":\"children\"},{\"name\":\"createdAt\"},{\"name\":\"documentContent\"},{\"name\":\"documentContentId\"},{\"name\":\"editedAt\"},{\"name\":\"externalThread\"},{\"name\":\"externalUser\"},{\"name\":\"id\"},{\"name\":\"initiativeUpdate\"},{\"name\":\"initiativeUpdateId\"},{\"name\":\"issue\"},{\"name\":\"issueId\"},{\"name\":\"parent\"},{\"name\":\"parentId\"},{\"name\":\"post\"},{\"name\":\"projectUpdate\"},{\"name\":\"projectUpdateId\"},{\"name\":\"quotedText\"},{\"name\":\"reactionData\"},{\"name\":\"reactions\"},{\"name\":\"resolvedAt\"},{\"name\":\"resolvingComment\"},{\"name\":\"resolvingCommentId\"},{\"name\":\"resolvingUser\"},{\"name\":\"syncedWith\"},{\"name\":\"threadSummary\"},{\"name\":\"updatedAt\"},{\"name\":\"url\"},{\"name\":\"user\"}]}}}"}

#### Step 4
Reasoning: Comments have a `user` field and a `children` field. Let's try querying comments filtered by user. I need to find Maya Chen's top-level comment that mentions a rollback plan. Top-level probably means a comment that has no parent (parentId is null).

First, let me search for Maya Chen's user ID, then query her comments and look for ones that mention "rollback".
Command: curl -sS https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: <TOKEN>" -d '{"query":"query { users(query: \"Maya\") { nodes { id name email } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Unknown argument 'query' on field 'Query.users'.\",\"locations\":[{\"line\":1,\"column\":15}]}]}"}

#### Step 5
Reasoning: The Linear API in this environment is a limited version. Let me check which queries exist. I'll try fetching comments directly and looking for ones that mention rollback.
Command: curl -sS https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: <TOKEN>" -d '{"query":"query { comments(first: 100) { nodes { id body createdAt user { name } parentId issue { identifier title } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"comments\":{\"nodes\":[{\"id\":\"047c2f3a-54e8-4a68-9a8e-f28fc64598b3\",\"body\":\"The rollback plan is drafted and ready for review.\",\"createdAt\":\"2026-06-01T09:00:00\",\"user\":{\"name\":\"Maya Chen\"},\"parentId\":\"5bad0ebf-158f-44da-8178-14ecc8bf3102\",\"issue\":{\"identifier\":\"WEB-1\",\"title\":\"Checkout latency spikes\"}},{\"id\":\"3421051c-619b-4ae1-b0a9-a079c06ab02f\",\"body\":\"Load test results are in and look good for the release.\",\"createdAt\":\"2026-06-01T09:00:00\",\"user\":{\"name\":\"Maya Chen\"},\"parentId\":null,\"issue\":{\"identifier\":\"WEB-1\",\"title\":\"Checkout latency spikes\"}},{\"id\":\"5a7fbc82-c8e5-425a-a249-27606fe219a0\",\"body\":\"Thanks, can you also share the rollback plan timeline?\",\"createdAt\":\"2026-06-01T09:00:00\",\"user\":{\"name\":\"Omar Haddad\"},\"parentId\":\"ab00b93d-79f4-4ba6-abbb-48ba1df045d4\",\"issue\":{\"identifier\":\"WEB-1\",\"title\":\"Checkout latency spikes\"}},{\"id\":\"5bad0ebf-158f-44da-8178-14ecc8bf3102\",\"body\":\"Looking into the latency numbers this afternoon.\",\"createdAt\":\"2026-06-01T09:00:00\",\"user\":{\"name\":\"Leo Park\"},\"parentId\":null,\"issue\":{\"identifier\":\"WEB-1\",\"title\":\"Checkout latency spikes\"}},{\"id\":\"8e3c7e66-ba1c-4b51-92fb-beea6d431288\",\"body\":\"Per Maya Chen's estimate, the rollback plan stays on hold until QA signs off.\",\"createdAt\":\"2026-06-01T09:00:00\",\"user\":{\"name\":\"Sam Rivera\"},\"parentId\":null,\"issue\":{\"identifier\":\"WEB-1\",\"title\":\"Checkout latency spikes\"}},{\"id\":\"a6cec921-abad-45b5-94bf-f4fde4deaf0f\",\"body\":\"The rollback plan covers the mobile checkout flow as well.\",\"createdAt\":\"2026-06-01T09:00:00\",\"user\":{\"name\":\"Maya Chen\"},\"parentId\":null,\"issue\":{\"identifier\":\"WEB-2\",\"title\":\"Checkout latency spikes on mobile\"}},{\"id\":\"ab00b93d-79f4-4ba6-abbb-48ba1df045d4\",\"body\":\"Summarizing today's performance review for the team.\",\"createdAt\":\"2026-06-01T09:00:00\",\"user\":{\"name\":\"Maya Chen\"},\"parentId\":null,\"issue\":{\"identifier\":\"WEB-1\",\"title\":\"Checkout latency spikes\"}},{\"id\":\"ded3b3a6-8200-4ced-959b-56b275044023\",\"body\":\"The rollback plan looks solid from my side.\",\"createdAt\":\"2026-06-01T09:00:00\",\"user\":{\"name\":\"Maya Lopez\"},\"parentId\":null,\"issue\":{\"identifier\":\"WEB-1\",\"title\":\"Checkout latency spikes\"}},{\"id\":\"e2aca69a-30c5-409a-b5c3-85af87ea9f76\",\"body\":\"The rollback plan is drafted and ready for review.\",\"createdAt\":\"2026-06-01T09:00:00\",\"user\":{\"name\":\"Maya Chen\"},\"parentId\":null,\"issue\":{\"identifier\":\"WEB-1\",\"title\":\"Checkout latency spikes\"}},{\"id\":\"ee15ca46-a27e-4789-b294-0b972d726d00\",\"body\":\"Pagination edge cases need design input.\",\"createdAt\":\"2026-06-01T09:00:00\",\"user\":{\"name\":\"Leo Park\"},\"parentId\":null,\"issue\":{\"identifier\":\"WEB-3\",\"title\":\"Search results pagination\"}}]}}}"}

#### Step 6
Reasoning: Maya Chen's comments:
1. `047c2f3a...` "Rollback plan has been drafted and is ready for review." — parentId: 5bad0ebf (a child comment, not top-level)
2. `3421051c...` "Load test results are in, and they're looking good for the release." — top-level (parentId is null), but doesn't mention rollback
3. `a6cec921...` "Rollback plan also covers the mobile checkout flow." — top-level, parentId is null, WEB-2
4. `ab00b93d...` "Summarizing today's performance review for the team." — top-level, but doesn't mention rollback
5. `e2aca69a...` "Rollback plan has been drafted and is ready for review." — top-level, parentId is null, WEB-1

So there are two top-level comments by Maya Chen that mention the rollback plan:
- `e2aca69a` (WEB-1): "Rollback plan has been drafted and is ready for review."
- `a6cec921` (WEB-2): "Rollback plan also covers the mobile checkout flow."

Hmm, ambiguous. The task says "the top-level comment by Maya Chen that mentions the rollback plan." Both apply. Wait — but the list is first:100, so there might be more comments. Let me check pagination. Also, could there be a distinction: "mentioning the rollback plan" — both mention it.

Hmm, one is WEB-1 and the other is WEB-2. Let me check if there are additional comments beyond the first 100. Let me fetch with pagination and look at the totalCount.

Actually, let me think about what distinguishes the two. "The top-level comment by Maya Chen that mentions the rollback plan" — singular. Perhaps there's only one top-le
Command: curl -sS https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: <TOKEN>" -d '{"query":"query { comments(first: 100) { totalCount pageInfo { hasNextPage endCursor } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'totalCount' on type 'CommentConnection'.\",\"locations\":[{\"line\":1,\"column\":32}]}]}"}

#### Step 7
Reasoning: The comments connection doesn't have a totalCount. Let me check the fields of CommentConnection to look into pagination.
Command: curl -sS https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: <TOKEN>" -d '{"query":"query { __type(name: \"CommentConnection\") { fields { name } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"fields\":[{\"name\":\"edges\"},{\"name\":\"nodes\"},{\"name\":\"pageInfo\"}]}}}"}

#### Step 8
Reasoning: Let me think about the candidate comments from Maya Chen that are top-level (parentId = null) and mention the rollback plan.

From the first 100 comments:
1. `047c2f3a...` - "The rollback plan has been drafted and is ready for review." - Maya Chen - parentId: `5bad0ebf...` (NOT top-level)
2. `3421051c...` - "The load test results came back and look good for release." - Maya Chen - parentId: null - but doesn't mention the rollback plan
3. `5a7fbc82...` - Omar Haddad (not Maya Chen)
4. `5bad0ebf...` - Leo Park
5. `8e3c7e66...` - Sam Rivera (mentions Maya Chen and the rollback plan, but the author is Sam, and it's top-level — but the task says "Maya Chen's top-level comment that mentions the rollback plan")
6. `a6cec921...` - "The rollback plan also covers the mobile checkout flow." - Maya Chen - parentId: null - top-level, mentions the rollback plan ✓ (WEB-2)
7. `ab00b93d...` - Maya Chen - "Summarizing today's performance review for the team." - top-level, doesn't mention the rollback plan
8. `ded3b3a6...` - Maya Lopez (not Maya Chen) - "The rollback plan looks solid from my side." - top-level, but the author is Maya Lopez
9. `e2aca69a...` - "The rollback plan has been drafted and is ready for review." - Maya Chen - parentId: null - top-level, mentions the rollback plan ✓ (WEB-1)
10. `ee15ca46...` - Leo Park - doesn't mention the rollback plan

So, there are two candidates for Maya Chen's top-level comments that mention the rollback plan:
- `a6cec921...` (WEB-2): "The rollback 
Command: curl -sS https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: <TOKEN>" -d '{"query":"query { comments(first: 100) { nodes { id } pageInfo { hasNextPage endCursor } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"comments\":{\"nodes\":[{\"id\":\"047c2f3a-54e8-4a68-9a8e-f28fc64598b3\"},{\"id\":\"3421051c-619b-4ae1-b0a9-a079c06ab02f\"},{\"id\":\"5a7fbc82-c8e5-425a-a249-27606fe219a0\"},{\"id\":\"5bad0ebf-158f-44da-8178-14ecc8bf3102\"},{\"id\":\"8e3c7e66-ba1c-4b51-92fb-beea6d431288\"},{\"id\":\"a6cec921-abad-45b5-94bf-f4fde4deaf0f\"},{\"id\":\"ab00b93d-79f4-4ba6-abbb-48ba1df045d4\"},{\"id\":\"ded3b3a6-8200-4ced-959b-56b275044023\"},{\"id\":\"e2aca69a-30c5-409a-b5c3-85af87ea9f76\"},{\"id\":\"ee15ca46-a27e-4789-b294-0b972d726d00\"}],\"pageInfo\":{\"hasNextPage\":false,\"endCursor\":\"eyJmaWVsZCI6ICIyMDI2LTA2LTAxVDA5OjAwOjAwIiwgImlkIjogImVlMTVjYTQ2LWEyN2UtNDc4OS1iMjk0LTBiOTcyZDcyNmQwMCJ9\"}}}}"}

#### Step 9
Reasoning: I've checked all the comments (hasNextPage: false, 10 total). The top-level comments from Maya Chen that mention the rollback plan:

1. `e2aca69a-30c5-409a-b5c3-85af87ea9f76` (WEB-1): "The rollback plan has been created and is ready for review." — parentId is null
2. `a6cec921-abad-45b5-94bf-f4fde4deaf0f` (WEB-2): "The rollback plan also covers the mobile checkout flow." — parentId is null

The first one `047c2f3a` has parentId `5bad0ebf`, so it's not top-level.

Hmm, the task says "the top-level comment" (singular). But there are two. Which one is the user referring to?

- WEB-1 e2aca69a: "The rollback plan has been created and is ready for review." — this is a comment about the state of the rollback plan, and appending "Approved." makes sense in this context (the comment states it's ready for review, and adding Approved indicates approval).
- WEB-2 a6cec921: "The rollback plan also covers the mobile checkout flow." — appending "Approved." here is less likely.

Hmm, this is ambiguous. "The top-level comment that mentions the rollback plan" — singular. The most natural reading is the comment that is about the rollback plan itself: "The rollback plan has been created and is ready for review." Appending "Approved." to a comment saying "ready for review" is a very natural approval action.

Actually, wait — I should probably also check the body of comments on other issues. The comment query returned 10 total across all issues. So the candidates are only these two.

Should I updat
Command: curl -sS https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: <TOKEN>" -d '{"query":"mutation { commentUpdate(id: \"e2aca69a-30c5-409a-b5c3-85af87ea9f76\", body: \"The rollback plan is drafted and ready for review. Approved.\") { id body editedAt } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Unknown argument 'body' on field 'Mutation.commentUpdate'.\",\"locations\":[{\"line\":1,\"column\":70}]},{\"message\":\"Cannot query field 'id' on type 'CommentPayload'.\",\"locations\":[{\"line\":1,\"column\":142}]},{\"message\":\"Cannot query field 'body' on type 'CommentPayload'.\",\"locations\":[{\"line\":1,\"column\":145}]},{\"message\":\"Cannot query field 'editedAt' on type 'CommentPayload'.\",\"locations\":[{\"line\":1,\"column\":150}]},{\"message\":\"Field 'commentUpdate' argument 'input' of type 'CommentUpdateInput!' is required, but it was not provided.\",\"locations\":[{\"line\":1,\"column\":12}]}]}"}

#### Step 10
Reasoning: I need to use the input structure for this.
Command: curl -sS https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: <TOKEN>" -d '{"query":"mutation { commentUpdate(input: {id: \"e2aca69a-30c5-409a-b5c3-85af87ea9f76\", body: \"The rollback plan is drafted and ready for review. Approved.\"}) { success comment { id body editedAt } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Field 'id' is not defined by type 'CommentUpdateInput'.\",\"locations\":[{\"line\":1,\"column\":34}]},{\"message\":\"Field 'commentUpdate' argument 'id' of type 'String!' is required, but it was not provided.\",\"locations\":[{\"line\":1,\"column\":12}]}]}"}

#### Step 11
Reasoning: The mutation signature is `commentUpdate(id: String!, input: CommentUpdateInput!)`. Let me verify the exact field.
Command: curl -sS https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: <TOKEN>" -d '{"query":"mutation { commentUpdate(id: \"e2aca69a-30c5-409a-b5c3-85af87ea9f76\", input: {body: \"The rollback plan is drafted and ready for review. Approved.\"}) { success comment { id body editedAt } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"commentUpdate\":{\"success\":true,\"comment\":{\"id\":\"e2aca69a-30c5-409a-b5c3-85af87ea9f76\",\"body\":\"The rollback plan is drafted and ready for review. Approved.\",\"editedAt\":\"2026-09-29T05:12:22.871157+00:00\"}}}}"}

#### Step 12
Reasoning: Updated. Verifying — the response already confirms that the body has been changed. That should be sufficient.

Done. Updated Maya Chen's top-level comment on WEB-1 ("Checkout latency spikes"):

> "The rollback plan is drafted and ready for review. **Approved.**"

One note: she also has a top-level comment on WEB-2 ("The rollback plan covers the mobile checkout flow as well.") — I left that alone since it reads as informational, not pending approval. Say the word if you wanted "Approved." on that one too.
Command: 
Response: null

## Final answer
Done. Updated Maya Chen's top-level comment on WEB-1 ("Checkout latency spikes"):

> "The rollback plan is drafted and ready for review. **Approved.**"

One note: she also has a top-level comment on WEB-2 ("The rollback plan covers the mobile checkout flow as well.") — I left that alone since it reads as informational, not pending approval. Say the word if you wanted "Approved." on that one too.

## State diff
- UPDATE comments `e2aca69a-30c5-409a-b5c3-85af87ea9f76`: {"body": ["The rollback plan is drafted and ready for review.", "The rollback plan is drafted and ready for review. Approved."], "editedAt": [null, "2026-09-29T05:12:22.871157"]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["e2aca69a-30c5-409a-b5c3-85af87ea9f76"]}. Provisional outcome: incomplete. Provisional exposed facts: [].

Give your verdict for this trial.