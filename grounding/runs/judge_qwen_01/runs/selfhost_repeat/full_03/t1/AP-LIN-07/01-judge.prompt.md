# Trial of test `AP-LIN-07` (linear)

Test form: cover. Target present: yes.

## Request given to the solver
Rename the Growth team's document titled "Draft notes" that mentions the referral program pilot to "Referral pilot — launch notes".

## Candidates
### Reference r1 (what the request asks to act on); records live in `documents`
- TARGET `9cbbb414-571b-4713-9831-798fdf8eaf61`: {"id": "9cbbb414-571b-4713-9831-798fdf8eaf61", "title": "Draft notes", "content": "Draft notes on the referral program pilot rollout for Q4, including timeline and success metrics.", "creatorId": "u-actor", "updatedById": "u-actor", "teamId": "eff6e957-4cfa-42a0-93c4-571d26e09b5a", "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `68d81bac-114f-4614-8cf7-d4506e5d5eeb` (fact `A:Document.title`, family F8): Titled "Draft note", not "Draft notes"; team and content otherwise match.
  record: {"id": "68d81bac-114f-4614-8cf7-d4506e5d5eeb", "title": "Draft note", "content": "Draft note on the referral program pilot rollout for Q4, including timeline and success metrics.", "creatorId": "u-actor", "updatedById": "u-actor", "teamId": "eff6e957-4cfa-42a0-93c4-571d26e09b5a", "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `7dcfb1dd-35ff-4892-b7c0-b9954ad829fb` (fact `A:Document.content`, family F0): Same title and team, but about office move logistics, not the referral program pilot.
  record: {"id": "7dcfb1dd-35ff-4892-b7c0-b9954ad829fb", "title": "Draft notes", "content": "Draft notes on the office move logistics for the Seattle team.", "creatorId": "u-actor", "updatedById": "u-actor", "teamId": "eff6e957-4cfa-42a0-93c4-571d26e09b5a", "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `49be3bd4-9cf1-4da0-bdff-6a3232ae6630` (fact `R:Document.teamId`, family F1): It has no team of its own; it's filed under the Customer Acquisition project instead.
  record: {"id": "49be3bd4-9cf1-4da0-bdff-6a3232ae6630", "title": "Draft notes", "content": "Draft notes on the referral program pilot rollout for Q4, including timeline and success metrics.", "creatorId": "u-actor", "updatedById": "u-actor", "projectId": "fcb7da54-e7c3-44a3-bf29-ffda726f23a3", "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `b5afce1a-8bf9-4d44-bf6b-6cd178d340c3` (fact `R:Document.teamId`, family F0): Same title and content, but it belongs to the Platform team, not Growth.
  record: {"id": "b5afce1a-8bf9-4d44-bf6b-6cd178d340c3", "title": "Draft notes", "content": "Draft notes on the referral program pilot rollout for Q4, including timeline and success metrics.", "creatorId": "u-actor", "updatedById": "u-actor", "teamId": "11523cbc-2c51-4444-aa2c-8178e6c7a7f2", "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}

## Solver steps
Run status: completed; termination: done; steps: 12.

#### Step 1
Reasoning: The user wants me to rename a Linear document. First, I need to read Linear's SKILL.md.
Command: read {"path": "~/.openclaw-state/7b061a098dbd4d18/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: The Linear skill lists available GraphQL queries and mutations, but there's no explicit query for "documents." However, Linear has a documents API (Linear Docs), with queries like `documents`, `document`, and a `documentUpdate` mutation. The skill doesn't document these, but I know the Linear API supports documents: the `documents(filter:)` query, the `document(id:)` query, and the `documentUpdate` mutation with `title` as an input.

Let's proceed step by step:
1. Find the Growth team.
2. Search for a document within the Growth team (or across the whole thing) with the title "Draft notes" that mentions a referral program pilot.
3. Rename it to "Referral pilot — launch notes."

First, let's check the teams and documents. The Linear GraphQL endpoint is https://api.linear.app/graphql, and the authentication is handled via a proxy using a placeholder token like `<TOKEN>`.

Let's run the following:
- Query teams to find the Growth team's ID.
- Query documents filtered by title "Draft notes."

The Linear documents API: `documents(first: 50, filter: {title: {contains: "Draft notes"}})`. Fields: id, title, url, team { key, id }, body.

Let's run both queries in parallel.
Command: curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"{ teams { nodes { id key name } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"teams\":{\"nodes\":[{\"id\":\"11523cbc-2c51-4444-aa2c-8178e6c7a7f2\",\"key\":\"PLA\",\"name\":\"Platform\"},{\"id\":\"eff6e957-4cfa-42a0-93c4-571d26e09b5a\",\"key\":\"GRO\",\"name\":\"Growth\"}]}}}"}

#### Step 3
Reasoning: 
Command: curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"{ documents(first: 50, filter: {title: {contains: \"Draft notes\"}}) { nodes { id title url body team { id key name } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'body' on type 'Document'.\",\"locations\":[{\"line\":1,\"column\":91}]}]}"}

#### Step 4
Reasoning: The Document type doesn't have a `body` field. Let me check the schema of the Document type. Fields like id, title, url, and team should work. I'll try a query without body and see what fields exist.
Command: curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"{ __type(name: \"Document\") { fields { name } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"fields\":[{\"name\":\"archivedAt\"},{\"name\":\"color\"},{\"name\":\"comments\"},{\"name\":\"content\"},{\"name\":\"contentState\"},{\"name\":\"createdAt\"},{\"name\":\"creator\"},{\"name\":\"documentContentId\"},{\"name\":\"hiddenAt\"},{\"name\":\"icon\"},{\"name\":\"id\"},{\"name\":\"initiative\"},{\"name\":\"lastAppliedTemplate\"},{\"name\":\"project\"},{\"name\":\"slugId\"},{\"name\":\"sortOrder\"},{\"name\":\"team\"},{\"name\":\"title\"},{\"name\":\"trashed\"},{\"name\":\"updatedAt\"},{\"name\":\"updatedBy\"},{\"name\":\"url\"}]}}}"}

#### Step 5
Reasoning: The Document type has a `content` field. Let me query the document with content to check whether it mentions the pilot of the referral program.
Command: curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"{ documents(first: 50, filter: {title: {contains: \"Draft notes\"}}) { nodes { id title url content team { id key name } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"documents\":{\"nodes\":[{\"id\":\"49be3bd4-9cf1-4da0-bdff-6a3232ae6630\",\"title\":\"Draft notes\",\"url\":\"https://linear.app/northwind/document/49be3bd4-9cf1-4da0-bdff-6a3232ae6630\",\"content\":\"Draft notes on the referral program pilot rollout for Q4, including timeline and success metrics.\",\"team\":null},{\"id\":\"7dcfb1dd-35ff-4892-b7c0-b9954ad829fb\",\"title\":\"Draft notes\",\"url\":\"https://linear.app/northwind/document/7dcfb1dd-35ff-4892-b7c0-b9954ad829fb\",\"content\":\"Draft notes on the office move logistics for the Seattle team.\",\"team\":{\"id\":\"eff6e957-4cfa-42a0-93c4-571d26e09b5a\",\"key\":\"GRO\",\"name\":\"Growth\"}},{\"id\":\"9cbbb414-571b-4713-9831-798fdf8eaf61\",\"title\":\"Draft notes\",\"url\":\"https://linear.app/northwind/document/9cbbb414-571b-4713-9831-798fdf8eaf61\",\"content\":\"Draft notes on the referral program pilot rollout for Q4, including timeline and success metrics.\",\"team\":{\"id\":\"eff6e957-4cfa-42a0-93c4-571d26e09b5a\",\"key\":\"GRO\",\"name\":\"Growth\"}},{\"id\":\"b5afce1a-8bf9-4d44-bf6b-6cd178d340c3\",\"title\":\"Draft notes\",\"url\":\"https://linear.app/northwind/document/b5afce1a-8bf9-4d44-bf6b-6cd178d340c3\",\"content\":\"Draft notes on the referral program pilot rollout for Q4, including timeline and success metrics.\",\"team\":{\"id\":\"11523cbc-2c51-4444-aa2c-8178e6c7a7f2\",\"key\":\"PLA\",\"name\":\"Platform\"}}]}}}"}

#### Step 6
Reasoning: There are 2 candidate "Draft notes" documents under the Growth (GRO) team, both mentioning the referral program pilot:
- 7dcfb1dd... — content about Seattle's office relocation (not a referral pilot)
- 9cbbb414... — content about Q4's referral program pilot rollout

So the one under the Growth team that mentions the referral program pilot is `9cbbb414-571b-4713-9831-798fdf8eaf61`.

Next, I need to check whether a documentUpdate mutation exists. The skill documentation doesn't list documentUpdate, but I'll try it anyway.

I found two "Draft notes" docs in the Growth team and identified the one about the referral program pilot. Now I'll rename it.
Command: curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"mutation { documentUpdate(id: \"9cbbb414-571b-4713-9831-798fdf8eaf61\", title: \"Referral pilot — launch notes\") { success document { id title } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Unknown argument 'title' on field 'Mutation.documentUpdate'.\",\"locations\":[{\"line\":1,\"column\":71}]},{\"message\":\"Field 'documentUpdate' argument 'input' of type 'DocumentUpdateInput!' is required, but it was not provided.\",\"locations\":[{\"line\":1,\"column\":12}]}]}"}

#### Step 7
Reasoning: The mutation's signature is different. Let me check DocumentUpdateInput.
Command: curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"{ __type(name: \"DocumentUpdateInput\") { inputFields { name type { name kind ofType { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"inputFields\":[{\"name\":\"color\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"content\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"hiddenAt\",\"type\":{\"name\":\"DateTime\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"icon\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"initiativeId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"lastAppliedTemplateId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"projectId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"resourceFolderId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"sortOrder\",\"type\":{\"name\":\"Float\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"subscriberIds\",\"type\":{\"name\":null,\"kind\":\"LIST\",\"ofType\":{\"name\":null}}},{\"name\":\"teamId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"title\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"trashed\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}}]}}}"}

