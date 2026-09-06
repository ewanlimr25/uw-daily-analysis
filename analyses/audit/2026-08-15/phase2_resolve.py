#!/usr/bin/env python3
"""Phase 2 (2026-07-04) — C20 daily-bar path-aware resolution + C21 SPY benchmark.

Adapted verbatim (path only) from the 2026-06-20 resolver:
  * Weekly entry = report_date (weekly envelopes carry the Friday date).
  * Resolve PAPER outcomes for ALL directional/vol rows regardless of tier/size;
    carry `was_sized` so the sized-book expectancy view stays separable.
  * canonical_class collapses the fragmented dealer*/distribution labels.
  * LEAP never resolved until 90D window closes.
Adds `entry_regime_bucket` / `post_freeze` passthrough for regime-stratified Phase 3.
"""
import json, os, statistics
from collections import defaultdict

AUD = "analyses/audit/2026-08-15"
OHLC = f"{AUD}/_ohlc"

PX = {}
for fn in os.listdir(OHLC):
    d = json.load(open(f"{OHLC}/{fn}"))
    if d.get("ok") and d.get("bars"):
        PX[d["symbol"]] = d["bars"]
SPY = PX.get("SPY")

WIN = {"0DTE": (1, None), "swing": (10, 3), "weekly": (10, 5),
       "LEAP": (90, 30), "vol": (10, None)}
SIZED = {"full", "half", "starter", "quarter"}


def canonical_class(c):
    if not c:
        return c
    cl = c.lower()
    if cl.startswith("dealer") or "dex_flip" in cl or cl == "dealer_flip":
        return "dealer_positioning"
    if cl.endswith("distribution") or cl == "distribution":
        return "dark_pool_distribution"
    if cl in ("bearish_flow_single_leg_put",):
        return "bearish_flow"
    if cl in ("multileg_directional_conflicted", "directional_conflict"):
        return "multileg_directional"
    if cl in ("single_leg_put", "single_leg_whale"):
        return "single_leg_whale"
    if cl in ("sector_leader", "sector_rotation"):
        return "sector_rotation"
    return c


def entry_idx(bars, date):
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
    entry = bars[ei]["close"]
    up, dn = entry + R, entry - R
    fwd = bars[ei + 1: ei + 1 + nwin]
    if not fwd:
        return ("INCONCLUSIVE_window_open", None, None, None, False, False)
    mae = 0.0
    for k, b in enumerate(fwd):
        if direction == "long":
            adv = (entry - b["low"]) / entry * 100
            hit_win = b["high"] >= up
            hit_loss = b["low"] <= dn
        else:
            adv = (b["high"] - entry) / entry * 100
            hit_win = b["low"] <= dn
            hit_loss = b["high"] >= up
        mae = max(mae, adv)
        if hit_win and hit_loss:
            return ("LOSS", k + 1, -R / entry * 100, mae, True, True)
        if hit_loss:
            return ("LOSS", k + 1, -R / entry * 100, mae, False, True)
        if hit_win:
            return ("WIN", k + 1, R / entry * 100, mae, False, True)
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
    out3, off3, *_ = walk_directional(bars, ei, direction, R, min(3, nwin))
    outcome = out.split("_")[0] if out.startswith("INCONCLUSIVE") else out
    reason = out[len("INCONCLUSIVE_"):] if out.startswith("INCONCLUSIVE") else None
    return {"outcome": outcome, "inconclusive_reason": reason, "trigger_offset": off,
            "realised_return_pct": round(ret, 3) if ret is not None else None,
            "max_adverse_excursion_pct": round(mae, 3) if mae is not None else None,
            "R_pct": round(R / bars[ei]["close"] * 100, 3), "entry_px": bars[ei]["close"],
            "ambiguous_bar": amb, "window_complete": comp, "nwin": nwin,
            "outcome_3d": out3.split("_")[0] if out3.startswith("INCONCLUSIVE") else out3,
            "fast_trigger": bool(off and off <= 3)}


def resolve_vol(bars, ei, kind, nwin=10):
    if ei is None or ei < 15:
        return None
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
    win = ratio > 1.0 if kind == "vol_long" else ratio < 1.0
    outcome = "WIN" if win else "LOSS"
    if not complete and abs(ratio - 1.0) < 0.10:
        outcome, reason = "INCONCLUSIVE", "window_open"
    else:
        reason = None
    return {"outcome": outcome, "inconclusive_reason": reason, "trigger_offset": None,
            "realised_return_pct": round((ratio - 1.0) * 100 * (1 if kind == "vol_long" else -1), 3),
            "max_adverse_excursion_pct": None, "R_pct": round(base / bars[ei]["close"] * 100, 3),
            "entry_px": bars[ei]["close"], "ambiguous_bar": False,
            "window_complete": complete, "nwin": nwin, "vol_resolution": "rv_direction_proxy",
            "rv_ratio": round(ratio, 3)}


