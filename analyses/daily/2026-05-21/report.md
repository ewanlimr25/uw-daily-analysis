# Daily Market Analysis — 2026-05-21

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL / UPTREND. SPY 742.72 (-0.91% from 90d high), above 20/50 SMA. Breadth 37.5% bullish — participation bearish-skewed despite tape. SPY/QQQ/IWM all NEAR_FLIP pinned to call walls (SPY 743, QQQ 715, IWM 283). DEX flipped POSITIVE today on SPY/QQQ for the first time in ~7 sessions — pre-directional swing-long tell. Sector lean: Tech +$4.97B dominates (5/5 persistence), Healthcare flipped −$127M today (single-day rotation OUT).
- **Top 0DTE play:** SPY 738/745 iron condor — both 740 magnet + 743 call wall + 737 put wall form a sticky range; breakout-short trigger lives at SPY <737 (gamma flip ladder). QQQ 708/717 strangle equivalent.
- **Top swing build:** **MSFT long, half size** (raw_score 11, HIGH-tier, 4/4 LOAD-BEARING tools cited). DP $3.84B across 7,058 trades + OI +630k 5d BUILDING + DEX flipped POSITIVE post-3-ZGL-whipsaw. Fresh LEAP build: Dec'27 595C/705C +8k OI each. Win-rate: dark_pool_accumulation NULL backtest → sized half (NA-floor). Invalidation: break of $417.90 on DP block-tier sell skew >0.55, or OI trend flips UNWINDING 2 sessions.
- **Top LEAP candidate:** **TLT long** (Jan 2028 $105C +32.7k OI today, $405M+ premium spent; net Jan'28 calls +80k vs puts +13k). Defensive rate-cut LEAP convex — not a hedge. Sized starter (4/9 LEAP-radar gates passed, sub-threshold confidence). Invalidation: 10Y yield >4.7% OR cum_premium_flow 90d flips negative for 10 sessions.
- **Biggest risk:** Bear setups have a **0.727 historical win-rate today vs bull 0.375** — the tape is UPTREND but the calibration says bearish single-name shorts are outperforming. Net book should run **neutral-to-short**. Largest correlation cluster: WDAY/ZS/MDB/SNOW/CRWD (data-cloud vol cluster corr 0.70-0.78) — risk-monitor deduped to SNOW (NEUTRAL) + MDB (SHORT) as cluster expression. Soft hedge: QQQ Jun-19 590/580 put-vertical 10-15% of long delta (trigger if Tech persistence breaks below 3/5).

## 1. Regime & Gamma State

- **`risk_market_regime`:** TRANSITIONAL — UPTREND, SPY 742.72 (+4.43% 30d), above 20SMA=730 + 50SMA=695, -0.91% from 90d high. Breadth 37.5% bullish (3,849 bearish-flow tickers vs 2,310 bullish across 6,159 with options) → tape is rallying on narrow Tech leadership.
- **Per-index gamma table (today's expiry / 0DTE):**

| Idx | Spot | 0DTE ZGL | Today Flip | Call Wall | Put Wall | 0–45d Regime | Today Regime |
|---|---|---|---|---|---|---|---|
| SPY | 739.48 | 689.71 | 670 | **743 (+0.48%)** | 737 | NEGATIVE (underneath) | **NEAR_FLIP** — POSITIVE today |
| QQQ | 710.41 | 498.38 | 500 | **715 (+0.65%)** | 709 | NEGATIVE (-$55B total) | **NEAR_FLIP** — POSITIVE today |
| IWM | 280.40 | 263.30 | 263 | **283 (+0.93%)** | 279 | mixed | **PIN/TREND-UP** |

- **`options_flow_dte_volume_share`:** 0DTE=24.7%, weekly=32%, monthly=28.5%, LEAP=5.5% → **BALANCED** regime hint. No retail-extreme tape; institutional weeklies+monthlies still own 60% of volume.
- **`historical_vrp` (SPY):** IV30=14.4%, RV30=10.6%, VRP=+3.78pp → **FAIR**. Premium-selling has no statistical edge on the broad index today; single-name premium-sell only.

## 2. 0DTE / Intraday Plays

**Index 0DTE rules:**
- **SPY**: holds >740 → magnet to 743 wall (iron condor / pin trade); breaks <737 → gamma flip ladder targets 735/733 (loss of put wall + 0–45d still NEGATIVE underneath = trend-day short trigger).
- **QQQ**: holds >710 → roll to 715 wall; breaks <709 → flush 705 (resistance wall).
- **IWM**: holds >280 → magnet 283 (highest GEX wall ~$463B); loses <279 → drop to 263 flip strike opens trend.

**0DTE pin candidates:**

| Ticker | Spot | Pin | Dist% | GEX@Pin | Trade Play |
|---|---|---|---|---|---|
| SPY | 739.48 | **740–743** | +0.07/+0.48% | $3.5–4.7B | Sell 738/745 iron condor 0DTE |
| QQQ | 710.41 | **710–715** | +0.0/+0.65% | $0.39–1.27B | Short 708/717 strangle 0DTE |
| IWM | 280.40 | **280–283** | 0/+0.93% | $0.14–0.46B | Sell 278/284 iron fly |
| AAPL | 303.05 | **302.5–305** | -0.18/+0.64% | $0.42–0.58B | Sell 300/307.5 IC 5/22 |
| TSLA | 418.58 | **420** | +0.34% | $0.28B | Sell 415/425 strangle 5/22 |
| NVDA | 220.99 | **225 (5/22)** | +1.81% | $2.35B | Pre-earnings hedge: 215/235 IC with defined wings — NOT a naked sell into print |

**Urgency-ranked persistent sweeps (≥3 of 5 days):**

| Ticker | Side | Persist | $M (5d) | Smart $ | Hedge? |
|---|---|---|---|---|---|
| TSM | BULL | 4/5 | 242 | ask-side calls | DIRECTIONAL (30d +$544M BULLISH — cleanest semi long) |
| INTC | BULL | 5/5 | 980 | ask-side | DIRECTIONAL (30d +$229M aligned) |
| SNDK | BULL | 5/5 | 550 | ask-side | DIRECTIONAL (30d +$936M strong alignment) |
| ARM | BULL | 3/5 | 419 | ask-side | DIRECTIONAL (30d +$63M weak-aligned) |
| NVDA | BEAR | 5/5 | 5,312 | bid-hit calls | DIRECTIONAL (30d −$54M aligns) |
| TSLA | BEAR | 5/5 | 6,572 | ask-side puts | DROPPED (30d +$920M OPPOSITE → flow_conflict −3) |
| META | BEAR | 5/5 | 596 | bid-hit | DIRECTIONAL (30d −$497M aligns) |
| GOOGL | BEAR | 5/5 | 692 | bid-hit | DIRECTIONAL (30d −$129M aligns) |
| AAPL | BEAR | 5/5 | 1,055 | mixed | DIRECTIONAL (30d +$487M MIXED — sweeps fading drift) |
| AMD | BULL | 5/5 | 1,442 | mixed | **HEDGE-AMBIGUOUS** (30d +$351M MIXED, today bear premium contradicts) |

**OPEX-week pinning candidates:** N/A — May OPEX was 5/15 (6 days ago), June OPEX 5/19 (29 days away). Pin mechanics applied only at 0DTE level above.

## 2a. Swing Dealer Positioning (1–4 weeks)

**Index swing dealer table:**

| Idx | DEX ($) | Sign | Vanna | 10d ZGL Trajectory | ZGL Flip | Swing Bias |
|---|---|---|---|---|---|---|
| SPY | +$69.1T | POSITIVE | -38M (call-heavy) | total_GEX exploded -$361B (5/19) → +$2.75T (5/21) | **5/20 NEGATIVE→POSITIVE** | **LONG-LEAN** — vol-compression rally setup |
| QQQ | +$13.1T | POSITIVE | -5.6M (call-heavy) | flipped POSITIVE today after 8 sessions FULLY_NEGATIVE | **5/21 today's flip — LIVE** | **LONG but FRAGILE** — needs to clear ZGL $714.88 |
| IWM | +$488B | WEAK-POS | **+20M (put-heavy!)** | ZGL collapsed 173→92 | NO clean flip | **LONG (vanna-squeeze candidate)** |

**Single-name swing dealer reads:**

| Ticker | DEX | Vanna | Swing Bias | Note |
|---|---|---|---|---|
| NVDA | +$50.1T STRONG POS | -145M call-heavy | LONG-with-caveat | GEX exploded 8x in 3d. Damps vol, capping upside short-term. Earnings 28May will re-rate. |
| AAPL | +$10.5T STRONG POS | -57M | **LONG** | GEX 10d: $187B → $1.42T. DP $1.08B confirms. Quiet grind higher. |
| MSFT | +$5.88T POS | -20M | **LONG** | 3 ZGL flips 5/11–5/14, resolved POSITIVE (held 7d). Breakout intact. |
| MU | +$7.89T STRONG POS | -2.7M | LONG | call_dex 12x put_dex — but accum DISQUALIFIED + flow_conflict −3 → DROPPED from book. |
| TSLA | +$22.8T STRONG POS | -30M | LONG | Bullish DEX vs bearish persistent sweeps + flow_conflict → DROPPED from book. |
| ARM | +$408B STRONG POS | n/a | LONG | call_dex 31x put_dex — extreme one-sided book. |
| IBM | +$271B STRONG POS | n/a | LONG | call_dex 14x put_dex. |
| MCHP | +$11.3B STRONG POS | n/a | LONG | call_dex 36x put_dex (cleanest one-way book in dataset). |
| SNDK | +$976B STRONG POS | n/a | LONG | 5.4x ratio. |

**Vanna-squeeze BUY setups:** **IWM** is the only true vanna-squeeze candidate (put-heavy book + falling VIX = dealer-cover-buy fuel). All other indices/megacaps are call-heavy → vanna *pressure* not *squeeze*. **BUT IWM dropped from sizing book** via flow_conflict (cum_flow_30d = −$1.07B OPPOSITE long thesis) — keep on watch only.

**ZGL regime-flip detections (10d):** QQQ 5/21 today (live); SPY 5/20 (first positive GEX print after 7-session deep-negative regime); MSFT 5/14 final flip POS held 7d; META 5/14 fragile POS.

## 2b. Sector Rotation

**Rotation regime call: `defensive→cyclical` (with growth-overlay)** — confidence MEDIUM-HIGH. Cyclical leg unambiguous (Industrials 5x prior-day magnitude); defensive leg partial (only Healthcare flipped, Utilities/Staples still positive but tiny).

| Sector | Net Flow Today | 5d Persistence | Trend | Rotation Call |
|---|---:|---:|---|---|
| Technology | +$4,975M | 1.0 | DURABLE INFLOW | rotating-IN (anchor) |
| Consumer Cyclical | +$666M | 1.0 | persistent | rotating-IN |
| Industrials | +$620M | 1.0 | **accelerating (5x prior-day)** | rotating-IN (highest conviction delta) |
| Communication Services | +$571M | 1.0 | persistent | rotating-IN |
| Energy | +$201M | 1.0 | persistent | confirming (contradicts regime snapshot's outflow tag) |
| Financial Services | +$145M | 1.0 | steady | confirming |
| **Healthcare** | **−$127M** | **0.8 ↓ from 1.0** | **SIGN FLIPPED** | **rotating-OUT** |

**Single-name leaders by rotating-IN sector** (institutional DTE share ≥50% required):

| Ticker | Sector | Net Flow | Inst Share | Tag |
|---|---|---:|---:|---|
| **MCHP** | Tech | +$219M | **88.0%** | sector_rotation, top-of-leaderboard |
| **UPS** | Industrials | +$3.8M | **67.8%** | sector_rotation Industrials leader |
| DE | Industrials | +$3.5M | 50.2% | sector_rotation (but flow_conflict −1) |
| CAT | Industrials | +$1.9M | 39.1% | watch — sub-threshold institutional |
| **CPNG** | Cons Cyclical | +$7.8M | **94.3%** | deepest institutional in cyclical leaders |
| AMZN | Cons Cyclical | +$15.4M | 32.7% | tactical only — weekly-skewed |
| **Z** | Comm Svc | +$30.5M | **89.1%** | #1 single-name net flow today in non-Tech-megacap space |
| SPOT | Comm Svc | +$8.1M | 50.4% | flow_conflict −1 (−$44M cum_flow) → DROPPED |
| SNDK | Tech | +$151M | 45.4% | downgrade to sector_tactical (weekly mix) |

**Rotation OUT — Healthcare bearish leaders:** **ABT** (−$17M today, **83.4% monthly institutional**, PCR 5.7) is the clean institutional-grade fade; HCA / NVO / JNJ also bearish but smaller. **Use ABT, not the others.**

## 3. Swing Setups (1–6 weeks)

Ranked by **risk-monitor post-gate final size**. HIGH/MEDIUM tier only (raw_score ≥ 7) plus catalyst-anchored LOW.

### 3a. Long swings (regime-aligned)

| Ticker | Score | Tier | Thesis | Structure | Invalidation | Final Size |
|---|---:|---|---|---|---|---|
| **MSFT** | 11 | **HIGH** | DP $3.84B (block+mega 4/4 LB tools confirmed) + OI +630k 5d BUILDING + DEX flipped POS + Dec'27 LEAP build 595C/705C +8k each. Institutional accumulation overrides 7-of-10 day bearish flow tape. | Long stock or Jun-19 425C / Jul-17 430C; bull put spread 410/400 Jun-19 if seeking premium-collect | <$417.90 on block-tier sell skew >0.55, or OI trend UNWINDING 2 sessions | **half** |
| **AAPL** | 10 | **HIGH** | DP $3.62B at 98% mega buy ratio + OI +611k BUILDING + DEX +$10.5T. Quiet institutional grind. | Long Jun-19 310C / Jul-17 315C; defended DP shelves $304.99 / $302.25 | <$302.25 with block buy-ratio collapse, or B/S ratio <2.0 | **starter** (NA-floor on dark_pool_accumulation backtest) |
| **TSM** | 9 | MED | Sweep persistence 4/5 bull + 30d cum_flow +$544M BULLISH (cleanest semi long); DP $22.6M + 26k OI | Long Jun-19 calls / Bull call spread Jul-17 | sweep persistence drops <3 + 30d cum_flow flat | starter |
| **SNDK** | 9 | MED | Sweep persistence 5/5 + cum_flow +$936M (largest 30d accretion in book); top bullish flow +$151M | Long stock + protective Jul puts; or call spread Jun-19 | flow reverses bearish + persistence breaks | starter |
| **MCHP** | 8 | MED | Top bullish premium +$219M today (#1 single-day net flow) + DEX call-dex 36x put-dex + sector_rotation Tech leader 88% institutional | Bull call spread Jun-19 + watch tomorrow for sweep persistence confirmation | single-day sweep not confirmed on 5/22 → flag stale; sector_persistence breaks | starter |
| **ARM** | 7 | MED | DEX call-dex 31x + sweep persistence 3/5 + top bullish premium +$19M | Bull put spread (per playbook batch) | flow_conflict_lite present — wait for cum_flow to print >$200M aligned | starter |
| **INTC** | 7 | MED | Sweep persistence 5/5 + 30d cum +$229M | Bull put spread Jun-19 (per batch) | persistence drops <3 | starter |
| **IBM** | 7 | MED | 6.9x options volume + top bullish premium +$24M + watchlist DP $32.5M | Follow smart money directional (long calls Jun-19) | flow reversal | starter |
| **MSTR** | 7 | MED | Multileg-strategist $27.5M 170/177.5 5/29 call vertical — 1-week directional, defined risk. **DISAGREES with batch scan ("No Clear Edge") — prefer multileg read.** | 170/177.5 5/29 call vertical (debit ~$3.50) | BTC < prior week low; MSTR < 165 close | starter |
| **TLT** | 6 | LOW-elevated | LEAP convex: Jan'28 $105C +32.7k OI today ($405M+ premium); net Jan'28 calls +80k vs puts +13k. Defensive rate-cut bet. | Long Jan'28 $105C or call diagonal Jul/Jan'28 | 10Y yield >4.7%; cum_flow_90d flips negative 10 sessions | starter |
| WMT | 6 | LOW | Accumulation DP $529M + OI +174k + 4x vol; but single-day bear sweep $54M conflicts | Long stock + protective puts; skip naked calls | DP shelf $130.85 fails | starter |
| QCOM | 6 | LOW | DP $321M + OI +204k BUILDING + B/S 1.59 | Long Jul calls or call spread | OI trend FLAT + block buy-ratio <0.50 | starter |
| AMAT | 5 | LOW | DP $475M + OI +110k BUILDING + B/S 4.08 | Bull call spread Jun-19 | $426.85 DP shelf fails | starter |
| PANW | 5 | LOW | Earnings BUY VOL + KINK at 29May + flow bullish; corr-cluster winner (vs CRWD) | Diagonal: short 252 29May, long 252 17Jul | KINK dissipates pre-event | half (vol play, VRR 0.867) |
| DELL | 4 | LOW | Earnings BUY VOL 28May + BACKWARDATION + flow bullish $5M + AI server thesis | Call vertical 255/270 Jun-5 + short put 235 (risk-reversal) | analyst-flow agreement breaks | half |
| UPS | 4 | LOW | Industrials sector leader 67.8% inst | Long stock / call spread Jul | Industrials persistence <0.6 | starter |
| AMZN | 4 | LOW | Sector_rotation Cyclical tactical (weekly-skewed) | Tactical short-dated calls only | weekly volume drops | starter |
| CPNG | 4 | LOW | Cyclical leader 94.3% institutional | Long stock | sector_persistence breaks | starter |

### 3b. Short / fade swings (defined risk only)

| Ticker | Score | Tier | Thesis | Structure | Invalidation | Final Size |
|---|---:|---|---|---|---|---|
| **NVDA** | 8 | **MED** (vol-structure) | Earnings 28 May postmarket. BACKWARDATION 73→44 + skew COMPLACENT (28d skew_ratio 0.994) + flow_conflict_lite aligned bear + front_iv_ratio 1.686 panic-confirmed. The 738k OI build is **0/1-DTE gamma chase, not accumulation** (per accumulation-hunter deep-read). | **Long Jun-5 ATM straddle** for ER convexity (BUY VOL); or 720P/770C strangle Jun-19; defined-risk only | front_iv_ratio drops <1.10 pre-print (event priced out) OR 30d skew flips TAIL_HEDGING | starter (binary catalyst → max 1/3 of normal short size) |
| **META** | 8 | MED | Sweep persistence 5/5 bear + 30d cum −$497M (load-bearing) + accumulation DISTRIBUTION (mega 0% buy ratio) + OI puts building. **But price RANGEBOUND $599-618 last 10d → directional break required.** Net flow today only −$6.6M (essentially tied) — wait for confirmation. | **Bear put spread Jun-19 600/580** or July 590/570; defined risk only | reclaim of $620 with Tech persistence ≥4 | starter |
| ABT | 5 | MED-elevated | Healthcare rotation OUT (sector 5d→1d sign flip) + 83.4% institutional puts + bearish confluence 5 (PCR z+2.83). **Crowd already short — fade-the-fade risk.** | Bear call spread Jul 95/100; do NOT chase long puts (consensus) | Healthcare flow flips positive ≥0.6 persistence | half |
| MDB | 4 | MED | Parabolic +40.5% / IVR 91 / earnings BUY VOL 28May / contrarian iron condor candidate. Corr-cluster C2 winner of short-vol leg. | **Iron condor 330/345C + 285/270P Jun-19** (collect ~25% width) | spot >$340 or <$285; IV expansion >100 IVR | half (vol play) |
| MRVL | 4 | MED | Earnings BUY VOL ★ 27May. BACKWARDATION 155→75 (extreme front kink) + flow bearish + 30d skew COMPLACENT (-0.06 — calls richer than puts pre-print = mispricing) | Long Jun-5 put-side strangle $190; or short Jun-5 ATM call diagonal vs long Jul | front kink dissipates >2 days pre-event | half |
| WDAY | 5 | LOW (corr-deduped) | Earnings TONIGHT/tomorrow 22May. BACKWARDATION 258→67 — but **C2 cluster dedup** (lower raw vs SNOW/MDB). | Long Jun-5 put-side strangle (cheap dispersion); pass otherwise | catalyst is binary, skip after ER | starter |
| NBIS | 5 | LOW | Sweep persistence 4/5 + accumulation DISTRIBUTION (block 0.41/mega 0.33 net selling). Flow_conflict_lite (+$52M cum opposite). | Bear call spread Jun 230/245 | persistence drops <3 | starter |
| ASTS | 4 | LOW | Sweep persistence 5/5 + 30d cum −$63M aligned | Long puts / put spread Jun | persistence breaks | starter |
| CMI | 3 | LOW | Bearish premium −$19M today + PCR collapsed to 0.07 (call-chase exhaustion) | Bear call spread 660/680 Jun-19 (per contrarian-scanner) | spot >$655 + bullish flow reversal | starter |
| CMCSA | 3 | LOW | **Multileg disagrees with batch:** Jan'27 30/35 call diagonal $12M (BACKWARDATION vol-mispricing + re-rate); flow_conflict_lite | Long-dated call diagonal Jan'27 | spot fails to reclaim $26 | starter |
| **DROPPED** | | | | | | |
| TSLA SHORT | n/a | DROP | cum_flow_30d=+$920M OPPOSITE → mechanical flow_conflict −3 | n/a — wait for 30d cum to flip negative | — | skip |
| MU LONG | n/a | DROP | accumulation DISQUALIFIED (block 0.48/mega 0.62 NEUTRAL — DP is two-sided exit liquidity, not accumulation) + flow_conflict −3 (cum −$576M opposite) | n/a | — | skip |
| GOOG SHORT | n/a | DROP | cum_flow_30d=+$334M OPPOSITE → flow_conflict −3 | n/a | — | skip |
| IWM LONG (vanna) | n/a | DROP | True vanna setup BUT cum_flow_30d=−$1.07B OPPOSITE long → flow_conflict −3. Watch only. | n/a | — | skip |
| CRWD SHORT | 4 | DROP | Corr-cluster C1 loser to PANW (corr 0.824) | n/a | — | skip |
| XLI / XLB SHORT | 1 | DROP | flow_conflict_lite (XLI +$28M opposite); sector_persistence INFLOW contradicts hedge | n/a | — | skip |
| AVGO LONG | 1 | DROP | Sweep hedge-flagged + bearish premium today | n/a (KINK trade lives in §5 vol-surface only) | — | skip |
| AMD LONG | 4 | LOW (excluded HIGH-conv) | Sweep BULL but HEDGE-FLAGGED + dealer FLAT | starter only — not a recommended trade today | hedge classification flips directional | starter |

## 4. LEAP Builds (6–24 months)

**Zero HIGH-conviction LEAP surfaces today** (none clear the 6/9-gate threshold). Top sub-threshold watch only:

| Ticker | DTE_min | OI Build 10d | cum_flow_90d | Gates Passed | Note |
|---|---:|---:|---:|---:|---|
| **TLT** | 610 | +2.75M net | +$13.2M (MIXED, thin) | **4/9** | Jan'28 $105C +32.7k today ($405M+ premium). Surface to §3a — defensive LEAP convex on rate-cut cycle. |

**Disqualifications (and why):**
- **MSFT**: leap-positioning-radar flagged COVERED_CALL (call bid-vol > ask-vol = institutional overwriting). **BUT** deep-dive shows Dec'27 595C +8k OI and 705C +8k OI at premium $24.80 and $12.20 avg respectively — these ARE fresh OTM call builds. The pattern is consistent with collar/yield-enhance overlay on the DP cash equity position, not pure directional LEAP buying. Treat MSFT as institutional accumulation (§3a) not a LEAP build.
- **AAPL**: same COVERED_CALL fingerprint, even cleaner (DP buy ratio 0.876 + call bid-vol > ask-vol). The Jan'28 $300C build is being SOLD against the $1.08B DP cash. **LEAP-collar overlay**, not LEAP buying.
- **NVDA, META, GOOG**: no top-20 fresh DTE≥180 OI builds large enough today. Equity DP only.
- **PLTR, NOW**: bearish LEAP puts (DIRECTIONAL_SHORT signature) — disqualified from LONG screen.
- **SPX**: $7000P 2027 + $6000P 2027 are portfolio hedges, not single-name LEAP.

**Position-roll callouts (same-day near→far):** GDX put (balance 0.853) — clean miner hedge extension; BABA call (0.40) net build at far DTE; HYG call (0.30) credit-risk bullish bet brewing (but dropped via flow_conflict).

## 5. Volatility Surface

**KINKED + catalyst — SELL VOL candidates (premium-rich, event-driven):**

| Ticker | Kink Expiry | Implied Event | IV-Z | Trade |
|---|---|---|---|---|
| **SMTC** | front 26May | Earnings 26May postmarket | +2.30 (100 pct) | **Iron condor 110/120/175/185 short 30May** (22.6% implied move pre-print) |
| **CRWD** | 22May (133%) | Earnings 03Jun | +1.34 (83 pct) | **Calendar: sell 13Jun ATM, buy 17Jul ATM** — but C1 cluster loser to PANW; size accordingly |
| **PANW** | 29May (116% kink) | Earnings 02Jun | +1.06 (83 pct) | **Calendar: sell 29May 252C/252P, buy 17Jul 252C/252P** |
| **ZS** | front 22May (134%) | Earnings 26May postmarket | +1.06 (86 pct) | Iron condor or calendar — corr-deduped (kept SNOW as cluster expression) |
| **AVGO** | 18Jun KINK 106% | Earnings 03Jun + 19Jun OPEX | n/a | **Calendar: sell Jun-5 ATM, buy Jun-18 ATM** — own the kink |

**BACKWARDATION + COMPLACENT skew — BUY VOL (event-priced-cheap):**

| Ticker | Front IV / Back IV | Skew Read | Trade |
|---|---|---|---|
| **NVDA** | 73 → 44 (panic ratio 1.66) | 28d skew_ratio 0.994 → **COMPLACENT** | **★★ Long Jun-5 ATM straddle for ER**; cleanest setup on board |
| **MRVL** | 155 → 75 (most extreme) | -0.06 COMPLACENT | **★ Long Jun-5 put-side strangle $190** |
| **CRWD** | 133 → 58 | COMPLACENT 30d | (see calendar above) |

**No clean no-catalyst backwardation calendars** — every front-end backwardation in the dataset maps to an earnings line (May 26 – Jun 4 cluster).

**Single-contract IV outliers (z>2):** None institutional. All outliers (SOXS, BULL, FFAI, QBTS) are sub-$5 strike artifacts — skip.

**Implied moves (computed, top names):** SMTC 22.6% (26May), NVDA ~6.5% (28May), MU ~9% (front 134% IV), WDAY ~16% (258% front), CRWD 2.0% (already crushed forward — likely understated), PANW 1.8%, SNOW 2.7%.

## 6. Risk & Correlation

**Correlation clusters (corr ≥ 0.70, treat as ONE position):**

| Cluster | Members | Top Corr | Sized Member | Dropped |
|---|---|---|---|---|
| **C1 Sec-Vol** | CRWD, PANW | 0.824 | **PANW** (raw=5) | CRWD (raw=4) |
| **C2 Data-Cloud-Vol** | WDAY, ZS, MDB, SNOW, CRWD | 0.70-0.78 | **SNOW (NEUTRAL) + MDB (SHORT)** | ZS, WDAY |

Sub-0.70 informational (no dedup applied): ARM/TSM 0.64, META/NVDA 0.64, AMD/INTC 0.66, AMAT/AMD 0.69.

**Regime gates applied:**
- **Regime conflict (UPTREND vs SHORT)** — net −1 tier on shorts without catalyst. Exemptions granted: NVDA (ER 28May), MDB (ER 28May), MRVL (ER 27May), WDAY (ER tonight), ABT (Healthcare rotation OUT alignment). Demoted by regime gate: META, NBIS, ASTS, CMI, CRWD.
- **VRP gate** — SPY VRP FAIR. SMTC SELL VOL on FAIR VRP took −1 demote (no edge); kept since vol_realisation_rate 0.867 single-name supported.
- **Panic gate** — NVDA front_iv_ratio 1.686 > 1.10 → converted from delta short to vol-structure trade.
- **Correlation gate** — applied (see clusters above).
- **Sector gate** — ABT short aligned with Healthcare OUT (no penalty); no Healthcare longs in book.

**Calibration tilt observed:** bear_flow win_rate 0.727 vs bull_flow 0.375 in current dataset → today's tape structurally rewards single-name shorts more than longs despite UPTREND. Net book delta ≈ +0.45 (NOT triggering 0.6 hedge mandate).

**Hedge sleeve recommendation:** **Soft hedge optional** — QQQ Jun-19 590/580 put-vertical at 10–15% of long delta. Trigger: Tech sector_flow_persistence drops below 3/5 for ≥2 sessions. Avoid VIX call ladder — VRP FAIR makes long-vol marginally negative-EV.

**Adverse-flow exit list (from yesterday's `conviction_2026-05-20`):**

| Ticker | Yesterday's Thesis | Today's Read | Exit Verdict |
|---|---|---|---|
| MSFT | LONG | net_flow −$2.4M tape-bearish but DP $3.84B + OI +115k institutional dominance | **KEEP** |
| AAPL | LONG | net_flow −$222k but DP $4.56B + OI +105k | **KEEP** |
| TLT | LONG | DP $30M + OI +1.81M 5d strengthening | **KEEP** |
| CRWD | (likely LONG) | bearish flow + C1 dedup | **EXIT** |
| GOOG | LONG | bullish flow + DP $935M + OI +56k — flow reversed bullish today | **REINSTATE WATCH** (was dropped via short flow_conflict; tomorrow reconsider as LONG) |

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

| Ticker | Dir | Raw | Tier | Score Components (with audit) | Dom. Class | LB Tools | cum_flow_30d | Win Rate | Pre-Risk | Risk Gates | Final | Invalidation |
|---|---|---:|---|---|---|---|---:|---:|---|---|---|---|
| **MSFT** | LONG | 11 | HIGH | +3 accum (accumulation-hunter / dark_pool_block_stratified $2.3B + insights_institutional_accumulation B/S 2.59) +3 DEX (dealer-positioning / options_structure_dex +$5.88T, 3 ZGL flips POS) +3 cum_flow_bull (sig-conv-quant / historical_cumulative_premium_flow +$665M load-bearing) +1 OI BUILDING +1 conv-matrix proxy | dark_pool_accumulation | **4/4** | +665M | NA | half | regime no-op, VRP no-op, panic no-op, corr no-op, sector no-op | **half** | <$417.90 on block-tier sell skew >0.55 OR OI UNWINDING 2 sessions |
| **AAPL** | LONG | 10 | HIGH | +3 accum (DP $3.62B 98% mega buy + B/S 7.05) +3 DEX (+$10.5T) +3 cum_flow_bull (+$487M MIXED-but-mag>med) +1 OI +611k | dark_pool_accumulation | **4/4** | +487M | NA | starter | no-op all | **starter** | <$302.25 with B/S collapse <2.0 |
| **SNDK** | LONG | 9 | MED | +1 sweep persist 5/5 + +3 cum_flow_bull (+$936M load) +1 OI +3 today bull premium +$151M (top-of-leaderboard) +0 sector net (Tech leader -1 weekly mix) | multi_day_sweep | 3/4 | +936M | 0.375 | starter | no-op | **starter** | persistence drops <3 + flow flips bearish |
| **TSM** | LONG | 9 | MED | +1 sweep persist 4/5 +3 cum_flow_bull +$544M LOAD +3 accum proxy (DP $22.6M + 26k OI) +1 OI +1 sector SOX | multi_day_sweep | 3/4 | +544M | 0.375 | starter | no-op | **starter** | persistence breaks + 30d flow flat |
| **MCHP** | LONG | 8 | MED | +1 sweep watch +3 cum_flow_bull +3 DEX LOAD (call_dex 36x put_dex) +1 sector leader | bullish_flow | 3/4 | +147M | 0.375 | starter | no-op | **starter** | single-day sweep not confirmed 5/22 |
| **NVDA** | SHORT (vol-structure) | 8 | MED | +1 sweep persist 5/5 +3 cum_flow_bear LOAD (-$54M aligned) +1 earnings ★★ +1 vol-surface BACKWARDATION+COMPLACENT skew +2 bear premium today -$190M | bearish_flow | 3/4 | −54M | 0.727 | half | regime no-op (earnings exempt), **panic −1 → convert delta short to vol structure** | **starter (vol-structure)** | front_iv_ratio <1.10 pre-print OR skew flips TAIL_HEDGING |
| **META** | SHORT | 8 | MED | +1 sweep persist 5/5 +3 cum_flow_bear LOAD (-$497M) +3 accum DISTRIBUTION LOAD (mega 0% buy) +1 OI puts building | bearish_flow | 3/4 | −497M | 0.727 | half | regime **−1** (no catalyst) | **starter** | reclaim $620 with Tech persistence ≥4 |
| **ARM** | LONG | 7 | MED | +1 sweep persist 3/5 +3 DEX LOAD (call_dex 31x) +3 cum_flow_bull (+$63M weak-aligned) | bullish_flow | 2/4 | +63M | 0.375 | starter | no-op | **starter** | cum_flow flips bearish |
| **INTC** | LONG | 7 | MED | +1 sweep persist 5/5 +3 cum_flow_bull LOAD (+$229M aligned) +3 accum proxy +1 OI lite −1 flow_conflict_lite (MIXED label) | multi_day_sweep | 2/4 | +229M | 0.375 | starter | no-op | **starter** | persistence drops <3 |
| **IBM** | LONG | 7 | MED | +1 sweep +3 cum_flow_bull LOAD (+$215M) +3 today bull premium watchlist 6.9x vol | bullish_flow | 2/4 | +215M | 0.375 | starter | no-op | **starter** | 6.9x vol not confirmed 5/22 |
| **MSTR** | LONG | 7 | MED | +2 multileg call vertical $27.5M ratio 0.93 +3 cum_flow_lite-bull (+$205M MIXED) +1 sweep mega (cum aligned, kept) +1 OI | multileg_directional | 2/4 | +205M | 0.375 | starter | no-op | **starter** | BTC < prior week low OR MSTR <165 |

**Multileg vs batch_scan disagreements** (prefer multileg per audit policy):
- **MSTR**: batch says "No Clear Edge" — multileg sees $27.5M 170/177.5 5/29 call vertical → **multileg wins**, surface trade.
- **IWM**: batch says "No Clear Edge" — multileg sees 5 distinct put structures $53M ledger → multileg wins (but IWM dropped via flow_conflict; keep tag for context).
- **CMCSA**: batch says "Aggressive long puts" — multileg sees Jan'27 $12M call diagonal → **multileg wins** (long-dated CALL diagonal).
- **MSFT/AAPL/SNDK/TSM/MCHP/NVDA/ABT/FXI**: batch says "No Clear Edge / Stay Flat" — specialist agents found institutional confluence → **specialists win**.

**Conviction-scoring rubric** (embedded for auditability):
```
Daily conviction score = Σ:
  +3  dealer-positioning DEX flip or vanna-squeeze in trade direction
  +3  3+ aligned signals in accumulation-hunter (DP+OI+oi_smart_positioning, dark_pool_block_stratified institutional-tier) [LOAD-BEARING]
  +1  multi-day OI build (historical_oi_trend BUILDING, lookback ≥5d)
  +1  insights_conviction_matrix DIRECTIONAL_LONG, confidence >70 (LEAP gate; demoted as positive scorer)
  +3  historical_cumulative_premium_flow net directional accretion in trade direction (30d) [LOAD-BEARING]
  +1  in sweep-tracker top 5 by hot_chains_sweep_persistence [SUPPRESSED for SPY/QQQ/IWM/SPXW + top-10 mega-caps unless cum_flow_30d aligns]
  +1  sector-rotation-strategist names ticker as single-name leader within rotating sector (persistence ≥3)
  +1  in earnings-scout BUY VOL or SELL VOL
  +2  in multileg-strategist with directional structure
  +1  in vol-surface-scout KINKED or BACKWARDATION with VRP-aligned bias
  -2  contrarian-scanner flags overcrowded long with rising pcr_zscore (VRP positive)
  -3  flow_conflict (cum_flow_30d clearly opposite dominant_signal_class, magnitude > union-median)
  -1  flow_conflict_lite (MIXED or aligned but bottom-quartile magnitude)
  -1  risk-monitor correlation cluster (corr > 0.7) — applied in 2b
  -3  risk_market_regime conflicts with trade direction — applied in 2b

Tiers: ≥10 HIGH | 7–9 MED | 3–6 LOW | ≤2 drop. HIGH requires ≥3/4 LOAD-BEARING tools cited.
Sizing map: win_rate ≥0.70 full | 0.50-0.70 half | <0.50 starter / skip.
```

## 8. Watch-only — single signal, no confluence

Candidates surfaced from one Phase 1 agent but failed the 2-agent confluence gate OR the 4-of-min signal-cluster confluence ≥4. Listed for journaling, NOT for entry today.

- **WMT** — accumulation-hunter MED-HIGH but sweep-tracker sees single-day bear sweep $54M conflicting; watch tomorrow for resolution.
- **HYG** — accumulation-hunter MED (credit risk-on) but flow_conflict (-$30M opposite); confluence-gate fail.
- **DE** — sector_rotation Industrials leader but flow_conflict_lite (-$20M opposite); confluence-gate fail.
- **SPOT** — sector_rotation Comm Svc leader but flow_conflict (-$44M opposite).
- **CAT** — sector_rotation Industrials sub-threshold (39% institutional).
- **AVGO** — vol-surface 18Jun KINK 106% (calendar candidate) — watch only since sweep is hedge-flagged + bearish premium today.
- **CRWV / SPOT / LITE / KWEB / XLI bullish flow** — single-agent flow flags without DP/OI confluence.
- **MRVL bullish flow** — earnings BUY VOL only, no other agent supports.
- **NBIS** — sweep persistence 4/5 bear + accum DISTRIBUTION but flow_conflict_lite (+$52M opposite); watch for cum_flow flip to confirm.
- **SOXX / SOXL / SMH / SOX** — semi ETFs with hedge-ambiguous bullish persistence; only TSM passes clean.
- **DELL** — single-agent earnings BUY VOL + vol-surface BACKWARDATION; no confluence from accumulation or dealer-positioning.

## Appendix — Watchlist Write-Back Confirmation

```
watchlist_write_back_confirmation: SUCCESS
group: conviction_2026-05-21
tickers: [MSFT, NVDA, META, TLT, SNDK]
groups_count: 10
total_tickers_in_all_groups: 31
```

Top-5 selection rationale: top-2 by post-risk tier (MSFT half-long, NVDA structured short) + #3-#4 (META short, AAPL DP-anchored long) + TLT as the convex non-correlated LEAP rates bet. AAPL was a candidate for top-5 over SNDK but the watchlist write-back tickers reflect risk-monitor's hand-back (MSFT/NVDA/META/TLT/SNDK).

---

*Generated by `/daily-analysis` two-phase agent fleet — 11 Phase 1 specialists, signal-confluence-quant + risk-monitor in Phase 2.*
