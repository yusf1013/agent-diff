Write scenario `DV-LIN-01` for the linear domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:ProjectMilestone.status", "kind": "A", "subkind": "state", "entity": "ProjectMilestone", "table": "project_milestones", "field": "status", "evidence": "ProjectMilestone.status", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F1", "F0"]}
{"id": "A:ProjectMilestone.targetDate", "kind": "A", "subkind": "time", "entity": "ProjectMilestone", "table": "project_milestones", "field": "targetDate", "evidence": "ProjectMilestone.targetDate", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F6", "F1", "F0"]}
{"id": "R:Issue.projectMilestoneId", "kind": "R", "roles": ["Issue.projectMilestoneId"], "meaning": "issue milestone", "mutation": "SUB_OR_DROP", "designated_substitutes": ["Issue.projectId without the milestone"], "suggested_families": ["F1", "F2", "F8", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.