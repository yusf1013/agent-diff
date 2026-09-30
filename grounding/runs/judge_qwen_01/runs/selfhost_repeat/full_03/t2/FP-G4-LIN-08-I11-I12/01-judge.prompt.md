# Trial of test `FP-G4-LIN-08-I11-I12` (linear)

Test form: fact probe. Target present: no.

## Request given to the solver
Set the priority of the 3-point sub-issue of MOB-42 due on October 15 to High. If there isn't one, just tell me.

## Candidates
### Reference r1 (what the request asks to act on); records live in `issues`
- No target: no record meets this reference.
- DECOY `83d6717c-e985-4dcf-898d-92c5c0fd36d7` (fact `A:Issue.estimate`, family F7): Same parent (MOB-42) and same due date, but its estimate is 2, not 3.
  record: {"id": "83d6717c-e985-4dcf-898d-92c5c0fd36d7", "identifier": "MOB-51", "title": "Fix Apple Pay sheet copy", "teamId": "0576069f-f49a-4be2-80ab-fad2bfc741eb", "stateId": "4a9cf737-a0f4-4fee-acb6-27d126f3a5b4", "creatorId": "u-actor", "priority": 4.0, "priorityLabel": "Low", "number": 51.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "estimate": 2, "dueDate": "2026-10-15", "parentId": "7228f1ff-c1e3-40b3-b6d3-25911ebdb320"}
- DECOY `dbe63732-1de8-4e2d-b483-83184827e6ec` (fact `A:Issue.estimate`, family F1): Same parent and due date, and its priority is Medium (3), but its estimate is 5, not 3.
  record: {"id": "dbe63732-1de8-4e2d-b483-83184827e6ec", "identifier": "MOB-52", "title": "Fix Apple Pay sheet analytics", "teamId": "0576069f-f49a-4be2-80ab-fad2bfc741eb", "stateId": "4a9cf737-a0f4-4fee-acb6-27d126f3a5b4", "creatorId": "u-actor", "priority": 3.0, "priorityLabel": "Medium", "number": 52.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "estimate": 5, "dueDate": "2026-10-15", "parentId": "7228f1ff-c1e3-40b3-b6d3-25911ebdb320"}

## Solver steps
Run status: completed; termination: done; steps: 6.

#### Step 1
Reasoning: The user is asking about Linear: they want me to set the priority of the 3-point sub-issue of MOB-42 that has a due date of October 15 to High. First, let me read the Linear skill.
Command: read {"path": "~/.openclaw-state/60ebc921237b4b90/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: The SKILL.md is pretty sparse on GraphQL schema details. I need to query MOB-42 to find its sub-issues, and look for 3-point sub-issues whose due date is October 15 (probably 2026-10-15, or maybe a past 2025-10-15? The current date is Friday, 2026-10-16, so a due date of October 15 = 2026-10-15 makes sense — yesterday).

Let me construct a GraphQL query. Linear's GraphQL API:

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
      }
    }
  }
}
```

The subIssues field might be `subIssues(orderBy: position)`. Let me give it a try.

The issue ID in the API is a UUID, but the `issue(id:)` field also accepts a human-readable identifier ("MOB-42") — in fact, Linear's `issue` query accepts an ID that is a UUID or a human-readable format. Yeah, it accepts `issue(id: "MOB-42")`.

Regarding the estimate field: in Linear's GraphQL, Issue has `estimate` (Int?), and `points` may not exist. In fact, in newer Linear, `estimate` is an Int. There might also be a `estimatePoints`? I'll use `estimate` and filter by dueDate == "2026-10-15" (date-only format).

Due date: Linear stores dueDate as a full ISO8601 datetime, e.g. "2026-10-15T00:00:00.000Z". Querying with a date-only string might work because Linear accepts "YYYY-MM-DD" for dates. I'll query and check.

First, let me run the query to get the sub-issues of MOB-42.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"query { issue(id: \"MOB-42\") { id identifier title subIssues(first: 50) { nodes { id identifier title estimate dueDate } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'subIssues' on type 'Issue'.\",\"locations\":[{\"line\":1,\"column\":51}]}]}"}

#### Step 3
Reasoning: Let's check the Linear GraphQL API. The relationship is via the `relatedIssues` or `issues` fields. In Linear's GraphQL API, is `subIssues` on Issue? Let me think about it. In the Linear API, is it `issue.subIssues { nodes }`? Hmm, the error says "Cannot query field 'subIssues' on type 'Issue'". So, sub-issues need to be found via the `IssueRelation` type. Does Linear's API have an `issues(filter: { id: { eq: ... }, relation: { type: { eq: "sub_issue" } } })`? Actually, Linear's GraphQL has `issueRelations` and filters like `IssueFilter` with `relation`? Let me check the documentation. In the Linear API, the top-level `issues` query accepts a filter like:

```
issues(filter: { id: { eq: "..." } })
```

For sub-issues, there's a filter field called `relation` of type `IssueRelationFilter`, which has `type` (e.g. "sub_issue") and `issue` (the ID). Actually, according to Linear's docs, IssueFilter has the following fields: `assignee`, `createdAt`, `dueDate`, `id`, `identifier`, `label`, `labels`, `priority`, `project`, `projectMember`, `release`, `search`, `sort`, `state`, `team`, `updatedAt`, `workflowState`, `issue`, `relation`? Let me try to recall. Linear's `IssueFilter` includes the following:
- `issue` (IssueFilter?) No, that's not it…

From Linear's API reference (graphql), the fields of `IssueFilter` are: `assignee`, `createdAt`, `dueDate`, `id`, `identifier`, `label`, `labels`, `priority`, `project`, `projectMember`, `release`, `search`, `sort`, `state`, `team`, `update
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"query { __type(name: \"IssueFilter\") { fields { name type { name kind ofType { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"fields\":null}}}"}

