#!/usr/bin/env python3
"""Phase 3d (NEW 2026-07-25) — is the C21 benchmark-excess column measuring EDGE
or is it measuring the SPY base rate?

Motivation. Three consecutive audits (07-11, 07-18, 07-25) have led with "the
benchmark-excess sign is non-stationary": bearish_flow went +29.4pp -> -3.2pp ->
-10.8pp on overlapping data. The standing interpretation was that the underlying
edge is regime-dependent. This phase tests the cheaper alternative:

    H0(artifact): book WR is ~constant across strata; SPY's benchmark WR is what
    moves; therefore excess = bookWR - spyWR is ~ -1 * spyWR + const, and the
    "non-stationarity" is entirely the benchmark's, not the book's.

Mechanism if H0 holds: the resolver is a path-aware FIRST-TOUCH test on each
instrument's OWN 0.5*ATR(14). Single names are more leptokurtic relative to their
own trailing ATR than a diversified index is, so names touch +/-R at a ~coin-flip
rate in almost any tape, while SPY's first-touch rate swings hard with drift.
Excess then mechanically tracks -spyWR.

Test: build every (stratum) cell with n>=8, regress excess on spyWR (OLS, stdlib),
and report slope + R^2 + the dispersion ratio sd(bookWR)/sd(spyWR). Slope ~ -1,
high R^2, and dispersion ratio << 1 all support H0(artifact).
"""
import json, math, statistics

AUD = "analyses/audit/2026-08-01"
SPY = json.load(open(f"{AUD}/_ohlc/SPY.json"))["bars"]
rows = [json.loads(l) for l in open(f"{AUD}/phase_2_outcomes.jsonl")]
dec = [r for r in rows if r["outcome"] in ("WIN", "LOSS")]


def eidx(bars, d):
    idx = None
    for i, x in enumerate(bars):
        if x["date"] == d:
            return i
        if x["date"] < d:
            idx = i
        else:
            break
    return idx


def spyret(d, n):
    i = eidx(SPY, d)
    if i is None:
        return None
    f = SPY[i + 1: i + 1 + n]
    return None if not f else (f[-1]["close"] - SPY[i]["close"]) / SPY[i]["close"] * 100


for r in dec:
    v = spyret(r["report_date"], r.get("nwin") or 10)
    r["_tape"] = None if v is None else ("UP" if v > 0 else "DOWN")

BENCH = [r for r in dec if r.get("spy_benchmark_win") is not None]


def cell(sub):
    if len(sub) < 8:
        return None
    bwr = sum(1 for r in sub if r["outcome"] == "WIN") / len(sub)
    swr = sum(1 for r in sub if r["spy_benchmark_win"]) / len(sub)
    return {"n": len(sub), "book_wr": round(bwr, 3), "spy_wr": round(swr, 3),
            "excess_pp": round((bwr - swr) * 100, 1)}


cells = {}
# a. direction x tape
for tape in ("UP", "DOWN"):
    for d in ("long", "short"):
        c = cell([r for r in BENCH if r["_tape"] == tape and r.get("thesis_direction") == d])
        if c: cells[f"tape={tape}/{d}"] = c
# b. regime bucket x direction
for rb in ("uptrend", "pullback_in_uptrend", "choppy", "transitional_other"):
    for d in ("long", "short"):
        c = cell([r for r in BENCH if r.get("regime_bucket") == rb and r.get("thesis_direction") == d])
        if c: cells[f"regime={rb}/{d}"] = c
# c. canonical class
for cl in sorted({r.get("canonical_class") for r in BENCH}):
    c = cell([r for r in BENCH if r.get("canonical_class") == cl])
    if c: cells[f"class={cl}"] = c
# d. class x tape (the cells the last 3 audits actually quoted)
for cl in ("bearish_flow", "bullish_flow", "dark_pool_accumulation", "multileg_directional"):
    for tape in ("UP", "DOWN"):
        c = cell([r for r in BENCH if r.get("canonical_class") == cl and r["_tape"] == tape])
        if c: cells[f"class={cl}/tape={tape}"] = c
