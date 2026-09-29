I was unable to change Maya Chen's email to maya.chen.new@northwind.example via the Linear API.

**Findings:**
- Located Maya Chen: ID `u-maya`, current email `maya.chen@northwind.example`.
- The `User` type exposes an `email` field (readable), but the available mutations do not support updating it:
  - `userUpdate` uses `UserUpdateInput`, whose fields are only: avatarUrl, description, displayName, name, statusEmoji, statusLabel, statusUntilAt, timezone — **no `email`**.
  - `userSettingsUpdate` uses `UserSettingsUpdateInput` (notification/subscription prefs) — **no `email`**.
  - No other mutation (e.g., `organizationInviteCreate`, admin role mutations) provides an email-change parameter for an existing user.
- A direct mutation attempt confirmed the server rejects it: `Field 'email' is not defined by type 'UserUpdateInput'`.

**Conclusion:** Linear's email address is tied to a user's authentication identity and can only be changed through the Linear account settings in the app (with re-authentication). There is no supported GraphQL API mutation to modify an existing user's email, so this task cannot be completed through the API.
