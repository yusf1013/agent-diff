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
Reasoning: The user wants to rename a document in Linear's Growth team from "Draft notes" to "Referral pilot — launch notes". I should read the SKILL.md for linear to figure out how to do this.
Command: read {"path": "~/.openclaw-state/f7d851e556904b55/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: The skill doesn't document an API for documents. Linear has a GraphQL API for documents. Let me try querying it. The base URL is https://api.linear.app/graphql. I can find the "Draft notes" document in the Growth team, and rename it to "Referral pilot — launch notes".

Linear's document API: there's a `documents` query and a `documentUpdate` mutation. Let me try exploring. First, find the team and document.

I'll write a small script. First, search for documents with the title "Draft notes".
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ teams { nodes { id name key url } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'url' on type 'Team'.\",\"locations\":[{\"line\":1,\"column\":31}]}]}"}

#### Step 3
Reasoning: Let's query the teams without the url field.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ teams { nodes { id name key } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"teams\":{\"nodes\":[{\"id\":\"11523cbc-2c51-4444-aa2c-8178e6c7a7f2\",\"name\":\"Platform\",\"key\":\"PLA\"},{\"id\":\"eff6e957-4cfa-42a0-93c4-571d26e09b5a\",\"name\":\"Growth\",\"key\":\"GRO\"}]}}}"}

#### Step 4
Reasoning: Found the growth team: id eff6e957-4cfa-42a0-93c4-571d26e09b5a. Next I need to find the document "Draft Notes". Linear documents are accessible via the `documents` query (the Linear API has a Documents API, and the `documents(filter:)` query, which supports teamId in the filter). Let me check. The Linear API has:

```
{
  documents(filter: { team: { id: { eq: "..." } } }) {
    nodes { id title url createdAt updatedAt }
  }
}
```

And then `documentUpdate(id: ...) { ... }`? Actually, does Linear have a `documentUpdate` mutation? There's `issueCreate`, and for documents there's `documentUpdate` (added in 2024). Let me first try querying the documents.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ documents(filter: { team: { id: { eq: \"eff6e957-4cfa-42a0-93c4-571d26e09b5a\" } } }) { nodes { id title url createdAt } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Field 'team' is not defined by type 'DocumentFilter'.\",\"locations\":[{\"line\":1,\"column\":23}]}]}"}

#### Step 5
Reasoning: Let's check the DocumentFilter type. I'll try using introspection.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ __type(name: \"DocumentFilter\") { inputFields { name type { name kind ofType { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"inputFields\":[{\"name\":\"and\",\"type\":{\"name\":null,\"kind\":\"LIST\",\"ofType\":{\"name\":null}}},{\"name\":\"createdAt\",\"type\":{\"name\":\"DateComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"creator\",\"type\":{\"name\":\"UserFilter\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"id\",\"type\":{\"name\":\"IDComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"initiative\",\"type\":{\"name\":\"InitiativeFilter\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"or\",\"type\":{\"name\":null,\"kind\":\"LIST\",\"ofType\":{\"name\":null}}},{\"name\":\"project\",\"type\":{\"name\":\"ProjectFilter\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"slugId\",\"type\":{\"name\":\"StringComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"title\",\"type\":{\"name\":\"StringComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"updatedAt\",\"type\":{\"name\":\"DateComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}}]}}}"}

#### Step 6
Reasoning: The document filter doesn't have a team field. Let me try searching by the title "Draft notes".
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ documents(filter: { title: { eq: \"Draft notes\" } }) { nodes { id title slugId url createdAt } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"documents\":{\"nodes\":[{\"id\":\"49be3bd4-9cf1-4da0-bdff-6a3232ae6630\",\"title\":\"Draft notes\",\"slugId\":\"49be3bd4-9cf1-4da0-bdff-6a3232ae6630\",\"url\":\"https://linear.app/northwind/document/49be3bd4-9cf1-4da0-bdff-6a3232ae6630\",\"createdAt\":\"2026-06-01T09:00:00\"},{\"id\":\"7dcfb1dd-35ff-4892-b7c0-b9954ad829fb\",\"title\":\"Draft notes\",\"slugId\":\"7dcfb1dd-35ff-4892-b7c0-b9954ad829fb\",\"url\":\"https://linear.app/northwind/document/7dcfb1dd-35ff-4892-b7c0-b9954ad829fb\",\"createdAt\":\"2026-06-01T09:00:00\"},{\"id\":\"9cbbb414-571b-4713-9831-798fdf8eaf61\",\"title\":\"Draft notes\",\"slugId\":\"9cbbb414-571b-4713-9831-798fdf8eaf61\",\"url\":\"https://linear.app/northwind/document/9cbbb414-571b-4713-9831-798fdf8eaf61\",\"createdAt\":\"2026-06-01T09:00:00\"},{\"id\":\"b5afce1a-8bf9-4d44-bf6b-6cd178d340c3\",\"title\":\"Draft notes\",\"slugId\":\"b5afce1a-8bf9-4d44-bf6b-6cd178d340c3\",\"url\":\"https://linear.app/northwind/document/b5afce1a-8bf9-4d44-bf6b-6cd178d340c3\",\"createdAt\":\"2026-06-01T09:00:00\"}]}}}"}

#### Step 7
Reasoning: There are 4 documents with the title "Draft notes". I need to identify which one belongs to the Growth team. The DocumentFilter doesn't have a team filter. Let me check the fields on the Document type to find a way to identify the team.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ __type(name: \"Document\") { fields { name type { name kind ofType { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"fields\":[{\"name\":\"archivedAt\",\"type\":{\"name\":\"DateTime\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"color\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"comments\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"CommentConnection\"}}},{\"name\":\"content\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"contentState\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"createdAt\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"DateTime\"}}},{\"name\":\"creator\",\"type\":{\"name\":\"User\",\"kind\":\"OBJECT\",\"ofType\":null}},{\"name\":\"documentContentId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"hiddenAt\",\"type\":{\"name\":\"DateTime\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"icon\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"id\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"ID\"}}},{\"name\":\"initiative\",\"type\":{\"name\":\"Initiative\",\"kind\":\"OBJECT\",\"ofType\":null}},{\"name\":\"lastAppliedTemplate\",\"type\":{\"name\":\"Template\",\"kind\":\"OBJECT\",\"ofType\":null}},{\"name\":\"project\",\"type\":{\"name\":\"Project\",\"kind\":\"OBJECT\",\"ofType\":null}},{\"name\":\"slugId\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"String\"}}},{\"name\":\"sortOrder\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"Float\"}}},{\"name\":\"team\",\"type\":{\"name\":\"Team\",\"kind\":\"OBJECT\",\"ofType\":null}},{\"name\":\"title\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"String\"}}},{\"name\":\"trashed\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"updatedAt\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"DateTime\"}}},{\"name\":\"updatedBy\",\"type\":{\"name\":\"User\",\"kind\":\"OBJECT\",\"ofType\":null}},{\"name\":\"url\",\"type\":{\"name\":null,\"kind\":\"NON_NULL\",\"ofType\":{\"name\":\"String\"}}}]}}}"}

#### Step 8
Reasoning: I need to figure out which of the 4 "Draft notes" documents belongs to the Growth team. The Document type has a `team` field.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ documents(filter: { title: { eq: \"Draft notes\" } }) { nodes { id title team { id name key } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"documents\":{\"nodes\":[{\"id\":\"49be3bd4-9cf1-4da0-bdff-6a3232ae6630\",\"title\":\"Draft notes\",\"team\":null},{\"id\":\"7dcfb1dd-35ff-4892-b7c0-b9954ad829fb\",\"title\":\"Draft notes\",\"team\":{\"id\":\"eff6e957-4cfa-42a0-93c4-571d26e09b5a\",\"name\":\"Growth\",\"key\":\"GRO\"}},{\"id\":\"9cbbb414-571b-4713-9831-798fdf8eaf61\",\"title\":\"Draft notes\",\"team\":{\"id\":\"eff6e957-4cfa-42a0-93c4-571d26e09b5a\",\"name\":\"Growth\",\"key\":\"GRO\"}},{\"id\":\"b5afce1a-8bf9-4d44-bf6b-6cd178d340c3\",\"title\":\"Draft notes\",\"team\":{\"id\":\"11523cbc-2c51-4444-aa2c-8178e6c7a7f2\",\"name\":\"Platform\",\"key\":\"PLA\"}}]}}}"}

#### Step 9
Reasoning: Two documents in the growth team are titled "Draft notes." Need to disambiguate. The user said "the document titled 'Draft notes' in the growth team," in the singular. Two matches. Let's get more details: createdAt, updatedBy, content preview, comments, projects. All four have the same createdAt (2026-06-01T09:00:00). Check updatedAt and content preview.

Two "Draft notes" documents exist under Growth — checking which one is the right target:
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ documents(filter: { title: { eq: \"Draft notes\" } }) { nodes { id title updatedAt updatedBy { name } content project { name key } comments { nodes { body createdAt } } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'key' on type 'Project'.\",\"locations\":[{\"line\":1,\"column\":126}]}]}"}

#### Step 10
Reasoning: I need to investigate this further. Let me check the details. Let's remove the key from the project and try again.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ documents(filter: { title: { eq: \"Draft notes\" } }) { nodes { id title updatedAt updatedBy { name } content project { name identifier } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'identifier' on type 'Project'.\",\"locations\":[{\"line\":1,\"column\":126}]}]}"}

#### Step 11
Reasoning: Let's get the content and updatedAt of both documents on the growth.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ a: document(id: \"7dcfb1dd-35ff-4892-b7c0-b9954ad829fb\") { id title updatedAt updatedBy { name } content } b: document(id: \"9cbbb414-571b-4713-9831-798fdf8eaf61\") { id title updatedAt updatedBy { name } content } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"a\":{\"id\":\"7dcfb1dd-35ff-4892-b7c0-b9954ad829fb\",\"title\":\"Draft notes\",\"updatedAt\":\"2026-06-01T09:00:00\",\"updatedBy\":{\"name\":\"Jordan Lee\"},\"content\":\"Draft notes on the office move logistics for the Seattle team.\"},\"b\":{\"id\":\"9cbbb414-571b-4713-9831-798fdf8eaf61\",\"title\":\"Draft notes\",\"updatedAt\":\"2026-06-01T09:00:00\",\"updatedBy\":{\"name\":\"Jordan Lee\"},\"content\":\"Draft notes on the referral program pilot rollout for Q4, including timeline and success metrics.\"}}}"}

#### Step 12
Reasoning: Found it. The one about the "referral program pilot rollout" (id 9cbbb414-...) matches the target name "Referral pilot — launch notes". The other one is about office relocation logistics, so it's a distractor.

Next, I'll update the title.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"mutation { documentUpdate(input: { id: \"9cbbb414-571b-4713-9831-798fdf8eaf61\", title: \"Referral pilot — launch notes\" }) { success document { id title url } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Field 'id' is not defined by type 'DocumentUpdateInput'.\",\"locations\":[{\"line\":1,\"column\":36}]},{\"message\":\"Field 'documentUpdate' argument 'id' of type 'String!' is required, but it was not provided.\",\"locations\":[{\"line\":1,\"column\":12}]}]}"}

#### Step 13
Reasoning: The mutation signature is `documentUpdate(id: String!, input: DocumentUpdateInput)`. Let me try checking DocumentUpdateInput.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ __type(name: \"DocumentUpdateInput\") { inputFields { name type { name kind ofType { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"__type\":{\"inputFields\":[{\"name\":\"color\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"content\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"hiddenAt\",\"type\":{\"name\":\"DateTime\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"icon\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"initiativeId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"lastAppliedTemplateId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"projectId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"resourceFolderId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"sortOrder\",\"type\":{\"name\":\"Float\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"subscriberIds\",\"type\":{\"name\":null,\"kind\":\"LIST\",\"ofType\":{\"name\":null}}},{\"name\":\"teamId\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"title\",\"type\":{\"name\":\"String\",\"kind\":\"SCALAR\",\"ofType\":null}},{\"name\":\"trashed\",\"type\":{\"name\":\"Boolean\",\"kind\":\"SCALAR\",\"ofType\":null}}]}}}"}

#### Step 14
Reasoning: The id is an argument, not an input field. Also, "Draft notes" exists in 2 items under Growth — one is about office relocation logistics, and the other is about the referral program pilot. The user asked to rename the "Draft notes" in the Growth team to "Referral pilot — launch notes". There's ambiguity, but the referral pilot one (9cbbb414) clearly matches the new title. That's the one to rename.

The Growth team has two docs named "Draft notes" — one about office move logistics, one about the referral program pilot. Renaming the referral pilot one:
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"mutation { documentUpdate(id: \"9cbbb414-571b-4713-9831-798fdf8eaf61\", input: { title: \"Referral pilot — launch notes\" }) { success document { id title url } } }"}'
Response: {"status": "success", "stdout": "{\"data\":null,\"errors\":[{\"message\":\"Cannot return null for non-nullable field DocumentPayload.success.\",\"locations\":[{\"line\":1,\"column\":124}],\"path\":[\"documentUpdate\",\"success\"]}]}"}

#### Step 15
Reasoning: The mutation returned null — something failed. Maybe documentUpdate requires the `id` argument to be the document's slugId or uuid, or maybe the mutation silently failed. Let me try using `slugId` as the id argument, or try querying again to check if the title has changed.
Command: curl -s https://api.linear.app/graphql -H 'Content-Type: application/json' -d '{"query":"{ document(id: \"9cbbb414-571b-4713-9831-798fdf8eaf61\") { id title url } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"document\":{\"id\":\"9cbbb414-571b-4713-9831-798fdf8eaf61\",\"title\":\"Referral pilot — launch notes\",\"url\":\"https://linear.app/northwind/document/9cbbb414-571b-4713-9831-798fdf8eaf61\"}}}"}

#### Step 16
Reasoning: The update succeeded (the null success error seems to be a quirk of the schema, but the document has been renamed). Confirmed: the title is now "Referral pilot — launch notes". Done.

Done. Renamed the Growth team's "Draft notes" → **"Referral pilot — launch notes"** ([link](https://linear.app/northwind/document/9cbbb414-571b-4713-9831-798fdf8eaf61)).

Note: Growth had two docs titled "Draft notes" — the other one (about Seattle office move logistics) is untouched.
Command: 
Response: null

## Final answer
Done. Renamed the Growth team's "Draft notes" → **"Referral pilot — launch notes"** ([link](https://linear.app/northwind/document/9cbbb414-571b-4713-9831-798fdf8eaf61)).

Note: Growth had two docs titled "Draft notes" — the other one (about Seattle office move logistics) is untouched.

## State diff
- UPDATE documents `9cbbb414-571b-4713-9831-798fdf8eaf61`: {"title": ["Draft notes", "Referral pilot — launch notes"]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["9cbbb414-571b-4713-9831-798fdf8eaf61"]}. Provisional outcome: incomplete. Provisional exposed facts: [].

Give your verdict for this trial.