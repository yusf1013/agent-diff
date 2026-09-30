Everything's in place. Summary:

**Created**
- **BE-3** — "Q1 Infrastructure Overhaul" (epic, Backend team) → assigned to **Olga Petrova**, priority **High**
- **BE-4** — "Upgrade Redis cluster to v7" → parent set to BE-3, assigned to **Jamal Abdullah**

**Dependencies**
- BE-4 is **blocked by BE-1** "Complete PostgreSQL database migration to Aurora" (relation created as blocks: BE-1 → BE-4). This Linear instance only supports `blocks`/`related`/`duplicate`/`similar` relation types, so "blocked by" is expressed as the migration blocking the Redis upgrade — same effect.

**Comment**
- The standup note was added to BE-4, then deleted as you corrected. Verified: BE-4 has no comments. (Note: I did **not** re-add it to the migration ticket — you only asked to delete it. Say the word if it should land on BE-1.)

⚠️ One thing to flag: there are **two** migration tickets in the Backend team — **BE-1** and **BE-2**, identical titles, descriptions, and both In Progress. I wired the dependency to **BE-1**. If BE-2 is the one that actually matters (or if one should be archived), let me know and I'll switch the dependency or clean up the dupe.
