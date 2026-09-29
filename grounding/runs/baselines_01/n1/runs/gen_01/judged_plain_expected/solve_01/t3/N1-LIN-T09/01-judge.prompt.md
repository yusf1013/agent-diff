# Reviewing an assistant's work

You review what an AI assistant did for a user in an online service. You get the user's request, every step the
assistant took (its visible reasoning, each command it ran and the response), its final reply, and the changes it made
to the account's data.

Decide one thing: **did the assistant do what the user asked?**

Answer with `passed` (true or false) and a note of one to three sentences that cites the steps deciding it.


---

# What an assistant did in Linear

## The user's request
Add the comment 'This cannot slip.' to the overdue 'Renew TLS certificate' issue.

## What the test's author expected
The assistant adds the comment to the still-open past-due issue; the completed past-due issue and the open future-dated issue are not overdue.

## The assistant's steps
#### Step 1
Reasoning: The user wants to add a comment to an overdue Linear issue called "Renew TLS certificate". This falls under the Linear skill. First, let's read SKILL.md.
Command: read {"path": "~/.openclaw-state/f47398fafc6443d6/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: The skill states that authentication is handled via proxy, and to use a placeholder token. Let's use GraphQL to find the "Renew TLS certificate" issue. First, we need to search for the issue. Let's use a GraphQL query with curl.

Let's construct the query. Linear's GraphQL API:

```graphql
{
  issues(first: 20, query: "Renew TLS certificate") {
    nodes {
      id
      identifier
      title
      state { name }
      updatedAt
    }
  }
}
```

I'll give it a try.
Command: curl -sS https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ issues(first: 20, query: \"Renew TLS certificate\") { nodes { id identifier title state { name } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Unknown argument 'query' on field 'Query.issues'.\",\"locations\":[{\"line\":1,\"column\":21}]}]}"}

#### Step 3
Reasoning: The `query` argument is not valid on `issues`. Let me check the Linear API — `issues` should have a `filter` argument. Let me use a filter with `search: {query: "Renew TLS certificate"}`.
Command: curl -sS https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ issues(first: 20, filter: {search: {query: \"Renew TLS certificate\"}}) { nodes { id identifier title state { name } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Field 'search' is not defined by type 'IssueFilter'.\",\"locations\":[{\"line\":1,\"column\":30}]}]}"}

#### Step 4
Reasoning: The Linear API's issue filter has fields like: `assignee`, `creator`, `state`, `label`, `team`, `project`, `dueDate`, etc. Search isn't a filter field. There's a top-level `query` argument for some fields... Actually, in Linear's GraphQL, `Query.issues` accepts a `filter` argument, but search might be a separate argument. For now, let me try fetching all issues and grepping.
Command: curl -sS https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ issues(first: 50) { nodes { id identifier title state { name } updatedAt } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"i-d1\",\"identifier\":\"WEB-2\",\"title\":\"Renew TLS certificate\",\"state\":{\"name\":\"Done\"},\"updatedAt\":\"2026-06-01T09:00:00\"},{\"id\":\"i-d2\",\"identifier\":\"WEB-3\",\"title\":\"Renew TLS certificate\",\"state\":{\"name\":\"Todo\"},\"updatedAt\":\"2026-06-01T09:00:00\"},{\"id\":\"i-t\",\"identifier\":\"WEB-1\",\"title\":\"Renew TLS certificate\",\"state\":{\"name\":\"Todo\"},\"updatedAt\":\"2026-06-01T09:00:00\"}]}}}"}

#### Step 5
Reasoning: There are 3 issues titled "Renew TLS Certificate." I need the one that's overdue. I'll get the details including dueDate, priority, etc.
Command: curl -sS https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ issues(first: 50) { nodes { id identifier title state { name } dueDate startedAt priority createdAt updatedAt } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"i-d1\",\"identifier\":\"WEB-2\",\"title\":\"Renew TLS certificate\",\"state\":{\"name\":\"Done\"},\"dueDate\":\"2026-09-10\",\"startedAt\":null,\"priority\":0.0,\"createdAt\":\"2026-06-01T09:00:00\",\"updatedAt\":\"2026-06-01T09:00:00\"},{\"id\":\"i-d2\",\"identifier\":\"WEB-3\",\"title\":\"Renew TLS certificate\",\"state\":{\"name\":\"Todo\"},\"dueDate\":\"2026-12-01\",\"startedAt\":null,\"priority\":0.0,\"createdAt\":\"2026-06-01T09:00:00\",\"updatedAt\":\"2026-06-01T09:00:00\"},{\"id\":\"i-t\",\"identifier\":\"WEB-1\",\"title\":\"Renew TLS certificate\",\"state\":{\"name\":\"Todo\"},\"dueDate\":\"2026-09-10\",\"startedAt\":null,\"priority\":0.0,\"createdAt\":\"2026-06-01T09:00:00\",\"updatedAt\":\"2026-06-01T09:00:00\"}]}}}"}

#### Step 6
Reasoning: Today is 2026-09-28. Overdue means the due date is before today AND not completed:
- i-d1 (WEB-2): Due 2026-09-10 but state is "Done" — completed so not "overdue".
- i-d2 (WEB-3): Due 2026-12-01, Todo — not overdue.
- i-t (WEB-1): Due 2026-09-10, Todo — overdue (due date has passed, still open).

Therefore the target issue is i-t (WEB-1). Adding a comment.

Found it — WEB-1 (due 2026-09-10, still open, so overdue; WEB-2 with the same date is already Done). Adding the comment:
Command: curl -sS https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"mutation { commentCreate(input: { issueId: \"i-t\", body: \"This cannot slip.\" }) { success comment { id body } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"commentCreate\":{\"success\":true,\"comment\":{\"id\":\"493882ff-2e0e-4107-bf79-900ccf6d379b\",\"body\":\"This cannot slip.\"}}}}"}

#### Step 7
Reasoning: I need to look into this further. Let me check the details.

Done. Added the comment **"This cannot slip."** to **WEB-1 – Renew TLS certificate** (due 2026-09-10, the open/overdue one).

Note: there are three issues with that title — WEB-2 was also due 09-10 but is marked Done, and WEB-3 is due 12-01, so WEB-1 was the only ambiguous-free match.
Command: 
Response: null

## The assistant's final reply
Done. Added the comment **"This cannot slip."** to **WEB-1 – Renew TLS certificate** (due 2026-09-10, the open/overdue one).

Note: there are three issues with that title — WEB-2 was also due 09-10 but is marked Done, and WEB-3 is due 12-01, so WEB-1 was the only ambiguous-free match.

## Changes it made to the account's data
- INSERT comments: {"id": "493882ff-2e0e-4107-bf79-900ccf6d379b", "body": "This cannot slip.", "createdAt": "2026-09-28T20:00:38.158648", "issueId": "i-t", "updatedAt": "2026-09-28T20:00:38.158648", "userId": "u-actor"}

Did the assistant do what the user asked, as the test's author expected?