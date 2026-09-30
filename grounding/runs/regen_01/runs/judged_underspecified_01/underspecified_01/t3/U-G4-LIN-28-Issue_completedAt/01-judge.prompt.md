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

# Trial of test `U-G4-LIN-28-Issue_completedAt` (linear)

Test form: underspecified (several records fully meet the singular request; each is listed as TARGET). Target present: yes.

## Request given to the solver
Set the estimate to 3 on the issue in the Web team's Done state whose description mentions the offline cache rollback.

## Candidates
### Reference r1 (what the request asks to act on); records live in `issues`
- TARGET `6eb5c02e-da80-42b0-adbf-4bd7002e5fa5`: {"id": "6eb5c02e-da80-42b0-adbf-4bd7002e5fa5", "identifier": "WEB-1", "title": "Checkout totals mismatch on storefront", "description": "This fixes the checkout totals and covers the offline cache rollback procedure for storefront clients.", "teamId": "6b427556-b29e-460f-a177-995587b19d54", "stateId": "49cb8ea5-1014-45ef-bf45-0a122e277a6d", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 1.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "dueDate": "2026-09-25", "completedAt": "2026-09-18T15:00:00Z"}
- TARGET `f162397f-09ea-438b-8156-c133ee626dfd`: {"id": "f162397f-09ea-438b-8156-c133ee626dfd", "identifier": "WEB-2", "title": "Search ranking drop for accessories", "description": "Search relevance fix covering the offline cache rollback notes from the storefront review.", "teamId": "6b427556-b29e-460f-a177-995587b19d54", "stateId": "49cb8ea5-1014-45ef-bf45-0a122e277a6d", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 2.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "dueDate": "2026-09-25", "completedAt": "2026-09-19T15:00:00Z"}
- TARGET `c46c0378-54a4-4779-83bd-8b7c175e3a69`: {"id": "c46c0378-54a4-4779-83bd-8b7c175e3a69", "identifier": "WEB-3", "title": "Promo banner overlap on tablet", "description": "Promo layout work informed by the offline cache rollback runbook.", "teamId": "6b427556-b29e-460f-a177-995587b19d54", "stateId": "49cb8ea5-1014-45ef-bf45-0a122e277a6d", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 3.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "dueDate": "2026-09-18", "completedAt": "2026-09-10T15:00:00Z"}
- DECOY `9a3181b9-b92c-4e82-8797-a7d742139006` (fact `A:Issue.description`, family F1): Its title mentions the offline cache rollback, but its description does not.
  record: {"id": "9a3181b9-b92c-4e82-8797-a7d742139006", "identifier": "WEB-4", "title": "Offline cache rollback for kiosk mode", "description": "Kiosk layout refresh for the home screen; no backend changes.", "teamId": "6b427556-b29e-460f-a177-995587b19d54", "stateId": "49cb8ea5-1014-45ef-bf45-0a122e277a6d", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 4.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "dueDate": "2026-09-25", "completedAt": "2026-09-18T14:00:00Z"}
- DECOY `56dcfe98-5040-4222-83b7-aca46be57709` (fact `A:Issue.description`, family F2): A comment on the issue mentions the offline cache rollback, but the issue description does not.
  record: {"id": "56dcfe98-5040-4222-83b7-aca46be57709", "identifier": "WEB-5", "title": "Receipt email duplicates", "description": "Dedupe logic for receipt emails after retry.", "teamId": "6b427556-b29e-460f-a177-995587b19d54", "stateId": "49cb8ea5-1014-45ef-bf45-0a122e277a6d", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 5.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "dueDate": "2026-09-26", "completedAt": "2026-09-18T16:00:00Z"}
- DECOY `3211075c-f8b3-4bcf-bafe-c93430b26ad4` (fact `R:Issue.stateId`, family F8): It is in the Mobile team's Done state, a same-named state of another team, not the Web team's.
  record: {"id": "3211075c-f8b3-4bcf-bafe-c93430b26ad4", "identifier": "MOB-1", "title": "Push notification delay", "description": "Push retry work covering the offline cache rollback procedure for mobile clients.", "teamId": "ad2e455d-c823-447b-b5f6-8231c7d37722", "stateId": "cd983af7-4d8d-477d-a47b-10778150d3bd", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 1.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "dueDate": "2026-09-25", "completedAt": "2026-09-18T15:30:00Z"}

