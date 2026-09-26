Write scenario `AR-LIN-25` for the linear domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "H:IssueLabel.parentId", "kind": "H", "roles": ["IssueLabel.parentId"], "meaning": "label group vs member labels", "mutation": "LEVEL", "designated_substitutes": ["group label taken as applied label, or member label for the group"], "suggested_families": ["F4", "F2"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.