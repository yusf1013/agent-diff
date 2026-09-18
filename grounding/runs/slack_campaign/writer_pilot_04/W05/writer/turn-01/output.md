**Route:** Conversation → Conversation Membership
**Resolution mode:** multiple

**Request:** "Post 'Please complete the compliance training module by end of this week.' to the onboarding channels that have exactly 6 members."

**Selection conditions:** public channel whose name/topic concerns new-hire onboarding; exactly 6 conversation members (actor included if a member).

| Referent | Environment facts | Interpretation |
|---|---|---|
| #onboarding-fall | Public channel, topic "New hire onboarding cohort", 6 conversation members | Match |
| #onboarding-spring | Public channel, topic "New hire onboarding cohort", 6 conversation members; one member also belongs to several unrelated channels and has posted unrelated messages elsewhere | Match with unrelated activity |
| #onboarding-winter | Public channel, topic "New hire onboarding cohort", but only 4 conversation members | Wrong member count only |
| #marketing-launch | Public channel, topic "Q3 product launch planning", 6 conversation members | Wrong topic/name (not onboarding) only |
| #onboarding-legacy | Private channel, topic "New hire onboarding cohort", 6 conversation members, actor not a member | Not discoverable/public — fails container access |
| #onboarding-eu | Public channel, topic "New hire onboarding cohort", 6 conversation memberships recorded but one is a workspace membership rather than a conversation membership for this channel | Miscounted membership binding — true conversation-member count is 5 |