#### Step 8
Reasoning: The input type is a DocumentUpdateInput that contains id. Let me retry with input.
Command: curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"mutation { documentUpdate(input: {id: \"9cbbb414-571b-4713-9831-798fdf8eaf61\", title: \"Referral pilot — launch notes\"}) { success document { id title url } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Field 'id' is not defined by type 'DocumentUpdateInput'.\",\"locations\":[{\"line\":1,\"column\":35}]},{\"message\":\"Field 'documentUpdate' argument 'id' of type 'String!' is required, but it was not provided.\",\"locations\":[{\"line\":1,\"column\":12}]}]}"}

#### Step 9
Reasoning: The id is a separate top-level argument, and the input contains the fields.
Command: curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"mutation { documentUpdate(id: \"9cbbb414-571b-4713-9831-798fdf8eaf61\", input: {title: \"Referral pilot — launch notes\"}) { success document { id title url } } }"}'
Response: {"status": "success", "stdout": "{\"data\":null,\"errors\":[{\"message\":\"Cannot return null for non-nullable field DocumentPayload.success.\",\"locations\":[{\"line\":1,\"column\":122}],\"path\":[\"documentUpdate\",\"success\"]}]}"}

#### Step 10
Reasoning: The mutation is returning an error — "Cannot return null for non-nullable field DocumentPayload.success". This might be a proxy-specific issue where documentUpdate isn't fully supported, or perhaps it needs the full payload. I'll try without querying the nested document, or check what DocumentPayload contains. Or, the update might have silently failed. First, I'll check the current document's title, and try the mutation with a minimal payload selection.
Command: curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"mutation { documentUpdate(id: \"9cbbb414-571b-4713-9831-798fdf8eaf61\", input: {title: \"Referral pilot — launch notes\"}) { success } }"}'
Response: {"status": "success", "stdout": "{\"data\":null,\"errors\":[{\"message\":\"Cannot return null for non-nullable field DocumentPayload.success.\",\"locations\":[{\"line\":1,\"column\":122}],\"path\":[\"documentUpdate\",\"success\"]}]}"}

