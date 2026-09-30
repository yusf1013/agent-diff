Write scenario `G4-SLK-01` for the slack domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:User.email", "kind": "A", "subkind": "identity", "entity": "User", "table": "users", "field": "email", "evidence": "profile.email", "mutation": "DROP", "designated_substitutes": ["User.username", "User.real_name", "User.display_name"], "suggested_families": ["F8", "F1", "F0"]}
{"id": "A:User.is_bot", "kind": "A", "subkind": "state", "entity": "User", "table": "users", "field": "is_bot", "evidence": "`is_bot`", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F1", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.