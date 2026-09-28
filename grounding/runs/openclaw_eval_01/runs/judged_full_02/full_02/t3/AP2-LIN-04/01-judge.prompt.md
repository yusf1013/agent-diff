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

# Trial of test `AP2-LIN-04` (linear)

Test form: cover. Target present: yes.

## Request given to the solver
The Fall Kickoff cycle that starts September 29 and includes the checkout timeout issue assigned to Sam Rivera needs its end date pushed to October 20.

## Candidates
### Reference r1 (what the request asks to act on); records live in `cycles`
- TARGET `c-target`: {"id": "c-target", "teamId": "t-web", "number": 14.0, "name": "Fall Kickoff", "startsAt": "2026-09-29T00:00:00", "endsAt": "2026-10-13T00:00:00", "isActive": false, "isNext": false, "isPast": false, "isFuture": false, "isPrevious": false, "progress": 0.0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `c-name` (fact `A:Cycle.name`, family F8): Mobile's cycle is named Fall Kickoff Retro, not Fall Kickoff; it also starts September 29 and has its own checkout timeout issue assigned to Sam Rivera.
  record: {"id": "c-name", "teamId": "t-mob", "number": 7.0, "name": "Fall Kickoff Retro", "startsAt": "2026-09-29T00:00:00", "endsAt": "2026-10-13T00:00:00", "isActive": false, "isNext": false, "isPast": false, "isFuture": false, "isPrevious": false, "progress": 0.0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `c-time` (fact `A:Cycle.startsAt`, family F7): Platform also has a cycle named Fall Kickoff with a checkout timeout issue assigned to Sam Rivera, but it starts September 15, the cycle before.
  record: {"id": "c-time", "teamId": "t-plat", "number": 5.0, "name": "Fall Kickoff", "startsAt": "2026-09-15T00:00:00", "endsAt": "2026-09-29T00:00:00", "isActive": false, "isNext": false, "isPast": false, "isFuture": false, "isPrevious": false, "progress": 0.0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `c-split` (fact `B:Issue.cycleId`, family F5): Growth's Fall Kickoff cycle also starts September 29, but the checkout timeout issue there is assigned to Leo Park; the issue assigned to Sam Rivera is a different one, about the onboarding checklist.
  record: {"id": "c-split", "teamId": "t-growth", "number": 9.0, "name": "Fall Kickoff", "startsAt": "2026-09-29T00:00:00", "endsAt": "2026-10-13T00:00:00", "isActive": false, "isNext": false, "isPast": false, "isFuture": false, "isPrevious": false, "progress": 0.0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}

## Solver steps
Run status: completed; termination: done; steps: 12.

#### Step 1
Reasoning: The user is asking me to modify a Linear cycle called "Fall Kickoff" that starts on September 29 and includes a checkout timeout issue assigned to Sam Rivera. They want to extend the end date to October 20.

There's an available Linear skill. I should first read its SKILL.md.
Command: read {"path": "~/.openclaw-state/bf9b869da594456b/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: SKILL.md is pretty thin on details about the cycles/projects API. I need to look into how to query cycles in Linear. Linear's GraphQL API has `cycles`, `cycle`, `projectUpdate`, `cycleUpdate`, and so on.

Task: find the "Fall Kickoff" cycle that starts on September 29 and includes the checkout timeout issue assigned to Sam Rivera. I need to extend the end date to October 20.

First, let me verify authentication and do some exploration. I need to find:
1. The checkout timeout issue assigned to Sam Rivera
2. The "Fall Kickoff" cycle that starts on September 29
3. Update the end date to October 20, 2026

Let me start with a query. The API might need a token. According to the skill, authentication is handled automatically via a proxy, so I should use the placeholder token `<TOKEN>`.

First let me query users to find Sam Rivera, and search for the checkout timeout issue.
Command: curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"{ users(limit: 100, filter: {name: {contains: \"Rivera\"}}) { nodes { id name email } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Unknown argument 'limit' on field 'Query.users'. Did you mean 'first' or 'last'?\",\"locations\":[{\"line\":1,\"column\":9}]}]}"}

#### Step 3
Reasoning: 
Command: curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"{ cycles(limit: 50) { nodes { id name startDate dueDate completedAt team { key } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Unknown argument 'limit' on field 'Query.cycles'. Did you mean 'first' or 'last'?\",\"locations\":[{\"line\":1,\"column\":10}]},{\"message\":\"Cannot query field 'startDate' on type 'Cycle'. Did you mean 'startsAt'?\",\"locations\":[{\"line\":1,\"column\":39}]},{\"message\":\"Cannot query field 'dueDate' on type 'Cycle'.\",\"locations\":[{\"line\":1,\"column\":49}]}]}"}

#### Step 4
Reasoning: I need to correct the schema — use `first`/`last`, and use the `startsAt`/`endsAt` fields.
Command: curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"{ users(first: 100, filter: {name: {contains: \"Rivera\"}}) { nodes { id name email } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"users\":{\"nodes\":[{\"id\":\"u-sam\",\"name\":\"Sam Rivera\",\"email\":\"sam.rivera@northwind.example\"}]}}}"}

#### Step 5
Reasoning: 
Command: curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"{ cycles(first: 50) { nodes { id name startsAt endsAt completedAt team { key } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"cycles\":{\"nodes\":[{\"id\":\"c-name\",\"name\":\"Fall Kickoff Retro\",\"startsAt\":\"2026-09-29T00:00:00\",\"endsAt\":\"2026-10-13T00:00:00\",\"completedAt\":null,\"team\":{\"key\":\"MOB\"}},{\"id\":\"c-split\",\"name\":\"Fall Kickoff\",\"startsAt\":\"2026-09-29T00:00:00\",\"endsAt\":\"2026-10-13T00:00:00\",\"completedAt\":null,\"team\":{\"key\":\"GRO\"}},{\"id\":\"c-support\",\"name\":\"Winter Wrap\",\"startsAt\":\"2026-08-18T00:00:00\",\"endsAt\":\"2026-09-01T00:00:00\",\"completedAt\":null,\"team\":{\"key\":\"SUP\"}},{\"id\":\"c-target\",\"name\":\"Fall Kickoff\",\"startsAt\":\"2026-09-29T00:00:00\",\"endsAt\":\"2026-10-13T00:00:00\",\"completedAt\":null,\"team\":{\"key\":\"WEB\"}},{\"id\":\"c-time\",\"name\":\"Fall Kickoff\",\"startsAt\":\"2026-09-15T00:00:00\",\"endsAt\":\"2026-09-29T00:00:00\",\"completedAt\":null,\"team\":{\"key\":\"PLA\"}}]}}}"}