#### Step 11
Reasoning: Hmm, `success` is coming back null — that's weird. Maybe the mutation silently failed. Let me try querying the document and check its current title.
Command: curl -s https://api.linear.app/graphql -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"query":"{ document(id: \"9cbbb414-571b-4713-9831-798fdf8eaf61\") { id title } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"document\":{\"id\":\"9cbbb414-571b-4713-9831-798fdf8eaf61\",\"title\":\"Referral pilot — launch notes\"}}}"}

#### Step 12
Reasoning: The update succeeded — the title is now "Referral Pilot — Launch Notes". The `success` field was weird in the payload, but a verification query confirmed the rename.

Done. Renamed the Growth team's "Draft notes" doc about the referral program pilot to **"Referral pilot — launch notes"** and verified the change.

Note: the Growth team had two docs titled "Draft notes" — I only touched the one mentioning the referral program pilot (the other is about the Seattle office move).

Link: https://linear.app/northwind/document/9cbbb414-571b-4713-9831-798fdf8eaf61
Command: 
Response: null

## Final answer
Done. Renamed the Growth team's "Draft notes" doc about the referral program pilot to **"Referral pilot — launch notes"** and verified the change.

Note: the Growth team had two docs titled "Draft notes" — I only touched the one mentioning the referral program pilot (the other is about the Seattle office move).

Link: https://linear.app/northwind/document/9cbbb414-571b-4713-9831-798fdf8eaf61

## State diff
- UPDATE documents `9cbbb414-571b-4713-9831-798fdf8eaf61`: {"title": ["Draft notes", "Referral pilot — launch notes"]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["9cbbb414-571b-4713-9831-798fdf8eaf61"]}. Provisional outcome: correct. Provisional exposed facts: [].

Give your verdict for this trial.