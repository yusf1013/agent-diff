Write scenario `AR-LIN-21` for the linear domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:Issue.createdAt", "kind": "A", "subkind": "time", "entity": "Issue", "table": "issues", "field": "createdAt", "evidence": "Issue.createdAt", "mutation": "DROP", "designated_substitutes": ["Issue.completedAt", "Issue.dueDate", "Issue.updatedAt"], "suggested_families": ["F7", "F6", "F1", "F0"]}
{"id": "R:Issue.creatorId", "kind": "R", "roles": ["Issue.creatorId"], "meaning": "issue creator", "mutation": "SUB_OR_DROP", "designated_substitutes": ["Issue.assigneeId", "issue_subscriber_user_association"], "suggested_families": ["F1", "F2", "F8", "F0"]}
{"id": "R:Issue.teamId", "kind": "R", "roles": ["Issue.teamId"], "meaning": "issue team", "mutation": "SUB_OR_DROP", "designated_substitutes": ["team whose label is on the issue", "parent team (H:Team.parentId)"], "suggested_families": ["F1", "F2", "F8", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.