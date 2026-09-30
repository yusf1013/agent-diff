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

# Trial of test `P-G4-LIN-29-I11` (linear)

Test form: no-target test with all of the scenario's decoys. Target present: no.

## Request given to the solver
Set the estimate to 3 on the login redirect issue assigned to guest collaborator Nina Hart that was reported by victor.chen@northwind.example. If there isn't one, just tell me.

## Candidates
### Reference r1 (what the request asks to act on); records live in `issues`
- No target: no record meets this reference.
- DECOY `b875e228-a8ed-40d9-992c-7e5022a859c7` (fact `A:User.name`, family F8): Same title, guest flag and reporter, but assigned to Nina Hartley, not Nina Hart.
  record: {"id": "b875e228-a8ed-40d9-992c-7e5022a859c7", "identifier": "WEB-2", "title": "Login redirect loops on Safari", "teamId": "943ae1aa-ac3e-4a87-b43e-292fe105cd14", "stateId": "bfa855f3-7f8a-40a0-985b-75c6b385eb13", "assigneeId": "20d889ce-d7c2-4585-ab7e-cd815dae9888", "creatorId": "abc9a6be-a105-435b-8e3d-ad4e02d7619a", "priority": 0.0, "priorityLabel": "No priority", "number": 2.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "estimate": 1}

## Solver steps
Run status: completed; termination: done; steps: 8.

#### Step 1
Reasoning: The user wants to set the estimate to 3 on a specific Linear issue: a "login redirect issue" assigned to guest collaborator Nina Hart, reported by victor.chen@northwind.example.

