# Phase 1 findings digest — 2026-08-11

Ten Phase 1 agents ran (opex-pin-strategist correctly not spawned: third Friday is 2026-08-21, 10 days out).

## Confluence gate result (>=2 distinct Phase 1 agents flagging the same name positively)

| Ticker | Flagging agents | Direction | Notes |
|---|---|---|---|
| NBIS | accumulation-hunter (HIGH), vol-surface-scout (KINKED + strong neg VRP) | long | dealer-positioning near-miss flip + "vanna pressure"; sweep-tracker shows a CONFLICTING 3/5 bearish sweep tape |
| AXON | accumulation-hunter (MEDIUM/LOW), sector-rotation-strategist (named Industrials leader) | long | accumulation decelerating; top DP price level 72% closing-cross contaminated |
| NVDA | multileg-strategist (bearish Oct16 P220/P180 vertical, repeat 2), sweep-tracker (bearish 5/5) | SHORT | sweep-tracker DEMOTES it: 30d cum_flow +$255M bullish = hedge-flow signature |
| GOOGL | sweep-tracker (bearish 3/5, aligned cum_flow, "strongest mega-cap co-signal"), dealer-positioning (book de-risked, front-end panic 1.254), vol-surface-scout (KINKED 08-14) | SHORT | vol-surface attributes the kink to MACRO (Retail Sales 08-14), not idiosyncratic |
| MU | sweep-tracker (bearish 5/5, downgraded watch-only), vol-surface-scout (KINKED 08-21, neg VRP) | SHORT | BOTH agents caveat heavily: sweep driven by a deep-ITM financing put; kink attributed to FOMC-minutes macro |

## Failed the confluence gate — single agent only (report section 8)

SE (accumulation-hunter HIGH, Step-0 confluence 6), SOFI / BX / EQT / XOM / OXY / DINO / VLO / VRT / RKLB / UNP / V / IREN / GS (sector-rotation leaders, 1 agent), TGT / HD / LOW / TJX / ROST / WMT (earnings-scout SELL VOL, 1 agent), CSCO / AMAT (earnings-scout CALENDAR, 1 agent), INTC / SPCX (sweep-tracker bearish, 1 agent), TLT (multileg Sept18 FOMC straddle, 1 agent), CRWV / TSLA / SNDK (vol-surface only), EWZ / MSTR (multileg watch-only/screened).

## Agent-by-agent

### gamma-flip-tracker (section 2 advisory, 0 points)
- SPY: spot 770.60, ZGL 789.87 (reliable, 2.5% above spot), regime NEGATIVE, total_gex +$209.4M, call wall 780 (+1.22%), put wall AT THE MONEY at 770 (-$255.1M, the largest negative-GEX strike on the book sits on top of spot). Regime flipped POSITIVE->NEGATIVE on 08-10, ONE session ago; 5 flips in 30 days.
- QQQ: spot 718.26, ZGL 769.03 **zgl_reliable=false** (7.07% away; zgl_delta +548.58 on the flip = extrapolation artifact), regime NEGATIVE, total_gex +$55.8M, call wall 730 (+1.63%), put wall AT THE MONEY 718. Flipped POSITIVE->NEGATIVE TODAY; 5 flips in 30 days.
- Read: ATM short-gamma cliff on BOTH indices = whipsaw amplification, not a pin. Favors long gamma / debit verticals over premium selling. CPI tomorrow can gap spot through either wall before hedging engages.

### dealer-positioning-strategist
- **ZERO qualifying DEX flips across 11 names.** The +1 mechanized rubric line fires for NOBODY today.
- Near-misses, both failing the magnitude floor: GOOGL (net_dex +$3.028B 08-10 -> -$7.04M 08-11, prior 10 sessions positive, |flip| 0.2% of the $797.8M floor) and NBIS (3 straight negative sessions -> +$25.3M, |flip| 13% of the $196.8M floor). Both whipsaw-around-zero, correctly rejected.
- **No vanna squeeze anywhere**: the VIX leg needs >=3 consecutive down sessions; the streak broke 08-10 (14.90->15.46). GOOGL and NBIS are the only put-heavy books; downgraded to "vanna pressure, not squeeze".
- Front-end IV panic (>1.05) live on MSFT 1.085, META 1.079, GOOGL 1.254, NBIS 1.279 — read as CPI event pricing.
- DEX magnitude deteriorating 40-95% off this week's peak on SPY/QQQ/NVDA/MSTR/MU while staying positive. NVDA is the most likely near-term flip candidate.
- Tool defect surfaced: `zero_gamma_level` intermittently implausible (QQQ ZGL 249.5 vs $718 spot; NVDA 7.56 vs ~$180 spot) — the known ZGL-grid artifact.

