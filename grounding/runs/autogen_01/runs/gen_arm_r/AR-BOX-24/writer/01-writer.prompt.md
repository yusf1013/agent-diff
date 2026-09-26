Write scenario `AR-BOX-24` for the box domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:User.login", "kind": "A", "subkind": "identity", "entity": "User", "table": "box_users", "field": "login", "evidence": "mini user", "mutation": "DROP", "designated_substitutes": ["User.name"], "suggested_families": ["F8", "F1", "F0"]}
{"id": "A:Task.message", "kind": "A", "subkind": "text", "entity": "Task", "table": "box_tasks", "field": "message", "evidence": "task dict", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F1", "F2", "F0"]}
{"id": "A:Task.created_at", "kind": "A", "subkind": "time", "entity": "Task", "table": "box_tasks", "field": "created_at", "evidence": "task dict", "mutation": "DROP", "designated_substitutes": ["Task.due_at"], "suggested_families": ["F7", "F6", "F1", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.