The mechanical checks of scenario.json found these problems:
- Claim check: AP-CAL-02.r1: claim R:CalendarListEntry.calendar_id not killed by witness user:maya.chen@northwind.example (original=True, mutant=True)
- Claim check: AP-CAL-02.r1: witness user:maya.chen@northwind.example reused for B:AclRule.calendar_id
- Claim check: AP-CAL-02.r1: claim B:AclRule.calendar_id not killed by witness user:maya.chen@northwind.example (original=True, mutant=True)

Fix scenario.json (edit it in place), then reply with a short summary of what you changed.