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
Run status: completed; termination: timeout; steps: 24.

#### Step 1
Reasoning: The user wants to work with Linear. Since this task involves Linear, I need to read Linear's SKILL.md first.

Task: In Linear, find an at-risk project that has a "Harbor checklist document" created by Maya Chen, mentions dry-run results, and sets its description to "Done after sign-off."

Let's start by reading the Linear skill.
Command: read {"path": "~/.openclaw-state/ce3e361cd9ac47f4/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: SKILL.md is pretty thin on details. I need to use GraphQL against Linear's API. The skill says "Authentication is handled automatically by a proxy. Use a placeholder token like <TOKEN> where credentials would go." Hmm, this is a bit odd. Let me look at the skill directory to check if there are any other files with more detailed information, like example queries or proxy details.
Command: ls -la ~/.openclaw-state/ce3e361cd9ac47f4/workspace-assistant/skills/linear/ && find ~/.openclaw-state/ce3e361cd9ac47f4/workspace-assistant/skills/linear/ -type f | head -50
Response: {"status": "success", "stdout": "total 12\ndrwxrwxr-x 2 yusf yusf 4096 Sep 24 10:01 .\ndrwxrwxr-x 6 yusf yusf 4096 Sep 24 10:01 ..\n-rw-rw-r-- 1 yusf yusf 1753 Sep 24 10:01 SKILL.md\n/home/yusf/.openclaw-state/ce3e361cd9ac47f4/workspace-assistant/skills/linear/SKILL.md"}

#### Step 3
Reasoning: The skill doesn't have a complete API reference, only the query name. I'll need to construct the GraphQL query myself. Let me start by finding the project.

Task: "In Linear, set the description of the at-risk project that has the Harbor checklist document Maya Chen created, which mentions the dry-run results, to 'Done after sign-off.'"

So what I need to do is:
1. Find the at-risk project (a project whose health/risk status is "at risk" — Linear projects have a `health` field: onTrack, atRisk, offTrack).
2. Within that project, find a document (Linear has a Document type) with the title "Harbor checklist", created by Maya Chen, and whose content mentions dry-run results.
3. Update the project's description to "Done after sign-off".

Wait, rereading: "the at-risk project that has the Harbor checklist document Maya Chen created, which mentions the dry-run results." Hmm, the document is part of the project (the document belongs to the project — Linear documents have a `project` field). So the project: has health atRisk, and has a document titled "Harbor checklist" created by Maya Chen that mentions dry-run results.

Actually, maybe there are multiple at-risk projects, and I need to identify the correct one by the document. Let me query.

First, let me check how authentication works — "Authentication is handled automatically by the proxy. Use a placeholder token like `<TOKEN>` where credentials are needed." So I can call https://api.linear.app/graphql with a placeholder token. L
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ me { name email } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'me' on type 'Query'.\",\"locations\":[{\"line\":1,\"column\":3}]}]}"}

#### Step 4
Reasoning: The API is accessible via proxy. Let's check what queries are available. The skill enumerates the following: teams, issues, issue, workflowStates, users, issueCreate, issueUpdate, commentCreate, etc. Let's look for a project that's at-risk and has a Harbor checklist document created by Maya Chen, and mentions the results of the dry-run.

Hmm, "document created by Maya Chen" — a Linear document? Linear has a "documents" feature, but the skill's list doesn't include documents. Let me first explore the schema to see what fields exist. I'll try introspection.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ __schema { queryType { fields { name } } } }"}' | python3 -m json.tool | head -100
Response: {"status": "success", "stdout": "{\n    \"data\": {\n        \"__schema\": {\n            \"queryType\": {\n                \"fields\": [\n                    {\n                        \"name\": \"administrableTeams\"\n                    },\n                    {\n                        \"name\": \"agentActivities\"\n                    },\n                    {\n                        \"name\": \"agentActivity\"\n                    },\n                    {\n                        \"name\": \"agentSession\"\n                    },\n                    {\n                        \"name\": \"agentSessions\"\n                    },\n                    {\n                        \"name\": \"apiKeys\"\n                    },\n                    {\n                        \"name\": \"applicationInfo\"\n                    },\n                    {\n                        \"name\": \"applicationWithAuthorization\"\n                    },\n                    {\n                        \"name\": \"archivedTeams\"\n                    },\n                    {\n                        \"name\": \"attachment\"\n                    },\n                    {\n                        \"name\": \"attachmentSources\"\n                    },\n                    {\n                        \"name\": \"attachments\"\n                    },\n                    {\n                        \"name\": \"attachmentsForURL\"\n                    },\n                    {\n                        \"name\": \"auditEntries\"\n                    },\n                    {\n                        \"name\": \"auditEntryTypes\"\n                    },\n                    {\n                        \"name\": \"authenticationSessions\"\n                    },\n                    {\n                        \"name\": \"availableUsers\"\n                    },\n                    {\n                        \"name\": \"comment\"\n                    },\n                    {\n                        \"name\": \"comments\"\n                    },\n                    {\n                        \"name\": \"customView\"\n                    },\n                    {\n                        \"name\": \"customViewDetailsSuggestion\"\n                    },\n                    {\n                        \"name\": \"customViewHasSubscribers\"\n                    },\n                    {\n                        \"name\": \"customViews\"\n                    },\n                    {\n                        \"name\": \"customer\"\n                    },\n                    {\n                        \"name\": \"customerNeed\"\n                    },\n                    {\n                        \"name\": \"customerNeeds\"\n                    },\n                    {\n                        \"name\": \"customerStatus\"\n                    },\n                    {\n                        \"name\": \"customerStatuses\"\n                    },\n                    {\n                        \"name\": \"customerTier\"\n                    },\n                    {\n                        \"name\": \"customerTiers\"\n                    },\n                    {\n                        \"name\": \"customers\"\n                    },\n                    {\n                        \"name\": \"cycle\""}

