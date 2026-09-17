Route: Conversation Membership → User → Reaction → Message → Conversation

Request: Is Alex still a member of the channel where they reacted 🚀 to the message announcing the new deployment pipeline?

| Referent | Environment facts | Interpretation |
|---|---|---|
| Alex Rivera's membership in #infra-updates | Alex Rivera reacted 🚀 to the message "New deployment pipeline is live" posted in #infra-updates, and Alex Rivera is a current member of #infra-updates | Alternative through Alex Rivera |
| Alex Kim's membership in #platform-eng | Alex Kim reacted 🚀 to the message "New deployment pipeline is live" posted in #platform-eng, and Alex Kim is a current member of #platform-eng | Alternative through Alex Kim |
| Alex Rivera's membership in #infra-updates (wrong emoji) | Alex Rivera reacted 👍 (not 🚀) to the deployment pipeline message in #infra-updates, and is a member of #infra-updates | Wrong emoji only |
| Alex Kim's membership in #platform-eng (wrong topic) | Alex Kim reacted 🚀 to a message announcing an office relocation, not the deployment pipeline, in #platform-eng, and is a member of #platform-eng | Wrong message topic only |
| Alex Chen, no membership in #backend-team | Alex Chen reacted 🚀 to the deployment pipeline announcement posted in #backend-team, but Alex Chen has no membership record for #backend-team (left the channel) | Missing membership relation only |
| Alex Diaz, membership in #platform-eng only | Alex Diaz reacted 🚀 to the deployment pipeline announcement posted in #infra-updates, but Alex Diaz's only channel membership is in #platform-eng, not #infra-updates | Membership-channel/message-location binding failure only |