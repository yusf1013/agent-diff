Write scenario `G4-BOX-08` for the box domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "R:Hub.created_by_id", "kind": "R", "roles": ["Hub.created_by_id"], "meaning": "hub creator", "mutation": "SUB_OR_DROP", "designated_substitutes": ["Hub.updated_by_id"], "suggested_families": ["F1", "F2", "F8", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.