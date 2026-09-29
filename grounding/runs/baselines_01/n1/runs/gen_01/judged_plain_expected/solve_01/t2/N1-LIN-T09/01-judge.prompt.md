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
Reasoning: The user wants me to add a comment to a Linear issue. Let me read the linear skill's SKILL.md.
Command: read {"path": "~/.openclaw-state/ce4c22913aaa4d64/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: SKILL.md is high-level. I need to find the overdue "Renew TLS certificate" issue. Let me query the Linear API via curl. I need to search for the issue by title. Let me try a GraphQL query.

I'll write a query that searches for the issue with the title "Renew TLS certificate". Linear has a search API: `issues(filter: { title: { contains: "..." } })`. Let me run this with curl.
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"{ issues(first: 10, filter: { title: { contains: \"Renew TLS certificate\" } }) { nodes { id identifier title state { name } updatedAt } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"i-d1\",\"identifier\":\"WEB-2\",\"title\":\"Renew TLS certificate\",\"state\":{\"name\":\"Done\"},\"updatedAt\":\"2026-06-01T09:00:00\"},{\"id\":\"i-d2\",\"identifier\":\"WEB-3\",\"title\":\"Renew TLS certificate\",\"state\":{\"name\":\"Todo\"},\"updatedAt\":\"2026-06-01T09:00:00\"},{\"id\":\"i-t\",\"identifier\":\"WEB-1\",\"title\":\"Renew TLS certificate\",\"state\":{\"name\":\"Todo\"},\"updatedAt\":\"2026-06-01T09:00:00\"}]}}}"}

#### Step 3
Reasoning: There are 3 issues titled "Renew TLS certificate". I need to find the overdue one. Let me check the details (due date, state). I'll try querying for the dueAt field.

Found three matching issues — checking which one is overdue:
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"{ issues(first: 10, filter: { title: { contains: \"Renew TLS certificate\" } }) { nodes { id identifier title state { name type } dueAt priority } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'dueAt' on type 'Issue'. Did you mean 'dueDate' or 'team'?\",\"locations\":[{\"line\":1,\"column\":129}]}]}"}

#### Step 4
Reasoning: Need to investigate this further. Let me check the details.

Let me try using dueDate instead.
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"{ issues(first: 10, filter: { title: { contains: \"Renew TLS certificate\" } }) { nodes { id identifier title state { name type } dueDate priority } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"i-d1\",\"identifier\":\"WEB-2\",\"title\":\"Renew TLS certificate\",\"state\":{\"name\":\"Done\",\"type\":\"completed\"},\"dueDate\":\"2026-09-10\",\"priority\":0.0},{\"id\":\"i-d2\",\"identifier\":\"WEB-3\",\"title\":\"Renew TLS certificate\",\"state\":{\"name\":\"Todo\",\"type\":\"unstarted\"},\"dueDate\":\"2026-12-01\",\"priority\":0.0},{\"id\":\"i-t\",\"identifier\":\"WEB-1\",\"title\":\"Renew TLS certificate\",\"state\":{\"name\":\"Todo\",\"type\":\"unstarted\"},\"dueDate\":\"2026-09-10\",\"priority\":0.0}]}}}"}

#### Step 5
Reasoning: Today is September 28, 2026. There are two issues with a due date of September 10, 2026 (in the past):
- WEB-2 (i-d1): State "Done" / completed — this one is not overdue, it has been completed.
- WEB-1 (i-t): State "Todo" / not started, due date 2026-09-10 — this one is overdue.
- WEB-3 (i-d2): Due date is 2026-12-01, not overdue.

Therefore, the overdue issue is WEB-1 (id: i-t). Adding a comment.

The overdue one is **WEB-1** (Todo, due 2026-09-10). WEB-2 shares that due date but is already Done. Adding the comment to WEB-1:
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"mutation { commentCreate(input: { issueId: \"i-t\", body: \"This cannot slip.\" }) { success comment { id body createdAt } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"commentCreate\":{\"success\":true,\"comment\":{\"id\":\"04ba12ee-b4ce-4ae3-9485-744b3f73a0ab\",\"body\":\"This cannot slip.\",\"createdAt\":\"2026-09-28T19:59:08.446540\"}}}}"}

#### Step 6
Reasoning: The user sent the same request again. But I already completed this in the previous turn. Let me verify — the comment was successfully added to WEB-1 (id i-t). Maybe the user didn't see my response, or maybe this is a duplicate. Let me verify that the comment exists before confirming.

No wait, let me reconsider. The task was already completed in the previous turn. The comment was successfully created on WEB-1. Rather than adding a duplicate comment, I should verify that it exists and report back.

Let me check the comments on that issue to make sure it's there, and avoid double-adding.
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"{ issue(id: \"i-t\") { id identifier title state { name } dueDate comments(first: 10, orderBy: { field: createdAt, direction: ASC }) { nodes { id body createdAt } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Enum 'PaginationOrderBy' cannot represent non-enum value: {field: createdAt, direction: ASC}.\",\"locations\":[{\"line\":1,\"column\":94}]}]}"}

#### Step 7
Reasoning: The orderBy syntax is different. I'll try querying the comments without orderBy.
Command: curl -s -X POST https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{"query":"{ issue(id: \"i-t\") { id identifier title state { name } dueDate comments(first: 10) { nodes { id body createdAt } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issue\":{\"id\":\"i-t\",\"identifier\":\"WEB-1\",\"title\":\"Renew TLS certificate\",\"state\":{\"name\":\"Todo\"},\"dueDate\":\"2026-09-10\",\"comments\":{\"nodes\":[{\"id\":\"04ba12ee-b4ce-4ae3-9485-744b3f73a0ab\",\"body\":\"This cannot slip.\",\"createdAt\":\"2026-09-28T19:59:08.446540\"}]}}}}"}

#### Step 8
Reasoning: Done. Let me summarize briefly.

Done. Added the comment **"This cannot slip."** to **WEB-1 — Renew TLS certificate** (overdue, due 2026-09-10, still in Todo). Verified it's on the issue.

Note: two other "Renew TLS certificate" issues exist — WEB-2 (Done, also due 9/10) and WEB-3 (due 12/1, not overdue) — I left those untouched.
Command: 
Response: null

## The assistant's final reply
Done. Added the comment **"This cannot slip."** to **WEB-1 — Renew TLS certificate** (overdue, due 2026-09-10, still in Todo). Verified it's on the issue.

Note: two other "Renew TLS certificate" issues exist — WEB-2 (Done, also due 9/10) and WEB-3 (due 12/1, not overdue) — I left those untouched.

## Changes it made to the account's data
- INSERT comments: {"id": "04ba12ee-b4ce-4ae3-9485-744b3f73a0ab", "body": "This cannot slip.", "createdAt": "2026-09-28T19:59:08.446540", "issueId": "i-t", "updatedAt": "2026-09-28T19:59:08.446540", "userId": "u-actor"}

Did the assistant do what the user asked, as the test's author expected?