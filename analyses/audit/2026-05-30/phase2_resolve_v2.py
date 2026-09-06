#!/usr/bin/env python3
"""Phase 2 (2026-05-30 run) — C20 daily-bar path-aware resolution + C21 SPY benchmark.

Differences vs the 2026-05-29 run (close-only):
  C20  true-range ATR(14); walk daily HIGH/LOW bar-by-bar; -1R-first stop rule
       evaluated on intraday extremes (recovers ~80% of the true path rule);
       MAE from daily extremes, not daily close.
  C21  per directional row: spy_benchmark_win = same-direction SPY bet entered the
       same day clears +1R_SPY (path-aware) over the same window.
  C22  signal-backtest NOT used as a point-in-time benchmark (no --date); carried as
       general_class_behaviour colour only (handled in Phase 3).
  C3   realized_pnl_pct written per closed directional call (advisory expectancy record).
"""
import json, os, statistics
from collections import defaultdict

AUD = "analyses/audit/2026-05-30"
OHLC = f"{AUD}/_ohlc"

# ---- load OHLC -------------------------------------------------------------
PX = {}
for fn in os.listdir(OHLC):
    d = json.load(open(f"{OHLC}/{fn}"))
    if d.get("ok") and d.get("bars"):
        PX[d["symbol"]] = d["bars"]
SPY = PX.get("SPY")

WEEK_FRIDAY = {"2026-W18": "2026-05-01", "2026-W19": "2026-05-08",
               "2026-W20": "2026-05-15", "2026-W21": "2026-05-22",
               "2026-W22": "2026-05-29"}

# trading-day window per horizon: (primary_window, secondary_window)
WIN = {"0DTE": (1, None), "swing": (10, 3), "weekly": (10, 5),
       "LEAP": (90, 30), "vol": (10, None)}

NOT_TRADE_SECTIONS = {"watch_only", "leap_disqualified"}


def entry_idx(bars, date):
    """Index of the bar on `date`, else the last bar with date <= date."""
    idx = None
    for i, b in enumerate(bars):
        if b["date"] == date:
            return i
        if b["date"] < date:
            idx = i
        else:
            break
    return idx


def atr_true_range(bars, ei, n=14):
    if ei is None or ei < n + 1:
        return None
    trs = []
    for i in range(ei - n, ei):
        h, l, pc = bars[i]["high"], bars[i]["low"], bars[i - 1]["close"]
        trs.append(max(h - l, abs(h - pc), abs(l - pc)))
    return statistics.mean(trs) if trs else None


def walk_directional(bars, ei, direction, R, nwin):
    """Path-aware first-trigger walk over up to nwin bars after entry.
    Returns (outcome, trigger_bar_offset, realised_ret_pct, mae_pct, ambiguous, window_complete)."""
    entry = bars[ei]["close"]
    up, dn = entry + R, entry - R          # target/stop levels
    fwd = bars[ei + 1: ei + 1 + nwin]
    if not fwd:
        return ("INCONCLUSIVE_window_open", None, None, None, False, False)
    mae = 0.0
    for k, b in enumerate(fwd):
        # adverse excursion in thesis direction
        if direction == "long":
            adv = (entry - b["low"]) / entry * 100
            hit_win = b["high"] >= up
            hit_loss = b["low"] <= dn
        else:  # short
            adv = (b["high"] - entry) / entry * 100
            hit_win = b["low"] <= dn
            hit_loss = b["high"] >= up
        mae = max(mae, adv)
        if hit_win and hit_loss:
            # both touched same daily bar — order unknown; conservative = stop first
            ret = -R / entry * 100
            return ("LOSS", k + 1, ret, mae, True, True)
        if hit_loss:
            ret = -R / entry * 100
            return ("LOSS", k + 1, ret, mae, False, True)
        if hit_win:
            ret = R / entry * 100
            return ("WIN", k + 1, ret, mae, False, True)
    # no trigger over available window
    end = fwd[-1]["close"]
    ret = (end - entry) / entry * 100 * (1 if direction == "long" else -1)
    complete = len(fwd) >= nwin
    return ("INCONCLUSIVE_no_threshold" if complete else "INCONCLUSIVE_window_open",
            None, ret, mae, False, complete)