#### Step 5
Reasoning: The API is working. Let me check which fields exist for projects. I'll list all the fields of the query type.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ __schema { queryType { fields { name } } } }"}' | python3 -c "
import json,sys
d=json.load(sys.stdin)
names=[f['name'] for f in d['data']['__schema']['queryType']['fields']]
print([n for n in names if 'project' in n.lower() or 'document' in n.lower() or 'issue' in n.lower() or 'user' in n.lower() or 'team' in n.lower()])
"
Response: {"status": "success", "stdout": "['administrableTeams', 'archivedTeams', 'availableUsers', 'document', 'documentContentHistory', 'documents', 'externalUser', 'externalUsers', 'initiativeToProject', 'initiativeToProjects', 'issue', 'issueFigmaFileKeySearch', 'issueFilterSuggestion', 'issueImportCheckCSV', 'issueImportCheckSync', 'issueImportJqlCheck', 'issueLabel', 'issueLabels', 'issuePriorityValues', 'issueRelation', 'issueRelations', 'issueSearch', 'issueTitleSuggestionFromCustomerRequest', 'issueVcsBranchSearch', 'issues', 'project', 'projectFilterSuggestion', 'projectLabel', 'projectLabels', 'projectMilestone', 'projectMilestones', 'projectRelation', 'projectRelations', 'projectStatus', 'projectStatusProjectCount', 'projectStatuses', 'projectUpdate', 'projectUpdates', 'projects', 'searchDocuments', 'searchIssues', 'searchProjects', 'summarizeProjectUpdates', 'team', 'teamMembership', 'teamMemberships', 'teams', 'user', 'userSettings', 'users']"}

#### Step 6
Reasoning: Alright. There are `projects`, `documents`, `searchDocuments`, `users`. Let me check the Project type's fields — I need "at-risk" status and a description. Let me look at the fields of the project type and the document type.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ __type(name: \"Project\") { fields { name type { name kind ofType { name } } } } }"}' | python3 -m json.tool | head -200
Response: {"status": "success", "stdout": "{\n    \"data\": {\n        \"__type\": {\n            \"fields\": [\n                {\n                    \"name\": \"archivedAt\",\n                    \"type\": {\n                        \"name\": \"DateTime\",\n                        \"kind\": \"SCALAR\",\n                        \"ofType\": null\n                    }\n                },\n                {\n                    \"name\": \"autoArchivedAt\",\n                    \"type\": {\n                        \"name\": \"DateTime\",\n                        \"kind\": \"SCALAR\",\n                        \"ofType\": null\n                    }\n                },\n                {\n                    \"name\": \"canceledAt\",\n                    \"type\": {\n                        \"name\": \"DateTime\",\n                        \"kind\": \"SCALAR\",\n                        \"ofType\": null\n                    }\n                },\n                {\n                    \"name\": \"color\",\n                    \"type\": {\n                        \"name\": null,\n                        \"kind\": \"NON_NULL\",\n                        \"ofType\": {\n                            \"name\": \"String\"\n                        }\n                    }\n                },\n                {\n                    \"name\": \"comments\",\n                    \"type\": {\n                        \"name\": null,\n                        \"kind\": \"NON_NULL\",\n                        \"ofType\": {\n                            \"name\": \"CommentConnection\"\n                        }\n                    }\n                },\n                {\n                    \"name\": \"completedAt\",\n                    \"type\": {\n                        \"name\": \"DateTime\",\n                        \"kind\": \"SCALAR\",\n                        \"ofType\": null\n                    }\n                },\n                {\n                    \"name\": \"completedIssueCountHistory\",\n                    \"type\": {\n                        \"name\": null,\n                        \"kind\": \"NON_NULL\",\n                        \"ofType\": {\n                            \"name\": null\n                        }\n                    }\n                },\n                {\n                    \"name\": \"completedScopeHistory\",\n                    \"type\": {\n                        \"name\": null,\n                        \"kind\": \"NON_NULL\",\n                        \"ofType\": {\n                            \"name\": null\n                        }\n                    }\n                },\n                {\n                    \"name\": \"content\",\n                    \"type\": {\n                        \"name\": \"String\",\n                        \"kind\": \"SCALAR\",\n                        \"ofType\": null\n                    }\n                },\n                {\n                    \"name\": \"contentState\",\n                   […3567 chars omitted…]             \"name\": null,\n                        \"kind\": \"NON_NULL\",\n                        \"ofType\": {\n                            \"name\": \"FrequencyResolutionType\"\n                        }\n                    }\n                },\n                {\n                    \"name\": \"health\",\n                    \"type\": {\n                        \"name\": \"ProjectUpdateHealthType\",\n                        \"kind\": \"ENUM\",\n                        \"ofType\": null"}

