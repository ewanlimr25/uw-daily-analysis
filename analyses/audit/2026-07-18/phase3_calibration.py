#!/usr/bin/env python3
"""Phase 3 — Calibration Audit. Uses repo helpers for market_excess + Kelly gate.
Stdlib binomial two-sided test + Benjamini-Hochberg FDR (C23). No scipy."""
import json, math, sys, statistics
sys.path.insert(0, "scripts")
from excess_winrate import market_excess  # noqa
from kelly_sizing import (payoff_ratio, expectancy, capped_half_kelly,  # noqa
                          tier_expectancy_monotone, ClosedCall)

AUD = "analyses/audit/2026-07-18"
rows = [json.loads(l) for l in open(f"{AUD}/phase_2_outcomes.jsonl")]
dec = [r for r in rows if r["outcome"] in ("WIN", "LOSS")]


def binom_cdf(k, n, p):
    return sum(math.comb(n, i) * p**i * (1 - p)**(n - i) for i in range(0, k + 1))


def binom_two_sided(wins, n, p0):
    """Two-sided binomial p via doubling the smaller tail (clamped to 1)."""
    if n == 0:
        return 1.0
    p0 = min(max(p0, 1e-6), 1 - 1e-6)
    lower = binom_cdf(wins, n, p0)
    upper = 1 - binom_cdf(wins - 1, n, p0)
    return min(1.0, 2 * min(lower, upper))


def benjamini_hochberg(pvals, fdr=0.10):
    """Return set of indices that survive BH at the given FDR."""
    idx = sorted(range(len(pvals)), key=lambda i: pvals[i])
    m = len(pvals)
    survive = set()
    kmax = -1
    for rank, i in enumerate(idx, start=1):
        if pvals[i] <= rank / m * fdr:
            kmax = rank
    for rank, i in enumerate(idx, start=1):
        if rank <= kmax:
            survive.add(i)
    return survive


def wr(sub):
    w = sum(1 for r in sub if r["outcome"] == "WIN")
    return w, len(sub), (w / len(sub) if sub else None)


# ---------- 1. per-canonical-class table ----------
classes = {}
for r in dec:
    classes.setdefault(r["canonical_class"], []).append(r)

class_rows = []
pvals = []
for c, sub in classes.items():
    w, n, realised = wr(sub)
    if n < 8:
        continue  # headline floor (C23); 5-7 go to appendix
    claimed_vals = [r["claimed_win_rate"] for r in sub if r["claimed_win_rate"] is not None]
    claimed = statistics.mean(claimed_vals) if claimed_vals else None
    # SPY benchmark WR over this class's directional rows
    sb = [r for r in sub if r.get("spy_benchmark_win") is not None]
    spy_wr = (sum(1 for r in sb if r["spy_benchmark_win"]) / len(sb)) if sb else None
    excess = market_excess(realised, spy_wr) if spy_wr is not None else None
    p = binom_two_sided(w, n, claimed) if claimed is not None else None
    class_rows.append({"class": c, "n": n, "realised_wr": round(realised, 3),
                       "claimed_wr": round(claimed, 3) if claimed else None,
                       "divergence_pp": round((claimed - realised) * 100, 1) if claimed else None,
                       "spy_benchmark_wr": round(spy_wr, 3) if spy_wr is not None else None,
                       "realised_excess_pp": round(excess * 100, 1) if excess is not None else None,
                       "spy_n": len(sb), "p_raw": p})
    if p is not None:
        pvals.append(p)

# BH across classes with a p-value
pidx = [i for i, cr in enumerate(class_rows) if cr["p_raw"] is not None]
survive = benjamini_hochberg([class_rows[i]["p_raw"] for i in pidx], fdr=0.10)
for j, i in enumerate(pidx):
    class_rows[i]["bh_survives"] = (j in survive)

# appendix thin-N classes (5-7)
thin = []
for c, sub in classes.items():
    w, n, realised = wr(sub)
    if 5 <= n < 8:
        thin.append({"class": c, "n": n, "realised_wr": round(realised, 3)})

# ---------- 2. per-tier reliability ----------
tier_tbl = {}
for t in ["HIGH", "MEDIUM", "LOW", "DROP"]:
    sub = [r for r in dec if r["tier"] == t]
    w, n, realised = wr(sub)
    tier_tbl[t] = {"n": n, "wr": round(realised, 3) if realised is not None else None}

# per-era tier reliability (inversion persistence)
era_tier = {}
for era in ["era_0525_0529", "era_0530_0605", "pre_freeze_post_0606", "2026-06-12"]:
    era_tier[era] = {}
    for t in ["HIGH", "MEDIUM", "LOW", "DROP"]:
        sub = [r for r in dec if r["rubric_era"] == era and r["tier"] == t]
        w, n, realised = wr(sub)
        era_tier[era][t] = {"n": n, "wr": round(realised, 3) if realised is not None else None}

# ---------- 3. Brier + reliability deciles + log-loss ----------
graded = [r for r in dec if r["claimed_win_rate"] is not None]
def y(r): return 1 if r["outcome"] == "WIN" else 0
brier = statistics.mean([(r["claimed_win_rate"] - y(r))**2 for r in graded]) if graded else None
def clamp(p): return min(max(p, 0.01), 0.99)
logloss = -statistics.mean([y(r)*math.log(clamp(r["claimed_win_rate"])) +
                            (1-y(r))*math.log(1-clamp(r["claimed_win_rate"])) for r in graded]) if graded else None