# e. tier
for t in ("LOW", "MEDIUM", "DROP"):
    c = cell([r for r in BENCH if r["tier"] == t])
    if c: cells[f"tier={t}"] = c
# f. rubric era
for e in ("era_0525_0529", "era_0530_0605", "pre_freeze_post_0606", "2026-06-12"):
    c = cell([r for r in BENCH if r["rubric_era"] == e])
    if c: cells[f"era={e}"] = c

xs = [c["spy_wr"] for c in cells.values()]
ys = [c["excess_pp"] for c in cells.values()]
bs = [c["book_wr"] for c in cells.values()]
n = len(xs)
mx, my = statistics.mean(xs), statistics.mean(ys)
sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
sxx = sum((x - mx) ** 2 for x in xs)
slope = sxy / sxx
intercept = my - slope * mx
ss_res = sum((y - (intercept + slope * x)) ** 2 for x, y in zip(xs, ys))
ss_tot = sum((y - my) ** 2 for y in ys)
r2 = 1 - ss_res / ss_tot
sd_book, sd_spy = statistics.pstdev(bs), statistics.pstdev(xs)

print(f"=== EXCESS-vs-SPY-BASE REGRESSION over {n} strata cells (n>=8 each) ===")
print(f"{'cell':44} {'n':>4} {'bookWR':>7} {'spyWR':>7} {'excess':>8}")
for k, c in sorted(cells.items(), key=lambda kv: kv[1]["spy_wr"]):
    print(f"{k:44} {c['n']:4} {c['book_wr']:7} {c['spy_wr']:7} {c['excess_pp']:+8}pp")

print(f"\nOLS  excess_pp = {intercept:+.1f} + ({slope:+.1f}) * spy_wr")
print(f"     slope (pp per 1.00 of spyWR) = {slope:+.1f}   [-100 == pure artifact]")
print(f"     R^2 = {r2:.3f}")
print(f"     sd(bookWR) = {sd_book:.4f}   sd(spyWR) = {sd_spy:.4f}   "
      f"dispersion ratio = {sd_book/sd_spy:.3f}  [<<1 == book is pinned, benchmark moves]")
print(f"     book WR range = [{min(bs):.3f}, {max(bs):.3f}]  spread={max(bs)-min(bs):.3f}")
print(f"     spy  WR range = [{min(xs):.3f}, {max(xs):.3f}]  spread={max(xs)-min(xs):.3f}")

# variance decomposition of excess
var_ex = statistics.pvariance(ys)
var_book_pp = statistics.pvariance([b * 100 for b in bs])
var_spy_pp = statistics.pvariance([x * 100 for x in xs])
print(f"\nVARIANCE DECOMPOSITION of excess (pp^2): var(excess)={var_ex:.1f} "
      f"var(bookWR)={var_book_pp:.1f} var(spyWR)={var_spy_pp:.1f}")
print(f"     share of excess variance attributable to the BENCHMARK moving = "
      f"{var_spy_pp/(var_spy_pp+var_book_pp)*100:.1f}%")

# the leptokurtosis mechanism: first-touch rate of names vs SPY
tot = len(BENCH)
name_decided = tot
spy_dec = sum(1 for r in BENCH if r["spy_benchmark_win"] is not None)
print(f"\nMECHANISM CHECK — first-touch |outcome| dispersion:")
print(f"  book WR across cells stays within {max(bs)-min(bs):.3f} while the SPY benchmark "
      f"ranges {max(xs)-min(xs):.3f} — names regress to ~coin-flip on their own ATR.")

json.dump({"cells": cells, "slope_pp_per_spywr": round(slope, 1), "intercept": round(intercept, 1),
           "r2": round(r2, 3), "sd_book_wr": round(sd_book, 4), "sd_spy_wr": round(sd_spy, 4),
           "dispersion_ratio": round(sd_book / sd_spy, 3),
           "benchmark_share_of_excess_variance_pct": round(var_spy_pp / (var_spy_pp + var_book_pp) * 100, 1),
           "n_cells": n},
          open(f"{AUD}/phase_3d_excess_artifact.jsonl", "w"), indent=1)
print("\nwrote phase_3d_excess_artifact.jsonl")
