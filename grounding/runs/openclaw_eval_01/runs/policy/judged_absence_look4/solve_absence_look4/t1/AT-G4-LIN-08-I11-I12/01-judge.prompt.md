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

# Trial of test `AT-G4-LIN-08-I11-I12` (linear)

Test form: absence twin (no target; the request presupposes one, with no escape clause). Target present: no.

## Request given to the solver
Set the priority of the 3-point sub-issue of MOB-42 due on October 15 to High.

## Candidates
### Reference r1 (what the request asks to act on); records live in `issues`
- No target: no record meets this reference.
- DECOY `i-mob-51` (fact `A:Issue.estimate`, family F7): Same parent (MOB-42) and same due date, but its estimate is 2, not 3.
  record: {"id": "i-mob-51", "identifier": "MOB-51", "title": "Fix Apple Pay sheet copy", "teamId": "t-mob", "stateId": "t-mob-st-1", "creatorId": "u-actor", "priority": 4.0, "priorityLabel": "Low", "number": 51.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "estimate": 2, "dueDate": "2026-10-15", "parentId": "i-mob-42"}
- DECOY `i-mob-52` (fact `A:Issue.estimate`, family F1): Same parent and due date, and its priority is Medium (3), but its estimate is 5, not 3.
  record: {"id": "i-mob-52", "identifier": "MOB-52", "title": "Fix Apple Pay sheet analytics", "teamId": "t-mob", "stateId": "t-mob-st-1", "creatorId": "u-actor", "priority": 3.0, "priorityLabel": "Medium", "number": 52.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "estimate": 5, "dueDate": "2026-10-15", "parentId": "i-mob-42"}

## Solver steps
Run status: completed; termination: done; steps: 19.

#### Step 1
Reasoning: The user is requesting a task in Linear: set the priority of a 3-point sub-issue of MOB-42 whose due date is October 15 to High.

First, let me read Linear's SKILL.md.
Command: read {"path": "~/.openclaw-state/5b86ca3b6e534ac2/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: I need to find MOB-42's sub-issue that has 3 points of effort (estimate), and whose deadline is October 15. Let me query the Linear GraphQL API.

First, I need to find the issue for MOB-42, then look for sub-issues whose estimate is 3 points and whose deadline is October 15 (2026-10-15).

Let me write a GraphQL query. The Linear API supports the following:

```graphql
query {
  issue(id: "MOB-42") {
    id
    title
    subIssues {
      nodes {
        id
        identifier
        title
        estimate
        dueDate
        priority
      }
    }
  }
}
```

After that, I'll update the matching issue with issueUpdate specifying priority: 2 (in Linear, priority 2 = High; the mapping is: 0 = No priority, 1 = Low, 2 = High, 3 = Urgent).

Let me run the query.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"query { issue(identifier: \"MOB-42\") { id identifier title subIssues(first: 50) { nodes { id identifier title estimate dueDate priority } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Unknown argument 'identifier' on field 'Query.issue'.\",\"locations\":[{\"line\":1,\"column\":15}]},{\"message\":\"Cannot query field 'subIssues' on type 'Issue'.\",\"locations\":[{\"line\":1,\"column\":59}]},{\"message\":\"Field 'issue' argument 'id' of type 'String!' is required, but it was not provided.\",\"locations\":[{\"line\":1,\"column\":9}]}]}"}

