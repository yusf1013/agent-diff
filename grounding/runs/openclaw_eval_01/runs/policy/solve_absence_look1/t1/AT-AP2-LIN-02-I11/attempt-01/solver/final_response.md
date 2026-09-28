Hold on — I found the issue, but the details don't fully match your description, so I want to confirm before changing anything.

**What I found:**
- **"Renew SSO certificate" (IT-2)** — filed by Leo Park (leo.park@northwind.example) ✓ — but it's assigned to **Dana Whitfield, `dana.whitfield@northwind.example`**, who is **not** a guest (internal employee, `guest: false`)
- **Dana Whitfield, `dana.whitfield.ext@northwind.example`** — this one *is* a guest/contractor (`guest: true`), but has **zero issues assigned** to her, SSO or otherwise

So the only "Renew SSO certificate" issue is assigned to the internal Dana, not the guest contractor. It looks like there may be a name collision in Linear (two "Dana Whitfield" users), and your description matches neither user fully.

How do you want to proceed?
1. **Mark IT-2 as Urgent anyway** (assuming the internal Dana Whitfield is who you meant)
2. **Something else** — e.g., if you have the issue identifier or a different title in mind, send it over and I'll pull it up
