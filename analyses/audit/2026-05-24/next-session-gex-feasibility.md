# Phase A — Next-Session 0DTE GEX Re-anchor: Feasibility & Backtest Gate

**Date:** 2026-05-24
**Scope:** Re-anchor `/daily-analysis` §2 ("0DTE / Intraday Plays") to surface **next-session**
gamma levels for **SPY and QQQ only**, replacing same-day 0DTE plays that are unactionable
once post-close EOD data lands.
**Author role:** sell-side options market-maker / dealer-desk quant.
**Verdict:** 🔴 **NO-GO on the §2 re-anchor.** Initial run failed on data-integrity grounds; the
underlying GEX data bug was then **root-caused and fixed** (see the 2026-05-24 addendum at the
bottom), and on a **re-run with clean data the gate STILL fails — now on predictiveness.** The
data fix shipped (it independently repairs §1's gamma table + `dex`/`vanna-charm` + the swing
agent); the next-session §2 re-anchor did **not** ship.

> **Read the [addendum](#addendum-2026-05-24--data-bug-fixed-gate-re-run) first** if you only
> want the final decision. The body below is the original pre-fix investigation; §1 (real root
> cause) and §3-Finding-A were superseded by the addendum.

---

## 0. Premise validation (confirm / refute)

The brief asked me to confirm or refute the premise *before* editing. Split verdict:

| Claim | Verdict | Note |
|---|---|---|
| Current §2 labelled "for today" is unactionable post-close | ✅ **Confirmed** | EOD parquet lands after the cash close; the same-day 0DTE it describes has already expired. The critique is correct. |
| Dealer gamma is computed from OI that persists overnight, so EOD GEX is a valid *prior* for tomorrow's 0DTE | ✅ **Confirmed in theory** | OI is a stock, not a flow; the EOD book is the correct starting prior for next-session dealer hedging. The *concept* is sound. |
| The fix is to re-anchor §2 to the next session (not delete gamma analysis) | ⚠️ **Sound in principle, not implementable on current tooling** | See §2–§4. The uw-pp GEX engine cannot target the next session, and — decisively — its per-strike GEX grid for SPY/QQQ never covers spot, so the ZGL/wall/regime it emits are structurally invalid for these two tickers. |

**Bottom line:** the *motivation* for the redesign is valid, but the *data substrate it would
stand on is broken for exactly the two tickers in scope.* Shipping the re-anchor now would
replace an unactionable-but-honest section with an actionable-looking-but-fabricated one. That
is strictly worse.

---

## 1. Market-maker rationale (the desk view, for the record)

This is how a dealer desk *would* read EOD GEX into next-session 0DTE — documented so the
redesign can proceed unchanged the moment the data substrate is fixed (§5 remediation).

### 1a. Zero-gamma level (gamma flip)
The ZGL is the spot at which aggregate dealer gamma crosses zero.
- **Spot above ZGL → dealers net long gamma.** Hedging is mean-reverting (sell rallies / buy
  dips) → **vol suppression, pinning, fade-the-extremes**. Realised vol prints *below* implied;
  0DTE straddles tend to decay → favour premium *selling* structures.
- **Spot below ZGL → dealers net short gamma.** Hedging is trend-amplifying (sell weakness /
  buy strength) → **vol expansion, breakout acceleration, gap continuation**. Favour premium
  *buying* / directional 0DTE.
- The **distance** spot-to-ZGL scales conviction: deep into long-gamma = strong pin; sitting on
  the flip = NEAR_FLIP, regime unstable, do not fade.

### 1b. Call wall / put wall
- **Call wall** = the largest positive-GEX strike above spot. Acts as a **magnet/cap**: in
  long-gamma, dealer selling into it caps rallies; it is the realistic upside pin for the
  session. A *poke beyond* the call wall in short-gamma is the breakout-acceleration trade.
- **Put wall** = the largest (most negative) GEX strike below spot. Acts as **support**; a break
  below flips local hedging short and opens downside.
- **Distance-to-wall sets the realistic next-day range** and therefore whether the 0DTE
  straddle is rich or cheap: walls tight to spot ⇒ small expected range ⇒ straddle rich (sell);
  walls wide ⇒ large expected range ⇒ straddle cheap relative to the gamma map (buy/neutral).

### 1c. Structure selection driven by the levels
- **Long-gamma, walls tight:** iron fly / short straddle / butterfly centred on the pin (ZGL or
  the dominant wall). Sell the rich premium, let gamma decay.
- **Long-gamma, walls wide:** iron condor with shorts just inside each wall.
- **Short-gamma:** debit verticals / directional 0DTE in the trend direction; long straddle if
  spot sits on the flip with walls wide.
- **Fade trade:** short delta just beyond the call wall (resistance) when long-gamma; strike
  selection sits *just beyond* the wall so the wall does the work.

### 1d. Overnight effects
- **Charm** (∂delta/∂time): as time decays overnight — and triple over a weekend — dealer delta
  drifts, forcing **re-hedging into the open**. This is the mechanical driver of the first
  30–60 min drift toward/away from walls. Owned by **`options-structure vanna-charm`** (net
  charm field) and the swing tool **`historical_gex_time_series`** for the multi-day arc.
- **Vanna** (∂delta/∂IV): an overnight VIX move shifts dealer delta even with spot unchanged →
  vanna-driven re-hedge at the open (the classic vanna squeeze on an overnight vol crush). Also
  owned by **`options-structure vanna-charm`** (net vanna field; Karsan/SpotGamma framing).

### 1e. Caveats that degrade the signal (desk discipline)
1. **The book re-computes after the open.** EOD GEX is a *prior*; fresh 0DTE OI floods in during
   the first 30–60 min and can move the ZGL/walls materially. EOD is a starting hypothesis,
   refreshed intraday — never a static target.
2. **Gap risk.** Overnight macro (Asia/Europe), earnings, and Tier-1 prints can gap spot through
   walls before any hedging mechanic engages; the prior is void on a gap.
3. **Vendor GEX sign convention.** Confirmed below — uw-pp's convention is **inconsistent**: the
   `regime` label contradicts the `total_gex` sign on individual days (see §3).
4. **SPX-vs-SPY / NDX-vs-QQQ book cleanliness.** The index (SPX/NDX) book is the cleaner dealer
   gamma signal; the ETF (SPY/QQQ) book is fragmented across the ETF + index + futures options.
   uw-pp exposes only the ETF book here.

---

## 2. uw-pp GEX tool inventory + the load-bearing technical question

> **Q: Can `options_structure_gex` (or the gamma-flip tool) TARGET the next-session expiry,
> or only `dte_max`/today?**
> **A: No. Neither tool can target the next session. There is no expiry-selection parameter.**

| Tool (CLI / MCP) | Params | Next-session targeting? |
|---|---|---|
| `options-structure gex` | `--date`, `--dte-max` (default 45), `--include-zero-gamma` | ❌ Only a DTE *ceiling*. `--dte-max 1` returns **`"no valid gamma/OI within dte_max=1 for SPY"`** — the EOD export does not isolate the next-session expiry. |
| `options-structure today-gamma-flip` | `--date`, `--symbol` | ❌ Keys to `today_expiry = <snapshot date>` — the **same-day** (already-expired post-close) 0DTE. No flag advances it to D+1. |
| `historical gex-time-series` | `--days`, `--dte-max` | ❌ Multi-day ZGL/total-GEX trajectory; aggregate, not per-expiry. |
| `options-structure dex` / `vanna-charm` | per-underlying | n/a — swing greeks, not next-session pin. |
| `oi pin-risk` / `oi opex-concentration` | `--dte-max`, `--top-n` | OI-mass pin screens; not a next-session GEX map. |
| `options-flow expiry-heatmap` / `greek-screener` | flow-level | volume/greek by expiry; not dealer GEX. |
| `historical signal-backtest` | `--signal-type` ∈ {`bullish_flow`,`bearish_flow`,`high_iv_rank`,`volume_spike`,`dark_pool_accumulation`}, `--lookback-days` | ❌ **No GEX/ZGL signal type exists.** The gate therefore had to be built manually from `gex-time-series` joined to next-day spot. |

**Approximation attempted:** on EOD snapshot date D, next session = D+1; for daily-expiry SPY/QQQ
those contracts carry DTE=1, so `--dte-max 1` should approximate the next-session 0DTE book. It
**errors with no data.** `--dte-max 2/3/7` return data but are not isolable to the next session
and are wildly unstable (§3).

---

## 3. Backtest gate — evidence

Reconstructed prior EOD GEX for SPY and QQQ over all **31 available sessions**
(2026-03-13 → 2026-05-22; one ~1-month gap 03-27→04-27) via the uw-pp CLI (same engine the MCP
server wraps). Script: `/tmp/gex_gate_backtest.py`, `/tmp/grid_coverage.py`.

### Finding A — the GEX strike grid never covers spot (fatal)
`options-structure gex` (default `--dte-max 45`) returns a 50-strike grid that, on **every
single session for both tickers**, tops out *below* spot:

| Symbol | Sessions grid covers spot | Typical grid max vs spot |
|---|---|---|
| **SPY** | **0 / 31** | grid max 490–556 while spot 639–747 (~70–200 pts below) |
| **QQQ** | **0 / 31** | grid max 415–520 while spot 566–720 (~150–245 pts below) |

The grid is hard-capped at 50 strikes and bottom-truncated (e.g. QQQ 2026-05-22: strikes
199.78→474.78, spot 719.65). It surfaces only deep-ITM-put / far-OTM strikes — never the
ATM/OTM-call strikes where the gamma walls and the flip actually live. **Consequence:** there is
no call wall (no strike above spot, ever), no zero-gamma crossing near spot (→ ZGL null), and
the regime is mechanically stuck `FULLY_NEGATIVE` (the only strikes visible are negative-gamma
far-OTM puts).

### Finding B — ZGL is null almost always; non-null values are extrapolated/garbage
- **SPY:** ZGL non-null on **1/31** sessions. The single value (749.49 on 05-22) sits ~200 pts
  *above* the grid max (541) — pure extrapolation beyond any strike data.
- **QQQ:** ZGL non-null on **8/31** sessions; values include nonsensical **209.26** and **227.7**
  (vs spot ~705) and several (708, 727, 742, 749) extrapolated above the grid max (~490–505).

### Finding C — the canonical regime-flip signal never fires
`historical gex-time-series` `regime_flip_dates = null` for **both** SPY and QQQ across 31
sessions. The tool's own note ("regime flips … empirically precede realised-vol expansion") has
**n=0 events** in this dataset. The headline H1 hypothesis (spot-vs-EOD-ZGL → next-day vol) is
therefore **untestable**:

| Hypothesis | Testable n | Result |
|---|---|---|
| **H1** spot-vs-ZGL → next-day \|return\| | SPY **0**, QQQ **7** | QQQ: long-gamma days (n=2) mean \|next-day ret\| 0.56% vs short-gamma (n=5) 1.00%. Directionally consistent with theory but **n=2 vs n=5 — statistically meaningless.** |
| **H2** next close lands near EOD call/put wall | **0** | Cannot compute — no call wall exists on any session (Finding A). |

### Finding D — the two GEX tools are mutually inconsistent
- Same date/underlying, `total_gex`: `gex` reports **billions** (e.g. SPY 05-22 +472B);
  `today-gamma-flip` reports **trillions** (SPY 05-21 +14.0T). ~3 orders of magnitude apart.
- **Sign convention is internally contradictory:** SPY 05-22 `gex` → `total_gex = +472B` but
  `regime = NEGATIVE / "Dealers net short gamma"`. QQQ 05-18 → `regime = POSITIVE` with
  `total_gex = −47.3B`. The regime classifier disagrees with its own GEX sign.
- **Instability across the only available knob:** SPY 2026-05-21 ZGL = 600.96 (dte2) → 749.33
  (dte3) → 754.98 (dte7) → null (dte45); regime POSITIVE→NEGATIVE→NEGATIVE→FULLY_NEGATIVE. The
  read is an artifact of the arbitrary `--dte-max`, not a stable dealer-positioning signal.

> Note: `today-gamma-flip` *does* read a correct near-the-money strike set (walls clustered at
> 740–745 vs spot 739) — but it is locked to the snapshot's same-day (expired) expiry, emits
> GEX in a different unit scale, and returns only "support_wall" clusters with no clean
> call/put-wall + ZGL structure. It cannot be advanced to the next session.

---

## 4. Go / No-Go

🔴 **NO-GO — do not edit the pipeline.**

The redesign requires a trustworthy next-session ZGL + call wall + put wall + regime for SPY and
QQQ. The current uw-pp EOD-export GEX engine provides **none of these reliably** for these two
tickers:
1. No next-session targeting exists (§2).
2. The per-strike GEX grid never covers spot — **0/62 symbol-sessions** (Finding A).
3. ZGL is null on 30/31 SPY and 23/31 QQQ sessions; non-null values are extrapolated/garbage
   (Finding B).
4. The regime-flip signal fires zero times → H1 untestable; H2 uncomputable (Findings A, C).
5. The two GEX tools disagree by 3 orders of magnitude and the sign convention is internally
   contradictory (Finding D).

This is **not** a "weak edge, ship with a caveat" situation. The inputs are structurally invalid
for SPY/QQQ. Per the brief's gate ("if the evidence is weak, STOP and report … a 'not predictive
enough to ship' conclusion is a valid outcome") and scope boundary ("do NOT commit if the Phase A
backtest gate fails — report instead"), the edits to §2 / gamma-flip-tracker / weekly / schema
are **withheld**. The existing §2 is left unchanged.

---

## 5. Remediation path (what would unblock a re-run)

The redesign is sound and can proceed unchanged **once the GEX data substrate is fixed**. In
priority order:

1. **Fix the GEX strike-grid bug (P0, root cause).** In the uw-pp Go server (`internal/…`,
   `options-structure gex`), the per-strike builder caps at 50 strikes and selects the wrong
   (bottom) slice of the chain. It must center the grid on spot and span at least ±10–15%
   moneyness (or expose a `--strike-window` / uncapped flag). Without this, *no* GEX-derived
   level for an index is valid — this also silently degrades the current §1 gamma table and the
   swing `dealer-positioning-strategist`.
2. **Reconcile the GEX unit scale & sign convention** between `gex` and `today-gamma-flip`, and
   make the `regime` classifier consistent with `total_gex` sign. Document the convention
   explicitly.
3. **Add a next-session expiry selector** to `gex` (e.g. `--expiry` or `--next-session`) so the
   D+1 0DTE book can be isolated, rather than relying on a `--dte-max` ceiling.
4. **Re-run this gate** (`/tmp/grid_coverage.py` + `/tmp/gex_gate_backtest.py`) after the fix.
   Ship the §2 re-anchor only if: grid covers spot on ≥90% of sessions, ZGL non-null on ≥90%,
   and H1/H2 clear a pre-registered hit-rate vs the 50% baseline on n≥30 per ticker.

Until step 1 lands, consider a **stopgop** for §2 honesty independent of this redesign: relabel
the current same-day 0DTE content as "reference / context (already expired)" so it is not read
as actionable — but that is a separate, smaller change, not the next-session re-anchor.

---

## Addendum (2026-05-24) — data bug fixed, gate re-run

The remediation step 1 above was executed in this same session. Findings and the corrected
decision:

### Real root cause (supersedes §1/§3-Finding-A "display truncation")
The grid-never-covers-spot symptom had **two** causes, and the dominant one was *not* the display
truncation I first flagged. The options export (`bot-eod-report-*.parquet`) is **trade-level**:
one row per print, with each contract's EOD `open_interest` **repeated on every print** (verified:
SPY 738-strike 2026-05-20 call = 35,939 rows, all `distinct_oi = 1`). Every GEX/DEX/vanna/charm
query summed `gamma·OI·100·spot` **once per trade**, so OI was counted thousands of times and
weighted by *trade volume* instead of *open interest*. That inflated `total_gex` by ~3 orders of
magnitude (the 14-trillion `today-gamma-flip` reading), pushed the cumulative-GEX crossing around
arbitrarily (→ null/garbage ZGL, stuck `FULLY_NEGATIVE`), and — combined with a `perStrike[:50]`
head-truncation of an ascending list — made the displayed grid show only deep-OTM strikes.