#### Step 3
Reasoning: The API schema is different. Let's check the schema: the `issue` query requires an `id` argument (String!) — probably accepts UUIDs. There's no subIssues field on Issue. Maybe there's `childIssues` or `relatedIssues`. Let me try introspecting.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ __schema { queryType { fields { name args { name type { name kind ofType { name } } } } } types { ... on __Type { name kind fields { name } } } } }"}' | head -c 6000
Response: {"status": "success", "stdout": "{\"data\":{\"__schema\":{\"queryType\":{\"fields\":[{\"name\":\"administrableTeams\",\"args\":[{\"name\":\"after\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"before\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"filter\",\"type\":{\"name\":\"TeamFilter\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"first\",\"type\":{\"name\":\"Int\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"includeArchived\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"last\",\"type\":{\"name\":\"Int\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"orderBy\",\"type\":{\"name\":\"PaginationOrderBy\",\"kind\":\"ENUM\",\"ofType\":null}}]},{\"name\":\"agentActivities\",\"args\":[{\"name\":\"after\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"before\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"filter\",\"type\":{\"name\":\"AgentActivityFilter\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"first\",\"type\":{\"name\":\"Int\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"includeArchived\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"last\",\"type\":{\"name\":\"Int\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"orderBy\",\"type\":{\"name\":\"PaginationOrderBy\",\"kind\":\"ENUM\",\"ofType\":null}}]},{\"name\":\"agentActivity\",\"args\":[{\"name\":\"id\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"String\"}}}]},{\"name\":\"agentSession\",\"args\":[{\"name\":\"id\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"String\"}}}]},{\"name\":\"agentSessions\",\"args\":[{\"name\":\"after\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"before\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"first\",\"type\":{\"name\":\"Int\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"includeArchived\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"last\",\"type\":{\"name\":\"Int\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"orderBy\",\"type\":{\"name\":\"PaginationOrderBy\",\"kind\":\"ENUM\",\"ofType\":null}}]},{\"name\":\"apiKeys\",\"args\":[{\"name\":\"after\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"before\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"first\",\"type\":{\"name\":\"Int\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"includeArchived\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"last\",\"type\":{\"name\":\"Int\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"orderBy\",\"type\":{\"name\":\"PaginationOrderBy\",\"kind\":\"ENUM\",\"ofType\":null}}]},{\"name\":\"applicationInfo\",\"args\":[{\"name\":\"clientId\",\"type\":{\"name\":null,\"kind\": […3774 chars omitted…] l}},{\"name\":\"orderBy\",\"type\":{\"name\":\"PaginationOrderBy\",\"kind\":\"ENUM\",\"ofType\":null}}]},{\"name\":\"customView\",\"args\":[{\"name\":\"id\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"String\"}}}]},{\"name\":\"customViewDetailsSuggestion\",\"args\":[{\"name\":\"filter\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"JSONObject\"}}},{\"name\":\"modelName\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}}]},{\"nam"}

#### Step 4
Reasoning: I need to investigate the issue query's arguments. Let me check the "issues" field and the Issue type, and try to find the childIssueRelations or a sub-issue field.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ queryTypeFields: __type(name: \"Query\") { fields { name args { name } } } }"}' | python3 -c "
import json,sys
d=json.load(sys.stdin)
for f in d['data']['queryTypeFields']['fields']:
    if f['name'] in ('issues','issue'):
        print(f['name'], [a['name'] for a in f['args']])
"
Response: {"status": "success", "stdout": "issue ['id']\nissues ['after', 'before', 'filter', 'first', 'includeArchived', 'last', 'orderBy', 'sort']"}

#### Step 5
Reasoning: `issues` supports filters. Let's check the fields of IssueFilter and the fields of Issue (sub-issues via relations? In Linear, parent/child is via the `subIssues` field — the error said "Cannot query field 'subIssues' on type 'Issue'". Maybe the field name is `childIssues` or `descendants`… let me introspect the Issue type.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ t: __type(name: \"Issue\") { fields { name } } }"}' | python3 -c "
import json,sys
d=json.load(sys.stdin)
print([f['name'] for f in d['data']['t']['fields']])
"
Response: {"status": "success", "stdout": "['activitySummary', 'addedToCycleAt', 'addedToProjectAt', 'addedToTeamAt', 'archivedAt', 'asksExternalUserRequester', 'asksRequester', 'assignee', 'attachments', 'autoArchivedAt', 'autoClosedAt', 'botActor', 'branchName', 'canceledAt', 'children', 'comments', 'documents', 'completedAt', 'createdAt', 'creator', 'customerTicketCount', 'cycle', 'delegate', 'description', 'descriptionState', 'documentContent', 'dueDate', 'estimate', 'externalUserCreator', 'favorite', 'formerAttachments', 'formerNeeds', 'history', 'id', 'identifier', 'incomingSuggestions', 'integrationSourceType', 'inverseRelations', 'labelIds', 'labels', 'lastAppliedTemplate', 'needs', 'number', 'parent', 'previousIdentifiers', 'priority', 'priorityLabel', 'prioritySortOrder', 'project', 'projectMilestone', 'reactionData', 'reactions', 'recurringIssueTemplate', 'relations', 'slaBreachesAt', 'slaHighRiskAt', 'slaMediumRiskAt', 'slaStartedAt', 'slaType', 'snoozedBy', 'snoozedUntilAt', 'sortOrder', 'sourceComment', 'startedAt', 'startedTriageAt', 'state', 'subIssueSortOrder', 'subscribers', 'suggestions', 'suggestionsGeneratedAt', 'syncedWith', 'team', 'title', 'trashed', 'triagedAt', 'updatedAt', 'url']"}

