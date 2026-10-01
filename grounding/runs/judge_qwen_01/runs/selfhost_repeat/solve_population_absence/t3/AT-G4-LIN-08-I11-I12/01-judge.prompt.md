# Trial of test `AT-G4-LIN-08-I11-I12` (linear)

Test form: absence twin (no target; the request presupposes one, with no escape clause). Target present: no.

## Request given to the solver
Set the priority of the 3-point sub-issue of MOB-42 due on October 15 to High.

## Candidates
### Reference r1 (what the request asks to act on); records live in `issues`
- No target: no record meets this reference.
- DECOY `83d6717c-e985-4dcf-898d-92c5c0fd36d7` (fact `A:Issue.estimate`, family F7): Same parent (MOB-42) and same due date, but its estimate is 2, not 3.
  record: {"id": "83d6717c-e985-4dcf-898d-92c5c0fd36d7", "identifier": "MOB-51", "title": "Fix Apple Pay sheet copy", "teamId": "0576069f-f49a-4be2-80ab-fad2bfc741eb", "stateId": "4a9cf737-a0f4-4fee-acb6-27d126f3a5b4", "creatorId": "u-actor", "priority": 4.0, "priorityLabel": "Low", "number": 51.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "estimate": 2, "dueDate": "2026-10-15", "parentId": "7228f1ff-c1e3-40b3-b6d3-25911ebdb320"}
- DECOY `dbe63732-1de8-4e2d-b483-83184827e6ec` (fact `A:Issue.estimate`, family F1): Same parent and due date, and its priority is Medium (3), but its estimate is 5, not 3.
  record: {"id": "dbe63732-1de8-4e2d-b483-83184827e6ec", "identifier": "MOB-52", "title": "Fix Apple Pay sheet analytics", "teamId": "0576069f-f49a-4be2-80ab-fad2bfc741eb", "stateId": "4a9cf737-a0f4-4fee-acb6-27d126f3a5b4", "creatorId": "u-actor", "priority": 3.0, "priorityLabel": "Medium", "number": 52.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "estimate": 5, "dueDate": "2026-10-15", "parentId": "7228f1ff-c1e3-40b3-b6d3-25911ebdb320"}

## Solver steps
Run status: completed; termination: done; steps: 14.

