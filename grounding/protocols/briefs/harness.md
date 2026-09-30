# Brief: the second harness (session "harness")

Rules for every session: [README.md](README.md). Study folder: `grounding/runs/harness_scout_01/`.

## The question

Which real-world agent harnesses, other than OpenClaw, can run all three solver models within each provider's
terms, and what would connecting each to our runner take? The models: the self-hosted Qwen3.8-27B (an
OpenAI-compatible endpoint), GPT-6.1 Sol on the PI's OpenAI plan, and Sonnet 5.5 on the PI's Claude plan. The PI
wants a real harness, not our toy loop, and asks whether Claude's and Codex's own agents should count as solvers
themselves.

## Materials

- Our OpenClaw adapter, the model for any integration: `grounding/integrations/openclaw/README.md` and
  `runtime.py` (isolated state per attempt, the curl shim that redirects the services' URLs to the run's
  environment, skills carrying the API documentation, the fake clock for Calendar, the transcript turned into judge
  steps, usage accounting, the 10-minute limit).
- The toy harness for comparison: `grounding/solver/README.md`.
- The PI's notes, section E, and OpenClaw's own documentation on subscription use (installed under
  `~/.npm-global/lib/node_modules/openclaw/docs/concepts/oauth.md`), which states OpenAI's login is supported in
  third-party tools and that Anthropic staff allowed Claude CLI reuse.

## Steps

1. Desk survey of candidates: Claude Code (headless `claude -p`), Codex CLI, OpenCode, Goose, Cline or Roo, Aider,
   and any other harness with real users. For each: which of the three models it can run and how (native provider,
   OpenAI-compatible endpoint, Anthropic-compatible endpoint, proxies); whether the PI's plans may be used in it,
   from the providers' own terms pages, with links and dates; tool set (shell, files, web); transcripts we can turn
   into judge steps; clock control; per-run isolation; timeouts; usage reporting.
2. Smoke tests for the two best candidates, on three of our tests each, with the run's environment reached through
   our curl shim: Claude Code with Sonnet 5.5 on the plan; Codex CLI with Sol on the plan, at most 10 requests in
   total (the plan's quota is reserved for the lead's runs). Qwen only if the lead says the self-host is up; do not
   use Purdue. Keep every transcript.
3. Estimate the integration for each: what of the adapter transfers, what is new, and the risks.
4. Recommend one harness, or a pairing of the vendors' own agents if that is the honest answer, with the reasons.

## Deliverable

`grounding/runs/harness_scout_01/report.md`: status; the candidate table; the terms findings with sources; the
smoke evidence; the integration estimates; the recommendation. Message the lead after the desk survey and at the end.
