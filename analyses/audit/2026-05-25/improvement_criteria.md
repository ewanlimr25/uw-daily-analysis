# Improvement Criteria Register — `/daily-analysis` & `/weekly-analysis`

**Run date:** 2026-05-25
**Author voice:** buy-side options PM + sell-side flow trader + market-maker quant (composite desk).
**Mandate:** a research-justified, ranked register of *candidate* improvements. **Propose-only.** No command or agent file was edited this session. The only writes this session were the register (this file) and one config edit (wiring the `yahoo-finance` MCP server — see Setup).
**Status of each criterion:** a proposal gated behind a *measurable acceptance criterion* that must pass before `/goal` (or a future apply-mode) ships it.

---

## Setup completed this session (the one allowed config write)

- Added `yahoo-finance` (`uvx mcp-yahoo-finance`, mirrored from the home-scope `~/.claude.json` projects entry) to `.mcp.json` and granted `mcp__yahoo-finance__*` in `.claude/settings.json`.
- **Verified resolution:** `claude mcp list` → `yahoo-finance: uvx mcp-yahoo-finance - ✓ Connected`. Protocol handshake returns `mcp-yahoo-finance v1.27.1`, 10 tools: `get_current_stock_price`, `get_stock_price_by_date`, `get_stock_price_date_range`, `get_historical_stock_prices`, `get_dividends`, `get_income_statement`, `get_cashflow`, `get_earning_dates`, `get_news`, `get_recommendations`.
- This unblocks the price-history-dependent criteria (PEAD continuation **C7**, 52-week-high gate **C8**) and gives an independent cross-check on UW-derived levels and the 03-27→04-27 UW data gap.

---

## Evidence base & methodology

Three independent evidence streams feed every criterion's dual gate:

1. **Empirical backbone — the 2026-05-23 `/calibration-audit`** (most recent of three full runs: 05-09, 05-15, 05-23; plus a 05-24 GEX-feasibility note). The daily track record is **unchanged since Friday 2026-05-22** (no reports 05-23→05-25), so re-running 7 phases on an identical dataset would be wasteful — the 05-23 output is the correct "starting evidence." Its P0/P1 patches were already applied in commit `a1d0507`; this register goes **beyond** those, it does not re-litigate them.
2. **Live tool probes (this session)** — I called the backing `uw-pp` MCP tools directly to characterise current behaviour (see "Tool-probe findings" below). These supersede the 05-23 audit where the tool's behaviour has since changed.
3. **Academic / industry literature** — verified via WebSearch; specific findings (not vibes) cited inline and collected in the Appendix.

### Hard limitations (these bound every "validated" claim)
- **Dataset is tiny and non-contiguous.** `historical_available_dates` shows ~30 trading days total with a **one-month hole (2026-03-27 → 2026-04-27)**. Effective continuous window ≈ 04-27 → 05-22 (~19 sessions) plus an earlier 03-13→03-27 block. **Any in-repo "backtest" is sample-starved**; this is itself the motivation for several criteria (Bailey & López de Prado: minimum backtest length, PBO).
- **The track record is 73 fully-resolved calls** (05-23 Phase 3), single regime (FAIR/MILD VRP, TRANSITIONAL→UPTREND). No vol-shock in sample — short-vol left tail unsampled.
- Where I could not validate an edge on this repo's data, the entry is marked **`UNVALIDATED`** and its acceptance criterion *includes building the validation first*.

### Tool-probe findings (2026-05-25, direct `uw-pp` calls)
| Probe | Result | Implication |
|---|---|---|
| `historical_signal_backtest dark_pool_accumulation` | `total_signals: 0` (empty) | The single best-calibrated class **cannot be backtested** by its own tool. |
| `historical_signal_backtest bullish_flow` | n=8, **win_rate 100%**, all signals dated 05-19/05-20 | No regime control + ~2-day depth → this is **beta in an up-tape**, not an edge. |
| `historical_signal_backtest bearish_flow` | n=7, win_rate **28.6%** (same week) | Shorts "lost" only because the tape rose — unconditional WR is regime-confounded. |
| `historical_signal_backtest high_iv_rank` | n=10, vol_realisation 60% | Mixed; small N. |
| `historical_signal_backtest volume_spike` | n=9, 22.2%, universe = `GIF/BLCN/PEX/IGLD/UTHY/ESGE` | **No liquidity floor** — returns un-tradable micro-ETFs. |
| `historical_vrp SPY` | IV30 0.145 / RV 0.106 / VRP +0.039 / regime **FAIR** | Works per-ticker; under-used (cited n=3, INSUFFICIENT_N in track record). |
| `historical_trend NVDA` | full per-day bullish/bearish premium, net_flow, IV-rank, OI | Rich; supports OI-confirmed-flow and realised-WR computation. |

> **Correction to the 05-23 audit:** that audit reported `historical_signal_backtest` returned empty for *all five* classes. As of today it returns data for four of five (`dark_pool_accumulation` still empty). The tool is **not dead — it is worse in a subtler way**: regime-confounded, ~2-day-deep, no liquidity floor. The fix is not "restore the tool," it is "stop trusting an unconditional, sample-starved win-rate for sizing" (**C2**).

---

# EXEC SUMMARY — Top P0 changes

> **Revised 2026-05-25 (post-review).** The user correctly flagged that the original P0-C1 ("decision.json never emitted") rested on a stale premise. Git confirms the envelope emission + schema + validator **all first landed in commit `193afec` on 2026-05-23**, and the most recent daily report (`2026-05-22.md`) **predates the feature**. No `/daily-analysis` has run since (05-23 Sat, 05-24 Sun, 05-25 today). The absence of envelopes is therefore *expected for legacy reports*, not a foundational bug. **C1 is downgraded from P0-fix to P2-verification** (smoke-test the new emission on the next run).
>
> **Pass 2 — full staleness sweep (every criterion grepped against current files, not summaries):**
>
> | ID | Verdict | What the current files *already* do (so the criterion was narrowed) |
> |---|---|---|
> | C1 | **STALE → P2-verify** | Envelope shipped 05-23 (`193afec`); just unrun. |
> | C2 | **PARTLY STALE → narrowed** | Quant already N-caps win-rate (0.75/0.85/0.90, lines 46-51) + short-floors. Residual = market-excess adj + liquidity floor + cap-threshold below 0.70. |
> | C4 | **PARTLY STALE → narrowed** | sweep-tracker already requires cum_flow-*direction* alignment (mega-cap, ranking, unscored). Residual = OI-confirmed *opening* on the scored flow classes. |
> | C5 | **PARTLY STALE → narrowed** | VRP already drives *sign*-based up/down sizing (risk-monitor L16, vol-surface L12). Residual = *magnitude*/percentile scaler. |
> | C3 | holds (minor credit) | Quant cites payoff asymmetry anecdotally (L52) but computes no per-call expectancy. |
> | C6 | holds (minor credit) | vol-surface reads `term_skew` for tail context, not as a lottery fade. |
> | C7,C9,C10 | **hold fully** | No PEAD drift play; panic gate still binary (no slope scaler); no routine/opportunistic insider split. |
> | C8,C12 | **hold fully** | No 52wk/price-structure anchor; no liquidity floor anywhere. |
> | C11,C13,C14 | hold | Conjunction, cross-agent class-precedence, and yahoo-cross-check genuinely absent. |
>
> Net: no criterion was withdrawn, but **C2/C4/C5 were materially narrowed** (the repo already guards more than the first draft credited), and **C1 dropped to verification**. The two live-evidence P0s (C11, C12) and the narrowed C2 still stand.

The desk's one-paragraph read: **the analytical fleet is well-scoped, the 05-23 rubric patches were correct, and the machine-readable calibration loop is freshly wired (just unexercised). The two live problems are that it sizes off a structurally unreliable win-rate, and that the top-of-book score is an additive pile of correlated signals.**

1. **P0-C2 — Add a market-excess (regime) adjustment + liquidity floor on top of the existing win-rate cap.** The Step-5 ladder (full ≥0.70 / half 0.50-0.70 / skip <0.50) keys off `historical_signal_backtest`, which **today** (live probe) returns a 100% bullish win-rate measured over two days of an up-tape on a universe that includes micro-ETFs. **Credit where due (verified this pass):** the quant is *not* naive — it already N-caps the quote (n<10 → 0.75, 10-20 → 0.85, ≥20 → 0.90, never 1.00; quant lines 46-51, motivated verbatim by "low N routinely returns 100% in trending tapes") and floors the short side. **But the cap controls magnitude, not beta:** a 0.75-capped up-tape bullish name *still clears the 0.70 full-size line*. The genuine residual gap is a *market-excess* win-rate (signal WR − SPY same-window WR) so beta can't masquerade as edge, plus a liquidity floor (= C12), plus tightening the n<10 cap below 0.70 so single-regime small-N signals size at most half.

2. **P0-C11 — Make the top-of-book score a conjunction, not an additive narrative pile.** The 05-23 audit's sharpest finding is a **tier inversion (HIGH 60.0% < MED 62.5%, n=49)**. The audit diagnosed it under the prior 3-of-4 gate ("filters the wrong way around") and applied a 3-of-5 gate as the fix — but that fix is **unvalidated out-of-sample** (the audit explicitly defers confirmation to a 2026-05-30 re-run). C11 is an *independent, complementary* lever on the same inversion, not a duplicate of the 3-of-5 gate. Additive HIGH calls built from correlated same-view signals (DP block + institutional-accumulation + conviction-matrix) lose, while the genuine ≥0.80 WR appears only when `dark_pool_block_stratified` **∧** `cum_premium_flow` direction **∧** `insights_institutional_accumulation` all agree. Gate the big accumulation points on `cum_premium_flow` alignment (≥$50M, same sign) — a conjunction multiplier — to restore HIGH>MED monotonicity. (Complements both the 3-of-5 gate *and* the existing flow_conflict penalty — see C11 overlap note.)

