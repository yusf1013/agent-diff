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

# Trial of test `SN1M-LIN-T06` (linear)

Test form: cover (target and all decoys). Target present: yes.

## Request given to the solver
Hand the "Update privacy policy copy" issue in the Lantern project over to Dana.

## Candidates
### Reference r1 (what the request asks to act on); records live in `issues`
- TARGET `i-g62`: {"id": "i-g62", "identifier": "WEB-2", "title": "Update privacy policy copy", "teamId": "tm-4a", "stateId": "tm-4a-st-1", "assigneeId": "u-maya", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 2.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "projectId": "pr-62"}
- DECOY `i-g61` (fact `R:Issue.projectId`, family F0): the same title in Harbor
  record: {"id": "i-g61", "identifier": "WEB-1", "title": "Update privacy policy copy", "teamId": "tm-4a", "stateId": "tm-4a-st-1", "assigneeId": "u-maya", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 1.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "projectId": "pr-61"}
- DECOY `i-g63` (fact `R:Issue.projectId`, family F0): the same title in no project
  record: {"id": "i-g63", "identifier": "WEB-3", "title": "Update privacy policy copy", "teamId": "tm-4a", "stateId": "tm-4a-st-1", "assigneeId": "u-maya", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 3.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `i-g64` (fact `A:Issue.title`, family F8): Lantern's Update terms of service copy
  record: {"id": "i-g64", "identifier": "WEB-4", "title": "Update terms of service copy", "teamId": "tm-4a", "stateId": "tm-4a-st-1", "assigneeId": "u-maya", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 4.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "projectId": "pr-62"}

## Solver steps
Run status: completed; termination: done; steps: 10.

#### Step 1
Reasoning: The user wants to assign the issue "Update privacy policy copy" in the Linear project "Lantern" to Dana. Since the Linear skill is applicable, I should first read its SKILL.md.
Command: read {"path": "~/.openclaw-state/b3690c57c4fb46e2/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: I need to search for the "Update privacy policy copy" issue in the Lantern project and reassign it to Dana. First, I'll query the issue and get Dana's user ID. I'll use the GraphQL API.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ project(name: \"Lantern\") { id name issues(filter: { title: { contains: \"Update privacy policy copy\" } }) { nodes { id identifier title assignee { id name email } } } } users(filter: { name: { contains: \"Dana\" } }) { nodes { id name email } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Unknown argument 'name' on field 'Query.project'.\",\"locations\":[{\"line\":1,\"column\":11}]},{\"message\":\"Field 'project' argument 'id' of type 'String!' is required, but it was not provided.\",\"locations\":[{\"line\":1,\"column\":3}]}]}"}

#### Step 3
Reasoning: I need to find the project by name first. Let me query projects.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ projects(filter: { name: { contains: \"Lantern\" } }) { nodes { id name url } } users(filter: { name: { contains: \"Dana\" } }) { nodes { id name email } } }"}'
Response: {"status": "success", "stdout": "{\"data\":null,\"errors\":[{\"message\":\"Cannot return null for non-nullable field Query.projects.\",\"locations\":[{\"line\":1,\"column\":3}],\"path\":[\"projects\"]}]}"}

#### Step 4
Reasoning: The projects query failed — probably an authentication issue, or the projects query needs a team scope. Let me try querying projects without a filter.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ projects { nodes { id name } } }"}'
Response: {"status": "success", "stdout": "{\"data\":null,\"errors\":[{\"message\":\"Cannot return null for non-nullable field Query.projects.\",\"locations\":[{\"line\":1,\"column\":3}],\"path\":[\"projects\"]}]}"}

#### Step 5
Reasoning: Hmm, the projects query is failing. It's possible that this API version doesn't have `projects`, or the proxy might be handling it in a different way. Let me try `teams` and `issues`.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ teams { nodes { id name } } }"}'; echo; curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ issues(filter: { title: { contains: \"privacy policy\" } }) { nodes { id identifier title project { id name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"teams\":{\"nodes\":[{\"id\":\"tm-4a\",\"name\":\"Web\"}]}}}\n{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"i-g61\",\"identifier\":\"WEB-1\",\"title\":\"Update privacy policy copy\",\"project\":{\"id\":\"pr-61\",\"name\":\"Harbor\"}},{\"id\":\"i-g62\",\"identifier\":\"WEB-2\",\"title\":\"Update privacy policy copy\",\"project\":{\"id\":\"pr-62\",\"name\":\"Lantern\"}},{\"id\":\"i-g63\",\"identifier\":\"WEB-3\",\"title\":\"Update privacy policy copy\",\"project\":null}]}}}"}

#### Step 6
Reasoning: The issue "Update Privacy Policy Wording" is within the Lantern project: id i-g62, identifier WEB-2.

