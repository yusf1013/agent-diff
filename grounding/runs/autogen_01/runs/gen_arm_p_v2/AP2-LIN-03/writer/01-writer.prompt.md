Write scenario `AP2-LIN-03` for the linear domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:Team.description", "kind": "A", "subkind": "text", "entity": "Team", "table": "teams", "field": "description", "evidence": "Team.description", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F1", "F2", "F0"]}
{"id": "A:Team.key", "kind": "A", "subkind": "identity", "entity": "Team", "table": "teams", "field": "key", "evidence": "Team.key", "mutation": "DROP", "designated_substitutes": ["Team.name"], "suggested_families": ["F8", "F1", "F0"]}
{"id": "A:Team.private", "kind": "A", "subkind": "state", "entity": "Team", "table": "teams", "field": "private", "evidence": "Team.private", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F1", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.