Write scenario `G4-BOX-05` for the box domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:User.name", "kind": "A", "subkind": "identity", "entity": "User", "table": "box_users", "field": "name", "evidence": "mini user", "mutation": "DROP", "designated_substitutes": ["User.login"], "suggested_families": ["F8", "F1", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.