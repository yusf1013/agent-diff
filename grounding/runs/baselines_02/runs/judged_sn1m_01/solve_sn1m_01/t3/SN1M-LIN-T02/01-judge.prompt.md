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

# Trial of test `SN1M-LIN-T02` (linear)

Test form: cover (target and all decoys). Target present: yes.

## Request given to the solver
The invoice PDF ticket that's due Nov 6 and sized at 5 points: the client moved the deadline to Nov 20, can you update it?

## Candidates
### Reference r1 (what the request asks to act on); records live in `issues`
- TARGET `i-b13`: {"id": "i-b13", "identifier": "WEB-3", "title": "Invoice PDF layout refresh", "teamId": "tm-4a", "stateId": "tm-4a-st-1", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 3.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "estimate": 5, "dueDate": "2026-11-06"}
- DECOY `i-b11` (fact `A:Issue.estimate`, family F7): estimate 3, the estimate scale's neighbour of 5
  record: {"id": "i-b11", "identifier": "WEB-1", "title": "Invoice PDF layout refresh", "teamId": "tm-4a", "stateId": "tm-4a-st-1", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 1.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "estimate": 3, "dueDate": "2026-11-06"}
- DECOY `i-b14` (fact `A:Issue.estimate`, family F7): estimate 8, the scale's other neighbour of 5
  record: {"id": "i-b14", "identifier": "WEB-4", "title": "Invoice PDF layout refresh", "teamId": "tm-4a", "stateId": "tm-4a-st-1", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 4.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "estimate": 8, "dueDate": "2026-11-06"}
- DECOY `i-b12` (fact `A:Issue.dueDate`, family F0): due Nov 13, a week later
  record: {"id": "i-b12", "identifier": "WEB-2", "title": "Invoice PDF layout refresh", "teamId": "tm-4a", "stateId": "tm-4a-st-1", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 2.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "estimate": 5, "dueDate": "2026-11-13"}
- DECOY `i-b15` (fact `A:Issue.dueDate`, family F0): no due date
  record: {"id": "i-b15", "identifier": "WEB-5", "title": "Invoice PDF layout refresh", "teamId": "tm-4a", "stateId": "tm-4a-st-1", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 5.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "estimate": 5}

## Solver steps
Run status: completed; termination: done; steps: 7.

