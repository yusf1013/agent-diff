# Linear source-to-interface map

The local GraphQL API schema and API extract are listed and hashed in [sources.json](sources.json). Native seed names are retained. Only declarations, not resolvers or database implementations, support this map.

| Native vocabulary | API definition |
|---|---|
| `teams.id`, `.name`, `.key` | `Team` fields and `teams` query. |
| `users.id`, `.name`, `.displayName` | `User` fields and `users` query. Supplied actor identity fixes authentication scope. |
| `issues.id`, `.identifier`, `.title`, `.description`, `.createdAt`, `.dueDate` | `Issue` fields; issues query/filter and issue update input. |
| `issues.teamId`, `.assigneeId`, `.stateId`, `.parentId` | Input reference IDs and the corresponding `Issue.team`, `assignee`, `state`, and `parent` object IDs. `parentId` is not populated in the initial seed but is declared in the API. |
| `issues.priority` | Documented numeric enum: 0 none, 1 urgent, 2 high, 3 normal, 4 low. Priority is not the separate Urgent label. |
| `workflow_states.id`, `.teamId`, `.name`, `.type` | `WorkflowState` and team relation; `workflowStates` query and state create/archive operations. |
| `issue_labels.id`, `.name`, `.teamId` | `IssueLabel` and team relation, issueLabels query, label create/update operations. |
| `issue_label_issue_association.issue_id`, `.issue_label_id` | Native association identity; API exposes issue labels and accepts label IDs. No invented association scalar ID. |
| `comments.id`, `.issueId`, `.userId`, `.body` | `Comment` fields and issue/user relations; comment query/create/update/delete. |
| `team_memberships.teamId`, `.userId` | Team membership relationships exposed through `Team.members` and membership definitions. Member counts are recomputed from the supplied relationships, including zero-member teams. |
| `issue_relations.id`, `.issueId`, `.relatedIssueId`, `.type` | `IssueRelation` and source/related issue relations, `Issue.relations`/`inverseRelations`, relation create/delete. Source → related issue is interpreted from the seed's directed blocks edges. |

Archive timestamps are automatic representations of removal, not computed replacement values; removal cards leave `Written attributes` empty. A card listing an existing subject plus relationships records its local contribution, not a complete task-solving procedure. For example, packet-rate computation uses related workflow-state names after selecting the donor's packet issues.
