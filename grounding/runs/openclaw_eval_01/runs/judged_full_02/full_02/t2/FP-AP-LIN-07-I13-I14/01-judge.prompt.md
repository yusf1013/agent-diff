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

# Trial of test `FP-AP-LIN-07-I13-I14` (linear)

Test form: fact probe. Target present: no.

## Request given to the solver
Rename the Growth team's document titled "Draft notes" that mentions the referral program pilot to "Referral pilot — launch notes". If there isn't one, just tell me.

## Candidates
### Reference r1 (what the request asks to act on); records live in `documents`
- No target: no record meets this reference.
- DECOY `d-team-f1` (fact `R:Document.teamId`, family F1): It has no team of its own; it's filed under the Customer Acquisition project instead.
  record: {"id": "d-team-f1", "title": "Draft notes", "content": "Draft notes on the referral program pilot rollout for Q4, including timeline and success metrics.", "creatorId": "u-actor", "updatedById": "u-actor", "projectId": "pr-growth", "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `d-team-f0` (fact `R:Document.teamId`, family F0): Same title and content, but it belongs to the Platform team, not Growth.
  record: {"id": "d-team-f0", "title": "Draft notes", "content": "Draft notes on the referral program pilot rollout for Q4, including timeline and success metrics.", "creatorId": "u-actor", "updatedById": "u-actor", "teamId": "t-platform", "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}

## Solver steps
Run status: completed; termination: done; steps: 14.

#### Step 1
Reasoning: The user wants to rename a Linear document. I need to read Linear's SKILL.md first.
Command: read {"path": "~/.openclaw-state/d9e17874954f4c93/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: The Linear skill doesn't list any document APIs at all. Linear does have a Documents feature. Let me check whether the API supports documents. The skill's API documentation only enumerates teams, issues, etc. But the user is asking about a document titled "Draft notes" that belongs to the Growth team.

The Linear API has document-related endpoints. I could check the schema, but... the skill's docs are limited. I might be able to run introspection, or just try querying documents. Let me try a GraphQL query against the Linear API using the placeholder token `<TOKEN>`.

Actually, according to the skill, authentication is handled automatically by the proxy, and I should use a placeholder token like `<TOKEN>`. So I should run curl with "Authorization: Bearer <TOKEN>" attached.

The Linear GraphQL API has a `document` query and a `documents` query (added around 2024). Let me give it a try:

```graphql
query {
  documents(filter: { title: { contains: "Draft notes" } }) {
    nodes {
      id
      title
      content
      team { key name }
    }
  }
}
```

Hmm, I'm not 100% sure about the filter syntax. Maybe I can just query all documents and filter on the client side. Let me start by introspecting to check whether a `documents` field exists on Query. I'll run a curl command.

First, let me try a simple query.
Command: curl -s -X POST https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"query { __schema { queryType { fields { name } } } }"}' | head -c 4000
Response: {"status": "success", "stdout": "{\"data\":{\"__schema\":{\"queryType\":{\"fields\":[{\"name\":\"administrableTeams\"},{\"name\":\"agentActivities\"},{\"name\":\"agentActivity\"},{\"name\":\"agentSession\"},{\"name\":\"agentSessions\"},{\"name\":\"apiKeys\"},{\"name\":\"applicationInfo\"},{\"name\":\"applicationWithAuthorization\"},{\"name\":\"archivedTeams\"},{\"name\":\"attachment\"},{\"name\":\"attachmentSources\"},{\"name\":\"attachments\"},{\"name\":\"attachmentsForURL\"},{\"name\":\"auditEntries\"},{\"name\":\"auditEntryTypes\"},{\"name\":\"authenticationSessions\"},{\"name\":\"availableUsers\"},{\"name\":\"comment\"},{\"name\":\"comments\"},{\"name\":\"customView\"},{\"name\":\"customViewDetailsSuggestion\"},{\"name\":\"customViewHasSubscribers\"},{\"name\":\"customViews\"},{\"name\":\"customer\"},{\"name\":\"customerNeed\"},{\"name\":\"customerNeeds\"},{\"name\":\"customerStatus\"},{\"name\":\"customerStatuses\"},{\"name\":\"customerTier\"},{\"name\":\"customerTiers\"},{\"name\":\"customers\"},{\"name\":\"cycle\"},{\"name\":\"cycles\"},{\"name\":\"document\"},{\"name\":\"documentContentHistory\"},{\"name\":\"documents\"},{\"name\":\"emailIntakeAddress\"},{\"name\":\"emoji\"},{\"name\":\"emojis\"},{\"name\":\"entityExternalLink\"},{\"name\":\"externalUser\"},{\"name\":\"externalUsers\"},{\"name\":\"failuresForOauthWebhooks\"},{\"name\":\"favorite\"},{\"name\":\"favorites\"},{\"name\":\"fetchData\"},{\"name\":\"initiative\"},{\"name\":\"initiativeRelation\"},{\"name\":\"initiativeRelations\"},{\"name\":\"initiativeToProject\"},{\"name\":\"initiativeToProjects\"},{\"name\":\"initiativeUpdate\"},{\"name\":\"initiativeUpdates\"},{\"name\":\"initiatives\"},{\"name\":\"integration\"},{\"name\":\"integrationHasScopes\"},{\"name\":\"integrationTemplate\"},{\"name\":\"integrationTemplates\"},{\"name\":\"integrations\"},{\"name\":\"integrationsSettings\"},{\"name\":\"issue\"},{\"name\":\"issueFigmaFileKeySearch\"},{\"name\":\"issueFilterSuggestion\"},{\"name\":\"issueImportCheckCSV\"},{\"name\":\"issueImportCheckSync\"},{\"name\":\"issueImportJqlCheck\"},{\"name\":\"issueLabel\"},{\"name\":\"issueLabels\"},{\"name\":\"issuePriorityValues\"},{\"name\":\"issueRelation\"},{\"name\":\"issueRelations\"},{\"name\":\"issueSearch\"},{\"name\":\"issueTitleSuggestionFromCustomerRequest\"},{\"name\":\"issueVcsBranchSearch\"},{\"name\":\"issues\"},{\"name\":\"notification\"},{\"name\":\"notificationSubscription\"},{\"name\":\"notificationSubscriptions\"},{\"name\":\"notifications\"},{\"name\":\"notificationsUnreadCount\"},{\"name\":\"organization\"},{\"name\":\"organizationDomainClaimRequest\"},{\"name\":\"organizationExists\"},{\"name\":\"organizationInvite\"},{\"name\":\"organizationInviteDetails\"},{\"name\":\"organizationInvites\"},{\"name\":\"organizationMeta\"},{\"name\":\"project\"},{\"name\":\"projectFilterSuggestion\"},{\"name\":\"projectLabel\"},{\"name\":\"projectLabels\"},{\"name\":\"projectMilestone\"},{\"name\":\"projectMilestones\"},{\"name\":\"projectRelation\"},{\"name\":\"projectRelations\"},{\"name\":\"projectStatus\"},{\"name\":\"projectStatusProjectCount\"},{\"name\":\"projectStatuses\"},{\"name\":\"projectUpdate\"},{\"name\":\"projectUpdates\"},{\"name\":\"projects\"},{\"name\":\"pushSubscriptionTest\"},{\"name\":\"rateLimitStatus\"},{\"name\":\"searchDocuments\"},{\"name\":\"searchIssues\"},{\"name\":\"searchProjects\"},{\"name\":\"semanticSearch\"},{\"name\":\"ssoUrlFromEmail\"},{\"name\":\"summarizeProjectUpdates\"},{\"name\":\"team\"},{\"name\":\"teamMembership\"},{\"name\":\"teamMemberships\"},{\"name\":\"teams\"},{\"name\":\"template\"},{\"name\":\"templates\"},{\"name\":\"templatesForIntegration\"},{\"name\":\"timeSchedule\"},{\"name\":\"timeSchedules\"},{\"name\":\"triageResponsibilities\"},{\"name\":\"triageResponsibility\"},{\"name\":\"user\"},{\"name\":\"userSettings\"},{\"name\":\"users\"},{\"name\":\"verifyGitHubEnterpriseServerInstallation\"},{\"name\":\"viewer\"},{\"name\":\"webhook\"},{\"name\":\"webhooks\"},{\"name\":\"workflowState\"},{\"name\":\"workflowStates\"}]}}}}"}

#### Step 3
Reasoning: The schema has `documents`, `searchDocuments`, and `document`. First let's look at the Growth team's documents. I'll try querying `teams` to find the Growth team, then query that team's `documents`.
Command: curl -s -X POST https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"query { teams { nodes { id name key } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"teams\":{\"nodes\":[{\"id\":\"t-growth\",\"name\":\"Growth\",\"key\":\"GRO\"},{\"id\":\"t-platform\",\"name\":\"Platform\",\"key\":\"PLA\"}]}}}"}

#### Step 4
Reasoning: I found the Growth team (t-growth). Next, let's search for the document titled "Draft notes" within that team. I'll use the searchDocuments query. Let me check the fields available on documents.
Command: curl -s -X POST https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"query { searchDocuments(query: \"Draft notes referral\") { nodes { id title description team { name key } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Unknown argument 'query' on field 'Query.searchDocuments'. Did you mean 'term'?\",\"locations\":[{\"line\":1,\"column\":25}]},{\"message\":\"Cannot query field 'description' on type 'DocumentSearchResult'.\",\"locations\":[{\"line\":1,\"column\":75}]},{\"message\":\"Field 'searchDocuments' argument 'term' of type 'String!' is required, but it was not provided.\",\"locations\":[{\"line\":1,\"column\":9}]}]}"}