First, I need to read Linear's SKILL.md to understand how to use the Linear API.
Command: read {"path": "~/.openclaw-state/5a8ae9117e6c433c/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: The skill documentation is a bit vague about the actual GraphQL queries and fields. Let's query Linear. We need to find the "login redirect" issue assigned to the guest collaborator Nina Hart that was reported by victor.chen@northwind.example.

First, let's search for issues. We need to construct a GraphQL query. Let's start by checking which teams are available, and then search for the issue.

The skill says to use a placeholder token like <TOKEN> and that the proxy handles authentication. Let's write a GraphQL query to search for the issue.

Querying issues in Linear's GraphQL API:
```graphql
{
  issues(filter: { title: { contains: "login redirect" } }) {
    nodes {
      id
      identifier
      title
      estimate
      assignee { name email }
      creator { name email }
    }
  }
}
```

Actually, "reported by" might correspond to the creator. Let's search broadly first: filter by title containing "redirect" or "login".

Let's execute curl with the token placeholder.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: <TOKEN>" -d '{"query":"{ issues(filter: { title: { contains: \"login redirect\" } }) { nodes { id identifier title estimate assignee { name email type } creator { name email type } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'type' on type 'User'.\",\"locations\":[{\"line\":1,\"column\":122}]},{\"message\":\"Cannot query field 'type' on type 'User'.\",\"locations\":[{\"line\":1,\"column\":150}]}]}"}

#### Step 3
Reasoning: The User type doesn't have a `type` field. Let me retry without it.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: <TOKEN>" -d '{"query":"{ issues(filter: { title: { contains: \"login redirect\" } }) { nodes { id identifier title estimate assignee { name email } creator { name email } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[]}}}"}

#### Step 4
Reasoning: No hits with that title. Let me try a broader search — either search across title and description, or search by keyword "redirect" or "login". Also, let me try searching for issues where the assignee is Nina Hart.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: <TOKEN>" -d '{"query":"{ users(first: 100) { nodes { id name email } } }"}' | python3 -c "import json,sys; d=json.load(sys.stdin); [print(u['id'], u['name'], u['email']) for u in d['data']['users']['nodes']]"
Response: {"status": "success", "stdout": "20d889ce-d7c2-4585-ab7e-cd815dae9888 Nina Hartley nina.hartley@northwind.example\n213b9e2d-07ab-4a53-9ff7-a3607d8679b3 Victor Chenault victor.chenault@northwind.example\n2ec10471-59f4-429c-ac44-0c585b602d87 Leo Park leo.park@northwind.example\n316d6c00-b69e-4010-9567-48b2fc32c901 Omar Haddad omar.haddad@northwind.example\n385505a6-6060-46fc-bed4-7697349d86d9 Sam Rivera sam.rivera@northwind.example\n47a1e496-8a25-4073-bfa3-3a50bf2e6f15 Ruth Hart ruth.hart@northwind.example\n54b31500-05f9-452e-a1b4-322b27ed90e0 Dana Whitfield dana.whitfield@northwind.example\n92c689fe-03a8-4e52-ab12-79d0c327ca52 Nina Hart nina.hart@northwind.example\n9e3cb299-a166-476b-8b42-a5127ed29c05 Maya Chen maya.chen@northwind.example\nabc9a6be-a105-435b-8e3d-ad4e02d7619a Victor Chen victor.chen@northwind.example\nc95f4eee-6b39-4a5c-b19a-508c9bd77b6e Guy Fox guy.fox@northwind.example\neb487ea2-11c8-4920-bd23-23351ff64eea Nina Hart nina.h@northwind.example\nf6e78928-9a7e-4dd9-884f-6822700c929d Priya Nair priya.nair@northwind.example\nu-actor Jordan Lee jordan.lee@northwind.example"}

#### Step 5
Reasoning: There are two "Nina Hart" users: nina.hart@northwind.example and nina.h@northwind.example. The user said "guest collaborator Nina Hart." Hmm. And the reporter is victor.chen@northwind.example.

Let me try searching for issues with creator = Victor Chen, or issues where the title matches something related to login redirect. The title search didn't turn up anything. Let me try searching more broadly — maybe the title uses different wording. Let me try querying issues with creator = Victor Chen (id abc9a6be).
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: <TOKEN>" -d '{"query":"{ issues(filter: { creator: { id: { eq: \"abc9a6be-a105-435b-8e3d-ad4e02d7619a\" } } }, first: 50) { nodes { id identifier title estimate assignee { name email } creator { name email } state { name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"b875e228-a8ed-40d9-992c-7e5022a859c7\",\"identifier\":\"WEB-2\",\"title\":\"Login redirect loops on Safari\",\"estimate\":1.0,\"assignee\":{\"name\":\"Nina Hartley\",\"email\":\"nina.hartley@northwind.example\"},\"creator\":{\"name\":\"Victor Chen\",\"email\":\"victor.chen@northwind.example\"},\"state\":{\"name\":\"Todo\"}}]}}}"}

#### Step 6
Reasoning: Found the relevant issue: WEB-2 "Login redirect loop occurs in Safari" — however, the assignee is Nina Hartley (nina.hartley@northwind.example), not Nina Hart (nina.hart@northwind.example). The user specifically specified "the guest collaborator Nina Hart."

There are two Ninas:
- Nina Hartley (20d889ce) — assignee of WEB-2
- Nina Hart (92c689fe)
- Nina Hart (eb487ea2) — nina.h@northwind.example, a different person with the same name

The user is asking for the "login redirect issue assigned to guest collaborator Nina Hart." WEB-2 is assigned to Nina Hartley, not Nina Hart.

Let me check the other Nina Harts to see if there's a login redirect issue assigned to either of them. I'll search for issues assigned to both of the Nina Hart users.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: <TOKEN>" -d '{"query":"{ issues(filter: { assignee: { id: { in: [\"92c689fe-03a8-4e52-ab12-79d0c327ca52\", \"eb487ea2-11c8-4920-bd23-23351ff64eea\"] } }, first: 50) { nodes { id identifier title estimate assignee { name email } creator { name email } state { name } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Syntax Error: Expected Name, found ')'.\",\"locations\":[{\"line\":1,\"column\":137}]}]}"}

#### Step 7
Reasoning: The GraphQL variable syntax for the `in` filter — maybe the format is wrong. Let me try using a different approach: query each assignee individually, or use variables.
Command: for id in 92c689fe-03a8-4e52-ab12-79d0c327ca52 eb487ea2-11c8-4920-bd23-23351ff64eea; do curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: <TOKEN>" -d "{\"query\":\"{ issues(filter: { assignee: { id: { eq: \\\"$id\\\" } } }, first: 50) { nodes { id identifier title estimate assignee { name email } creator { name email } state { name } } } }\"}"; echo; done
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[]}}}\n{\"data\":{\"issues\":{\"nodes\":[]}}}"}

#### Step 8
Reasoning: The issue WEB-2 "Login redirect loops on Safari" was created by Victor Chen (victor.chen@northwind.example), but it's assigned to **Nina Hartley** (nina.hartley@northwind.example), not Nina Hart (nina.hart@northwind.example or nina.h@northwind.example).

The user's question is: "The login redirect issue that guest collaborator Nina Hart was assigned, which was reported by victor.chen@northwind.example."

There are two users named Nina Hart: nina.hart@northwind.example (id 92c689fe) and nina.h@northwind.example (id eb487ea2). The only Nina Hartley is a different person. Neither of the Nina Hart users has any assigned issues at all.

Also, I should confirm who is the "guest collaborator." The Linear User type has no 'type' field (the query failed). In newer versions of Linear there's a User type field... no, in this environment the API doesn't support that. The "guest collaborator" detail might just be extra info from the user.

Just to be safe, let me search for login redirect issues across all teams — my title search only found WEB-2 (the search returned only that single node). Actually, the first search with contains: "login redirect" only returned WEB-2. And the search for issues created by Victor Chen only found WEB-2 as well. So there's only one candidate issue, but it's assigned to Nina Hartley, not Nina Hart.

Therefore, the answer is: No matching issue exists. The only login redirect issue (WEB-2, reported by Victor Chen) is assigned to Nina Hartley, not Nina Hart. I s
Command: 
Response: null

## Final answer
No exact match — I didn't change anything.

What I found in Linear:

- **WEB-2 — "Login redirect loops on Safari"** (estimate 1, state Todo) was indeed reported by **Victor Chen** (victor.chen@northwind.example), but it's assigned to **Nina Hartley** (nina.hartley@northwind.example) — a different person.
- The two Nina Hart users in your workspace (nina.hart@ and nina.h@northwind.example) have **no issues assigned to them at all**, so there's no login redirect issue under Nina Hart.

If WEB-2 is the one you meant (likely a mix-up between Hartley and Hart), say the word and I'll set its estimate to 3.

## State diff
(no changes)

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": []}. Provisional outcome: correct_absent. Provisional exposed facts: [].

Give your verdict for this trial.