def resolve_directional(bars, ei, direction, nwin):
    R = atr_true_range(bars, ei)
    if R is None or R <= 0:
        return None
    out, off, ret, mae, amb, comp = walk_directional(bars, ei, direction, R, nwin)
    outcome = out.split("_")[0] if out.startswith("INCONCLUSIVE") else out
    reason = out[len("INCONCLUSIVE_"):] if out.startswith("INCONCLUSIVE") else None
    return {"outcome": outcome, "inconclusive_reason": reason, "trigger_offset": off,
            "realised_return_pct": round(ret, 3) if ret is not None else None,
            "max_adverse_excursion_pct": round(mae, 3) if mae is not None else None,
            "R_pct": round(R / bars[ei]["close"] * 100, 3), "entry_px": bars[ei]["close"],
            "ambiguous_bar": amb, "window_complete": comp, "nwin": nwin}


def resolve_0dte(bars, ei, direction):
    """Next-session resolution. directional: moved +R in dir. long-gamma: |move|>=R.
    pin/short-gamma (stay-within): max |excursion| < R."""
    R = atr_true_range(bars, ei)
    if R is None or R <= 0 or ei + 1 >= len(bars):
        return None
    entry = bars[ei]["close"]; b = bars[ei + 1]
    up_exc = b["high"] - entry; dn_exc = entry - b["low"]
    maxexc = max(up_exc, dn_exc)
    if direction in ("long", "short"):
        if direction == "long":
            hit_win = b["high"] >= entry + R; hit_loss = b["low"] <= entry - R
            mae = dn_exc / entry * 100
        else:
            hit_win = b["low"] <= entry - R; hit_loss = b["high"] >= entry + R
            mae = up_exc / entry * 100
        if hit_win and not hit_loss:
            outcome = "WIN"
        elif hit_loss:                       # incl. same-bar both-touch (conservative)
            outcome = "LOSS"
        else:                                # neither +R nor -R in the single session
            outcome = "INCONCLUSIVE"
        ret = (b["close"] - entry) / entry * 100 * (1 if direction == "long" else -1)
        if outcome == "INCONCLUSIVE":
            return {"outcome": "INCONCLUSIVE", "inconclusive_reason": "no_threshold",
                    "trigger_offset": 1, "realised_return_pct": round(ret, 3),
                    "max_adverse_excursion_pct": round(mae, 3), "R_pct": round(R / entry * 100, 3),
                    "entry_px": entry, "ambiguous_bar": hit_win and hit_loss,
                    "window_complete": True, "nwin": 1}
    elif direction == "vol_long":  # long gamma — wants the break
        win = maxexc >= R
        outcome = "WIN" if win else "LOSS"; ret = (maxexc - R) / entry * 100; mae = 0.0
    else:  # pin / short gamma — wants to stay within
        win = maxexc < R
        outcome = "WIN" if win else "LOSS"; ret = (R - maxexc) / entry * 100; mae = maxexc / entry * 100
    return {"outcome": outcome, "inconclusive_reason": None, "trigger_offset": 1,
            "realised_return_pct": round(ret, 3), "max_adverse_excursion_pct": round(mae, 3),
            "R_pct": round(R / entry * 100, 3), "entry_px": entry, "ambiguous_bar": False,
            "window_complete": True, "nwin": 1}


def resolve_pin(bars, ei, nwin=5):
    """opex pin — stay within +/-R over the window (short-gamma)."""
    R = atr_true_range(bars, ei)
    if R is None or R <= 0:
        return None
    entry = bars[ei]["close"]; fwd = bars[ei + 1: ei + 1 + nwin]
    if not fwd:
        return {"outcome": "INCONCLUSIVE", "inconclusive_reason": "window_open", "entry_px": entry,
                "R_pct": round(R/entry*100,3), "realised_return_pct": None,
                "max_adverse_excursion_pct": None, "trigger_offset": None,
                "ambiguous_bar": False, "window_complete": False, "nwin": nwin}
    maxexc = max(max(b["high"] - entry, entry - b["low"]) for b in fwd)
    complete = len(fwd) >= nwin
    breached = maxexc >= R
    if breached:
        outcome = "LOSS"
    else:
        outcome = "WIN" if complete else "INCONCLUSIVE"
    return {"outcome": "INCONCLUSIVE" if outcome == "INCONCLUSIVE" else outcome,
            "inconclusive_reason": None if outcome != "INCONCLUSIVE" else "window_open",
            "trigger_offset": None, "realised_return_pct": round((R - maxexc)/entry*100, 3),
            "max_adverse_excursion_pct": round(maxexc/entry*100, 3),
            "R_pct": round(R/entry*100,3), "entry_px": entry, "ambiguous_bar": False,
            "window_complete": complete, "nwin": nwin}


