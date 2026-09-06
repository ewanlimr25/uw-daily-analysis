#!/usr/bin/env python3
"""Phase 3 (2026-05-30) — calibration WITH benchmark-excess (C21), reliability + log-loss
(C25), N>=8 floor + Benjamini-Hochberg (C23). Signal-backtest is colour only (C22)."""
import json, math, os, sys, statistics
from collections import defaultdict

sys.path.insert(0, "scripts")
from excess_winrate import market_excess
from kelly_sizing import payoff_ratio, expectancy, capped_half_kelly, tier_expectancy_monotone, ClosedCall

AUD = "analyses/audit/2026-05-30"
OHLC = f"{AUD}/_ohlc"

CANON = {
    "multi_day_sweep": "bullish_flow", "gamma_breakout": "bullish_flow",
    "dex_flip_long": "dealer_positioning", "dealer_flip": "dealer_positioning",
    "dealer_positioning_flip": "dealer_positioning", "dealer_dex_flip": "dealer_positioning",
    "dealer_positioning_long": "dealer_positioning", "dealer_positioning_short": "dealer_positioning",
    "dealer_charm_tailwind": "dealer_positioning", "dealer_negative_dex": "dealer_positioning",
    "directional_long": "bullish_flow", "contrarian_long": "bullish_flow",
    "contrarian_squeeze": "bullish_flow", "sector_leader": "bullish_flow",
    "directional_short": "bearish_flow", "distribution": "bearish_flow",
    "put_sweep_persistence": "bearish_flow", "crowded_one_way_flow": "bearish_flow",
    "adverse_sector_flow": "bearish_flow", "gamma_breakdown": "bearish_flow",
    "auto_fade": "contrarian_fade", "bull_put_fade": "contrarian_fade", "gamma_fade": "contrarian_fade",
    "vanna_squeeze": "dealer_positioning",
    "leap_directional": "leap", "leap_oi_build": "leap", "leap_accumulation": "leap",
    "leap_mixed": "leap", "leap_soft_watch": "leap",
    "earnings_buy_vol": "earnings_vol", "earnings_buyvol": "earnings_vol",
    "earnings_sell_vol": "earnings_vol", "earnings_sellvol": "earnings_vol",
    "earnings_vol_crush": "earnings_vol", "earnings_vol_sell": "earnings_vol",
    "earnings_directional_calls": "earnings_vol", "earnings_directional_bear": "earnings_vol",
    "earnings_skip": "earnings_vol",
    "vol_kink_long": "vol_surface", "vol_kink_short": "vol_surface", "vol_kink": "vol_surface",
    "kinked_calendar": "vol_surface", "calendar_long_vega": "vol_surface",
    "iv_term_structure_kink": "vol_surface", "vol_surface_kinked": "vol_surface",
    "vol_surface_backwardation": "vol_surface", "vol_surface_dislocation": "vol_surface",
    "implied_vs_realized": "vol_surface", "vol_calendar": "vol_surface",
    "positive_gex_pin": "gamma_pin", "opex_pin": "gamma_pin",
    "macro_hedge": "hedge", "hedge_sleeve": "hedge",
    "analyst_vs_flow": "contrarian_fade", "contrarian": "contrarian_fade",
    "covered_call": "bearish_flow", "sector_rotation": "sector_rotation",
}
DIRECTIONAL_CLASSES = {"bullish_flow", "bearish_flow", "dealer_positioning",
                       "multileg_directional", "contrarian_fade", "leap", "sector_rotation"}

def canon(c):
    if not c: return None
    return CANON.get(c.strip(), c.strip())

# ---- OHLC for terminal (no-stop) returns ----
PX = {}
for fn in os.listdir(OHLC):
    d = json.load(open(f"{OHLC}/{fn}"))
    if d.get("ok"): PX[d["symbol"]] = d["bars"]
WIN = {"0DTE": 1, "swing": 10, "weekly": 10, "LEAP": 90, "vol": 10}

def terminal_return(r):
    """Actual entry->window-end close move (no stop), signed by thesis direction."""
    tk = r.get("ticker_base") or r["ticker"]; ed = r.get("entry_date_used")
    if tk not in PX or not r.get("entry_px"): return None
    bars = PX[tk]; idx = next((i for i, b in enumerate(bars) if b["date"] == ed), None)
    if idx is None: return None
    nwin = WIN.get(r["horizon"], 10)
    end = bars[min(idx + nwin, len(bars) - 1)]
    if min(idx + nwin, len(bars) - 1) <= idx: return None
    sgn = 1 if r.get("thesis_direction") == "long" else (-1 if r.get("thesis_direction") == "short" else 0)
    if sgn == 0: return None
    return (end["close"] - r["entry_px"]) / r["entry_px"] * 100 * sgn

