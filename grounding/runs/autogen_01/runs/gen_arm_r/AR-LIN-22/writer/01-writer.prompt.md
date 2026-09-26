Write scenario `AR-LIN-22` for the linear domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "R:Document.projectId", "kind": "R", "roles": ["Document.projectId"], "meaning": "document's project", "mutation": "SUB_OR_DROP", "designated_substitutes": ["Document.initiativeId", "Document.teamId"], "suggested_families": ["F1", "F2", "F8", "F0"]}
{"id": "R:Document.updatedById", "kind": "R", "roles": ["Document.updatedById"], "meaning": "document last editor", "mutation": "SUB_OR_DROP", "designated_substitutes": ["Document.creatorId"], "suggested_families": ["F1", "F2", "F8", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.