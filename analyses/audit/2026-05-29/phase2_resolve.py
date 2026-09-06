#!/usr/bin/env python3
"""Phase 2 outcome resolution — close-to-close path-aware WIN/LOSS/INCONCLUSIVE.

DATA LIMITATION (documented): the yfinance MCP exposes CLOSE prices only — no
intraday high/low. So path-awareness is resolved on a close-to-close basis (an
adverse EOD close hitting -1R before a favorable EOD close hitting +1R = LOSS).
Intraday wicks are invisible; this is a faithful substitute, not a silent
extrapolation. R = 0.5 * ATR_proxy, where ATR_proxy = mean |close_t - close_{t-1}|
over the 14 bars preceding entry (a close-range analogue of ATR(14)).

Windows (trading days after entry close):
  0DTE   -> next session (+1)            [report is EOD; its 0DTE play targets next session]
  swing  -> 3 AND 10
  weekly -> 5 AND 10                     [entry = Friday close of the iso-week]
  LEAP   -> 30 AND 90

Vol trades (vol_long/vol_short): resolved against realized-vol DIRECTION (no
implied_move in legacy data, so true IV-vs-RV is impossible). vol_long WIN if
window realized vol > entry trailing vol; vol_short WIN if it contracted.
"""
import json
import datetime
import collections
from pathlib import Path

AUDIT = Path("analyses/audit/2026-05-29")
PX = AUDIT / "_px"
LAST_BAR = "2026-05-28"  # last available close in the price files

WIN, LOSS, INC, NA = "WIN", "LOSS", "INCONCLUSIVE", "NOT_A_TRADE"

WINDOWS = {
    "0DTE": [1],
    "swing": [3, 10],
    "weekly": [5, 10],
    "LEAP": [30, 90],
    "vol": [10],
}


def load_px(ticker):
    f = PX / f"{ticker}.json"
    if not f.exists():
        return None
    d = json.load(open(f))
    bars = d.get("bars", [])
    series = {}
    for b in bars:
        c = b.get("close")
        if c is not None:
            series[b["date"]] = float(c)
    return series if series else None


def iso_friday(rd):
    wk = int(rd.split("W")[1])
    return datetime.date.fromisocalendar(2026, wk, 5).isoformat()


def entry_date(row):
    rd = row["report_date"]
    if str(rd).startswith("2026-W"):
        return iso_friday(rd)
    return rd


def trading_dates(series):
    return sorted(series.keys())


def idx_on_or_after(dates, d):
    for i, x in enumerate(dates):
        if x >= d:
            return i
    return None


def atr_proxy(dates, series, entry_i):
    """mean |close_t - close_{t-1}| over up to 14 bars before entry."""
    diffs = []
    for j in range(max(1, entry_i - 14), entry_i + 1):
        if j >= 1 and j < len(dates):
            diffs.append(abs(series[dates[j]] - series[dates[j - 1]]))
    if not diffs:
        return None
    return sum(diffs) / len(diffs)


def resolve_window(dates, series, entry_i, entry_px, direction, n, R):
    """Path-aware close-to-close over n trading days. Returns (outcome, end_ret_pct, mae_pct, truncated)."""
    end_i = entry_i + n
    # A window only resolves if its FULL n trading days are available. Grading a
    # 30/90D LEAP thesis on a truncated 20-day stub would violate the path
    # definition, so an incomplete window is window_open (INCONCLUSIVE), never a
    # truncated WIN/LOSS. (Allow a 1-bar shortfall: last available bar is 05-28,
    # the 05-29 close is simply absent from the source.)
    if end_i > len(dates) - 1:
        if end_i == len(dates):  # exactly one bar short (missing 05-29) -> use last bar
            end_i = len(dates) - 1
        else:
            return ("OPEN", None, None, "window_open")
    if end_i <= entry_i:
        return ("OPEN", None, None, "window_open")
    sign = 1.0 if direction in ("long",) else -1.0  # short profits when price falls
    fav_hit = None
    adv_hit = None
    mae = 0.0  # max adverse excursion (in R, signed favorable convention)
    for i in range(entry_i + 1, end_i + 1):
        move = (series[dates[i]] - entry_px) * sign  # favorable if >0
        adverse = -move
        if adverse > mae:
            mae = adverse
        if move >= R and fav_hit is None:
            fav_hit = i
        if adverse >= R and adv_hit is None:
            adv_hit = i
        if fav_hit and adv_hit:
            break
    end_move = (series[dates[end_i]] - entry_px) * sign
    end_ret_pct = (series[dates[end_i]] - entry_px) / entry_px * 100.0 * sign
    mae_pct = -mae / entry_px * 100.0
    # path-aware: which threshold hit first
    if fav_hit and (adv_hit is None or fav_hit <= adv_hit):
        oc = WIN
    elif adv_hit and (fav_hit is None or adv_hit < fav_hit):
        oc = LOSS
    else:
        oc = None  # neither threshold
    return (oc, round(end_ret_pct, 2), round(mae_pct, 2), None)


