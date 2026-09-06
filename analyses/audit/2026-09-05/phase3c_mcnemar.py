#!/usr/bin/env python3
"""Phase 3c (C49 PRIMARY EDGE TEST) — paired McNemar, row-matched book vs same-window SPY.

C49 (2026-07-25 method register) demotes raw benchmark-excess to a secondary annotated
column and promotes (a) tape-conditioned book WR and (b) paired McNemar to the primary
edge test. McNemar is correct precisely because it is row-matched: each row carries its
own outcome AND its own same-window SPY outcome, so the benchmark cancels pairwise
instead of entering as a stratum-level denominator.

Also emits the C49 header requirements: the table-level dispersion ratio
sd(bookWR)/sd(benchWR) and the OLS of excess_pp on spy_wr (slope, R^2).
"""
import json
import math
import statistics
from collections import defaultdict

AUD = "analyses/audit/2026-09-05"

rows = [json.loads(l) for l in open(f"{AUD}/phase_2_outcomes.jsonl")]
dec = [r for r in rows if r.get("outcome") in ("WIN", "LOSS")
       and r.get("spy_benchmark_win") is not None]

# --- tape derivation (same rule as phase3c_tape.py: SPY close-to-close over the row's own window)
SPYB = json.load(open(f"{AUD}/_ohlc/SPY.json"))["bars"]


def _entry_idx(bars, date):
    idx = None
    for i, b in enumerate(bars):
        if b["date"] == date:
            return i
        if b["date"] < date:
            idx = i
        else:
            break
    return idx


def _spy_window_ret(date, nwin):
    ei = _entry_idx(SPYB, date)
    if ei is None:
        return None
    fwd = SPYB[ei + 1: ei + 1 + nwin]
    if not fwd:
        return None
    return (fwd[-1]["close"] - SPYB[ei]["close"]) / SPYB[ei]["close"] * 100


for _r in dec:
    _ret = _spy_window_ret(_r["report_date"], _r.get("nwin") or 10)
    _r["tape"] = None if _ret is None else ("UP" if _ret > 0 else "DOWN")
    _r["direction"] = _r.get("thesis_direction")


def binom_two_sided(b, c):
    """Exact McNemar: two-sided binomial on discordant pairs, p=0.5."""
    n = b + c
    if n == 0:
        return 1.0
    k = min(b, c)
    tail = sum(math.comb(n, i) for i in range(0, k + 1)) / (2 ** n)
    return min(1.0, 2 * tail)


def mcnemar(subset):
    """b = book wins where SPY lost; c = SPY won where book lost."""
    b = sum(1 for r in subset if r["outcome"] == "WIN" and not r["spy_benchmark_win"])
    c = sum(1 for r in subset if r["outcome"] == "LOSS" and r["spy_benchmark_win"])
    n = b + c
    stat = ((abs(b - c) - 1) ** 2) / n if n else 0.0
    return b, c, stat, binom_two_sided(b, c)


def bh(pvals, q=0.10):
    idx = sorted(range(len(pvals)), key=lambda i: pvals[i])
    m = len(pvals)
    out = [False] * m
    kmax = -1
    for rank, i in enumerate(idx, start=1):
        if pvals[i] <= q * rank / m:
            kmax = rank
    for rank, i in enumerate(idx, start=1):
        if rank <= kmax:
            out[i] = True
    return out


def wr(subset):
    n = len(subset)
    return (sum(1 for r in subset if r["outcome"] == "WIN") / n if n else None), n


# ---------- cell construction ----------
cells = []


def add(label, subset, minn=8):
    if len(subset) < minn:
        return
    b, c, stat, p = mcnemar(subset)
    w, n = wr(subset)
    spyw = sum(1 for r in subset if r["spy_benchmark_win"]) / n
    cells.append({"cell": label, "n": n, "book_wr": round(w, 3),
                  "spy_wr": round(spyw, 3), "excess_pp": round((w - spyw) * 100, 1),
                  "discordant_b": b, "discordant_c": c,
                  "mcnemar_stat": round(stat, 3), "mcnemar_p": round(p, 4)})


def tape(r):
    return r.get("tape")


DIRS = {"long": ["long"], "short": ["short"]}

add("ALL", dec)
for d, vals in DIRS.items():
    add(f"ALL / {d}", [r for r in dec if r.get("direction") in vals])
for t in ("UP", "DOWN"):
    add(f"{t} / all", [r for r in dec if tape(r) == t])
    for d, vals in DIRS.items():
        add(f"{t} / {d}", [r for r in dec if tape(r) == t and r.get("direction") in vals])

