Write scenario `AP-LIN-06` for the linear domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:Attachment.title", "kind": "A", "subkind": "identity", "entity": "Attachment", "table": "attachments", "field": "title", "evidence": "Attachment.title", "mutation": "DROP", "designated_substitutes": ["Attachment.url"], "suggested_families": ["F8", "F1", "F0"]}
{"id": "A:Attachment.url", "kind": "A", "subkind": "identity", "entity": "Attachment", "table": "attachments", "field": "url", "evidence": "Attachment.url", "mutation": "DROP", "designated_substitutes": ["Attachment.title"], "suggested_families": ["F8", "F1", "F0"]}
{"id": "R:Attachment.issueId", "kind": "R", "roles": ["Attachment.issueId"], "meaning": "attachment's issue", "mutation": "SUB_OR_DROP", "designated_substitutes": ["URL mentioned in the issue description"], "suggested_families": ["F1", "F2", "F8", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.