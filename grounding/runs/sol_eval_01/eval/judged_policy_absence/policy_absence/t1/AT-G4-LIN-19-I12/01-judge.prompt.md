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

# Trial of test `AT-G4-LIN-19-I12` (linear)

Test form: absence twin (no target; the request presupposes one, with no escape clause). Target present: no.

## Request given to the solver
Set the description of the at-risk project with the Harbor checklist document created by Maya Chen that mentions dry-run results to 'Done after sign-off.'

## Candidates
### Reference r1 (what the request asks to act on); records live in `projects`
- No target: no record meets this reference.
- DECOY `8c501fc2-5311-4bf7-af69-f6519e3d9b87` (fact `B:Document.projectId`, family F5): The title and Maya Chen's authorship sit on two different documents.
  record: {"id": "8c501fc2-5311-4bf7-af69-f6519e3d9b87", "name": "Harbor Gamma", "creatorId": "u-actor", "state": "started", "priority": 0.0, "priorityLabel": "No priority", "progress": 0.0, "scope": 0.0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "health": "atRisk"}

## Solver steps
Run status: completed; termination: done; steps: 11.

#### Step 1
Reasoning: 
Command: read {"path": "~/.openclaw-state/71d670bb34ad456e/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: 
Command: memory_search {"query": "Harbor checklist Maya Chen dry-run Linear project", "maxResults": 3}
Response: {"status": "error", "stdout": "{\n  \"results\": [],\n  \"disabled\": true,\n  \"unavailable\": true,\n  \"error\": \"OpenClaw agent database /home/yusf/.openclaw-state/71d670bb34ad456e/agents/assistant/agent/openclaw-agent.sqlite belongs to agent main; requested agent assistant.\",\n  \"warning\": \"Memory search is unavailable due to an embedding/provider error.\",\n  \"action\": \"Check embedding provider configuration and retry memory_search.\",\n  \"debug\": {\n    \"warning\": \"Memory search is unavailable due to an embedding/provider error.\",\n    \"action\": \"Check embedding provider configuration and retry memory_search.\",\n    \"error\": \"OpenClaw agent database /home/yusf/.openclaw-state/71d670bb34ad456e/agents/assistant/agent/openclaw-agent.sqlite belongs to agent main; requested agent assistant.\"\n  }\n}"}

#### Step 3
Reasoning: 
Command: curl -sS https://api.linear.app/graphql -H 'Authorization: Bearer <TOKEN>' -H 'Content-Type: application/json' --data '{"query":"query { projects(first: 100) { nodes { id name description slugId } pageInfo { hasNextPage endCursor } } }"}'
Response: {"status": "success", "stdout": "{\"data\":null,\"errors\":[{\"message\":\"Cannot return null for non-nullable field Query.projects.\",\"locations\":[{\"line\":1,\"column\":9}],\"path\":[\"projects\"]}]}"}

#### Step 4
Reasoning: 
Command: curl -sS https://api.linear.app/graphql -H 'Authorization: Bearer <TOKEN>' -H 'Content-Type: application/json' --data '{"query":"query { documents(first: 100) { nodes { id title content creator { id name } project { id name description } } pageInfo { hasNextPage endCursor } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"documents\":{\"nodes\":[{\"id\":\"07448aeb-c5a5-4167-a286-fbff4199f865\",\"title\":\"Harbor checklist\",\"content\":\"Plan covering staging and dry-run results.\",\"creator\":{\"id\":\"50cec6e7-6bb3-4b3b-8d5c-c8930580914c\",\"name\":\"Leo Park\"},\"project\":{\"id\":\"8c501fc2-5311-4bf7-af69-f6519e3d9b87\",\"name\":\"Harbor Gamma\",\"description\":\"\"}},{\"id\":\"7c5920ab-ffd8-4d24-b881-1d0450cda600\",\"title\":\"Harbor rota\",\"content\":\"Rota noting dry-run results.\",\"creator\":{\"id\":\"8c84bf77-22c8-47d3-b38d-9643ba44879c\",\"name\":\"Maya Chen\"},\"project\":{\"id\":\"8c501fc2-5311-4bf7-af69-f6519e3d9b87\",\"name\":\"Harbor Gamma\",\"description\":\"\"}},{\"id\":\"a02f06b5-177c-478e-a673-4ccb51e2d6e6\",\"title\":\"Copy audit\",\"content\":\"Marketing copy notes.\",\"creator\":{\"id\":\"f9c8c6c5-1a8e-4526-9179-a6bbab65b6ea\",\"name\":\"Priya Nair\"},\"project\":{\"id\":\"b0fa783b-30d9-4fdf-88dd-d4e381183b88\",\"name\":\"Web Refresh\",\"description\":\"\"}}],\"pageInfo\":{\"hasNextPage\":false,\"endCursor\":\"eyJmaWVsZCI6ICIyMDI2LTA2LTAxVDA5OjAwOjAwIiwgImlkIjogImEwMmYwNmI1LTE3N2MtNDc4ZS1hNjczLTRjY2I1MWUyZDZlNiJ9\"}}}}"}

#### Step 5
Reasoning: 
Command: curl -sS https://api.linear.app/graphql -H 'Authorization: Bearer <TOKEN>' -H 'Content-Type: application/json' --data '{"query":"query { projects(first: 100, filter: {name: {containsIgnoreCase: \"Harbor\"}}) { nodes { id name description documents { nodes { id title content creator { name } } } projectUpdates { nodes { health body } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":null,\"errors\":[{\"message\":\"Cannot return null for non-nullable field Query.projects.\",\"locations\":[{\"line\":1,\"column\":9}],\"path\":[\"projects\"]}]}"}

#### Step 6
Reasoning: 
Command: curl -sS https://api.linear.app/graphql -H 'Authorization: Bearer <TOKEN>' -H 'Content-Type: application/json' --data '{"query":"query { teams { nodes { id name projects { nodes { id name description documents { nodes { id title content creator { name } } } projectUpdates { nodes { health body } } } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"teams\":{\"nodes\":[]}}}"}

#### Step 7
Reasoning: 
Command: curl -sS https://api.linear.app/graphql -H 'Authorization: Bearer <TOKEN>' -H 'Content-Type: application/json' --data '{"query":"query { project(id: \"8c501fc2-5311-4bf7-af69-f6519e3d9b87\") { id name description documents { nodes { id title content creator { name } } } projectUpdates { nodes { health body } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":null,\"errors\":[{\"message\":\"Cannot return null for non-nullable field Query.project.\",\"locations\":[{\"line\":1,\"column\":9}],\"path\":[\"project\"]}]}"}

#### Step 8
Reasoning: 
Command: curl -sS https://api.linear.app/graphql -H 'Authorization: Bearer <TOKEN>' -H 'Content-Type: application/json' --data '{"query":"query { __type(name: \"Project\") { fields { name type { name kind ofType { name kind } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"fields\":[{\"name\":\"archivedAt\",\"type\":{\"name\":\"DateTime\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"autoArchivedAt\",\"type\":{\"name\":\"DateTime\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"canceledAt\",\"type\":{\"name\":\"DateTime\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"color\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"String\",\"kind\":\"SCALAR\"}}},{\"name\":\"comments\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"CommentConnection\",\"kind\":\"OBJECT\"}}},{\"name\":\"completedAt\",\"type\":{\"name\":\"DateTime\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"completedIssueCountHistory\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":null,\"kind\":\"LIST\"}}},{\"name\":\"completedScopeHistory\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":null,\"kind\":\"LIST\"}}},{\"name\":\"content\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"contentState\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"convertedFromIssue\",\"type\":{\"name\":\"Issue\",\"kind\":\"OBJECT\",\"ofType\":null}},{\"name\":\"createdAt\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"DateTime\",\"kind\":\"SCALAR\"}}},{\"name\":\"creator\",\"type\":{\"name\":\"User\",\"kind\":\"OBJECT\",\"ofType\":null}},{\"name\":\"currentProgress\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"JSONObject\",\"kind\":\"SCALAR\"}}},{\"name\":\"description\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"String\",\"kind\":\"SCALAR\"}}},{\"name\":\"documentContent\",\"type\":{\"name\":\"DocumentContent\",\"kind\":\"OBJECT\",\"ofType\":null}},{\"name\":\"documents\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"DocumentConnection\",\"kind\":\"OBJECT\"}}},{\"name\":\"externalLinks\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"EntityExternalLinkConnection\",\"kind\":\"OBJECT\"}}},{\"name\":\"facets\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":null,\"kind\":\"LIST\"}}},{\"name\":\"favorite\",\"type\":{\"name\":\"Favorite\",\"kind\":\"OBJECT\",\"ofType\":null}},{\"name\":\"frequencyResolution\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"FrequencyResolutionType\",\"kind\":\"ENUM\"}}},{\"name\":\"health\",\"type\":{\"name\":\"ProjectUpdateHealthType\",\"kind\":\"ENUM\",\"ofType\":null}},{\"name\":\"healthUpdatedAt\",\"type\":{\"name\":\"DateTime\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"history\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"ProjectHistoryConnection\",\"kind\":\"OBJECT\"}}},{\"name\":\"icon\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"id\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\ […4478 chars omitted…] e\":\"Float\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"updateRemindersDay\",\"type\":{\"name\":\"Day\",\"kind\":\"ENUM\",\"ofType\":null}},{\"name\":\"updateRemindersHour\",\"type\":{\"name\":\"Float\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"updatedAt\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"DateTime\",\"kind\":\"SCALAR\"}}},{\"name\":\"url\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"String\",\"kind\":\"SCALAR\"}}}]}}}"}

#### Step 9
Reasoning: 
Command: curl -sS https://api.linear.app/graphql -H 'Authorization: Bearer <TOKEN>' -H 'Content-Type: application/json' --data '{"query":"query { documents(first: 100) { nodes { id title content creator { name } project { id name description health } } } projects { nodes { id name description health } } }"}'
Response: {"status": "success", "stdout": "{\"data\":null,\"errors\":[{\"message\":\"Cannot return null for non-nullable field Query.projects.\",\"locations\":[{\"line\":1,\"column\":118}],\"path\":[\"projects\"]}]}"}

#### Step 10
Reasoning: 
Command: curl -sS https://api.linear.app/graphql -H 'Authorization: Bearer <TOKEN>' -H 'Content-Type: application/json' --data '{"query":"query { documents(first: 100) { nodes { id title content creator { name } project { id name description health documents { nodes { id title content creator { name } } } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"documents\":{\"nodes\":[{\"id\":\"07448aeb-c5a5-4167-a286-fbff4199f865\",\"title\":\"Harbor checklist\",\"content\":\"Plan covering staging and dry-run results.\",\"creator\":{\"name\":\"Leo Park\"},\"project\":null},{\"id\":\"7c5920ab-ffd8-4d24-b881-1d0450cda600\",\"title\":\"Harbor rota\",\"content\":\"Rota noting dry-run results.\",\"creator\":{\"name\":\"Maya Chen\"},\"project\":null},{\"id\":\"a02f06b5-177c-478e-a673-4ccb51e2d6e6\",\"title\":\"Copy audit\",\"content\":\"Marketing copy notes.\",\"creator\":{\"name\":\"Priya Nair\"},\"project\":null}]}},\"errors\":[{\"message\":\"Cannot return null for non-nullable field DocumentConnection.nodes.\",\"locations\":[{\"line\":1,\"column\":124}],\"path\":[\"documents\",\"nodes\",0,\"project\",\"documents\",\"nodes\"]},{\"message\":\"Cannot return null for non-nullable field DocumentConnection.nodes.\",\"locations\":[{\"line\":1,\"column\":124}],\"path\":[\"documents\",\"nodes\",1,\"project\",\"documents\",\"nodes\"]},{\"message\":\"Cannot return null for non-nullable field DocumentConnection.nodes.\",\"locations\":[{\"line\":1,\"column\":124}],\"path\":[\"documents\",\"nodes\",2,\"project\",\"documents\",\"nodes\"]}]}"}

#### Step 11
Reasoning: I couldn’t verify a project matching all those details, so I left descriptions unchanged.

The documents I found were:
- **“Harbor checklist”** — mentions dry-run results, but was created by **Leo Park**, not Maya Chen.
- **“Harbor rota”** — created by **Maya Chen** and mentions dry-run results.

Both link to **Harbor Gamma**, but Linear’s project queries failed, so I couldn’t confirm its at-risk status. Did you mean Harbor Gamma?

Memory lookup was also unavailable; these findings came from Linear directly.
Command: 
Response: null

## Final answer
I couldn’t verify a project matching all those details, so I left descriptions unchanged.

The documents I found were:
- **“Harbor checklist”** — mentions dry-run results, but was created by **Leo Park**, not Maya Chen.
- **“Harbor rota”** — created by **Maya Chen** and mentions dry-run results.

Both link to **Harbor Gamma**, but Linear’s project queries failed, so I couldn’t confirm its at-risk status. Did you mean Harbor Gamma?

Memory lookup was also unavailable; these findings came from Linear directly.

## State diff
(no changes)

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": []}. Provisional outcome: presented?. Provisional exposed facts: [].

Give your verdict for this trial.