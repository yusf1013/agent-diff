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

# Trial of test `P-G4-LIN-05-I12` (linear)

Test form: probe. Target present: no.

## Request given to the solver
Add the note Scope locked to the description of the Web team's current cycle, the one that ends on September 30. If there isn't one, just tell me.

## Candidates
### Reference r1 (what the request asks to act on); records live in `cycles`
- No target: no record meets this reference.
- DECOY `42f20ce6-141f-4a84-870a-6e9f46a354a7` (fact `R:Cycle.teamId`, family F8): Payments runs a Cycle 41 with the identical start and end dates and it is active too, but it belongs to the Payments team, not Web.
  record: {"id": "42f20ce6-141f-4a84-870a-6e9f46a354a7", "teamId": "042673ca-19ec-497b-af44-3fbcda13604b", "number": 41.0, "name": "Cycle 41", "startsAt": "2026-09-16T00:00:00Z", "endsAt": "2026-09-30T23:59:59Z", "isActive": true, "isNext": false, "isPast": false, "isFuture": false, "isPrevious": false, "progress": 0.0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}

## Solver steps
Run status: completed; termination: done; steps: 7.

#### Step 1
Reasoning: The user is asking to add a note "Scope locked" to the description of the Web team's current cycle in Linear (the one that ends on September 30). I need to use the Linear skill. First, let me read the skill.
Command: read {"path": "~/.openclaw-state/5c78a54f8e5f4ad1/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: The skill is minimal. I need to interact with the Linear GraphQL API via curl. What needs to be done:

1. Find the Web team (query teams).
2. Find its "current cycle"—a cycle that ends on September 30. Hmm, "cycle"—Linear has a "cycle" concept in its Project feature (project cycles). But it's also possible that "cycle" refers to a project. The user is saying "Web team's current cycle, i.e., the one ending on September 30." So I should query the team's cycles/projects that end on 2026-09-30.

Wait, the current date is 2026-09-30 (Wed 2026-09-30 07:12 EDT). So the cycle that ends today, September 30.

3. If found, update the description to append the note "Scope locked" (probably append to the existing description, or set the description if it's empty). "Add the note Scope locked to the description"—I should fetch the current description, append "Scope locked" to it, and update.

Let's start with the queries. First, get the teams and find the Web team's ID. Then query the team's cycles.

In Linear's GraphQL, the Team type has a `cycles` field: Team has `cycles: [Cycle!]!` (when using the cycles feature), and `projects`. Cycle type: `Cycle { id, name, number, startDate, targetDate, completedAt, description? ... }`. Does Cycle have `updateCycle`? Actually, Linear has a `cycleUpdate` mutation. Let me recall: Linear API mutations include `cycleCreate`, `cycleComplete`, `cycleUpdate`? I think `cycleUpdate(input: CycleUpdateInput!)` exists and supports description updates.

But I'm n
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"{ teams { nodes { id name key } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"teams\":{\"nodes\":[{\"id\":\"042673ca-19ec-497b-af44-3fbcda13604b\",\"name\":\"Payments\",\"key\":\"PAY\"},{\"id\":\"539359f9-71ad-4fcc-a93b-e942900bad47\",\"name\":\"Web\",\"key\":\"WEB\"}]}}}"}

#### Step 3
Reasoning: The Web team's ID is 539359f9-71ad-4fcc-a93b-e942900bad47. Next, I'll look for cycles. According to the skill documentation, the Linear GraphQL API has cycles. Let me try querying the cycles for this team.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"{ cycles(filter: {team: {id: {eq: \"539359f9-71ad-4fcc-a93b-e942900bad47\"}}}) { nodes { id name startDate endDate description } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'startDate' on type 'Cycle'. Did you mean 'startsAt'?\",\"locations\":[{\"line\":1,\"column\":96}]},{\"message\":\"Cannot query field 'endDate' on type 'Cycle'. Did you mean 'endsAt'?\",\"locations\":[{\"line\":1,\"column\":106}]}]}"}