#### Step 5
Reasoning: Let's check the searchDocuments field and the DocumentSearchResult type.
Command: curl -s -X POST https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"query { searchDocuments(term: \"referral\") { nodes { __typename ... on Document { id title description team { name key } } ... on Issue { id title } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Fragment cannot be spread here as objects of type 'DocumentSearchResult' can never be of type 'Document'.\",\"locations\":[{\"line\":1,\"column\":64}]},{\"message\":\"Cannot query field 'description' on type 'Document'.\",\"locations\":[{\"line\":1,\"column\":91}]},{\"message\":\"Fragment cannot be spread here as objects of type 'DocumentSearchResult' can never be of type 'Issue'.\",\"locations\":[{\"line\":1,\"column\":123}]}]}"}

#### Step 6
Reasoning: Let's check the schema of DocumentSearchResult and the Document type.
Command: curl -s -X POST https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"query { a: __type(name: \"DocumentSearchResult\") { fields { name } } b: __type(name: \"Document\") { fields { name type { name kind ofType { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"a\":{\"fields\":[{\"name\":\"archivedAt\"},{\"name\":\"color\"},{\"name\":\"comments\"},{\"name\":\"content\"},{\"name\":\"contentState\"},{\"name\":\"createdAt\"},{\"name\":\"creator\"},{\"name\":\"documentContentId\"},{\"name\":\"hiddenAt\"},{\"name\":\"icon\"},{\"name\":\"id\"},{\"name\":\"initiative\"},{\"name\":\"lastAppliedTemplate\"},{\"name\":\"metadata\"},{\"name\":\"project\"},{\"name\":\"slugId\"},{\"name\":\"sortOrder\"},{\"name\":\"team\"},{\"name\":\"title\"},{\"name\":\"trashed\"},{\"name\":\"updatedAt\"},{\"name\":\"updatedBy\"},{\"name\":\"url\"}]},\"b\":{\"fields\":[{\"name\":\"archivedAt\",\"type\":{\"name\":\"DateTime\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"color\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"comments\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"CommentConnection\"}}},{\"name\":\"content\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"contentState\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"createdAt\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"DateTime\"}}},{\"name\":\"creator\",\"type\":{\"name\":\"User\",\"kind\":\"OBJECT\",\"ofType\":null}},{\"name\":\"documentContentId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"hiddenAt\",\"type\":{\"name\":\"DateTime\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"icon\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"id\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"ID\"}}},{\"name\":\"initiative\",\"type\":{\"name\":\"Initiative\",\"kind\":\"OBJECT\",\"ofType\":null}},{\"name\":\"lastAppliedTemplate\",\"type\":{\"name\":\"Template\",\"kind\":\"OBJECT\",\"ofType\":null}},{\"name\":\"project\",\"type\":{\"name\":\"Project\",\"kind\":\"OBJECT\",\"ofType\":null}},{\"name\":\"slugId\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"String\"}}},{\"name\":\"sortOrder\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"Float\"}}},{\"name\":\"team\",\"type\":{\"name\":\"Team\",\"kind\":\"OBJECT\",\"ofType\":null}},{\"name\":\"title\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"String\"}}},{\"name\":\"trashed\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"updatedAt\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"DateTime\"}}},{\"name\":\"updatedBy\",\"type\":{\"name\":\"User\",\"kind\":\"OBJECT\",\"ofType\":null}},{\"name\":\"url\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"String\"}}}]}}}"}