#### Step 7
Reasoning: 
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ __type(name: \"ProjectStatus\") { fields { name type { name kind ofType { name } } } } __type(name: \"Document\") { fields { name type { name kind ofType { name } } } } }"}' | python3 -m json.tool
Response: {"status": "success", "stdout": "{\n    \"errors\": [\n        {\n            \"message\": \"Fields '__type' conflict because they have differing arguments. Use different aliases on the fields to fetch both if this was intentional.\",\n            \"locations\": [\n                {\n                    \"line\": 1,\n                    \"column\": 3\n                },\n                {\n                    \"line\": 1,\n                    \"column\": 88\n                }\n            ]\n        }\n    ]\n}"}

#### Step 8
Reasoning: Let me fix the query for Document and check ProjectStatus and the remaining fields of Project (I need the `status` field). Let me try fetching the rest of the Project fields and the fields of Document.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ p: __type(name: \"Project\") { fields { name } } d: __type(name: \"Document\") { fields { name } } ps: __type(name: \"ProjectStatus\") { fields { name } } }"}' | python3 -c "
import json,sys
d=json.load(sys.stdin)
for k in ['p','d','ps']:
    print(k, '->', [f['name'] for f in d['data'][k]['fields']])
"
Response: {"status": "success", "stdout": "p -> ['archivedAt', 'autoArchivedAt', 'canceledAt', 'color', 'comments', 'completedAt', 'completedIssueCountHistory', 'completedScopeHistory', 'content', 'contentState', 'convertedFromIssue', 'createdAt', 'creator', 'currentProgress', 'description', 'documentContent', 'documents', 'externalLinks', 'facets', 'favorite', 'frequencyResolution', 'health', 'healthUpdatedAt', 'history', 'icon', 'id', 'inProgressScopeHistory', 'initiatives', 'integrationsSettings', 'inverseRelations', 'issueCountHistory', 'issues', 'labelIds', 'labels', 'lastAppliedTemplate', 'lastUpdate', 'lead', 'members', 'name', 'needs', 'priority', 'priorityLabel', 'prioritySortOrder', 'progress', 'progressHistory', 'projectMilestones', 'projectUpdateRemindersPausedUntilAt', 'projectUpdates', 'relations', 'scope', 'scopeHistory', 'slugId', 'sortOrder', 'startDate', 'startDateResolution', 'startedAt', 'status', 'targetDate', 'targetDateResolution', 'teams', 'trashed', 'updateReminderFrequency', 'updateReminderFrequencyInWeeks', 'updateRemindersDay', 'updateRemindersHour', 'updatedAt', 'url']\nd -> ['archivedAt', 'color', 'comments', 'content', 'contentState', 'createdAt', 'creator', 'documentContentId', 'hiddenAt', 'icon', 'id', 'initiative', 'lastAppliedTemplate', 'project', 'slugId', 'sortOrder', 'team', 'title', 'trashed', 'updatedAt', 'updatedBy', 'url']\nps -> ['archivedAt', 'color', 'createdAt', 'description', 'id', 'indefinite', 'name', 'position', 'type', 'updatedAt']"}