#### Step 6
Reasoning: Issue has `children` (sub-issues), `estimate`, and `dueDate`. Next, I need to find MOB-42. `issue` requires an id (uuid). Either search for issues with a filter that matches the identifier, or just query with a filter. Let me check the fields of IssueFilter.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ t: __type(name: \"IssueFilter\") { inputFields { name type { name kind ofType { name } } } } }"}' | python3 -m json.tool | head -100
Response: {"status": "success", "stdout": "{\n    \"data\": {\n        \"t\": {\n            \"inputFields\": [\n                {\n                    \"name\": \"addedToCycleAt\",\n                    \"type\": {\n                        \"name\": \"NullableDateComparator\",\n                        \"kind\": \"INPUT_OBJECT\",\n                        \"ofType\": null\n                    }\n                },\n                {\n                    \"name\": \"addedToCyclePeriod\",\n                    \"type\": {\n                        \"name\": \"CyclePeriodComparator\",\n                        \"kind\": \"INPUT_OBJECT\",\n                        \"ofType\": null\n                    }\n                },\n                {\n                    \"name\": \"ageTime\",\n                    \"type\": {\n                        \"name\": \"NullableDurationComparator\",\n                        \"kind\": \"INPUT_OBJECT\",\n                        \"ofType\": null\n                    }\n                },\n                {\n                    \"name\": \"and\",\n                    \"type\": {\n                        \"name\": null,\n                        \"kind\": \"LIST\",\n                        \"ofType\": {\n                            \"name\": null\n                        }\n                    }\n                },\n                {\n                    \"name\": \"archivedAt\",\n                    \"type\": {\n                        \"name\": \"NullableDateComparator\",\n                        \"kind\": \"INPUT_OBJECT\",\n                        \"ofType\": null\n                    }\n                },\n                {\n                    \"name\": \"assignee\",\n                    \"type\": {\n                        \"name\": \"NullableUserFilter\",\n                        \"kind\": \"INPUT_OBJECT\",\n                        \"ofType\": null\n                    }\n                },\n                {\n                    \"name\": \"attachments\",\n                    \"type\": {\n                        \"name\": \"AttachmentCollectionFilter\",\n                        \"kind\": \"INPUT_OBJECT\",\n                        \"ofType\": null\n                    }\n                },\n                {\n                    \"name\": \"autoArchivedAt\",\n                    \"type\": {\n                        \"name\": \"NullableDateComparator\",\n                        \"kind\": \"INPUT_OBJECT\",\n                        \"ofType\": null\n                    }\n                },\n                {\n                    \"name\": \"autoClosedAt\",\n                    \"type\": {\n                        \"name\": \"NullableDateComparator\",\n                        \"kind\": \"INPUT_OBJECT\",\n                        \"ofType\": null\n                    }\n                },\n                {\n                    \"name\": \"accumulatedStateUpdatedAt\",\n                    \"type\": {\n                        \"name\": \"NullableDateComparator\",\n                        \"kind\": \"INPUT_OBJECT\",\n                        \"ofType\": null\n                    }\n                },\n                {\n                    \"name\": \"canceledAt\",\n                    \"type\": {\n                        \"name\": \"NullableDateComparator\",\n                        \"kind\": \"INPUT_OBJECT\",\n                        \"ofType\": null\n                    }\n                },\n                {\n                    \"name\": \"children\",\n                    \"type\": {\n                        \"name\": \"IssueCollectionFilter\",\n                        \"kind\": \"INPUT_OBJECT\",\n                        \"ofType\": null"}