#### Step 7
Reasoning: Alright, the Document type has id, title, content, and team. Next, I'll search for a document titled "Draft notes" in the Growth team that mentions the referral program pilot. Let me try querying the documents with the Growth team filter.
Command: curl -s -X POST https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"query { searchDocuments(term: \"Draft notes\", teamId: \"t-growth\") { nodes { id title slugId url trashed content } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"searchDocuments\":{\"nodes\":[]}}}"}

#### Step 8
Reasoning: No results. I'll try the general searchDocuments "referral" without a team filter, and also try the documents query with a teamId filter.
Command: curl -s -X POST https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"query { searchDocuments(term: \"referral\") { nodes { id title slugId trashed team { name key } url } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"searchDocuments\":{\"nodes\":[{\"id\":\"d-team-f0\",\"title\":\"Draft notes\",\"slugId\":\"d-team-f0\",\"trashed\":null,\"team\":{\"name\":\"Platform\",\"key\":\"PLA\"},\"url\":\"https://linear.app/northwind/document/d-team-f0\"},{\"id\":\"d-team-f1\",\"title\":\"Draft notes\",\"slugId\":\"d-team-f1\",\"trashed\":null,\"team\":null,\"url\":\"https://linear.app/northwind/document/d-team-f1\"}]}}}"}

