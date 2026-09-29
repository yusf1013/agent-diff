I could not make Leo Park the creator of the "Checkout spec" document because the Linear GraphQL API does not support changing a document's creator.

What I verified:
- The "Checkout spec" document (`doc-1`) currently has **Maya Chen** (`u-maya`) as creator (and last updater). I'm authenticated as **Jordan Lee** (`u-actor`), not Leo Park.
- `DocumentUpdateInput` only allows these fields: `color`, `content`, `hiddenAt`, `icon`, `initiativeId`, `lastAppliedTemplateId`, `projectId`, `resourceFolderId`, `sortOrder`, `subscriberIds`, `teamId`, `title`, `trashed` — there is **no creator/creatorId field**.
- `DocumentCreateInput` also has no creator field.
- A full-schema scan shows `creator` is only ever a read-only query/filter field, never a settable input.
- I attempted `documentUpdate(id: "doc-1", input: { creatorId: "u-leo" })` and the API explicitly rejected it: *"Field 'creatorId' is not defined by type 'DocumentUpdateInput'."*

In Linear, a document's `creator` is fixed to the user who created it and is immutable afterward — there is no mutation to reassign it. Achieving this would require either direct database access or Leo Park creating the document himself, neither of which is available through the current API/authentication. The operation the API would need to perform simply does not exist, so it cannot be completed here.
