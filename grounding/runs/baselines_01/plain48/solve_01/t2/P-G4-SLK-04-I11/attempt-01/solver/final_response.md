Found it, but couldn't add the reaction. Here's the situation in #launch-readiness:

- **Maya's card does exist**: "Launch checklist: rollback steps — 1) halt deploys 2) restore snapshot 3) verify health"
- **But the API rejects reactions on it**: both `reactions.add` and `reactions.get` return `message_not_found` for that message (ts `1789899900.000002`), and `conversations.replies` says `thread_not_found`.
- This isn't a permissions issue — I probed the channel with a reaction on a different card and it worked fine, then removed the probe cleanly. So Maya's message itself is the one the API won't operate on (it may be in a broken/special state on the backend).

So: no eyes reaction is on Maya's card, and I couldn't put one there. You could try reacting to it from the Slack UI — if it works there, it's a backend glitch specific to my API token's view; if it fails there too, the message may need to be re-posted by Maya.

The other two cards in the channel (Diego's handoff notes, Leo's cleanup steps) are unaffected and clean.