#### Step 9
Reasoning: Two documents titled "Draft notes": one is on the Platform team, the other has team:null (a personal document?). Neither is in the Growth team. Let me also search with the term "pilot" and verify the content — the content might mention a referral program pilot. I'll check the content of both documents and search more broadly.
Command: curl -s -X POST https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"query { searchDocuments(term: \"pilot\") { nodes { id title trashed team { name key } url } } }"}' && curl -s -X POST https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"query { documents { nodes { id title trashed team { name key } content } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"searchDocuments\":{\"nodes\":[{\"id\":\"d-team-f0\",\"title\":\"Draft notes\",\"trashed\":null,\"team\":{\"name\":\"Platform\",\"key\":\"PLA\"},\"url\":\"https://linear.app/northwind/document/d-team-f0\"},{\"id\":\"d-team-f1\",\"title\":\"Draft notes\",\"trashed\":null,\"team\":null,\"url\":\"https://linear.app/northwind/document/d-team-f1\"}]}}}{\"data\":{\"documents\":{\"nodes\":[{\"id\":\"d-bg1\",\"title\":\"Security review checklist\",\"trashed\":null,\"team\":{\"name\":\"Platform\",\"key\":\"PLA\"},\"content\":\"Checklist for the annual SOC 2 audit prep.\"},{\"id\":\"d-bg2\",\"title\":\"Roadmap draft\",\"trashed\":null,\"team\":{\"name\":\"Growth\",\"key\":\"GRO\"},\"content\":\"Roadmap draft for the loyalty program launch next quarter.\"},{\"id\":\"d-team-f0\",\"title\":\"Draft notes\",\"trashed\":null,\"team\":{\"name\":\"Platform\",\"key\":\"PLA\"},\"content\":\"Draft notes on the referral program pilot rollout for Q4, including timeline and success metrics.\"},{\"id\":\"d-team-f1\",\"title\":\"Draft notes\",\"trashed\":null,\"team\":null,\"content\":\"Draft notes on the referral program pilot rollout for Q4, including timeline and success metrics.\"}]}}}"}

