I updated the Finance folder (ID: 7100), but the **`modified_by`** field still shows **Jordan Lee** (the currently authenticated user).

**Key finding:** In the Box API, `modified_by` is a **read-only, system-populated field**. It is automatically set to whichever authenticated user performs the last update to the item. It cannot be manually assigned to a different user.

Current state of the Finance folder:
- **Name:** Finance
- **Modified By:** Jordan Lee (ID: 30000000001)
- **Modified At:** 2026-09-29T06:12:23

To show **Leo Park** as the last modifier, an update would need to be performed on the Finance folder while authenticated as Leo Park. I cannot accomplish this with the current credentials (Jordan Lee).
