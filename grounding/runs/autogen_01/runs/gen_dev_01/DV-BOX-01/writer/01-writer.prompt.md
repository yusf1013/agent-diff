Write scenario `DV-BOX-01` for the box domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:Hub.title", "kind": "A", "subkind": "identity", "entity": "Hub", "table": "box_hubs", "field": "title", "evidence": "hub dict", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F8", "F1", "F0"]}
{"id": "A:Hub.description", "kind": "A", "subkind": "text", "entity": "Hub", "table": "box_hubs", "field": "description", "evidence": "hub dict", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F1", "F2", "F0"]}
{"id": "A:Hub.created_at", "kind": "A", "subkind": "time", "entity": "Hub", "table": "box_hubs", "field": "created_at", "evidence": "hub dict", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F6", "F1", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.