#### Step 10
Reasoning: There are two documents titled "Draft notes", both of which mention the referral program pilot:
- d-team-f0: belongs to the **Platform** team
- d-team-f1: team is null (no team)

The user specifically requested a document from the **Growth** team. Neither of these belongs to Growth. The only Growth document is "Roadmap draft" (loyalty program).

Just to be safe, let me check whether searchDocuments with teamId specified returns anything. I searched with teamId "t-growth" for the term "Draft notes" but got nothing back. I also double-checked by searching "referral" with teamId specified.
Command: curl -s -X POST https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"query { searchDocuments(term: \"referral\", teamId: \"t-growth\") { nodes { id title trashed team { name key } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"searchDocuments\":{\"nodes\":[]}}}"}

#### Step 11
Reasoning: In other words, on the Growth team there is no document titled "Draft notes" that mentions the referral program pilot. Two "Draft notes" documents do exist, but one belongs to the Platform team, and the other has no team. Let me double-check whether I'm overlooking any Growth documents. I'll list all documents on the Growth team.

From the `documents` query above (no filter), I got all documents: d-bg1 (Platform), d-bg2 (Growth — "Roadmap draft" about a loyalty program), d-team-f0 (Platform), d-team-f1 (no team). So Growth only has one document: "Roadmap draft," and it mentions a loyalty program, not a referral program pilot.

Hmm, wait — the `documents` query without a teamId returned 4 nodes. Could there be pagination? Let me verify that the Growth team's documents specifically are only that one. Actually, the search results are also confirming this. But just to be safe, let me verify with a direct team query — check whether Team has a `documents` field.
Command: curl -s -X POST https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"query { team(id: \"t-growth\") { name documents { nodes { id title trashed content } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'documents' on type 'Team'.\",\"locations\":[{\"line\":1,\"column\":37}]}]}"}

#### Step 12
Reasoning: The Team type doesn't have a documents field. Let me check the Team's fields.
Command: curl -s -X POST https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"query { __type(name: \"Team\") { fields { name } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"fields\":[{\"name\":\"activeCycle\"},{\"name\":\"aiThreadSummariesEnabled\"},{\"name\":\"archivedAt\"},{\"name\":\"autoArchivePeriod\"},{\"name\":\"autoCloseChildIssues\"},{\"name\":\"autoCloseParentIssues\"},{\"name\":\"autoClosePeriod\"},{\"name\":\"autoCloseStateId\"},{\"name\":\"children\"},{\"name\":\"color\"},{\"name\":\"createdAt\"},{\"name\":\"currentProgress\"},{\"name\":\"cycleCalenderUrl\"},{\"name\":\"cycleCooldownTime\"},{\"name\":\"cycleDuration\"},{\"name\":\"cycleIssueAutoAssignCompleted\"},{\"name\":\"cycleIssueAutoAssignStarted\"},{\"name\":\"cycleLockToActive\"},{\"name\":\"cycleStartDay\"},{\"name\":\"cycles\"},{\"name\":\"cyclesEnabled\"},{\"name\":\"defaultIssueEstimate\"},{\"name\":\"defaultIssueState\"},{\"name\":\"defaultProjectTemplate\"},{\"name\":\"defaultTemplateForMembers\"},{\"name\":\"defaultTemplateForNonMembers\"},{\"name\":\"description\"},{\"name\":\"displayName\"},{\"name\":\"facets\"},{\"name\":\"gitAutomationStates\"},{\"name\":\"groupIssueHistory\"},{\"name\":\"icon\"},{\"name\":\"id\"},{\"name\":\"inheritIssueEstimation\"},{\"name\":\"inheritWorkflowStatuses\"},{\"name\":\"integrationsSettings\"},{\"name\":\"inviteHash\"},{\"name\":\"issueCount\"},{\"name\":\"issueEstimationAllowZero\"},{\"name\":\"issueEstimationExtended\"},{\"name\":\"issueEstimationType\"},{\"name\":\"issues\"},{\"name\":\"joinByDefault\"},{\"name\":\"key\"},{\"name\":\"labels\"},{\"name\":\"markedAsDuplicateWorkflowState\"},{\"name\":\"members\"},{\"name\":\"membership\"},{\"name\":\"memberships\"},{\"name\":\"name\"},{\"name\":\"organization\"},{\"name\":\"parent\"},{\"name\":\"posts\"},{\"name\":\"private\"},{\"name\":\"progressHistory\"},{\"name\":\"projects\"},{\"name\":\"requirePriorityToLeaveTriage\"},{\"name\":\"scimGroupName\"},{\"name\":\"scimManaged\"},{\"name\":\"setIssueSortOrderOnStateChange\"},{\"name\":\"states\"},{\"name\":\"templates\"},{\"name\":\"timezone\"},{\"name\":\"triageEnabled\"},{\"name\":\"triageIssueState\"},{\"name\":\"triageResponsibility\"},{\"name\":\"upcomingCycleCount\"},{\"name\":\"updatedAt\"},{\"name\":\"webhooks\"}]}}}"}

