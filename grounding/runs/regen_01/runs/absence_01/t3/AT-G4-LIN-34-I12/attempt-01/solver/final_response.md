I checked the Linear account and found a potential mismatch — let me lay it out before touching anything:

- There's exactly one document titled **"3D Secure Fallback Plan"**, and it is in the **Payments** team (key `PAY`).
- However, its actual content reads: *"This plan covers adding token refresh rotation for mobile sessions, with expiry windows and retry limits."*

That content is about **token refresh rotation**, not adding a 3D Secure fallback — so it fails the content condition in your request. The other document in the workspace ("Mobile Release Notes") doesn't match either.

I did **not** rename anything. Two options:

1. If you're confident that document is the right one despite the content mismatch, say so and I'll rename it to "3D Secure Fallback Plan — Final".
2. If the 3D Secure fallback plan is somewhere else (different workspace, different title, or a doc created under another name), point me to it and I'll do the rename.