def resolve_vol(bars, ei, kind, nwin=10):
    """RV-direction proxy with true ranges: compare in-window mean daily range to the
    14-bar pre-entry baseline. vol_long WIN if range expands; vol_short WIN if contracts."""
    if ei is None or ei < 15:
        return None
    # apples-to-apples realized intraday range (H-L, gap-free) for BOTH baseline and window
    base = statistics.mean([bars[i]["high"] - bars[i]["low"] for i in range(ei - 14, ei)])
    fwd = bars[ei + 1: ei + 1 + nwin]
    if base is None or base <= 0 or not fwd:
        return {"outcome": "INCONCLUSIVE", "inconclusive_reason": "window_open",
                "entry_px": bars[ei]["close"], "R_pct": None, "realised_return_pct": None,
                "max_adverse_excursion_pct": None, "trigger_offset": None,
                "ambiguous_bar": False, "window_complete": False, "nwin": nwin,
                "vol_resolution": "rv_direction_proxy"}
    inwin = statistics.mean([b["high"] - b["low"] for b in fwd])
    ratio = inwin / base
    complete = len(fwd) >= nwin
    if kind == "vol_long":
        win = ratio > 1.0
    else:
        win = ratio < 1.0
    outcome = "WIN" if win else "LOSS"
    if not complete and abs(ratio - 1.0) < 0.10:
        outcome, reason = "INCONCLUSIVE", "window_open"
    else:
        reason = None
    return {"outcome": outcome, "inconclusive_reason": reason, "trigger_offset": None,
            "realised_return_pct": round((ratio - 1.0) * 100 * (1 if kind == "vol_long" else -1), 3),
            "max_adverse_excursion_pct": None, "R_pct": round(base/bars[ei]["close"]*100,3),
            "entry_px": bars[ei]["close"], "ambiguous_bar": False,
            "window_complete": complete, "nwin": nwin, "vol_resolution": "rv_direction_proxy",
            "rv_ratio": round(ratio, 3)}


def spy_benchmark(entry_date, direction, nwin):
    """C21: same-direction SPY path-aware bet, same entry+window. Returns bool or None."""
    if direction not in ("long", "short") or not SPY:
        return None
    ei = entry_idx(SPY, entry_date)
    if ei is None:
        return None
    R = atr_true_range(SPY, ei)
    if R is None or R <= 0:
        return None
    out, *_ = walk_directional(SPY, ei, direction, R, nwin)
    if out == "WIN":
        return True
    if out == "LOSS" or out == "INCONCLUSIVE_no_threshold":
        return False
    return None  # window_open


