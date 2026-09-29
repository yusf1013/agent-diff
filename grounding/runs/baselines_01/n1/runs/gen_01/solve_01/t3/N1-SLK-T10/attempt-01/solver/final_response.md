I couldn't complete the invite — jordan.lee@example.com isn't in the workspace, so there's no user ID to invite.

What I checked:
- **#events2** exists (public channel, ID `C_EV2`, 2 members).
- **users.list** returned all 8 workspace members — no Jordan Lee, and no user with that email. (Only emails on file are `@northwind.example` or Nina Patel's `@example.com`.)
- **users.lookupByEmail** isn't available in this environment, so I couldn't double-check by email directly.

To get Jordan in, someone with admin access would first need to send them a workspace invite (by email) and have them accept it. Once they're a member, tell me and I'll drop them into #events2 — or if you can confirm Jordan's actual workspace email/user ID, I'll re-run the invite.
