# baselines_02: log

## 2026-09-30, 02:20: set-up

- Brief: [baselines_sonnet.md](../../protocols/briefs/baselines_sonnet.md). The question and the stated defaults are
  in the [README](README.md); nothing had run when they were written.
- `generate.py` wraps baselines_01's pieces (`n0/generate.py`: the repair prompt, the loader, the snapshots;
  `n0/cases.py`: the case builder) with the Claude Code backend of the generation kit. Changes from the Muse arms'
  procedure: the writer (Sonnet 5.5 at effort high, as the Muse arms ran at Muse's effort high) and up to three
  repair turns from the start (the Muse twins had one, then two more for N0M's Box).
- Case ids: `SN0M-<SVC>-<id>` and `SN1M-<SVC>-<id>`, apart from the Muse arms' `N0M-` and `N1M-`.
