The mechanical checks of scenario.json found these problems:
- Claim check: G4-CAL-04.r1: expected ['ev_br_close'] but query selects []
- Claim check: G4-CAL-04.r1: claim D:local_time not killed by witness ev_br_utc (original=False, mutant=False)
- Claim check: G4-CAL-04.r1: claim A:Event.start not killed by witness ev_br_sat (original=False, mutant=False)
- Claim check: G4-CAL-04.r1: claim A:Event.summary not killed by witness ev_br_sync (original=False, mutant=False)
- Claim check: G4-CAL-04.r1: claim A:Event.organizer_email not killed by witness ev_br_omar (original=False, mutant=False)

Fix scenario.json (edit it in place), then reply with a short summary of what you changed.