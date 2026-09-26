The mechanical checks of scenario.json found these problems:
- Claim check: AP2-SLK-05.r1: expected ['C_ATLAS'] but query selects ['C_ATLAS', 'C_OWNER', 'C_PLAIN']
- Claim check: AP2-SLK-05.r1: claim A:WorkspaceMembership.role not killed by witness C_OWNER (original=True, mutant=True)
- Claim check: AP2-SLK-05.r1: claim A:WorkspaceMembership.role not killed by witness C_PLAIN (original=True, mutant=True)

Fix scenario.json (edit it in place), then reply with a short summary of what you changed.