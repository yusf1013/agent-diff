# Reading a trial against its test's wording

You will read one recorded trial from a test of an AI assistant (the solver) that acts on a work service (files,
chat, calendar or an issue tracker) for a user. The test's author wrote a request and decided what it means: which
record it refers to, or that no record fits, or that several records fit and the solver should ask which one. The
bundle states the author's decision (the records marked TARGET, and each DECOY with the condition it fails), the
service's records, the solver's calls with its reasoning, and its final answer.

Your task is not to grade the solver against the author's decision. Your task is to decide whether the author's
decision is the only reasonable reading of the request, given what the solver did.

1. Read the request as a careful colleague of the user would, with the service's ordinary meaning of its words (what
   an action does in that service, what a term usually refers to there).
2. State the author's reading: what the request refers to, according to the bundle.
3. State the solver's reading: the reading under which what the solver did or answered would be right. If no
   reading makes it right, say so.
4. Choose one:
   - `test_wording`: the solver's reading is at least as natural as the author's, so the trial does not show a
     mistake. This includes a request whose words exclude a record the author counts as a match, include one the
     author counts as a decoy, or single out one record where the author counts several.
   - `natural_ambiguity`: the request can be read the solver's way, but the author's reading is clearly the more
     natural one; the solver misread a request that ordinary language leaves somewhat open.
   - `solver_error`: no reasonable reading of the request supports what the solver did.

Judge from the request's words and the records, not from the solver's arguments: a solver can argue for a reading
the words do not support, and it can act on a reasonable reading without saying so. Service behaviour that differs
from the real service, timeouts and other failures are outside this question; judge only the reading of the request.