#### Step 7
Reasoning: I need to find the MOB-42 issue. There's probably a filter for the identifier. Let me try using a filter on identifier in `issues` to find MOB-42. I'll check whether IssueFilter has an `identifier` field.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ t: __type(name: \"IssueFilter\") { inputFields { name } } }"}' | python3 -c "
import json,sys
d=json.load(sys.stdin)
print([f['name'] for f in d['data']['t']['inputFields']])
"
Response: {"status": "success", "stdout": "['addedToCycleAt', 'addedToCyclePeriod', 'ageTime', 'and', 'archivedAt', 'assignee', 'attachments', 'autoArchivedAt', 'autoClosedAt', 'accumulatedStateUpdatedAt', 'canceledAt', 'children', 'comments', 'completedAt', 'createdAt', 'creator', 'customerCount', 'customerImportantCount', 'cycle', 'cycleTime', 'delegate', 'description', 'dueDate', 'estimate', 'hasBlockedByRelations', 'hasBlockingRelations', 'hasDuplicateRelations', 'hasSuggestedTeams', 'hasRelatedRelations', 'hasSuggestedAssignees', 'hasSuggestedLabels', 'hasSuggestedProjects', 'hasSuggestedRelatedIssues', 'hasSuggestedSimilarIssues', 'id', 'labels', 'lastAppliedTemplate', 'leadTime', 'needs', 'number', 'or', 'parent', 'priority', 'project', 'projectMilestone', 'reactions', 'recurringIssueTemplate', 'searchableContent', 'slaStatus', 'snoozedBy', 'snoozedUntilAt', 'sourceMetadata', 'startedAt', 'state', 'subscribers', 'suggestions', 'team', 'title', 'triageTime', 'triagedAt', 'updatedAt']"}

#### Step 8
Reasoning: I can filter issues by `parent` (probably a parent UUID) and `estimate`. First, I need to get the UUID of MOB-42. The `issue` query only accepts an `id` (UUID). I'll search for issues using the title/identifier. Let me try using `issues` with a filter to search for issues... there's `searchableContent` or `number`/`team`. An easier approach: use the teams query to find the team key "MOB" and search for issues with number = 42 on that team. Or maybe I can use a search query? Let me check if there's a `search` query field. Let me quickly check the list of query fields for "search".
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ t: __type(name: \"Query\") { fields { name } } }"}' | python3 -c "
import json,sys
d=json.load(sys.stdin)
print([f['name'] for f in d['data']['t']['fields'] if 'search' in f['name'].lower() or f['name'] in ('teams','team')])
"
Response: {"status": "success", "stdout": "['issueFigmaFileKeySearch', 'issueSearch', 'issueVcsBranchSearch', 'searchDocuments', 'searchIssues', 'searchProjects', 'semanticSearch', 'team', 'teams']"}

#### Step 9
Reasoning: There's `issueSearch`. Let's check its arguments, or more simply, find the MOB team and use the `issues` filter with `parent` or `searchableContent`. Actually, more simply: use the `searchIssues` or `issueSearch` fields. Let's check the arguments for `issueSearch`.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ t: __type(name: \"Query\") { fields { name args { name } } } }"}' | python3 -c "
import json,sys
d=json.load(sys.stdin)
for f in d['data']['t']['fields']:
    if f['name'] in ('issueSearch','searchIssues'):
        print(f['name'], [a['name'] for a in f['args']])
"
Response: {"status": "success", "stdout": "issueSearch ['after', 'before', 'filter', 'first', 'includeArchived', 'last', 'orderBy', 'query']\nsearchIssues ['after', 'before', 'filter', 'first', 'includeArchived', 'includeComments', 'last', 'orderBy', 'teamId', 'term']"}

#### Step 10
Reasoning: First, I'll search for the MOB-42 issue. I'll use searchIssues with the specified term, or try using issues with a filter on number/team. Let me try the simple approach: searchIssues with term "MOB-42".
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ searchIssues(term: \"MOB-42\", first: 10) { nodes { id identifier title team { key } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"searchIssues\":{\"nodes\":[{\"id\":\"i-mob-42\",\"identifier\":\"MOB-42\",\"title\":\"Checkout crash on launch\",\"team\":{\"key\":\"MOB\"}},{\"id\":\"i-mob-421\",\"identifier\":\"MOB-421\",\"title\":\"Checkout crash, enterprise follow-up\",\"team\":{\"key\":\"MOB\"}}]}}}"}