def combine(short_o, long_o):
    """swing/weekly: short AND long window. disagreement = INC unless long decisive."""
    if short_o == long_o:
        return short_o if short_o in (WIN, LOSS) else INC
    # one is None (no threshold) or they conflict
    if long_o in (WIN, LOSS):
        if short_o in (WIN, LOSS) and short_o != long_o:
            return INC  # genuine conflict
        return long_o  # long decisive, short neutral
    if short_o in (WIN, LOSS) and long_o is None:
        return INC  # only short fired, long neutral -> not decisive
    return INC


def realized_vol(dates, series, i0, i1):
    rets = []
    for i in range(i0 + 1, i1 + 1):
        if i < len(dates):
            rets.append((series[dates[i]] - series[dates[i - 1]]) / series[dates[i - 1]])
    if len(rets) < 2:
        return None
    m = sum(rets) / len(rets)
    var = sum((r - m) ** 2 for r in rets) / (len(rets) - 1)
    return var ** 0.5


def is_trade(r):
    if r.get("section") in ("watch_only", "leap_disqualified"):
        return False
    if r.get("tier") == "DROP":
        return False
    fs = (r.get("final_size") or r.get("pre_risk_size") or "")
    if str(fs).lower() in ("skip", "watch_only", "none", "drop", ""):
        if r.get("final_size") is None and r.get("pre_risk_size") is None:
            return True
        return False
    return True