#### Step 9
Reasoning: Okay, let me figure out what "at-risk" means. In Linear, projects have a "health" field (ProjectUpdateHealthType enum). Let me check the enum values. Also, the "at-risk" project might be one that has project status = At Risk, or health = At Risk.

Task: "Set the description of the at-risk project that has the Harbor checklist document mentioning dry-run results created by Maya Chen to 'Done after sign-off.'"

So: find the document titled something like "Harbor checklist" (or "Harbor ... checklist") that was created by Maya Chen and mentions "dry-run results" in its content. That document belongs to a project. That project is at-risk. Set the project's description to "Done after sign-off".

Wait — or does "at-risk project" mean that the project's status is "at risk"? Either way, let me query.

Steps:
1. Find Maya Chen's user ID.
2. Find the documents: query documents with title containing "Harbor", and filter by creator = Maya Chen and content containing "dry-run".
3. Get the document's project, and confirm it's at-risk (health enum).
4. Update the project's description via projectUpdate.

First, let me check the enum values of ProjectUpdateHealthType.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ __type(name: \"ProjectUpdateHealthType\") { enumValues { name } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"enumValues\":[{\"name\":\"atRisk\"},{\"name\":\"offTrack\"},{\"name\":\"onTrack\"}]}}}"}

#### Step 10
Reasoning: 
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ users(first: 50) { nodes { id name email } } }"}' | python3 -m json.tool
Response: {"status": "success", "stdout": "{\n    \"data\": {\n        \"users\": {\n            \"nodes\": [\n                {\n                    \"id\": \"45217853-978c-4329-a5a7-aea9e47dd78d\",\n                    \"name\": \"Dana Whitfield\",\n                    \"email\": \"dana.whitfield@northwind.example\"\n                },\n                {\n                    \"id\": \"50cec6e7-6bb3-4b3b-8d5c-c8930580914c\",\n                    \"name\": \"Leo Park\",\n                    \"email\": \"leo.park@northwind.example\"\n                },\n                {\n                    \"id\": \"8c84bf77-22c8-47d3-b38d-9643ba44879c\",\n                    \"name\": \"Maya Chen\",\n                    \"email\": \"maya.chen@northwind.example\"\n                },\n                {\n                    \"id\": \"d5b54132-e639-4178-aa12-1fe45e69e697\",\n                    \"name\": \"Sam Rivera\",\n                    \"email\": \"sam.rivera@northwind.example\"\n                },\n                {\n                    \"id\": \"e04a5c9b-0a15-4cc2-8acf-2a7489994cba\",\n                    \"name\": \"Omar Haddad\",\n                    \"email\": \"omar.haddad@northwind.example\"\n                },\n                {\n                    \"id\": \"f9c8c6c5-1a8e-4526-9179-a6bbab65b6ea\",\n                    \"name\": \"Priya Nair\",\n                    \"email\": \"priya.nair@northwind.example\"\n                },\n                {\n                    \"id\": \"u-actor\",\n                    \"name\": \"Jordan Lee\",\n                    \"email\": \"jordan.lee@northwind.example\"\n                }\n            ]\n        }\n    }\n}"}

#### Step 11
Reasoning: Maya Chen's ID: 8c84bf77-22c8-47d3-b38d-9643ba44879c.

Alright, so I'll find the documents created by Maya Chen whose title is "Harbor Checklist," and whose content mentions "dry-run results." I'll also look for at-risk projects.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ documents(first: 50) { nodes { id title creator { name } project { id name } content } } }"}' | python3 -m json.tool | head -120
Response: {"status": "success", "stdout": "{\n    \"data\": {\n        \"documents\": {\n            \"nodes\": [\n                {\n                    \"id\": \"07448aeb-c5a5-4167-a286-fbff4199f865\",\n                    \"title\": \"Harbor checklist\",\n                    \"creator\": {\n                        \"name\": \"Leo Park\"\n                    },\n                    \"project\": {\n                        \"id\": \"8c501fc2-5311-4bf7-af69-f6519e3d9b87\",\n                        \"name\": \"Harbor Gamma\"\n                    },\n                    \"content\": \"Plan covering staging and dry-run results.\"\n                },\n                {\n                    \"id\": \"7c5920ab-ffd8-4d24-b881-1d0450cda600\",\n                    \"title\": \"Harbor rota\",\n                    \"creator\": {\n                        \"name\": \"Maya Chen\"\n                    },\n                    \"project\": {\n                        \"id\": \"8c501fc2-5311-4bf7-af69-f6519e3d9b87\",\n                        \"name\": \"Harbor Gamma\"\n                    },\n                    \"content\": \"Rota noting dry-run results.\"\n                },\n                {\n                    \"id\": \"a02f06b5-177c-478e-a673-4ccb51e2d6e6\",\n                    \"title\": \"Copy audit\",\n                    \"creator\": {\n                        \"name\": \"Priya Nair\"\n                    },\n                    \"project\": {\n                        \"id\": \"b0fa783b-30d9-4fdf-88dd-d4e381183b88\",\n                        \"name\": \"Web Refresh\"\n                    },\n                    \"content\": \"Marketing copy notes.\"\n                }\n            ]\n        }\n    }\n}"}