# canonical classes with n>=8, overall and per tape
cls_n = defaultdict(int)
for r in dec:
    cls_n[r.get("canonical_class")] += 1
for cl, n in sorted(cls_n.items(), key=lambda kv: -kv[1]):
    if not cl or n < 8:
        continue
    add(f"CLASS {cl}", [r for r in dec if r.get("canonical_class") == cl])
    for t in ("UP", "DOWN"):
        add(f"CLASS {cl} / {t}", [r for r in dec if r.get("canonical_class") == cl and tape(r) == t])

# post-freeze slices
pf = [r for r in dec if r.get("post_freeze")]
add("POST-FREEZE / all", pf)
for d, vals in DIRS.items():
    add(f"POST-FREEZE / {d}", [r for r in pf if r.get("direction") in vals])

# BH is applied WITHIN families. Pooling a pre-registered 7-cell primary family with a
# 28-cell exploratory class sweep mechanically destroys the primary finding (the 2026-07-25
# audit ran BH on the primary family only; expanding the family is not a new result).
PRIMARY = {"ALL", "ALL / long", "ALL / short",
           "UP / long", "UP / short", "DOWN / long", "DOWN / short"}
for c in cells:
    c["family"] = "primary" if c["cell"] in PRIMARY else "exploratory"
for fam in ("primary", "exploratory"):
    sub = [c for c in cells if c["family"] == fam]
    for c, f in zip(sub, bh([x["mcnemar_p"] for x in sub])):
        c["bh_significant"] = bool(f)

print("=== C49 PRIMARY EDGE TEST — paired McNemar (row-matched book vs same-window SPY) ===")
print("BH applied WITHIN family: primary = 7 pre-registered direction x tape cells;")
print("exploratory = per-class sweep. (Family pooling would be a post-hoc power tax.)")
print(f"{'cell':<34}{'n':>5}{'bookWR':>8}{'spyWR':>7}{'exc':>7}{'b':>5}{'c':>5}{'p':>9}  BH  fam")
for c in sorted(cells, key=lambda x: x["mcnemar_p"]):
    print(f"{c['cell']:<34}{c['n']:>5}{c['book_wr']:>8}{c['spy_wr']:>7}"
          f"{c['excess_pp']:>7}{c['discordant_b']:>5}{c['discordant_c']:>5}"
          f"{c['mcnemar_p']:>9.4f}  {'YES' if c['bh_significant'] else 'no':<3} {c['family'][:4]}")

# ---------- C49 header stats: dispersion ratio + OLS of excess on spy_wr ----------
strata = [c for c in cells if c["n"] >= 8 and not c["cell"].startswith("ALL")]
bwr = [c["book_wr"] for c in strata]
swr = [c["spy_wr"] for c in strata]
exc = [c["excess_pp"] for c in strata]
sd_b, sd_s = statistics.pstdev(bwr), statistics.pstdev(swr)
disp = sd_b / sd_s if sd_s else None

mx, my = statistics.mean(swr), statistics.mean(exc)
sxx = sum((x - mx) ** 2 for x in swr)
sxy = sum((x - mx) * (y - my) for x, y in zip(swr, exc))
slope = sxy / sxx if sxx else 0.0
icept = my - slope * mx
ss_tot = sum((y - my) ** 2 for y in exc)
ss_res = sum((y - (icept + slope * x)) ** 2 for x, y in zip(swr, exc))
r2 = 1 - ss_res / ss_tot if ss_tot else 0.0
# slope is in pp per unit spy_wr; pure artifact = -100
beta_book = 1 + slope / 100

print("\n=== C49 HEADER STATS (print BEFORE any class commentary) ===")
print(f"strata cells (n>=8): {len(strata)}")
print(f"sd(bookWR)={sd_b:.4f}  sd(benchWR)={sd_s:.4f}  DISPERSION RATIO={disp:.3f}")
print(f"OLS excess_pp = {icept:+.1f} {slope:+.1f} x spy_wr   R^2={r2:.3f}")
print(f"implied beta(bookWR|spyWR) = {beta_book:+.2f}   "
      f"benchmark share of excess variance = {abs(slope)/100*0 + r2*100:.1f}% (R^2)")

json.dump({"cells": cells,
           "dispersion_ratio": disp, "sd_book": sd_b, "sd_bench": sd_s,
           "ols_slope": slope, "ols_intercept": icept, "ols_r2": r2,
           "beta_book_given_spy": beta_book, "n_strata": len(strata)},
          open(f"{AUD}/phase_3c_mcnemar.jsonl", "w"), indent=1)
print("\nwrote phase_3c_mcnemar.jsonl")