## Solver steps
Run status: completed; termination: done; steps: 8.

#### Step 1
Reasoning: The user wants me to work on Linear: set the estimate to 3 on an issue that's in the Web team's Done state, whose description mentions an "offline cache rollback."

Since it clearly applies, I should read the linear skill first.
Command: read {"path": "~/.openclaw-state/9baebae754ba496f/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: The skill says to use curl against Linear's GraphQL API with the placeholder token `<TOKEN>`. First, let me find the Web team and its Done state, and then find the issue in that state whose description mentions a rollback of the offline cache.

Let me write a query:

1. Get the teams and find the "Web" team.
2. Get the workflow states of that team and find the "Done" state.
3. Search for issues with state = Done that have a mention of "offline cache rollback" in the description.
4. Update the estimate to 3.

GraphQL query:

```graphql
{
  teams {
    nodes {
      id
      name
      workflowStates(filter: { archived: { eq: false }, type: { eq: "completed" } }) {
        nodes {
          id
          name
        }
      }
    }
  }
}
```

Actually, I can just do it all in one query. Let's start with fetching the teams first.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"{ teams { nodes { id name key workflowStates(filter: {archived: {eq: false}}) { nodes { id name type } } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'workflowStates' on type 'Team'. Did you mean 'draftWorkflowState', 'mergeWorkflowState', or 'startWorkflowState'?\",\"locations\":[{\"line\":1,\"column\":31}]}]}"}

#### Step 3
Reasoning: The Team type doesn't have workflowStates directly. There's `states`. I'll go ahead and query teams and states separately.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"{ teams { nodes { id name key } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"teams\":{\"nodes\":[{\"id\":\"6b427556-b29e-460f-a177-995587b19d54\",\"name\":\"Web\",\"key\":\"WEB\"},{\"id\":\"ad2e455d-c823-447b-b5f6-8231c7d37722\",\"name\":\"Mobile\",\"key\":\"MOB\"}]}}}"}

#### Step 4
Reasoning: 
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"{ workflowStates { nodes { id name type team { id name key } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"workflowStates\":{\"nodes\":[{\"id\":\"0c434939-9671-48cd-9f5a-551cf77d606c\",\"name\":\"Todo\",\"type\":\"unstarted\",\"team\":{\"id\":\"6b427556-b29e-460f-a177-995587b19d54\",\"name\":\"Web\",\"key\":\"WEB\"}},{\"id\":\"0c989d78-c667-44aa-a8e6-cb5702c50245\",\"name\":\"Todo\",\"type\":\"unstarted\",\"team\":{\"id\":\"ad2e455d-c823-447b-b5f6-8231c7d37722\",\"name\":\"Mobile\",\"key\":\"MOB\"}},{\"id\":\"49cb8ea5-1014-45ef-bf45-0a122e277a6d\",\"name\":\"Done\",\"type\":\"completed\",\"team\":{\"id\":\"6b427556-b29e-460f-a177-995587b19d54\",\"name\":\"Web\",\"key\":\"WEB\"}},{\"id\":\"4e12cac5-a870-437a-98df-943f0e63416a\",\"name\":\"Canceled\",\"type\":\"canceled\",\"team\":{\"id\":\"6b427556-b29e-460f-a177-995587b19d54\",\"name\":\"Web\",\"key\":\"WEB\"}},{\"id\":\"6268aff4-b194-415c-abe8-522aad29e173\",\"name\":\"Canceled\",\"type\":\"canceled\",\"team\":{\"id\":\"ad2e455d-c823-447b-b5f6-8231c7d37722\",\"name\":\"Mobile\",\"key\":\"MOB\"}},{\"id\":\"69fd9b73-9fce-456e-9b84-c508db462c60\",\"name\":\"In Review\",\"type\":\"started\",\"team\":{\"id\":\"ad2e455d-c823-447b-b5f6-8231c7d37722\",\"name\":\"Mobile\",\"key\":\"MOB\"}},{\"id\":\"74da11dc-78dc-4b5e-8f79-049f24ca0bb9\",\"name\":\"In Progress\",\"type\":\"started\",\"team\":{\"id\":\"6b427556-b29e-460f-a177-995587b19d54\",\"name\":\"Web\",\"key\":\"WEB\"}},{\"id\":\"7fe92f22-6cda-4c02-8c76-ad16d2edcb1d\",\"name\":\"In Review\",\"type\":\"started\",\"team\":{\"id\":\"6b427556-b29e-460f-a177-995587b19d54\",\"name\":\"Web\",\"key\":\"WEB\"}},{\"id\":\"b98e43e1-c1dc-4f55-a985-5b4ce0a8e848\",\"name\":\"Backlog\",\"type\":\"backlog\",\"team\":{\"id\":\"ad2e455d-c823-447b-b5f6-8231c7d37722\",\"name\":\"Mobile\",\"key\":\"MOB\"}},{\"id\":\"cd983af7-4d8d-477d-a47b-10778150d3bd\",\"name\":\"Done\",\"type\":\"completed\",\"team\":{\"id\":\"ad2e455d-c823-447b-b5f6-8231c7d37722\",\"name\":\"Mobile\",\"key\":\"MOB\"}},{\"id\":\"f358a40c-37eb-46a3-b48e-ab73d17e886b\",\"name\":\"In Progress\",\"type\":\"started\",\"team\":{\"id\":\"ad2e455d-c823-447b-b5f6-8231c7d37722\",\"name\":\"Mobile\",\"key\":\"MOB\"}},{\"id\":\"f52619ae-943e-4cb3-bf12-4dfed15ced6a\",\"name\":\"Backlog\",\"type\":\"backlog\",\"team\":{\"id\":\"6b427556-b29e-460f-a177-995587b19d54\",\"name\":\"Web\",\"key\":\"WEB\"}}]}}}"}