#### Step 11
Reasoning: Note: search returns both MOB-42 (id "i-mob-42") and MOB-421 (id "i-mob-421"). I need MOB-42, whose id is "i-mob-42". To avoid ambiguity, I'll use the id. Next, I'll fetch the children of MOB-42.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ issue(id: \"i-mob-42\") { id identifier title children(first: 50) { nodes { id identifier title estimate dueDate priority } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issue\":{\"id\":\"i-mob-42\",\"identifier\":\"MOB-42\",\"title\":\"Checkout crash on launch\",\"children\":{\"nodes\":[{\"id\":\"i-mob-51\",\"identifier\":\"MOB-51\",\"title\":\"Fix Apple Pay sheet copy\",\"estimate\":2.0,\"dueDate\":\"2026-10-15\",\"priority\":4.0},{\"id\":\"i-mob-52\",\"identifier\":\"MOB-52\",\"title\":\"Fix Apple Pay sheet analytics\",\"estimate\":5.0,\"dueDate\":\"2026-10-15\",\"priority\":3.0},{\"id\":\"i-mob-57\",\"identifier\":\"MOB-57\",\"title\":\"Polish saved-card search\",\"estimate\":5.0,\"dueDate\":\"2026-10-22\",\"priority\":4.0}]}}}}"}

#### Step 12
Reasoning: There are three sub-issues. Which one is "the 3-point sub-issue"? MOB-51 is 2 points, MOB-52 is 5 points, and MOB-57 is 5 points. Hmm, none of them are 3 points. Wait—maybe I should double-check. The user is saying "the 3-point sub-issue of MOB-42 that's due on October 15." None of the child issues show an estimate of 3. Let me check again... maybe there are more child issues beyond the 50 I fetched, or perhaps the estimates are in a different format. The estimates are 2.0, 5.0, 5.0. Hmm.

Wait—maybe "3-point" refers to something else, or there's a pagination issue. Let me query all child issues without a limit, or check totalCount.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ issue(id: \"i-mob-42\") { children(first: 100) { totalCount nodes { id identifier title estimate dueDate priority } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'totalCount' on type 'IssueConnection'.\",\"locations\":[{\"line\":1,\"column\":50}]}]}"}

#### Step 13
Reasoning: The connection type doesn't have totalCount? Unusual, but no problem. The first query returned 3 child issues. Let me check if there are more than 50 child issues — the first query used first:50 and got 3, so that's all of them.

Wait — the user asked for the "3-point subissue of MOB-42 with a due date of October 15." The estimates are 2.0, 5.0, 5.0. There's no 3-point one. Hmm. The estimates shown are 2.0 and 5.0. There's no 3-point subissue.

Hold on — maybe there are more child issues beyond the 50 items? No, only 3 were returned. But let me double-check: perhaps the child issues have their own child issues, or maybe MOB-421 is also relevant. The user clearly said "subissue of MOB-42." None of the child issues have an estimate of 3 points.

Hmm, let me reconsider. Maybe the priority values: the priority field returns 4.0, 3.0, 4.0. Linear's priorities: 0=No priority, 1=Urgent, 2=High, 3=Medium, 4=Low.

The user asked for the 3-point subissue with a due date of October 15. The child issues with a due date of October 15 are MOB-51 (2 points) and MOB-52 (5 points). There's no 3-point one.

Maybe I should check the child issues of MOB-42 more carefully — perhaps there are archived child issues, or ones that didn't show up in the list. Let me query with includeArchived. Actually, the Issue type's children field — let me check its arguments. Also, it's possible the estimate is stored differently. Let me check archived child issues too.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ t: __type(name: \"Issue\") { fields { name args { name } } } }"}' | python3 -c "
import json,sys
d=json.load(sys.stdin)
for f in d['data']['t']['fields']:
    if f['name'] in ('children','relations','incomingSuggestions'):
        print(f['name'], [a['name'] for a in f['args']])
"
Response: {"status": "success", "stdout": "children ['after', 'before', 'filter', 'first', 'includeArchived', 'last', 'orderBy']\nincomingSuggestions ['after', 'before', 'first', 'includeArchived', 'last', 'orderBy']\nrelations ['after', 'before', 'first', 'includeArchived', 'last', 'orderBy']"}