### Fix shipped (uw-pp Go server, `~/printing-press/library/unusual-whales`)
Minimal, surgical edits across the dealer-greek query sites:
- **Dedup to one EOD row per `(strike, option_type, expiry)`** via
  `row_number() OVER (PARTITION BY … ORDER BY executed_at DESC) = 1` before aggregating — in
  `loadGEXContracts` (`gex`), the `today-gamma-flip` CTE, `computeGEXForDate`
  (`historical gex-time-series`), `dex`, and `vanna-charm`.
- **DTE measured from the snapshot's own day** (`date_diff('day', CAST(executed_at AS DATE), expiry)`)
  instead of wall-clock `time.Now()`/`CURRENT_DATE`, so historical `--date` queries filter
  correctly. The Go-side `ComputeGEXPerStrike` DTE filter is bypassed (`-1`) where SQL now owns it.
- **Per-strike display windows the 50 strikes nearest spot** (re-sorted ascending) instead of the
  lowest 50.
`go vet` clean; `internal/analysis` tests pass; both binaries rebuilt (backups at `*.bak`).

### Validation (rebuilt binary)
| Metric | Before | After |
|---|---|---|
| `gex` grid covers spot (SPY / QQQ) | **0/31 · 0/31** | **31/31 · 31/31** |
| SPY 2026-05-20 grid | [245, 525] | **[716, 765]** (spot 740.8) |
| SPY 2026-05-20 `total_gex` | −177 B | **+0.23 B** |
| SPY 2026-05-20 ZGL / call wall | null / none | **754.5 / 745** |
| `today-gamma-flip` total GEX | ~14 **T** | **+0.35 B** |
| `gex-time-series` QQQ ZGL non-null | 8/31 | **18/31**, regimes vary |