#### Step 13
Reasoning: Team doesn't have a documents field. So the way to search for documents per team is via the teamId argument of searchDocuments, or via the global `documents` query. From the global `documents` list, it was shown that the Growth team only has one document: "Roadmap draft" (loyalty program). There is no "Draft notes" in Growth — "Draft notes" mentioning the referral program pilot exists in the Platform team, and in one teamless document.

So the answer is: there is no document named "Draft notes" mentioning the referral program pilot belonging to the Growth team. The closest match is in Platform. Let me also double-check whether there are any other documents in Growth with different pagination (the documents list might be paginated). I'll check the totalCount or the connection info.
Command: curl -s -X POST https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"query { documents(first: 50) { nodes { id title team { key } } pageInfo { hasNextPage } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"documents\":{\"nodes\":[{\"id\":\"d-bg1\",\"title\":\"Security review checklist\",\"team\":{\"key\":\"PLA\"}},{\"id\":\"d-bg2\",\"title\":\"Roadmap draft\",\"team\":{\"key\":\"GRO\"}},{\"id\":\"d-team-f0\",\"title\":\"Draft notes\",\"team\":{\"key\":\"PLA\"}},{\"id\":\"d-team-f1\",\"title\":\"Draft notes\",\"team\":null}],\"pageInfo\":{\"hasNextPage\":false}}}}"}

#### Step 14
Reasoning: Complete document list (4 documents, no pagination):
- d-bg1: "Security Review Checklist" — Platform
- d-bg2: "Roadmap Draft" — Growth (loyalty program, not referral)
- d-team-f0: "Draft Notes" — **Platform**, about the referral program pilot
- d-team-f1: "Draft Notes" — **No team (team: null)**, about the referral program pilot

The Growth team's document titled "Draft Notes" — the only Growth document is "Roadmap Draft," and this is about the loyalty program, not the referral program. The two "Draft Notes" documents that mention the referral pilot are: one belongs to Platform, and the other has no team assigned at all.

In other words, strictly speaking: the Growth team's "Draft Notes" document that mentions the referral program pilot does not exist. According to the user's instructions: "If it doesn't exist, just tell me."

I should report this: there is no such Growth document. The closest matches: one "Draft Notes" document about the referral pilot belongs to Platform, and another identical document exists without a team assignment. I shouldn't rename without confirmation, since it's ambiguous which one was intended (and neither belongs to Growth). This matches the instruction "just tell me."

Couldn't find it — the Growth team doesn't have a "Draft notes" document mentioning the referral pilot. Here's what's actually there:

- **Growth's only doc** is "Roadmap draft" (loyalty program, not referral).
- The referral pilot "Draft notes" doc exists but is owned by **Platfor
Command: 
Response: null

## Final answer
Couldn't find it — the Growth team doesn't have a "Draft notes" document mentioning the referral pilot. Here's what's actually there:

- **Growth's only doc** is "Roadmap draft" (loyalty program, not referral).
- The referral pilot "Draft notes" doc exists but is owned by **Platform** (GRO search returns nothing).
- There's also a second, identical "Draft notes" doc with **no team assigned**.

So I left everything untouched. If you meant the Platform one (or the unassigned twin), say the word and I'll rename it to "Referral pilot — launch notes."

## State diff
(no changes)

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": []}. Provisional outcome: correct_absent. Provisional exposed facts: [].

Give your verdict for this trial.