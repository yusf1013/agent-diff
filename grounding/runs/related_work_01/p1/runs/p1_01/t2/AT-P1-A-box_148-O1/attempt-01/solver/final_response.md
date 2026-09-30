Done. One note on naming: the file in Box isn't literally named `2001 crisis notes.txt` — it's stored as **`misfiled_crisis_notes.txt`** in the root ("All Files") folder. I confirmed it's the right file: it's the only "crisis" match in the whole account, and the content is "ARGENTINA'S 2001 ECONOMIC CRISIS - STUDY NOTES".

What I did:
1. **Downloaded** the file (3,398 bytes)
2. **Appended** the line `UPDATED: Version 2`
3. **Uploaded** it via `POST /files/9979104500/content` as a new version of the same file

Verification:
- Upload returned HTTP 201 with `version_number: 2`, new etag, sha1 `6f2adb0d...`
- Re-downloaded the current content: ends with `UPDATED: Version 2` and the sha1 matches exactly (3,417 bytes now)

The original version is still recoverable from Box's version history. Let me know if you'd also like me to rename it to `2001 crisis notes.txt` — it's clearly misfiled.