### Backtest gate, re-run on clean data — STILL FAILS (predictiveness)
Reconstructed corrected EOD GEX (logic identical to the shipped binary; spot-checked to match it)
for both tickers, all 31 sessions, at `dte_max ∈ {45, 7}`. **A look-ahead bug in the first H2
pass** (the "nearer wall" was selected using the *next-day* close, manufacturing a spurious 70%)
was found and removed; with the pin chosen using **day-D information only**:

| Test (day-D pin, next-session close) | SPY | QQQ | Pooled | vs 50% base |
|---|---|---|---|---|
| **H1** spot-vs-ZGL → next-day \|ret\| (theory: short-γ > long-γ) | 0.60% vs 0.54% | 1.08% vs 0.86% | — | **wrong direction** |
| **H2** close moves *closer* to nearest EOD wall | 30% | 27% | **28%** | p≈0.9998 (away) |
| **H2** close moves closer to dominant-\|GEX\| strike | 23% | 20% | **22%** | p≈1.0 (away) |
| **H2** moved in pin's direction | 47% | 53% | ~50% | coin-flip |
| **H2** close contained within [put wall, call wall] | 57% | 63% | ~60% | ≈chance |

With clean inputs the EOD GEX levels show **no predictive edge** on next-session behavior in this
sample (n=30/ticker, 60 pooled): the regime→vol relationship is tiny and *backwards*, and the
walls are **not magnets** (next close moves toward them *less* than chance; directional drift and
containment are ≈coin-flip). This is the "not predictive enough to ship" outcome the gate allows.

