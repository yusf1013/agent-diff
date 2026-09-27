Checked ENG-7's relations in Linear — the blocking relation you described doesn't exist. What's actually there is the opposite:

- **ENG-7 (Upgrade auth library) → blocks → ENG-9 (Run database migration for the v2 schema)**

So ENG-7 is blocking the migration issue, not the other way around. Per your preflight rule, I didn't touch it. If you want, I can either delete this relation, or flip/add a relation so ENG-7 is blocked by ENG-9 — just say which.
