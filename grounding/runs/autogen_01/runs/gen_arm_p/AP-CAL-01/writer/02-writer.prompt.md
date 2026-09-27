The mechanical checks of scenario.json found these problems:
- Claim check: AP-CAL-01.r1: expected ['cs-north@northwind.example'] but query selects ['cle_cs-north@northwind.example']
- Claim check: AP-CAL-01.r1: claim A:Calendar.summary not killed by witness cs-renewals@northwind.example (original=False, mutant=False)
- Claim check: AP-CAL-01.r1: claim A:Calendar.summary not killed by witness finance-ops@northwind.example (original=False, mutant=False)
- Claim check: AP-CAL-01.r1: claim A:CalendarListEntry.selected not killed by witness cs-south@northwind.example (original=False, mutant=False)
- Claim check: AP-CAL-01.r1: claim A:CalendarListEntry.selected not killed by witness cs-east@northwind.example (original=False, mutant=False)

Fix scenario.json (edit it in place), then reply with a short summary of what you changed.