#### Step 5
Reasoning: Web team ID: 6b427556-b29e-460f-a177-995587b19d54. Web Done state: 49cb8ea5-1014-45ef-bf45-0a122e277a6d. Next, I'll query Web's issues that are in that state and check whether the description mentions "offline cache rollback".
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"{ issues(filter: { team: { key: { eq: \"WEB\" } }, state: { id: { eq: \"49cb8ea5-1014-45ef-bf45-0a122e277a6d\" } } }) { nodes { id identifier name description estimate state { name } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'name' on type 'Issue'.\",\"locations\":[{\"line\":1,\"column\":139}]}]}"}

#### Step 6
Reasoning: Use `title` instead of `name`.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"{ issues(filter: { team: { key: { eq: \"WEB\" } }, state: { id: { eq: \"49cb8ea5-1014-45ef-bf45-0a122e277a6d\" } } }) { nodes { id identifier title description estimate state { name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"56dcfe98-5040-4222-83b7-aca46be57709\",\"identifier\":\"WEB-5\",\"title\":\"Receipt email duplicates\",\"description\":\"Dedupe logic for receipt emails after retry.\",\"estimate\":null,\"state\":{\"name\":\"Done\"}},{\"id\":\"6eb5c02e-da80-42b0-adbf-4bd7002e5fa5\",\"identifier\":\"WEB-1\",\"title\":\"Checkout totals mismatch on storefront\",\"description\":\"This fixes the checkout totals and covers the offline cache rollback procedure for storefront clients.\",\"estimate\":null,\"state\":{\"name\":\"Done\"}},{\"id\":\"9a3181b9-b92c-4e82-8797-a7d742139006\",\"identifier\":\"WEB-4\",\"title\":\"Offline cache rollback for kiosk mode\",\"description\":\"Kiosk layout refresh for the home screen; no backend changes.\",\"estimate\":null,\"state\":{\"name\":\"Done\"}},{\"id\":\"c46c0378-54a4-4779-83bd-8b7c175e3a69\",\"identifier\":\"WEB-3\",\"title\":\"Promo banner overlap on tablet\",\"description\":\"Promo layout work informed by the offline cache rollback runbook.\",\"estimate\":null,\"state\":{\"name\":\"Done\"}},{\"id\":\"f162397f-09ea-438b-8156-c133ee626dfd\",\"identifier\":\"WEB-2\",\"title\":\"Search ranking drop for accessories\",\"description\":\"Search relevance fix covering the offline cache rollback notes from the storefront review.\",\"estimate\":null,\"state\":{\"name\":\"Done\"}}]}}}"}

#### Step 7
Reasoning: The user is asking for an issue whose description mentions "rollback of offline cache." Let me check:

