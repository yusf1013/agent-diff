# Trial of test `P-G4-LIN-08-I16` (linear)

Test form: probe. Target present: no.

## Request given to the solver
Set the priority of the 3-point sub-issue of MOB-42 due on October 15 to High. If there isn't one, just tell me.

## Candidates
### Reference r1 (what the request asks to act on); records live in `issues`
- No target: no record meets this reference.
- DECOY `76674469-a624-448e-834a-9425ecb0c874` (fact `A:Issue.identifier`, family F1): Same estimate and due date, and its title mentions MOB-42, but it is a sub-issue of MOB-7.
  record: {"id": "76674469-a624-448e-834a-9425ecb0c874", "identifier": "MOB-56", "title": "MOB-42 follow-up: Apple Pay sheet", "teamId": "0576069f-f49a-4be2-80ab-fad2bfc741eb", "stateId": "4a9cf737-a0f4-4fee-acb6-27d126f3a5b4", "creatorId": "u-actor", "priority": 4.0, "priorityLabel": "Low", "number": 56.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "estimate": 3, "dueDate": "2026-10-15", "parentId": "e6e2f7f7-2d17-4647-bf83-f46eff5934e2"}

## Solver steps
Run status: completed; termination: done; steps: 4.

#### Step 1
Reasoning: Let's check the Linear skill, since this task involves Linear.
Command: read {"path": "~/.openclaw-state/986c2d85842b4208/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: The skill documentation is thin on the actual GraphQL schema details. I know the Linear GraphQL API well. What needs to be done is:

1. Find MOB-42 (issue with the identifier MOB-42).
2. Find its sub-issues (child issues), and filter for those whose estimate (points) = 3 and due date = 2026-10-15.
3. If exactly one exists, set its priority to High (priority = 3, since Linear's priorities are: 0=No priority, 1=Urgent, 2=High, 3=Medium, 4=Low — no wait, actually: 0 = None, 1 = Urgent, 2 = High, 3 = Medium, 4 = Low).

So High = 2.

Let's run a query. Authentication: "Authentication is handled automatically via the proxy. Where credentials would go, use a placeholder token like `<TOKEN>`."

So I should use curl with a placeholder token. The proxy will handle authentication.

Query:

```graphql
query {
  issue(id: "MOB-42") {
    id
    identifier
    title
    childIssues(first: 50) {
      nodes {
        id
        identifier
        title
        estimate
        dueDate
        priority
        priorityName
      }
    }
  }
}
```

Then filter for ones where estimate == 3 and dueDate == 2026-10-15.

After that, update:

```graphql
mutation {
  issueUpdate(id: "<id>", input: {priority: 2}) {
    success
    issue { id priorityName }
  }
}
```

Let's run the first query.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"query { issue(id: \"MOB-42\") { id identifier title dueDate childIssues(first: 100) { nodes { id identifier title estimate dueDate priorityName } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'childIssues' on type 'Issue'. Did you mean 'children'?\",\"locations\":[{\"line\":1,\"column\":59}]}]}"}

#### Step 3
Reasoning: The field is `children`, not `childIssues`. Let's retry.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"query { issue(id: \"MOB-42\") { id identifier title dueDate children(first: 100) { nodes { id identifier title estimate dueDate priority } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issue\":{\"id\":\"7228f1ff-c1e3-40b3-b6d3-25911ebdb320\",\"identifier\":\"MOB-42\",\"title\":\"Checkout crash on launch\",\"dueDate\":null,\"children\":{\"nodes\":[{\"id\":\"383c10b8-c8ec-4487-8b2f-cabdf03772cd\",\"identifier\":\"MOB-57\",\"title\":\"Polish saved-card search\",\"estimate\":5.0,\"dueDate\":\"2026-10-22\",\"priority\":4.0}]}}}}"}

#### Step 4
Reasoning: MOB-42 has only one sub-issue: MOB-57, estimate 5.0, due 2026-10-22. It's neither a 3-point issue nor due on October 15. So the answer is: no matching sub-issue exists.

Nope — MOB-42 ("Checkout crash on launch") has only one sub-issue: **MOB-57** "Polish saved-card search" (5 points, due Oct 22). No 3-point sub-issue due October 15, so I didn't change anything.
Command: 
Response: null

## Final answer
Nope — MOB-42 ("Checkout crash on launch") has only one sub-issue: **MOB-57** "Polish saved-card search" (5 points, due Oct 22). No 3-point sub-issue due October 15, so I didn't change anything.

## State diff
(no changes)

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": []}. Provisional outcome: absent_unclear. Provisional exposed facts: [].

Give your verdict for this trial.