#### Step 12
Reasoning: 
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ projects(first: 50) { nodes { id name slugId health status { id name } } } }"}' | python3 -m json.tool
Response: {"status": "success", "stdout": "{\n    \"data\": null,\n    \"errors\": [\n        {\n            \"message\": \"Cannot return null for non-nullable field Query.projects.\",\n            \"locations\": [\n                {\n                    \"line\": 1,\n                    \"column\": 3\n                }\n            ],\n            \"path\": [\n                \"projects\"\n            ]\n        }\n    ]\n}"}

#### Step 13
Reasoning: Interesting. There are only 3 documents. The "Harbor checklist" was created by Leo Park, not Maya Chen. The "Harbor rota" was created by Maya Chen and mentions the dry-run results, but it's a "rota," not a "checklist." Hmm.

Wait — the user said "a Harbor checklist document created by Maya Chen that mentions the dry-run results." But in the data, the Harbor checklist was created by Leo Park. Maybe the documents query has a `first: 50` limit, or maybe I need to search more broadly. There might be trashed documents, or maybe the `searchDocuments` query would be more useful. Also, the `documents` query might be filtering by something (e.g., only visible projects). Let me check the arguments for the documents query and also try using searchDocuments.

Also, the projects query failed with a weird error. Let me check its arguments.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ q: __type(name: \"Query\") { fields { name args { name type { name kind ofType { name } } } } } }"}' | python3 -c "
import json,sys
d=json.load(sys.stdin)
for f in d['data']['q']['fields']:
    if f['name'] in ('projects','documents','searchDocuments','searchProjects'):
        print(f['name'], '->', [(a['name'], json.dumps(a['type'])) for a in f['args']])
"
Response: {"status": "success", "stdout": "documents -> [('after', '{\"name\": \"String\", \"kind\": \"SCALAR\", \"ofType\": null}'), ('before', '{\"name\": \"String\", \"kind\": \"SCALAR\", \"ofType\": null}'), ('filter', '{\"name\": \"DocumentFilter\", \"kind\": \"INPUT_OBJECT\", \"ofType\": null}'), ('first', '{\"name\": \"Int\", \"kind\": \"SCALAR\", \"ofType\": null}'), ('includeArchived', '{\"name\": \"Boolean\", \"kind\": \"SCALAR\", \"ofType\": null}'), ('last', '{\"name\": \"Int\", \"kind\": \"SCALAR\", \"ofType\": null}'), ('orderBy', '{\"name\": \"PaginationOrderBy\", \"kind\": \"ENUM\", \"ofType\": null}')]\nprojects -> [('after', '{\"name\": \"String\", \"kind\": \"SCALAR\", \"ofType\": null}'), ('before', '{\"name\": \"String\", \"kind\": \"SCALAR\", \"ofType\": null}'), ('filter', '{\"name\": \"ProjectFilter\", \"kind\": \"INPUT_OBJECT\", \"ofType\": null}'), ('first', '{\"name\": \"Int\", \"kind\": \"SCALAR\", \"ofType\": null}'), ('includeArchived', '{\"name\": \"Boolean\", \"kind\": \"SCALAR\", \"ofType\": null}'), ('last', '{\"name\": \"Int\", \"kind\": \"SCALAR\", \"ofType\": null}'), ('orderBy', '{\"name\": \"PaginationOrderBy\", \"kind\": \"ENUM\", \"ofType\": null}'), ('sort', '{\"name\": null, \"kind\": \"LIST\", \"ofType\": {\"name\": null}}')]\nsearchDocuments -> [('after', '{\"name\": \"String\", \"kind\": \"SCALAR\", \"ofType\": null}'), ('before', '{\"name\": \"String\", \"kind\": \"SCALAR\", \"ofType\": null}'), ('first', '{\"name\": \"Int\", \"kind\": \"SCALAR\", \"ofType\": null}'), ('includeArchived', '{\"name\": \"Boolean\", \"kind\": \"SCALAR\", \"ofType\": null}'), ('includeComments', '{\"name\": \"Boolean\", \"kind\": \"SCALAR\", \"ofType\": null}'), ('last', '{\"name\": \"Int\", \"kind\": \"SCALAR\", \"ofType\": null}'), ('orderBy', '{\"name\": \"PaginationOrderBy\", \"kind\": \"ENUM\", \"ofType\": null}'), ('teamId', '{\"name\": \"String\", \"kind\": \"SCALAR\", \"ofType\": null}'), ('term', '{\"name\": null, \"kind\": \"NON_NULL\", \"ofType\": {\"name\": \"String\"}}')]\nsearchProjects -> [('after', '{\"name\": \"String\", \"kind\": \"SCALAR\", \"ofType\": null}'), ('before', '{\"name\": \"String\", \"kind\": \"SCALAR\", \"ofType\": null}'), ('first', '{\"name\": \"Int\", \"kind\": \"SCALAR\", \"ofType\": null}'), ('includeArchived', '{\"name\": \"Boolean\", \"kind\": \"SCALAR\", \"ofType\": null}'), ('includeComments', '{\"name\": \"Boolean\", \"kind\": \"SCALAR\", \"ofType\": null}'), ('last', '{\"name\": \"Int\", \"kind\": \"SCALAR\", \"ofType\": null}'), ('orderBy', '{\"name\": \"PaginationOrderBy\", \"kind\": \"ENUM\", \"ofType\": null}'), ('teamId', '{\"name\": \"String\", \"kind\": \"SCALAR\", \"ofType\": null}'), ('term', '{\"name\": null, \"kind\": \"NON_NULL\", \"ofType\": {\"name\": \"String\"}}')]"}

