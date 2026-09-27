Write scenario `AP2-LIN-01` for the linear domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:Issue.completedAt", "kind": "A", "subkind": "time", "entity": "Issue", "table": "issues", "field": "completedAt", "evidence": "Issue.completedAt", "mutation": "DROP", "designated_substitutes": ["Issue.createdAt", "Issue.dueDate", "Issue.updatedAt"], "suggested_families": ["F7", "F6", "F1", "F0"]}
{"id": "A:Issue.description", "kind": "A", "subkind": "text", "entity": "Issue", "table": "issues", "field": "description", "evidence": "Issue.description", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F1", "F2", "F0"]}
{"id": "R:Issue.stateId", "kind": "R", "roles": ["Issue.stateId"], "meaning": "issue workflow state", "mutation": "SUB_OR_DROP", "designated_substitutes": ["same-named state of another team"], "suggested_families": ["F1", "F2", "F8", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.