def binom_two_sided(k, n, p):
    """Two-sided exact binomial p-value of k successes in n under null prob p."""
    if n == 0: return 1.0
    pk = math.comb(n, k) * p**k * (1 - p)**(n - k)
    tot = 0.0
    for i in range(n + 1):
        pi = math.comb(n, i) * p**i * (1 - p)**(n - i)
        if pi <= pk * 1.0000001: tot += pi
    return min(1.0, tot)

def benjamini_hochberg(pvals, fdr=0.10):
    """Return set of indices that survive BH at given FDR."""
    m = len(pvals)
    order = sorted(range(m), key=lambda i: pvals[i])
    survivors = set(); kmax = -1
    for rank, i in enumerate(order, 1):
        if pvals[i] <= rank / m * fdr: kmax = rank
    for rank, i in enumerate(order, 1):
        if rank <= kmax: survivors.add(i)
    return survivors

def main():
    rows = [json.loads(l) for l in open(f"{AUD}/phase_2_outcomes.jsonl") if l.strip()]
    for r in rows:
        r["_canon"] = canon(r.get("dominant_signal_class"))
        r["_decided"] = r["outcome"] in ("WIN", "LOSS")
        r["_y"] = 1 if r["outcome"] == "WIN" else (0 if r["outcome"] == "LOSS" else None)

    # ---------- 1. per-class table ----------
    by = defaultdict(list)
    for r in rows:
        if r["_canon"]: by[r["_canon"]].append(r)

    class_rows = []
    for cls, rs in by.items():
        dec = [r for r in rs if r["_decided"]]
        if not dec: continue
        n = len(dec); w = sum(r["_y"] for r in dec); realised = w / n
        claims = [r["claimed_win_rate"] for r in rs if r.get("claimed_win_rate") is not None]
        claimed = statistics.mean(claims) if claims else None
        # benchmark-excess (only on rows carrying a SPY benchmark = directional decided)
        bench = [r for r in dec if r.get("spy_benchmark_win") is not None]
        spy_wr = (sum(1 for r in bench if r["spy_benchmark_win"]) / len(bench)) if bench else None
        bench_realised = (sum(r["_y"] for r in bench) / len(bench)) if bench else None
        excess = market_excess(bench_realised, spy_wr) if (spy_wr is not None and bench_realised is not None) else None
        div = (claimed - realised) if claimed is not None else None
        p = binom_two_sided(w, n, claimed) if claimed is not None else None
        class_rows.append({"cls": cls, "n": n, "claimed": claimed, "realised": realised,
                           "excess": excess, "spy_wr": spy_wr, "bench_n": len(bench),
                           "divergence_pp": (div * 100 if div is not None else None),
                           "p": p, "n_claim": len(claims)})

    # BH across classes that have a claim AND N>=8
    headline = [c for c in class_rows if c["n"] >= 8]
    thin = [c for c in class_rows if 5 <= c["n"] < 8]
    flagged_idx = [i for i, c in enumerate(headline) if c["p"] is not None]
    pvs = [headline[i]["p"] for i in flagged_idx]
    surv = benjamini_hochberg(pvs) if pvs else set()
    bh_survivors = {flagged_idx[j] for j in surv}
    for i, c in enumerate(headline):
        c["bh_flag"] = (i in bh_survivors) and (abs(c["divergence_pp"] or 0) > 10)

    # ---------- 2. tier reliability ----------
    tiers = {}
    for t in ("HIGH", "MEDIUM", "LOW"):
        dec = [r for r in rows if r.get("tier") == t and r["_decided"]]
        if dec:
            w = sum(r["_y"] for r in dec); tiers[t] = (len(dec), w / len(dec))

    # ---------- 3. Brier + reliability deciles + log-loss ----------
    scored = [r for r in rows if r["_decided"] and r.get("claimed_win_rate") is not None]
    brier = statistics.mean([(r["claimed_win_rate"] - r["_y"])**2 for r in scored]) if scored else None
    ll = None
    if scored:
        s = 0.0
        for r in scored:
            p = min(0.99, max(0.01, r["claimed_win_rate"])); y = r["_y"]
            s += -(y * math.log(p) + (1 - y) * math.log(1 - p))
        ll = s / len(scored)
    buckets = [(0.0,0.4),(0.4,0.5),(0.5,0.6),(0.6,0.7),(0.7,0.8),(0.8,0.9),(0.9,1.01)]
    relia = []
    for lo, hi in buckets:
        b = [r for r in scored if lo <= r["claimed_win_rate"] < hi]
        if b:
            relia.append({"bucket": f"{lo:.2f}-{hi:.2f}", "n": len(b),
                          "pred": statistics.mean([r["claimed_win_rate"] for r in b]),
                          "real": statistics.mean([r["_y"] for r in b])})

    # ---------- 4. quintiles on raw_score ----------
    sc = sorted([r for r in rows if r["_decided"] and r.get("raw_score") is not None],
                key=lambda r: r["raw_score"])
    quint = []
    if sc:
        q = len(sc) // 5 or 1
        for i in range(5):
            grp = sc[i*q:(i+1)*q] if i < 4 else sc[i*q:]
            if grp:
                w = sum(r["_y"] for r in grp)
                quint.append({"q": i+1, "lo": grp[0]["raw_score"], "hi": grp[-1]["raw_score"],
                              "n": len(grp), "wr": w/len(grp)})

    # ---------- 5. C3 expectancy + Kelly gate ----------
    # two reads: path-aware +/-R bracket, and terminal (no-stop) move
    exp_tbl = {}
    for t in ("HIGH", "MEDIUM", "LOW"):
        dec = [r for r in rows if r.get("tier") == t and r["_decided"]
               and r.get("thesis_direction") in ("long", "short")]
        if not dec: continue
        wr = sum(r["_y"] for r in dec) / len(dec)
        term = [terminal_return(r) for r in dec]; term = [x for x in term if x is not None]
        wins = [x for x in term if x > 0]; losses = [x for x in term if x <= 0]
        aw = statistics.mean(wins) if wins else 0.0
        al = statistics.mean(losses) if losses else 0.0
        pr = payoff_ratio(aw, al) if losses else None
        ex = statistics.mean(term) if term else None
        hk = capped_half_kelly(wr, pr) if pr else 0.0
        exp_tbl[t] = {"n": len(dec), "wr": wr, "term_expectancy": ex, "payoff": pr,
                      "half_kelly": hk, "n_term": len(term)}
    # Kelly live-activation gate
    closed = []
    for r in rows:
        if r["_decided"] and r.get("tier") in ("HIGH","MEDIUM","LOW") and r.get("thesis_direction") in ("long","short"):
            tr = terminal_return(r)
            if tr is not None:
                closed.append(ClosedCall(tier=r["tier"], realized_pnl_pct=tr, won=(r["_y"] == 1)))
    try:
        gate = tier_expectancy_monotone(closed)
    except Exception as e:
        gate = {"status": "ERROR", "reason": str(e)}

    out = {"classes_headline": headline, "classes_thin": thin, "tiers": tiers,
           "brier": brier, "log_loss": ll, "reliability": relia, "quintiles": quint,
           "expectancy": exp_tbl, "kelly_gate": gate,
           "n_decided": sum(1 for r in rows if r["_decided"]), "n_scored": len(scored)}
    json.dump(out, open(f"{AUD}/phase_3_calibration.jsonl", "w"), indent=1, default=str)

    # ---- console ----
    print(f"decided={out['n_decided']} brier-scored={len(scored)} Brier={brier:.3f} LogLoss={ll:.3f}")
    print("\n=== PER-CLASS (N>=8 headline) ===")
    print(f"{'class':24} {'N':>3} {'claim':>6} {'real':>6} {'excess':>7} {'spyWR':>6} {'div':>7} {'BH':>4}")
    for c in sorted(headline, key=lambda c: -(c['excess'] if c['excess'] is not None else -9)):
        cl = f"{c['claimed']*100:.1f}" if c['claimed'] is not None else " -"
        ex = f"{c['excess']*100:+.1f}" if c['excess'] is not None else "  n/a"
        sp = f"{c['spy_wr']*100:.0f}" if c['spy_wr'] is not None else " -"
        dv = f"{c['divergence_pp']:+.1f}" if c['divergence_pp'] is not None else "  -"
        print(f"{c['cls']:24} {c['n']:>3} {cl:>6} {c['realised']*100:>5.1f} {ex:>7} {sp:>6} {dv:>7} {'FLAG' if c.get('bh_flag') else '':>4}")
    print("\nTHIN_N (5-7, appendix):", [(c['cls'], c['n']) for c in thin])
    print("\n=== TIERS ===")
    for t in ("HIGH","MEDIUM","LOW"):
        if t in tiers: print(f"  {t}: n={tiers[t][0]} WR={tiers[t][1]*100:.1f}%")
    print("\n=== RELIABILITY DECILES ===")
    for b in relia: print(f"  {b['bucket']}: pred={b['pred']*100:.0f}% real={b['real']*100:.0f}% n={b['n']}")
    print("\n=== QUINTILES (raw_score) ===")
    for q in quint: print(f"  Q{q['q']} [{q['lo']}..{q['hi']}]: n={q['n']} WR={q['wr']*100:.1f}%")
    print("\n=== C3 EXPECTANCY (terminal no-stop move) ===")
    for t in ("HIGH","MEDIUM","LOW"):
        if t in exp_tbl:
            e=exp_tbl[t]; pr=f"{e['payoff']:.2f}" if e['payoff'] else "n/a"
            print(f"  {t}: n={e['n']} WR={e['wr']*100:.1f}% term_exp={e['term_expectancy']:+.2f}% payoff={pr} halfK={e['half_kelly']:.3f}")
    print("Kelly gate:", gate)

if __name__ == "__main__":
    main()
