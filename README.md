# uw-daily-analysis

**Status: retired, frozen as history (2026-09-06).** This repo is no longer run. It is kept public as the
record of a 2026 experiment: a post-market options-flow research desk built as a Claude Code agent fleet
on Unusual Whales data, with a calibration loop that graded its own calls against realized outcomes.

## What is retired, and where

| Command / product | Repo | Status |
|---|---|---|
| `/daily-analysis` (16-agent nightly report + `decision.json` envelope) | this repo | **retired 2026-09-06**; last run 2026-09-04 |
| `/weekly-analysis` (same fleet on 5-day inputs + thesis scorecard) | this repo | **retired 2026-09-06**; last run 2026-W36 |
| `/calibration-audit` (path-aware outcome grading, McNemar, BH, log-loss) | this repo | **retired 2026-09-06**; last run 2026-09-05 |
| `/market-scan`, `/weekly-review` Layer 2, its `/calibration-audit` (the June redesign, 7 agents) | `market-analysis` | **frozen 2026-09-05** after 54 sessions; no longer run |

The command files are archived, unchanged, in `.claude/_archive_commands/`. `.claude/commands/` no longer
exists, so none of them can be invoked by accident. Do not re-create them or extend the agent fleet.

**What replaced them.** `market-analysis` became a deterministic options-premium engine (`make daily`,
no model in the loop): two pre-registered index-vol strategies with forward paper ledgers, and, from the
week of 2026-09-14, a nightly "desk sheet" that ports the two deterministic pieces of this repo that were
worth keeping (`scripts/zerodte_setup.py` and the dealer-gamma build) and grades its own levels forward.

## Why (the short version)

The full assessment lives in the sibling `findings` repo, `findings/uw-daily-analysis/` (`RESEARCH/90`
commands effectiveness, `91` levels backtest, `92` run cost, `DESIGN/50` desk sheet, `DECISIONS.md`).
`CHANGELOG.md` (2026-09-06 entry) carries the summary. The facts that decided it:

- 878 calls over 73 envelopes, 751 decided: win rate 0.394; the sized book (47 rows) 0.426 with a
  negative mean; the HIGH tier 0.143, the worst tier five audits in a row; log-loss 0.788, above ln 2.
- No sized daily trade after 2026-07-07: 43 consecutive empty boards through 2026-09-04. The frozen rubric's
  top tiers were arithmetically unreachable (the 2026-09-05 audit's own P0), so the calibration loop could
  neither lift the freeze nor be falsified.
- The two blocks the owner actually wanted, the SPY/QQQ dealer-gamma map and the next-day 0DTE setup, are
  two sub-second scripts; the fleet's prose contradicted the script on 92 of 124 index-days.
- The published GEX walls held 37% of next-day ranges against 55% for a same-width box centred on the
  close (McNemar p 2e-5); no level source beat randomly placed levels on touch-and-reject.
- A daily run was about 64 active minutes, 69 M tokens and 23 subagents (about $177 at list price).

## What is here

| Path | What it holds |
|---|---|
| `analyses/daily/<date>/` | 90 daily reports (2026-04-30 to 09-04); `decision.json` envelopes from 05-25 (73) |
| `analyses/weekly/<YYYY-WW>/` | 19 weekly reports (W18 to W36) |
| `analyses/audit/<date>/` | 24 calibration audits with their phase checkpoints and the Yahoo OHLC caches they resolved from |
| `.claude/_archive_commands/` | the three retired command files (plus two pre-v2 versions, untracked) |
| `.claude/agents/` | the 16 agent prompts, in their last audit-applied state (2026-08-30 recs) |
| `schemas/decision_envelope.schema.json` | the envelope contract every report was validated against |
| `scripts/` | stdlib-only helpers (0DTE setup, GEX next-session backtest, Kelly sizing, enrichment, the envelope validator); still runnable |
| `AUDIT.md`, `.claude/PERMISSIONS_AUDIT.md`, `CHANGELOG.md` | the May capability audit, the permission model, the dated change log |

The reports were rendered by `market-visual` and are the evidence for the retirement decision; that is
why `analyses/` is committed despite the `.gitignore` rule (new folders would need `git add -f`).

## Running what still runs

```
python3 -m unittest discover -s scripts/tests -p 'test_*.py'   # 423 tests, stdlib only
python3 scripts/zerodte_setup.py --symbols SPY,QQQ --days 60    # needs the All Options parquet export
python3 scripts/validate_decision.py analyses/daily/2026-09-04/decision.json
```

API keys for the enrichment scripts resolve through `scripts/_env.py` (see `.env.example`); none are
committed. The `uw` and `fz` CLIs the agents called are separate tools and are not part of this repo.

## Reading the history

`CLAUDE.md` is the operating manual the fleet ran under, kept as written except for the retired banner.
`CHANGELOG.md` is newest-first and records every calibration cycle. Each audit folder's `phase_*.md`
files are readable summaries; the `.jsonl` files beside them are the row-level data.
