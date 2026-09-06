# 02 — Edge analysis: where `fz` augments the workflows

Each finding names the **current source** (or its absence), the **desk objection** `fz` answers,
the **factual basis**, and a score. Findings are ordered by impact. The repo's own documents are the
primary evidence: `AUDIT.md §4` ("Missing capabilities the trader desk would want") and the
data-sources table row that ends *"Short interest, borrow rates, float, institutional/analyst
positioning — **Intentionally absent**."*

Rubric — **Impact:** CRITICAL/HIGH/MEDIUM/LOW · **Effort:** S/M/L · **Edge:** A=alpha R=risk O=operational

---

## E1 — Short-interest + float gate · **HIGH · S · A·R**
**Touch points:** `fundamentals-gate` (Phase 2b), `risk-monitor` gate stack (Phase 2d), `contrarian-scanner` (Phase 1).
**Current source:** none. `AUDIT.md §4` — *"HIGH — Short interest + borrow rate … core to interpreting bullish flow … Not present in the `uw-pp` tool catalog. Genuinely missing and directly flow-relevant."*

**Desk objection it answers:** a sweep into a 25%-short, 8-day-to-cover name is squeeze fuel; the
identical sweep into a clean float is a clean directional bet. A *short* thesis into high SI + low
float is a squeeze trap, not a clean fade. The repo sizes both identically today.

**What `fz` provides:** `fz quote <T> --agent --select 'fundamentals.Short Float,fundamentals.Short Ratio,fundamentals.Shs Float'`
returns short float %, days-to-cover, and float for the top-5 — free, deterministic, point-in-time.
(Verified syntax: dotted paths, comma-separated, **no inner quotes** around keys with spaces — see `04 §1`.)

