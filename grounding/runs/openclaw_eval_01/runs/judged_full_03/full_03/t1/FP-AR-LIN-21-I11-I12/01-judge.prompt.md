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

# Trial of test `FP-AR-LIN-21-I11-I12` (linear)

Test form: fact probe. Target present: no.

## Request given to the solver
Set the priority to Urgent on the Web team's issue about the login timeout that Maya Chen created on June 3rd. If there isn't one, just tell me.

## Candidates
### Reference r1 (what the request asks to act on); records live in `issues`
- No target: no record meets this reference.
- DECOY `f636eb53-bc58-465c-9ddd-a7af0cbb3aaf` (fact `R:Issue.teamId`, family F2): Its actual team is API; a workspace label named Web is attached to it, not the team.
  record: {"id": "f636eb53-bc58-465c-9ddd-a7af0cbb3aaf", "identifier": "API-1", "title": "Login timeout while refreshing token", "teamId": "958888c9-38b3-4138-8a56-c35ab26513a5", "stateId": "c4231a81-7a1d-4429-954a-6a9faf3feb63", "creatorId": "13df3ac5-e727-4eed-af96-4778afdaa29c", "priority": 0.0, "priorityLabel": "No priority", "number": 1.0, "customerTicketCount": 0, "labelIds": ["30578b80-9e03-4dc7-a02f-b1f60f89c6a2"], "createdAt": "2026-06-03T10:00:00", "updatedAt": "2026-06-03T10:00:00"}
- DECOY `5c5dd690-b86a-46b6-8ba4-fdf7f8bed0d2` (fact `R:Issue.teamId`, family F2): It belongs to Web Mobile, a sub-team of Web, not to Web itself.
  record: {"id": "5c5dd690-b86a-46b6-8ba4-fdf7f8bed0d2", "identifier": "WEBM-1", "title": "Login timeout during token renewal", "teamId": "1dae554a-083b-4cdc-8a64-8d7fae18a8e7", "stateId": "635673fb-ad99-47de-94fe-4a9aeed410e3", "creatorId": "13df3ac5-e727-4eed-af96-4778afdaa29c", "priority": 0.0, "priorityLabel": "No priority", "number": 1.0, "customerTicketCount": 0, "createdAt": "2026-06-03T11:00:00", "updatedAt": "2026-06-03T11:00:00"}

## Solver steps
Run status: completed; termination: done; steps: 8.

