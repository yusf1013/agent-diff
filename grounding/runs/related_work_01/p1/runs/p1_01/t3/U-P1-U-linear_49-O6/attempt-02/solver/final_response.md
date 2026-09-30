All done and verified. Here's what I fixed in the Archaeology team (ARCH):

**1. Deadlock resolved**
- Found two relations: ARCH-1 blocks ARCH-2 (correct) and ARCH-2 blocks ARCH-1 (erroneous)
- Deleted the incorrect `rel-lab-blocks-photo-002` relation — Lab no longer blocks Photography

**2. Workflow extended**
- Created **ARCH-5: "Final Site Report Compilation - Season 3"** in the Archaeology team
- Set up both blockers: ARCH-1 (Photography) → blocks ARCH-5, and ARCH-2 (Lab) → blocks ARCH-5

**3. Assignments**
- ARCH-1 (Photography) → Ximena Rodríguez
- ARCH-2 (Lab Analysis) → Nneka Okonkwo
- ARCH-5 (Final Report) → Søren Andersen

**4. Status moved**
- ARCH-1 is now **In Progress** (no longer blocked)

**5. Documentation comment**
- Added the `WORKFLOW_FIX:` comment to ARCH-2, exactly as specified

Final state verified:
- **ARCH-1** Photography — In Progress, Ximena, blocks ARCH-2 + ARCH-5, blocked by nothing
- **ARCH-2** Lab — Blocked (correctly, by ARCH-1 only), Nneka, blocks ARCH-5
- **ARCH-5** Final Report — Backlog, Søren, blocked by both ARCH-1 and ARCH-2

The chain now reads cleanly: Photography → Lab Analysis → Final Report.