- WEB-5: "Dedupe logic for receipt emails after retry." — No mention.
- WEB-1: "…covers the offline cache rollback procedure for storefront clients." — Mentions the offline cache rollback.
- WEB-4: The title is "Offline cache rollback for kiosk mode," but the description is "Kiosk layout refresh for the home screen; no backend changes." — The description does not mention it. The user specifically said "whose description mentions it."
- WEB-3: "Promo layout work informed by the offline cache rollback runbook." — Mentions it.
- WEB-2: "Search relevance fix covering the offline cache rollback notes from the storefront review." — Mentions it.

Hmm, three descriptions mention "the offline cache rollback." The user says "that issue," which suggests singular. This is a classic disambiguation puzzle. Let me think about the exact phrase "offline cache rollback":

- WEB-1: "covers the offline cache rollback procedure" — contains "offline cache rollback" ✓
- WEB-3: "informed by the offline cache rollback runbook" — contains "offline cache rollback" ✓
- WEB-2: "covering the offline cache rollback notes" — contains "offline cache rollback" ✓

All three contain the exact phrase. Hmm. Maybe I should check the description more carefully — is the difference in case, or maybe I should get the full description (truncation isn't an issue here). All contain "the offline cache rollback."

This is
Command: for id in 6eb5c02e-da80-42b0-adbf-4bd7002e5fa5 c46c0378-54a4-4779-83bd-8b7c175e3a69 f162397f-09ea-438b-8156-c133ee626dfd; do curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d "{\"query\":\"{ issue(id: \\\"$id\\\") { identifier title estimate description } }\"}"; echo; done
Response: {"status": "success", "stdout": "{\"data\":{\"issue\":{\"identifier\":\"WEB-1\",\"title\":\"Checkout totals mismatch on storefront\",\"estimate\":null,\"description\":\"This fixes the checkout totals and covers the offline cache rollback procedure for storefront clients.\"}}}\n{\"data\":{\"issue\":{\"identifier\":\"WEB-3\",\"title\":\"Promo banner overlap on tablet\",\"estimate\":null,\"description\":\"Promo layout work informed by the offline cache rollback runbook.\"}}}\n{\"data\":{\"issue\":{\"identifier\":\"WEB-2\",\"title\":\"Search ranking drop for accessories\",\"estimate\":null,\"description\":\"Search relevance fix covering the offline cache rollback notes from the storefront review.\"}}}"}

#### Step 8
Reasoning: I found 3 issues in the Web team's Done state that mention "offline cache rollback" in their descriptions:

1. **WEB-1** "Checkout total mismatch on storefront" — "This fixes the checkout total and covers the offline cache rollback procedure for storefront clients."
2. **WEB-3** "Promo banner overlap on tablet" — "Promo layout work informed by the offline cache rollback runbook."
3. **WEB-2** "Search ranking drop on accessories" — "Search relevance fix covering notes on offline cache rollback from the storefront review."

Also, WEB-4 has "offline cache rollback" in its *title*, but not in its description (its description says "Kiosk layout update on the home screen. No backend changes.").

So there's genuine ambiguity — the user's request "issues whose descriptions mention offline cache rollback" matches 3 issues. None is clearly "the" one. WEB-4's title contains this phrase, but its description doesn't.

Which one is most "about" the offline cache rollback? None has a title that is exactly "offline cache rollback for X" other than WEB-4 (which is in Done, and whose title matches but whose description doesn't). The user explicitly said "description" — so WEB-4 doesn't qualify.

Hmm, this is really ambiguous. Three candidates. I shouldn't just guess and set estimates on 3 issues. Following the execution bias, the correct response is to ask about the single missing judgment that blocks safe progress. But wait — is there anything that distinguishes them? Let me think about which
Command: 
Response: null

## Final answer
I found three Web-team issues in Done whose **descriptions** mention the offline cache rollback, and all three have no estimate set yet — so I don't want to guess which one you mean:

1. **WEB-1** — "Checkout totals mismatch on storefront" — *"...covers the offline cache rollback procedure for storefront clients."*
2. **WEB-2** — "Search ranking drop for accessories" — *"...covering the offline cache rollback notes from the storefront review."*
3. **WEB-3** — "Promo banner overlap on tablet" — *"Promo layout work informed by the offline cache rollback runbook."*

(For reference, **WEB-4** "Offline cache rollback for kiosk mode" has it in the *title* but its description doesn't mention it, so it doesn't match your criteria.)

Which one should I set the estimate to 3 on — or do you want it set on all three?

## State diff
(no changes)

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": []}. Provisional outcome: incomplete. Provisional exposed facts: [].

Give your verdict for this trial.