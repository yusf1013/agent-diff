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