### sector-rotation-strategist
- **rotation_regime: growth->value, HIGH confidence.** Tech (growth) netted OUT -$140.8M; Financials +$13.78M and Energy +$12.45M (value) netted IN. Macro corroborates: 10Y rising 4.72%, USD weakening, core PCE sticky 3.29%.
- Persistence is DEGENERATE — all 11 sectors at 1.0. Zero discrimination; conviction differentiation came from netted magnitude + ETF cross-confirm + price tape instead.
- Critical gap: `market_regime.sector_rotation` only surfaces 6 of 11 sectors. Healthcare, Real Estate, Basic Materials, Comm Services have NO netted direction — no rotation call is possible for them regardless of tape.
- IN (netted-confirmed, gross agrees, ETF confirms): Energy (EQT, XOM, OXY, DINO, VLO), Industrials (AXON, VRT, RKLB, UNP), Financial Services (SOFI, BX, V, IREN, GS) — with the finding that the Financials leg is **regional banks specifically** (KRE +$8.35M BULLISH persistent) while broad XLF actually contradicts (-$1.96M MIXED).
- OUT but gross-vs-netted DISAGREE => watch_only per C55: Technology (gross +$2.13B vs netted -$140.8M, the most extreme split in the book; IGV -$14.46M BEARISH-persistent agrees with OUT, SMH +$3.83M disagrees => the OUT is real but concentrated in software/mega-cap, not semis), Consumer Cyclical (weakest evidence, ETFs disagree too), Consumer Defensive (strongest of the three: XLP price AND XLP ETF flow both independently confirm OUT).
- ETF tape top inflows: XLI +$16.6M, EWY +$12.6M, KRE +$8.35M. Top outflows: GDX -$52.7M, IGV -$14.46M, XLP -$9.29M.

### sweep-tracker (informational, 0 rubric points)
- Tier-1 persistent (5/5 sessions): MU bearish (**downgraded watch-only** — driven by the deep-ITM financing put, and 30d cum_flow is +$164M BULLISH against it), SPCX bearish (aligned, thin name), SNDK bearish (**known put-sale netting contamination**, 30d +$1.17B bullish opposing), INTC bearish (cleanest, 30d -$823M aligned).
- Mega-cap hedge-flow filter demotions: NVDA (bearish sweep vs +$255M bullish cum_flow), AAPL (flat cum_flow), SPX (bullish sweep vs -$2.7B bearish cum_flow — the Dec-2026 7000C block is deep-ITM stock replacement).
- SPY/QQQ/SPXW bearish sweeps ARE cum_flow-aligned but flagged as CPI tail-hedging, not conviction.
- GOOGL: bearish 3/5, cum_flow -$39.8M aligned, price -3.84% — the one mega-cap where sweep + cum_flow + price + screener all agree.
- TSLA/MSFT/AMD/PLTR/META/AMZN all `dominant_direction: mixed` at 5/5 => no directional thesis by disqualifier rule.

### accumulation-hunter
- **Headline: today's mega-tier DP tape is dominated by the closing-cross artifact** — 67-93% of mega-tier premium across MU/AMAT/MSFT/AVGO/APO/OKLO/IBM/GOOGL/GOOG/AMD/AAPL/TSM/NVDA executed 20:00:06Z-20:12:44Z at a single repeated price, often re-reported at 21:19:36Z at the exact same price.
- **NBIS (HIGH)**: mega buy_ratio 0.881 ($151.7M, n=4) all executed 19:38-19:48Z, BEFORE the cross window. Largest print 471,400sh / $90.5M @ $192.05. institutional-accumulation ACCUMULATION, buy/sell 1.98. oi-trend BUILDING 5/5 consecutive. DP shelf $191.00-192.06. distribution_flag PRESENT (call OI closing, $2.48M at strike 220). insider_cluster_flag false. dp_block_to_float 0.00233.
- **SE (HIGH)**: mega buy_ratio 1.00 ($52.7M, n=3, 15:43-17:17Z, zero contamination). accumulation buy/sell 1.66. oi-trend BUILDING 5/5. DP shelf $130.02-131.29. distribution_flag PRESENT and strong — THREE ITM/near-money call strikes closing on heavy volume ($7.09M + $6.5M + $6.1M), the strongest distribution counter-signal in the scan. insider_cluster_flag false. dp_block_to_float 0.000357.
- **AXON (MEDIUM/LOW)**: no mega tier; block buy_ratio 0.856 ($79.7M, n=48). Top price level $636.31 is ~72% closing-cross-timed; the clean remainder (~$60.8M, 14:19-19:55Z) is genuinely buy-side. oi-trend BUILDING but DECELERATING (+4,787 -> +2,916 -> +663 -> +588). distribution_flag false. insider_cluster_flag false. dp_block_to_float 0.0000738 (thin).
- **Explicit disqualifications**: SNDK (institutional-accumulation NEUTRAL, buy/sell 0.82 sell-leaning; mega buy_ratio 0.0 = 100% sell; largest print $23.42 BELOW NBBO mid = special/reference-priced, not aggressive buying — the known put-sale-netting/off-market pattern), MU (52%+ of mega premium at the 20:00 cross at identical price $868.52; surviving large prints ~$12 below mid = off-market reference blocks), AMAT (mega buy_ratio 0.012 = 98.8% SELL — distribution not accumulation), APO/OKLO/IBM (top prints entirely cross-timestamped or late-reprints at the identical cross price), MSFT/AVGO (93.4% / 89.2% cross-contaminated), GOOGL/GOOG/AMD/NVDA/AAPL/TSM (68-76% contaminated AND already net-bearish on options flow).

