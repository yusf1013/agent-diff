Write scenario `AR-LIN-23` for the linear domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "R:Comment.resolvingUserId", "kind": "R", "roles": ["Comment.resolvingUserId"], "meaning": "user who resolved the thread", "mutation": "SUB_OR_DROP", "designated_substitutes": ["Comment.userId"], "suggested_families": ["F1", "F2", "F8", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.