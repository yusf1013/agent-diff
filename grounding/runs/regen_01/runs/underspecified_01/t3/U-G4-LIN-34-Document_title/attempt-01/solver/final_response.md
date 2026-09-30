Done. The document "3D Secure Fallback Plan" in the Payments team — the one whose content covers adding 3D Secure fallback for failed checkout payments (retry sequence + exemption flags) — is now renamed to **3D Secure Fallback Plan — Final**.

Notes on the disambiguation: the team had three similarly-named docs. One covered token refresh rotation (wrong topic), one was an "Archived Copy," and the active one (`ab3ad48d`) was the fallback plan itself — that's the one renamed. (The API returned a cosmetic null on the `success` field in the mutation payload, but the update verified cleanly.)
