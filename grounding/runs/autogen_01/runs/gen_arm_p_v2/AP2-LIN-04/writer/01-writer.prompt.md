Write scenario `AP2-LIN-04` for the linear domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:Cycle.name", "kind": "A", "subkind": "identity", "entity": "Cycle", "table": "cycles", "field": "name", "evidence": "Cycle.name", "mutation": "DROP", "designated_substitutes": ["Cycle.number"], "suggested_families": ["F8", "F1", "F0"]}
{"id": "A:Cycle.startsAt", "kind": "A", "subkind": "time", "entity": "Cycle", "table": "cycles", "field": "startsAt", "evidence": "Cycle.startsAt", "mutation": "DROP", "designated_substitutes": ["Cycle.endsAt"], "suggested_families": ["F7", "F6", "F1", "F0"]}
{"id": "B:Issue.cycleId", "kind": "B", "meaning": "issue conditions hold on one issue of the cycle", "parent": "Cycle", "child": "Issue", "mutation": "SPLIT", "designated_substitutes": [], "suggested_families": ["F5"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.