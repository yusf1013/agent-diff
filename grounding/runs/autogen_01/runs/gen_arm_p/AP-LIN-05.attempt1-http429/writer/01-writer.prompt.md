Write scenario `AP-LIN-05` for the linear domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:Comment.createdAt", "kind": "A", "subkind": "time", "entity": "Comment", "table": "comments", "field": "createdAt", "evidence": "Comment.createdAt", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F6", "F1", "F0"]}
{"id": "A:Comment.resolvedAt", "kind": "A", "subkind": "state", "entity": "Comment", "table": "comments", "field": "resolvedAt", "evidence": "resolved thread (resolvedAt present)", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F1", "F0"]}
{"id": "B:Comment.issueId", "kind": "B", "meaning": "author and body conditions hold on one comment", "parent": "Issue", "child": "Comment", "mutation": "SPLIT", "designated_substitutes": [], "suggested_families": ["F5"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.