**Factual basis:** AAPL verified `Short Float 0.92%`, `Short Ratio 3.05`, `Shs Float 14.67B`
(`04 §1`). Days-to-cover and % float short are the canonical squeeze-pressure inputs on any
equity desk. **Honest:** borrow fee / HTB still absent (`fz` limit #4) — this closes the SI/DTC/float
leg of the §4 gap, not the borrow leg.

**Mechanic (proposed, see `03`):** fundamentals-gate emits `short_float`, `short_ratio`, `float`;
risk-monitor adds a squeeze axis — SHORT thesis into `Short Float ≥ 20%` AND `Short Ratio ≥ 5` → flag
squeeze risk (−1 tier); LONG momentum into the same = squeeze-tailwind note. contrarian-scanner gains
the crowding axis it lacks (short crowding, not just put/call crowding).

---

## E2 — Float-normalized conviction · **HIGH · S · A**
**Touch points:** `accumulation-hunter` (Phase 1), `signal-confluence-quant` (Phase 2a).
**Current source:** none — UW gives block $ size and OI Δ, but **not** float to normalize against.

**Desk objection:** order size is only meaningful as a fraction of available float/ADV. A $100k
dark-pool block into AAPL's 14.67B float is noise; the same block into a 5M-float micro-cap is
conviction. The block-tier filter (mega/block) is a *dollar* filter, not a *float-relative* one.

**What `fz` provides:** `Shs Float` per name → `block_notional / (Shs Float × price)` and
`OI_contracts × 100 / Shs Float` become computable conviction normalizers.

**Factual basis:** float-to-order-size normalization is standard market-maker practice; the sibling
`stock-deep-dive` audit (2026-05-25, `00`) makes the same "rank the name against itself / the
universe" argument. The repo has no float field today (data-sources table). Start advisory; the
threshold (e.g., block ≥ X% of float) must be backtested before scoring (`03`, B-phase).

---

## E3 — Candidate pre-filter / squeeze + RS lane in Step 0 · **HIGH · M · A·O**
**Touch points:** Step 0 top-of-funnel (both `/daily-analysis` and `/weekly-analysis`).
**Current source:** `uw screener bullish-bearish`, `uw screener iv-rank`, `uw screener volume-vs-average` — all *flow-derived* funnels.

**Desk objection:** the funnel only sees names that already lit up the options tape. Squeeze setups
and relative-strength leaders that haven't yet hit the flow screener are invisible until too late.

**What `fz` provides:** `fz screen` adds orthogonal, non-flow entry axes — `sh_short_o20`
(squeeze candidates), `ta_newhigh`/`ta_p_channelup` (RS/breakout), `fa_*` (fundamental quality),
`earningsdate_thisweek` — and can enforce the repo's own liquidity floor **server-side**
(`sh_price_o5` + average-volume filter), returning a pre-qualified set so each Phase-1 agent stops
re-filtering. Verified: `fz screen --filter cap_midover,sh_short_o15` returned a live qualified list
(`04 §2`).

**Factual basis:** the repo already enforces `price ≥ $5 AND 20d $-ADV ≥ $50M` per agent (C12);
pushing that into the screen call is a token saving with no behavior change. The squeeze/RS lane is
net-new candidate surface. `stock-deep-dive`'s audit lists "candidate generation" as an explicit
missing capability — `fz screen` is that generator.

---

## E4 — Analyst consensus + target in the debate · **MEDIUM · S · R**
**Touch points:** `bull-researcher`/`bear-researcher` (Phase 2c), `fundamentals-gate` (Phase 2b).
**Current source:** `uw insights analyst-vs-flow` (a divergence label). `AUDIT.md`: "analyst positioning (beyond flow)" absent for prose context.

**Desk objection:** the bull/bear debate has no explicit consensus rating or upside-to-target number
to argue over — it argues flow vs flow.

**What `fz` provides:** `Recom` (1.00–5.00) and `Target Price` per name → upside-to-target % and a
consensus tilt the researchers can cite. **Honest:** partly covered by `uw insights analyst-vs-flow`;
`fz` adds the raw number + a cross-source check (Finviz vs Finnhub divergence is itself a flag).

**Factual basis:** AAPL `Recom 1.98`, `Target Price 316.07` vs `Price 310.85` → +1.7% to target
(`04 §1`). Free per name.

---

## E5 — `insider-clusters` as an accumulation co-flag · **MEDIUM · S · A**
**Touch points:** `accumulation-hunter` (Phase 1), `fundamentals-gate` (Phase 2b).
**Current source:** Finnhub MSPR (a blended monthly ratio) in fundamentals-gate.

**Desk objection:** MSPR collapses a month of activity into one number; it can't tell you that
*three distinct officers* bought this week. Cluster conviction is exactly what accumulation-hunter
hunts, and it has no insider corroborant today.

**What `fz` provides:** `fz insider-clusters --days 7 --min-buyers 2 --side buy` → distinct-buyer
count per ticker. Verified: WHF, 2 owners, 3 txns (`04 §3`).

**Factual basis:** consistent with the repo's C11 *conjunction* philosophy (a signal pays full only
in conjunction). An insider cluster ∧ dark-pool block ∧ cumulative-premium-flow is a stronger
conjunction than any leg alone. Desk rationale: opportunistic, clustered insider buying has
documented predictive content (Cohen, Malloy & Pomorski, *J. Finance* 2012, "Decoding Inside
Information"). Add as a narrative co-flag (0 rubric points) until calibrated — per repo discipline.

---

## E6 — `breadth` as a logged regime cross-check · **MEDIUM · S · R·O**
**Touch points:** Step 0 macro snapshot, `risk-monitor` regime gate.
**Current source:** `uw risk market-regime` (a label) + `uw` breadth %.

**Desk objection:** a single regime label hides breadth *divergence* — index green while the
advance-decline is red is a classic distribution tell the label won't show.

**What `fz` provides:** `fz breadth --group sector` → free, independent, **logged** advancers/
decliners/pct_green series (verified `236/263/46.92%`, `04 §4`); `--days N` makes it a trend. A
second opinion on regime from a different data lineage.

**Factual basis:** advance-decline breadth is the oldest regime/divergence tell in technical
analysis; having it logged lets `/calibration-audit` test whether breadth divergence preceded regime
flips. Advisory (0 points) cross-check, not a new gate.

---

## E7 — `quote-drift` tripwire on the conviction watchlist · **LOW · M · R**
**Touch points:** `risk-monitor` watchlist write-back (gate 12), next-day Step 0.
**Current source:** `uw watchlist alerts` tracks *flow* reversals only.

**Desk objection:** a held conviction name can have its short float spike, analyst target cut, or
guidance re-rate overnight — a fundamentals change the flow-only watchlist never sees.

**What `fz` provides:** snapshot `fz quote` on each top-5 at write-back; next session
`fz quote-drift <T> --since <date>` flags which of the 84 fields moved. A fundamentals-change
tripwire layered onto the existing feedback loop.

**Factual basis:** the repo already maintains a `conviction_<date>` watchlist; this adds a
fundamentals delta with near-zero new machinery (`fz` persists snapshots automatically). Requires a
prior snapshot (`fz` limit #6).

---

## E8 — Technical / RS color for accumulation vs distribution · **LOW · S · A**
**Touch points:** `accumulation-hunter` (Phase 1).
**Current source:** none — UW gives flow, not price-context.

**Desk objection:** dark-pool blocks at the 52-week *low* read as accumulation; the same blocks at
the 52-week *high* with insider selling read as distribution. The agent has no price context.

**What `fz` provides:** `RSI (14)`, `SMA20/50/200` (% from), `Perf *`, `52W High/Low` (% from) per
name — free. AAPL: `RSI 78.85`, `52W High -0.31%` (at highs) (`04 §1`). Advisory color only.

---

## Where `fz` adds **nothing** (scope discipline)

0DTE timing, dealer gamma/vanna (gamma-flip-tracker, dealer-positioning-strategist), IV
term-structure/skew (earnings-scout, vol-surface-scout), GEX/DEX, OI rolls/pin (opex-pin-strategist),
sweep persistence (sweep-tracker) — **all UW microstructure, zero `fz` overlap.** No duplication risk;
`fz` never competes with the flow engine, it only supplies the non-flow context the engine lacks.
