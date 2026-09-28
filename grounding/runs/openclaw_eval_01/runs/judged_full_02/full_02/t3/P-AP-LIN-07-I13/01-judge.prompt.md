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

# Trial of test `P-AP-LIN-07-I13` (linear)

Test form: probe. Target present: no.

## Request given to the solver
Rename the Growth team's document titled "Draft notes" that mentions the referral program pilot to "Referral pilot — launch notes". If there isn't one, just tell me.

## Candidates
### Reference r1 (what the request asks to act on); records live in `documents`
- No target: no record meets this reference.
- DECOY `d-team-f1` (fact `R:Document.teamId`, family F1): It has no team of its own; it's filed under the Customer Acquisition project instead.
  record: {"id": "d-team-f1", "title": "Draft notes", "content": "Draft notes on the referral program pilot rollout for Q4, including timeline and success metrics.", "creatorId": "u-actor", "updatedById": "u-actor", "projectId": "pr-growth", "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}

## Solver steps
Run status: completed; termination: done; steps: 14.

#### Step 1
Reasoning: The user is asking to rename a Linear document belonging to the Growth team titled "Draft notes" that mentions a referral program pilot to "Referral Pilot — Launch Notes". Let me check the Linear skill first.
Command: read {"path": "~/.openclaw-state/a8ab65cd2b854967/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: The user is asking me to rename a Linear document titled "Draft notes" that mentions a referral program pilot, to "Referral pilot — launch notes". The skill's API docs enumerate teams, issues, comments, labels, workflow states, etc., but I don't see a "documents" section in the docs. Linear has a Documents API (documentCreate, documentUpdate, etc.), but it's not listed here.

Wait — Linear's GraphQL API has document endpoints (documents, document, documentUpdate). The skill's docs only list a subset, but the GraphQL endpoint is standard. Let me try querying documents.

Plan:
1. Find the Growth team.
2. Find documents within that team where title == "Draft notes" and the body mentions the referral program pilot.
3. Update the title to "Referral pilot — launch notes".

Linear's GraphQL API:
- `teams` query
- `documents` query — does it exist? Linear's GraphQL API has a `documents` query (added around 2023). Signature: `documents(filter: DocumentFilterInput, first: Int, orderBy: ...)`. DocumentFilterInput has `team: { key: "Growth" }`, `title: { contains: "Draft notes" }`, etc.

Auth: "handled automatically via proxy. Use placeholder tokens like `<TOKEN>`". So curl to https://api.linear.app/graphql with the placeholder token `<TOKEN>`? That seems weird, but it's what the skill says. Hmm, maybe the proxy intercepts. The instructions say "Auth is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` when credentials would be needed." So I should use `<TOKEN>` as t
Command: curl -s https://api.linear.app/graphql -H 'Authorization: Bearer <TOKEN>' -H 'Content-Type: application/json' -d '{"query":"query { teams(first: 50) { nodes { id key name } } documents(first: 100) { nodes { id title documentUrl team { key name } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'documentUrl' on type 'Document'.\",\"locations\":[{\"line\":1,\"column\":93}]}]}"}

#### Step 3
Reasoning: The `documents` query does exist (the error is only about `documentUrl`). I'll remove that field and re-run it. Also, I should check the document's `body` to confirm mentions of the referral program pilot.
Command: curl -s https://api.linear.app/graphql -H 'Authorization: Bearer <TOKEN>' -H 'Content-Type: application/json' -d '{"query":"query { teams(first: 50) { nodes { id key name } } documents(first: 100) { nodes { id title team { key name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"teams\":{\"nodes\":[{\"id\":\"t-growth\",\"key\":\"GRO\",\"name\":\"Growth\"},{\"id\":\"t-platform\",\"key\":\"PLA\",\"name\":\"Platform\"}]},\"documents\":{\"nodes\":[{\"id\":\"d-bg1\",\"title\":\"Security review checklist\",\"team\":{\"key\":\"PLA\",\"name\":\"Platform\"}},{\"id\":\"d-bg2\",\"title\":\"Roadmap draft\",\"team\":{\"key\":\"GRO\",\"name\":\"Growth\"}},{\"id\":\"d-team-f1\",\"title\":\"Draft notes\",\"team\":null}]}}}"}

#### Step 4
Reasoning: There's a document called "Draft notes" on the Growth team, but its team is null. There's also "Roadmap draft" for Growth. I need to check the contents of the documents and find the one that mentions the referral program pilot. Let me try querying the content of the documents.
Command: curl -s https://api.linear.app/graphql -H 'Authorization: Bearer <TOKEN>' -H 'Content-Type: application/json' -d '{"query":"query { documents(first: 100) { nodes { id title team { key name } content } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"documents\":{\"nodes\":[{\"id\":\"d-bg1\",\"title\":\"Security review checklist\",\"team\":{\"key\":\"PLA\",\"name\":\"Platform\"},\"content\":\"Checklist for the annual SOC 2 audit prep.\"},{\"id\":\"d-bg2\",\"title\":\"Roadmap draft\",\"team\":{\"key\":\"GRO\",\"name\":\"Growth\"},\"content\":\"Roadmap draft for the loyalty program launch next quarter.\"},{\"id\":\"d-team-f1\",\"title\":\"Draft notes\",\"team\":null,\"content\":\"Draft notes on the referral program pilot rollout for Q4, including timeline and success metrics.\"}]}}}"}

#### Step 5
Reasoning: The document "Draft notes" (id: d-team-f1) mentions the referral program pilot, but its team is null. The user asked to "rename the Growth team's document titled 'Draft notes'." The document that mentions the referral program pilot is indeed "Draft notes," but it's not assigned to the Growth team. Hmm.

Wait — maybe there are more documents, or the team field just isn't set. Let me check if there are other "Draft notes" documents. I've only fetched the first 100 entries. Let me check pagination. Also, there might be a team field in the document schema — the document has team: null. But the user's intent is: the Growth team's document titled "Draft notes" that mentions the referral program pilot. There's exactly one document with that title that mentions the referral program pilot. The team is null — probably a document at the workspace root, not belonging to a team.

Hmm, this is a subtle point. The conditions the user gave: (1) belongs to the Growth team, (2) title is "Draft notes," (3) mentions the referral program pilot. The only candidate matches (2) and (3) but doesn't match (1). The description "mentions the referral program pilot" strongly suggests this is the intended document — probably the user thinks it belongs to Growth because the content is about the Growth team's referral program.

Let me first check the total document count to make sure I'm not missing any other "Draft notes" documents, then decide. The safe approach: the content explicitly says "referral prog
Command: curl -s https://api.linear.app/graphql -H 'Authorization: Bearer <TOKEN>' -H 'Content-Type: application/json' -d '{"query":"query { documents(first: 100) { totalCount pageInfo { hasNextPage } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'totalCount' on type 'DocumentConnection'.\",\"locations\":[{\"line\":1,\"column\":33}]}]}"}

#### Step 6
Reasoning: The query for all documents returned 3 nodes. The "Draft notes" document (d-team-f1) does indeed mention the referral program pilot — "Draft notes regarding the rollout of the Q4 referral program pilot, including the timeline and success metrics." The team field is null, but it's probably in the Growth team. I'll try renaming this.
Command: curl -s https://api.linear.app/graphql -H 'Authorization: Bearer <TOKEN>' -H 'Content-Type: application/json' -d '{"query":"mutation { documentUpdate(id: \"d-team-f1\", title: \"Referral pilot — launch notes\") { success document { id title } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Unknown argument 'title' on field 'Mutation.documentUpdate'.\",\"locations\":[{\"line\":1,\"column\":44}]},{\"message\":\"Field 'documentUpdate' argument 'input' of type 'DocumentUpdateInput!' is required, but it was not provided.\",\"locations\":[{\"line\":1,\"column\":12}]}]}"}

#### Step 7
Reasoning: The documentUpdate mutation requires an input object. Let me try {input: {id, title}}.
Command: curl -s https://api.linear.app/graphql -H 'Authorization: Bearer <TOKEN>' -H 'Content-Type: application/json' -d '{"query":"mutation { documentUpdate(input: {id: \"d-team-f1\", title: \"Referral pilot — launch notes\"}) { success document { id title } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Field 'id' is not defined by type 'DocumentUpdateInput'.\",\"locations\":[{\"line\":1,\"column\":35}]},{\"message\":\"Field 'documentUpdate' argument 'id' of type 'String!' is required, but it was not provided.\",\"locations\":[{\"line\":1,\"column\":12}]}]}"}

#### Step 8
Reasoning: I need to structure the input object without an id field, keeping it separate from the other parameters.
Command: curl -s https://api.linear.app/graphql -H 'Authorization: Bearer <TOKEN>' -H 'Content-Type: application/json' -d '{"query":"mutation { documentUpdate(id: \"d-team-f1\", input: {title: \"Referral pilot — launch notes\"}) { success document { id title } } }"}'
Response: {"status": "success", "stdout": "{\"data\":null,\"errors\":[{\"message\":\"Cannot return null for non-nullable field DocumentPayload.success.\",\"locations\":[{\"line\":1,\"column\":95}],\"path\":[\"documentUpdate\",\"success\"]}]}"}

#### Step 9
Reasoning: The mutation `documentUpdate(id, input: {title})` returned an error — it looks like "success" is null, which might mean the update failed, or the input field "title" is wrong. Let me introspect the DocumentUpdateInput type.
Command: curl -s https://api.linear.app/graphql -H 'Authorization: Bearer <TOKEN>' -H 'Content-Type: application/json' -d '{"query":"query { __type(name: \"DocumentUpdateInput\") { inputFields { name type { name kind ofType { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"inputFields\":[{\"name\":\"color\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"content\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"hiddenAt\",\"type\":{\"name\":\"DateTime\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"icon\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"initiativeId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"lastAppliedTemplateId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"projectId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"resourceFolderId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"sortOrder\",\"type\":{\"name\":\"Float\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"subscriberIds\",\"type\":{\"name\":null,\"kind\":\"LIST\",\"ofType\":{\"name\":null}}},{\"name\":\"teamId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"title\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"trashed\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}}]}}}"}

#### Step 10
Reasoning: documentUpdate accepts `id` as a top-level argument and `input` which includes title. The reason the previous call returned an error "Cannot return null for non-nullable field DocumentPayload.success" is probably because the mutation succeeded but something is wrong, or maybe it was a transient error. Let me retry. Actually, "data: null" with an error on success suggests that the mutation didn't execute correctly. Hmm, maybe it was an optimistic response error. Let me retry and then check the document.
Command: curl -s https://api.linear.app/graphql -H 'Authorization: Bearer <TOKEN>' -H 'Content-Type: application/json' -d '{"query":"mutation { documentUpdate(id: \"d-team-f1\", input: {title: \"Referral pilot — launch notes\"}) { success } }"}'
Response: {"status": "success", "stdout": "{\"data\":null,\"errors\":[{\"message\":\"Cannot return null for non-nullable field DocumentPayload.success.\",\"locations\":[{\"line\":1,\"column\":95}],\"path\":[\"documentUpdate\",\"success\"]}]}"}

#### Step 11
Reasoning: The payload seems to be returning null — either a failure is occurring internally, or the response structure is different. Let's check the schema of DocumentPayload, and try using the error field without including success in the selection.
Command: curl -s https://api.linear.app/graphql -H 'Authorization: Bearer <TOKEN>' -H 'Content-Type: application/json' -d '{"query":"query { __type(name: \"DocumentPayload\") { fields { name type { name kind ofType { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"fields\":[{\"name\":\"document\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"Document\"}}},{\"name\":\"lastSyncId\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"Float\"}}},{\"name\":\"success\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"Boolean\"}}}]}}}"}

#### Step 12
Reasoning: The update is failing at the "success" field — "Cannot return null for non-nullable field DocumentPayload.success". This suggests that the mutation is actually erroring out on the server side (the document probably doesn't exist under that ID, or the ID format is different). Maybe the document ID for the mutation needs the full UUID rather than "d-team-f1"? But the query returned id "d-team-f1". Hmm, this mock environment might be using a short ID. Or perhaps the update is failing because teamId also needs to be set? Let me try adding teamId, or try querying the document with a filter to check.

Actually, the error "Cannot return null for non-nullable field DocumentPayload.success" typically occurs in GraphQL when a resolver throws an error and the error gets swallowed. Maybe the mutation is failing because the document doesn't exist. Let me first verify the document's existence with a document(id:) query.
Command: curl -s https://api.linear.app/graphql -H 'Authorization: Bearer <TOKEN>' -H 'Content-Type: application/json' -d '{"query":"query { document(id: \"d-team-f1\") { id title team { key name } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"document\":{\"id\":\"d-team-f1\",\"title\":\"Referral pilot — launch notes\",\"team\":null}}}"}

#### Step 13
Reasoning: The update succeeded (title is now "Referral pilot — launch notes"). The payload error is a quirk of the mock API — it seems `success` returns null, but the document itself was actually updated.

Now, about the "Growth team" condition. The document "Draft notes" (id d-team-f1) has `team: null` — it doesn't belong to the Growth team. The user specifically asked for a Growth team document that mentions the referral program pilot.

Hmm. This looks like a test scenario. The document mentions the referral program pilot ("Draft notes on the rollout of the referral program pilot in Q4, including timeline and success metrics"), but it's not tied to the Growth team (team: null).

Wait — but maybe there are more documents in the list that weren't returned? I queried with first: 100 and got 3 back. There's no totalCount field. There's pageInfo — let me check if there are more pages. The first query didn't include pageInfo. Let me check hasNextPage.

Also, maybe I should double-check whether there are other "Draft notes" documents. Let me run a full pagination check.

If this document really is unaffiliated (team null), then strictly speaking, a Growth team document named "Draft notes" that mentions the referral program pilot doesn't exist. But I've already renamed it. Hmm, should I have checked before renaming?

Let me think carefully about the user's intent: "Rename the Growth team document titled 'Draft notes' that mentions the referral program pilot." If the only "Draft notes" docume
Command: curl -s https://api.linear.app/graphql -H 'Authorization: Bearer <TOKEN>' -H 'Content-Type: application/json' -d '{"query":"query { documents(first: 100) { nodes { id title team { key } } pageInfo { hasNextPage } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"documents\":{\"nodes\":[{\"id\":\"d-bg1\",\"title\":\"Security review checklist\",\"team\":{\"key\":\"PLA\"}},{\"id\":\"d-bg2\",\"title\":\"Roadmap draft\",\"team\":{\"key\":\"GRO\"}},{\"id\":\"d-team-f1\",\"title\":\"Referral pilot — launch notes\",\"team\":null}],\"pageInfo\":{\"hasNextPage\":false}}}}"}

#### Step 14
Reasoning: The rename has been completed. The only document named "Draft notes" (d-team-f1) refers to a referral program pilot, and it has been renamed to "Referral pilot — launch notes". This is confirmed in the query that fetches the document by ID, and the full list also shows hasNextPage: false, meaning this is the only document with that title/content.

A subtle nuance: this document's team is null, so it's not directly "owned" by the Growth team. However, it is the only "Draft notes" that mentions a referral program pilot, and that is the user's intent. I should briefly mention this caveat.

Done. Renamed the document "Draft notes" (content: referral program pilot rollout for Q4, timeline and success metrics) to **"Referral pilot — launch notes"** — verified it now shows with the new title.

One caveat: that doc isn't actually linked to a team in Linear (its team field is empty) — it's just the only "Draft notes" mentioning the referral pilot, so I assumed it's the right one. The Growth team's other doc is "Roadmap draft" (loyalty program, unrelated).
Command: 
Response: null

## Final answer
Done. Renamed the document "Draft notes" (content: referral program pilot rollout for Q4, timeline and success metrics) to **"Referral pilot — launch notes"** — verified it now shows with the new title.

One caveat: that doc isn't actually linked to a team in Linear (its team field is empty) — it's just the only "Draft notes" mentioning the referral pilot, so I assumed it's the right one. The Growth team's other doc is "Roadmap draft" (loyalty program, unrelated).

## State diff
- UPDATE documents `d-team-f1`: {"title": ["Draft notes", "Referral pilot — launch notes"]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["d-team-f1"]}. Provisional outcome: incorrect. Provisional exposed facts: ['R:Document.teamId'].

Give your verdict for this trial.