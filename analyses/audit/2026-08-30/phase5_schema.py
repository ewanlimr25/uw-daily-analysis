#!/usr/bin/env python3
"""Phase 5 — grade the FROZEN rubric (version 2026-06-12). Propose-only; no re-weight.

Per the skill's rubric-freeze clause this phase reports, per regime stratum:
  * frozen weight vs measured marginal contribution for each scored component line
  * tier-cut monotonicity status vs the frozen cuts (HIGH >=9 / MED 7-8 / LOW 3-6 / DROP <=2)
  * the P0.6 out-of-regime half-cap grade
It emits NO weight or cut edits — only pre-registered hypotheses for a future audit.

New this run: every component contribution is reported BOTH as raw WR delta and as
tape-conditioned WR delta, because Phase 3d established that ~71% of the variance in
the benchmark-excess column is the SPY base rate moving rather than the book.
"""
import json, math, statistics, re
from collections import defaultdict

AUD = "analyses/audit/2026-08-30"
SPY = json.load(open(f"{AUD}/_ohlc/SPY.json"))["bars"]
rows = [json.loads(l) for l in open(f"{AUD}/phase_2_outcomes.jsonl")]
dec = [r for r in rows if r["outcome"] in ("WIN", "LOSS")]


def eidx(bars, d):
    idx = None
    for i, x in enumerate(bars):
        if x["date"] == d: return i
        if x["date"] < d: idx = i
        else: break
    return idx


def spyret(d, n):
    i = eidx(SPY, d)
    if i is None: return None
    f = SPY[i + 1: i + 1 + n]
    return None if not f else (f[-1]["close"] - SPY[i]["close"]) / SPY[i]["close"] * 100


for r in dec:
    v = spyret(r["report_date"], r.get("nwin") or 10)
    r["_tape"] = None if v is None else ("UP" if v > 0 else "DOWN")


def wr(sub):
    if not sub: return None
    return sum(1 for r in sub if r["outcome"] == "WIN") / len(sub)


def binom_two_sided(w, n, p0):
    if n == 0: return 1.0
    p0 = min(max(p0, 1e-6), 1 - 1e-6)
    lo = sum(math.comb(n, i) * p0**i * (1 - p0)**(n - i) for i in range(0, w + 1))
    hi = 1 - sum(math.comb(n, i) * p0**i * (1 - p0)**(n - i) for i in range(0, w))
    return min(1.0, 2 * min(lo, hi))


def bh(pvals, fdr=0.10):
    idx = sorted(range(len(pvals)), key=lambda i: pvals[i]); m = len(pvals); kmax = -1
    for rank, i in enumerate(idx, 1):
        if pvals[i] <= rank / m * fdr: kmax = rank
    return {i for rank, i in enumerate(idx, 1) if rank <= kmax}


# ---------- component-line normalization ----------
def norm_component(comp):
    """Collapse a score_components[] entry to a frozen-rubric line label."""
    tool = (comp.get("source_tool") or comp.get("tool") or "").lower()
    agent = (comp.get("source_agent") or "").lower()
    pts = comp.get("points") or 0
    desc = (comp.get("criterion") or comp.get("description") or comp.get("reason") or "").lower()
    blob = f"{tool} {agent} {desc}".replace("-", "_")
    if "block" in blob and "strat" in blob: return "accumulation_conjunction(+3)"
    if "institutional_accumulation" in blob or "institutional accumulation" in blob: return "accumulation_conjunction(+3)"
    if "dex" in blob or "dealer" in blob: return "dealer_dex_flip(+1)"
    if "cumulative_premium" in blob or "cum_premium" in blob or "cum-flow" in blob: return "cum_flow_intent(+1)"
    if "multileg" in blob or "multi_leg" in blob: return "multileg_structure(+2)"
    if "oi_trend" in blob or "oi-trend" in blob: return "oi_trend_building(+1)"
    if "sector_flow" in blob or "sector-flow" in blob: return "sector_persistence(+1)"
    if "term_skew" in blob or "iv_term" in blob or "front_end_iv" in blob: return "vol_term_structure(+/-)"
    if "signal_confluence" in blob: return "signal_confluence(+1)"
    if "sweep" in blob: return "sweep_persistence(+1)"
    if "gex" in blob or "gamma" in blob: return "gamma_context(+1)"
    if "earnings" in blob: return "earnings_catalyst(+/-)"
    if "screener" in blob: return "screener_context(+1)"
    return f"other:{tool[:28] or 'unlabelled'}"


line_rows = defaultdict(lambda: {"with": [], "pts": []})
for r in dec:
    seen = set()
    for comp in (r.get("score_components") or []):
        lab = norm_component(comp)
        pts_ = comp.get("points") or 0
        lab = f"{lab}[{'+' if pts_>0 else ('-' if pts_<0 else '0')}{abs(pts_)}]"
        if lab in seen: continue
        seen.add(lab)
        line_rows[lab]["with"].append(r)
        line_rows[lab]["pts"].append(comp.get("points") or 0)