### contrarian-scanner — EMPTY BOOK (correctly)
- VRP gate FAILS both indices: QQQ -0.0479 NEGATIVE (IV 19.65% below realised 24.44%) => hard abort on the whole Nasdaq-correlated complex. SPY +0.0037 is noise around fair value, not rich vol.
- P/C z-scores are NOWHERE NEAR extreme: SPY z=-0.584 NORMAL, QQQ z=-0.447 NORMAL, both inside +/-1 sigma. There is no crowd to fade.
- The "rising z" trajectory leg remains unsatisfiable (tool has no --date flag).
- SPY price-vs-flow divergence true (price +3.19% vs bearish flow) but IV rank 11.85 LOW => hedging-bid signature, not a short-premium setup.
- Selling front-end premium the night before a Tier-1 CPI print, on a curve already bumped at 08-12/08-14, is the wrong side of priced-in risk.

### earnings-scout
- Structural finding: every screened name shows an elevated 3-DTE (08-14) bucket spanning CPI + PPI + Retail Sales at once. For the six retailers (print dates 08-18 -> 08-20) the hygiene module cleanly separates it — the genuine earnings kink sits one tenor later at 08-21 (10 DTE), uncontaminated.
- **TGT — SELL VOL full size**: earnings 08-19, kink AT 08-21 prominence 17.6%, 17 tenors kept / 0 dropped (best liquidity, 1,785 contracts at the kink), front-end ratio 1.575, term-skew TAIL_HEDGING (+0.0467, ratio 1.13) => tail priced alongside the kink. implied_move 2.02%, ATM IV 67.15% -> ~40-43% crush.
- HD SELL VOL moderate-full (kink prominence only 7.7%, borderline; ratio 1.568; skew TAIL_HEDGING; implied_move 1.95%).
- LOW SELL VOL **half** (skew COMPLACENT ratio 1.018 = flat back-month => front-only kink is a coin flip). implied_move 1.57%.
- TJX SELL VOL **half** (skew UNMEASURABLE — insufficient coverage, not flat). implied_move 1.49%.
- ROST SELL VOL **half** + execution-risk flag (highest raw prominence 21.2% but only 4 tenors survive and the kink tenor has just 77 contracts). implied_move 1.90%.
- WMT SELL VOL moderate (skew NORMAL 1.068, not confirmed-stretched). implied_move 1.58%.
- CSCO CALENDAR + **macro-contaminated**: earnings 08-12 postmarket, the SAME DAY as CPI. Front 3-DTE bucket captures CPI + earnings + PPI together — not cleanly attributable. implied_move 6.93%.
- AMAT CALENDAR + **macro-contaminated + false-lead kink**: the detected kink is at 09-18 (38 DTE), which does NOT match the 08-13 earnings date, so it fails the "kink AT the earnings expiry" gate. implied_move 7.03%.
- SKIP: ADI (no distinct event premium at the tenor that matters; implied_move null), BABA (kink prominence 1.3%, fails the 5% floor; implied_move null).