#### Step 1
Reasoning: The user wants to update a Linear ticket: a 5-point invoice PDF ticket with a November 6 deadline, moving the deadline to November 20. First, I should read Linear's SKILL.md.
Command: read {"path": "~/.openclaw-state/4f371a94963f471e/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: The skill describes how to use the Linear API. I need to find the ticket that's due Nov 6, sized at 5 points, and is related to an invoice PDF. I'll try querying Linear's GraphQL API.

First, I need to search for the issue. Let me query for issues that have a 5-point estimate and a due date of 2026-11-06.

I'll go with a search-based approach. Linear's GraphQL has an `issues(filter: ...)` query. First, let me try searching by a keyword like "invoice".
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ issues(filter: {search: {query: \"invoice pdf\"}, state: {type: {eq: null}}}) { nodes { id identifier title estimate dueAt state { name } points } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Field 'search' is not defined by type 'IssueFilter'.\",\"locations\":[{\"line\":1,\"column\":19}]},{\"message\":\"Cannot query field 'dueAt' on type 'Issue'. Did you mean 'dueDate' or 'team'?\",\"locations\":[{\"line\":1,\"column\":118}]},{\"message\":\"Cannot query field 'points' on type 'Issue'.\",\"locations\":[{\"line\":1,\"column\":139}]}]}"}

#### Step 3
Reasoning: The search filter is wrong. Let me check Linear's schema. The filter for issues uses `filter: { search: ... }`, but the search field might have a different name. In Linear's GraphQL, `IssueFilter` includes fields like `query`? Actually, Linear has a top-level `search` field, and the issue filter has `id`, `ids`, `number`, `title`, `state`, `team`, `workflowStates`, `assignee`, `estimate`, `dueDate` (I think the filter has `dueDate` with operators). Let me try the `title` filter containing "invoice" and the `estimate` filter eq 5.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ issues(filter: {title: {contains: \"invoice\"}, estimate: {eq: 5}}) { nodes { id identifier title estimate dueDate state { name } team { key } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[]}}}"}

#### Step 4
Reasoning: No results. Try a broader search.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ issues(first: 100, orderBy: updatedAt) { nodes { id identifier title estimate dueDate state { name } team { key } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"i-b11\",\"identifier\":\"WEB-1\",\"title\":\"Invoice PDF layout refresh\",\"estimate\":3.0,\"dueDate\":\"2026-11-06\",\"state\":{\"name\":\"Todo\"},\"team\":{\"key\":\"WEB\"}},{\"id\":\"i-b12\",\"identifier\":\"WEB-2\",\"title\":\"Invoice PDF layout refresh\",\"estimate\":5.0,\"dueDate\":\"2026-11-13\",\"state\":{\"name\":\"Todo\"},\"team\":{\"key\":\"WEB\"}},{\"id\":\"i-b13\",\"identifier\":\"WEB-3\",\"title\":\"Invoice PDF layout refresh\",\"estimate\":5.0,\"dueDate\":\"2026-11-06\",\"state\":{\"name\":\"Todo\"},\"team\":{\"key\":\"WEB\"}},{\"id\":\"i-b14\",\"identifier\":\"WEB-4\",\"title\":\"Invoice PDF layout refresh\",\"estimate\":8.0,\"dueDate\":\"2026-11-06\",\"state\":{\"name\":\"Todo\"},\"team\":{\"key\":\"WEB\"}},{\"id\":\"i-b15\",\"identifier\":\"WEB-5\",\"title\":\"Invoice PDF layout refresh\",\"estimate\":5.0,\"dueDate\":null,\"state\":{\"name\":\"Todo\"},\"team\":{\"key\":\"WEB\"}}]}}}"}

#### Step 5
Reasoning: There are multiple "Invoice PDF layout refresh" tickets. The matching one: due date November 6, 5 points → WEB-3 (id i-b13). WEB-2 has 5 points but its due date is November 13. WEB-1 has 3 points. WEB-4 has 8 points. WEB-5 has no due date.

So WEB-3 is the one. Update its dueDate to 2026-11-20.

Found the one: **WEB-3 "Invoice PDF layout refresh"** (5 points, due Nov 6). Updating the deadline to Nov 20:
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"mutation { issueUpdate(id: \"i-b13\", input: { dueDate: \"2026-11-20\" }) { success identifier title dueDate } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'identifier' on type 'IssuePayload'.\",\"locations\":[{\"line\":1,\"column\":81}]},{\"message\":\"Cannot query field 'title' on type 'IssuePayload'.\",\"locations\":[{\"line\":1,\"column\":92}]},{\"message\":\"Cannot query field 'dueDate' on type 'IssuePayload'.\",\"locations\":[{\"line\":1,\"column\":98}]}]}"}

#### Step 6
Reasoning: IssuePayload only has success and maybe issue. Let me try using the issue field.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"mutation { issueUpdate(id: \"i-b13\", input: { dueDate: \"2026-11-20\" }) { success issue { identifier title dueDate } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issueUpdate\":{\"success\":true,\"issue\":{\"identifier\":\"WEB-3\",\"title\":\"Invoice PDF layout refresh\",\"dueDate\":\"2026-11-20\"}}}}"}

#### Step 7
Reasoning: Done. Updated WEB-3 from November 6th to November 20th.

Done ✅

**WEB-3 — Invoice PDF layout refresh** (5 pts)
- Deadline: Nov 6 → **Nov 20, 2026**

Note: there were a couple of other invoice PDF tickets also due Nov 6 (WEB-1 at 3 pts, WEB-4 at 8 pts) — left those alone since you specified the 5-point one. Let me know if those need moving too.
Command: 
Response: null

## Final answer
Done ✅

**WEB-3 — Invoice PDF layout refresh** (5 pts)
- Deadline: Nov 6 → **Nov 20, 2026**

Note: there were a couple of other invoice PDF tickets also due Nov 6 (WEB-1 at 3 pts, WEB-4 at 8 pts) — left those alone since you specified the 5-point one. Let me know if those need moving too.

## State diff
- UPDATE issues `i-b13`: {"dueDate": ["2026-11-06", "2026-11-20"]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["i-b13"]}. Provisional outcome: correct. Provisional exposed facts: [].

Give your verdict for this trial.