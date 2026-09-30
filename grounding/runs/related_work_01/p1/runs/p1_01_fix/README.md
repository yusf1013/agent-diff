# p1_01_fix: four P1 variants rerun with repaired seeds

In four underspecified Linear variants, the copied issue took the identifier the replica gives the team's next issue,
because the copy did not advance the team's issueCount (P1's construction flaw, found in p1_01's trial
t2/U-P1-U-linear_38-O1). Each of these requests creates issues in that team, so every issueCreate there failed with a
500. materialize.py now gives a copied issue the team's next number and advances the counter, as creating it through
Linear would (identifiers unchanged). These four variants' p1_01 trials are artifacts of the seed, and their
results come from this run.
