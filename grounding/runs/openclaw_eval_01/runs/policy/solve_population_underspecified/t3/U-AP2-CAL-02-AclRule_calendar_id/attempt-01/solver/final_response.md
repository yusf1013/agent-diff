Your calendar list has **two** calendars named "Design Team," and they're identical in every way I can check — same owner (you), same timezone, same color, no description, no readable events. From the API side I can't tell them apart except by ID:

1. `c_1b1ced0bd34a6944fa9b3ff3bb@group.calendar.google.com`
2. `c_bc9ab8dbc86a11c78e84d54d55@group.calendar.google.com`

Which one should I hide — or would you like me to hide both? (Hiding is reversible, so if you're unsure I can hide one and you can check the calendar list in the UI.)

⚠️ 🛠️ Exec failed: `run for id → run do echo → fetch https://www.googleapis.com/calendar/v3/$id/acl -> run jq → run done`
