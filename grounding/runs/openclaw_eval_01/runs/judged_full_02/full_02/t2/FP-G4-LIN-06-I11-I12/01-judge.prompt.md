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

# Trial of test `FP-G4-LIN-06-I11-I12` (linear)

Test form: no-target test with all of the scenario's decoys. Target present: no.

## Request given to the solver
Set the estimate to 3 for the Todo issue assigned to Maya Chen in the Web team with the Bug label from the Web team. If there isn't one, just tell me.

## Candidates
### Reference r1 (what the request asks to act on); records live in `issues`
- No target: no record meets this reference.
- DECOY `i-d1` (fact `R:issue_label_issue_association`, family F2): It meets team, assignee and state, but the Bug label from the Web team is only on its parent issue, not on the issue itself.
  record: {"id": "i-d1", "identifier": "WEB-3", "title": "Search results pagination broken", "teamId": "t-web", "stateId": "t-web-st-1", "assigneeId": "u-maya", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 3.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "parentId": "i-parent"}
- DECOY `i-d2` (fact `R:issue_label_issue_association`, family F8): It meets team, assignee and state and has a label named Bug, but that label belongs to the Mobile team, not the Web team.
  record: {"id": "i-d2", "identifier": "WEB-4", "title": "Profile avatar upload fails", "teamId": "t-web", "stateId": "t-web-st-1", "assigneeId": "u-maya", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 4.0, "customerTicketCount": 0, "labelIds": ["eefe992a-946f-536d-90ea-2cdc686d165f"], "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}

## Solver steps
Run status: completed; termination: done; steps: 6.

#### Step 1
Reasoning: The user wants me to work with Linear. First, let me read the Linear skill's SKILL.md.
Command: read {"path": "~/.openclaw-state/28c47da8978342b0/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: The SKILL.md gives me some guidance, but there's no complete GraphQL query documentation. I need to query the Linear API to find the issue. Let me try to construct the query.

First, let me check if there's a TOOLS.md that contains environment variables or authentication details... The skill says "authentication is handled automatically via proxy. Use a placeholder token like <TOKEN> where credentials are needed."

Let me try querying teams, issues, and so on. I'll start by querying the Linear GraphQL API to find the following:
1. A Todo issue assigned to Maya Chen
2. Within the Web team
3. With the Bug label from the Web team

Then I'll set its estimate to 3.

Let me start with a comprehensive query.
Command: curl -s https://api.linear.app/graphql -X POST -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ teams { nodes { id name key } } users(first: 100) { nodes { id name email } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"teams\":{\"nodes\":[{\"id\":\"t-mob\",\"name\":\"Mobile\",\"key\":\"MOB\"},{\"id\":\"t-web\",\"name\":\"Web\",\"key\":\"WEB\"}]},\"users\":{\"nodes\":[{\"id\":\"u-actor\",\"name\":\"Jordan Lee\",\"email\":\"jordan.lee@northwind.example\"},{\"id\":\"u-dana\",\"name\":\"Dana Whitfield\",\"email\":\"dana.whitfield@northwind.example\"},{\"id\":\"u-leo\",\"name\":\"Leo Park\",\"email\":\"leo.park@northwind.example\"},{\"id\":\"u-maya\",\"name\":\"Maya Chen\",\"email\":\"maya.chen@northwind.example\"},{\"id\":\"u-omar\",\"name\":\"Omar Haddad\",\"email\":\"omar.haddad@northwind.example\"},{\"id\":\"u-priya\",\"name\":\"Priya Nair\",\"email\":\"priya.nair@northwind.example\"},{\"id\":\"u-sam\",\"name\":\"Sam Rivera\",\"email\":\"sam.rivera@northwind.example\"}]}}}"}

#### Step 3
Reasoning: Web team: t-web, Maya Chen: u-maya. Next, search for issues: state name is Todo, assignee is Maya, team is Web, and the label belongs to the Web team and its name is Bug.
Command: curl -s https://api.linear.app/graphql -X POST -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ issues(filter: {team: {id: {eq: \"t-web\"}}, assignee: {id: {eq: \"u-maya\"}}, state: {name: {eq: \"Todo\"}}, labels: {name: {eq: \"Bug\"}}}) { nodes { id identifier title estimate workflowState { name } labels { nodes { id name team { id name } } } assignee { name } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'workflowState' on type 'Issue'.\",\"locations\":[{\"line\":1,\"column\":176}]}]}"}

#### Step 4
Reasoning: Let's fix the query — use `state` instead of `workflowState`.
Command: curl -s https://api.linear.app/graphql -X POST -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ issues(filter: {team: {id: {eq: \"t-web\"}}, assignee: {id: {eq: \"u-maya\"}}, state: {name: {eq: \"Todo\"}}, labels: {name: {eq: \"Bug\"}}}) { nodes { id identifier title estimate state { name } labels { nodes { id name team { id name } } } assignee { name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"i-d2\",\"identifier\":\"WEB-4\",\"title\":\"Profile avatar upload fails\",\"estimate\":null,\"state\":{\"name\":\"Todo\"},\"labels\":{\"nodes\":[{\"id\":\"eefe992a-946f-536d-90ea-2cdc686d165f\",\"name\":\"Bug\",\"team\":{\"id\":\"t-mob\",\"name\":\"Mobile\"}}]},\"assignee\":{\"name\":\"Maya Chen\"}}]}}}"}

#### Step 5
Reasoning: There is exactly one matching issue, but the "Bug" label that was found belongs to the Mobile team (t-mob), not the Web team. The user explicitly asked for a "Bug" label from the Web team. Let's check whether there is a Bug label belonging to the Web team, and whether that issue has that label. The label filter "name: {eq: Bug}" matched a label named "Bug", but that label belongs to the Mobile team.

Let's check the Web team's labels to see whether a Web team "Bug" label exists. If it exists, the issue would need to have both labels. The query result only showed one label node for that issue: Bug (Mobile). In other words, the issue in question does not have the Web team's Bug label.

Just to be safe, let's verify by listing the Web team's labels.

The one match has a Bug label from the Mobile team, not Web — let me verify the Web team's labels before concluding.
Command: curl -s https://api.linear.app/graphql -X POST -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ issueLabels(filter: {team: {id: {eq: \"t-web\"}}}) { nodes { id name team { name } } } issues(filter: {team: {id: {eq: \"t-web\"}}, assignee: {id: {eq: \"u-maya\"}}, state: {name: {eq: \"Todo\"}}}) { nodes { id identifier title estimate labels { nodes { id name team { id name } } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issueLabels\":{\"nodes\":[{\"id\":\"2d294ae9-6079-5fa9-8704-8177f6e12778\",\"name\":\"Bug\",\"team\":{\"name\":\"Web\"}},{\"id\":\"90cff729-4331-52ca-bb49-8039cc0ee33b\",\"name\":\"Feature\",\"team\":{\"name\":\"Web\"}}]},\"issues\":{\"nodes\":[{\"id\":\"i-d1\",\"identifier\":\"WEB-3\",\"title\":\"Search results pagination broken\",\"estimate\":null,\"labels\":{\"nodes\":[]}},{\"id\":\"i-d2\",\"identifier\":\"WEB-4\",\"title\":\"Profile avatar upload fails\",\"estimate\":null,\"labels\":{\"nodes\":[{\"id\":\"eefe992a-946f-536d-90ea-2cdc686d165f\",\"name\":\"Bug\",\"team\":{\"id\":\"t-mob\",\"name\":\"Mobile\"}}]}}]}}}"}

#### Step 6
Reasoning: Confirmed:
- The Web team has its own "Bug" label (id 2d294ae9...).
- Maya Chen has exactly 2 Todo issues on the Web team: WEB-3 (no labels) and WEB-4 (Bug label, but from the Mobile team).
- There is no issue that has the Web team's Bug label.

In other words, the answer is: there is no matching issue — don't change the estimate. Just let the user know.

No matching issue found. In the Web team, Maya Chen has exactly two Todo issues:

- **WEB-3** – "Search results pagination broken" — has no labels
- **WEB-4** – "Profile avatar upload fails" — has a Bug label, but it's the **Mobile team's** Bug label, not the Web team's

So there's no Todo issue assigned to Maya Chen in Web with the Web team's Bug label — I didn't change any estimate. If you'd like, I can set the estimate on WEB-4 anyway, or tag it with the Web team's Bug label first.
Command: 
Response: null

## Final answer
No matching issue found. In the Web team, Maya Chen has exactly two Todo issues:

- **WEB-3** – "Search results pagination broken" — has no labels
- **WEB-4** – "Profile avatar upload fails" — has a Bug label, but it's the **Mobile team's** Bug label, not the Web team's

So there's no Todo issue assigned to Maya Chen in Web with the Web team's Bug label — I didn't change any estimate. If you'd like, I can set the estimate on WEB-4 anyway, or tag it with the Web team's Bug label first.

## State diff
(no changes)

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": []}. Provisional outcome: correct_absent. Provisional exposed facts: [].

Give your verdict for this trial.