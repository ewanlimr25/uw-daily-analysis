#!/usr/bin/env python3
"""Phase 4 — Tool Attribution. Class-controlled marginal contribution + BH + ubiquity
confound + N>=5 floor. Plus fz advisory (C15-C18) gating. Tool labels canonicalized
(CLI form and legacy underscore form are merged)."""
import json, statistics, math, sys
sys.path.insert(0, "scripts")

AUD = "analyses/audit/2026-07-18"
rows = [json.loads(l) for l in open(f"{AUD}/phase_2_outcomes.jsonl")]
dec = [r for r in rows if r["outcome"] in ("WIN", "LOSS")]


def canon_tool(t):
    t = t.strip()
    if t.startswith("uw "):
        t = t[3:]
    return t.replace(" ", "_").replace("-", "_")


def tools_of(r):
    out = set()
    for raw in r["tools_cited"]:
        for part in raw.split(" / "):
            if part.strip():
                out.add(canon_tool(part))
    return out


def wr(sub):
    w = sum(1 for r in sub if r["outcome"] == "WIN")
    return (w / len(sub)) if sub else None, len(sub)


def benjamini_hochberg(pvals, fdr=0.10):
    idx = sorted(range(len(pvals)), key=lambda i: pvals[i]); m = len(pvals); kmax = -1
    for rank, i in enumerate(idx, 1):
        if pvals[i] <= rank / m * fdr:
            kmax = rank
    return {i for rank, i in enumerate(idx, 1) if rank <= kmax}


def binom_cdf(k, n, p):
    return sum(math.comb(n, i) * p**i * (1 - p)**(n - i) for i in range(k + 1))


def two_prop_p(w1, n1, w2, n2):
    """Two-sided z-test on the difference of proportions (normal approx)."""
    if n1 == 0 or n2 == 0:
        return 1.0
    p1, p2 = w1 / n1, w2 / n2
    p = (w1 + w2) / (n1 + n2)
    se = math.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
    if se == 0:
        return 1.0
    z = (p1 - p2) / se
    return math.erfc(abs(z) / math.sqrt(2))


# universe of canonical tools
all_tools = set()
for r in dec:
    all_tools |= tools_of(r)

classes = sorted(set(r["canonical_class"] for r in dec))
tool_rows = []
for t in sorted(all_tools):
    cited = [r for r in dec if t in tools_of(r)]
    n_cited = len(cited)
    if n_cited < 5:
        tool_rows.append({"tool": t, "n": n_cited, "tier": "INSUFFICIENT_N"})
        continue
    # class-controlled marginal contribution
    num = den = 0.0
    contributions = []
    for c in classes:
        cw = [r for r in dec if r["canonical_class"] == c and t in tools_of(r)]
        cwo = [r for r in dec if r["canonical_class"] == c and t not in tools_of(r)]
        wr_w, n_w = wr(cw); wr_wo, n_wo = wr(cwo)
        if n_w >= 2 and n_wo >= 2 and wr_w is not None and wr_wo is not None:
            diff = wr_w - wr_wo
            num += diff * n_w; den += n_w
            contributions.append((c, round(diff * 100, 1), n_w, n_wo))
    marg = (num / den) if den else None
    # overall with/without (for ubiquity + winner/loser asymmetry)
    wr_w_all, n_w_all = wr(cited)
    not_cited = [r for r in dec if t not in tools_of(r)]
    wr_wo_all, n_wo_all = wr(not_cited)
    winners = [r for r in dec if r["outcome"] == "WIN"]
    losers = [r for r in dec if r["outcome"] == "LOSS"]
    frac_winners = sum(1 for r in winners if t in tools_of(r)) / len(winners)
    frac_losers = sum(1 for r in losers if t in tools_of(r)) / len(losers)
    ubiquity = n_cited / len(dec)
    w1 = sum(1 for r in cited if r["outcome"] == "WIN")
    w2 = sum(1 for r in not_cited if r["outcome"] == "WIN")
    p = two_prop_p(w1, n_cited, w2, len(not_cited))
    tool_rows.append({"tool": t, "n": n_cited, "marg_contrib_pp": round(marg * 100, 1) if marg is not None else None,
                      "wr_with": round(wr_w_all, 3), "wr_without": round(wr_wo_all, 3),
                      "frac_of_winners": round(frac_winners, 3), "frac_of_losers": round(frac_losers, 3),
                      "ubiquity": round(ubiquity, 3), "p_raw": p, "class_contribs": contributions})

# BH across scored tools
scored = [tr for tr in tool_rows if tr.get("marg_contrib_pp") is not None]
bh = benjamini_hochberg([tr["p_raw"] for tr in scored], 0.10)
scored_idx = {id(tr): i for i, tr in enumerate(scored)}
for tr in scored:
    tr["bh_survives"] = scored_idx[id(tr)] in bh


