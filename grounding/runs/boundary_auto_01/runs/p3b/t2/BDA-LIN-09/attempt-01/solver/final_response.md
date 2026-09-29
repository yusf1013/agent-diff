Unable to complete: changing a user's email is not supported by the Linear API.

What I found:
- Maya Chen's Linear user record: id `u-maya`, current email `maya.chen@northwind.example`.
- The only user-account mutation available is `userUpdate` (args: `id`, `input: UserUpdateInput`).
- `UserUpdateInput` only supports: `avatarUrl`, `description`, `displayName`, `name`, `statusEmoji`, `statusLabel`, `statusUntilAt`, `timezone`. There is no `email` field to set.
- `User.email` is exposed as a read-only field, and no other mutation manages a user's login email.

Conclusion: The Linear GraphQL API does not expose a way to change a user's email address. This is a security-sensitive change that must be handled through account settings / authentication flows rather than the API, so I could not set Maya Chen's email to `maya.chen.new@northwind.example`.
