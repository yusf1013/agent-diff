The mechanical checks of scenario.json found these problems:
- Claim check: G4-CAL-05.r1: expected ['apac@northwind.example'] but query selects ['cle_apac@northwind.example']
- Claim check: G4-CAL-05.r1: claim A:CalendarListEntry.access_role not killed by witness apac-notes@northwind.example (original=False, mutant=False)
- Claim check: G4-CAL-05.r1: claim A:CalendarListEntry.summary_override not killed by witness apac-team@northwind.example (original=False, mutant=False)
- Claim check: G4-CAL-05.r1: claim A:CalendarListEntry.summary_override not killed by witness apac-team-old@northwind.example (original=False, mutant=False)
- Claim check: G4-CAL-05.r1: claim A:CalendarListEntry.hidden not killed by witness apac-team-2017@northwind.example (original=False, mutant=False)

Fix scenario.json (edit it in place), then reply with a short summary of what you changed.