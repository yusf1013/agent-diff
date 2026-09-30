Write scenario `G4-SLK-05` for the slack domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:Conversation.is_dm", "kind": "A", "subkind": "state", "entity": "Conversation", "table": "channels", "field": "is_dm", "evidence": "is_im", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F1", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.