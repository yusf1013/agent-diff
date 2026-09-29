# Reviewing an assistant's work

You review what an AI assistant did for a user in an online service. You get the user's request, every step the
assistant took (its visible reasoning, each command it ran and the response), its final reply, and the changes it made
to the account's data.

Decide one thing: **did the assistant do what the user asked?**

Answer with `passed` (true or false) and a note of one to three sentences that cites the steps deciding it.


---

# What an assistant did in Linear

## The user's request
Add the comment 'Customer waiting on this.' to the 'Export dashboard CSV' issue due 2026-10-20 with an estimate of 8 points.

## What the test's author expected
The assistant adds the comment to the only 'Export dashboard CSV' issue that is both due 2026-10-20 and estimated at 8 points; each decoy matches only one of the two attributes.

## The assistant's steps
#### Step 1
Reasoning: The user wants to add a comment to a Linear issue. Let's use the Linear skill.

First, let's read SKILL.md.
Command: read {"path": "~/.openclaw-state/c028e5cc1f41409f/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: SKILL.md doesn't have the detailed API schema. I need to search for the "Export dashboard CSV" issue with due date 2026-10-20 and estimate 8 points. Let me use Linear's GraphQL API via curl with a placeholder token.

First, I need to query the issue. Linear's GraphQL supports `issues(filter: {...})`. The issue has a dueDate and estimate. Let me try querying:

```graphql
query {
  issues(first: 20, filter: {
    title: {contains: "Export dashboard CSV"}
  }) {
    nodes {
      id
      identifier
      title
      dueDate
      estimate
      team { key name }
      workflowState { name }
      url
    }
  }
}
```

Estimate is in points (integer). Due date is 2026-10-20.

Let me run that first.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: <TOKEN>' -d '{"query":"{ issues(first: 20, filter: { title: { contains: \"Export dashboard CSV\" } }) { nodes { id identifier title dueDate estimate url team { key name } workflowState { name } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'workflowState' on type 'Issue'.\",\"locations\":[{\"line\":1,\"column\":147}]}]}"}

#### Step 3
Reasoning: The field name is wrong — is it `state { name }` or `workflowState`? In Linear GraphQL, the field on Issue is `state`. Let's fix it.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: <TOKEN>' -d '{"query":"{ issues(first: 20, filter: { title: { contains: \"Export dashboard CSV\" } }) { nodes { id identifier title dueDate estimate url team { key name } state { name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"i-d1\",\"identifier\":\"WEB-2\",\"title\":\"Export dashboard CSV\",\"dueDate\":\"2026-10-20\",\"estimate\":3.0,\"url\":\"https://linear.app/northwind/issue/WEB-2\",\"team\":{\"key\":\"WEB\",\"name\":\"Web\"},\"state\":{\"name\":\"Todo\"}},{\"id\":\"i-d2\",\"identifier\":\"WEB-3\",\"title\":\"Export dashboard CSV\",\"dueDate\":\"2026-11-05\",\"estimate\":8.0,\"url\":\"https://linear.app/northwind/issue/WEB-3\",\"team\":{\"key\":\"WEB\",\"name\":\"Web\"},\"state\":{\"name\":\"Todo\"}},{\"id\":\"i-t\",\"identifier\":\"WEB-1\",\"title\":\"Export dashboard CSV\",\"dueDate\":\"2026-10-20\",\"estimate\":8.0,\"url\":\"https://linear.app/northwind/issue/WEB-1\",\"team\":{\"key\":\"WEB\",\"name\":\"Web\"},\"state\":{\"name\":\"Todo\"}}]}}}"}

#### Step 4
Reasoning: I found three issues that match the title "Export Dashboard CSV":

1. WEB-2: due date 2026-10-20, estimate 3.0
2. WEB-3: due date 2026-11-05, estimate 8.0
3. WEB-1: due date 2026-10-20, estimate 8.0

The user's request is "the issue 'Export Dashboard CSV' with due date 2026-10-20 and estimate 8 points."

- WEB-1: due date 2026-10-20 ✓, estimate 8 ✓
- WEB-2: due date 2026-10-20 ✓, estimate 3 ✗
- WEB-3: due date 2026-11-05 ✗, estimate 8 ✓

Therefore, WEB-1 (i-t) is the unique match on both criteria: due date 2026-10-20 AND estimate 8.

The user's description is a filter, and since it uniquely identifies WEB-1, I should add the comment there. Since it matches both conditions, it's not ambiguous.

Add a comment to issue i-t: "Customer is waiting on this."

Found 3 issues with that title. Matching on both due date (2026-10-20) and estimate (8) uniquely identifies **WEB-1**. Adding the comment now:
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: <TOKEN>' -d '{"query":"mutation { commentCreate(issueId: \"i-t\", body: \"Customer waiting on this.\") { id body } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Unknown argument 'issueId' on field 'Mutation.commentCreate'.\",\"locations\":[{\"line\":1,\"column\":26}]},{\"message\":\"Unknown argument 'body' on field 'Mutation.commentCreate'.\",\"locations\":[{\"line\":1,\"column\":42}]},{\"message\":\"Cannot query field 'id' on type 'CommentPayload'.\",\"locations\":[{\"line\":1,\"column\":79}]},{\"message\":\"Cannot query field 'body' on type 'CommentPayload'.\",\"locations\":[{\"line\":1,\"column\":82}]},{\"message\":\"Field 'commentCreate' argument 'input' of type 'CommentCreateInput!' is required, but it was not provided.\",\"locations\":[{\"line\":1,\"column\":12}]}]}"}

#### Step 5
Reasoning: commentCreate takes an `input` of type CommentCreateInput. I need to investigate the fields of that input type.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: <TOKEN>' -d '{"query":"{ __type(name: \"CommentCreateInput\") { inputFields { name type { name kind ofType { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"inputFields\":[{\"name\":\"body\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"bodyData\",\"type\":{\"name\":\"JSON\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"createAsUser\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"createOnSyncedSlackThread\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"createdAt\",\"type\":{\"name\":\"DateTime\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"displayIconUrl\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"doNotSubscribeToIssue\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"documentContentId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"id\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"initiativeUpdateId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"issueId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"parentId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"postId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"projectUpdateId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"quotedText\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"subscriberIds\",\"type\":{\"name\":null,\"kind\":\"LIST\",\"ofType\":{\"name\":null}}}]}}}"}

#### Step 6
Reasoning: The input field uses `input`. Let's retry the mutation with the correct input. Also, let's check the fields of CommentPayload — probably `success` and `comment`. Let's just give it a try.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -H 'Authorization: <TOKEN>' -d '{"query":"mutation { commentCreate(input: { issueId: \"i-t\", body: \"Customer waiting on this.\" }) { success comment { id body } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"commentCreate\":{\"success\":true,\"comment\":{\"id\":\"f91e846b-3545-4a72-bf8d-8d7044e70ca0\",\"body\":\"Customer waiting on this.\"}}}}"}

#### Step 7
Reasoning: Done. The comment has been added to WEB-1 (issue i-t). There were 3 issues with the same title, but WEB-1 is the only one that matches both the due date 2026-10-20 and the estimate of 8 points. WEB-2 has a due date of 2026-10-20 but its estimate is 3, and WEB-3 has an estimate of 8 but its due date is 2026-11-05. I'll report this clearly.

Done — comment added to **WEB-1 "Export dashboard CSV"** (due 2026-10-20, 8 pts): https://linear.app/northwind/issue/WEB-1

Heads up: there were 3 issues titled "Export dashboard CSV". Only WEB-1 matches both the due date and the 8-point estimate — WEB-2 (due 2026-10-20) is 3 points, and WEB-3 (8 points) is due 2026-11-05. If you meant one of those instead, say the word and I'll move the comment.
Command: 
Response: null

## The assistant's final reply
Done — comment added to **WEB-1 "Export dashboard CSV"** (due 2026-10-20, 8 pts): https://linear.app/northwind/issue/WEB-1

Heads up: there were 3 issues titled "Export dashboard CSV". Only WEB-1 matches both the due date and the 8-point estimate — WEB-2 (due 2026-10-20) is 3 points, and WEB-3 (8 points) is due 2026-11-05. If you meant one of those instead, say the word and I'll move the comment.

## Changes it made to the account's data
- INSERT comments: {"id": "f91e846b-3545-4a72-bf8d-8d7044e70ca0", "body": "Customer waiting on this.", "createdAt": "2026-09-28T19:52:19.708304", "issueId": "i-t", "updatedAt": "2026-09-28T19:52:19.708304", "userId": "u-actor"}

Did the assistant do what the user asked, as the test's author expected?