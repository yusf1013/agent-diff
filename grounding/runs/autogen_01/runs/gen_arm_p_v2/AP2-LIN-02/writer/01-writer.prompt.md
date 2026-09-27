Write scenario `AP2-LIN-02` for the linear domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:User.email", "kind": "A", "subkind": "identity", "entity": "User", "table": "users", "field": "email", "evidence": "User.email", "mutation": "DROP", "designated_substitutes": ["User.displayName", "User.name"], "suggested_families": ["F8", "F1", "F0"]}
{"id": "A:User.guest", "kind": "A", "subkind": "state", "entity": "User", "table": "users", "field": "guest", "evidence": "User.guest", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F1", "F0"]}
{"id": "A:User.name", "kind": "A", "subkind": "identity", "entity": "User", "table": "users", "field": "name", "evidence": "User.name", "mutation": "DROP", "designated_substitutes": ["User.displayName", "User.displayName", "User.email"], "suggested_families": ["F8", "F1", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.