#### Step 4
Reasoning: The filter type isn't named "IssueFilter". Let me check the Issue type itself and look for fields like relations, parent, childIssues. I'll investigate the fields of the Issue type.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"query { __type(name: \"Issue\") { fields { name } } }"}' | head -c 4000
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"fields\":[{\"name\":\"activitySummary\"},{\"name\":\"addedToCycleAt\"},{\"name\":\"addedToProjectAt\"},{\"name\":\"addedToTeamAt\"},{\"name\":\"archivedAt\"},{\"name\":\"asksExternalUserRequester\"},{\"name\":\"asksRequester\"},{\"name\":\"assignee\"},{\"name\":\"attachments\"},{\"name\":\"autoArchivedAt\"},{\"name\":\"autoClosedAt\"},{\"name\":\"botActor\"},{\"name\":\"branchName\"},{\"name\":\"canceledAt\"},{\"name\":\"children\"},{\"name\":\"comments\"},{\"name\":\"documents\"},{\"name\":\"completedAt\"},{\"name\":\"createdAt\"},{\"name\":\"creator\"},{\"name\":\"customerTicketCount\"},{\"name\":\"cycle\"},{\"name\":\"delegate\"},{\"name\":\"description\"},{\"name\":\"descriptionState\"},{\"name\":\"documentContent\"},{\"name\":\"dueDate\"},{\"name\":\"estimate\"},{\"name\":\"externalUserCreator\"},{\"name\":\"favorite\"},{\"name\":\"formerAttachments\"},{\"name\":\"formerNeeds\"},{\"name\":\"history\"},{\"name\":\"id\"},{\"name\":\"identifier\"},{\"name\":\"incomingSuggestions\"},{\"name\":\"integrationSourceType\"},{\"name\":\"inverseRelations\"},{\"name\":\"labelIds\"},{\"name\":\"labels\"},{\"name\":\"lastAppliedTemplate\"},{\"name\":\"needs\"},{\"name\":\"number\"},{\"name\":\"parent\"},{\"name\":\"previousIdentifiers\"},{\"name\":\"priority\"},{\"name\":\"priorityLabel\"},{\"name\":\"prioritySortOrder\"},{\"name\":\"project\"},{\"name\":\"projectMilestone\"},{\"name\":\"reactionData\"},{\"name\":\"reactions\"},{\"name\":\"recurringIssueTemplate\"},{\"name\":\"relations\"},{\"name\":\"slaBreachesAt\"},{\"name\":\"slaHighRiskAt\"},{\"name\":\"slaMediumRiskAt\"},{\"name\":\"slaStartedAt\"},{\"name\":\"slaType\"},{\"name\":\"snoozedBy\"},{\"name\":\"snoozedUntilAt\"},{\"name\":\"sortOrder\"},{\"name\":\"sourceComment\"},{\"name\":\"startedAt\"},{\"name\":\"startedTriageAt\"},{\"name\":\"state\"},{\"name\":\"subIssueSortOrder\"},{\"name\":\"subscribers\"},{\"name\":\"suggestions\"},{\"name\":\"suggestionsGeneratedAt\"},{\"name\":\"syncedWith\"},{\"name\":\"team\"},{\"name\":\"title\"},{\"name\":\"trashed\"},{\"name\":\"triagedAt\"},{\"name\":\"updatedAt\"},{\"name\":\"url\"}]}}}"}

