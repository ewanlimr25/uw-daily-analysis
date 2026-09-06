#!/usr/bin/env python3
"""Phase 3b — regime-stratified supplement (2026-07-04).

The late-June PULLBACK/CHOPPY shift is the first non-pure-uptrend data the audit has
seen. This grades three things prior single-regime audits could not:
  1. Tier inversion presence in uptrend vs pullback strata (is it regime-invariant?)
  2. Long-edge / short-problem split by regime bucket (does short selection get worse
     as the tape falls?)
  3. The P0.6 OUT-OF-REGIME half-cap: do the half-capped (rubric_regime-gated /
     out_of_regime) names underperform — i.e. is the cap protecting, or taxing?
All advisory where decided-N < 10 per arm.
"""
import json, statistics

AUD = "analyses/audit/2026-08-08"
rows = [json.loads(l) for l in open(f"{AUD}/phase_2_outcomes.jsonl")]
dec = [r for r in rows if r["outcome"] in ("WIN", "LOSS")]


def wr(sub):
    w = sum(1 for r in sub if r["outcome"] == "WIN")
    return (w, len(sub), round(w / len(sub), 3) if sub else None)


def excess(sub):
    """book WR minus SPY-benchmark WR over the same rows (directional only)."""
    sb = [r for r in sub if r.get("spy_benchmark_win") is not None]
    if not sb:
        return None, 0
    book_w, book_n, book_wr = wr(sb)
    spy_wr = sum(1 for r in sb if r["spy_benchmark_win"]) / len(sb)
    return round((book_wr - spy_wr) * 100, 1), len(sb)


out = {}

# 1. tier reliability by regime bucket
print("=== TIER RELIABILITY BY REGIME BUCKET ===")
tier_by_regime = {}
for rb in ("uptrend", "pullback_in_uptrend", "choppy", "transitional_other"):
    sub = [r for r in dec if r.get("regime_bucket") == rb]
    tier_by_regime[rb] = {}
    line = f"  {rb:22}"
    for t in ("HIGH", "MEDIUM", "LOW", "DROP"):
        ts = [r for r in sub if r["tier"] == t]
        w, n, rwr = wr(ts)
        tier_by_regime[rb][t] = {"n": n, "wr": rwr}
        line += f" {t}={rwr}({n})" if rwr is not None else f" {t}=-({n})"
    print(line)
out["tier_by_regime"] = tier_by_regime

# 2. long/short edge by regime bucket
print("\n=== LONG / SHORT BOOK EXCESS vs SPY BY REGIME BUCKET ===")
dir_by_regime = {}
for rb in ("uptrend", "pullback_in_uptrend", "choppy", "transitional_other"):
    dir_by_regime[rb] = {}
    for d in ("long", "short"):
        sub = [r for r in dec if r.get("regime_bucket") == rb and r.get("thesis_direction") == d]
        w, n, rwr = wr(sub)
        exc, exc_n = excess(sub)
        dir_by_regime[rb][d] = {"n": n, "wr": rwr, "excess_pp": exc, "excess_n": exc_n}
        if n:
            print(f"  {rb:22} {d:5} n={n:3} WR={rwr}  excess={exc}pp (benchN={exc_n})")
out["dir_by_regime"] = dir_by_regime

# 3. OUT-OF-REGIME half-cap grading
print("\n=== P0.6 OUT-OF-REGIME HALF-CAP GRADING ===")
oor = [r for r in dec if r.get("out_of_regime")]
inr = [r for r in dec if not r.get("out_of_regime")]
rr_gated = [r for r in dec if "rubric_regime" in (r.get("gate_verdicts") or {})]
rr_ungated = [r for r in dec if "rubric_regime" not in (r.get("gate_verdicts") or {})]
for lab, sub in (("out_of_regime", oor), ("in_regime", inr),
                 ("rubric_regime_gated", rr_gated), ("rubric_regime_ungated", rr_ungated)):
    w, n, rwr = wr(sub)
    exc, exc_n = excess(sub)
    print(f"  {lab:24} n={n:3} WR={rwr}  excess={exc}pp")
    out[f"halfcap_{lab}"] = {"n": n, "wr": rwr, "excess_pp": exc}
out["halfcap_advisory"] = (len(oor) < 10)
print(f"  -> half-cap grading {'ADVISORY (oor decided<10)' if len(oor) < 10 else 'ACTIONABLE'}: oor_decided={len(oor)}")

# 4. post-freeze view (freeze-lift gate)
print("\n=== POST-FREEZE (frozen rubric 2026-06-12) ===")
pf = [r for r in dec if r.get("post_freeze")]
pf_tier = {}
for t in ("HIGH", "MEDIUM", "LOW", "DROP"):
    w, n, rwr = wr([r for r in pf if r["tier"] == t])
    pf_tier[t] = {"n": n, "wr": rwr}
print(f"  post-freeze decided={len(pf)} tier dist={ {t: pf_tier[t]['n'] for t in pf_tier} }")
print(f"  HIGH n={pf_tier['HIGH']['n']} MEDIUM n={pf_tier['MEDIUM']['n']} -> "
      f"freeze-lift {'CANNOT RUN (n=0 raw>=7)' if pf_tier['HIGH']['n']+pf_tier['MEDIUM']['n']==0 else 'has data'}")
out["post_freeze_tier"] = pf_tier
out["post_freeze_decided"] = len(pf)
w, n, rwr = wr(pf)
exc, exc_n = excess(pf)
print(f"  post-freeze book WR={rwr} (n={n})  excess={exc}pp")
out["post_freeze_book"] = {"wr": rwr, "n": n, "excess_pp": exc}

# 5. vol_short regime dependence (RV-proxy caveat)
print("\n=== VOL CLASS BY REGIME (RV-proxy — NOT true IV-vs-RV) ===")
for d in ("vol_long", "vol_short"):
    for rb in ("uptrend", "pullback_in_uptrend", "choppy", "transitional_other"):
        sub = [r for r in dec if r.get("thesis_direction") == d and r.get("regime_bucket") == rb]
        w, n, rwr = wr(sub)
        if n:
            print(f"  {d:9} {rb:22} n={n:2} WR={rwr}")
out["note"] = "vol resolution is rv_direction_proxy; vol_short collapse tracks RV expansion in the pullback, not a true IV-vs-RV miss"

json.dump(out, open(f"{AUD}/phase_3b_regime.jsonl", "w"), indent=1)
print("\nwrote phase_3b_regime.jsonl")
