Write scenario `DV-SLK-01` for the slack domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:User.timezone", "kind": "A", "subkind": "state", "entity": "User", "table": "users", "field": "timezone", "evidence": "`tz`; null rendered as a default zone", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F1", "F0"]}
{"id": "A:User.title", "kind": "A", "subkind": "text", "entity": "User", "table": "users", "field": "title", "evidence": "profile.title", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F1", "F2", "F0"]}
{"id": "A:User.is_active", "kind": "A", "subkind": "state", "entity": "User", "table": "users", "field": "is_active", "evidence": "`deleted` = not is_active", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F1", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.