#### Step 5
Reasoning: The field is `children`. Let's query that.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"query { issue(id: \"MOB-42\") { id identifier title children(first: 50) { nodes { id identifier title estimate dueDate priority } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issue\":{\"id\":\"7228f1ff-c1e3-40b3-b6d3-25911ebdb320\",\"identifier\":\"MOB-42\",\"title\":\"Checkout crash on launch\",\"children\":{\"nodes\":[{\"id\":\"83d6717c-e985-4dcf-898d-92c5c0fd36d7\",\"identifier\":\"MOB-51\",\"title\":\"Fix Apple Pay sheet copy\",\"estimate\":2.0,\"dueDate\":\"2026-10-15\",\"priority\":4.0},{\"id\":\"dbe63732-1de8-4e2d-b483-83184827e6ec\",\"identifier\":\"MOB-52\",\"title\":\"Fix Apple Pay sheet analytics\",\"estimate\":5.0,\"dueDate\":\"2026-10-15\",\"priority\":3.0},{\"id\":\"383c10b8-c8ec-4487-8b2f-cabdf03772cd\",\"identifier\":\"MOB-57\",\"title\":\"Polish saved-card search\",\"estimate\":5.0,\"dueDate\":\"2026-10-22\",\"priority\":4.0}]}}}}"}

#### Step 6
Reasoning: The user is looking for a sub-issue of MOB-42 that is "3 points" and has a due date of October 15.

Children:
- MOB-51: estimate 2.0, due 2026-10-15, priority 4
- MOB-52: estimate 5.0, due 2026-10-15, priority 3
- MOB-57: estimate 5.0, due 2026-10-22, priority 4

Hmm. There isn't a single sub-issue with an estimate of exactly 3 points and a due date of October 15. MOB-52 has a priority of 3 (not an estimate of 3), and its due date is October 15. MOB-51 has an estimate of 2 and a due date of October 15.

Wait — "3 points" probably means an estimate of 3.0. None of them match. However, it's possible that there are more children beyond the first 50 — no, there are only 3 in total.

Hmm, but wait: maybe the user is confusing the priority of 3 with 3 points? Or is there another team issue? Let me check whether there are other issues with the same identifier "MOB-42" — identifiers are usually unique. Also, there might be hidden/archived children. Let me double-check whether there are any children that weren't displayed. The first:50 returned 3 nodes.

So, there is no 3-point sub-issue with a due date of October 15. The closest match: MOB-52 has a due date of October 15 and a priority of 3 (already Medium priority 3? Linear's priorities are 0=No priority, 1=Urgent, 2=High, 3=Medium, 4=Low).

Therefore the answer is: no sub-issue matching the description exists. The two sub-issues due October 15 are MOB-51 (2 points) and MOB-52 (5 points).

Just to be safe, maybe I should check for a
Command: 
Response: null

## Final answer
I checked MOB-42 ("Checkout crash on launch") and its sub-issues — there's no 3-point sub-issue due on October 15, so I didn't change anything.

What actually exists under MOB-42:

- **MOB-51** – "Fix Apple Pay sheet copy" — 2 pts, due Oct 15, priority Low
- **MOB-52** – "Fix Apple Pay sheet analytics" — 5 pts, due Oct 15, priority Medium
- **MOB-57** – "Polish saved-card search" — 5 pts, due Oct 22, priority Low

In case you meant one of these: MOB-52 is the one due Oct 15 with a "3" attached (though that's its priority value, not its estimate). If you want, I can set MOB-51 or MOB-52 to High — just say which.

## State diff
(no changes)

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": []}. Provisional outcome: presented?. Provisional exposed facts: [].

Give your verdict for this trial.