Next, I'll find Dana. I need the user list to get Dana's user ID.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ users { nodes { id name email displayName } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"users\":{\"nodes\":[{\"id\":\"u-actor\",\"name\":\"Jordan Lee\",\"email\":\"jordan.lee@northwind.example\",\"displayName\":\"jordan\"},{\"id\":\"u-dana\",\"name\":\"Dana Whitfield\",\"email\":\"dana.whitfield@northwind.example\",\"displayName\":\"dana\"},{\"id\":\"u-leo\",\"name\":\"Leo Park\",\"email\":\"leo.park@northwind.example\",\"displayName\":\"leo\"},{\"id\":\"u-maya\",\"name\":\"Maya Chen\",\"email\":\"maya.chen@northwind.example\",\"displayName\":\"maya\"},{\"id\":\"u-omar\",\"name\":\"Omar Haddad\",\"email\":\"omar.haddad@northwind.example\",\"displayName\":\"omar\"},{\"id\":\"u-priya\",\"name\":\"Priya Nair\",\"email\":\"priya.nair@northwind.example\",\"displayName\":\"priya\"},{\"id\":\"u-sam\",\"name\":\"Sam Rivera\",\"email\":\"sam.rivera@northwind.example\",\"displayName\":\"sam\"}]}}}"}

#### Step 7
Reasoning: The Lantern project issue is i-g62 (WEB-2). Assign it to Dana Whitfield (u-dana).
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"mutation { issueUpdate(id: \"i-g62\", assigneeId: \"u-dana\") { id identifier title assignee { name } success } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Unknown argument 'assigneeId' on field 'Mutation.issueUpdate'.\",\"locations\":[{\"line\":1,\"column\":37}]},{\"message\":\"Cannot query field 'id' on type 'IssuePayload'.\",\"locations\":[{\"line\":1,\"column\":61}]},{\"message\":\"Cannot query field 'identifier' on type 'IssuePayload'.\",\"locations\":[{\"line\":1,\"column\":64}]},{\"message\":\"Cannot query field 'title' on type 'IssuePayload'.\",\"locations\":[{\"line\":1,\"column\":75}]},{\"message\":\"Cannot query field 'assignee' on type 'IssuePayload'.\",\"locations\":[{\"line\":1,\"column\":81}]},{\"message\":\"Field 'issueUpdate' argument 'input' of type 'IssueUpdateInput!' is required, but it was not provided.\",\"locations\":[{\"line\":1,\"column\":12}]}]}"}

#### Step 8
Reasoning: The skill says issueUpdate exists. The argument is "input" of type IssueUpdateInput!. Let me try it with input.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"mutation { issueUpdate(input: { id: \"i-g62\", assigneeId: \"u-dana\" }) { id identifier title assignee { id name } success } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Field 'id' is not defined by type 'IssueUpdateInput'.\",\"locations\":[{\"line\":1,\"column\":33}]},{\"message\":\"Cannot query field 'id' on type 'IssuePayload'.\",\"locations\":[{\"line\":1,\"column\":72}]},{\"message\":\"Cannot query field 'identifier' on type 'IssuePayload'.\",\"locations\":[{\"line\":1,\"column\":75}]},{\"message\":\"Cannot query field 'title' on type 'IssuePayload'.\",\"locations\":[{\"line\":1,\"column\":86}]},{\"message\":\"Cannot query field 'assignee' on type 'IssuePayload'.\",\"locations\":[{\"line\":1,\"column\":92}]},{\"message\":\"Field 'issueUpdate' argument 'id' of type 'String!' is required, but it was not provided.\",\"locations\":[{\"line\":1,\"column\":12}]}]}"}

#### Step 9
Reasoning: The mutation signature is `issueUpdate(id: String!, input: IssueUpdateInput!)`. Let's try it with this.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"mutation { issueUpdate(id: \"i-g62\", input: { assigneeId: \"u-dana\" }) { success issue { id identifier title assignee { id name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issueUpdate\":{\"success\":true,\"issue\":{\"id\":\"i-g62\",\"identifier\":\"WEB-2\",\"title\":\"Update privacy policy copy\",\"assignee\":{\"id\":\"u-dana\",\"name\":\"Dana Whitfield\"}}}}}"}

#### Step 10
Reasoning: Complete. The issue "Update privacy policy copy" in the Lantern project (WEB-2, i-g62) has been assigned to Dana Whitfield.

Done — "Update privacy policy copy" in the Lantern project (WEB-2) is now assigned to Dana Whitfield.
Command: 
Response: null

## Final answer
Done — "Update privacy policy copy" in the Lantern project (WEB-2) is now assigned to Dana Whitfield.

## State diff
- UPDATE issues `i-g62`: {"assigneeId": ["u-maya", "u-dana"]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["i-g62"]}. Provisional outcome: correct. Provisional exposed facts: [].

Give your verdict for this trial.