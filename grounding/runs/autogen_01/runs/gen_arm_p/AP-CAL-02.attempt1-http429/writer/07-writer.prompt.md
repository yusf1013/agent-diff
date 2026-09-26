The mechanical checks of scenario.json found these problems:
- Claim check: AP-CAL-02.r1: expected ['user:maya.chen@northwind.example'] but query selects [{'calendar_id': 'team-roadmap@northwind.example', 'id': 'user:maya.chen@northwind.example'}]
- Claim check: AP-CAL-02.r1: claim R:CalendarListEntry.calendar_id not killed by witness user:maya.chen@northwind.example (original=False, mutant=False)
- Claim check: AP-CAL-02.r1: witness user:maya.chen@northwind.example reused for B:AclRule.calendar_id
- Claim check: AP-CAL-02.r1: claim B:AclRule.calendar_id not killed by witness user:maya.chen@northwind.example (original=False, mutant=False)

Fix scenario.json (edit it in place), then reply with a short summary of what you changed.