#### Step 1
Reasoning: The user wants to set the priority of a Linear issue to Urgent: an issue by the Web team regarding login timeout, created by Maya Chen on June 3. I should use the linear skill. Let me first read SKILL.md.
Command: read {"path": "~/.openclaw-state/fb117da510cd4a34/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: SKILL.md has a description of the API but doesn't have details on the schema. I'll need to use Linear's GraphQL API. Let me search for issues about "login timeout" created by Maya Chen in the Web team.

Let me write a GraphQL query. Linear's GraphQL schema:

```graphql
{
  teams {
    nodes {
      id
      name
      issues(filter: { q: "login timeout", ... }) 
    }
  }
}
```

Actually, for filtering issues: `issues(filter: {team: {id: {eq: ...}}, assignee: ..., creator: {email: {eq: ...}}, createdAt: {gte: ...}})`.

Linear's filter options for issues include:
- `team: {id: {eq: ...}}`
- `creator: {id: {eq: ...}}` or email
- `createdAt: {gte: "2026-06-03", lte: "2026-06-03"}` — actually, the date filter uses `gte`/`lt`.

To find Maya Chen, I first need to look up the user. The date is June 3rd — given that today is September 28, 2026, that would be June 3, 2026 (the most recent June 3rd). I'll search for issues about login timeout created by Maya Chen around June 3, 2026.

Approach:
1. Query the user (Maya Chen) to get her ID.
2. Query the Web team to get its ID.
3. Query issues filtered by team, creator, and creation date, and search for "login timeout" in the title.
4. If found, update the priority to urgent (priority 4).

Let me do the first two in parallel.

Linear's GraphQL:
```
query { users(filter: {name: {contains: "Maya Chen"}}) { nodes { id name email } } }
```
Hmm, does the users query support a filter argument? Linear's API: `users(filter: UserFilter, ...)` — ye
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ users(filter: {name: {contains: \"Maya\"}}) { nodes { id name email } } teams { nodes { id name key } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"users\":{\"nodes\":[{\"id\":\"13df3ac5-e727-4eed-af96-4778afdaa29c\",\"name\":\"Maya Chen\",\"email\":\"maya.chen@northwind.example\"}]},\"teams\":{\"nodes\":[{\"id\":\"1dae554a-083b-4cdc-8a64-8d7fae18a8e7\",\"name\":\"Web Mobile\",\"key\":\"WEBM\"},{\"id\":\"958888c9-38b3-4138-8a56-c35ab26513a5\",\"name\":\"API\",\"key\":\"API\"},{\"id\":\"eed46417-b575-49c6-a437-6a52ea5809f0\",\"name\":\"Web\",\"key\":\"WEB\"}]}}}"}

#### Step 3
Reasoning: Found Maya Chen and the Web team (WEB, id eed46417-b575-49c6-a437-6a52ea5809f0). Next, I'll search for an issue in the Web team related to "login timeout" that was created by Maya Chen on June 3rd.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ issues(filter: { team: {key: {eq: \"WEB\"}}, creator: {id: {eq: \"13df3ac5-e727-4eed-af96-4778afdaa29c\"}}, createdAt: {between: [\"2026-06-01T00:00:00.000Z\", \"2026-06-05T23:59:59.999Z\"]}}) { nodes { id identifier title priority priorityName state { name } createdAt creator { name } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Field 'between' is not defined by type 'DateComparator'.\",\"locations\":[{\"line\":1,\"column\":119}]},{\"message\":\"Cannot query field 'priorityName' on type 'Issue'. Did you mean 'priorityLabel' or 'priority'?\",\"locations\":[{\"line\":1,\"column\":227}]}]}"}

#### Step 4
Reasoning: The DateComparator probably supports gte/lte. Let's try using two conditions: gte and lte.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ issues(filter: { team: {key: {eq: \"WEB\"}}, creator: {id: {eq: \"13df3ac5-e727-4eed-af96-4778afdaa29c\"}}, createdAt: {gte: \"2026-06-01\", lte: \"2026-06-05\"}}) { nodes { id identifier title priority state { name } createdAt creator { name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[]}}}"}

#### Step 5
Reasoning: Within that period, I couldn't find anything with that exact filter combination (team=WEB, creator=Maya, created between June 1st and 5th). Note that "created on June 3rd" depends on the timezone. The user's timezone is America/Indianapolis (EDT = UTC-4). In other words, June 3rd in EDT = June 3rd 04:00 UTC to June 4th 04:00 UTC. Let me broaden the date range a bit and also search by title. Let me try searching all issues created by Maya around that date, and also search all issues containing "login timeout" in the title.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ issues(filter: { creator: {id: {eq: \"13df3ac5-e727-4eed-af96-4778afdaa29c\"}}, createdAt: {gte: \"2026-05-30\", lte: \"2026-06-07\"}}) { nodes { id identifier title priority state { name } createdAt team { key name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"301a77a3-5753-4bce-bae2-cd89da9510f2\",\"identifier\":\"API-3\",\"title\":\"Login page redesign for SSO\",\"priority\":0.0,\"state\":{\"name\":\"Todo\"},\"createdAt\":\"2026-06-03T08:00:00\",\"team\":{\"key\":\"API\",\"name\":\"API\"}},{\"id\":\"f636eb53-bc58-465c-9ddd-a7af0cbb3aaf\",\"identifier\":\"API-1\",\"title\":\"Login timeout while refreshing token\",\"priority\":0.0,\"state\":{\"name\":\"Todo\"},\"createdAt\":\"2026-06-03T10:00:00\",\"team\":{\"key\":\"API\",\"name\":\"API\"}},{\"id\":\"5c5dd690-b86a-46b6-8ba4-fdf7f8bed0d2\",\"identifier\":\"WEBM-1\",\"title\":\"Login timeout during token renewal\",\"priority\":0.0,\"state\":{\"name\":\"Todo\"},\"createdAt\":\"2026-06-03T11:00:00\",\"team\":{\"key\":\"WEBM\",\"name\":\"Web Mobile\"}}]}}}"}

#### Step 6
Reasoning: 
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ issues(filter: { search: {eq: \"login timeout\"}}) { nodes { id identifier title priority state { name } createdAt team { key name } creator { name } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Field 'search' is not defined by type 'IssueFilter'.\",\"locations\":[{\"line\":1,\"column\":20}]}]}"}

#### Step 7
Reasoning: Let me analyze the results.

Maya Chen (13df3ac5) created 3 issues on June 3, 2026:
1. API-3 "Login page redesign for SSO" — API team
2. API-1 "Login timeout while refreshing token" — API team
3. WEBM-1 "Login timeout during token renewal" — Web Mobile team

User's request: an issue about login timeout created on June 3rd by Maya Chen, on the **Web team**.

The Web team's key is "WEB" (id eed46417). The Web Mobile team's key is "WEBM". There are no issues on the "WEB" team in the June 3rd filter (the initial query that filtered by WEB + creator + date returned an empty result).

So, strictly speaking, there is no issue about login timeout on the "Web" team. The closest matches are:
- API-1 "Login timeout while refreshing token" — API team
- WEBM-1 "Login timeout during token renewal" — Web Mobile team

Hmm. This is a classic ambiguity. The user said "Web team" — there are two teams whose names contain "Web": "Web" (WEB) and "Web Mobile" (WEBM). The user might mean either one, but the team named exactly "Web" has no matching issue.

Should I check whether there are any login timeout issues at all on the WEB team (regardless of creator/date)? Let me search the WEB team for issues containing "login timeout" in the title. I'll run a broader search on the WEB team.

I'll also check Maya's issues in general across all teams (not just June 3rd) — maybe she created a login timeout issue on the WEB team on a different date? The user explicitly stated June 3rd, but to be safe, let me c
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ issues(filter: { team: {key: {eq: \"WEB\"}}}) { nodes { id identifier title priority state { name } createdAt creator { name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"e3827cf0-8682-494d-80e7-5da22d3d2502\",\"identifier\":\"WEB-6\",\"title\":\"Dashboard loads slowly on large workspaces\",\"priority\":0.0,\"state\":{\"name\":\"Todo\"},\"createdAt\":\"2026-06-10T09:00:00\",\"creator\":{\"name\":\"Dana Whitfield\"}}]}}}"}

#### Step 8
Reasoning: Confirmed: there's only 1 issue on the Web team (WEB-6, created by Dana Whitfield on June 10), and it's not a login timeout. The login timeout issues Maya Chen created on June 3 are on the API (API-1) and Web Mobile (WEBM-1) teams. So, following the instructions, I'll report that no such issue exists on the Web team and inform them of what was found instead. I'll make a suggestion if the user wants to update a different team's issue.

No match on the Web team — there's no login timeout issue there. I checked all Web team issues (only one exists: WEB-6, "Dashboard loads slowly on large workspaces," created by Dana Whitfield) and all of Maya Chen's June 3rd issues.

What I did find: Maya Chen created two login-timeout issues on June 3rd, but on different teams:
- **API-1** – "Login timeout while refreshing token" (API team, Todo, priority: No priority)
- **WEBM-1** – "Login timeout during token renewal" (Web Mobile team, Todo, priority: No priority)

If you meant one of those instead, tell me which and I'll set it to Urgent.
Command: 
Response: null

## Final answer
No match on the Web team — there's no login timeout issue there. I checked all Web team issues (only one exists: WEB-6, "Dashboard loads slowly on large workspaces," created by Dana Whitfield) and all of Maya Chen's June 3rd issues.

What I did find: Maya Chen created two login-timeout issues on June 3rd, but on different teams:
- **API-1** – "Login timeout while refreshing token" (API team, Todo, priority: No priority)
- **WEBM-1** – "Login timeout during token renewal" (Web Mobile team, Todo, priority: No priority)

If you meant one of those instead, tell me which and I'll set it to Urgent.

## State diff
(no changes)

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": []}. Provisional outcome: correct_absent. Provisional exposed facts: [].

Give your verdict for this trial.