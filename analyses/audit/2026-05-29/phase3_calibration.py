#!/usr/bin/env python3
"""Phase 3 — calibration: claimed vs realised WR, tier reliability, Brier,
score quintiles, C3 expectancy + fractional-Kelly live-activation gate."""
import json, collections, statistics, sys
from pathlib import Path
sys.path.insert(0, "scripts")
import kelly_sizing as ks

AUDIT = Path("analyses/audit/2026-05-29")
WIN, LOSS = "WIN", "LOSS"

# collapse bespoke prose class strings onto canonical families
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
    "multileg_directional": "multileg_directional",
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

def canon(c):
    if not c: return None
    c = c.strip()
    return CANON.get(c, c)

def main():
    rows = [json.loads(l) for l in open(AUDIT / "phase_2_outcomes.jsonl")]
    dec = [r for r in rows if r["outcome"] in (WIN, LOSS)]

    # ---- per-signal-class claimed vs realised (N>=5)
    by_cls = collections.defaultdict(list)
    for r in dec:
        by_cls[canon(r.get("dominant_signal_class"))].append(r)
    cls_table = []
    for c, rs in sorted(by_cls.items(), key=lambda kv: -len(kv[1])):
        if c is None or len(rs) < 5: continue
        n = len(rs)
        realised = sum(1 for r in rs if r["outcome"] == WIN) / n
        claimed_vals = [r["claimed_win_rate"] for r in rs if r.get("claimed_win_rate") is not None]
        claimed = statistics.mean(claimed_vals) if claimed_vals else None
        div = (claimed - realised) * 100 if claimed is not None else None
        cls_table.append({"signal_class": c, "n": n, "claimed_wr": round(claimed,3) if claimed else None,
                          "claimed_n": len(claimed_vals), "realised_wr": round(realised,3),
                          "divergence_pp": round(div,1) if div is not None else None,
                          "flag": (div is not None and abs(div) > 10)})

    # ---- per-tier reliability
    tier_table = []
    for t in ("HIGH", "MEDIUM", "LOW"):
        rs = [r for r in dec if r.get("tier") == t]
        if not rs:
            tier_table.append({"tier": t, "n": 0, "realised_wr": None}); continue
        wr = sum(1 for r in rs if r["outcome"] == WIN) / len(rs)
        tier_table.append({"tier": t, "n": len(rs), "realised_wr": round(wr,3)})
    wr_map = {t["tier"]: t["realised_wr"] for t in tier_table}
    monotone = all(x is not None for x in wr_map.values()) and wr_map["HIGH"] > wr_map["MEDIUM"] > wr_map["LOW"]
    inversions = []
    if wr_map.get("HIGH") is not None and wr_map.get("MEDIUM") is not None and wr_map["HIGH"] <= wr_map["MEDIUM"]:
        inversions.append("HIGH<=MEDIUM")
    if wr_map.get("MEDIUM") is not None and wr_map.get("LOW") is not None and wr_map["MEDIUM"] <= wr_map["LOW"]:
        inversions.append("MEDIUM<=LOW")

    # ---- Brier (rows with claimed_win_rate + outcome)
    brier_rows = [r for r in dec if r.get("claimed_win_rate") is not None]
    brier = statistics.mean([(r["claimed_win_rate"] - (1.0 if r["outcome"]==WIN else 0.0))**2 for r in brier_rows]) if brier_rows else None

    # ---- conviction quintiles on raw_score
    scored = [r for r in dec if r.get("raw_score") is not None]
    scored.sort(key=lambda r: r["raw_score"])
    quint = []
    if scored:
        q = max(1, len(scored)//5)
        for i in range(5):
            chunk = scored[i*q:(i+1)*q] if i<4 else scored[i*q:]
            if not chunk: continue
            wr = sum(1 for r in chunk if r["outcome"]==WIN)/len(chunk)
            quint.append({"quintile": i+1, "n": len(chunk),
                          "score_range": [chunk[0]["raw_score"], chunk[-1]["raw_score"]],
                          "realised_wr": round(wr,3)})

    # ---- C3 expectancy per tier (directional signed only) + Kelly gate
    diru = [r for r in dec if r.get("thesis_direction") in ("long","short")
            and r.get("horizon") in ("swing","weekly","LEAP") and r.get("realised_return_pct") is not None]
    exp_table = []
    closed_for_gate = []
    for t in ("HIGH","MEDIUM","LOW"):
        rs = [r for r in diru if r.get("tier")==t]
        if not rs:
            exp_table.append({"tier": t, "n": 0}); continue
        wins=[r["realised_return_pct"] for r in rs if r["outcome"]==WIN]
        loss=[r["realised_return_pct"] for r in rs if r["outcome"]==LOSS]
        wr = len(wins)/len(rs)
        expc = statistics.mean([r["realised_return_pct"] for r in rs])
        pr = ks.payoff_ratio(statistics.mean(wins), statistics.mean(loss)) if wins and loss else None
        kelly = ks.capped_half_kelly(wr, pr) if pr else None
        exp_table.append({"tier": t, "n": len(rs), "realised_wr": round(wr,3),
                          "expectancy_pct": round(expc,3), "payoff_ratio": round(pr,3) if pr else None,
                          "capped_half_kelly": round(kelly,4) if kelly is not None else None})
        for r in rs:
            closed_for_gate.append(ks.ClosedCall(tier=t, realized_pnl_pct=r["realised_return_pct"], won=(r["outcome"]==WIN)))
    # gate
    try:
        gate = ks.tier_expectancy_monotone(closed_for_gate)
    except Exception as e:
        gate = {"status": "ERROR", "reason": str(e)}

    result = {
        "n_decided": len(dec), "signal_class_table": cls_table, "tier_table": tier_table,
        "tier_monotone": monotone, "tier_inversions": inversions,
        "brier": round(brier,4) if brier is not None else None, "brier_n": len(brier_rows),
        "quintiles": quint, "expectancy_table": exp_table, "kelly_gate": gate,
        "directional_n": len(diru),
    }
    json.dump(result, open(AUDIT / "phase_3_calibration.jsonl", "w"), indent=1)
    print(json.dumps(result, indent=1))

if __name__ == "__main__":
    main()