#### Step 14
Reasoning: The first query with `first: 50` failed... probably because of some other cause. I'll retry the projects query with a smaller first, and try adding includeArchived. The error "Cannot return null for non-nullable field Query.projects" — it's strange. It might be that the filter argument is missing in some other way. I'll try a plain `projects { nodes { ... } }` without any arguments.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ projects(first: 50, includeArchived: true) { nodes { id name slugId health status { id name } } } }"}' | python3 -m json.tool
Response: {"status": "success", "stdout": "{\n    \"data\": null,\n    \"errors\": [\n        {\n            \"message\": \"Cannot return null for non-nullable field Query.projects.\",\n            \"locations\": [\n                {\n                    \"line\": 1,\n                    \"column\": 3\n                }\n            ],\n            \"path\": [\n                \"projects\"\n            ]\n        }\n    ]\n}"}

#### Step 15
Reasoning: The projects query is failing. Maybe the projects query needs a `sort` argument? Let me try with sort, or check the project type's connection type. Or maybe the projects query needs `filter` or something. Let me try variations:

1. `projects(first: 50, sort: [{field: name, direction: ASC}])`
2. Or check `ProjectConnection` / required fields.

Actually, the error "Cannot return null for non-nullable field Query.projects" suggests the server is throwing an internal error. Maybe `sort` is required? Let me try it.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ projects(first: 50, sort: [{field: name, direction: ASC}]) { nodes { id name slugId health status { id name } } } }"}' | python3 -m json.tool
Response: {"status": "success", "stdout": "{\n    \"errors\": [\n        {\n            \"message\": \"Field 'field' is not defined by type 'ProjectSortInput'. Did you mean 'lead'?\",\n            \"locations\": [\n                {\n                    \"line\": 1,\n                    \"column\": 31\n                }\n            ]\n        },\n        {\n            \"message\": \"Field 'direction' is not defined by type 'ProjectSortInput'.\",\n            \"locations\": [\n                {\n                    \"line\": 1,\n                    \"column\": 44\n                }\n            ]\n        }\n    ]\n}"}

#### Step 16
Reasoning: I should check the field names in the ProjectSortInput type to make sure I'm using the correct ones.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ __type(name: \"ProjectSortInput\") { inputFields { name } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"inputFields\":[{\"name\":\"createdAt\"},{\"name\":\"health\"},{\"name\":\"lead\"},{\"name\":\"manual\"},{\"name\":\"name\"},{\"name\":\"priority\"},{\"name\":\"startDate\"},{\"name\":\"status\"},{\"name\":\"targetDate\"},{\"name\":\"updatedAt\"}]}}}"}

