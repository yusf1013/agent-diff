Found Diego Alvarez's (U_DIEGO) message about the gateway rollback ("Gateway rollback finished on prod, the error rate is back to baseline.") in 3 private channels and set the topic of each to "Post-release monitoring":
1. C_REL (release-ops)
2. C_REL-sm5 (deploy-ops)
3. C_REL-sm8 (release-sync)
All three conversations.setTopic calls returned ok:true.