#### Step 4
Reasoning: Correct the field names: startsAt, endsAt.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"{ cycles(filter: {team: {id: {eq: \"539359f9-71ad-4fcc-a93b-e942900bad47\"}}}) { nodes { id name startsAt endsAt description } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"cycles\":{\"nodes\":[{\"id\":\"b16dee4a-ad3d-49ef-aa47-0787a6f115e4\",\"name\":\"Cycle 40\",\"startsAt\":\"2026-09-02T00:00:00\",\"endsAt\":\"2026-09-15T23:59:59\",\"description\":null}]}}}"}

#### Step 5
Reasoning: The only cycle listed ends on 2026-09-15. There's no cycle that ends on September 30. Let me try checking other statuses — maybe the cycles query is only returning active ones. Let me try querying without the team filter, or check if there's an archived flag. Let me look at all cycles.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"{ cycles { nodes { id name startsAt endsAt status { name } team { key } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'status' on type 'Cycle'.\",\"locations\":[{\"line\":1,\"column\":44}]}]}"}

#### Step 6
Reasoning: The team filter only returned Cycle 40 (September 2nd – September 15th). There's no cycle that ends on September 30th. Let me check all cycles across all teams without a filter and verify — but what matters is the Web team. To be thorough, I'll try querying cycles for all teams.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"{ cycles { nodes { id name startsAt endsAt team { key name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"cycles\":{\"nodes\":[{\"id\":\"42f20ce6-141f-4a84-870a-6e9f46a354a7\",\"name\":\"Cycle 41\",\"startsAt\":\"2026-09-16T00:00:00\",\"endsAt\":\"2026-09-30T23:59:59\",\"team\":{\"key\":\"PAY\",\"name\":\"Payments\"}},{\"id\":\"b16dee4a-ad3d-49ef-aa47-0787a6f115e4\",\"name\":\"Cycle 40\",\"startsAt\":\"2026-09-02T00:00:00\",\"endsAt\":\"2026-09-15T23:59:59\",\"team\":{\"key\":\"WEB\",\"name\":\"Web\"}},{\"id\":\"c921b0df-e2e7-4f2e-92a9-afdf59fd231f\",\"name\":\"Cycle 40\",\"startsAt\":\"2026-09-02T00:00:00\",\"endsAt\":\"2026-09-15T23:59:59\",\"team\":{\"key\":\"PAY\",\"name\":\"Payments\"}}]}}}"}

#### Step 7
Reasoning: The Web team's current cycle (cycle 40) ends on September 15, not September 30. There is no Web cycle that ends on September 30 — the cycle ending September 30 belongs to the Payments team (cycle 41).

The user asked to add "Scope locked" to the description of the Web team's current cycle that ends on September 30. That cycle doesn't exist for the Web team. The instructions say "if there isn't one, just tell me."

Therefore, I should tell them that no such cycle exists: the Web team's current cycle is cycle 40, which ends on September 15. The cycle ending September 30 is the Payments team's cycle 41. I should not unilaterally add the note to a different cycle or a different team's cycle.

I checked the Linear workspace — the Web team doesn't have a cycle ending September 30.

Here's what exists:

- **Web (WEB):** Cycle 40 — runs Sep 2–15, 2026 (already ended)
- **Payments (PAY):** Cycle 41 — runs Sep 16–30, 2026 (this is the one ending Sep 30, but it's Payments, not Web)

The Web team appears to have no cycle scheduled for the Sep 16–30 window. Per your instruction, I didn't add the note anywhere. If you'd like, I can either add "Scope locked" to Web's Cycle 40, or to Payments' Cycle 41 — just say the word.
Command: 
Response: null

## Final answer
I checked the Linear workspace — the Web team doesn't have a cycle ending September 30.

Here's what exists:

- **Web (WEB):** Cycle 40 — runs Sep 2–15, 2026 (already ended)
- **Payments (PAY):** Cycle 41 — runs Sep 16–30, 2026 (this is the one ending Sep 30, but it's Payments, not Web)

The Web team appears to have no cycle scheduled for the Sep 16–30 window. Per your instruction, I didn't add the note anywhere. If you'd like, I can either add "Scope locked" to Web's Cycle 40, or to Payments' Cycle 41 — just say the word.

## State diff
(no changes)

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": []}. Provisional outcome: presented?. Provisional exposed facts: [].

Give your verdict for this trial.