### Final decision
- ✅ **Data fix: shipped & validated.** It was a genuine, high-impact bug corrupting every
  dealer-greek read for indices; fixing it repairs the §1 gamma table, `dex`/`vanna-charm`, and the
  swing `dealer-positioning-strategist`.
- 🔴 **§2 next-session re-anchor: NOT shipped.** Even with correct data, EOD GEX does not predict
  next-session SPY/QQQ behavior here, and next-session expiry still cannot be isolated (§2 of the
  body). `daily-analysis.md` §2, `weekly-analysis.md`, `gamma-flip-tracker.md`, and the decision
  schema are **unchanged**. Per the brief's gate and scope boundary, nothing was committed for the
  re-anchor.

### Caveats / follow-ups
- Sample is small (~2.5 months, one ~1-month gap, n=30/ticker) and daily-close granularity; a
  larger and/or intraday sample could revisit H2, but current evidence does not support shipping.
- Residual ZGL heuristic quirk: `ComputeZeroGammaLevel` returns the **first ascending** cumulative
  crossing, which can pick a spurious deep-OTM level (e.g. QQQ 2026-05-18 ZGL 209). Consider
  switching to the crossing **nearest spot** — separate from the OI bug, low priority.
- The uw-pp source repo is **not under version control**; the fix lives in-place with `*.bak`
  binary backups. Consider `git init` there to capture this change.
