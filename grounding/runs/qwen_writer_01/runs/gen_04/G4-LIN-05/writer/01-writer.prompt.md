Write scenario `G4-LIN-05` for the linear domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:Cycle.endsAt", "kind": "A", "subkind": "time", "entity": "Cycle", "table": "cycles", "field": "endsAt", "evidence": "Cycle.endsAt", "mutation": "DROP", "designated_substitutes": ["Cycle.startsAt"], "suggested_families": ["F7", "F6", "F1", "F0"]}
{"id": "R:Cycle.teamId", "kind": "R", "roles": ["Cycle.teamId"], "meaning": "cycle's team", "mutation": "SUB_OR_DROP", "designated_substitutes": ["same-numbered cycle of another team"], "suggested_families": ["F1", "F2", "F8", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.