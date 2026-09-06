# /calibration-audit — Implementation Plan

*Drafted 2026-05-09. This plan governs both (a) the skill scaffolding under `.claude/commands/calibration-audit.md` and (b) the pilot run that produces `phase_1_*.md` through `phase_7_*.md` in this directory.*

---

## Skill location decision

Project convention is `.claude/commands/` — the existing `/daily-analysis` and `/weekly-analysis` skills both live there. CLAUDE.md lists them under the "Skills" header, confirming that `commands/` is where invokable `/<name>` skills are wired in this project. Therefore:

- **Skill file**: `.claude/commands/calibration-audit.md`
- **Output root**: `analyses/audit/<YYYY-MM-DD>/`
- **Per-phase checkpoints**: `phase_<N>_<slug>.md`

No `.claude/skills/` directory exists or is referenced in this project.

---

## Phase ordering (matches user spec exactly — no deviation)

| Phase | Slug | Output | Depends on | Model |
|---|---|---|---|---|
| 1 | `inventory` | parsed JSONL + checkpoint | analyses/*.md, analyses/weekly/*.md | Haiku 4.5 (parsing is mechanical) |
| 2 | `outcome_resolution` | per-call WIN/LOSS/INCONCLUSIVE | Phase 1 JSONL | Opus 4.7 (judgment on edge cases) |
| 3 | `calibration` | reliability table + Brier + divergence flags | Phase 2 outcomes | Opus 4.7 |
| 4 | `tool_attribution` | tool tier list with marginal-contribution math | Phases 1+2 | Opus 4.7 |
| 5 | `schema_critique` | rubric reweight + tier rebin proposal + holdout test | Phases 3+4 | Opus 4.7 |
| 6 | `decision_audit` | gate-compliance trace per call | Phase 1 + agent files | Opus 4.7 |
| 7 | `recommendations` | prioritized propose-only patch list | All prior phases | Opus 4.7 |

Each checkpoint must be **self-contained** — a reviewer can read it without re-running prior phases. A crash mid-Phase-N must leave Phases 1..N-1 reviewable.

---

## Open defaults to encode in skill frontmatter

```yaml
outcome_windows:
  0DTE: same-day close vs entry
  swing: 3D and 10D
  LEAP: 30D and 90D
  weekly: 5D and 10D
min_dataset:
  daily: 10
  weekly: 3
disposition: propose-only       # v1: never auto-edits agent files
cadence: on-demand
win_threshold: ">=+1R in thesis direction without -1R prior drawdown"
relax_threshold: false          # if true, runs below min_dataset with NOISE banner
```

---

## Pilot run constraints (today, 2026-05-09)

The dataset is **7 daily + 2 weekly reports** — below both default thresholds (10 daily / 3 weekly). The pilot will run with `relax_threshold=true` and stamp every checkpoint with a **DATASET-SIZE-RELAXED** banner. All conclusions are noise-dominated and explicitly marked structural / qualitative rather than statistical.

---

## Implementation order (this session)

1. ✅ Write this plan checkpoint
2. Author `.claude/commands/calibration-audit.md`
3. Pilot Phase 1 — parse 7 daily + 2 weekly reports → JSONL
4. Pilot Phase 2 — call `mcp__uw-historical__trend_analyzer` + `signal_backtest` per ticker × horizon
5. Pilot Phase 3 — calibration math on the limited dataset
6. Pilot Phase 4 — tool attribution
7. Pilot Phase 5 — schema critique (mostly structural; data-thin)
8. Pilot Phase 6 — decision-process audit (process audit doesn't need large N)
9. Pilot Phase 7 — recommendations
10. Write `SUMMARY.md` (≤400 words, desk-strategist voice)

No deviation from the seven phases. Proceeding.