def main():
    rows = [json.loads(l) for l in open(AUDIT / "phase_1_inventory.jsonl")]
    out_rows = []
    counts = collections.Counter()
    for r in rows:
        r = dict(r)
        if not is_trade(r):
            r["outcome"] = NA
            r["inconclusive_reason"] = "not_a_trade"
            out_rows.append(r)
            counts[NA] += 1
            continue
        tk = r["ticker_base"]
        series = load_px(tk)
        ed = entry_date(r)
        horizon = r.get("horizon") or "swing"
        direction = r.get("thesis_direction") or "long"
        is_vol = horizon == "vol" or direction in ("vol_long", "vol_short")
        if series is None:
            r["outcome"] = INC
            r["inconclusive_reason"] = "data_unavailable"
            out_rows.append(r)
            counts[INC] += 1
            continue
        dates = trading_dates(series)
        entry_i = idx_on_or_after(dates, ed)
        if entry_i is None or entry_i >= len(dates) - 1:
            r["outcome"] = INC
            r["inconclusive_reason"] = "window_open"
            out_rows.append(r)
            counts[INC] += 1
            continue
        entry_px = series[dates[entry_i]]
        r["entry_resolved_date"] = dates[entry_i]
        r["entry_px"] = round(entry_px, 4)

        Rraw = atr_proxy(dates, series, entry_i)
        is_0dte = horizon == "0DTE"
        is_pin = r.get("section") == "opex_pin"

        # 0DTE / OPEX-pin: absolute-move test vs R over a short window
        # (next session for 0DTE; up to 5 sessions to OPEX for a pin). A short-vol /
        # pin trade WINs when price STAYS within +/-R; a long-gamma 0DTE WINs on a
        # >=R break. Directional 0DTE (dir long/short) falls through to the
        # directional path below.
        if (is_0dte or is_pin) and (is_vol or direction in ("vol_long", "vol_short")):
            if not Rraw or Rraw <= 0:
                r["outcome"] = INC; r["inconclusive_reason"] = "no_atr"
                out_rows.append(r); counts[INC] += 1; continue
            R = 0.5 * Rraw
            nwin = 1 if is_0dte else 5
            end_i = entry_i + nwin
            if end_i > len(dates) - 1:
                end_i = len(dates) - 1
            if end_i <= entry_i:
                r["outcome"] = INC; r["inconclusive_reason"] = "window_open"
                out_rows.append(r); counts[INC] += 1; continue
            max_abs = max(abs(series[dates[i]] - entry_px) for i in range(entry_i + 1, end_i + 1))
            short_vol = direction == "vol_short" or r.get("section") in ("opex_pin", "vol_short")
            stayed = max_abs < R
            r["abs_move_dollar"] = round(max_abs, 4)
            r["R_dollar"] = round(R, 4)
            r["outcome"] = WIN if (stayed == short_vol) else LOSS
            r["outcome_window"] = f"{'0DTE next-session' if is_0dte else 'pin 5D'} abs-move vs R"
            r["realised_return_pct"] = round(max_abs / entry_px * 100, 2)
            out_rows.append(r); counts[r["outcome"]] += 1; continue

        if is_vol:
            # realized-vol direction proxy over 10 trading days vs trailing 14d
            end_i = min(entry_i + 10, len(dates) - 1)
            if end_i <= entry_i + 2:
                r["outcome"] = INC
                r["inconclusive_reason"] = "window_open"
                out_rows.append(r); counts[INC] += 1; continue
            rv_win = realized_vol(dates, series, entry_i, end_i)
            rv_entry = realized_vol(dates, series, max(0, entry_i - 14), entry_i)
            r["rv_window"] = round(rv_win, 5) if rv_win else None
            r["rv_entry_trailing"] = round(rv_entry, 5) if rv_entry else None
            if rv_win is None or rv_entry is None:
                r["outcome"] = INC; r["inconclusive_reason"] = "data_unavailable"
            else:
                vl = direction == "vol_long" or r.get("section") == "vol_long"
                if vl:
                    r["outcome"] = WIN if rv_win > rv_entry else LOSS
                else:
                    r["outcome"] = WIN if rv_win < rv_entry else LOSS
                r["outcome_window"] = "10D realized-vol direction (proxy; no implied_move)"
                r["realised_return_pct"] = round((rv_win - rv_entry) / rv_entry * 100, 2)
            out_rows.append(r); counts[r["outcome"]] += 1; continue

        # directional
        R = atr_proxy(dates, series, entry_i)
        if not R or R <= 0:
            r["outcome"] = INC; r["inconclusive_reason"] = "no_atr"
            out_rows.append(r); counts[INC] += 1; continue
        R = 0.5 * R
        r["R_dollar"] = round(R, 4)
        wins = WINDOWS.get(horizon, [3, 10])
        per = []
        for n in wins:
            oc, endret, mae, note = resolve_window(dates, series, entry_i, entry_px, direction, n, R)
            per.append({"n": n, "outcome": oc, "end_ret_pct": endret, "mae_pct": mae, "note": note})
        r["window_detail"] = per
        # combine — "OPEN" means that window's full horizon isn't available yet
        if len(per) == 1:
            o = per[0]["outcome"]
            if o == "OPEN":
                final, reason = INC, "window_open"
            elif o in (WIN, LOSS):
                final, reason = o, None
            else:
                final, reason = INC, "no_threshold"
        else:
            short_o, long_o = per[0]["outcome"], per[1]["outcome"]
            if short_o == "OPEN" and long_o == "OPEN":
                final, reason = INC, "window_open"
            elif long_o == "OPEN":
                # only the short window is available -> resolve on it if decisive
                final = short_o if short_o in (WIN, LOSS) else INC
                reason = "long_window_open" if final == INC else "short_window_only"
            elif short_o == "OPEN":
                final = long_o if long_o in (WIN, LOSS) else INC
                reason = None if final in (WIN, LOSS) else "no_threshold"
            else:
                final = combine(short_o, long_o)
                reason = None if final in (WIN, LOSS) else "window_disagreement_or_neutral"
        r["outcome"] = final
        if reason:
            r["inconclusive_reason"] = reason
        # report stats from the longest COMPLETED window
        completed = [p for p in per if p["end_ret_pct"] is not None]
        if completed:
            r["realised_return_pct"] = completed[-1]["end_ret_pct"]
            r["max_adverse_excursion_pct"] = completed[-1]["mae_pct"]
        r["outcome_window"] = f"{horizon}:{wins}"
        out_rows.append(r)
        counts[final] += 1

    with open(AUDIT / "phase_2_outcomes.jsonl", "w") as f:
        for r in out_rows:
            f.write(json.dumps(r) + "\n")

    print(json.dumps(dict(counts), indent=1))
    # breakdown among trades only
    trades = [r for r in out_rows if r["outcome"] != NA]
    decided = [r for r in trades if r["outcome"] in (WIN, LOSS)]
    print(f"\ntrades={len(trades)} decided(WIN+LOSS)={len(decided)} "
          f"win_rate={sum(1 for r in decided if r['outcome']==WIN)/len(decided)*100:.1f}%" if decided else "no decided")
    # inconclusive reasons
    inc_reasons = collections.Counter(r.get("inconclusive_reason") for r in trades if r["outcome"] == INC)
    print("INC reasons:", dict(inc_reasons))
    # by horizon
    for h in ["0DTE", "swing", "weekly", "LEAP", "vol"]:
        hs = [r for r in trades if (r.get("horizon") == h or (h == "vol" and (r.get("thesis_direction") in ("vol_long", "vol_short"))))]
        dec = [r for r in hs if r["outcome"] in (WIN, LOSS)]
        wr = (sum(1 for r in dec if r["outcome"] == WIN) / len(dec) * 100) if dec else None
        print(f"  {h:7} n={len(hs):3} decided={len(dec):3} wr={wr if wr is None else round(wr,1)}")


if __name__ == "__main__":
    main()