### vol-surface-scout
- **Headline: a DISPERSION mispricing, not a directional vol call.** Index IV near the bottom of its own distribution (SPY percentile 5.95, QQQ 2.38) while single-name realised vol runs 4-12x index rv20. Critically single-name IMPLIED has not caught up either — every AI/semis name carries strongly NEGATIVE VRP. Setup favors buying single-name vol / staying flat index vol; it is a correlation mispricing, not stock-picking.
- Substrate defect confirmed: `iv-percentile-zscore --lookback-days 252` returned `dates_used: 84` on EVERY name — below the 120-day floor, so all percentiles are provisional.
- 7 of 10 raw term-structure labels flipped under hygiene; 5 of 10 flipped at base_shape.
- KINKED-with-catalyst names are all MACRO, not idiosyncratic: QQQ + GOOGL kink at 08-14 (Retail Sales); SPY + MU kink at 08-21 (session after FOMC Minutes). None appear in the earnings-catalyst screen.
- BACKWARDATION calendar candidates: **none qualify** — CRWV 1.26 / SNDK 1.176 / NBIS 1.279 all carry front-end ratio >1.10 with no resolution => "event still pending, don't fade". Buy the straddle, don't sell a calendar.
- Idiosyncratic outliers, watch-only: TSLA 08-24 tenor (prominence 76%, the largest of the batch, 3,695 contracts, NO identifiable catalyst — do not size), MSTR 08-28 (prominence 11.3%, thinnest kink relative to neighbours).
- No SELL VOL bias emitted anywhere: 8 of 10 names carry strongly negative VRP.

### multileg-strategist
- **NVDA — highest conviction, genuine campaign**: Oct16 P220/P180 debit put vertical, multileg_ratio 0.971 both legs, volumes matched within 2.6%. Term-structure basis: at the traded 66 DTE tenor the curve is FLAT (front-week backwardation is the macro stack) => a directional bet, not disguised vol timing. OPENING — the 220P leg was flagged building +30,028 on 08-10. Repeat count 2. Note 08-10 carried a flow_conflict on NVDA (cum_flow bullish then); today's -$51.5M flip RESOLVES it.
- TLT Sept18 82-strike straddle — clean event play, genuine local kink AT Sept18 (20.0% IV vs 12.0%/13.0% neighbours, n=2,781) against the Sept 16 FOMC. Non-directional. Repeat 1.
- EWZ Oct16/Nov20 C37 calendar — weak anchor (local contango 0.4pt), repeat 1, no aligned whale ticket => watch-only.
- MSTR Aug21/Oct16 C95 calendar — raw label KINKED at Dec-18, four expiries beyond the back leg; at the traded tenors the curve is flat-to-mildly-backwardated => **cannot be cleanly anchored to either play type**, screened.
- **Screened as FINANCING, not theses**: TLT C75/C76 (deep ITM near-parity, ~$0.35 extrinsic — the same rolling family flagged 08-06 with strikes rolled 76/77 -> 75/76), RTX C125 diagonal (delta 0.989, ~$99 ITM), TGT C80/C85 diagonal (delta 0.988+, ~$67-72 ITM), SPX/SPXW 7000C/8000P box family (size-matched pairs, confirmed recurring 08-03 through today).
- Context only: SPXW Sept25 P6300/P6400 vertical (standing crash hedge, 45 DTE past the CPI window), SPY Aug21 C785/P760 strangle (explicit CPI/PPI/Retail-Sales/FOMC-minutes event hedge), VIX multi-expiry call ladder (the most persistent multi-day theme in the book, >=3 sessions).
- DRAM excluded — P30 line prices at $0.001/share on 56,900 contracts, degenerate/stale contract.

### leap-positioning-radar — EMPTY BOOK
- No ticker cleared 6-of-9 gates. LEAP share of DTE volume is only 4.0% today.
- The DTE>180 screen was dominated by: covered-call WRITES dressed as OI growth (SPHR Feb-2027 180C 100% bid-side, CXW 35C 100% bid-side), sub-$5 names failing C12 (MPT $4.02, KOS $2.555, GRAB $3.73), OTM put hedges (HL, AG), and index/ETF lottery strikes.
- VNET was the one genuinely ask-dominant bullish print — **fails C12 liquidity** (20d ADV $27.5M < $50M).
- Three candidates cleared C12 and reached verification; ALL failed Gate 4 (90d cumulative-premium-flow accretion): TTD (oi-trend BUILDING 10/10 but 90d net -$38.2M on $772M gross, and the fresh DTE528 15C print is bid-side dominant = call SELLING), VRT (BUILDING 10/10 but 90d net -$6.07M on $3.44B gross = dead flat, 0.18% of gross), DIS (BUILDING 10/10 but 90d net -$49.2M BEARISH — wrong direction).
- **No cross-horizon confirmation**: none of NBIS / SE / AXON appear anywhere in the DTE>180 biggest-increases list.
