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

# Trial of test `FP-G4-LIN-34-I13-I14` (linear)

Test form: fact probe. Target present: no.

## Request given to the solver
Rename the '3D Secure Fallback Plan' document in the Payments team whose content covers adding 3D Secure fallback to '3D Secure Fallback Plan — Final'. If there isn't one, just tell me.

## Candidates
### Reference r1 (what the request asks to act on); records live in `documents`
- No target: no record meets this reference.
- DECOY `00e89b1a-c164-4763-b5cb-47f2f08e4da1` (fact `R:Document.teamId`, family F1): Same title and content, but it belongs to the project named Payments instead of the Payments team.
  record: {"id": "00e89b1a-c164-4763-b5cb-47f2f08e4da1", "title": "3D Secure Fallback Plan", "content": "This plan covers adding 3D Secure fallback for failed checkout payments, with the retry sequence and exemption flags.", "creatorId": "u-actor", "updatedById": "u-actor", "projectId": "73246b52-7de3-4005-8277-2eda0b7213af", "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `bf8b0925-9da9-4052-b0ab-a8d4a6a67d36` (fact `R:Document.teamId`, family F8): Same title and content, but it belongs to the Payouts team, not the Payments team.
  record: {"id": "bf8b0925-9da9-4052-b0ab-a8d4a6a67d36", "title": "3D Secure Fallback Plan", "content": "This plan covers adding 3D Secure fallback for failed checkout payments, with the retry sequence and exemption flags.", "creatorId": "u-actor", "updatedById": "u-actor", "teamId": "03d397ac-0ab1-4006-bd56-e1d8ddce957e", "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}

## Solver steps
Run status: completed; termination: done; steps: 7.

#### Step 1
Reasoning: I need to investigate this further. Let me check the details.

The user wants to rename a Linear document in the Payments team. First, let me read the Linear skill.
Command: read {"path": "~/.openclaw-state/be14c39d48834660/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: The user is asking about renaming a "document" in Linear. Linear has "documents" (like Notion-style pages), but the Linear GraphQL API in this skill only mentions issues, comments, labels, states, teams, users, relations. There's no "documents" query in the API docs provided by the skill.

Let me think about what Linear offers. Linear has "Documents" (linear.app documents), and the GraphQL API has a `documents` query and `documentUpdate` mutation, plus `projectInitiatives`... Actually, the Linear API does have `documents`, `document` queries, `documentCreate`, `documentUpdate`, `documentArchive`, and `documentCommentCreate` mutations. But this skill's API docs list is limited to the items enumerated — no documents.

Hmm, but the skill's API docs might be partial. Let me try querying the Linear GraphQL API directly. The skill says authentication is handled automatically via a proxy, and to use a placeholder token like `<TOKEN>`.

Let me try:

```bash
curl -s https://api.linear.app/graphql -X POST -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"..."}'
```

First, I need to find the Payments team, then find a document named "3D Secure Fallback Plan" whose content is about adding a 3D Secure fallback.

The Linear GraphQL API supports:
- `teams` query: `{ teams { nodes { id name key } } }`
- `documents(filter: { team: { slug: "PAY" } })`? Actually, the filter for the `documents` query is a DocumentFilter where team is `{ id: ... }` or `{ slug: 
Command: curl -s https://api.linear.app/graphql -X POST -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"{ teams(first:100){ nodes { id name key } } documents(first:100){ nodes { id title url team { id name key } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"teams\":{\"nodes\":[{\"id\":\"03d397ac-0ab1-4006-bd56-e1d8ddce957e\",\"name\":\"Payouts\",\"key\":\"POT\"},{\"id\":\"2c616976-4b35-4d8f-940c-782d0f46c51f\",\"name\":\"Payments\",\"key\":\"PAY\"}]},\"documents\":{\"nodes\":[{\"id\":\"00e89b1a-c164-4763-b5cb-47f2f08e4da1\",\"title\":\"3D Secure Fallback Plan\",\"url\":\"https://linear.app/northwind/document/00e89b1a-c164-4763-b5cb-47f2f08e4da1\",\"team\":null},{\"id\":\"539c6bbb-8d39-4826-9bc6-f69f5cb55f00\",\"title\":\"Mobile Release Notes\",\"url\":\"https://linear.app/northwind/document/539c6bbb-8d39-4826-9bc6-f69f5cb55f00\",\"team\":{\"id\":\"03d397ac-0ab1-4006-bd56-e1d8ddce957e\",\"name\":\"Payouts\",\"key\":\"POT\"}},{\"id\":\"bf8b0925-9da9-4052-b0ab-a8d4a6a67d36\",\"title\":\"3D Secure Fallback Plan\",\"url\":\"https://linear.app/northwind/document/bf8b0925-9da9-4052-b0ab-a8d4a6a67d36\",\"team\":{\"id\":\"03d397ac-0ab1-4006-bd56-e1d8ddce957e\",\"name\":\"Payouts\",\"key\":\"POT\"}}]}}}"}

#### Step 3
Reasoning: There are 2 documents titled "3D Secure Fallback Plan": one is unaffiliated (team: null), and the other belongs to the Payouts (POT) team. Neither is under the Payments (PAY) team. However, the user's condition is "one whose content covers the addition of 3D Secure fallback" — so I need to check the content. Let me fetch the content of both documents and verify which one is the Payments one. The first document is team: null — this might be a document shared across multiple teams. Let me fetch the content.

Found two docs with that name but none are clearly on the Payments team. Let me check their content to confirm.
Command: curl -s https://api.linear.app/graphql -X POST -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"{ a: document(id: \"00e89b1a-c164-4763-b5cb-47f2f08e4da1\") { title content } b: document(id: \"bf8b0925-9da9-4052-b0ab-a8d4a6a67d36\") { title content } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"a\":{\"title\":\"3D Secure Fallback Plan\",\"content\":\"This plan covers adding 3D Secure fallback for failed checkout payments, with the retry sequence and exemption flags.\"},\"b\":{\"title\":\"3D Secure Fallback Plan\",\"content\":\"This plan covers adding 3D Secure fallback for failed checkout payments, with the retry sequence and exemption flags.\"}}}"}

#### Step 4
Reasoning: Both documents have the same title and same content. One (00e89b1a) has team: null — unassigned. The other (bf8b0925) belongs to the Payouts team (POT), not Payments (PAY).

The user asked for documents "within the Payments team." Neither document belongs to the Payments team. The one without a team (team: null) is not part of the Payments team — it's unassigned.

Hmm, should the document with team: null be considered as belonging to Payments? No — team is null, meaning unassigned. The user specifically said "within the Payments team." I should report that it doesn't exist.

But wait — maybe I should double-check whether there are more documents (pagination, first:100 should be enough). Also, there might be archived documents. Should I check with includeArchived? The Linear API's documents query might support an archiveState filter. Let me try including archived documents just to be safe.

Let me try: documents(first:100, archiveState: ARCHIVED) — actually, the filter syntax in the Linear API is `documents(first:100, archiveState: ARCHIVED)`. Let me try it.

I've confirmed both have identical content, but neither is in the Payments team—one is unassigned and the other is in Payouts. I'll check archived documents to be thorough before drawing a conclusion.
Command: curl -s https://api.linear.app/graphql -X POST -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"{ documents(first:100, archiveState: ARCHIVED){ nodes { id title url team { name key } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Unknown argument 'archiveState' on field 'Query.documents'.\",\"locations\":[{\"line\":1,\"column\":24}]}]}"}

#### Step 5
Reasoning: I need to check if there's an includeArchived argument or similar in the schema, so I'm introspecting the arguments available for the documents field.
Command: curl -s https://api.linear.app/graphql -X POST -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"{ __type(name: \"Query\") { fields { name args { name type { name kind ofType { name kind } } } } } }"}' | python3 -c "
import json,sys
d=json.load(sys.stdin)
for f in d['data']['__type']['fields']:
    if f['name'] in ('documents','document'):
        print(f['name'], [a['name'] for a in f['args']])
"
Response: {"status": "success", "stdout": "document ['id']\ndocuments ['after', 'before', 'filter', 'first', 'includeArchived', 'last', 'orderBy']"}

#### Step 6
Reasoning: The `documents` query has an `includeArchived` argument. Let's also check archived documents.
Command: curl -s https://api.linear.app/graphql -X POST -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"{ documents(first:100, includeArchived: true){ nodes { id title url archivedAt team { name key } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"documents\":{\"nodes\":[{\"id\":\"00e89b1a-c164-4763-b5cb-47f2f08e4da1\",\"title\":\"3D Secure Fallback Plan\",\"url\":\"https://linear.app/northwind/document/00e89b1a-c164-4763-b5cb-47f2f08e4da1\",\"archivedAt\":null,\"team\":null},{\"id\":\"539c6bbb-8d39-4826-9bc6-f69f5cb55f00\",\"title\":\"Mobile Release Notes\",\"url\":\"https://linear.app/northwind/document/539c6bbb-8d39-4826-9bc6-f69f5cb55f00\",\"archivedAt\":null,\"team\":{\"name\":\"Payouts\",\"key\":\"POT\"}},{\"id\":\"bf8b0925-9da9-4052-b0ab-a8d4a6a67d36\",\"title\":\"3D Secure Fallback Plan\",\"url\":\"https://linear.app/northwind/document/bf8b0925-9da9-4052-b0ab-a8d4a6a67d36\",\"archivedAt\":null,\"team\":{\"name\":\"Payouts\",\"key\":\"POT\"}}]}}}"}

#### Step 7
Reasoning: Including archived ones, I've checked all the documents in the workspace. There are exactly 3 documents in total, none of which belong to the Payments team:

1. "3D Secure Fallback Plan" — team: null (not assigned to a team)
2. "Mobile Release Notes" — Payouts
3. "3D Secure Fallback Plan" — Payouts

Both of the "3D Secure Fallback Plan" documents have the same content ("This plan covers adding 3D Secure fallback to failed checkout payments, including retry sequences and exemption flags."), and both match the content description. However, neither is on the Payments team (PAY) — one is unassigned and the other is on the Payouts (POT) team.

The user's request was "If it doesn't exist, just tell me" — the condition "within the Payments team" is not satisfied. I shouldn't rename either one (since it's ambiguous which one was intended, and renaming the Payouts one would be the wrong target). The user explicitly said "if it doesn't exist, just tell me." Therefore, the correct action is to report and not rename.

I'll report this clearly and concisely.

I checked all documents in the workspace (including archived) and there's no '3D Secure Fallback Plan' in the **Payments (PAY)** team, so I didn't rename anything.

Here's what exists with that title and matching content (both say "adding 3D Secure fallback for failed checkout payments, with the retry sequence and exemption flags"):

- **3D Secure Fallback Plan** — *no team assigned* — https://linear.app/northwind/document/00e89b1a-c
Command: 
Response: null

## Final answer
I checked all documents in the workspace (including archived) and there's no '3D Secure Fallback Plan' in the **Payments (PAY)** team, so I didn't rename anything.

Here's what exists with that title and matching content (both say "adding 3D Secure fallback for failed checkout payments, with the retry sequence and exemption flags"):

- **3D Secure Fallback Plan** — *no team assigned* — https://linear.app/northwind/document/00e89b1a-c164-4763-b5cb-47f2f08e4da1
- **3D Secure Fallback Plan** — **Payouts (POT)** team — https://linear.app/northwind/document/bf8b0925-9da9-4052-b0ab-a8d4a6a67d36

If one of these is the one you meant (e.g., the unassigned one was supposed to live under Payments), tell me which and I'll rename it to '3D Secure Fallback Plan — Final'.

## State diff
(no changes)

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": []}. Provisional outcome: presented?. Provisional exposed facts: [].

Give your verdict for this trial.