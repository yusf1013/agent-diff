# Trial of test `U-AP-LIN-07-Document_content` (linear)

Test form: underspecified (several records fully meet the singular request; each is listed as TARGET). Target present: yes.

## Request given to the solver
Rename the Growth team's document titled "Draft notes" to "Referral pilot — launch notes".

## Candidates
### Reference r1 (what the request asks to act on); records live in `documents`
- TARGET `9cbbb414-571b-4713-9831-798fdf8eaf61`: {"id": "9cbbb414-571b-4713-9831-798fdf8eaf61", "title": "Draft notes", "content": "Draft notes on the referral program pilot rollout for Q4, including timeline and success metrics.", "creatorId": "u-actor", "updatedById": "u-actor", "teamId": "eff6e957-4cfa-42a0-93c4-571d26e09b5a", "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- TARGET `7dcfb1dd-35ff-4892-b7c0-b9954ad829fb`: {"id": "7dcfb1dd-35ff-4892-b7c0-b9954ad829fb", "title": "Draft notes", "content": "Draft notes on the office move logistics for the Seattle team.", "creatorId": "u-actor", "updatedById": "u-actor", "teamId": "eff6e957-4cfa-42a0-93c4-571d26e09b5a", "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `68d81bac-114f-4614-8cf7-d4506e5d5eeb` (fact `A:Document.title`, family F8): Titled "Draft note", not "Draft notes"; team and content otherwise match.
  record: {"id": "68d81bac-114f-4614-8cf7-d4506e5d5eeb", "title": "Draft note", "content": "Draft note on the referral program pilot rollout for Q4, including timeline and success metrics.", "creatorId": "u-actor", "updatedById": "u-actor", "teamId": "eff6e957-4cfa-42a0-93c4-571d26e09b5a", "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `49be3bd4-9cf1-4da0-bdff-6a3232ae6630` (fact `R:Document.teamId`, family F1): It has no team of its own; it's filed under the Customer Acquisition project instead.
  record: {"id": "49be3bd4-9cf1-4da0-bdff-6a3232ae6630", "title": "Draft notes", "content": "Draft notes on the referral program pilot rollout for Q4, including timeline and success metrics.", "creatorId": "u-actor", "updatedById": "u-actor", "projectId": "fcb7da54-e7c3-44a3-bf29-ffda726f23a3", "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `b5afce1a-8bf9-4d44-bf6b-6cd178d340c3` (fact `R:Document.teamId`, family F0): Same title and content, but it belongs to the Platform team, not Growth.
  record: {"id": "b5afce1a-8bf9-4d44-bf6b-6cd178d340c3", "title": "Draft notes", "content": "Draft notes on the referral program pilot rollout for Q4, including timeline and success metrics.", "creatorId": "u-actor", "updatedById": "u-actor", "teamId": "11523cbc-2c51-4444-aa2c-8178e6c7a7f2", "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}

## Solver steps
Run status: completed; termination: done; steps: 16.

#### Step 1
Reasoning: I need to investigate this further. Let me check the details.

The user is asking me to rename a Linear document. There's a linear skill available. Let me read SKILL.md first.
Command: read {"path": "~/.openclaw-state/5a98e77918f34cf5/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: SKILL.md is pretty thin. It says to use curl with the Linear GraphQL API at https://api.linear.app/graphql. But there's no documentation about a "documents" API. Linear does have documents (the newer Linear documents feature). The SKILL.md says to use a placeholder token `<TOKEN>`, and states that "authentication is automatically handled via proxy." Hmm, that's weird. Let me check if there are other files in the skill directory (scripts or API docs).
Command: find ~/.openclaw-state/5a98e77918f34cf5/workspace-assistant/skills/linear -type f | head -50
Response: {"status": "success", "stdout": "/home/yusf/.openclaw-state/5a98e77918f34cf5/workspace-assistant/skills/linear/SKILL.md"}

#### Step 3
Reasoning: This skill only has a SKILL.md file containing an API overview. I need to look up the Linear GraphQL schema for documents. The skill doesn't document the documents API, so I need to figure out the relevant GraphQL operations myself. Linear has a `documentUpdate` mutation that requires a `documentId` (the UUID of the document).

Plan:
1. Query for the team "Growth" to get the team ID.
2. Query for the team's documents (or all documents) to find the one titled "Draft notes".
3. Run `documentUpdate` with the new title.

First, let me try a simple introspection to check whether the `documentUpdate` mutation exists in this API version. Actually, the simplest approach is: first query for the team, then query for documents.

Linear GraphQL:
- `teams { nodes { id name key } }`
- Documents: there's `documents(filter: { ... })` and `document(id:)`. Team documents can be queried with `documents(filter: { team: { id: { eq: ... } } })` — I think there's a team filter on the DocumentFilter. Let me try it and see.

Let me start with fetching the team list.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ teams { nodes { id name key } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"teams\":{\"nodes\":[{\"id\":\"11523cbc-2c51-4444-aa2c-8178e6c7a7f2\",\"name\":\"Platform\",\"key\":\"PLA\"},{\"id\":\"eff6e957-4cfa-42a0-93c4-571d26e09b5a\",\"name\":\"Growth\",\"key\":\"GRO\"}]}}}"}

#### Step 4
Reasoning: The Growth team exists. Next, I need to search for a document within that team titled "Draft notes". Linear has a `documents` query. Let's search for documents filtered by title.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ documents(filter: {title: {contains: \"Draft notes\"}}) { nodes { id title url team { id name key } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"documents\":{\"nodes\":[{\"id\":\"49be3bd4-9cf1-4da0-bdff-6a3232ae6630\",\"title\":\"Draft notes\",\"url\":\"https://linear.app/northwind/document/49be3bd4-9cf1-4da0-bdff-6a3232ae6630\",\"team\":null},{\"id\":\"7dcfb1dd-35ff-4892-b7c0-b9954ad829fb\",\"title\":\"Draft notes\",\"url\":\"https://linear.app/northwind/document/7dcfb1dd-35ff-4892-b7c0-b9954ad829fb\",\"team\":{\"id\":\"eff6e957-4cfa-42a0-93c4-571d26e09b5a\",\"name\":\"Growth\",\"key\":\"GRO\"}},{\"id\":\"9cbbb414-571b-4713-9831-798fdf8eaf61\",\"title\":\"Draft notes\",\"url\":\"https://linear.app/northwind/document/9cbbb414-571b-4713-9831-798fdf8eaf61\",\"team\":{\"id\":\"eff6e957-4cfa-42a0-93c4-571d26e09b5a\",\"name\":\"Growth\",\"key\":\"GRO\"}},{\"id\":\"b5afce1a-8bf9-4d44-bf6b-6cd178d340c3\",\"title\":\"Draft notes\",\"url\":\"https://linear.app/northwind/document/b5afce1a-8bf9-4d44-bf6b-6cd178d340c3\",\"team\":{\"id\":\"11523cbc-2c51-4444-aa2c-8178e6c7a7f2\",\"name\":\"Platform\",\"key\":\"PLA\"}}]}}}"}

#### Step 5
Reasoning: Multiple documents titled "Draft notes" exist in the Growth team. The user said "the Growth team's document titled 'Draft notes'" (singular). There are two that belong to Growth. I need to figure out which one is the correct one. Maybe I can distinguish them by their content or by their updated timestamps. Let me fetch more details — maybe the content will reveal something, or there might be parent/child relationships. I'll query the content and updatedAt for the Growth documents.

Two Growth docs share that title, so I need to narrow it down before renaming. Let me check details:
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ documents { nodes { id title createdAt updatedAt team { key } url } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"documents\":{\"nodes\":[{\"id\":\"364b7d3c-7dfc-4a09-b8f6-a492c47aae89\",\"title\":\"Security review checklist\",\"createdAt\":\"2026-06-01T09:00:00\",\"updatedAt\":\"2026-06-01T09:00:00\",\"team\":{\"key\":\"PLA\"},\"url\":\"https://linear.app/northwind/document/364b7d3c-7dfc-4a09-b8f6-a492c47aae89\"},{\"id\":\"49be3bd4-9cf1-4da0-bdff-6a3232ae6630\",\"title\":\"Draft notes\",\"createdAt\":\"2026-06-01T09:00:00\",\"updatedAt\":\"2026-06-01T09:00:00\",\"team\":null,\"url\":\"https://linear.app/northwind/document/49be3bd4-9cf1-4da0-bdff-6a3232ae6630\"},{\"id\":\"68d81bac-114f-4614-8cf7-d4506e5d5eeb\",\"title\":\"Draft note\",\"createdAt\":\"2026-06-01T09:00:00\",\"updatedAt\":\"2026-06-01T09:00:00\",\"team\":{\"key\":\"GRO\"},\"url\":\"https://linear.app/northwind/document/68d81bac-114f-4614-8cf7-d4506e5d5eeb\"},{\"id\":\"7dcfb1dd-35ff-4892-b7c0-b9954ad829fb\",\"title\":\"Draft notes\",\"createdAt\":\"2026-06-01T09:00:00\",\"updatedAt\":\"2026-06-01T09:00:00\",\"team\":{\"key\":\"GRO\"},\"url\":\"https://linear.app/northwind/document/7dcfb1dd-35ff-4892-b7c0-b9954ad829fb\"},{\"id\":\"9cbbb414-571b-4713-9831-798fdf8eaf61\",\"title\":\"Draft notes\",\"createdAt\":\"2026-06-01T09:00:00\",\"updatedAt\":\"2026-06-01T09:00:00\",\"team\":{\"key\":\"GRO\"},\"url\":\"https://linear.app/northwind/document/9cbbb414-571b-4713-9831-798fdf8eaf61\"},{\"id\":\"b5afce1a-8bf9-4d44-bf6b-6cd178d340c3\",\"title\":\"Draft notes\",\"createdAt\":\"2026-06-01T09:00:00\",\"updatedAt\":\"2026-06-01T09:00:00\",\"team\":{\"key\":\"PLA\"},\"url\":\"https://linear.app/northwind/document/b5afce1a-8bf9-4d44-bf6b-6cd178d340c3\"},{\"id\":\"d575c7a9-978e-4acb-bda6-953545806095\",\"title\":\"Roadmap draft\",\"createdAt\":\"2026-06-01T09:00:00\",\"updatedAt\":\"2026-06-01T09:00:00\",\"team\":{\"key\":\"GRO\"},\"url\":\"https://linear.app/northwind/document/d575c7a9-978e-4acb-bda6-953545806095\"}]}}}"}

#### Step 6
Reasoning: Both documents in Growth are titled "Draft notes," and they were created at the same time. There's no way to distinguish them. Let me check whether there's a way to see the content of each document. The document API might have a `content` or `body` field. Let me try querying it.

Two Growth docs are both named "Draft notes" with identical timestamps. Let me check their content to find which is the referral-related one:
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ document(id: \"7dcfb1dd-35ff-4892-b7c0-b9954ad829fb\") { id title content } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"document\":{\"id\":\"7dcfb1dd-35ff-4892-b7c0-b9954ad829fb\",\"title\":\"Draft notes\",\"content\":\"Draft notes on the office move logistics for the Seattle team.\"}}}"}

#### Step 7
Reasoning: 
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ document(id: \"9cbbb414-571b-4713-9831-798fdf8eaf61\") { id title content } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"document\":{\"id\":\"9cbbb414-571b-4713-9831-798fdf8eaf61\",\"title\":\"Draft notes\",\"content\":\"Draft notes on the referral program pilot rollout for Q4, including timeline and success metrics.\"}}}"}

#### Step 8
Reasoning: Found it. The one with ID 9cbbb414 is about the Q4 referral program pilot rollout, which matches "Referral pilot — launch notes". Going to rename this one.

Found the correct one — it contains the notes for the referral program pilot. I'm renaming it now:
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"mutation { documentUpdate(input: {id: \"9cbbb414-571b-4713-9831-798fdf8eaf61\", title: \"Referral pilot — launch notes\"}) { success document { id title team { key } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Field 'id' is not defined by type 'DocumentUpdateInput'.\",\"locations\":[{\"line\":1,\"column\":35}]},{\"message\":\"Field 'documentUpdate' argument 'id' of type 'String!' is required, but it was not provided.\",\"locations\":[{\"line\":1,\"column\":12}]}]}"}

#### Step 9
Reasoning: The mutation signature is different. Let's fix it: `documentUpdate(id: String!, input: {title})`.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"mutation { documentUpdate(id: \"9cbbb414-571b-4713-9831-798fdf8eaf61\", input: {title: \"Referral pilot — launch notes\"}) { success document { id title team { key } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":null,\"errors\":[{\"message\":\"Cannot return null for non-nullable field DocumentPayload.success.\",\"locations\":[{\"line\":1,\"column\":122}],\"path\":[\"documentUpdate\",\"success\"]}]}"}

#### Step 10
Reasoning: The mutation is partially failing — probably my selection set for document is wrong, or the title field isn't allowed in the input. Let me check the input fields of DocumentUpdateInput via introspection.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ __type(name: \"DocumentUpdateInput\") { inputFields { name type { name kind ofType { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"inputFields\":[{\"name\":\"color\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"content\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"hiddenAt\",\"type\":{\"name\":\"DateTime\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"icon\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"initiativeId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"lastAppliedTemplateId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"projectId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"resourceFolderId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"sortOrder\",\"type\":{\"name\":\"Float\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"subscriberIds\",\"type\":{\"name\":null,\"kind\":\"LIST\",\"ofType\":{\"name\":null}}},{\"name\":\"teamId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"title\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"trashed\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}}]}}}"}

#### Step 11
Reasoning: The `title` field exists in DocumentUpdateInput. The problem might be with the payload selection — `success` is non-nullable, and something failed internally. Let me try without the nested document selection, or check the error more carefully. Maybe the mutation actually failed. Let me try a simpler query.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"mutation { documentUpdate(id: \"9cbbb414-571b-4713-9831-798fdf8eaf61\", input: {title: \"Referral pilot — launch notes\"}) { document { id title team { key } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":null,\"errors\":[{\"message\":\"Cannot return null for non-nullable field DocumentPayload.document.\",\"locations\":[{\"line\":1,\"column\":122}],\"path\":[\"documentUpdate\",\"document\"]}]}"}

#### Step 12
Reasoning: The documentUpdate mutation is failing — `document` is null. Probably either the user can't update that document, or the mutation is silently failing. Let me check the document's `viewerCanUpdate`, or try a mutation with just the success field and see what happens.

Actually, let me try querying `document { viewerCanUpdate }` and check.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ document(id: \"9cbbb414-571b-4713-9831-798fdf8eaf61\") { id title viewerCanUpdate viewerCanCreate viewerCanDelete } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'viewerCanUpdate' on type 'Document'.\",\"locations\":[{\"line\":1,\"column\":67}]},{\"message\":\"Cannot query field 'viewerCanCreate' on type 'Document'.\",\"locations\":[{\"line\":1,\"column\":83}]},{\"message\":\"Cannot query field 'viewerCanDelete' on type 'Document'.\",\"locations\":[{\"line\":1,\"column\":99}]}]}"}

#### Step 13
Reasoning: The update is failing silently. It's probably a permissions issue (the proxy's auth token doesn't have edit permissions on that doc), or the title with the em dash is the cause. To isolate the problem, let me first test with a simpler title.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"mutation { documentUpdate(id: \"9cbbb414-571b-4713-9831-798fdf8eaf61\", input: {title: \"Referral pilot — launch notes\"}) { success } }"}' ; echo; curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"mutation { documentUpdate(id: \"9cbbb414-571b-4713-9831-798fdf8eaf61\", input: {title: \"Test rename\"}) { success } }"}'
Response: {"status": "success", "stdout": "{\"data\":null,\"errors\":[{\"message\":\"Cannot return null for non-nullable field DocumentPayload.success.\",\"locations\":[{\"line\":1,\"column\":122}],\"path\":[\"documentUpdate\",\"success\"]}]}\n{\"data\":null,\"errors\":[{\"message\":\"Cannot return null for non-nullable field DocumentPayload.success.\",\"locations\":[{\"line\":1,\"column\":104}],\"path\":[\"documentUpdate\",\"success\"]}]}"}

#### Step 14
Reasoning: documentUpdate consistently returns null — either it's silently failing, or the proxy is mocking it. Let me check whether the title has actually been changed by re-querying the document.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ document(id: \"9cbbb414-571b-4713-9831-798fdf8eaf61\") { id title } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"document\":{\"id\":\"9cbbb414-571b-4713-9831-798fdf8eaf61\",\"title\":\"Test rename\"}}}"}

#### Step 15
Reasoning: Interesting — the update itself is succeeding. The error was simply because the mutation's payload field `success`/`document` couldn't be selected on the response (the API seems to be returning null for these fields in this environment, a quirk of the mock/API). The title actually got changed to "Test rename". I need to set it back to the correct title "Referral pilot — launch notes" and verify.

The mutation works — only the payload return type has an issue in this API build, but the title did change. Let me set the correct title and verify:
Command: curl -s -o /dev/null https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"mutation { documentUpdate(id: \"9cbbb414-571b-4713-9831-798fdf8eaf61\", input: {title: \"Referral pilot — launch notes\"}) { success } }"}'; curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ document(id: \"9cbbb414-571b-4713-9831-798fdf8eaf61\") { id title content team { name key } url } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"document\":{\"id\":\"9cbbb414-571b-4713-9831-798fdf8eaf61\",\"title\":\"Referral pilot — launch notes\",\"content\":\"Draft notes on the referral program pilot rollout for Q4, including timeline and success metrics.\",\"team\":{\"name\":\"Growth\",\"key\":\"GRO\"},\"url\":\"https://linear.app/northwind/document/9cbbb414-571b-4713-9831-798fdf8eaf61\"}}}"}

#### Step 16
Reasoning: Done. The Growth team's "Draft notes" doc (the one about the referral program pilot rollout) has been renamed to "Referral pilot — launch notes". Note: the Growth team had two docs named "Draft notes" — one about Seattle office moving logistics, which I left as-is. Should briefly mention that point.

Done. Renamed in the Growth team (GRO):

- **"Draft notes" → "Referral pilot — launch notes"** — the one covering the Q4 referral program pilot rollout (timeline + success metrics)
- Link: https://linear.app/northwind/document/9cbbb414-571b-4713-9831-798fdf8eaf61

Heads up: Growth had a second doc also titled "Draft notes" (about Seattle office move logistics). I left that one untouched — let me know if that was the one you meant instead.
Command: 
Response: null

## Final answer
Done. Renamed in the Growth team (GRO):

- **"Draft notes" → "Referral pilot — launch notes"** — the one covering the Q4 referral program pilot rollout (timeline + success metrics)
- Link: https://linear.app/northwind/document/9cbbb414-571b-4713-9831-798fdf8eaf61

Heads up: Growth had a second doc also titled "Draft notes" (about Seattle office move logistics). I left that one untouched — let me know if that was the one you meant instead.

## State diff
- UPDATE documents `9cbbb414-571b-4713-9831-798fdf8eaf61`: {"title": ["Draft notes", "Referral pilot — launch notes"]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["9cbbb414-571b-4713-9831-798fdf8eaf61"]}. Provisional outcome: incomplete. Provisional exposed facts: [].

Give your verdict for this trial.