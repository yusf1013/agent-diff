Write scenario `G4-LIN-08` for the linear domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:Issue.dueDate", "kind": "A", "subkind": "time", "entity": "Issue", "table": "issues", "field": "dueDate", "evidence": "Issue.dueDate", "mutation": "DROP", "designated_substitutes": ["Cycle.endsAt", "ProjectMilestone.targetDate", "Issue.completedAt", "Issue.createdAt", "Issue.updatedAt"], "suggested_families": ["F7", "F6", "F1", "F0"]}
{"id": "A:Issue.estimate", "kind": "A", "subkind": "quantity", "entity": "Issue", "table": "issues", "field": "estimate", "evidence": "Issue.estimate", "mutation": "DROP", "designated_substitutes": ["Issue.priority"], "suggested_families": ["F7", "F0"]}
{"id": "A:Issue.identifier", "kind": "A", "subkind": "identity", "entity": "Issue", "table": "issues", "field": "identifier", "evidence": "Issue.identifier (team key + number)", "mutation": "DROP", "designated_substitutes": ["Issue.title"], "suggested_families": ["F8", "F1", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.