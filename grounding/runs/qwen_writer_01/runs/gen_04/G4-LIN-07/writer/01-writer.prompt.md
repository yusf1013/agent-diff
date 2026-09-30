Write scenario `G4-LIN-07` for the linear domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "R:Issue.assigneeId", "kind": "R", "roles": ["Issue.assigneeId"], "meaning": "issue assignee", "mutation": "SUB_OR_DROP", "designated_substitutes": ["Issue.creatorId", "issue_subscriber_user_association", "Comment.userId (commenter)"], "suggested_families": ["F1", "F2", "F8", "F0"]}
{"id": "R:Issue.projectId", "kind": "R", "roles": ["Issue.projectId"], "meaning": "issue project", "mutation": "SUB_OR_DROP", "designated_substitutes": ["project of the parent issue", "project named in the title"], "suggested_families": ["F1", "F2", "F8", "F0"]}
{"id": "R:Issue.cycleId", "kind": "R", "roles": ["Issue.cycleId"], "meaning": "issue cycle", "mutation": "SUB_OR_DROP", "designated_substitutes": ["cycle of another team with the same number", "D:current_cycle by date only"], "suggested_families": ["F1", "F2", "F8", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.