# reliability deciles
edges = [0.0, 0.50, 0.55, 0.60, 0.65, 0.70, 0.80, 0.90, 1.01]
deciles = []
for lo, hi in zip(edges, edges[1:]):
    bucket = [r for r in graded if lo <= r["claimed_win_rate"] < hi]
    if bucket:
        pred = statistics.mean([r["claimed_win_rate"] for r in bucket])
        hit = statistics.mean([y(r) for r in bucket])
        deciles.append({"range": f"[{lo:.2f},{hi:.2f})", "n": len(bucket),
                        "pred_mean": round(pred, 3), "realised_hit": round(hit, 3)})

# ---------- 4. conviction-vs-outcome by raw_score ----------
score_tbl = {}
for s in sorted(set(r["raw_score"] for r in dec if r["raw_score"] is not None)):
    sub = [r for r in dec if r["raw_score"] == s]
    w, n, realised = wr(sub)
    score_tbl[s] = {"n": n, "wr": round(realised, 3) if realised else 0.0}

# ---------- 5. expectancy + Kelly gate ----------
# closed calls = sized decided (the live-sizing population). tier in HIGH/MED/LOW only.
closed = [ClosedCall(tier=r["tier"], realized_pnl_pct=r["realized_pnl_pct"], won=(r["outcome"]=="WIN"))
          for r in dec if r["was_sized"] and r["realized_pnl_pct"] is not None and r["tier"] in ("HIGH","MEDIUM","LOW")]
gate = tier_expectancy_monotone(closed)
# per-tier expectancy on PAPER (all decided) for colour
tier_exp = {}
for t in ["HIGH", "MEDIUM", "LOW", "DROP"]:
    pnl = [r["realised_return_pct"] for r in dec if r["tier"] == t and r["realised_return_pct"] is not None]
    wins = [p for p in pnl if p > 0]; losses = [p for p in pnl if p <= 0]
    pr = payoff_ratio(statistics.mean(wins), statistics.mean(losses)) if wins and losses else None
    wsub = [r for r in dec if r["tier"] == t]
    _, _, rwr = wr(wsub)
    tier_exp[t] = {"mean_pnl": round(statistics.mean(pnl), 3) if pnl else None,
                   "payoff_ratio": round(pr, 3) if pr else None,
                   "half_kelly": round(capped_half_kelly(rwr, pr), 4) if (rwr is not None and pr) else None,
                   "n": len(pnl)}

out = {"class_table": class_rows, "thin_n_appendix": thin, "tier_reliability": tier_tbl,
       "era_tier_reliability": era_tier, "brier": round(brier, 4) if brier else None,
       "log_loss": round(logloss, 4) if logloss else None, "reliability_deciles": deciles,
       "score_table": {str(k): v for k, v in score_tbl.items()},
       "kelly_gate": gate, "tier_expectancy": tier_exp, "graded_n": len(graded)}
json.dump(out, open(f"{AUD}/phase_3_calibration.jsonl", "w"), indent=1)

# ---- print ----
print("=== CLASS TABLE (decided>=8) ===")
print(f"{'class':24} {'n':>3} {'real':>5} {'claim':>5} {'div':>6} {'spyWR':>6} {'excess':>7} {'p':>6} BH")
for cr in sorted(class_rows, key=lambda x: x["n"], reverse=True):
    print(f"{cr['class']:24} {cr['n']:3} {cr['realised_wr']:.2f}  "
          f"{(cr['claimed_wr'] or 0):.2f}  {str(cr['divergence_pp']):>5}  "
          f"{str(cr['spy_benchmark_wr']):>5}  {str(cr['realised_excess_pp']):>6}  "
          f"{(cr['p_raw'] or 1):.3f}  {'Y' if cr.get('bh_survives') else 'n'}")
print("\nthin-N appendix (5-7):", thin)
print("\n=== TIER RELIABILITY ===", tier_tbl)
print("=== ERA x TIER (inversion persistence) ===")
for era, tt in era_tier.items():
    print(f"  {era:22}", {t: f"{v['wr']}({v['n']})" if v['wr'] is not None else f"-({v['n']})" for t, v in tt.items()})
print(f"\nBRIER={out['brier']}  LOG-LOSS={out['log_loss']}  graded_n={len(graded)}")
print("RELIABILITY DECILES:")
for d in deciles:
    print(f"  {d['range']:14} n={d['n']:3} pred={d['pred_mean']:.2f} realised={d['realised_hit']:.2f}")
print("\nSCORE -> WR:", {k: f"{v['wr']:.2f}(n{v['n']})" for k, v in score_tbl.items()})
print("\nKELLY GATE:", gate["status"], "|", gate["reason"])
print("TIER EXPECTANCY (paper):")
for t, v in tier_exp.items():
    print(f"  {t:7} mean_pnl={v['mean_pnl']} payoff={v['payoff_ratio']} half_kelly={v['half_kelly']} n={v['n']}")