def main():
    rows = [json.loads(l) for l in open(f"{AUD}/phase_1_inventory.jsonl") if l.strip()]
    out_rows = []
    counts = defaultdict(int)
    for r in rows:
        tk = r.get("ticker_base") or r["ticker"]
        sec = r["section"]; hor = r["horizon"]; tdir = r.get("thesis_direction")
        # entry date
        if r["report_kind"] == "weekly":
            edate = WEEK_FRIDAY.get(r["report_date"], r["report_date"])
        else:
            edate = r["report_date"]
        res = None; mode = None
        if sec in NOT_TRADE_SECTIONS or r.get("tier") == "DROP" or r.get("pre_risk_size") == "skip":
            res = {"outcome": "NOT_A_TRADE", "inconclusive_reason": None}
            mode = "not_a_trade"
        elif tk not in PX:
            res = {"outcome": "INCONCLUSIVE", "inconclusive_reason": "data_unavailable"}
            mode = "no_px"
        else:
            bars = PX[tk]; ei = entry_idx(bars, edate)
            if ei is None:
                res = {"outcome": "INCONCLUSIVE", "inconclusive_reason": "data_unavailable"}
                mode = "no_entry_bar"
            elif sec == "opex_pin":
                res = resolve_pin(bars, ei); mode = "pin"
            elif hor == "0DTE":
                res = resolve_0dte(bars, ei, tdir or "long"); mode = "0dte"
            elif tdir in ("vol_long", "vol_short") or sec in ("vol_long", "vol_short"):
                kind = tdir if tdir in ("vol_long", "vol_short") else sec
                res = resolve_vol(bars, ei, kind); mode = "vol"
            elif tdir in ("long", "short"):
                nwin = WIN.get(hor, WIN["swing"])[0]
                res = resolve_directional(bars, ei, tdir, nwin); mode = "directional"
            else:
                # fallback by section
                if sec == "swing_short":
                    res = resolve_directional(bars, ei, "short", WIN.get(hor, WIN["swing"])[0]); mode = "directional"
                elif sec in ("swing_long", "leap"):
                    res = resolve_directional(bars, ei, "long", WIN.get(hor, WIN["swing"])[0]); mode = "directional"
            if res is None:
                res = {"outcome": "INCONCLUSIVE", "inconclusive_reason": "data_unavailable"}
                mode = mode or "unresolved"
        # SPY benchmark for directional rows
        spy_win = None
        if mode in ("directional", "0dte") and tdir in ("long", "short"):
            nwin = WIN.get(hor, WIN["swing"])[0] if hor != "0DTE" else 1
            spy_win = spy_benchmark(edate, tdir, nwin)
        # C33: LEAP 0.5xATR first-trigger fires in the first ~2 days — that tests a 2-day
        # move, not a 30/90D thesis. Never score LEAP WIN/LOSS until the window closes;
        # carry the interim mark-to-market (window_open_mtm) instead. No LEAP can have 30
        # forward trading days by the 2026-05-29 last bar, so all LEAPs are window_open.
        if hor == "LEAP" and res.get("outcome") in ("WIN", "LOSS", "INCONCLUSIVE"):
            res["window_open_mtm"] = res.get("realised_return_pct")
            res["outcome"] = "INCONCLUSIVE"
            res["inconclusive_reason"] = "leap_window_open"
        nr = dict(r)
        nr.update(res)
        nr["resolution_mode"] = mode
        nr["entry_date_used"] = edate
        nr["spy_benchmark_win"] = spy_win
        # C3 realised pnl for closed directional/0dte
        if res.get("outcome") in ("WIN", "LOSS") and mode in ("directional", "0dte", "vol", "pin"):
            nr["realized_pnl_pct"] = res.get("realised_return_pct")
        else:
            nr["realized_pnl_pct"] = None
        out_rows.append(nr)
        counts[res.get("outcome", "?")] += 1
        counts[f"mode:{mode}"] += 1

    with open(f"{AUD}/phase_2_outcomes.jsonl", "w") as f:
        for r in out_rows:
            f.write(json.dumps(r) + "\n")

    # summary
    dec = [r for r in out_rows if r["outcome"] in ("WIN", "LOSS")]
    win = sum(1 for r in dec if r["outcome"] == "WIN")
    print(f"rows={len(out_rows)} WIN={win} LOSS={len(dec)-win} decided={len(dec)} "
          f"WR={win/len(dec)*100:.1f}%")
    print("outcomes:", {k: v for k, v in sorted(counts.items()) if not k.startswith('mode:')})
    print("modes:", {k[5:]: v for k, v in sorted(counts.items()) if k.startswith('mode:')})
    # directional by direction
    for d in ("long", "short", "vol_long", "vol_short"):
        sub = [r for r in dec if r.get("thesis_direction") == d]
        if sub:
            w = sum(1 for r in sub if r["outcome"] == "WIN")
            print(f"  {d}: n={len(sub)} WR={w/len(sub)*100:.1f}%")
    # by mode
    for m in ("0dte", "pin"):
        sub = [r for r in dec if r.get("resolution_mode") == m]
        if sub:
            w = sum(1 for r in sub if r["outcome"] == "WIN")
            print(f"  mode {m}: n={len(sub)} WR={w/len(sub)*100:.1f}%")
    # SPY benchmark coverage + direction-specific base rates (the C21 inputs)
    sb = [r for r in out_rows if r.get("spy_benchmark_win") is not None]
    sbw = sum(1 for r in sb if r["spy_benchmark_win"])
    print(f"SPY benchmark resolved on {len(sb)} directional rows; blended base rate={sbw/len(sb)*100:.1f}%" if sb else "no SPY benchmark rows")
    for d in ("long", "short"):
        sub = [r for r in sb if r.get("thesis_direction") == d]
        if sub:
            w = sum(1 for r in sub if r["spy_benchmark_win"])
            bk = [x for x in dec if x.get("thesis_direction") == d]
            bkw = sum(1 for x in bk if x["outcome"] == "WIN")
            print(f"  SPY-{d} base rate={w/len(sub)*100:.1f}% (n={len(sub)}) vs BOOK-{d}={bkw/len(bk)*100:.1f}% "
                  f"-> excess={bkw/len(bk)*100 - w/len(sub)*100:+.1f}pp")


if __name__ == "__main__":
    main()
