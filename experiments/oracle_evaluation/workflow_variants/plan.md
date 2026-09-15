# Workflow implementation variants — Slack 98

Five independent repeats each (increased by the user before launch):

A ordered: unchanged policy and schema; append a short instruction to finish applicability across all lines before execution, then grounding, then accounting.
B separated: A plus three labeled concise clauses inside each existing explanation string (Applicability / Execution / Grounding). No schema fields added.
C two-turn: baseline policy, existing applicability-only projected output in turn 1; retain the exact conversation and assistant response and request the full assessment in turn 2. No new initial context, no semantic feedback. The full final schema is unchanged.

All use same recorded Slack 98 evidence, Sonnet 5, medium effort, 16,000 output-token cap, after-evidence placement. Launch independent conversations in parallel; turns within a conversation stay sequential. Existing one mechanical repair allowed after each completed full assessment, with original and repaired judgments compared separately. Prior baseline is the five-run grounding-procedure experiment (3/5 correct mutation applicability, 5/5 consistent expected grounding and L3 performed). No additional baseline calls initially.

Expected: L1-L6 active/performed, L7-L8 inactive/performed, O1/O2/O3/O5 correct and O4/O6/O7/O8 incorrect. No missing task lines, card links, net changes or response paragraphs. These expectations and this plan are not model inputs. Compare categorical verdicts, first-stage/final changes, thinking-summary clarity, validation and repairs, latency, total input/output/thinking usage, and output size. No semantic repairs or test-specific rules. Choose the least complex variant supported by observations; five repeats of one instance cannot establish a low general error rate.