def resolve_pin(bars, ei, nwin=5):
    """Pin resolution — DUAL RULE (C59, 2026-08-15 audit P2 #8).

    `outcome` keeps the legacy TOUCH rule (any +/-1R excursion during the window == LOSS)
    so this cycle's numbers stay comparable with the prior ten audits.
    `outcome_settle` applies the SETTLEMENT rule: an iron fly / short straddle / butterfly
    profits from price *finishing* inside the band, so what matters is the distance at the
    END of the window, not whether the tape brushed the wing intraday and came back.

    Both are emitted for one cycle; C59's acceptance bar is >=3 of 9 rows diverging, decided
    at the next audit. Do NOT switch the headline to outcome_settle before that.
    """
    R = atr_true_range(bars, ei)
    if R is None or R <= 0:
        return None
    entry = bars[ei]["close"]; fwd = bars[ei + 1: ei + 1 + nwin]
    if not fwd:
        return {"outcome": "INCONCLUSIVE", "inconclusive_reason": "window_open", "entry_px": entry,
                "R_pct": round(R / entry * 100, 3), "realised_return_pct": None,
                "max_adverse_excursion_pct": None, "trigger_offset": None,
                "ambiguous_bar": False, "window_complete": False, "nwin": nwin,
                "outcome_settle": "INCONCLUSIVE", "pin_rule_divergent": False}
    maxexc = max(max(b["high"] - entry, entry - b["low"]) for b in fwd)
    complete = len(fwd) >= nwin
    breached = maxexc >= R
    outcome = "LOSS" if breached else ("WIN" if complete else "INCONCLUSIVE")

    # Settlement rule: |close_at_window_end - entry| vs R.
    settle_dist = abs(fwd[-1]["close"] - entry)
    if not complete:
        outcome_settle = "INCONCLUSIVE"
    else:
        outcome_settle = "WIN" if settle_dist < R else "LOSS"

    return {"outcome": outcome,
            "inconclusive_reason": None if outcome != "INCONCLUSIVE" else "window_open",
            "trigger_offset": None, "realised_return_pct": round((R - maxexc) / entry * 100, 3),
            "max_adverse_excursion_pct": round(maxexc / entry * 100, 3),
            "R_pct": round(R / entry * 100, 3), "entry_px": entry, "ambiguous_bar": False,
            "window_complete": complete, "nwin": nwin,
            "outcome_settle": outcome_settle,
            "settle_dist_pct": round(settle_dist / entry * 100, 3),
            "pin_rule_divergent": bool(complete and outcome != outcome_settle)}


def spy_benchmark(entry_date, direction, nwin):
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
    if out in ("LOSS", "INCONCLUSIVE_no_threshold"):
        return False
    return None


