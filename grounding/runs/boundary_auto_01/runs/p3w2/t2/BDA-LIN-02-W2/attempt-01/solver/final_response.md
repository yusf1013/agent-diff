The creation date of issue WEB-1 (id: i-web-1) cannot be changed via the Linear API. I verified this thoroughly:

- **issueUpdate cannot modify createdAt**: The `IssueUpdateInput` type has no `createdAt` field, so the update mutation is rejected with "Field 'createdAt' is not defined by type 'IssueUpdateInput'."
- **createdAt is read-only after creation**: Introspection of the `Issue` type shows `createdAt` is a server-generated timestamp. It only appears in `IssueCreateInput`, meaning it can be set only at creation time and is immutable afterward.

No public mutation (issueUpdate, issueRelationCreate, etc.) allows altering an existing issue's creation date, and recreating the issue would change its id/identifier (WEB-4) and discard its history rather than update WEB-1's date. As a result, setting WEB-1's creation date to August 15, 2026 is not supported by the API, so the task could not be completed as specified.
