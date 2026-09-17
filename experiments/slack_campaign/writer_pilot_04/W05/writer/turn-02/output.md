## Audit

**Roots reconstructed from all facts:**
- #onboarding-fall — onboarding topic, 6 members → qualifies.
- #onboarding-spring — onboarding topic, 6 members (extra unrelated member activity elsewhere doesn't disqualify) → qualifies.
- #onboarding-winter — onboarding topic, only 4 members → excluded, count fails.
- #marketing-launch — 6 members but topic unrelated to onboarding → excluded, topic fails.
- #onboarding-legacy — onboarding topic, 6 members, but private and actor not a member → outside discoverable population, excluded.
- Former row 6 was defective: a "conversation membership record" cannot actually be a workspace-membership record — these are separate relations/tables, so the construction was incoherent and admitted no real chain at all (neither a true negative nor a coherent match). Replaced with a genuine scope-based negative: an identically-purposed channel in a *different* workspace than the actor's selected one, which is excluded because discovery is limited to the actor's selected workspace, not because of any membership miscount.

**Condition → negative mapping:**
- Member count = 6 → #onboarding-winter (4 members).
- Topic concerns onboarding → #marketing-launch (unrelated topic).
- Discoverability (public, accessible) → #onboarding-legacy (private, non-member).
- Workspace scope (actor's selected workspace) → #onboarding-uk (right topic/count, wrong workspace).

**Capability check:** Member count is derived from conversation-membership records (H01) — a specific supported read. Topic is a directly stored/readable attribute. The downstream action, posting a supplied message, is a supported write requiring no extra capability beyond channel access, consistent with the two positive roots. Both negatives relying on access (private / other workspace) are excluded per the discovery rule limiting population to public channels in the actor's selected workspace.

**Repair:** Removed the incoherent membership-binding negative and replaced it with a workspace-scope negative that is structurally sound and does not conflate membership types.

## Final Sketch

**Route:** Conversation → Conversation Membership
**Resolution mode:** multiple

**Request:** "Post 'Please complete the compliance training module by end of this week.' to the onboarding channels that have exactly 6 members."

**Selection conditions:** public channel, in the actor's selected workspace, whose name/topic concerns new-hire onboarding; exactly 6 conversation members (actor included if a member).

| Referent | Environment facts | Interpretation |
|---|---|---|
| #onboarding-fall | Public channel in actor's workspace, topic "New hire onboarding cohort", 6 conversation members | Match |
| #onboarding-spring | Public channel in actor's workspace, topic "New hire onboarding cohort", 6 conversation members; one member also belongs to several unrelated channels and has posted unrelated messages elsewhere | Match with unrelated activity |
| #onboarding-winter | Public channel in actor's workspace, topic "New hire onboarding cohort", but only 4 conversation members | Wrong member count only |
| #marketing-launch | Public channel in actor's workspace, topic "Q3 product launch planning", 6 conversation members | Wrong topic/name (not onboarding) only |
| #onboarding-legacy | Private channel, topic "New hire onboarding cohort", 6 conversation members, actor not a member | Not publicly discoverable — access fails |
| #onboarding-uk | Public channel, topic "New hire onboarding cohort", 6 conversation members, but located in a different workspace than the actor's selected one | Outside actor's workspace scope — discovery fails |