#### Step 14
Reasoning: MOB-52 is 5 points, and MOB-57 is also 5 points. I can't find any 3-point subtasks yet. The children might be paginated, and there could be more beyond the first 50 — I'll fetch the next page and also check the archived ones. Let me try querying with `after` using the last cursor.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ issue(id: \"i-mob-42\") { children(first: 50) { pageInfo { hasNextPage endCursor } nodes { id identifier title estimate dueDate priority } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issue\":{\"children\":{\"pageInfo\":{\"hasNextPage\":false,\"endCursor\":\"eyJmaWVsZCI6ICIyMDI2LTA2LTAxVDA5OjAwOjAwIiwgImlkIjogImktbW9iLTU3In0=\"},\"nodes\":[{\"id\":\"i-mob-51\",\"identifier\":\"MOB-51\",\"title\":\"Fix Apple Pay sheet copy\",\"estimate\":2.0,\"dueDate\":\"2026-10-15\",\"priority\":4.0},{\"id\":\"i-mob-52\",\"identifier\":\"MOB-52\",\"title\":\"Fix Apple Pay sheet analytics\",\"estimate\":5.0,\"dueDate\":\"2026-10-15\",\"priority\":3.0},{\"id\":\"i-mob-57\",\"identifier\":\"MOB-57\",\"title\":\"Polish saved-card search\",\"estimate\":5.0,\"dueDate\":\"2026-10-22\",\"priority\":4.0}]}}}}"}

#### Step 15
Reasoning: There are only 3 sub-issues (hasNextPage: false). The user is looking for "a sub-issue of MOB-42 with an estimate of 3 points that is due on October 15." However, among the children, there are none that have an estimate of 3.0 and are due on 2026-10-15:
- MOB-51: estimate 2, due 2026-10-15
- MOB-52: estimate 5, due 2026-10-15
- MOB-57: estimate 5, due 2026-10-22

Hmm. Maybe "3 points" means a different scale — Linear's estimates are usually in point units. Or maybe the sub-issue is nested (a sub-issue of a sub-issue)? Let me check the children of each child. Or maybe the estimate is a different value — perhaps the estimate field is displaying a multiplier. Let me check the grandchildren.

None of the direct sub-issues match estimate 3 + due Oct 15. Let me check nested children.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ a: issue(id: \"i-mob-51\") { children(first: 50) { nodes { id identifier title estimate dueDate priority } } } b: issue(id: \"i-mob-52\") { children(first: 50) { nodes { id identifier title estimate dueDate priority } } } c: issue(id: \"i-mob-57\") { children(first: 50) { nodes { id identifier title estimate dueDate priority } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"a\":{\"children\":{\"nodes\":[]}},\"b\":{\"children\":{\"nodes\":[]}},\"c\":{\"children\":{\"nodes\":[]}}}}"}

#### Step 16
Reasoning: None of the child issues have children. The direct child issues are as follows:
- MOB-51: estimate 2, due 2026-10-15
- MOB-52: estimate 5, due 2026-10-15
- MOB-57: estimate 5, due 2026-10-22

None of them have an estimate of 3. Hmm. The user said "a 3-point sub-issue of MOB-42 due October 15." Maybe "sub-issue" includes issues related via the "sub-issue" relation (in Linear, sub-issues can be linked from any team, and the `children` field should include those). But there were only 3 items. Wait — could the children filter be excluding archived ones by default? Let me try checking with includeArchived: true.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ issue(id: \"i-mob-42\") { children(first: 50, includeArchived: true) { nodes { id identifier title estimate dueDate priority } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issue\":{\"children\":{\"nodes\":[{\"id\":\"i-mob-51\",\"identifier\":\"MOB-51\",\"title\":\"Fix Apple Pay sheet copy\",\"estimate\":2.0,\"dueDate\":\"2026-10-15\",\"priority\":4.0},{\"id\":\"i-mob-52\",\"identifier\":\"MOB-52\",\"title\":\"Fix Apple Pay sheet analytics\",\"estimate\":5.0,\"dueDate\":\"2026-10-15\",\"priority\":3.0},{\"id\":\"i-mob-57\",\"identifier\":\"MOB-57\",\"title\":\"Polish saved-card search\",\"estimate\":5.0,\"dueDate\":\"2026-10-22\",\"priority\":4.0}]}}}}"}

#### Step 17
Reasoning: Hmm, MOB-42 only has 3 sub-issues, and none of them have an estimate of 3 with a due date of October 15th. The estimates are 2, 5, 5. Wait — "3-point sub-issue" — could the estimate be 3 for one of them? No, it's not. Let me check other MOB-42-like issues... maybe "i-mob-421" is a different issue. Or there might be another team with key MOB. The search only returned those.

