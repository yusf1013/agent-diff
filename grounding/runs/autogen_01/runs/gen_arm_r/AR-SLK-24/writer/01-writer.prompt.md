Write scenario `AR-SLK-24` for the slack domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "R:channel_members", "kind": "R", "roles": ["channel_members.user_id", "channel_members.channel_id"], "meaning": "conversation membership", "mutation": "SUB_OR_DROP", "designated_substitutes": ["posted in the channel (location of authored message)", "reacted in the channel"], "suggested_families": ["F1", "F2", "F8", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.