base_wr = wr(dec)
out_lines = []
pvals = []
for lab, d in sorted(line_rows.items(), key=lambda kv: -len(kv[1]["with"])):
    sub = d["with"]
    if len(sub) < 8: continue
    ids = {id(r) for r in sub}
    without = [r for r in dec if id(r) not in ids]
    w_wr, wo_wr = wr(sub), wr(without)
    marg = (w_wr - wo_wr) * 100
    wins = sum(1 for r in sub if r["outcome"] == "WIN")
    p = binom_two_sided(wins, len(sub), wo_wr)
    # tape-conditioned
    tape_marg = {}
    for tape in ("UP", "DOWN"):
        st = [r for r in sub if r["_tape"] == tape]
        wt = [r for r in without if r["_tape"] == tape]
        if len(st) >= 8 and wt:
            tape_marg[tape] = round((wr(st) - wr(wt)) * 100, 1)
    frozen_pts = statistics.mode(d["pts"]) if d["pts"] else None
    out_lines.append({"line": lab, "n": len(sub), "frozen_points": frozen_pts,
                      "wr_with": round(w_wr, 3), "wr_without": round(wo_wr, 3),
                      "marginal_pp": round(marg, 1), "p_raw": round(p, 4),
                      "tape_conditioned_marginal_pp": tape_marg})
    pvals.append(p)

surv = bh(pvals)
for i, l in enumerate(out_lines):
    l["bh_survives"] = i in surv

print("=== FROZEN-RUBRIC COMPONENT GRADING (rubric_version 2026-06-12 frozen) ===")
print(f"{'component line':34} {'pts':>4} {'n':>4} {'WRwith':>7} {'WRw/o':>7} {'marg':>7} {'p':>7} BH  {'UPtape':>7} {'DNtape':>7}")
for l in out_lines:
    tm = l["tape_conditioned_marginal_pp"]
    print(f"{l['line']:34} {str(l['frozen_points']):>4} {l['n']:4} {l['wr_with']:7.3f} {l['wr_without']:7.3f} "
          f"{l['marginal_pp']:+7.1f} {l['p_raw']:7.3f} {'Y ' if l['bh_survives'] else 'n '} "
          f"{str(tm.get('UP','--')):>7} {str(tm.get('DOWN','--')):>7}")

# ---------- tier-cut monotonicity vs frozen cuts ----------
print("\n=== TIER-CUT MONOTONICITY vs FROZEN CUTS (HIGH>=9 / MED 7-8 / LOW 3-6 / DROP<=2) ===")
bands = {"DROP(<=2)": lambda s: s <= 2, "LOW(3-6)": lambda s: 3 <= s <= 6,
         "MED(7-8)": lambda s: 7 <= s <= 8, "HIGH(>=9)": lambda s: s >= 9}
band_out = {}
for lab, fn in bands.items():
    sub = [r for r in dec if r["raw_score"] is not None and fn(r["raw_score"])]
    band_out[lab] = {"n": len(sub), "wr": round(wr(sub), 3) if sub else None}
    print(f"  {lab:12} n={len(sub):3} WR={band_out[lab]['wr']}")
mono = [band_out[k]["wr"] for k in ("DROP(<=2)", "LOW(3-6)", "MED(7-8)", "HIGH(>=9)") if band_out[k]["wr"] is not None]
print(f"  monotone ascending DROP->HIGH? {mono == sorted(mono)}  ({mono})")

# post-freeze only
print("\n  post-freeze (2026-06-12+) only:")
pf = [r for r in dec if r.get("post_freeze")]
for lab, fn in bands.items():
    sub = [r for r in pf if r["raw_score"] is not None and fn(r["raw_score"])]
    print(f"    {lab:12} n={len(sub):3} WR={round(wr(sub),3) if sub else None}")

# ---------- half-cap ----------
oor = [r for r in dec if r.get("out_of_regime")]
inr = [r for r in dec if not r.get("out_of_regime")]
print(f"\n=== P0.6 OUT-OF-REGIME HALF-CAP ===")
print(f"  out_of_regime n={len(oor)} WR={round(wr(oor),3)}   in_regime n={len(inr)} WR={round(wr(inr),3)}")
print(f"  delta={round((wr(oor)-wr(inr))*100,1)}pp  -> {'ACTIONABLE' if len(oor)>=10 else 'ADVISORY'}; "
      f"cap is {'PROTECTIVE' if wr(oor) < wr(inr) else 'TAXING'}")

json.dump({"component_lines": out_lines, "tier_bands": band_out,
           "monotone": mono == sorted(mono),
           "halfcap": {"oor_n": len(oor), "oor_wr": round(wr(oor), 3),
                       "in_n": len(inr), "in_wr": round(wr(inr), 3),
                       "delta_pp": round((wr(oor) - wr(inr)) * 100, 1)}},
          open(f"{AUD}/phase_5_schema.jsonl", "w"), indent=1)
print("\nwrote phase_5_schema.jsonl")