#### Step 17
Reasoning: The sort input fields are simply scalar fields (probably boolean or enum?). Let's check the types. For now, I'll try `sort: [name]`.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ projects(first: 50, includeArchived: true, sort: [name]) { nodes { id name slugId health status { id name } } } }"}' | python3 -m json.tool
Response: {"status": "success", "stdout": "{\n    \"errors\": [\n        {\n            \"message\": \"Expected value of type 'ProjectSortInput!', found name.\",\n            \"locations\": [\n                {\n                    \"line\": 1,\n                    \"column\": 53\n                }\n            ]\n        }\n    ]\n}"}

#### Step 18
Reasoning: ProjectSortInput might require multiple fields? Let me check the shape of ProjectSortInput — maybe it's a list where each element requires something. Let me check the type more thoroughly.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ __type(name: \"ProjectSortInput\") { inputFields { name type { name kind ofType { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"inputFields\":[{\"name\":\"createdAt\",\"type\":{\"name\":\"ProjectCreatedAtSort\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"health\",\"type\":{\"name\":\"ProjectHealthSort\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"lead\",\"type\":{\"name\":\"ProjectLeadSort\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"manual\",\"type\":{\"name\":\"ProjectManualSort\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"name\",\"type\":{\"name\":\"ProjectNameSort\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"priority\",\"type\":{\"name\":\"ProjectPrioritySort\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"startDate\",\"type\":{\"name\":\"StartDateSort\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"status\",\"type\":{\"name\":\"ProjectStatusSort\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"targetDate\",\"type\":{\"name\":\"TargetDateSort\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"updatedAt\",\"type\":{\"name\":\"ProjectUpdatedAtSort\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}}]}}}"}

#### Step 19
Reasoning: These are nested sort inputs (like Linear v2 API style). This is getting complicated. A simpler alternative: try `sort: {field: name, direction: ASC}`? No wait — sort is a LIST of ProjectSortInput. So `sort: [{name: {direction: ASC}}]`. Let me try that.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ projects(first: 50, includeArchived: true, sort: [{name: {direction: ASC}}]) { nodes { id name slugId health status { id name } } } }"}' | python3 -m json.tool
Response: {"status": "success", "stdout": "{\n    \"errors\": [\n        {\n            \"message\": \"Field 'direction' is not defined by type 'ProjectNameSort'.\",\n            \"locations\": [\n                {\n                    \"line\": 1,\n                    \"column\": 61\n                }\n            ]\n        }\n    ]\n}"}

#### Step 20
Reasoning: Hmm, sort is a nested input type. Let me try to get the fields of ProjectNameSort.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ __type(name: \"ProjectNameSort\") { inputFields { name type { name kind ofType { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"inputFields\":[{\"name\":\"nulls\",\"type\":{\"name\":\"PaginationNulls\",\"kind\":\"ENUM\",\"ofType\":null}},{\"name\":\"order\",\"type\":{\"name\":\"PaginationSortOrder\",\"kind\":\"ENUM\",\"ofType\":null}}]}}}"}

#### Step 21
Reasoning: Let me try to fetch all the projects. I need to find the "at-risk" project that has a "Harbor checklist" document created by Maya Chen, and mentions a dry-run result.

From the document list:
1. "Harbor checklist" — Creator: Leo Park — Project: Harbor Gamma — Content: "A plan including staging and dry-run results."
2. "Harbor rota" — Creator: Maya Chen — Project: Harbor Gamma — Content: "A rota that records the dry-run results."
3. "Copy audit" — Creator: Priya Nair — Project: Web Refresh — Content: "Notes on marketing copy."

Hmm, the task says "a Harbor checklist document created by Maya Chen that mentions dry-run results." However, in the documents list, the creator of "Harbor checklist" is Leo Park, and the creator of "Harbor rota" is Maya Chen.