def main():
    rows = [json.loads(l) for l in open(f"{AUD}/phase_1_inventory.jsonl") if l.strip()]
    out_rows = []
    counts = defaultdict(int)
    for r in rows:
        tk = r["ticker"]; sec = r["section"]; hor = r["horizon"]; tdir = r.get("thesis_direction")
        edate = r["report_date"]
        was_sized = r.get("final_size") in SIZED
        is_pin = (r.get("dominant_signal_class") == "opex_pin") or sec == "opex_pin"
        res = None; mode = None
        directionless = (tdir == "neutral" and not is_pin)
        if directionless:
            res = {"outcome": "NOT_A_TRADE", "inconclusive_reason": "directionless"}; mode = "not_a_trade"
        elif tk not in PX:
            res = {"outcome": "INCONCLUSIVE", "inconclusive_reason": "data_unavailable"}; mode = "no_px"
        else:
            bars = PX[tk]; ei = entry_idx(bars, edate)
            if ei is None:
                res = {"outcome": "INCONCLUSIVE", "inconclusive_reason": "data_unavailable"}; mode = "no_entry_bar"
            elif is_pin:
                res = resolve_pin(bars, ei); mode = "pin"
            elif tdir in ("vol_long", "vol_short") or sec in ("vol_long", "vol_short"):
                kind = tdir if tdir in ("vol_long", "vol_short") else sec
                res = resolve_vol(bars, ei, kind); mode = "vol"
            elif tdir in ("long", "short"):
                nwin = WIN.get(hor, WIN["swing"])[0]
                res = resolve_directional(bars, ei, tdir, nwin); mode = "directional"
            else:
                if sec == "swing_short":
                    res = resolve_directional(bars, ei, "short", WIN.get(hor, WIN["swing"])[0]); mode = "directional"
                elif sec in ("swing_long", "leap"):
                    res = resolve_directional(bars, ei, "long", WIN.get(hor, WIN["swing"])[0]); mode = "directional"
            if res is None:
                res = {"outcome": "INCONCLUSIVE", "inconclusive_reason": "data_unavailable"}; mode = mode or "unresolved"
        spy_win = None
        if mode == "directional" and tdir in ("long", "short"):
            nwin = WIN.get(hor, WIN["swing"])[0]
            spy_win = spy_benchmark(edate, tdir, nwin)
        if hor == "LEAP" and res.get("outcome") in ("WIN", "LOSS", "INCONCLUSIVE"):
            res["window_open_mtm"] = res.get("realised_return_pct")
            res["outcome"] = "INCONCLUSIVE"
            res["inconclusive_reason"] = "leap_window_open"
        nr = dict(r)
        nr.update(res)
        nr["canonical_class"] = canonical_class(r.get("dominant_signal_class"))
        nr["resolution_mode"] = mode
        nr["entry_date_used"] = edate
        nr["was_sized"] = was_sized
        nr["spy_benchmark_win"] = spy_win
        nr["realized_pnl_pct"] = (res.get("realised_return_pct")
                                  if res.get("outcome") in ("WIN", "LOSS") and mode in ("directional", "vol", "pin")
                                  else None)
        out_rows.append(nr)
        counts[res.get("outcome", "?")] += 1
        counts[f"mode:{mode}"] += 1

    with open(f"{AUD}/phase_2_outcomes.jsonl", "w") as f:
        for r in out_rows:
            f.write(json.dumps(r) + "\n")

    dec = [r for r in out_rows if r["outcome"] in ("WIN", "LOSS")]
    win = sum(1 for r in dec if r["outcome"] == "WIN")
    print(f"rows={len(out_rows)} WIN={win} LOSS={len(dec)-win} decided={len(dec)} "
          f"WR={win/len(dec)*100:.1f}%" if dec else "no decided")
    print("outcomes:", {k: v for k, v in sorted(counts.items()) if not k.startswith('mode:')})
    print("inconclusive reasons:", dict(defaultdict(int, {
        rr: sum(1 for r in out_rows if r.get("inconclusive_reason") == rr)
        for rr in set(r.get("inconclusive_reason") for r in out_rows if r.get("inconclusive_reason"))})))
    print("modes:", {k[5:]: v for k, v in sorted(counts.items()) if k.startswith('mode:')})
    for lab, sub in (("SIZED", [r for r in dec if r["was_sized"]]),
                     ("PAPER(benched)", [r for r in dec if not r["was_sized"]])):
        if sub:
            w = sum(1 for r in sub if r["outcome"] == "WIN")
            print(f"  {lab}: n={len(sub)} WR={w/len(sub)*100:.1f}%")
    for d in ("long", "short", "vol_long", "vol_short"):
        sub = [r for r in dec if r.get("thesis_direction") == d]
        if sub:
            w = sum(1 for r in sub if r["outcome"] == "WIN")
            print(f"  {d}: n={len(sub)} WR={w/len(sub)*100:.1f}%")
    # regime-bucket stratified WR
    print("DECIDED BY REGIME BUCKET:")
    for rb in ("uptrend", "pullback_in_uptrend", "choppy", "transitional_other"):
        sub = [r for r in dec if r.get("regime_bucket") == rb]
        if sub:
            w = sum(1 for r in sub if r["outcome"] == "WIN")
            print(f"  {rb:22} n={len(sub):3} WR={w/len(sub)*100:.1f}%")
    print("POST-FREEZE decided:", len([r for r in dec if r.get("post_freeze")]),
          "| OUT-OF-REGIME decided:", len([r for r in dec if r.get("out_of_regime")]))
    sb = [r for r in out_rows if r.get("spy_benchmark_win") is not None]
    if sb:
        sbw = sum(1 for r in sb if r["spy_benchmark_win"])
        print(f"SPY benchmark resolved on {len(sb)} directional rows; blended base={sbw/len(sb)*100:.1f}%")
        for d in ("long", "short"):
            sub = [r for r in sb if r.get("thesis_direction") == d]
            dd = [x for x in dec if x.get("thesis_direction") == d]
            if sub and dd:
                w = sum(1 for r in sub if r["spy_benchmark_win"])
                bkw = sum(1 for x in dd if x["outcome"] == "WIN")
                print(f"  SPY-{d} base={w/len(sub)*100:.1f}% (n={len(sub)}) vs BOOK-{d}={bkw/len(dd)*100:.1f}% "
                      f"-> excess={bkw/len(dd)*100 - w/len(sub)*100:+.1f}pp")


if __name__ == "__main__":
    main()
