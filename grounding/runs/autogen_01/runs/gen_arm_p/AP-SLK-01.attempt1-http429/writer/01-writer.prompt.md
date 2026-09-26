Write scenario `AP-SLK-01` for the slack domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:User.username", "kind": "A", "subkind": "identity", "entity": "User", "table": "users", "field": "username", "evidence": "users.info/list `name`", "mutation": "DROP", "designated_substitutes": ["User.email", "User.real_name", "User.display_name"], "suggested_families": ["F8", "F1", "F0"]}
{"id": "A:User.real_name", "kind": "A", "subkind": "identity", "entity": "User", "table": "users", "field": "real_name", "evidence": "real_name/profile.real_name", "mutation": "DROP", "designated_substitutes": ["User.username", "User.email", "User.display_name"], "suggested_families": ["F8", "F1", "F0"]}
{"id": "A:User.display_name", "kind": "A", "subkind": "identity", "entity": "User", "table": "users", "field": "display_name", "evidence": "profile.display_name", "mutation": "DROP", "designated_substitutes": ["User.username", "User.email", "User.real_name"], "suggested_families": ["F8", "F1", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.