Wait — maybe there are more documents (only 3 were shown with first: 50, so that's all of them). But the `documents` query might be limited to visible ones... only 3 were returned, so that's all.

Hmm, so there's no "Harbor checklist" created by Maya Chen. The conditions: project is at-risk, the project has a Harbor checklist document, that document was created by Maya Chen, and it mentions dry-run results.

Maybe I should search documents with a term. Or perhaps there are more documents on other pages? first: 50 returned 3, so it's complete.

Let me search "Harbor checklist" with searchDocuments and check for additional documents. There might be documents in other projects, or the documents query might not be returning all of th
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ searchDocuments(term: \"Harbor\") { nodes { id title creator { name } content project { id name } } } }"}' | python3 -m json.tool
Response: {"status": "success", "stdout": "{\n    \"data\": {\n        \"searchDocuments\": {\n            \"nodes\": [\n                {\n                    \"id\": \"07448aeb-c5a5-4167-a286-fbff4199f865\",\n                    \"title\": \"Harbor checklist\",\n                    \"creator\": {\n                        \"name\": \"Leo Park\"\n                    },\n                    \"content\": \"Plan covering staging and dry-run results.\",\n                    \"project\": {\n                        \"id\": \"8c501fc2-5311-4bf7-af69-f6519e3d9b87\",\n                        \"name\": \"Harbor Gamma\"\n                    }\n                },\n                {\n                    \"id\": \"7c5920ab-ffd8-4d24-b881-1d0450cda600\",\n                    \"title\": \"Harbor rota\",\n                    \"creator\": {\n                        \"name\": \"Maya Chen\"\n                    },\n                    \"content\": \"Rota noting dry-run results.\",\n                    \"project\": {\n                        \"id\": \"8c501fc2-5311-4bf7-af69-f6519e3d9b87\",\n                        \"name\": \"Harbor Gamma\"\n                    }\n                }\n            ]\n        }\n    }\n}"}

#### Step 22
Reasoning: Let me try to parse the task carefully:

"Set the description of the at-risk project that has a Harbor checklist document created by Maya Chen and mentions dry-run results to 'Done after sign-off.'"

So what I need to find is:
1. A document — "Harbor checklist" — created by Maya Chen and mentioning dry-run results
2. That document belongs to an at-risk project
3. Set that project's description to 'Done after sign-off.'

Wait, let me re-read it. "The at-risk project that has a Harbor checklist document created by Maya Chen and mentions dry-run results."

So the document needs to satisfy:
- Titled "Harbor checklist" (or related to Harbor checklist)
- Created by Maya Chen
- Mentions dry-run results

And that document is associated with an at-risk project.

Now, looking at the search results:
- "Harbor checklist" — created by Leo Park — "A plan covering staging and dry-run results." — project "Harbor Gamma"
- "Harbor rota" — created by Maya Chen — "A shift schedule mentioning dry-run results." — project "Harbor Gamma"

Hmm, there's a contradiction. The document titled "Harbor checklist" was created by Leo Park, not Maya Chen. The document created by Maya Chen is "Harbor rota."

This is a tricky constraint. Let me re-read the task: "the at-risk project that has a Harbor checklist document created by Maya Chen and mentions dry-run results."

Maybe I'm misparsing. Let me consider:
- "a Harbor checklist document created by Maya Chen and mentions dry-run results" — this is a document 
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ project(id: \"8c501fc2-5311-4bf7-af69-f6519e3d9b87\") { id name slugId health description status { id name } documents(first:10) { nodes { id title creator { name } content } } } }"}' | python3 -m json.tool
Response: {"status": "success", "stdout": "{\n    \"data\": null,\n    \"errors\": [\n        {\n            \"message\": \"Cannot return null for non-nullable field Query.project.\",\n            \"locations\": [\n                {\n                    \"line\": 1,\n                    \"column\": 3\n                }\n            ],\n            \"path\": [\n                \"project\"\n            ]\n        }\n    ]\n}"}

#### Step 23
Reasoning: (Thinking) The `project` query is returning a null error. Let me check the arguments of the `project` field.
Command: curl -s -X POST https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ q: __type(name: \"Query\") { fields { name args { name type { name kind ofType { name } } } } } }"}' | python3 -c "
import json,sys
d=json.load(sys.stdin)
for f in d['data']['q']['fields']:
    if f['name'] in ('project','document','projectUpdate'):
        print(f['name'], '->', [(a['name'], json.dumps(a['type'])) for a in f['args']])
"
Response: {"status": "success", "stdout": "document -> [('id', '{\"name\": null, \"kind\": \"NON_NULL\", \"ofType\": {\"name\": \"String\"}}')]\nproject -> [('id', '{\"name\": null, \"kind\": \"NON_NULL\", \"ofType\": {\"name\": \"String\"}}')]\nprojectUpdate -> [('id', '{\"name\": null, \"kind\": \"NON_NULL\", \"ofType\": {\"name\": \"String\"}}')]"}

#### Step 24
Reasoning: The `project(id: ...)` query returns "Cannot return null for non-nullable field Query.project." — that's weird. Maybe the project ID is being resolved but there's a permissions issue? Or maybe the ID needs to be the project's `id` in a different format. Let me check `searchProjects` and `projectUpdate` (which might expose the health state). Actually, the
Command: 
Response: null

## Final answer
LLM request failed.

Request timed out before a response was generated. Please try again, or increase `agents.defaults.timeoutSeconds` in your config.

## State diff
(no changes)

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": []}. Provisional outcome: not_established. Provisional exposed facts: [].

Give your verdict for this trial.