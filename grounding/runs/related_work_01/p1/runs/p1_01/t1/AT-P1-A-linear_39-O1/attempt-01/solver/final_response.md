Done. There was no Engineering team in your Linear workspace, so I created one first (ENGIN), then built the chain:

- **ENGIN-1 Alpha** — blocks → Beta
- **ENGIN-2 Beta** — blocks → Gamma
- **ENGIN-3 Gamma**

Verified via the relations query: `ENGIN-1 blocks ENGIN-2`, `ENGIN-2 blocks ENGIN-3`, Gamma has no outgoing relations. The dependency chain is exactly Alpha → Beta → Gamma.
