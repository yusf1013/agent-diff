The mechanical checks of scenario.json found these problems:
- Claim check: G4-CAL-05.r1: expected ['team-travel@northwind.example'] but query selects ['cle_team-travel@northwind.example']
- Claim check: G4-CAL-05.r1: claim A:CalendarListEntry.summary_override not killed by witness team-travel-board@northwind.example (original=False, mutant=False)
- Claim check: G4-CAL-05.r1: claim A:CalendarListEntry.access_role not killed by witness team-travel-ext@northwind.example (original=False, mutant=False)
- Claim check: G4-CAL-05.r1: claim A:CalendarListEntry.hidden not killed by witness team-travel-vis@northwind.example (original=False, mutant=False)

Fix scenario.json (edit it in place), then reply with a short summary of what you changed.