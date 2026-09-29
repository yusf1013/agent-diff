Done, with two caveats:

**✅ Tag added** — `legal-review` is now on **Beacon Vendor Agreement.pdf** in Vendor Contracts (tags: `renewal`, `legal-review`).

**⚠️ Version mismatch** — you said version 6, but the file (id 7102) is currently at **version 5**. I matched on everything else: the only locked vendor agreement in that folder, already tagged `renewal`. The other file there (Pier Vendor Agreement) is unlocked, v2, tagged `misc`. If "version 6" was a hard requirement, let me know and I'll back this out.

**⚠️ Lock side effect** — Box clears the lock when file attributes are updated via PUT. The tag update silently unlocked the file, so I re-applied the lock with its original settings (lock active, downloads allowed) right after. Confirmed restored.