#### Step 6
Reasoning: Sam Rivera (u-sam). There are multiple cycles named "Fall Kickoff":
- c-split: Fall Kickoff, GRO, 2026-09-29 → 2026-10-13
- c-target: Fall Kickoff, WEB, 2026-09-29 → 2026-10-13
- c-time: Fall Kickoff, PLA, 2026-09-15 → 2026-09-29
- c-name: "Fall Kickoff Retro", MOB, 2026-09-29 → 2026-10-13 (the name is different, so it's excluded)

The one that "starts on September 29 and includes the checkout timeout issue assigned to Sam Rivera" — I need to check which cycle contains that issue. Let me try querying for issues whose title contains "checkout timeout" and whose assignee is Sam.
Command: curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"{ issues(first: 50, filter: {title: {contains: \"checkout timeout\"}, assignee: {id: {eq: \"u-sam\"}}}) { nodes { id identifier title assignee { name } cycle { id name } team { key } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[]}}}"}

#### Step 7
Reasoning: No matches were found. I'll broaden the search scope — searching for issues with "checkout" in the title and "timeout" in the title separately, as well as issues assigned to Sam.
Command: curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"{ issues(first: 50, filter: {title: {contains: \"checkout\"}}) { nodes { id identifier title assignee { name } cycle { id name } team { key } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[]}}}"}

#### Step 8
Reasoning: 
Command: curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"{ issues(first: 50, filter: {assignee: {id: {eq: \"u-sam\"}}}) { nodes { id identifier title assignee { name } cycle { id name } team { key } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"i-growth-b\",\"identifier\":\"GRO-2\",\"title\":\"Rewrite onboarding checklist copy\",\"assignee\":{\"name\":\"Sam Rivera\"},\"cycle\":{\"id\":\"c-split\",\"name\":\"Fall Kickoff\"},\"team\":{\"key\":\"GRO\"}},{\"id\":\"i-mob-a\",\"identifier\":\"MOB-1\",\"title\":\"Checkout timeout on Apple Pay sheet\",\"assignee\":{\"name\":\"Sam Rivera\"},\"cycle\":{\"id\":\"c-name\",\"name\":\"Fall Kickoff Retro\"},\"team\":{\"key\":\"MOB\"}},{\"id\":\"i-plat-a\",\"identifier\":\"PLA-1\",\"title\":\"Checkout timeout during 3DS redirect\",\"assignee\":{\"name\":\"Sam Rivera\"},\"cycle\":{\"id\":\"c-time\",\"name\":\"Fall Kickoff\"},\"team\":{\"key\":\"PLA\"}},{\"id\":\"i-web-14\",\"identifier\":\"WEB-1\",\"title\":\"Checkout timeout on payment retry\",\"assignee\":{\"name\":\"Sam Rivera\"},\"cycle\":{\"id\":\"c-target\",\"name\":\"Fall Kickoff\"},\"team\":{\"key\":\"WEB\"}}]}}}"}

