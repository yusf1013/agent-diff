I checked Linear, and there's **no Web team issue assigned to Maya Chen that blocks "Checkout crash on Safari" (WEB-1)** — so I didn't change anything.

Here's what I found:

- **WEB-1 – Checkout crash on Safari** (assigned to Leo Park) has exactly one blocking relation: it **blocks** WEB-5.
- The only Web team issue assigned to Maya Chen is **WEB-5 – Retry backoff for failed webhooks**, but the direction is reversed: WEB-1 blocks *it*, not the other way around.
- I also checked all other Web team issues (WEB-2, WEB-8) — neither has any blocking relations, and both are assigned to Leo Park.

So the blocker relationship runs the opposite way. If you actually meant setting WEB-5's estimate to 5 (the Maya Chen Web issue involved in that pairing), just say the word and I'll update it.
