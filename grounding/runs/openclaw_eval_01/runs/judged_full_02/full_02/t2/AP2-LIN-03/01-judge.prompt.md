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

# Trial of test `AP2-LIN-03` (linear)

Test form: cover. Target present: yes.

## Request given to the solver
Rename the private team whose key starts with GR and whose description mentions the Q3 OKR pilot rollout to 'Growth Pod'.

## Candidates
### Reference r1 (what the request asks to act on); records live in `teams`
- TARGET `t-growth`: {"id": "t-growth", "name": "Growth", "key": "GRW", "displayName": "Growth", "organizationId": "org-northwind", "description": "Coordinates the Q3 OKR pilot rollout across regional sales teams.", "createdAt": "2025-01-01T00:00:00", "updatedAt": "2025-01-01T00:00:00", "aiThreadSummariesEnabled": false, "autoArchivePeriod": 6.0, "cycleCooldownTime": 0.0, "cycleDuration": 2.0, "cycleIssueAutoAssignCompleted": false, "cycleIssueAutoAssignStarted": false, "cycleLockToActive": false, "cycleStartDay": 1.0, "cyclesEnabled": true, "defaultIssueEstimate": 1.0, "groupIssueHistory": false, "inheritIssueEstimation": false, "inheritWorkflowStatuses": false, "issueCount": 0, "issueEstimationAllowZero": fals…
- DECOY `t-growthpartnerships` (fact `A:Team.key`, family F1): Named Growth Partnerships and just as private with the same Q3 OKR pilot rollout description, but its key is PTN, which doesn't start with GR.
  record: {"id": "t-growthpartnerships", "name": "Growth Partnerships", "key": "PTN", "displayName": "Growth Partnerships", "organizationId": "org-northwind", "description": "Coordinates the Q3 OKR pilot rollout across regional sales teams.", "createdAt": "2025-01-01T00:00:00", "updatedAt": "2025-01-01T00:00:00", "aiThreadSummariesEnabled": false, "autoArchivePeriod": 6.0, "cycleCooldownTime": 0.0, "cycleDuration": 2.0, "cycleIssueAutoAssignCompleted": false, "cycleIssueAutoAssignStarted": false, "cycleLockToActive": false, "cycleStartDay": 1.0, "cyclesEnabled": true, "defaultIssueEstimate": 1.0, "groupIssueHistory": false, "inheritIssueEstimation": false, "inheritWorkflowStatuses": false, "issueCount…
- DECOY `t-growthops` (fact `A:Team.description`, family F0): Same GR-prefixed key and privacy as Growth, but its description is about internal tooling, not the Q3 OKR pilot rollout.
  record: {"id": "t-growthops", "name": "Growth Ops", "key": "GRO", "displayName": "Growth Ops", "organizationId": "org-northwind", "description": "Handles internal tooling requests and support tickets for the growth organization.", "createdAt": "2025-01-01T00:00:00", "updatedAt": "2025-01-01T00:00:00", "aiThreadSummariesEnabled": false, "autoArchivePeriod": 6.0, "cycleCooldownTime": 0.0, "cycleDuration": 2.0, "cycleIssueAutoAssignCompleted": false, "cycleIssueAutoAssignStarted": false, "cycleLockToActive": false, "cycleStartDay": 1.0, "cyclesEnabled": true, "defaultIssueEstimate": 1.0, "groupIssueHistory": false, "inheritIssueEstimation": false, "inheritWorkflowStatuses": false, "issueCount": 0, "iss…
- DECOY `t-growthanalytics` (fact `A:Team.private`, family F0): Same GR-prefixed key and description as Growth, but this team is not private.
  record: {"id": "t-growthanalytics", "name": "Growth Analytics", "key": "GRA", "displayName": "Growth Analytics", "organizationId": "org-northwind", "description": "Coordinates the Q3 OKR pilot rollout across regional sales teams.", "createdAt": "2025-01-01T00:00:00", "updatedAt": "2025-01-01T00:00:00", "aiThreadSummariesEnabled": false, "autoArchivePeriod": 6.0, "cycleCooldownTime": 0.0, "cycleDuration": 2.0, "cycleIssueAutoAssignCompleted": false, "cycleIssueAutoAssignStarted": false, "cycleLockToActive": false, "cycleStartDay": 1.0, "cyclesEnabled": true, "defaultIssueEstimate": 1.0, "groupIssueHistory": false, "inheritIssueEstimation": false, "inheritWorkflowStatuses": false, "issueCount": 0, "is…

## Solver steps
Run status: completed; termination: done; steps: 8.

#### Step 1
Reasoning: The user is asking me to use the Linear skill to rename a private team. Let me start by reading the Linear skill's SKILL.md.
Command: read {"path": "~/.openclaw-state/931bea529dd44e7b/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: I need to find the private team whose key starts with "GR" and whose description mentions the Q3 OKR pilot rollout. I'll try querying the Linear API for teams with their keys and descriptions.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ teams { nodes { id key name description isPrivate } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'isPrivate' on type 'Team'. Did you mean 'private'?\",\"locations\":[{\"line\":1,\"column\":43}]}]}"}

#### Step 3
Reasoning: The field is `private`. Let me retry.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ teams { nodes { id key name description private } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"teams\":{\"nodes\":[{\"id\":\"t-eng\",\"key\":\"ENG\",\"name\":\"Engineering\",\"description\":\"Builds and maintains the core product platform.\",\"private\":false},{\"id\":\"t-growth\",\"key\":\"GRW\",\"name\":\"Growth\",\"description\":\"Coordinates the Q3 OKR pilot rollout across regional sales teams.\",\"private\":true},{\"id\":\"t-growthanalytics\",\"key\":\"GRA\",\"name\":\"Growth Analytics\",\"description\":\"Coordinates the Q3 OKR pilot rollout across regional sales teams.\",\"private\":false},{\"id\":\"t-growthops\",\"key\":\"GRO\",\"name\":\"Growth Ops\",\"description\":\"Handles internal tooling requests and support tickets for the growth organization.\",\"private\":true},{\"id\":\"t-growthpartnerships\",\"key\":\"PTN\",\"name\":\"Growth Partnerships\",\"description\":\"Coordinates the Q3 OKR pilot rollout across regional sales teams.\",\"private\":true},{\"id\":\"t-sales\",\"key\":\"SLS\",\"name\":\"Sales\",\"description\":\"Manages the enterprise sales pipeline and forecasting.\",\"private\":true}]}}}"}

#### Step 4
Reasoning: The only private team whose key starts with GR and whose description mentions "Q3 OKR pilot rollout" is `t-growth` (key GRW, name "Growth"). GRA is not private, and GRO's description is different. Therefore, I'll update the name to "Growth Pod".

I found the matching team: **Growth** (key GRW, private, description: "Coordinates the Q3 OKR pilot rollout…"). Updating its name now.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"mutation { teamUpdate(id: \"t-growth\", name: \"Growth Pod\") { id key name description private success } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Unknown argument 'name' on field 'Mutation.teamUpdate'.\",\"locations\":[{\"line\":1,\"column\":39}]},{\"message\":\"Cannot query field 'id' on type 'TeamPayload'.\",\"locations\":[{\"line\":1,\"column\":61}]},{\"message\":\"Cannot query field 'key' on type 'TeamPayload'.\",\"locations\":[{\"line\":1,\"column\":64}]},{\"message\":\"Cannot query field 'name' on type 'TeamPayload'.\",\"locations\":[{\"line\":1,\"column\":68}]},{\"message\":\"Cannot query field 'description' on type 'TeamPayload'.\",\"locations\":[{\"line\":1,\"column\":73}]},{\"message\":\"Cannot query field 'private' on type 'TeamPayload'.\",\"locations\":[{\"line\":1,\"column\":85}]},{\"message\":\"Field 'teamUpdate' argument 'input' of type 'TeamUpdateInput!' is required, but it was not provided.\",\"locations\":[{\"line\":1,\"column\":12}]}]}"}

#### Step 5
Reasoning: teamUpdate requires an `input` argument. Let's try introspecting the TeamUpdateInput type.

The mutation needs an `input` object. Checking the schema for the right shape:
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ __type(name: \"TeamUpdateInput\") { inputFields { name type { name kind ofType { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"inputFields\":[{\"name\":\"aiThreadSummariesEnabled\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"autoArchivePeriod\",\"type\":{\"name\":\"Float\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"autoCloseChildIssues\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"autoCloseParentIssues\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"autoClosePeriod\",\"type\":{\"name\":\"Float\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"autoCloseStateId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"color\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"cycleCooldownTime\",\"type\":{\"name\":\"Int\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"cycleDuration\",\"type\":{\"name\":\"Int\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"cycleEnabledStartDate\",\"type\":{\"name\":\"DateTime\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"cycleIssueAutoAssignCompleted\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"cycleIssueAutoAssignStarted\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"cycleLockToActive\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"cycleStartDay\",\"type\":{\"name\":\"Float\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"cyclesEnabled\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"defaultIssueEstimate\",\"type\":{\"name\":\"Float\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"defaultIssueStateId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"defaultProjectTemplateId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"defaultTemplateForMembersId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"defaultTemplateForNonMembersId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"description\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"groupIssueHistory\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"icon\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"inheritIssueEstimation\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"inheritProductIntelligenceScope\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"inheritWorkflowStatuses\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"issueEstimationAllowZero\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"issueEstimationExtended\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"issueEstimationType\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"joinByDefault\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"key\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"markedAsDuplicateWorkflowStateId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"name\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"parentId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"private\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"productIntelligenceScope\",\"type\":{\"name\":\"ProductIntelligenceScope\",\"kind\":\"ENUM\",\"ofType\":null}},{\"name\":\"requirePriorityToLeaveTriage\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"scimManaged\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"setIssueSortOrderOnStateChange\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"slackIssueComments\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"slackIssueStatuses\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"slackNewIssue\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"timezone\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"triageEnabled\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"upcomingCycleCount\",\"type\":{\"name\":\"Float\",\"kind\":\"SCALAR\",\"ofType\":null}}]}}}"}

#### Step 6
Reasoning: The input has `name` and `id` fields... wait, I don't see `id` in the list of input fields. Let me check — TeamUpdateInput should normally have `id`. Looking at the list: aiThreadSummariesEnabled, autoArchivePeriod, ..., key, name, parentId, private... I don't see an `id` field in this list. Hmm, that's weird. Let me check the arguments of the Mutation.teamUpdate field.

Actually, the error from earlier said: "Field 'teamUpdate' argument 'input' of type 'TeamUpdateInput!' is required." In other words, teamUpdate takes an input. But where does the id go? Probably the first argument of the mutation is `id`, and the second is `input`. Let me check the Mutation field.

`TeamUpdateInput` has `name`, but I need to verify where `id` lives on the mutation. Checking:
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ __type(name: \"Mutation\") { fields(includeDeprecated: true) { name args { name type { name kind ofType { name } } } } } }"}' | python3 -c "import json,sys; d=json.load(sys.stdin); f=[x for x in d['data']['__type']['fields'] if 'team' in x['name'].lower()]; print(json.dumps(f, indent=2))"
Response: {"status": "success", "stdout": "[\n  {\n    \"name\": \"integrationSlackOrAsksUpdateSlackTeamName\",\n    \"args\": [\n      {\n        \"name\": \"integrationId\",\n        \"type\": {\n          \"name\": null,\n          \"kind\": \"NON_NULL\",\n          \"ofType\": {\n            \"name\": \"String\"\n          }\n        }\n      }\n    ]\n  },\n  {\n    \"name\": \"teamCreate\",\n    \"args\": [\n      {\n        \"name\": \"copySettingsFromTeamId\",\n        \"type\": {\n          \"name\": \"String\",\n          \"kind\": \"SCALAR\",\n          \"ofType\": null\n        }\n      },\n      {\n        \"name\": \"input\",\n        \"type\": {\n          \"name\": null,\n          \"kind\": \"NON_NULL\",\n          \"ofType\": {\n            \"name\": \"TeamCreateInput\"\n          }\n        }\n      }\n    ]\n  },\n  {\n    \"name\": \"teamCyclesDelete\",\n    \"args\": [\n      {\n        \"name\": \"id\",\n        \"type\": {\n          \"name\": null,\n          \"kind\": \"NON_NULL\",\n          \"ofType\": {\n            \"name\": \"String\"\n          }\n        }\n      }\n    ]\n  },\n  {\n    \"name\": \"teamDelete\",\n    \"args\": [\n      {\n        \"name\": \"id\",\n        \"type\": {\n          \"name\": null,\n          \"kind\": \"NON_NULL\",\n          \"ofType\": {\n            \"name\": \"String\"\n          }\n        }\n      }\n    ]\n  },\n  {\n    \"name\": \"teamKeyDelete\",\n    \"args\": [\n      {\n        \"name\": \"id\",\n        \"type\": {\n          \"name\": null,\n          \"kind\": \"NON_NULL\",\n          \"ofType\": {\n            \"name\": \"String\"\n          }\n        }\n      }\n    ]\n  },\n  {\n    \"name\": \"teamMembershipCreate\",\n    \"args\": [\n      {\n        \"name\": \"input\",\n        \"type\": {\n          \"name\": null,\n          \"kind\": \"NON_NULL\",\n          \"ofType\": {\n            \"name\": \"TeamMembershipCreateInput\"\n          }\n        }\n      }\n    ]\n  },\n  {\n    \"name\": \"teamMembershipDelete\",\n    \"args\": [\n      {\n        \"name\": \"alsoLeaveParentTeams\",\n        \"type\": {\n          \"name\": \"Boolean\",\n          \"kind\": \"SCALAR\",\n          \"ofType\": null\n        }\n      },\n      {\n        \"name\": \"id\",\n        \"type\": {\n          \"name\": null,\n          \"kind\": \"NON_NULL\",\n          \"ofType\": {\n            \"name\": \"String\"\n          }\n        }\n      }\n    ]\n  },\n  {\n    \"name\": \"teamMembershipUpdate\",\n    \"args\": [\n      {\n        \"name\": \"id\",\n        \"type\": {\n          \"name\": null,\n          \"kind\": \"NON_NULL\",\n          \"ofType\": {\n            \"name\": \"String\"\n          }\n        }\n      },\n      {\n        \"name\": \"input\",\n        \"type\": {\n          \"name\": null,\n          \"kind\": \"NON_NULL\",\n          \"ofType\": {\n            \"name\": \"TeamMembershipUpdateInput\"\n          }\n        }\n      }\n    ]\n  },\n  {\n    \"name\": \"teamUnarchive\",\n    \"args\": [\n      {\n        \"name\": \"id\",\n        \"type\": {\n          \"name\": null,\n          \"kind\": \"NON_NULL\",\n          \"ofType\": {\n            \"name\": \"String\"\n          }\n        }\n      }\n    ]\n  },\n  {\n    \"name\": \"teamUpdate\",\n    \"args\": [\n      {\n        \"name\": \"id\",\n        \"type\": {\n          \"name\": null,\n          \"kind\": \"NON_NULL\",\n          \"ofType\": {\n            \"name\": \"String\"\n          }\n        }\n      },\n      {\n        \"name\": \"input\",\n        \"type\": {\n          \"name\": null,\n          \"kind\": \"NON_NULL\",\n          \"ofType\": {\n            \"name\": \"TeamUpdateInput\"\n          }\n        }\n      },\n      {\n        \"name\": \"mapping\",\n        \"type\": {\n          \"name\": \"InheritanceEntityMapping\",\n          \"kind\": \"INPUT_OBJECT\",\n          \"ofType\": null\n        }\n      }\n    ]\n  }\n]"}

#### Step 7
Reasoning: `teamUpdate` takes `id` and `input` (TeamUpdateInput), and has a `name` field. Let's execute the update.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"mutation { teamUpdate(id: \"t-growth\", input: { name: \"Growth Pod\" }) { success team { id key name description private } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"teamUpdate\":{\"success\":true,\"team\":{\"id\":\"t-growth\",\"key\":\"GRW\",\"name\":\"Growth Pod\",\"description\":\"Coordinates the Q3 OKR pilot rollout across regional sales teams.\",\"private\":true}}}}"}

#### Step 8
Reasoning: Done. The team GRW (Growth) has been renamed to "Growth Pod". Note: There were two other teams with the same description (GRA - Growth Analytics, public; PTN - Growth Partnerships, private) — the only one matching "private AND key starts with GR AND description mentions Q3 OKR pilot" was GRW (private). GRA also starts with GR but is not private. So the match is unambiguous. I'll report back.

Done. In Linear, team **Growth** (key `GRW`) — the only private team whose key starts with "GR" and whose description mentions the Q3 OKR pilot rollout — is now named **Growth Pod**.

For clarity, two other teams share that same description but didn't match your criteria: Growth Analytics (`GRA`, public) and Growth Partnerships (`PTN`, private but key doesn't start with GR). Those were left untouched.
Command: 
Response: null

## Final answer
Done. In Linear, team **Growth** (key `GRW`) — the only private team whose key starts with "GR" and whose description mentions the Q3 OKR pilot rollout — is now named **Growth Pod**.

For clarity, two other teams share that same description but didn't match your criteria: Growth Analytics (`GRA`, public) and Growth Partnerships (`PTN`, private but key doesn't start with GR). Those were left untouched.

## State diff
- UPDATE teams `t-growth`: {"displayName": ["Growth", "Growth Pod"], "name": ["Growth", "Growth Pod"]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["t-growth"]}. Provisional outcome: correct. Provisional exposed facts: [].

Give your verdict for this trial.