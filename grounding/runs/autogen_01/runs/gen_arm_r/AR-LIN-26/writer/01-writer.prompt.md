Write scenario `AR-LIN-26` for the linear domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "R:issue_subscriber_user_association", "kind": "R", "roles": ["issue_subscriber_user_association"], "meaning": "issue subscriber", "mutation": "SUB_OR_DROP", "designated_substitutes": ["Issue.assigneeId", "Issue.creatorId"], "suggested_families": ["F1", "F2", "F8", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.