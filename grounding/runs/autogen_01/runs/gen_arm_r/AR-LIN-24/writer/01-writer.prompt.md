Write scenario `AR-LIN-24` for the linear domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:Cycle.number", "kind": "A", "subkind": "identity", "entity": "Cycle", "table": "cycles", "field": "number", "evidence": "Cycle.number", "mutation": "DROP", "designated_substitutes": ["Cycle.name"], "suggested_families": ["F8", "F1", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.