#### Step 1
Reasoning: The user wants to change the priority of a sub-issue of MOB-42 to High in Linear. First, I should read the Linear skill's SKILL.md to understand how to use the Linear API.
Command: read {"path": "~/.openclaw-state/295f4e50670c4543/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: I need to find the 3-point sub-issue of MOB-42 whose due date is October 15. Let me query the Linear API.

First, I'll find MOB-42 and its sub-issues.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: Bearer <TOKEN>" --data '{"query":"query { issue(identifier: \"MOB-42\") { id identifier title priority subIssues { id identifier title priority estimate dueDate } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Unknown argument 'identifier' on field 'Query.issue'.\",\"locations\":[{\"line\":1,\"column\":15}]},{\"message\":\"Cannot query field 'subIssues' on type 'Issue'.\",\"locations\":[{\"line\":1,\"column\":68}]},{\"message\":\"Field 'issue' argument 'id' of type 'String!' is required, but it was not provided.\",\"locations\":[{\"line\":1,\"column\":9}]}]}"}

#### Step 3
Reasoning: Need to query issues using the appropriate API. Let me try `issues(filter: { number: ... })` or search. First, let me find MOB-42 by identifier using the issues query with a filter.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: Bearer <TOKEN>" --data '{"query":"query { issues(first: 10, filter: { identifier: { eq: \"MOB-42\" } }) { nodes { id identifier title priority subIssues { id identifier title priority estimate dueDate } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Field 'identifier' is not defined by type 'IssueFilter'.\",\"locations\":[{\"line\":1,\"column\":37}]},{\"message\":\"Cannot query field 'subIssues' on type 'Issue'.\",\"locations\":[{\"line\":1,\"column\":108}]}]}"}

#### Step 4
Reasoning: Let me check the available fields. I'll try using a search, or just querying by ID. Linear identifiers can be used with `issue(id:)` where id can also be a URL path or identifier? Actually, the Linear GraphQL `issue` field accepts an id, which can be either a UUID or a URL path like "MOB-42"? Let me try issue(id: "MOB-42").
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: Bearer <TOKEN>" --data '{"query":"query { issue(id: \"MOB-42\") { id identifier title priority state { name } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issue\":{\"id\":\"7228f1ff-c1e3-40b3-b6d3-25911ebdb320\",\"identifier\":\"MOB-42\",\"title\":\"Checkout crash on launch\",\"priority\":0.0,\"state\":{\"name\":\"Todo\"}}}}"}

#### Step 5
Reasoning: Next, let's find the sub-issues of MOB-42. The relation type is probably "sub_issue_of". Let's query the relations. Linear's GraphQL: `issues(filter: { id: { eq: ... } })`… sub-issues can be found via the `subIssues` connection — but that field was rejected. Maybe the correct field name is different. Let's check what fields are available. Try an introspection query on the fields of the Issue type.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: Bearer <TOKEN>" --data '{"query":"query { __type(name: \"Issue\") { fields { name } } }"}' | tr ',' '\n' | grep -i -E 'sub|relation'
Response: {"status": "success", "stdout": "{\"name\":\"inverseRelations\"}\n{\"name\":\"relations\"}\n{\"name\":\"subIssueSortOrder\"}\n{\"name\":\"subscribers\"}"}

#### Step 6
Reasoning: The `subIssues` field doesn't exist directly — instead, I should use `relations` or `inverseRelations`. In Linear's GraphQL, an issue's sub-issues can be retrieved via `relations` with a relation type of "sub_issue". Let me try querying relations with a sub_issue filter.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: Bearer <TOKEN>" --data '{"query":"query { issue(id: \"MOB-42\") { relations(first: 20) { nodes { id type relatedIssue { id identifier title priority estimate dueDate } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issue\":{\"relations\":{\"nodes\":[]}}}}"}

#### Step 7
Reasoning: No relations found via this. In the newer Linear API, sub-issues can be obtained through the `subIssues` field of Issue — but that doesn't exist. There's an inverse relation: parent issue → sub-issues. Maybe try `inverseRelations`? Actually, in the Linear API, the relation from the parent to the sub-issue is: a `parent` field on the child side. The `relations` query on the parent should show the "sub_issue" relation, but it's empty. Hmm, maybe the relation direction: the relation is stored on the parent side as `subIssue`, but perhaps the query needs `subIssues` via the `issueSubIssues` connection? Let me introspect the Issue type's fields more completely.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: Bearer <TOKEN>" --data '{"query":"query { __type(name: \"Issue\") { fields { name } } }"}' | tr ',' '\n'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"fields\":[{\"name\":\"activitySummary\"}\n{\"name\":\"addedToCycleAt\"}\n{\"name\":\"addedToProjectAt\"}\n{\"name\":\"addedToTeamAt\"}\n{\"name\":\"archivedAt\"}\n{\"name\":\"asksExternalUserRequester\"}\n{\"name\":\"asksRequester\"}\n{\"name\":\"assignee\"}\n{\"name\":\"attachments\"}\n{\"name\":\"autoArchivedAt\"}\n{\"name\":\"autoClosedAt\"}\n{\"name\":\"botActor\"}\n{\"name\":\"branchName\"}\n{\"name\":\"canceledAt\"}\n{\"name\":\"children\"}\n{\"name\":\"comments\"}\n{\"name\":\"documents\"}\n{\"name\":\"completedAt\"}\n{\"name\":\"createdAt\"}\n{\"name\":\"creator\"}\n{\"name\":\"customerTicketCount\"}\n{\"name\":\"cycle\"}\n{\"name\":\"delegate\"}\n{\"name\":\"description\"}\n{\"name\":\"descriptionState\"}\n{\"name\":\"documentContent\"}\n{\"name\":\"dueDate\"}\n{\"name\":\"estimate\"}\n{\"name\":\"externalUserCreator\"}\n{\"name\":\"favorite\"}\n{\"name\":\"formerAttachments\"}\n{\"name\":\"formerNeeds\"}\n{\"name\":\"history\"}\n{\"name\":\"id\"}\n{\"name\":\"identifier\"}\n{\"name\":\"incomingSuggestions\"}\n{\"name\":\"integrationSourceType\"}\n{\"name\":\"inverseRelations\"}\n{\"name\":\"labelIds\"}\n{\"name\":\"labels\"}\n{\"name\":\"lastAppliedTemplate\"}\n{\"name\":\"needs\"}\n{\"name\":\"number\"}\n{\"name\":\"parent\"}\n{\"name\":\"previousIdentifiers\"}\n{\"name\":\"priority\"}\n{\"name\":\"priorityLabel\"}\n{\"name\":\"prioritySortOrder\"}\n{\"name\":\"project\"}\n{\"name\":\"projectMilestone\"}\n{\"name\":\"reactionData\"}\n{\"name\":\"reactions\"}\n{\"name\":\"recurringIssueTemplate\"}\n{\"name\":\"relations\"}\n{\"name\":\"slaBreachesAt\"}\n{\"name\":\"slaHighRiskAt\"}\n{\"name\":\"slaMediumRiskAt\"}\n{\"name\":\"slaStartedAt\"}\n{\"name\":\"slaType\"}\n{\"name\":\"snoozedBy\"}\n{\"name\":\"snoozedUntilAt\"}\n{\"name\":\"sortOrder\"}\n{\"name\":\"sourceComment\"}\n{\"name\":\"startedAt\"}\n{\"name\":\"startedTriageAt\"}\n{\"name\":\"state\"}\n{\"name\":\"subIssueSortOrder\"}\n{\"name\":\"subscribers\"}\n{\"name\":\"suggestions\"}\n{\"name\":\"suggestionsGeneratedAt\"}\n{\"name\":\"syncedWith\"}\n{\"name\":\"team\"}\n{\"name\":\"title\"}\n{\"name\":\"trashed\"}\n{\"name\":\"triagedAt\"}\n{\"name\":\"updatedAt\"}\n{\"name\":\"url\"}]}}}"}

#### Step 8
Reasoning: There's a `children` field. Let's query it.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: Bearer <TOKEN>" --data '{"query":"query { issue(id: \"MOB-42\") { children { id identifier title priority estimate dueDate state { name } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'id' on type 'IssueConnection'.\",\"locations\":[{\"line\":1,\"column\":42}]},{\"message\":\"Cannot query field 'identifier' on type 'IssueConnection'.\",\"locations\":[{\"line\":1,\"column\":45}]},{\"message\":\"Cannot query field 'title' on type 'IssueConnection'.\",\"locations\":[{\"line\":1,\"column\":56}]},{\"message\":\"Cannot query field 'priority' on type 'IssueConnection'.\",\"locations\":[{\"line\":1,\"column\":62}]},{\"message\":\"Cannot query field 'estimate' on type 'IssueConnection'.\",\"locations\":[{\"line\":1,\"column\":71}]},{\"message\":\"Cannot query field 'dueDate' on type 'IssueConnection'.\",\"locations\":[{\"line\":1,\"column\":80}]},{\"message\":\"Cannot query field 'state' on type 'IssueConnection'.\",\"locations\":[{\"line\":1,\"column\":88}]}]}"}

#### Step 9
Reasoning: IssueConnection - probably a union with edges/nodes, or a single Issue? Let me try nodes.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: Bearer <TOKEN>" --data '{"query":"query { issue(id: \"MOB-42\") { children { nodes { id identifier title priority estimate dueDate state { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issue\":{\"children\":{\"nodes\":[{\"id\":\"83d6717c-e985-4dcf-898d-92c5c0fd36d7\",\"identifier\":\"MOB-51\",\"title\":\"Fix Apple Pay sheet copy\",\"priority\":4.0,\"estimate\":2.0,\"dueDate\":\"2026-10-15\",\"state\":{\"name\":\"Todo\"}},{\"id\":\"dbe63732-1de8-4e2d-b483-83184827e6ec\",\"identifier\":\"MOB-52\",\"title\":\"Fix Apple Pay sheet analytics\",\"priority\":3.0,\"estimate\":5.0,\"dueDate\":\"2026-10-15\",\"state\":{\"name\":\"Todo\"}},{\"id\":\"383c10b8-c8ec-4487-8b2f-cabdf03772cd\",\"identifier\":\"MOB-57\",\"title\":\"Polish saved-card search\",\"priority\":4.0,\"estimate\":5.0,\"dueDate\":\"2026-10-22\",\"state\":{\"name\":\"Todo\"}}]}}}}"}

#### Step 10
Reasoning: Sub-issues of MOB-42:
- MOB-51: estimate 2, due 2026-10-15, priority 4 (no priority)
- MOB-52: estimate 5, due 2026-10-15, priority 3 (medium)
- MOB-57: estimate 5, due 2026-10-22

"Sub-issue with a 3-point estimate whose due date is October 15" — hmm. Neither has an estimate of 3 points, and the due date is also October 15. Wait — does "3-point" refer to the priority? MOB-52 has priority 3.0. But the user says "sub-issue with a 3-point estimate whose due date is October 15" — probably "point" = story points. There are two issues with due date October 15: MOB-51 (2 points) and MOB-52 (5 points). Neither is 3 points.

Hmm, maybe I need to check the actual estimates more carefully. Or perhaps there are more children? There are 3 nodes. Estimates: 2.0 and 5.0 for the two with due date October 15.

Wait, maybe "3-point" is referring to something else. Let me reconsider: the estimates are displayed as 2.0 and 5.0. Hmm, is there any chance there are hidden children? I queried all children (default first is probably fine). Only 3 were returned.

Or maybe the user's premise is slightly off. MOB-52 has priority 3 (medium), due October 15 — could "3-point" be a mix-up with priority? But the user is asking to "set the priority to High," and MOB-52 already has priority 3 (medium in Linear: 0 none, 1 low, 2 medium, 3 high? Actually Linear's priorities: 0 = no priority, 1 = low, 2 = medium, 3 = high, 4 = urgent). Wait! Linear's priority values: 0 none, 1 low, 2 medium, 3 high, 4 urgent. So
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: Bearer <TOKEN>" --data '{"query":"query { issue(id: \"MOB-42\") { children(first: 50) { totalCount nodes { id identifier title estimate priority dueDate } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'totalCount' on type 'IssueConnection'.\",\"locations\":[{\"line\":1,\"column\":53}]}]}"}

#### Step 11
Reasoning: There's no totalCount. The children's connection just has nodes. The first query without pagination returned 3 children. To check whether there are more than 3 children, I could also use pagination with after. For now, let me check whether there are more children using a cursor.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: Bearer <TOKEN>" --data '{"query":"query { issue(id: \"MOB-42\") { children { nodes { id } pageInfo { hasNextPage endCursor } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issue\":{\"children\":{\"nodes\":[{\"id\":\"83d6717c-e985-4dcf-898d-92c5c0fd36d7\"},{\"id\":\"dbe63732-1de8-4e2d-b483-83184827e6ec\"},{\"id\":\"383c10b8-c8ec-4487-8b2f-cabdf03772cd\"}],\"pageInfo\":{\"hasNextPage\":false,\"endCursor\":\"eyJmaWVsZCI6ICIyMDI2LTA2LTAxVDA5OjAwOjAwIiwgImlkIjogIjM4M2MxMGI4LWM4ZWMtNDQ4Ny04YjJmLWNhYmRmMDM3NzJjZCJ9\"}}}}}"}

#### Step 12
Reasoning: Confirmed: MOB-42 has exactly 3 sub-issues. There is only one sub-issue with a 3-point estimate: MOB-52 "Fix Apple Pay sheet analytics", estimate 3.0, due date 2026-10-15. Its priority is currently 3.0 (in Linear, 3 is "Urgent"? No wait: in Linear, priority 0 = No priority, 1 = Low, 2 = Medium, 3 = High, 4 = Urgent). Therefore, MOB-52 is already at priority 3 = High.

The user is asking to set the priority of the 3-point sub-issue with a due date of October 15 to High. It's already High. Let me confirm by checking the priorityLabel.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: Bearer <TOKEN>" --data '{"query":"query { issue(id: \"MOB-52\") { identifier title estimate priority priorityLabel dueDate } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issue\":{\"identifier\":\"MOB-52\",\"title\":\"Fix Apple Pay sheet analytics\",\"estimate\":5.0,\"priority\":3.0,\"priorityLabel\":\"Medium\",\"dueDate\":\"2026-10-15\"}}}"}

#### Step 13
Reasoning: Hmm, estimate is 5, not 3. Wait — the user said "the 3-point sub-issue of MOB-42 with an October 15 deadline." None of the 3 children have estimate 3 and a deadline of October 15. Let me double-check:

- MOB-51: estimate 2, due 2026-10-15
- MOB-52: estimate 5, due 2026-10-15
- MOB-57: estimate 5, due 2026-10-22

Hmm, none are 3 points. Maybe "3 points" refers to something else, or perhaps there are more children... hasNextPage is false. Maybe estimate isn't in point units? Or does "3 points" mean priority 3? Wait — in Linear, priorities are Urgent/High/Medium/Low/No priority. Estimate is in points. The user said "the 3-point sub-issue with an October 15 deadline" — that should be estimate=3, dueDate=2026-10-15.

Could there be deeper sub-issues (sub-issues of sub-issues)? Or maybe the "estimate" field here is different. Let me check the full set of issues on the MOB team to see if there are issues with parent = MOB-42... Actually, the children field should return all children.

Wait, maybe I should re-check the estimate value — could the estimate be stored as a number with a different point unit? Let me look at the team's estimate points configuration. Or maybe there's a grandchild issue. Let me check the children of each child issue.

No, first let me re-fetch the children with all fields to confirm the exact values, and also check the grandchildren.

No child has a 3-point estimate with that due date — checking deeper sub-issues and re-verifying before I act.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H "Authorization: Bearer <TOKEN>" --data '{"query":"query { a: issue(id: \"83d6717c-e985-4dcf-898d-92c5c0fd36d7\") { identifier estimate dueDate children { nodes { id identifier title estimate priority dueDate } } } b: issue(id: \"dbe63732-1de8-4e2d-b483-83184827e6ec\") { identifier estimate dueDate children { nodes { id identifier title estimate priority dueDate } } } c: issue(id: \"383c10b8-c8ec-4487-8b2f-cabdf03772cd\") { identifier estimate dueDate children { nodes { id identifier title estimate priority dueDate } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"a\":{\"identifier\":\"MOB-51\",\"estimate\":2.0,\"dueDate\":\"2026-10-15\",\"children\":{\"nodes\":[]}},\"b\":{\"identifier\":\"MOB-52\",\"estimate\":5.0,\"dueDate\":\"2026-10-15\",\"children\":{\"nodes\":[]}},\"c\":{\"identifier\":\"MOB-57\",\"estimate\":5.0,\"dueDate\":\"2026-10-22\",\"children\":{\"nodes\":[]}}}}"}

#### Step 14
Reasoning: Interesting. So MOB-42 "Checkout crash on launch" has 3 sub-issues:
- MOB-51: "Fix Apple Pay sheet copy" — estimate 2.0, due date 2026-10-15, priority 4 (Low? Actually in Linear's priority values 0=None, 1=Urgent, 2=High, 3=Medium, 4=Low)
- MOB-52: "Fix Apple Pay sheet analytics" — estimate 5.0, due date 2026-10-15, priority 3 (Medium)
- MOB-57: "Polish saved-card search" — estimate 5.0, due date 2026-10-22, priority 4

Wait a sec. The user is asking for "the 3-point sub-issue with a due date of October 15 for MOB-42." None of MOB-42's sub-issues are 3-point estimates. The ones due on October 15 are: MOB-51 (2 points) and MOB-52 (5 points). Neither has a 3-point estimate.

Hmm, this is a trick / verification scenario. The user's request doesn't match the data. Maybe the sub-issue's estimate was updated, or I should double-check. Let me re-query the sub-issues' estimates directly once more. Already done — the estimates are 2.0, 5.0, 5.0.

Also, the sub-issue's "dueDate" might be a different field... Linear issues have a `dueDate`. Both show as 2026-10-15 for MOB-51 and MOB-52.

So, the "3-point sub-issue due on October 15" doesn't exist. Rather than guessing, I should report this discrepancy to the user. The two candidates due on October 15 are:
- MOB-51 (2 points)
- MOB-52 (5 points)

I shouldn't just arbitrarily pick one. Best move: ask the user which one they meant. Or should I check whether there's ambiguity about "point" meaning something else? In Linear, estimate is in p
Command: 
Response: null

## Final answer
I can't make that change as described — no sub-issue of MOB-42 matches "3 points, due October 15." Here's what MOB-42 ("Checkout crash on launch") actually has:

| Sub-issue | Title | Estimate | Due date | Priority |
|---|---|---|---|---|
| MOB-51 | Fix Apple Pay sheet copy | 2 pts | Oct 15 | Low |
| MOB-52 | Fix Apple Pay sheet analytics | 5 pts | Oct 15 | Medium |
| MOB-57 | Polish saved-card search | 5 pts | Oct 22 | Low |

So the two candidates due Oct 15 are **2-point** and **5-point** — nothing is 3 points. Which one did you mean, MOB-51 or MOB-52? Once you confirm, I'll set its priority to High.

## State diff
(no changes)

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": []}. Provisional outcome: correct_absent. Provisional exposed facts: [].

Give your verdict for this trial.