#### Step 9
Reasoning: Interesting. Multiple checkout timeout issues are assigned to Sam Rivera:

1. **MOB-1** "Checkout timeout on Apple Pay sheet" — cycle: c-name "Fall Kickoff Retro" (MOB team), starts 2026-09-29, ends 2026-10-13
2. **PLA-1** "Checkout timeout during 3DS redirect" — cycle: c-time "Fall Kickoff" (PLA team), starts 2026-09-15, ends 2026-09-29 — this doesn't start on Sept 29
3. **WEB-1** "Checkout timeout on payment retry" — cycle: c-target "Fall Kickoff" (WEB team), starts 2026-09-29, ends 2026-10-13
4. GRO-2 is not a checkout timeout issue.

The user said: "the Fall Kickoff cycle that starts on Sept 29 and contains the checkout timeout issue assigned to Sam Rivera."

Hmm, there are two candidates:
- c-name "Fall Kickoff Retro" (MOB) — starts Sept 29, contains MOB-1 checkout timeout issue. But its name is "Fall Kickoff Retro," not exactly "Fall Kickoff."
- c-target "Fall Kickoff" (WEB) — starts Sept 29, contains WEB-1 checkout timeout issue. The name is exactly "Fall Kickoff."
- c-split "Fall Kickoff" (GRO) — starts Sept 29, but only contains GRO-2, not a checkout timeout.
- c-time "Fall Kickoff" (PLA) — starts Sept 15, not Sept 29.

So the exact "Fall Kickoff" name + starts Sept 29 + contains checkout timeout assigned to Sam → c-target (WEB team) is the best match. c-name's cycle is "Fall Kickoff Retro," which contains a checkout timeout issue but the name is "Fall Kickoff Retro."

Hmm, this is ambiguous. But the user said "the Fall Kickoff cycle" — the name is exactly "Fall Kick
Command: curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"mutation { cycleUpdate(id: \"c-target\", input: { endsAt: \"2026-10-20T00:00:00\" }) { id name startsAt endsAt success } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'id' on type 'CyclePayload'.\",\"locations\":[{\"line\":1,\"column\":84}]},{\"message\":\"Cannot query field 'name' on type 'CyclePayload'.\",\"locations\":[{\"line\":1,\"column\":87}]},{\"message\":\"Cannot query field 'startsAt' on type 'CyclePayload'.\",\"locations\":[{\"line\":1,\"column\":92}]},{\"message\":\"Cannot query field 'endsAt' on type 'CyclePayload'.\",\"locations\":[{\"line\":1,\"column\":101}]}]}"}

#### Step 10
Reasoning: The mutation failed because of the selection fields. Let me retry with `success` only (the payload type).
Command: curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"mutation { cycleUpdate(id: \"c-target\", input: { endsAt: \"2026-10-20T00:00:00\" }) { success } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"cycleUpdate\":{\"success\":true}}}"}

#### Step 11
Reasoning: The update succeeded. Let's check whether the end date was actually changed.
Command: curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"{ cycle(id: \"c-target\") { id name team { key } startsAt endsAt } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"cycle\":{\"id\":\"c-target\",\"name\":\"Fall Kickoff\",\"team\":{\"key\":\"WEB\"},\"startsAt\":\"2026-09-29T00:00:00\",\"endsAt\":\"2026-10-20T00:00:00\"}}}"}

#### Step 12
Reasoning: Completed and confirmed. I'll provide a concise reply.

Done. The **Fall Kickoff** cycle on the WEB team (starts Sep 29, includes WEB-1 "Checkout timeout on payment retry" assigned to Sam Rivera) now ends **October 20** instead of October 13. Verified via API: `startsAt: 2026-09-29, endsAt: 2026-10-20`.
Command: 
Response: null

## Final answer
Done. The **Fall Kickoff** cycle on the WEB team (starts Sep 29, includes WEB-1 "Checkout timeout on payment retry" assigned to Sam Rivera) now ends **October 20** instead of October 13. Verified via API: `startsAt: 2026-09-29, endsAt: 2026-10-20`.

## State diff
- UPDATE cycles `c-target`: {"endsAt": ["2026-10-13T00:00:00", "2026-10-20T00:00:00"]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["c-target"]}. Provisional outcome: correct. Provisional exposed facts: [].

Give your verdict for this trial.