3. **P0-C12 — Liquidity floor on every screened candidate.** Cheapest high-value fix (ranks #2 overall): the `volume_spike` probe returned `GIF/BLCN/PEX/IGLD` micro-ETFs. A 20-day-ADV / price floor cleans the funnel *and* the win-rate denominator (shared with C2) in one change.

Everything below is ranked. P0 = sizing-breaking or calibration-breaking on **live** evidence; do before next session. P1 = clear edge, ship this/next cycle. P2 = polish, needs validation first, or verification of a just-shipped feature.

---

## Ranking model

Each criterion scored 1–5 on **Edge** (expected P&L/calibration impact), **Evidence** (strength of the dual gate), and **Cost-inv** (5 = cheap to implement). **Priority score = Edge × Evidence × Cost-inv** (max 125). Ties broken by dependency order (foundational first).

Re-ranked after the staleness sweep narrowed C2/C4/C5. Sorted by score; the **Δ** column marks what the narrowing changed.

| Rank | ID | Criterion | Edge | Evidence | Cost-inv | Score | Tier | Δ vs draft |
|---|---|---|---|---|---|---|---|---|
| 1 | C11 | Conjunction (interaction) scoring for accumulation | 5 | 4 | 4 | **80** | **P0** | — |
| 2 | C12 | Liquidity floor on all screened candidates | 4 | 4 | 5 | **80** | **P0** | tier P0/P1→P0 |
| 3 | C2 | Market-excess + liquidity floor *over* the existing win-rate cap | 4 | 5 | 3 | **60** | **P0** | 75→60 (E5→4) |
| 4 | C7 | Post-earnings drift (PEAD) continuation play | 4 | 5 | 3 | **60** | **P1** | — |
| 5 | C1 | **Verify** the just-shipped decision-envelope emission | 2 | 5 | 5 | **50** | **P2 (verify)** | 100→50, P0→P2 |
| 6 | C8 | 52-week-high proximity gate | 3 | 4 | 4 | **48** | **P2 (quick-win)** | — |
| 7 | C4 | Opening-confirmed flow on the *scored* classes | 4 | 5 | 2 | **40** | **P1** | 50→40 (E5→4) |
| 8 | C3 | Expectancy / fractional-Kelly sizing (phased) | 5 | 4 | 2 | **40** | **P1** | — |
| 9 | C5 | Single-name VRP *magnitude* scaler | 3 | 4 | 3 | **36** | **P2 ↓** | 60→36, **P1→P2** |
| 10 | C9 | IV term-structure SLOPE scaler | 3 | 4 | 3 | **36** | **P2** | — |
| 11 | C13 | Mutually-exclusive signal-class routing | 3 | 3 | 4 | **36** | **P2** | — |
| 12 | C14 | Yahoo independent price/earnings cross-check | 3 | 3 | 4 | **36** | **P2 (enabler)** | — |
| 13 | C6 | Lottery / expensive-skew short-vol fade | 3 | 4 | 2 | **24** | **P2** | — |
| 14 | C10 | Opportunistic-vs-routine insider weighting | 2 | 4 | 3 | **24** | **P2** | — |

> **Tiering is score-guided but actionability-adjusted** — score sets the order, but verification-only and needs-its-own-validation items are held at P2 regardless of a high cost-cheap score, and high-edge new plays stay P1 even a notch lower-scored:
> - **P0** (live-evidence, fixes the *current* book, ship before next session): **C11, C12, C2**.
> - **P1** (clear, well-evidenced edge to ship this/next cycle; higher build cost accepted): **C7, C4, C3**.
> - **P2**: verification-only (**C1**, score 50), a needs-its-own-validation quick-win (**C8**, 48), incremental refinement of *already-present* logic (**C5, C9**), de-dup/enabler (**C13, C14**), and lower-edge/data-thin (**C6, C10**).
>
> Why C1 (50) and C8 (48) out-score some P1 items yet sit in P2: C1 is pure verification (nothing is broken) and C8 must first clear its own WR-split backtest before it scores. Why C5 fell from P1: the staleness sweep showed VRP *sign*-based sizing already exists (risk-monitor L16) — only the *magnitude* scaler is new, so its incremental edge dropped 4→3.

---

# THE REGISTER

Template per entry — (a) desk rationale · (b) academic evidence · (c) repo backtest · (d) acceptance criterion · (e) target files + change type · conflict note.

---

## P0 — sizing- or calibration-breaking on live evidence (fix before next session)

> **C1 relocated.** The original lead P0 ("emit the decision envelope") was downgraded to **P2-verify** after git review showed the feature shipped 2026-05-23 and simply hasn't run yet — nothing is broken. See the revised **C1** entry in the P2 section.

### C2 — Market-excess (regime) adjustment + liquidity floor *on top of* the existing win-rate cap
**(e) Target / change type:** `.claude/agents/signal-confluence-quant.md` (win_rate sourcing step 2 + the N-conditional cap at lines 46-51); optional `scripts/excess_winrate.py` — **agent (+ script).** Also flags a **new MCP capability** (N2 below).

- **What already exists (verified this pass — do NOT re-implement).** The quant is not naive about trending-tape win-rates: lines 46-51 impose an **N-conditional cap** (`n<10` → 0.75, `10≤n<20` → 0.85, `n≥20` → 0.90, never 1.00), motivated verbatim by *"in-sample backtest with low N routinely returns 100% in trending tapes."* Line 52 adds a **short-side floor** (`win_rate<0.50` ⇒ `starter`/`skip`), and the 05-23 P0.1 fallback handles the *empty* case (cap 0.65, N<5 → 0.50). So three of the four obvious failure modes are already guarded.
- **(a) Desk rationale (the genuine residual).** The N-cap controls *magnitude* but not *beta*: today's `bullish_flow` 100% (n=8) is capped to **0.75 — which still clears the 0.70 full-size line.** A signal measured purely in an up-tape thus still full-sizes. The unaddressed gaps are (i) a **market-excess** win-rate (signal WR − SPY same-window WR) so beta can't read as edge; (ii) a **liquidity floor** (none exists — see C12); (iii) the n<10 cap sitting *above* the 0.70 full-size threshold, so a single-regime, 8-signal class can still be sized full.
- **(b) Academic.** López de Prado (selection bias / PBO: unconditional, multiply-tested win-rates are inflated). Bollerslev-Tauchen-Zhou (returns are conditional on the VRP state — an unconditional WR blends incompatible regimes). ([BTZ 2009, RFS 22:4463](https://academic.oup.com/rfs/article-abstract/22/11/4463/1565787))
- **(c) Repo backtest. MEASURED.** `bullish_flow` 100% (n=8, all 05-19/20) → **capped to 0.75 → still full size**; `bearish_flow` 28.6%; `volume_spike` 22.2% on `GIF/BLCN/PEX/…` (no liquidity floor). Phase 3 corroborates `multi_day_sweep` 0.43 vs 0.70 and `earnings_vol` 0.625 vs 0.85. The existing cap reduces the quoted number but not the sizing *decision* in the up-tape case.
- **(d) Acceptance criterion.** `win_rate` handed to the sizing map = **market-excess** over **n ≥ 10** signals on names passing a **liquidity floor** (20-day ADV ≥ $50M, price ≥ $5); else capped at 0.50 + `low_conviction_proxy`. **Tighten the n<10 cap to 0.69** (one notch below the full-size line) so an 8-signal up-week class sizes at most half. Re-running the probe set must show **no class full-sizing on a single up-week**. Brier (from C1 envelopes) improves vs the 0.224 baseline at next audit.
- **Conflict note.** Subsumes the liquidity portion of **C12**. *Extends* the existing N-cap and P0.1 fallback — do not duplicate them; the new logic is the excess-return subtraction + liquidity floor + the cap-threshold tweak.

### C11 — Conjunction (interaction-term) scoring for the accumulation complex
**(e) Target / change type:** `.claude/agents/signal-confluence-quant.md` (rubric), `.claude/commands/daily-analysis.md` + `weekly-analysis.md` (embedded rubric) — **agent + command.**

- **(a) Desk rationale.** The rubric is purely **additive**, so a name can accumulate a HIGH score from three signals that are really one view (dark-pool block + institutional-accumulation + conviction-matrix all express "someone is buying"). Additive scoring treats correlated evidence as independent and manufactures false conviction. The 05-23 desk note is explicit: *"the 'DP block + cum_flow alignment' pair is now the actual edge, not DP alone."* The real ≥0.80 WR is a **conjunction**.
- **(b) Academic.** The multiple-testing / non-independence problem (Bailey & López de Prado): summing correlated signals inflates apparent edge exactly as multiply-testing correlated strategies inflates the selected Sharpe. The fix — require *joint* confirmation — is the conditional/interaction analogue.
- **(c) Repo backtest. MEASURED.** Phase 3 tier inversion: **HIGH 60.0% < MED 62.5% (n=49)**. Phase 4: `dark_pool_block_stratified` softened +27.8→+21.8pp, now *"necessary but not sufficient"*; the audit observes WR climbs >0.80 only when DP-block **∧** cum_flow agree **∧** institutional-accum fires. Additive-narrative HIGH calls (MA, BL, MU-short) all lost.
- **(d) Acceptance criterion.** The `+3 dark_pool_accumulation` and `+2/+3 institutional-accumulation` lines pay **full weight only when `cum_premium_flow_30d` agrees in sign AND |flow| ≥ $50M**; otherwise **halved**. (Mirrors the existing sector-rotation conditional +1.) Acceptance = HIGH-tier realised WR > MED-tier on the next audit's out-of-sample cohort (monotonicity restored), measured from C1 envelopes.
- **Conflict note.** Distinct from the *two* existing cum_flow mechanisms — keep all three, document so `/goal` doesn't collapse them: (i) the 3-of-5 load-bearing gate counts tool *citations*; (ii) `flow_conflict` (−3) / `flow_conflict_lite` (−1) *subtract* when flow actively *opposes* the thesis. C11 instead *halves the positive accumulation points* when flow is merely **non-aligned** (MIXED / sub-$50M) — the exact case where flow_conflict_lite's −1 is too weak to stop a `+3 DP` / `+3 accum` additive pile from clearing the HIGH band.

### C12 — Liquidity floor on every screened candidate
**(e) Target / change type:** `.claude/commands/*.md` (Step 0 screens), `.claude/agents/signal-confluence-quant.md` — **command + agent.**

- **(a) Desk rationale.** A candidate the desk cannot fill at size is not a candidate. Junk names inflate the funnel, the backtest N, and the apparent breadth of "confluence."
- **(b) Academic.** Barbon & Buraschi — gamma/flow effects are *strongest in the least liquid names*, i.e. exactly where the signals are least reliable for a flow-follower and most likely to be un-exitable. ([Barbon & Buraschi, *Gamma Fragility*, SSRN 3725454](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3725454))
- **(c) Repo backtest. MEASURED.** `volume_spike` probe returned `GIF/BLCN/PEX/IGLD/UTHY/ESGE` — micro-ETFs with no institutional flow. No liquidity gate exists in any screen today.
- **(d) Acceptance criterion.** Every Phase-1 candidate must clear 20-day ADV ≥ $50M (or notional-equivalent) and price ≥ $5, via `screener_*` or yahoo `get_historical_stock_prices`. Junk names are excluded from the funnel *and* from win-rate computation. Acceptance = 0 sub-floor names in the next report's `calls[]`.
- **Conflict note.** Implement once; **C2** consumes the same floor. Cheapest high-value entry — could ship same PR as C2.

---

## P1 — clear edge, ship this/next cycle

### C4 — Opening-vs-closing flow discrimination (OI-confirmed directional flow)
**(e) Target / change type:** `.claude/agents/sweep-tracker.md`, `.claude/agents/signal-confluence-quant.md` (rubric gate) — **agent**; full version needs **new MCP tool N1.**

- **What already exists (verified this pass).** `sweep-tracker.md` line 31 already demotes index/mega-cap sweeps unless `historical_cumulative_premium_flow` 30d **direction** aligns with the sweep — but (i) only for the named mega-cap subset, (ii) only for *ranking* (sweep-persistence scores **0 points** since 05-23 P0.3). Direction-alignment is *not* the same as opening-confirmation.
- **(a) Desk rationale (the genuine new part).** A sweep/flow print that *closes* a position or hedges is noise; one that *opens* new institutional risk is signal. `cum_flow` *direction* (already used) does not distinguish opening from closing — a name can have aligned 30d net flow while today's print is a close. Isolating **buy-to-open** is the missing filter, and it should extend to the *scored* `bullish_flow`/`bearish_flow` classes and to non-mega-caps, not just mega-cap sweep ranking.
- **(b) Academic.** Pan & Poteshman (2006, RFS) — the predictive put-call ratio is built **only from buy-to-open volume**; low-P/C-minus-high-P/C earns **+40bps next day, +1%/week risk-adjusted**, from informed traders. The edge *disappears* without isolating opening volume. ([Pan & Poteshman, RFS 19:871](https://academic.oup.com/rfs/article-abstract/19/3/871/1646711))
- **(c) Repo backtest. PARTIAL.** `historical_trend` exposes per-day `net_flow` + `total_open_interest` (NVDA OI 15.06M→16.67M over the window); `oi_biggest_increases`/`oi_decrease_with_volume` give *aggregate* confirmation, so an aggregate OI-opening gate is buildable today. A *per-contract* opening filter is **UNVALIDATED** pending tool N1.
- **(d) Acceptance criterion.** The *scored* `bullish_flow`/`bearish_flow` rubric classes require **OI-confirmed opening** (same-name OI rises ≥ a configurable fraction of the day's contract volume, via `historical_oi_trend`/`oi_biggest_increases`), extended beyond the mega-cap subset. Acceptance = `bullish_flow`/`multi_day_sweep` realised WR closes ≥10pp of the claimed-vs-realised gap at next audit.
- **Conflict note.** Distinct from sweep-tracker's existing cum_flow-*direction* ranking filter (mega-cap, unscored) — C4 adds opening-*confirmation* to the *scored* flow classes. Also the route back to scoring for sweeps deprecated by P0.3 (OI-confirmed opening sweep co-flagged with accumulation).

### C7 — Post-Earnings Announcement Drift (PEAD) continuation play
**(e) Target / change type:** `.claude/agents/earnings-scout.md` (extend from pre-event-only to a post-event drift generator) or a new `earnings_drift` signal class; `scripts/finnhub_enrich.py` already has surprise streak; **uses yahoo `get_earning_dates` + `get_historical_stock_prices` + `historical_trend`** — **agent (+ script).**

- **(a) Desk rationale.** `earnings-scout` is *purely pre-event vol*. The fleet entirely misses the most-replicated anomaly in finance — drift *after* a surprise. A beat-and-raise with confirming post-print flow drifts for ~60 days; that is a swing long the book never takes.
- **(b) Academic.** Bernard & Thomas (1989/1990) — top-minus-bottom SUE decile ≈ **18% annualised over the 60 days post-announcement**; ~8–9% per quarter; the drift persists and does *not* reverse. ([Bernard & Thomas, PEAD; summary via Wikipedia / Semantic Scholar](https://en.wikipedia.org/wiki/Post%E2%80%93earnings-announcement_drift))
- **(c) Repo backtest. UNVALIDATED (data now available).** No PEAD logic exists. `finnhub_enrich` gives the beat/miss streak; yahoo (just wired) gives earnings dates + price history; `historical_trend` confirms post-print flow. The validation can now be built where it could not before.
- **(d) Acceptance criterion.** Build a post-earnings candidate generator (positive SUE/beat + positive guidance proxy + post-print bullish `net_flow` + price > pre-print close); backtest 10-day forward excess return over the covered names; ship a scored `swing_long` (`earnings_drift`) line **only if** the cohort's excess return is positive with hit-rate > 0.55 on n ≥ 10.
- **Conflict note.** Owns the **post**-event window; earnings-scout keeps the **pre**-event vol window. No overlap with the existing `earnings_vol` class (which is IV-crush/term-structure, not drift).

### C3 — Expectancy / fractional-Kelly sizing (payoff-aware, not hit-rate-only)
**(e) Target / change type:** `schemas/decision_envelope.schema.json` (add realised fields), `.claude/agents/signal-confluence-quant.md` + `risk-monitor.md` (sizing), `.claude/commands/calibration-audit.md` (compute expectancy) — **schema + agent.** Depends on envelopes accumulating (i.e. on runs resuming post-`193afec`, not on a C1 fix).

- **(a) Desk rationale.** The ladder sizes purely on hit-rate (0.70 / 0.50). A 55% strategy at 3:1 payoff dominates a 70% strategy at 1:1, but the rubric uses payoff only *anecdotally*: the quant's short-side floor (line 52) is justified by realised payoff asymmetry ("+0.37% avg short vs +9.81% bullish") — yet it never computes a *per-call* expectancy. Desks size on expected value. The repo records no per-call average win vs average loss, so systematic expectancy *cannot* currently be computed.
- **(b) Academic.** Kelly (1956) / fractional Kelly — optimal fraction `f* = W − (1−W)/R` requires both win-rate W *and* payoff ratio R; half-Kelly captures ≈75% of growth at ≈50% of the drawdown; **50–100 trades needed** for stable estimates (a binding caveat at ~30 days → use ≤½-Kelly with shrinkage and treat as advisory until N grows). ([Kelly criterion in practice — overview](https://www.avatrade.com/education/technical-analysis-indicators-strategies/the-kelly-criterion))
- **(c) Repo backtest. UNVALIDATED — and revealing why it matters.** The 05-23 raw_score→WR slope is now **nearly flat (58–64%)** and tiers are inverted: hit-rate alone has lost discriminating power. A payoff-aware metric may restore an actionable ordering. But the repo logs no realised P&L, so this must be built first.
- **(d) Acceptance criterion.** Envelope adds `realized_pnl_pct` + `payoff_ratio` per closed call (populated by `/calibration-audit` from C1 envelopes + `historical_trend`/yahoo prices). Sizing uses **capped half-Kelly**, floored at 0. Ship as a live sizer only once tier × expectancy is monotone on **n ≥ 30** closed calls; advisory-only below that.
- **Conflict note.** Replaces the win-rate-only ladder as the *sizing* input but keeps the tier system as the *gating* input. Needs the closed-loop record to accumulate first — i.e. envelopes from resumed runs (the C1 feature), advisory-only until n≥30.

---

## P2 — polish or needs validation first

### C8 — 52-week-high proximity gate for swing longs / distance for shorts
**(e) Target / change type:** `.claude/agents/signal-confluence-quant.md` (conditional gate); **uses yahoo `get_historical_stock_prices`** — **agent + MCP (yahoo).**

- **(a) Desk rationale.** The flow book has flow-momentum but no price-structure anchor. Names breaking to new highs continue; names far below struggle. Cheap confirming/disconfirming gate.
- **(b) Academic.** George & Hwang (2004, JF) — **nearness to the 52-week high dominates past-return momentum** in forecasting power, does not reverse long-run, and is profitable in 18 of 20 international markets (anchoring bias). ([George & Hwang, *The 52-Week High and Momentum Investing*, JF 2004](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.2004.00695.x))
- **(c) Repo backtest. UNVALIDATED (now feasible).** Yahoo just wired → %-from-52wk-high computable. No in-repo test yet.
- **(d) Acceptance criterion.** Backtest swing-long WR for candidates >95%-of-52wk-high vs <80%; ship a conditional **+1 (near-high long / far-from-high short)** only if the WR split ≥ 10pp on n ≥ 15.
- **Conflict note.** Additive +1; keep conditional so it does not re-inflate scores into the HIGH band (coordinate with C11's monotonicity goal).

### C5 — Single-name VRP *magnitude* scaler  *(re-tiered P1→P2 after staleness sweep — sign-based VRP sizing already exists)*
**(e) Target / change type:** `.claude/agents/vol-surface-scout.md`, `.claude/agents/earnings-scout.md`, `.claude/agents/signal-confluence-quant.md` (sizing); optional `scripts/vrp_percentile.py` — **agent (+ script).** Flags new MCP capability N3.

- **What already exists (verified this pass).** VRP is **not** merely a binary gate. `risk-monitor.md` line 16 already sizes by VRP *sign*: "long-vol candidates size up in negative-VRP weeks and size down in positive-VRP weeks; short-vol candidates do the inverse" — plus the −1-tier contradiction gate (line 41). `vol-surface-scout.md` line 12 sets BUY/SELL VOL bias by VRP sign. The 0DTE stack monetises VRP intraday. **This is why C5 fell to P2** — most of the value already ships.
- **(a) Desk rationale (the genuine new part).** What is thrown away is the **magnitude**: a single-name VRP at its 90th percentile and one barely positive both just read "positive → trim short-vol." The improvement is a **continuous percentile/tercile scaler** off *single-name* VRP (the current up/down is binary by sign and index-anchored), so conviction tracks *how* rich/cheap vol is, not just its sign.
- **(b) Academic.** Bollerslev-Tauchen-Zhou (2009, RFS) — VRP predicts market returns and **dominates P/E, the default spread, and CAY at the quarterly horizon (>15% R²)**. High VRP ⇒ premium-selling edge; low/negative VRP ⇒ premium-buying. ([BTZ 2009, RFS 22:4463](https://academic.oup.com/rfs/article-abstract/22/11/4463/1565787))
- **(c) Repo backtest. PARTIAL.** `historical_vrp` works per-ticker (SPY +0.039, FAIR) and accepts a `date` arg → a per-name VRP percentile series is buildable (one call per date today; see N3). VRP is already consumed *qualitatively by sign*, but cited only n=3 as a *scored-call* attribution; the **magnitude/percentile dimension is unused**. `earnings_vol` overconfidence (0.625 vs 0.85; DELL/MRVL blew through COMPLACENT skew) is partly a VRP-magnitude miss. Scaler itself **UNVALIDATED**.
- **(d) Acceptance criterion.** Build VRP percentile per name (≥30 obs, accumulating from C1 onward); premium-selling calls size up only when VRP ≥ 66th percentile, down/skip when ≤ 33rd. Backtest premium-selling realised WR by VRP tercile must be **monotone** before the scaler ships.
- **Conflict note.** Subsumes and generalises the 05-23 **P2.2** earnings_vol cap (COMPLACENT skew → 0.65) — VRP percentile is the continuous version of that discrete cap. Don't ship both; ship C5 and retire P2.2. Pairs with **C9** (VRP level + term-structure slope = complementary vol-regime scalers).

### C9 — IV term-structure SLOPE as a graded vol-regime scaler (replace the binary panic gate)
**(e) Target / change type:** `.claude/agents/vol-surface-scout.md`, `.claude/agents/earnings-scout.md`, `.claude/agents/risk-monitor.md` (panic gate) — **agent.**

- **(a) Desk rationale.** The panic gate is one binary threshold (`front_end_iv_ratio > 1.10`). The *slope* of the curve is itself a priced risk factor; backwardation depth should scale vol-buying / de-risk premium-selling continuously, not trip one switch.
- **(b) Academic.** Johnson (2017, JFQA 52:2461) — the VIX term-structure **SLOPE (2nd principal component) predicts variance-swap, VIX-future, and straddle returns across maturities**; it reflects the *price of variance risk*, incremental to other VRP proxies. ([Johnson, *Risk Premia and the VIX Term Structure*, JFQA 2017](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2548050))
- **(c) Repo backtest. UNVALIDATED.** `options_structure_iv_term_structure` is SUPPORTIVE (borderline); `front_end_iv_ratio` n=2. Slope-as-scaler untested.
- **(d) Acceptance criterion.** Compute per-name term-structure slope; backtest premium-selling-vs-buying WR by slope tercile; replace the binary gate with a graded size scalar only if the tercile ordering is monotone.
- **Conflict note.** Pairs with **C5** (both are vol-regime scalers — VRP level + term slope are complementary, like Johnson's "level vs slope"). Implement together or sequence C5 → C9.

### C6 — Lottery / expensive-skew short-vol fade screen
**(e) Target / change type:** `.claude/agents/vol-surface-scout.md` or `.claude/agents/contrarian-scanner.md` (new signal), rubric — **agent.**

- **(a) Desk rationale.** Retail demand for lottery-like OTM calls makes them systematically overpriced; harvesting that skew (or fading the crowded call-buying name) is a durable premium source the fleet does not systematically screen for.
- **(b) Academic.** Boyer & Vorkink (2014, JF) "Stock Options as Lotteries" — total skewness is **strongly negatively related to option returns; low-minus-high skew spread 10–50% per week**, compensating intermediaries for unhedgeable lottery demand. Bali-Cakici-Whitelaw MAX effect corroborates for the underlying. ([Boyer & Vorkink, JF 2014](https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.12152))
- **(c) Repo backtest. UNVALIDATED — and caution flag.** `vol-surface-scout` *already reads* `options_structure_term_skew` (line 9: "skew at 1y low = tail not priced; elevated = hedging demand") — but as tail/calendar context, **not** as a systematic Boyer-Vorkink short-vol fade, and with no lottery composite. `historical_pc_ratio_zscore` is **NEGATIVE (−22pp)** standalone — naive contrarian fades have *lost* in this regime. A skew/IV-conditioned fade is a different animal but must clear a higher bar.
- **(d) Acceptance criterion.** Define `lottery_score` = high IV-rank ∧ high positive call skew ∧ crowded call-buying z-score; backtest top-decile forward 5–10d returns; ship a **−2 fade** line only if top-decile underperforms by ≥ X% with p < 0.10 — *and* only in a non-UPTREND regime (given the contrarian-fade failure).
- **Conflict note.** High overlap with `contrarian-scanner` (already aborts in negative VRP) and the existing `−2 overcrowded-long` line — must be routed as one signal class, not stacked (see C13).

### C10 — Opportunistic-vs-routine insider weighting in `fundamentals-gate`
**(e) Target / change type:** `scripts/finnhub_enrich.py` (classification), `.claude/agents/fundamentals-gate.md` — **script + agent.**

- **(a) Desk rationale.** `fundamentals-gate` uses raw MSPR (average insider sentiment). Routine (calendar-scheduled) insider trades carry ~zero information; only opportunistic trades predict. Equal weighting dilutes the signal.
- **(b) Academic.** Cohen, Malloy & Pomorski (2012, JF) "Decoding Inside Information" — a portfolio of **opportunistic insiders earns 82bps/month abnormal; routine ≈ 0**; opportunistic trades predict future news and earnings-announcement returns. ([CMP 2012, JF](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.2012.01740.x))
- **(c) Repo backtest. UNVALIDATED.** Insider MSPR cited n<5 (INSUFFICIENT_N). Routine/opportunistic split needs per-insider trade history (Finnhub insider-transactions endpoint).
- **(d) Acceptance criterion.** Classify insiders as routine (trades in the same calendar month across ≥3 prior years) vs opportunistic; `fundamentals-gate` CONFIRM/CAUTION uses **opportunistic-only** MSPR; measure verdict accuracy vs outcome at next audit.
- **Conflict note.** Pure refinement of an existing input; no new scored line.

### C13 — Mutually-exclusive signal-class routing for the three MEDIUM overlaps
**(e) Target / change type:** `.claude/agents/signal-confluence-quant.md`, `vol-surface-scout.md`, `earnings-scout.md`, `sweep-tracker.md` — **agent.**

- **(a) Desk rationale.** Double-counting one idea (a calendar read by both multileg-strategist and vol-surface-scout; a KINKED earnings structure by both earnings-scout and vol-surface) inflates conviction on a single thesis. Clean books attribute one idea to one owner.
- **(b) Academic.** The non-independence principle again (Bailey & López de Prado) — correlated signals are not additive evidence.
- **(c) Repo backtest. MEASURED (qualitative).** The agent-fleet conflict matrix flags exactly three MEDIUM, PARTIAL-dedup pairs: **(5) multileg × vol-surface**, **(7) earnings-scout × vol-surface**, **(3) contrarian × sweep-tracker**. All other 8 pairs are CLEAN by design (phase boundaries / conditional gates).
- **(d) Acceptance criterion.** `signal-confluence-quant` routes each idea to exactly one `dominant_signal_class` with documented precedence: multileg-flow > vol-structure; earnings-scout owns `earnings_vol` KINKED; contrarian acknowledges sweep contradiction in prose with **no double-deduction**. Acceptance = 0 double-counted `score_components` across a 5-report audit (verifiable now that C1 makes components machine-readable).
- **Conflict note.** This is the *definitive* fix for the overlaps; **C6** must register through this router so it does not stack with the existing contrarian line.

### C14 — Yahoo independent price/earnings/recommendations cross-check (enabler + robustness)
**(e) Target / change type:** new `scripts/yahoo_xcheck.py`; consumed by `earnings-scout.md`, `signal-confluence-quant.md` — **script + agent + MCP (yahoo).**

- **(a) Desk rationale.** The newly-wired yahoo MCP is an *independent* source for price, earnings dates, and analyst recommendations. Cross-checking UW-derived levels reduces single-vendor risk and fills the **03-27 → 04-27 UW data hole**. It is also the data substrate for C7 (PEAD) and C8 (52wk).
- **(b) Academic.** Robustness/data-integrity (no single anomaly); its value is as the enabler for the well-cited C7 and C8.
- **(c) Repo backtest. MEASURED (connectivity).** Yahoo connected, 10 tools verified live this session. UW window has a 1-month gap that yahoo can bridge.
- **(d) Acceptance criterion.** `get_earning_dates` cross-checks `finnhub` `next_earnings_date` (flag discrepancies > 1 trading day); `get_historical_stock_prices` supplies 52wk-high and post-earnings drift inputs. Acceptance = both consumed by C7/C8 validations without error.
- **Conflict note.** Pure additive data source; route through existing agents, do not spawn a new agent.

### C1 — Verify (smoke-test) the just-shipped decision-envelope emission  *(downgraded from P0 after git review)*
**(e) Target / change type:** verification of `.claude/commands/daily-analysis.md` + `weekly-analysis.md` Step 9 (present since commit `193afec`); **no code change unless the smoke test fails** — **verification (+ fix only if broken).**

- **(a) Desk rationale.** The machine-readable calibration loop is the right design and is already wired — but it shipped 2026-05-23 and **has never executed** (no analysis has run since). A feature that has never run is unverified: Step 9 could have a path bug, the agents may not populate every schema field at runtime, and `/calibration-audit` Phase 1's envelope-consumption branch is untested. Confirm it works once, before the desk relies on it.
- **(b) Academic.** Same Bailey & López de Prado rationale for *why* the loop matters — the Deflated Sharpe Ratio and PBO need a clean, machine-readable trial log to correct for selection bias and multiple testing. But that argues for *exercising* the existing feature, not building one. ([SSRN 2460551](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2460551), [SSRN 2326253](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2326253))
- **(c) Repo backtest. CORRECTED (this premise was wrong in the first draft).** Git: `git log -S 'decision.json'` shows emission + `schemas/decision_envelope.schema.json` + `scripts/validate_decision.py` **all first appeared in `193afec` (2026-05-23)**; the latest daily report `2026-05-22.md` **predates it**; 05-23 Sat / 05-24 Sun / 05-25 today → **no `/daily-analysis` has run since**. The "0 envelopes on disk" is *expected for legacy reports*, not missing code. The first-draft "ASPIRATIONAL / NOT IMPLEMENTED" label was an over-reach from file-count inference; the schema-mapping Explore agent did not check git.
- **(d) Acceptance criterion.** The next `/daily-analysis` writes a schema-valid `analyses/<date>.decision.json` (`validate_decision.py` exit 0) with `macro_snapshot_signals` / `next_session_gex` / `next_session_0dte_setup` / per-call `win_rate*` / `gate_verdicts` / `fundamentals_verdict` **actually populated**; `/calibration-audit` Phase 1 ingests that envelope (not prose) for that date. Only a failure here promotes C1 back to a fix. **Backfilling pre-05-23 reports is explicitly OUT OF SCOPE** — they predate the current rubric and regime, so re-deriving envelopes for them would mix incompatible scoring.
- **Conflict note.** None. Envelopes accrue automatically as runs resume; this is a one-time check, not recurring work. C3's expectancy record and the machine-readable Brier/monotonicity checks behind C2/C11/C13 *consume* these envelopes as they accumulate — but none of them require a C1 "fix," only that runs happen.

---

# NEW MCP CAPABILITIES the parquets support but no tool exposes

Proposed additions to the `unusual-whales-mcp` source + the `unusual-whales-pp-cli-mcp` binary. Backing parquets (`~/Documents/Stocks`): **All Options, Dark pool, Hot Option Chains, OI changes, Stock Screener.**

| ID | Proposed tool | What it computes | Parquet support | Serves | Why no equivalent today |
|---|---|---|---|---|---|
| **N1** | `options_flow_opening_filter` | Per-contract flow where day's volume **exceeds prior-day contract OI** (= net new positioning), split buy-to-open vs sell-to-open by trade-side aggressor | **All Options** (every trade) + **OI changes** (prior-day OI) | **C4** (Pan-Poteshman opening-flow edge) | `oi_biggest_increases`/`oi_decrease_with_volume` are *aggregate* per-name; no per-contract opening/closing split exists |
| **N2** | `historical_signal_backtest --excess --min-n --liquidity-floor --history-days` | Same signal backtest but **SPY-excess** returns, configurable lookback depth (not ~2 days), minimum-N, and a liquidity floor | **All Options** + **Stock Screener** (ADV) + index series | **C2** (kills beta-as-edge win-rates) | Current tool is unconditional, ~2-day-deep, no liquidity floor, no excess-return mode |
| **N3** | `historical_vrp_series` | Vectorised per-name VRP **time series** + rolling percentile in one call (current tool returns one snapshot per call) | **All Options** (per-ticker IV30) + price history (RV) | **C5, C9** (VRP/term-slope terciles need a series) | `historical_vrp` is single-date; building a percentile needs N round-trips |
| **N4** | `screener_skew_lottery` | Cross-sectional rank of expensive-lottery names: high IV-rank ∧ high positive OTM-call skew ∧ crowded call-buy z-score | **Hot Option Chains** + **All Options** + **Stock Screener** | **C6** (Boyer-Vorkink fade) | `options_flow_iv_outliers` + `screener_iv_rank` exist separately; no composite lottery rank |

> **Edge test before building any of these:** N1 and N2 should be built only if the *aggregate/interim* versions (C4 via `historical_oi_trend`; C2 via the excess-WR script over MCP outputs) show enough lift to justify the source change. Do not build a parquet-direct tool where the MCP equivalent already clears the acceptance bar (per session mandate).

---

# Conflict / overlap notes for `/goal` (so it does not duplicate existing logic)

**Against the already-applied 05-23 patches (commit `a1d0507`) — do NOT re-implement:**
- 3-of-5 load-bearing-tool gate (incl. `insights_signal_confluence`) — **live**; C11 *complements* it (agreement vs citation-count), does not replace it.
- `hot_chains_sweep_persistence` deprecated to 0 points — **live**; C4 is the *path back* (OI-confirmed opening sweeps), not a re-add of the old line.
- `insights_conviction_matrix` LEAP-only — **live**; none of these criteria touch it.
- `insights_signal_confluence` +2 line, sector-rotation conditional +1, flow_conflict / flow_conflict_lite mutual-exclusivity — **live**.

**Against the 05-23 open P2 backlog — fold, don't duplicate:**
- 05-23 **P2.2** (earnings_vol cap on COMPLACENT skew) is **subsumed by C5** (VRP percentile is the continuous form). Ship C5, retire P2.2.
- 05-23 **P2.1** (formalise binary-earnings gate) and **P2.4** (schedule weekly auto-audit) are orthogonal process items — leave as-is; C1 makes P2.4 far more valuable (envelopes give the auto-audit clean input).
- 05-23 **P2.5** (investigate `dark_pool_block_stratified` decay) is *answered* by C11 — the decay is the additive-vs-conjunction problem, not tool drift.

**Within this register — sequencing & shared components:**
- **C1 is now a one-time verification, not a blocker.** The envelope feature shipped 2026-05-23 (`193afec`) and will populate automatically as runs resume. The machine-readable Brier/monotonicity checks behind C2/C11/C13 and the expectancy record behind C3 *consume* those envelopes as they accrue — they do not require any C1 fix, only that `/daily-analysis` runs.
- **C2 and C12** share one liquidity floor — ship together.
- **C5 and C9** are complementary vol-regime scalers (VRP level + term slope) — ship together or C5→C9.
- **C6 must route through C13** (else it stacks with the existing contrarian line).
- **C7, C8, C14** all depend on the yahoo MCP wired this session.

**Agent-fleet overlaps already CLEAN (no action — for `/goal`'s awareness):** gamma-flip-tracker (0DTE, 0-pt advisory) vs dealer-positioning-strategist (swing, scored); opex-pin vs gamma-flip (OPEX-conditional); sweep-tracker vs accumulation-hunter (sweep scores 0 standalone); sector-rotation vs single-name (conditional +1, 3-gate); fundamentals-gate vs debate (sequential phases); risk-monitor mechanical gates vs debate qualitative.

---

# Appendix — citations (verified via WebSearch, 2026-05-25)

1. **Variance risk premium predicts returns** — Bollerslev, Tauchen & Zhou (2009), *Expected Stock Returns and Variance Risk Premia*, **Review of Financial Studies 22(11):4463–4492**. VRP explains >15% of quarterly excess-return variation; dominates P/E, default spread, CAY. https://academic.oup.com/rfs/article-abstract/22/11/4463/1565787
2. **Backtest overfitting / selection bias** — Bailey & López de Prado, *The Deflated Sharpe Ratio* (SSRN 2460551) and *The Probability of Backtest Overfitting* (SSRN 2326253). Corrects Sharpe for multiple testing, non-normality, short samples; PBO via CSCV; minimum backtest length. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2460551 · https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2326253
3. **Option order-flow informativeness (opening volume)** — Pan & Poteshman (2006), *The Information in Option Volume for Future Stock Prices*, **RFS 19(3):871**. Buy-to-open P/C ratio: low-minus-high earns +40bps next day, +1%/week risk-adjusted; informed-trader driven. https://academic.oup.com/rfs/article-abstract/19/3/871/1646711
4. **Dealer gamma hedging / intraday vol** — Barbon & Buraschi (2021), *Gamma Fragility* (SSRN 3725454). Positive dealer gamma imbalance ⇒ intraday mean-reversion (vol suppression); negative ⇒ momentum; effect strongest in illiquid names. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3725454
5. **Lottery / skew overpricing** — Boyer & Vorkink (2014), *Stock Options as Lotteries*, **Journal of Finance 69(4)**. Total skewness strongly negatively related to option returns; low-minus-high skew 10–50%/week. https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.12152
6. **Post-earnings announcement drift** — Bernard & Thomas (1989, 1990). Top-minus-bottom SUE decile ≈18% annualised over 60d; ~8–9%/quarter; persists, does not reverse. https://en.wikipedia.org/wiki/Post%E2%80%93earnings-announcement_drift
7. **52-week-high momentum** — George & Hwang (2004), *The 52-Week High and Momentum Investing*, **JF 59(5):2145–2176**. Nearness-to-52wk-high dominates past-return momentum; no long-run reversal; 18/20 international markets. https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.2004.00695.x
8. **VIX term-structure slope as risk premium** — Johnson (2017), *Risk Premia and the VIX Term Structure*, **JFQA 52(6):2461–2490**. SLOPE (2nd PC) predicts variance-swap / VIX-future / straddle returns across maturities. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2548050
9. **Opportunistic vs routine insiders** — Cohen, Malloy & Pomorski (2012), *Decoding Inside Information*, **JF 67(3):1009–1043**. Opportunistic insiders 82bps/month abnormal; routine ≈0; opportunistic predict news + earnings returns. https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.2012.01740.x
10. **Position sizing on edge AND payoff** — Kelly (1956), fractional Kelly. `f* = W − (1−W)/R`; half-Kelly ≈75% growth at ≈50% drawdown; 50–100 trades for stable estimates. https://www.avatrade.com/education/technical-analysis-indicators-strategies/the-kelly-criterion

**Repo evidence sources:** `analyses/audit/2026-05-23/{SUMMARY,phase_3_calibration,phase_4_tools,phase_7_recommendations}.md`; live `uw-pp` probes (this session); schema↔script gap analysis; agent-fleet conflict matrix.

---

# ADDENDUM — 2026-05-27 `fz` (Finviz CLI) edge criteria (C15–C18)

> **Source audit:** `analyses/audit/2026-05-27-fz-edge/` (capability map `01`, edge analysis `02`, implementation plan `03`, evidence `04`). The `fz` CLI (`finviz-pp-cli`) closes the non-flow blind spot `AUDIT.md §4` flags as "genuinely missing" — short interest, days-to-cover, float, institutional/analyst positioning. **Phase A (advisory, 0 points) shipped 2026-05-27**: `scripts/fz_enrich.py`, the fundamentals-gate `fz_context` block, the Step-0 breadth cross-check + squeeze/RS funnel lanes, the accumulation insider-cluster co-flag, and the bull/bear analyst context. C15–C18 below are the **scored-gate promotions**, registered here and held advisory until `/calibration-audit` Phase 4 clears each threshold — exactly the discipline that kept C6/C7 NO-GO and gated C11.
>
> **Honest scope:** `fz` adds **no** options flow / greeks / dark pool / IV term-structure / GEX/DEX / OI — it cannot replace any `uw` tool. Finviz short interest is the exchange **semi-monthly settlement figure (~2-week lag)** — squeeze *context*, not a live borrow signal — and `fz` exposes **no borrow fee / HTB** field. So C15 closes the SI/DTC/float leg of the §4 gap, not the borrow leg.

| ID | Criterion | Owner agent(s) | Gate mechanic (when LIVE) | Promotion threshold (Phase 4) |
|---|---|---|---|---|
| **C15** | Short-interest squeeze gate | risk-monitor (+ fundamentals-gate context) | SHORT thesis into `short_float ≥ 20% ∧ days_to_cover ≥ 5` → **−1 tier** (squeeze trap). LONG momentum into same → squeeze-tailwind note (no size change). | After ≥10 reports carry `fz_context`, calibration shows SHORT calls into high-SI names underperform the short-class realised baseline. |
| **C16** | Float-normalized conviction | signal-confluence-quant (+ accumulation-hunter) | Dark-pool block / OI build pays full accumulation points only if ≥ X% of `float_shares` (X by backtest); below → halved. Extends the C11 conjunction. | Calibration shows the float-normalized block threshold separates winners from churn with effect size ≥ the C11 conjunction. |
| **C17** | Analyst-divergence axis | fundamentals-gate | `Recom`-vs-flow disagreement beyond a band → **CAUTION** contribution (downside-only, never CONFIRM-only). | Calibration shows flow-vs-analyst divergence has sign on outcomes. |
| **C18** | Insider-cluster conjunction | accumulation-hunter → signal-confluence-quant | `insider_cluster_present` ∧ dark-pool block ∧ cum-flow → **+1** to the accumulation line (conjunction-gated like C11). | Calibration shows the 3-way conjunction beats the 2-way (C11) baseline. |

### C15 — Short-interest squeeze gate  *(**CLOSED — RETIRED 2026-08-15**; was RE-SCOPED 2026-08-01)*

> **DECISION 2026-08-15 (audit P1 #4): C15 is RETIRED under option (ii) of the 2026-08-01 re-scope.** `squeeze_pressure`, `short_float_pct` and `days_to_cover` remain **permanent advisory context** in `fz_context` and the debate/fundamentals prose; they earn **0 rubric points, permanently**, and no future audit should re-run a C15 threshold test. Three findings, in ascending order of decisiveness:
> 1. **The absolute trigger is unreachable, but NOT for the reason the 2026-08-01 entry recorded.** That entry attributed it to `short_float` — wrong. Post-fix, `short_float` populates on **147 rows with real variance** (min 0.27%, median 3.14%, p90 14.93%, **max 30.22%**) and **7 rows clear ≥20%** (ASTS 20.21; NBIS 25.21–30.22 ×6). The binding leg is **`days_to_cover ≥ 5`: only 2 of 147 rows clear it, and none of them are the high-short-float names** — NBIS carries 30% short float at DTC ≈ 2.8–3.1 because the same C12 liquidity floor (20-day dollar-ADV ≥ $50M) that admits it also guarantees the volume to cover fast. **High short interest and high days-to-cover are structurally anti-correlated inside this universe.** The conjunction has 0 hits and always will.
> 2. **Option (i) — the top-decile re-expression — is starved on the arm that matters.** Of 23 SHORT-thesis rows carrying `fz_context`, **0 fall in the top short-float decile** (all 7 high-SI rows are LONG theses); the non-top-decile SHORT arm has 20 decided at WR 0.45. Against a bar of n≥30 **per arm**, one arm is empty.
> 3. **Decisive: the gate is now a no-op by construction.** C15's action is "**SHORT thesis into high SI → −1 tier**". Since the **2026-08-01 P0**, every directional short is routed to `watch_only` and **is never sized** — so there is no size for a squeeze gate to reduce. A tier downgrade applied to a position that cannot be taken changes nothing. Whatever C15 might have measured, it can no longer *act*.
> **If the universe changes** (a genuine high-DTC regime, or short-routing is lifted by a future audit), re-register it **fresh** with the then-observed distribution as the pre-registration basis — do not reopen this entry.

### C15 — original entry (historical; superseded by the retirement above)  *(RE-SCOPED 2026-08-01 — untestable by construction on this universe)*
> **STATUS 2026-08-01 (audit P2 #8): the acceptance bar as written can never be met, for a reason that is not sample size.** Of the 18 SHORT-thesis rows carrying `fz_context` across the whole corpus, **zero** clear `short_float ≥ 20% ∧ days_to_cover ≥ 5` — for a second consecutive audit. The realised squeeze-pressure distribution is **LOW 91 / unknown 44 / MODERATE 6, HIGH 0**. The fleet's candidate funnel is a mega-cap options-flow universe (C12 floors at price ≥ $5 **and** 20-day dollar-ADV ≥ $50M), and names with 20%+ short float essentially do not survive that floor. This is a **definitional mismatch between the criterion and the universe**, not an under-powered test — waiting for more reports cannot fix it.
> **Re-scoped bar (replaces the threshold column for C15):** either (i) re-express the gate on the universe's *own* distribution — e.g. SHORT theses into the **top decile of `short_float` among funnel-eligible names**, which is a reachable condition — and hold the same acceptance discipline (cross-regime ∧ n≥30 per arm ∧ BH-surviving); or (ii) **retire C15** and keep `squeeze_pressure` as permanent advisory context. Until one is chosen, C15 stays advisory at **0 points** and no further audit should re-run the unreachable absolute-threshold test. NB the underlying data is now *better* than it was: the 2026-08-01 `fz_enrich` row-match fix restored `short_float` / `days_to_cover` population, so option (i) is measurable from the next cycle.

- **(a) Desk rationale.** A bullish sweep into a 25%-short, 8-day-to-cover name is squeeze fuel; the identical sweep into a clean float is a clean directional bet. A *short* thesis into high SI + low float is a squeeze trap, not a clean fade. The fleet sizes both identically today — it has no short-interest field at all.
- **(b) Academic / desk.** Days-to-cover and % float short are the canonical squeeze-pressure inputs on any equity desk; short-squeeze dynamics (forced buy-in of crowded shorts) are well documented. **Honest:** borrow fee / HTB still absent — this is SI/DTC/float only.
- **(c) Repo backtest. UNVALIDATED (advisory now).** `fz_context` ships 2026-05-27; no outcome data yet. Verified live: ACHC `Short Float 27.72%`, `Short Ratio 7.68` (`04 §2`).
- **(d) Acceptance.** See threshold column. Until cleared, `fz_context` is logged but `tier_adjustment` stays Finnhub-driven.
- **(e) Targets.** `risk-monitor.md` (new squeeze axis), `fundamentals-gate.md` (context — shipped). **Conflict note:** complements the existing fundamentals VETO/CAUTION stack; squeeze is a *direction-conditional* tier move, not a fundamentals contradiction.

### C16 — Float-normalized conviction  *(UNBLOCKED 2026-08-01 — the blocker was a parse bug, not a missing field)*
> **STATUS 2026-08-01 (audit item 5): testable from the next cycle.** C16 was reported "untestable" for **four consecutive audits**, and each of the last two proposed adding a schema field to fix it. **Both diagnoses were wrong.** The field has existed since 2026-06-20 (`dp_block_to_float_ratio`, register C43), the agent contract has specified it since 2026-07-04, the validator has warned on its absence since 2026-07-25, and post-2026-07-27 envelopes emit it on **3/3** eligible rows. The actual blocker was one line in `scripts/fz_enrich.py`: `screen_fallback_fields` matched screener rows by exact `Ticker` equality, while upstream `fz screen` returns a **doubled first letter** (`MSFT` → `MMSFT`, the same synthetic-ticker artifact already logged against the quote grid). Every row was rejected, so `float_shares` came back `None`, so the ratio serialized as `null` on **0 of 9** populated rows — a null that looked exactly like the contract-mandated "fz unavailable" null.
> **Fixed 2026-08-01** (`_screen_row_matches` tolerates the doubled-letter form, plus a sole-row fallback for a ticker-scoped query; 6 regression tests). Verified live: MSFT float 7.31B, AVGO float 4.67B; `short_float_pct` / `days_to_cover` now populate too. `validate_decision.py` gained a **value-level** warning (null ratio *despite* `fz_context.available == true`) so a silent regression of the value, not just the key, is caught at emission. **C16's acceptance bar is unchanged** — threshold X still set by backtest, still shipped as a halving multiplier on the accumulation points, never a new additive line. It simply now has data to be decided on.
> **Transferable lesson:** an instrumentation field that is present-and-null is indistinguishable from a field that is absent-by-design unless the *emitter* is checked end-to-end. Two audits recommended a schema change for a bug that was never in the schema.

- **(a) Desk rationale.** Order size is only meaningful as a fraction of available float/ADV. A $100k block into AAPL's 14.67B float is noise; the same block into a 5M-float micro-cap is conviction. The block-tier filter is a *dollar* filter, not a *float-relative* one.
- **(b) Academic.** Float/ADV normalization is standard market-maker practice; mirrors the C12 liquidity-floor and the C11 conjunction logic.
- **(c) Repo backtest. UNVALIDATED.** `float_shares` parsed by `fz_enrich.derive`; no threshold backtested.
- **(d) Acceptance.** Threshold X set by backtest; ship as a halving multiplier on the accumulation points, never a new additive line (coordinate with C11 monotonicity).
- **(e) Targets.** `signal-confluence-quant.md`, `accumulation-hunter.md`. **Conflict note:** extends C11; do not double-count — C16 modulates the *same* accumulation points C11 gates on cum-flow.

### C17 — Analyst-divergence axis
- **(a) Desk rationale.** The bull/bear debate argues flow-vs-flow with no explicit consensus rating or upside-to-target to anchor on. A bullish-flow name already +2% past a `Recom 4.1` consensus target is a different risk than one −18% below a strong-buy target.
- **(b) Academic / desk.** Analyst-vs-flow disagreement is a recognised EV setup (the fleet already has `uw insights analyst-vs-flow` as a *label*); `fz` adds the raw `Recom` + `Target Price` numbers and a cross-source check (Finviz-vs-Finnhub divergence is itself a flag).
- **(c) Repo backtest. UNVALIDATED.** `recom` / `upside_to_target_pct` ship in `fz_context` + the debate prose; no outcome attribution yet.
- **(d) Acceptance.** Downside-only CAUTION contribution once divergence is shown to have sign on outcomes.
  - **SUPERSEDED 2026-07-04 (audit P2 #5 — bar pre-committed so goalposts can't move):** the acceptance bar is now **n ≥ 25 divergent decided ∧ both thesis directions represented ∧ BH-surviving FDR 0.10** (this line, not the looser sentence above, is binding; mirrored in `fundamentals-gate.md`). First scored read was positive — divergent rows 0.615 (n=13) vs short-book 0.422 — but short-only and thin. **Data caveat:** fz 1.0.0's quote-grid regression makes `recom`/`target_price` upstream-unrecoverable (no screener view carries them; `fz_enrich.py` reports them in `upstream_gaps`), so the divergence cell accrues no NEW rows until the upstream parser is fixed.
- **(e) Targets.** `fundamentals-gate.md`, `bull-/bear-researcher.md` (prose context — shipped). **Conflict note:** never a CONFIRM-only upgrade; routes through the existing CAUTION machinery, no new positive points.

### C18 — Insider-cluster conjunction  *(**CLOSED — RETIRED 2026-08-15**)*

> **DECISION 2026-08-15 (audit P1 #4): C18 is RETIRED as REFUTED-BY-ZERO-VARIANCE.** `insider_cluster_flag` has now been observed **20 times across the corpus and is `False` on every single one** — sixth consecutive audit carrying the same finding. **A predictor with zero variance cannot gate a conjunction at any sample size**: there is no arm to compare against, so the acceptance bar ("the 3-way conjunction beats the 2-way C11 baseline") is not merely unmet, it is *unmeasurable in principle* on this data. Post-fix the picture is unchanged (key present on 94 post-P0 calls, populated on 7, all `False`).
> **This is a different failure from C16.** C16 is *starved* — its field (`dp_block_to_float_ratio`) is populated on only 7 of 210 calls because the emitter still writes null, so more/better emission would decide it. **C18 is emitting fine and the answer is always the same value.** Either `fz insider-clusters` genuinely never fires on a mega-cap options-flow funnel (plausible: clustered opportunistic insider buying is a small/mid-cap phenomenon, and Cohen–Malloy–Pomorski's effect is measured on a far broader universe), or the co-flag's plumbing silently degrades to `False` instead of `null`. **Both readings terminate the criterion**; only the second is worth one session of diagnosis, and if the plumbing turns out to be broken the fix ships as a bug, not as a re-opened promotion.
> `insider_cluster_present` stays as **advisory prose context** in `accumulation-hunter` at 0 points. The `insider_cluster_flag` envelope field is **retained** (schema-additive, harmless, and it is how a future non-zero observation would surface) but no longer gates anything and no audit should re-test it. **C16 and C17 remain OPEN** — C16 starved-but-decidable, C17 advisory with its 2026-07-04 bar (n≥25 divergent decided ∧ both directions ∧ BH) unmet at n=14 / WR 0.571.

### C18 — original entry (historical; superseded by the retirement above)
- **(a) Desk rationale.** Finnhub MSPR collapses a month into one blended ratio; it cannot tell you *three distinct officers* bought this week. Cluster conviction is exactly what accumulation-hunter hunts and it has no insider corroborant today.
- **(b) Academic.** Cohen, Malloy & Pomorski (2012, JF) "Decoding Inside Information" — opportunistic, clustered insider buying earns ~82bps/month abnormal; routine ≈ 0. Consistent with the C11 conjunction philosophy (a signal pays full only in conjunction).
- **(c) Repo backtest. UNVALIDATED.** `fz insider-clusters` verified live (WHF, 2 owners, 3 txns — `04 §3`); co-flag ships advisory 2026-05-27.
- **(d) Acceptance.** +1 to the accumulation line only when the 3-way conjunction beats the 2-way C11 baseline out-of-sample.
- **(e) Targets.** `accumulation-hunter.md` (co-flag — shipped), `signal-confluence-quant.md` (scored line — gated). **Conflict note:** net-new vs Finnhub MSPR (distinct-buyer count, not a blended ratio); conjunction-gated like C11, never a standalone additive point.

**Discipline reminder (the single most important constraint):** until a C15–C18 item clears its Phase-4 threshold, its `fz` field stays advisory and earns **0 points**. This prevents `fz` from inflating conviction on a narrative — the exact failure mode the calibration loop exists to prevent.

**STATUS BOARD (updated 2026-08-15 audit P1 #4).** Fourteen months of accrual, no promotions:

| | status | why |
|---|---|---|
| **C15** | **RETIRED 2026-08-15** | absolute trigger unreachable (`days_to_cover ≥ 5` structurally excluded by the C12 ADV floor: 2/147 rows); top-decile re-expression starved on the SHORT arm (0 decided); and **the gate is a no-op since shorts stopped being sized** (2026-08-01 P0). |
| **C16** | **OPEN — starved** | field exists and is correct; emitter populates `dp_block_to_float_ratio` on **7 of 210** calls. Decidable if emission is fixed. |
| **C17** | **OPEN — advisory** | n=14 divergent decided, WR 0.571 vs book 0.414. Bar (n≥25 ∧ both directions ∧ BH) unmet. Upstream `fz` quote-grid regression still blocks new `recom` rows. |
| **C18** | **RETIRED 2026-08-15** | `insider_cluster_flag` observed 20×, **`False` every time** — zero variance cannot gate a conjunction at any n. |

**Transferable lesson (2026-08-15).** "Awaiting more data" and "cannot fire" look identical from inside a criterion register, and the difference is worth one query per audit. A criterion whose *trigger* has never fired is not pending — it is either mis-specified for the universe (C15) or answered (C18). Six audits carried these two as open items. **When a criterion goes three cycles without its trigger firing once, the next audit's job is to test the trigger's reachability, not to re-run the outcome test.**

**Repo evidence sources (addendum):** `analyses/audit/2026-05-27-fz-edge/{01-fz-capability-map,02-edge-analysis,03-implementation-plan,04-evidence-appendix}.md`; live `fz` probes 2026-05-27.

---

## 2026-06-20 audit pre-registrations (C40–C43)

> Registered by the 2026-06-20 calibration audit (`analyses/audit/2026-06-20/`). **The rubric is FROZEN at version `2026-06-12`** — these are pre-registered *hypotheses*, not edits. Each is decided by a FUTURE audit on data that does not yet exist; the **dataset that produced them is 100% single-regime (TRANSITIONAL/UPTREND)**, so every acceptance bar requires cross-regime evidence. Until a bar clears, the named weight/cut stays frozen exactly as-is.

| ID | Criterion | Owner agent(s) | Hypothesis / change direction | Acceptance bar (Phase 5) |
|---|---|---|---|---|
| **C40** | `+2 multileg_directional` weight too high | signal-confluence-quant | Reduce toward `+1` or gate on a confirmation leg — term-structure-inferred direction is not predicting realised direction. | cross-regime ∧ n≥30 per arm ∧ BH-surviving at FDR 0.10. Decided at the first audit after 30 resolved `multileg_directional` calls accrue, ≥1 out-of-UPTREND. |
| **C41** | `≥9` HIGH tier cut re-confirm | signal-confluence-quant | The cut must demonstrate HIGH-band WR ≥ MED-band WR before it carries any ranking claim. | n≥30 resolved raw-≥9 **post-freeze** calls, cross-regime, HIGH≥MED monotone. Today: **0** post-freeze raw-≥9 resolved → KEEP freeze + P0.6 half-cap. |
| **C42** | vol-component weights ungradeable | signal-confluence-quant | Hold — cannot grade the `+1/+2` vol weights while the win-rate substrate is broken and outcomes are RV-proxy. | (a) substrate quarantine lifted with a clean cross-regime backtest **and** (b) envelopes carry per-call `implied_move` for true IV-vs-RV resolution. |
| **C43** | schema-additive instrumentation (enables C16/C18 + debate gate) | signal-confluence-quant, risk-monitor, schema | Carry `dp_block_to_float_ratio`, `insider_cluster_flag`, per-call `implied_move`, and mandatory `debate_residuals.{bull,bear}` so the next audit can grade the float-block gate (C16), the insider conjunction (C18), vol IV-vs-RV (C42), and the debate gate. | Schema-additive, backward-compatible — **shipped 2026-06-20** (the *fields*); the C16/C18 *promotions* still require their own thresholds. |

### C40 — `+2 multileg_directional` weight too high
- **(a) Desk rationale.** The multileg `+2` line scores institutional spread structure on the premise that term-structure-anchored direction inference predicts. The 2026-06-20 audit measured the class realised **0.17 WR (n=12)** vs claimed 0.56 — a **BH-surviving** divergence (the only *directional* class to survive Benjamini-Hochberg), excess −8.3pp.
- **(b) Evidence.** Phase 3 `analyses/audit/2026-06-20/phase_3_calibration.md` (class table); Phase 4 `hot_chains_multileg` marginal −5.2pp.
- **(c) Single-regime caveat.** n=12, all UPTREND. The mechanism claim (term-structure direction ≠ realised direction) is plausible but unproven cross-regime.
- **(d) Acceptance.** Cross-regime ∧ n≥30 per arm ∧ BH-surviving. **Strongest-evidenced pre-registration of the 2026-06-20 run.**
- **(e) Targets.** `signal-confluence-quant.md` (the `+2 multileg-strategist directional structure` line). Freeze-safe until cleared.

### C41 — `≥9` HIGH tier cut re-confirm
- **(a) Desk rationale.** The conviction ladder is inverted at the top across **two consecutive audits** — 2026-06-12 (HIGH 0.222) and 2026-06-20 (HIGH **0.143**, dead last; raw 10/11/12 → 0%/33%/0%; frozen ≥9 band 0.385 < 7–8 band 0.462).
- **(b) Evidence.** Phase 2/3/5 of `analyses/audit/2026-06-20/`.
- **(c) Single-regime caveat.** The frozen-era (06-12+) calls have **0 resolved raw-≥9 outcomes**; the cut is graded only via pre-freeze scores. It cannot be re-binned on another single-window sample without repeating the documented failure mode.
- **(d) Acceptance.** n≥30 resolved raw-≥9 post-freeze calls, cross-regime, HIGH≥MED monotone. The P0.6 half-cap lift is an explicit edit by that audit, never discretionary.
- **(e) Targets.** `signal-confluence-quant.md` tier cuts; `risk-monitor.md` `rubric_regime` half-cap. **KEEP both frozen until the bar clears.**

### C42 — vol-component weights ungradeable
- **(a) Desk rationale.** `earnings_vol` (0.86→0.38) and `high_iv_rank` (0.84→0.38) are the most overconfident classes, but their *claims* are substrate-fabricated and their *outcomes* are RV-direction-proxy — neither side is trustworthy, so the vol weights cannot be graded.
- **(b) Evidence.** Phase 3 §(b) reliability decile [0.80,0.90) n=24 realised 0.42; Phase 4 vol-structure tools negative on RV-proxy.
- **(c) Caveat.** Two independent blockers (substrate + proxy) must both lift before any vol-weight grade is honest.
- **(d) Acceptance.** Clean cross-regime substrate backtest **and** per-call `implied_move` populated for true IV-vs-RV.
- **(e) Targets.** `signal-confluence-quant.md` vol lines; depends on C43's `implied_move`.

### C43 — schema-additive instrumentation (SHIPPED 2026-06-20)
- **(a) Desk rationale.** Three gates were ungradeable in 2026-06-20 for lack of data: debate (residuals on 5/201 rows), C16 (no float-block ratio), C18 (no insider-cluster flag), and vol IV-vs-RV (no per-call implied_move).
- **(b) Shipped.** Schema fields `dp_block_to_float_ratio`, `insider_cluster_flag`, per-call `implied_move` added (additive, optional, backward-compatible — all 23 existing envelopes still validate); `debate_residuals.{bull,bear}` population made mandatory in `risk-monitor.md`.
- **(c) Caveat.** Fields shipped ≠ promotions cleared — C16/C18 still need their own Phase-4 thresholds; this only makes them *testable*.
- **(d) Acceptance.** N/A (enabler, shipped). The promotions remain gated by C16/C18.
- **(e) Targets.** `schemas/decision_envelope.schema.json` (done), `signal-confluence-quant.md` (population instruction, done), `risk-monitor.md` (mandatory debate residuals, done).

---

## 2026-07-25 audit — auditor-method fixes + the first REFUTED closure (C49, C53, C54)

> Registered by the 2026-07-25 calibration audit (`analyses/audit/2026-07-25/`). The
> dataset is **cross-regime for the first time** (159 up-tape / 281 down-tape decided
> rows) on **100% verbatim provenance** (52/52 validated envelopes), which is what makes
> a P0 eligible under C23 — but note both P0-class items land on **auditor method**, not
> on the frozen subject rubric. **The rubric freeze is untouched.** Pre-registrations
> **C50** (`dealer_dex_flip +3`, tape-conditional), **C51** (`accumulation_conjunction
> +3`, +0.4pp at n=14) and **C52** (short-side selection has no alpha in any tape) are
> carried forward with their acceptance bars in `analyses/audit/2026-07-25/phase_5_schema.md`
> §5.5 and are **not actionable now**. C44–C48 live in their own audit folders
> (2026-06-27, 2026-07-04, 2026-07-11).

| ID | Criterion | Owner | Status | Bar / disposition |
|---|---|---|---|---|
| **C49** | Raw benchmark-excess is mostly denominator | `/calibration-audit` (auditor method) | **APPLIED 2026-07-25** | Demote `realised_excess` to an annotated secondary column; promote tape-conditioned book WR + paired McNemar to the primary edge test. |
| **C53** | C19 bearish-flow / single-leg **accrual** | register + fleet advisory notes | **CLOSED — REFUTED 2026-07-25** | Retired. No further accrual; a scored promotion needs a NEW pre-registration on a new substrate. |
| **C54** | Missed-gate denominator includes DROP rows | `/calibration-audit` (auditor method) | **APPLIED 2026-07-25** | Non-DROP denominator for the headline rate and the 20% drift threshold; DROP kept visible on its own line. |

### C49 — benchmark-excess is 71% denominator (auditor method)
- **(a) Desk rationale.** Three consecutive audits led with an excess-sign story:
  2026-07-11 "`bearish_flow` +29.4pp, the down-tape edge", 2026-07-18 "the sign
  reversed", and the raw form of this run's table. Each treated the flip as news about
  the *book*. It was news about the *benchmark*.
- **(b) Evidence.** Phase 3d (`phase_3d_excess_artifact.md`): OLS across 34 strata cells
  `excess_pp = +36.5 − 80.0 × spy_wr`, R² **0.636**; `sd(book) 0.1065` vs `sd(spy)
  0.1670` (dispersion ratio 0.638); implied **β(bookWR | spyWR) = +0.20**. **71.1% of
  the excess column's variance is the benchmark moving.** Robust across n≥15, n≥25,
  extreme-cell exclusion and n-weighting (slope −73 to −88). Three of four canonical
  classes have a book WR that does not move at all between rising and falling tape
  (`bearish_flow` 0.533→0.526, `dark_pool_accumulation` 0.400→0.400, `bullish_flow`
  0.400→0.429) while their excess swings 9–23pp — a ~3.1× noise amplification.
  `multileg_directional` (0.500→0.280) is the one class whose book genuinely moved.
- **(c) Caveat / what this does NOT overturn.** Excess remains the right *concept* and
  the C21 rationale stands; the row-matched paired long-book result survives exactly
  because McNemar cancels the benchmark pairwise. **Do not delete the column** — the
  audit would lose its only beta control. Over-correction is the live risk here.
- **(d) Acceptance.** N/A — auditor-method fix, applied directly. It edits no subject file.
- **(e) Targets.** `.claude/commands/calibration-audit.md` (the skill file; the Phase-7
  doc cited it as `.claude/skills/calibration-audit/SKILL.md`, which does not exist in
  this repo) — Phase 3 §1 class-table spec, Phase 3 output spec + header requirement,
  Phase 7 "edge before calibration" hard rule, method register.

### C53 — C19 (`bearish_flow` / single-leg accrual) CLOSED as REFUTED
- **(a) Desk rationale.** Six audits logged the same line: "`bearish_flow` shows
  positive excess but scores 0" — carried as evidence of an unscoreable down-tape edge
  awaiting graduation. Phase 3d shows there is nothing to graduate.
- **(b) Evidence.** Phase 3: `bearish_flow` realised **0.49 vs claimed 0.48 on n=94**
  (p=0.96 — the **best-calibrated large class in the book**). Phase 3c/3d: book WR
  **0.533 up-tape / 0.526 down-tape** — stationary; the excess swing (+3.3 → −12.3) was
  entirely the benchmark. Phase 3c paired McNemar DOWN/`bearish_flow` **p=0.2478, ns**.
  Post-freeze the class claims 0.519 and realises 0.491 (n=61, +2.9pp ✅).
- **(c) Scope — what this does NOT refute.** The **2026-05-29 `single_leg` PUT research**
  (Tier-1 opening/floor put, WR 0.635, n=266, +26pp, p<0.001) was a *different
  measurement on a different substrate*: raw single-print Parquet rows graded
  next-session, not the daily fleet's scored `bearish_flow` calls graded on a path-aware
  0.5-ATR window. Closing C19 refutes **the accrual claim** — that the fleet's
  `bearish_flow` class carries unscored edge waiting for a scored line — and **not** that
  backtest. The `uw options-flow single-leg` tier scan stays live and **advisory at 0
  rubric points**; the difference is that it is no longer accruing toward anything.
- **(d) Acceptance.** N/A — the criterion is closed, not re-barred. Any future scored
  bearish line requires a **new** C-numbered pre-registration stating its own substrate,
  its own cross-regime ∧ n≥30-per-arm ∧ BH-surviving bar, and a future decision window.
  Do not re-open C19 under its old ≥58%/≥60d/≥2-regime wording.
- **(e) Targets.** This register; `CLAUDE.md` §`uw options-flow single-leg`;
  `.claude/commands/daily-analysis.md` §Single-Leg Whale Signal;
  `.claude/commands/weekly-analysis.md` §Single-Leg Whale Persistence;
  `.claude/agents/accumulation-hunter.md`, `.claude/agents/contrarian-scanner.md`
  (co-flag notes). No rubric line changes — the signal scored 0 before and scores 0 now.

### C54 — missed-gate denominator counts the fleet's early exit as drift
- **(a) Desk rationale.** The ledger has been reporting 32–35% missed-gate rates across
  regime / vrp / event_risk / fundamentals — all past the 20% drift threshold, all
  pointing at `risk-monitor.md`. Decomposed by tier, **every single miss is a DROP row**.
- **(b) Evidence.** Phase 6.5: regime **0/7 HIGH, 0/20 MEDIUM, 0/94 LOW, 211/374 DROP**;
  vrp 0/7, 0/20, 1/94, 215/374; event_risk 0/7, 0/20, 0/94, 206/374; fundamentals 0/7,
  0/20, 2/94, 207/374. **Three misses across 121 non-DROP rows.** DROP names are
  eliminated before the full risk stack runs — correct, efficient behaviour.
- **(c) Caveat.** A genuine future drift confined to DROP rows would be masked by a
  naive exclusion, so the DROP figure stays printed on its own line; it is simply never
  folded into the headline rate or the drift threshold.
- **(d) Acceptance.** N/A — auditor-method fix, applied directly.
- **(e) Targets.** `.claude/commands/calibration-audit.md` Phase 6 (missed-gate ledger,
  agent-prompt drift detection, output spec). **No patch to `risk-monitor.md`** — the
  drift it was flagged for does not exist.

---

## 2026-08-01 audit — first subject-side P0 (C52 CLEARED), plus C55/C56

> **Source audit:** `analyses/audit/2026-08-01/`. Dataset: 578 verbatim envelope calls
> (58/58 `decision.json` validate clean), 501 decided, 232 up-tape / 269 down-tape.
> Provenance 100% verbatim, cross-regime — the C23 P0 eligibility bar is met. The
> 2026-06-12 rubric freeze is **untouched**: no weight edits, no cut re-bins. Every item
> below is either a sizing-*procedure* change (in scope under the freeze), a data-sourcing
> fix, or a pre-registration.

### C52 — short-side selection has no alpha in any tape  *(CLEARED → APPLIED 2026-08-01)*
- **(a) Status.** Registered 2026-07-25 as "suggestive, not proven" (DOWN/short McNemar
  p=0.1214). Its bar — **cross-regime ∧ n≥30 per arm ∧ BH-surviving** — is the same bar
  carried by register **#1** ("no short selection-alpha sizing") since 2026-06-20. **All
  three conditions are now met**, so the standing note was mechanized rather than renewed.
- **(b) Evidence.** Paired McNemar `ALL / short`: **p=0.0115, BH-surviving** on the
  pre-registered 7-cell primary family, **b=24** book-only wins vs **c=46** SPY-only wins,
  n=163. Row-matched, so the benchmark cancels pairwise and the C49 denominator artifact
  cannot explain it. Both tape arms clear n≥30 and agree in sign: **UP −13.0pp (n=92)**,
  **DOWN −14.1pp (n=71)**. Near-identical magnitude across tapes ⇒ **mis-selection, not
  mistiming**, which retires the "shorts may regain edge in a real downtrend" escape
  clause that the 2026-06-27 ruling declined to mechanize on. Corroborating: direction-call
  accuracy **36.0%** in a falling tape (126 of 197 down-tape directional rows were longs);
  sized book **0.294** vs DROP **0.411** in that tape, replicated exactly from 07-25.
- **(c) Caveats, recorded so the rule can be re-opened honestly.** The benchmark is a
  *naive index short* that resolved at 0.595; book shorts realised 0.460 — "materially
  worse than an easy alternative," **not** "loses money outright." n=163 decided is
  statistically sufficient but economically modest. The **long** book carries the mirror
  result and is untouched (`ALL / long` p=0.0046, BH-surviving, n=204, replicated from
  07-25's p=0.0081).
- **(d) Applied as.** Directional shorts route to **`watch_only`** — **routing, not
  suppression**: theses still generated, scored, gate-verdicted and serialized so the
  counterfactual keeps resolving. Instrument-agnostic (the 06-27 withdrawal of the
  single-name-vs-index preference stands). **Out of scope:** short legs in defined-risk
  spreads, vol structures, and the beta-hedge sleeve — hedge *use* ≠ directional expression.
  **Re-open trigger:** short-side paired McNemar non-significant across two consecutive
  cross-regime windows, decided by that audit, never discretionarily.
- **(e) Targets (applied).** `.claude/agents/risk-monitor.md` (sizing rule + superseding
  note on the old expression bullet), `.claude/agents/signal-confluence-quant.md`
  (pre-risk emission), `.claude/commands/daily-analysis.md` Step 5 + §3b,
  `.claude/commands/weekly-analysis.md` Step 5.

### C55 — `sector_rotation` reads a gross-turnover metric as if it were netted
- **(a) Desk rationale.** `options-flow sector-flow` and `sector-flow-persistence` compute
  `net_flow` as *gross call premium − gross put premium* — **sign-agnostic with respect to
  intent**. Aggressive put-selling and aggressive call-buying can produce the same signed
  number, and two-way churn reads as conviction. The two commands are also **one source,
  not two** (values identical to the dollar), so using one to confirm the other
  double-counts a single measurement. The only netted source in the CLI is
  `uw risk market-regime`'s `sector_rotation` field. They disagree materially: 2026-07-31
  showed **+$2.78B gross vs −$187.7M netted on Technology** — opposite signs, same session.
- **(b) Evidence.** Phase 3 §3.1: class realised **0.25 on n=32 decided against a 0.54
  claim**, BH-surviving at **p=0.002** — the worst realised win rate of any class with real
  N in the book. Phase 5 §5.1: `sector_persistence` 0-point emission **−44.2pp (n=8)**.
  Phase 4: `options-flow sector-flow-persistence` **−1.0pp marginal (n=57), NO-INFO**.
- **(c) Applied as (sourcing fix, NOT a weight change).** Direction now reads off the
  netted `market-regime.sector_rotation`; `sector-flow-persistence` is demoted to a
  **durability filter only**; netted-vs-gross disagreement ⇒ **`watch_only`, never a
  rotation call**, with both numbers printed. The conditional `+1` and its three gates are
  untouched — the rubric stays frozen.
- **(d) Acceptance (the replacement is NOT yet validated).** Cross-regime ∧ n≥30 per arm ∧
  BH-surviving, decided by a future audit. If the netted source proves merely noisier
  rather than better, C55 is re-opened by that audit.
- **(e) Targets (applied).** `.claude/agents/sector-rotation-strategist.md`.

### C56 — the `[0.55,0.65)` quote is anti-predictive; the 07-25 floor fixed the SIZE, not the NUMBER
- **(a) Verification of the 07-25 fix — it works.** On the six post-fix envelopes:
  **15/15** quoted rows carry `win_rate_source = backtest_clean` (provenance requirement
  100% enforced) and **all 11 in-band rows sized to `skip`** — none reached the half rung.
  The sizing consequence is fully neutralised.
- **(b) What did not improve.** The band still realises **≈0.29 on n=34 decided** (0.27 on
  n=22 in [0.55,0.60); 0.33 on n=12 in [0.60,0.65)) against ~0.58 predicted, and its
  **share of emissions rose from 25.0% to 73.3%** — the rubric's modal confidence
  statement remains a number the data says to invert.
- **(c) Applied now (non-fitting).** An in-band quote is **disclosure-only and may never be
  cited as supporting evidence for an upgrade** — not a tier promotion, not a size
  increase, not a tie-break. Stated in `audit_trail`.
- **(d) NOT applied — and why.** Re-deriving or suppressing the quote itself is **held**.
  Acceptance bar: **n≥30 post-fix quoted rows**; there are **15**. Acting now would fit a
  re-derivation to 15 observations, which is exactly the failure mode the 2026-06-12 freeze
  exists to prevent. Decided by a future audit.
- **(e) Targets.** `.claude/agents/signal-confluence-quant.md` (disclosure rule applied;
  re-derivation deferred).

### Vol-lane class ceilings (applied 2026-08-01, P1 #3) — pre-registered levels
- **(a) The literal recommendation was already done.** "Cap the vol lane at 0.80" shipped
  2026-06-06; **zero post-freeze quotes exceed 0.80**. The residual defect is different:
  `earnings_vol` and `high_iv_rank` now **pin at exactly 0.80** — all **9** post-freeze
  ≥0.80 quotes in the corpus are this lane — so the ceiling became their default quote
  rather than a rare maximum, while they realise **0.449 (n=78)** and **0.562 (n=16)**.
- **(b) Applied as.** Class-conditional ceilings: `earnings_vol` **0.55**, `high_iv_rank`
  **0.60**. Tightening-only on top of the N-cap and the absolute ceiling (tightest wins),
  so freeze-safe. Both land in `[0.55,0.65)`, so the anti-predictive floor then caps size
  at `starter` — intended stacking.
- **(c) Acceptance.** **The levels are pre-registered** (cross-regime ∧ n≥30 per arm ∧
  BH-surviving): the *existence* of a class ceiling is the calibration fix, the precise
  level is the tunable. Do not generalize to other classes without equivalent
  BH-surviving, multi-audit evidence.
- **(d) Targets (applied).** `.claude/agents/signal-confluence-quant.md`,
  `.claude/commands/daily-analysis.md` Step 5, `.claude/commands/weekly-analysis.md` Step 5.

### Carried forward unchanged (bars NOT met)
- **C50** — `dealer_dex_flip +3` is tape-conditional: **−36.0pp up-tape / +4.2pp down-tape
  (n=31)**, essentially unmoved from 07-25's −34.9/+4.1. Bar: n≥30 **per tape arm**, both
  arms same sign, BH-surviving. The mechanized DEX-flip test fires rarely, so this will
  take many cycles.
- **C51** — `accumulation_conjunction +3`: **+1.9pp at the +1 emission (n=42)**, **−0.7pp
  at the +3 emission (n=14)**. The heaviest weight in the rubric still has no measurable
  marginal contribution in either tape. Bar: n≥30 per arm, ≥2 regimes, BH-surviving.
- **C49** — **replicated on an independent window** (slope −81.9, R² 0.611, dispersion
  0.679, **68.4%** of excess variance is the benchmark, vs 07-25's −80.0 / 0.636 / 0.68 /
  71.1%). Raw benchmark-excess stays demoted; paired McNemar remains the primary edge test.
- **C53** — **confirmed, not merely unrebutted.** `bearish_flow` realised **0.500 vs a 0.49
  claim on n=106** (p=0.918 — best-calibrated large class in the book) and carries negative
  excess in **both** tapes (UP −14.3pp, DOWN −12.3pp). C19 was correctly closed as refuted.
- **C54** — **confirmed.** The DROP-inclusive aggregate would again read ~31%; decomposed,
  the live rubric shows **0/42 missed gates across all nine gates**. The one apparent
  exception (`debate`, 67.9% non-DROP) is a *second* instance of the same denominator
  error: 100% missing pre-freeze, **0% missing post-freeze** — the stage did not exist
  before the freeze. No agent-file drift patch.
- **P2 #7 — `veto_fp_rate` MONITOR, do not loosen.** VETO'd names realised **0.562 (n=16)**
  vs a 0.435 book, anti-effective on its face — but n=16 is barely past the C24 floor, the
  same agent's CAUTION verdict grades correctly (0.369 vs CONFIRM 0.476), and most VETO'd
  names were killed by other gates anyway. C24 forbids loosening on thin effectiveness
  data. Re-grade at n≥30 VETO'd-and-decided. Recorded in `risk-monitor.md`.