def tier_of(tr):
    if tr.get("tier") == "INSUFFICIENT_N":
        return "INSUFFICIENT_N"
    mc = tr["marg_contrib_pp"]
    if tr["ubiquity"] > 0.60:
        return "UBIQUITY_CONFOUNDED"
    if tr["frac_of_winners"] >= 0.80 and tr["frac_of_losers"] <= 0.30:
        return "CONFOUNDED"
    if mc is None:
        return "INSUFFICIENT_N"
    if mc >= 10:
        return "LOAD-BEARING"
    if mc >= 3:
        return "SUPPORTIVE"
    if mc <= -5:
        return "NEGATIVE"
    if abs(mc) <= 2:
        return "NO-INFO"
    return "SUPPORTIVE" if mc > 0 else "NEGATIVE"


for tr in tool_rows:
    tr["assigned_tier"] = tier_of(tr)
    # thin-N provisional
    if tr.get("n", 0) < 8 and tr["assigned_tier"] not in ("INSUFFICIENT_N",):
        tr["provisional"] = True

# ---------- fz advisory (C15-C18) ----------
fz = {}
# C15 squeeze: among SHORT-thesis decided, high-SI (short_float>=20 & dtc>=5) vs rest
shorts = [r for r in dec if r["thesis_direction"] == "short" and r.get("fz_short_float_pct") is not None]
hi_si = [r for r in shorts if (r.get("fz_short_float_pct") or 0) >= 20 and (r.get("fz_days_to_cover") or 0) >= 5]
lo_si = [r for r in shorts if r not in hi_si]
fz["C15_squeeze_short"] = {"n_short_with_fz": len(shorts), "n_hi_si": len(hi_si),
                            "hi_si_wr": round(wr(hi_si)[0], 3) if hi_si else None,
                            "lo_si_wr": round(wr(lo_si)[0], 3) if lo_si else None,
                            "verdict": "INSUFFICIENT_N" if len(hi_si) < 5 else "scored"}
# squeeze_pressure label distribution
from collections import Counter
fz["squeeze_pressure_dist"] = dict(Counter(r.get("fz_squeeze_pressure") for r in dec if r.get("fz_squeeze_pressure")))
# C17 flow-vs-analyst divergence: long-thesis with bearish analyst (recom>=3.5) or short-thesis with bullish (recom<=2.0)
div_rows = []
for r in dec:
    rec = r.get("fz_recom")
    if rec is None: continue
    d = r["thesis_direction"]
    if d == "long" and rec >= 3.5: div_rows.append(r)        # flow long, analysts bearish
    elif d == "short" and rec <= 2.0: div_rows.append(r)     # flow short, analysts bullish
fz["C17_flow_vs_analyst_divergence"] = {"n_divergent": len(div_rows),
    "divergent_wr": round(wr(div_rows)[0], 3) if div_rows else None,
    "verdict": "INSUFFICIENT_N" if len(div_rows) < 5 else "scored"}
fz["C18_insider_clusters"] = {"verdict": "NA — insider-cluster flag not carried in envelope calls[]"}
fz["C16_float_normalized_block"] = {"verdict": "NA — per-call DP-block/float ratio not in envelope"}
# breadth: divergence flag coverage
brd = [r for r in dec if r.get("breadth_divergence_flag") is not None]
fz["breadth_divergence"] = {"n_with_flag": sum(1 for r in brd if r.get("breadth_divergence_flag")),
                            "n_total": len(brd), "verdict": "advisory; structural only"}

json.dump({"tools": tool_rows, "fz": fz}, open(f"{AUD}/phase_4_tools.jsonl", "w"), indent=1)

# print
print(f"{'tool':42} {'n':>3} {'marg':>6} {'with':>5} {'wo':>5} {'ubq':>5} {'p':>6} {'BH':>2}  TIER")
for tr in sorted(tool_rows, key=lambda x: (x.get('marg_contrib_pp') is None, -(x.get('marg_contrib_pp') or -999))):
    if tr["assigned_tier"] == "INSUFFICIENT_N":
        print(f"{tr['tool']:42} {tr['n']:3}  {'--':>5} {'':5} {'':5} {'':5} {'':6} {'':2}  INSUFFICIENT_N")
        continue
    print(f"{tr['tool']:42} {tr['n']:3} {str(tr['marg_contrib_pp']):>6} {tr['wr_with']:.2f}  {tr['wr_without']:.2f}  "
          f"{tr['ubiquity']:.2f}  {tr['p_raw']:.3f}  {'Y' if tr.get('bh_survives') else 'n'}  "
          f"{tr['assigned_tier']}{' (prov)' if tr.get('provisional') else ''}")
print("\n=== fz advisory ===")
for k, v in fz.items():
    print(f"  {k}: {v}")