Wait — maybe the estimate field is a number, and 3 points = estimate 3.0? Not present in the results. Could it be that the sub-issues are linked via relations rather than via children? Or maybe the estimates are displayed as "2.0" — hmm.

Let me recheck by filtering with estimate=3 and parent=i-mob-42. Or maybe the estimate of one of these issues has been changed. Let me query the issues filtered by parent id and estimate 3.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ issues(filter: { parent: { id: { eq: \"i-mob-42\" } }, estimate: { eq: 3 } }, first: 50) { nodes { id identifier title estimate dueDate priority } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[]}}}"}

#### Step 18
Reasoning: There is no sub-issue with a point value of 3 in MOB-42. The sub-issues are as follows:
- MOB-51: point value 2, deadline 2026-10-15
- MOB-52: point value 5, deadline 2026-10-15
- MOB-57: point value 5, deadline 2026-10-22

Neither of them has a point value of 3. The user asked for "the sub-issue with 3 points from MOB-42 whose deadline is October 15." There is no such sub-issue. Maybe the user is mistaken, or perhaps the "point value" is referring to something else. Could the point value have been changed recently? Should I check the history? Let me check the estimate history of these sub-issues. Or maybe it's a different issue — perhaps MOB-42 has a different sub-issue that I haven't found yet. Let me try searching all issues within the MOB team that have an estimate of 3 and a deadline of October 15.

No sub-issue of MOB-42 has an estimate of 3. Let me check the wider picture before concluding — maybe it's estimated elsewhere or was recently changed.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"{ issues(filter: { team: { key: { eq: \"MOB\" } }, estimate: { eq: 3 } }, first: 50) { nodes { id identifier title estimate dueDate parent { identifier } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[]}}}"}

#### Step 19
Reasoning: There is no issue with an estimate of 3 in the MOB team. The subtasks of MOB-42 are as follows:
- MOB-51: estimate 2, due 2026-10-15, priority 4 (urgent? Actually, Linear's priority is: 0=None, 1=Urgent, 2=High, 3=Medium, 4=Low)
- MOB-52: estimate 5, due 2026-10-15, priority 3 (Medium)
- MOB-57: estimate 5, due 2026-10-22, priority 4

There is no subtask with an estimate of 3 points. There are no nested subtasks either, and no archived ones either. I should report this discrepancy rather than guess. The user said "a subtask of MOB-42 with an estimate of 3 points and a due date of October 15." There is no subtask that satisfies both conditions. Two subtasks are due October 15 (estimates 2 and 5), and there is no subtask with an estimate of 3.

I should ask which one they're referring to, rather than updating the wrong issue. This is a case where "one missing judgment is preventing safe progress." Let me present the findings and confirm.

I checked MOB-42 ("Checkout crash on launch") and its sub-issues, but there's no sub-issue with a 3-point estimate. The three sub-issues are:

- **MOB-51** — Fix Apple Pay sheet copy — **2 pts**, due Oct 15
- **MOB-52** — Fix Apple Pay sheet analytics — **5 pts**, due Oct 15
- **MOB-57** — Polish saved-card search — **5 pts**, due Oct 22

I also checked for nested sub-issues and archived ones, and for any MOB issue estimated at 3 points — nothing. So either the estimate was changed, or the description doesn't quite line up.

Two sub-issues are
Command: 
Response: null

## Final answer
I checked MOB-42 ("Checkout crash on launch") and its sub-issues, but there's no sub-issue with a 3-point estimate. The three sub-issues are:

- **MOB-51** — Fix Apple Pay sheet copy — **2 pts**, due Oct 15
- **MOB-52** — Fix Apple Pay sheet analytics — **5 pts**, due Oct 15
- **MOB-57** — Polish saved-card search — **5 pts**, due Oct 22

I also checked for nested sub-issues and archived ones, and for any MOB issue estimated at 3 points — nothing. So either the estimate was changed, or the description doesn't quite line up.

Two sub-issues are due Oct 15 (MOB-51 and MOB-52). Which one should I set to High priority?

## State diff
(no changes)

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": []}. Provisional outcome: presented?. Provisional exposed facts: [].

Give your verdict for this trial.