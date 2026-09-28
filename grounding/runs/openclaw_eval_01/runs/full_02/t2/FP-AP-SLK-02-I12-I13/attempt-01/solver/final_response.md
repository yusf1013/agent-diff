No such channel exists. I checked all 4 channels in the workspace — there's no incident channel dedicated to the checkout outage:

- **incidents-auth** — active, but explicitly "unrelated to checkout" (login rate-limiting)
- **incidents-billing** — archived; billing reconciliation, though its topic mentions it "holds the checkout outage postmortem thread for reference"
- **incidents-shipping** — archived, logistics incidents

Closest match is **incidents-billing** since it references the checkout outage postmortem, but it's a billing channel, not the checkout incident channel itself — so I didn't unarchive it. Say the word if you want that one unarchived instead.
