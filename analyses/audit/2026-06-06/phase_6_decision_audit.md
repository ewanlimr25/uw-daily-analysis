# Phase 6 — Decision-Process Audit (2026-06-06 · C24 gate effectiveness)

## 1. Quant compliance (`signal-confluence-quant`)

- **Σ-points reconciliation: 126/126 structured rows** (Σ component points == raw_score). The
  validator guarantees this on envelopes; the prose-era rows that carried components also pass.
- **Sizing-map: 256/266 compliant-or-downgraded.** 10 apparent upgrades above the
  win-rate-implied size (map: ≥0.70 full / 0.50–0.70 half / <0.50 starter; `quarter`
  respected; downgrades always allowed):
  - **9 are legacy-prose rows from 05-06…05-11 + W21** — the known pre-tightening cohort,
    unchanged from prior audits.
  - **1 is NEW and envelope-era: `LLY 2026-06-05` — claimed_win_rate 0.392 → map says
    `starter`, sized `half` (pre-risk).** First sizing-map violation since the envelope
    discipline shipped. One row, but it's verbatim provenance, in the newest report, on a
    sub-0.50 win-rate name into a risk-off tape. `signal-confluence-quant.md` needs the
    reminder, not a rewrite. (Phase 7, P1.)
- Envelope rows sized above the map at *final* size: **0** — risk-monitor never up-sized.

## 2. Risk-monitor compliance + gate firing (84 envelope rows with `gate_verdicts`)

| Gate | Fired | Of 84 | Note |
|---|---|---|---|
| event_risk | 57 | **68%** | fires on 2 of every 3 calls |
| fundamentals | 26 | 31% | |
| regime | 12 | 14% | |
| panic | 11 | 13% | |
| cluster | 11 | 13% | |
| vrp | 4 | 5% | |
| sector | 1 | 1% | |

Missed-gate ledger: **0 candidate missed event_risk firings** — nothing is slipping past;
the gate's problem is the opposite (below). No agent-prompt drift exceeds the 20% threshold
this run.

## 3. ⭐ C24 gate effectiveness — does the gate find losers? (decided rows only)

| Gate | Downgraded WR | Ungated WR | Decided-N (gated) | Read |
|---|---|---|---|---|
| **event_risk** | 43% (n=46) | 43% (n=7) | **≥10 → reportable** | **Zero discrimination.** Fires on 68% of calls and its downgrades perform exactly like the ungated book. A gate that taxes everything equally is a haircut, not a filter. |
| **fundamentals** | 39% (n=23) | 47% (n=30) | ≥10 → reportable | **Working direction** — gated names underperform by 8pp. |
| panic | 20% (n=5) | 46% (n=48) | <10 ADVISORY | Strong loser-finding direction; the front-IV panic gate looks real but thin. |
| cluster | 71% (n=7) | 39% (n=46) | <10 ADVISORY | **Anti-effective direction** — correlation-cluster downgrades hit *winners*. Watch; do not act (C24 floor). |
| vrp | 57% (n=7) | 41% (n=46) | <10 ADVISORY | Mildly anti-effective direction; thin. |
| regime | 44% (n=9) | 43% (n=44) | <10 ADVISORY | No discrimination yet. |
| sector | n=0 | — | — | Never fired on a decided row. |

### Fundamentals-gate FP-rate (CAUTION+VETO pooled, n=20 decided — first reportable read)

- CONFIRM: 8W/7L = **53%** · CAUTION: 7W/11L = **39%** · VETO: 1W/1L (n=2, thin).
- **`veto_fp_rate` (CAUTION+VETO would-have-won) = 40% (8/20).** The gate's downgrades lose
  materially more than its confirms (−14pp) — **the fundamentals gate is earning its keep**,
  the first Phase-2b stage with reportable positive discrimination. Pure-VETO N is still 2;
  keep tracking before claiming the kill-switch itself is calibrated.

### Debate-gate effectiveness (n=34 decided with residual)

The envelope stores a **single scalar** `debate_residual_confidence` (not the bull/bear pair
the skill's check expects — observability gap, Phase 7 P2). Stratifying on the scalar:
- residual ≥ 0.6 → **48% WR (12/25)** · residual < 0.6 → **33% WR (3/9)**.
- Directionally right (higher residual → more wins), and the low-residual cohort losing 2-of-3
  says the debate's *doubt* is informative. Advisory at this N; not theatre, not yet proven.

## 4. Desk read (buy-side PM post-mortem)

1. **The gate stack's one well-functioning stage is fundamentals** (−8pp on gated names, 40%
   FP-rate on 20 decided) — ironic, given it's the newest gate and advisory-leaning. C24's
   "did VETO kill alpha?" worry is so far **no**.
2. **`event_risk` is the gate to fix**: 68% firing rate, zero discrimination on 46+7 decided.
   It has become a default stamp — when everything is event-risk, nothing is. Tighten its
   trigger definition (named binary event within the horizon window, not ambient macro), do
   NOT remove it (C24 — its insurance value belongs to the regime that finally showed up
   06-05; notably it still didn't discriminate *that* week).
3. **cluster/vrp anti-effective directions are watch-items only** (n=7 each) — flagged for
   the next audit when June resolves; the C24 floor forbids action.
4. **Process discipline is otherwise intact**: 100% Σ-points, no final-size upsizing, no
   missed event_risk firings, one envelope-era sizing slip (LLY).

## Output
- `phase_6_decision_audit.jsonl` — compliance flags + per-gate effectiveness numerics.
- `phase6_decision.py` — reproducible.
