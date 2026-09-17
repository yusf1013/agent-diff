**Review Roster – Profile-Shown Workspaces & Audit-Log Match**

I checked each user's profile (`profile.team`) and cross-referenced it against messages in the audit-log channels (C1, C2, C3) that have a reaction from Alex Rivera (U200, team T1).

**Findings per channel:**
- **C1**: Message by U100 ("Completed quarterly access audit for Prod workspace.") — reacted 👍 by **U200 (Alex)** → team **T1** ✅
- **C2**: Message by U101 had a ✅ reaction, but from U201 (not Alex) → no match
- **C3**: Message by U102 had an 👀 reaction, but from U203 (not Alex) → no match

**Full roster with profile-shown workspace:**
| User | Name | Profile Workspace | Alex-reacted audit message found? |
|------|------|--------------------|-------------------------------------|
| U100 | Grace Kim | T1 | ✅ Yes (C1) |
| U101 | Sam Okafor | T2 | ❌ No |
| U102 | Priya Nair | T3 | ❌ No |

**Final filtered result (only workspaces with a qualifying Alex-reacted audit message):**
- **U100 — Grace Kim — Workspace: T1**

U101 (T2) and U102 (T3) were excluded since no audit-log channel message tied to their workspace had a reaction from Alex.
