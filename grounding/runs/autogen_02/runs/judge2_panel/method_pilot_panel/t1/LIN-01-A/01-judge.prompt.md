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

# Trial of test `LIN-01-A` (linear)

Test form: policy panel. Target present: yes.

## Request given to the solver
Move the Mobile team's high-priority bug that's assigned to Priya Nair to In Review.

## Candidates
### Reference r1 (what the request asks to act on); records live in `issues`
- No target: no record meets this reference.
- DECOY `i-mob-13` (fact `R:Issue.assigneeId`): Priya created MOB-13; Leo is assigned.
  record: {"id": "i-mob-13", "identifier": "MOB-2", "title": "Push notifications arrive twice", "teamId": "t-mob", "stateId": "t-mob-st-1", "assigneeId": "u-leo", "creatorId": "u-priya", "priority": 2.0, "priorityLabel": "High", "number": 2.0, "customerTicketCount": 0, "labelIds": ["lab-bug"], "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `i-mob-14` (fact `A:Issue.priority`): Low priority.
  record: {"id": "i-mob-14", "identifier": "MOB-3", "title": "Settings toggle misaligned on tablets", "teamId": "t-mob", "stateId": "t-mob-st-1", "assigneeId": "u-priya", "creatorId": "u-dana", "priority": 4.0, "priorityLabel": "Low", "number": 3.0, "customerTicketCount": 0, "labelIds": ["lab-bug"], "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `i-mob-16` (fact `R:issue_label_issue_association`): Only the parent epic carries the Bug label.
  record: {"id": "i-mob-16", "identifier": "MOB-5", "title": "Cache images for offline mode", "teamId": "t-mob", "stateId": "t-mob-st-1", "assigneeId": "u-priya", "creatorId": "u-dana", "priority": 2.0, "priorityLabel": "High", "number": 5.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "parentId": "i-mob-15"}
- DECOY `i-mob-17` (fact `A:IssueLabel.name`): Labeled Feature.
  record: {"id": "i-mob-17", "identifier": "MOB-6", "title": "Add biometric login", "teamId": "t-mob", "stateId": "t-mob-st-1", "assigneeId": "u-priya", "creatorId": "u-dana", "priority": 2.0, "priorityLabel": "High", "number": 6.0, "customerTicketCount": 0, "labelIds": ["lab-feat"], "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `i-web-21` (fact `A:Team.name`): Web team.
  record: {"id": "i-web-21", "identifier": "WEB-1", "title": "Checkout button unresponsive on Safari", "teamId": "t-web", "stateId": "t-web-st-1", "assigneeId": "u-priya", "creatorId": "u-dana", "priority": 2.0, "priorityLabel": "High", "number": 1.0, "customerTicketCount": 0, "labelIds": ["lab-bug"], "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
### Reference r2 (what the request asks to act on); records live in `workflow_states`
- TARGET `t-mob-st-3`: {"id": "t-mob-st-3", "teamId": "t-mob", "name": "In Review", "position": 3.0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `t-web-st-3` (fact `R:WorkflowState.teamId`): The Web team's In Review state.
  record: {"id": "t-web-st-3", "teamId": "t-web", "name": "In Review", "position": 3.0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `t-mob-st-2` (fact `A:WorkflowState.name`): Mobile's In Progress state.
  record: {"id": "t-mob-st-2", "teamId": "t-mob", "name": "In Progress", "position": 2.0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}

## Solver steps
Run status: completed; termination: done; steps: 17.

#### Step 1
Reasoning: I need to find the Mobile team's high-priority bug assigned to Priya Nair, then move it to "In Review". Let me start by finding the relevant team, user, and workflow state.
Command: curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -d '{
    "query": "{
      teams {
        nodes {
          id
          name
          key
        }
      }
      users {
        nodes {
          id
          name
          emailAddress
        }
      }
      workflowStates {
        nodes {
          id
          name
          type
        }
      }
    }
  }'
Response: {"status": "success", "stdout": "Request body is not a valid JSON", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_e8c3efbd6d26408bb7ea9c343a7ca58e_m33cqyki"}

#### Step 2
Reasoning: The JSON had issues with quoting. Let me fix the command with proper escaping.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ teams { nodes { id name key } } users { nodes { id name emailAddress } } workflowStates { nodes { id name type } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'emailAddress' on type 'User'.\",\"locations\":[{\"line\":1,\"column\":59}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_e8c3efbd6d26408bb7ea9c343a7ca58e_m33cqyki"}

#### Step 3
Reasoning: The `emailAddress` field doesn't exist on User. Let me remove it and retry.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ teams { nodes { id name key } } users { nodes { id name } } workflowStates { nodes { id name type } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"teams\":{\"nodes\":[{\"id\":\"t-mob\",\"name\":\"Mobile\",\"key\":\"MOB\"},{\"id\":\"t-web\",\"name\":\"Web\",\"key\":\"WEB\"}]},\"users\":{\"nodes\":[{\"id\":\"u-actor\",\"name\":\"Jordan Lee\"},{\"id\":\"u-dana\",\"name\":\"Dana Whitfield\"},{\"id\":\"u-leo\",\"name\":\"Leo Park\"},{\"id\":\"u-maya\",\"name\":\"Maya Chen\"},{\"id\":\"u-omar\",\"name\":\"Omar Haddad\"},{\"id\":\"u-priya\",\"name\":\"Priya Nair\"},{\"id\":\"u-sam\",\"name\":\"Sam Rivera\"}]},\"workflowStates\":{\"nodes\":[{\"id\":\"t-mob-st-0\",\"name\":\"Backlog\",\"type\":\"backlog\"},{\"id\":\"t-mob-st-1\",\"name\":\"Todo\",\"type\":\"unstarted\"},{\"id\":\"t-mob-st-2\",\"name\":\"In Progress\",\"type\":\"started\"},{\"id\":\"t-mob-st-3\",\"name\":\"In Review\",\"type\":\"started\"},{\"id\":\"t-mob-st-4\",\"name\":\"Done\",\"type\":\"completed\"},{\"id\":\"t-mob-st-5\",\"name\":\"Canceled\",\"type\":\"canceled\"},{\"id\":\"t-web-st-0\",\"name\":\"Backlog\",\"type\":\"backlog\"},{\"id\":\"t-web-st-1\",\"name\":\"Todo\",\"type\":\"unstarted\"},{\"id\":\"t-web-st-2\",\"name\":\"In Progress\",\"type\":\"started\"},{\"id\":\"t-web-st-3\",\"name\":\"In Review\",\"type\":\"started\"},{\"id\":\"t-web-st-4\",\"name\":\"Done\",\"type\":\"completed\"},{\"id\":\"t-web-st-5\",\"name\":\"Canceled\",\"type\":\"canceled\"}]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_e8c3efbd6d26408bb7ea9c343a7ca58e_m33cqyki"}

#### Step 4
Reasoning: Now I have the IDs:
- Mobile team: "t-mob"
- Priya Nair: "u-priya"
- "In Review" workflow state: "t-mob-st-3"

I need to find the high-priority bug assigned to Priya Nair in the Mobile team. Let me query issues with these filters.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ issues(filter: { team: { key: { eq: \"MOB\" } }, assignee: { id: { eq: \"u-priya\" } }, priority: { eq: 2 } }, first: 10) { nodes { id identifier name priority state { id name } workflowState { id name } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'name' on type 'Issue'.\",\"locations\":[{\"line\":1,\"column\":145}]},{\"message\":\"Cannot query field 'workflowState' on type 'Issue'.\",\"locations\":[{\"line\":1,\"column\":177}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_e8c3efbd6d26408bb7ea9c343a7ca58e_m33cqyki"}

#### Step 5
Reasoning: The `name` and `workflowState` fields don't exist on Issue. Let me use `title` and `state` instead.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ issues(filter: { team: { key: { eq: \"MOB\" } }, assignee: { id: { eq: \"u-priya\" } }, priority: { eq: 2 } }, first: 10) { nodes { id identifier title priority state { id name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"i-mob-16\",\"identifier\":\"MOB-5\",\"title\":\"Cache images for offline mode\",\"priority\":2.0,\"state\":{\"id\":\"t-mob-st-1\",\"name\":\"Todo\"}},{\"id\":\"i-mob-17\",\"identifier\":\"MOB-6\",\"title\":\"Add biometric login\",\"priority\":2.0,\"state\":{\"id\":\"t-mob-st-1\",\"name\":\"Todo\"}}]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_e8c3efbd6d26408bb7ea9c343a7ca58e_m33cqyki"}

#### Step 6
Reasoning: I found two high-priority issues, but the task specifies a "bug". Let me check if there's a way to filter by issue type (bug vs feature). Let me query with additional fields to see the type/branch of these issues.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ issues(filter: { team: { key: { eq: \"MOB\" } }, assignee: { id: { eq: \"u-priya\" } }, priority: { eq: 2 } }, first: 10) { nodes { id identifier title priority state { id name } type { id name } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'type' on type 'Issue'.\",\"locations\":[{\"line\":1,\"column\":178}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_e8c3efbd6d26408bb7ea9c343a7ca58e_m33cqyki"}

#### Step 7
Reasoning: Let me try other field names for issue type/category - maybe it's `branch` or `category`.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ issues(filter: { team: { key: { eq: \"MOB\" } }, assignee: { id: { eq: \"u-priya\" } }, priority: { eq: 2 } }, first: 10) { nodes { id identifier title priority state { id name } branch { id name } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'branch' on type 'Issue'.\",\"locations\":[{\"line\":1,\"column\":178}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_e8c3efbd6d26408bb7ea9c343a7ca58e_m33cqyki"}

#### Step 8
Reasoning: Let me try to introspect the Issue type to see what fields are available.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ __type(name: \"Issue\") { fields { name } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"fields\":[{\"name\":\"activitySummary\"},{\"name\":\"addedToCycleAt\"},{\"name\":\"addedToProjectAt\"},{\"name\":\"addedToTeamAt\"},{\"name\":\"archivedAt\"},{\"name\":\"asksExternalUserRequester\"},{\"name\":\"asksRequester\"},{\"name\":\"assignee\"},{\"name\":\"attachments\"},{\"name\":\"autoArchivedAt\"},{\"name\":\"autoClosedAt\"},{\"name\":\"botActor\"},{\"name\":\"branchName\"},{\"name\":\"canceledAt\"},{\"name\":\"children\"},{\"name\":\"comments\"},{\"name\":\"documents\"},{\"name\":\"completedAt\"},{\"name\":\"createdAt\"},{\"name\":\"creator\"},{\"name\":\"customerTicketCount\"},{\"name\":\"cycle\"},{\"name\":\"delegate\"},{\"name\":\"description\"},{\"name\":\"descriptionState\"},{\"name\":\"documentContent\"},{\"name\":\"dueDate\"},{\"name\":\"estimate\"},{\"name\":\"externalUserCreator\"},{\"name\":\"favorite\"},{\"name\":\"formerAttachments\"},{\"name\":\"formerNeeds\"},{\"name\":\"history\"},{\"name\":\"id\"},{\"name\":\"identifier\"},{\"name\":\"incomingSuggestions\"},{\"name\":\"integrationSourceType\"},{\"name\":\"inverseRelations\"},{\"name\":\"labelIds\"},{\"name\":\"labels\"},{\"name\":\"lastAppliedTemplate\"},{\"name\":\"needs\"},{\"name\":\"number\"},{\"name\":\"parent\"},{\"name\":\"previousIdentifiers\"},{\"name\":\"priority\"},{\"name\":\"priorityLabel\"},{\"name\":\"prioritySortOrder\"},{\"name\":\"project\"},{\"name\":\"projectMilestone\"},{\"name\":\"reactionData\"},{\"name\":\"reactions\"},{\"name\":\"recurringIssueTemplate\"},{\"name\":\"relations\"},{\"name\":\"slaBreachesAt\"},{\"name\":\"slaHighRiskAt\"},{\"name\":\"slaMediumRiskAt\"},{\"name\":\"slaStartedAt\"},{\"name\":\"slaType\"},{\"name\":\"snoozedBy\"},{\"name\":\"snoozedUntilAt\"},{\"name\":\"sortOrder\"},{\"name\":\"sourceComment\"},{\"name\":\"startedAt\"},{\"name\":\"startedTriageAt\"},{\"name\":\"state\"},{\"name\":\"subIssueSortOrder\"},{\"name\":\"subscribers\"},{\"name\":\"suggestions\"},{\"name\":\"suggestionsGeneratedAt\"},{\"name\":\"syncedWith\"},{\"name\":\"team\"},{\"name\":\"title\"},{\"name\":\"trashed\"},{\"name\":\"triagedAt\"},{\"name\":\"updatedAt\"},{\"name\":\"url\"}]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_e8c3efbd6d26408bb7ea9c343a7ca58e_m33cqyki"}

#### Step 9
Reasoning: I don't see a direct "type" or "category" field on Issue. Let me check the filter options for issues to see if there's a way to filter by category (bug, feature, task, etc.).
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ __type(name: \"IssueWhereInput\") { inputFields { name } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":null}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_e8c3efbd6d26408bb7ea9c343a7ca58e_m33cqyki"}

#### Step 10
Reasoning: Let me try to introspect the Issue type's query argument to find the filter type.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ __type(name: \"Query\") { fields { name args { name type { name kind ofType { name kind } } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"fields\":[{\"name\":\"administrableTeams\",\"args\":[{\"name\":\"after\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"before\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"filter\",\"type\":{\"name\":\"TeamFilter\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"first\",\"type\":{\"name\":\"Int\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"includeArchived\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"last\",\"type\":{\"name\":\"Int\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"orderBy\",\"type\":{\"name\":\"PaginationOrderBy\",\"kind\":\"ENUM\",\"ofType\":null}}]},{\"name\":\"agentActivities\",\"args\":[{\"name\":\"after\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"before\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"filter\",\"type\":{\"name\":\"AgentActivityFilter\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"first\",\"type\":{\"name\":\"Int\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"includeArchived\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"last\",\"type\":{\"name\":\"Int\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"orderBy\",\"type\":{\"name\":\"PaginationOrderBy\",\"kind\":\"ENUM\",\"ofType\":null}}]},{\"name\":\"agentActivity\",\"args\":[{\"name\":\"id\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"String\",\"kind\":\"SCALAR\"}}}]},{\"name\":\"agentSession\",\"args\":[{\"name\":\"id\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"String\",\"kind\":\"SCALAR\"}}}]},{\"name\":\"agentSessions\",\"args\":[{\"name\":\"after\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"before\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"first\",\"type\":{\"name\":\"Int\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"includeArchived\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"last\",\"type\":{\"name\":\"Int\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"orderBy\",\"type\":{\"name\":\"PaginationOrderBy\",\"kind\":\"ENUM\",\"ofType\":null}}]},{\"name\":\"apiKeys\",\"args\":[{\"name\":\"after\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"before\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"first\",\"type\":{\"name\":\"Int\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"includeArchived\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"last\",\"type\":{\"name\":\"Int\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"orderBy\",\"type\":{\"name\":\"PaginationOrderBy\",\"kind\":\"ENUM\",\"ofType\":null}}]},{\"name\":\"applicationInfo\",\"args\":[{\"name\":\"clientId\",\"type\":{ […43116 chars omitted…] "ofType\":null}},{\"name\":\"first\",\"type\":{\"name\":\"Int\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"includeArchived\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"last\",\"type\":{\"name\":\"Int\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"orderBy\",\"type\":{\"name\":\"PaginationOrderBy\",\"kind\":\"ENUM\",\"ofType\":null}}]}]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_e8c3efbd6d26408bb7ea9c343a7ca58e_m33cqyki"}

#### Step 11
Reasoning: Let me check the IssueFilter input type to see if there's a way to filter by issue category (bug vs feature).
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ __type(name: \"IssueFilter\") { inputFields { name } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"inputFields\":[{\"name\":\"addedToCycleAt\"},{\"name\":\"addedToCyclePeriod\"},{\"name\":\"ageTime\"},{\"name\":\"and\"},{\"name\":\"archivedAt\"},{\"name\":\"assignee\"},{\"name\":\"attachments\"},{\"name\":\"autoArchivedAt\"},{\"name\":\"autoClosedAt\"},{\"name\":\"accumulatedStateUpdatedAt\"},{\"name\":\"canceledAt\"},{\"name\":\"children\"},{\"name\":\"comments\"},{\"name\":\"completedAt\"},{\"name\":\"createdAt\"},{\"name\":\"creator\"},{\"name\":\"customerCount\"},{\"name\":\"customerImportantCount\"},{\"name\":\"cycle\"},{\"name\":\"cycleTime\"},{\"name\":\"delegate\"},{\"name\":\"description\"},{\"name\":\"dueDate\"},{\"name\":\"estimate\"},{\"name\":\"hasBlockedByRelations\"},{\"name\":\"hasBlockingRelations\"},{\"name\":\"hasDuplicateRelations\"},{\"name\":\"hasSuggestedTeams\"},{\"name\":\"hasRelatedRelations\"},{\"name\":\"hasSuggestedAssignees\"},{\"name\":\"hasSuggestedLabels\"},{\"name\":\"hasSuggestedProjects\"},{\"name\":\"hasSuggestedRelatedIssues\"},{\"name\":\"hasSuggestedSimilarIssues\"},{\"name\":\"id\"},{\"name\":\"labels\"},{\"name\":\"lastAppliedTemplate\"},{\"name\":\"leadTime\"},{\"name\":\"needs\"},{\"name\":\"number\"},{\"name\":\"or\"},{\"name\":\"parent\"},{\"name\":\"priority\"},{\"name\":\"project\"},{\"name\":\"projectMilestone\"},{\"name\":\"reactions\"},{\"name\":\"recurringIssueTemplate\"},{\"name\":\"searchableContent\"},{\"name\":\"slaStatus\"},{\"name\":\"snoozedBy\"},{\"name\":\"snoozedUntilAt\"},{\"name\":\"sourceMetadata\"},{\"name\":\"startedAt\"},{\"name\":\"state\"},{\"name\":\"subscribers\"},{\"name\":\"suggestions\"},{\"name\":\"team\"},{\"name\":\"title\"},{\"name\":\"triageTime\"},{\"name\":\"triagedAt\"},{\"name\":\"updatedAt\"}]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_e8c3efbd6d26408bb7ea9c343a7ca58e_m33cqyki"}

#### Step 12
Reasoning: There's no category field in the filter. The task mentions a "bug" - let me check the labels on the issues to see if either has a "Bug" label, or let me check all issues for the Mobile team assigned to Priya to find which one is a bug.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ issues(filter: { team: { key: { eq: \"MOB\" } }, assignee: { id: { eq: \"u-priya\" } } }, first: 20) { nodes { id identifier title priority labels { id name } state { id name } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'id' on type 'IssueLabelConnection'.\",\"locations\":[{\"line\":1,\"column\":148}]},{\"message\":\"Cannot query field 'name' on type 'IssueLabelConnection'.\",\"locations\":[{\"line\":1,\"column\":151}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_e8c3efbd6d26408bb7ea9c343a7ca58e_m33cqyki"}

#### Step 13
Reasoning: The labels field is a connection type. Let me fix the query structure.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ issues(filter: { team: { key: { eq: \"MOB\" } }, assignee: { id: { eq: \"u-priya\" } } }, first: 20) { nodes { id identifier title priority labels { edges { node { id name } } } state { id name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"i-mob-14\",\"identifier\":\"MOB-3\",\"title\":\"Settings toggle misaligned on tablets\",\"priority\":4.0,\"labels\":{\"edges\":[{\"node\":{\"id\":\"lab-bug\",\"name\":\"Bug\"}}]},\"state\":{\"id\":\"t-mob-st-1\",\"name\":\"Todo\"}},{\"id\":\"i-mob-16\",\"identifier\":\"MOB-5\",\"title\":\"Cache images for offline mode\",\"priority\":2.0,\"labels\":{\"edges\":[]},\"state\":{\"id\":\"t-mob-st-1\",\"name\":\"Todo\"}},{\"id\":\"i-mob-17\",\"identifier\":\"MOB-6\",\"title\":\"Add biometric login\",\"priority\":2.0,\"labels\":{\"edges\":[{\"node\":{\"id\":\"lab-feat\",\"name\":\"Feature\"}}]},\"state\":{\"id\":\"t-mob-st-1\",\"name\":\"Todo\"}}]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_e8c3efbd6d26408bb7ea9c343a7ca58e_m33cqyki"}

#### Step 14
Reasoning: I found the issue. MOB-3 "Settings toggle misaligned on tablets" is the only issue with the "Bug" label, and it has priority 4.0 (Urgent, which is the highest priority - definitely "high-priority"). I need to update this issue (id: "i-mob-14") to move it to the "In Review" workflow state (id: "t-mob-st-3").
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"mutation { issueUpdate(id: \"i-mob-14\", input: { workflowStateId: \"t-mob-st-3\" }) { success issue { id identifier title state { id name } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Field 'workflowStateId' is not defined by type 'IssueUpdateInput'.\",\"locations\":[{\"line\":1,\"column\":49}]}]}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_e8c3efbd6d26408bb7ea9c343a7ca58e_m33cqyki"}

#### Step 15
Reasoning: Let me check the IssueUpdateInput type to see the correct field name for updating the workflow state.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"{ __type(name: \"IssueUpdateInput\") { inputFields { name } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"inputFields\":[{\"name\":\"addedLabelIds\"},{\"name\":\"assigneeId\"},{\"name\":\"autoClosedByParentClosing\"},{\"name\":\"cycleId\"},{\"name\":\"delegateId\"},{\"name\":\"description\"},{\"name\":\"descriptionData\"},{\"name\":\"dueDate\"},{\"name\":\"estimate\"},{\"name\":\"labelIds\"},{\"name\":\"lastAppliedTemplateId\"},{\"name\":\"parentId\"},{\"name\":\"priority\"},{\"name\":\"prioritySortOrder\"},{\"name\":\"projectId\"},{\"name\":\"projectMilestoneId\"},{\"name\":\"removedLabelIds\"},{\"name\":\"slaBreachesAt\"},{\"name\":\"slaStartedAt\"},{\"name\":\"slaType\"},{\"name\":\"snoozedById\"},{\"name\":\"snoozedUntilAt\"},{\"name\":\"sortOrder\"},{\"name\":\"stateId\"},{\"name\":\"subIssueSortOrder\"},{\"name\":\"subscriberIds\"},{\"name\":\"teamId\"},{\"name\":\"title\"},{\"name\":\"trashed\"}]}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_e8c3efbd6d26408bb7ea9c343a7ca58e_m33cqyki"}

#### Step 16
Reasoning: The field is `stateId`, not `workflowStateId`. Let me update the mutation.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -d '{"query":"mutation { issueUpdate(id: \"i-mob-14\", input: { stateId: \"t-mob-st-3\" }) { success issue { id identifier title state { id name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issueUpdate\":{\"success\":true,\"issue\":{\"id\":\"i-mob-14\",\"identifier\":\"MOB-3\",\"title\":\"Settings toggle misaligned on tablets\",\"state\":{\"id\":\"t-mob-st-3\",\"name\":\"In Review\"}}}}}", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_e8c3efbd6d26408bb7ea9c343a7ca58e_m33cqyki"}

#### Step 17
Reasoning: The mutation succeeded. The Mobile team's high-priority bug (MOB-3 "Settings toggle misaligned on tablets") assigned to Priya Nair has been successfully moved to the "In Review" workflow state.


<done>
Successfully moved the Mobile team's high-priority bug "Settings toggle misaligned on tablets" (MOB-3), assigned to Priya Nair, from "Todo" to "In Review".
</done>
Command: 
Response: null

## Final answer
Successfully moved the Mobile team's high-priority bug "Settings toggle misaligned on tablets" (MOB-3), assigned to Priya Nair, from "Todo" to "In Review".

## State diff
- UPDATE issues `i-mob-14`: {"stateId": ["t-mob-st-1", "t-mob-st-3"]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["i-mob-14"], "r2": ["t-mob-st-3"]}. Provisional outcome: incorrect. Provisional exposed facts: ['A:Issue.priority'].

Give your verdict for this trial.