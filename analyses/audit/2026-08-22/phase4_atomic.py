#!/usr/bin/env python3
"""Phase 4b — ATOMIC tool attribution.

The 2026-08-15 audit found 122 distinct citation strings over 1,225 instances (60
singletons, 52 concatenations) — tool tiers were resting on fragmented denominators.
P1 #1 shipped a canonical-id contract (post-fix cohort: 0 concatenations). This script
recovers a comparable table over the FULL corpus by splitting concatenations on
+ / , / "and" / "via", normalizing spelling to the canonical `uw <group> <sub>` /
`scripts/*.py` ids, and dropping per-call argument suffixes (--symbol X, --days N,
--date ...). Class-conditional marginal contribution, BH FDR 0.10.
"""
import json, re, math
from collections import defaultdict

AUD = "analyses/audit/2026-08-22"
rows = [json.loads(l) for l in open(f"{AUD}/phase_2_outcomes.jsonl")]
dec = [r for r in rows if r["outcome"] in ("WIN", "LOSS")]

SPLIT = re.compile(r"\s*(?:\+|,|/(?=\s)|(?<=\s)/|\band\b|\bvia\b|\bover\b)\s*", re.I)
ARG = re.compile(r"\s--?[a-z][\w-]*(?:\s+[^\s+,]+)?", re.I)
PAREN = re.compile(r"\([^)]*\)")

ALIAS = {
    "iv term-structure hygiene": "scripts/term_structure_hygiene.py",
    "iv-term-structure hygiene": "scripts/term_structure_hygiene.py",
    "term structure hygiene.py": "scripts/term_structure_hygiene.py",
    "hygiene": "scripts/term_structure_hygiene.py",
    "term_structure_hygiene.py": "scripts/term_structure_hygiene.py",
    "dex flip.py": "scripts/dex_flip.py",
    "dex_flip.py": "scripts/dex_flip.py",
    "front-end-iv-ratio": "uw options-structure front-end-iv-ratio",
    "front end iv ratio": "uw options-structure front-end-iv-ratio",
    "term-skew": "uw options-structure term-skew",
    "term skew": "uw options-structure term-skew",
    "iv-term-structure": "uw options-structure iv-term-structure",
    "iv term structure": "uw options-structure iv-term-structure",
    "biggest-increases": "uw oi biggest-increases",
    "biggest increases": "uw oi biggest-increases",
    "sector-flow-persistence": "uw options-flow sector-flow-persistence",
    "market-regime.sector rotation": "uw risk market-regime",
    "market-regime.sector_rotation": "uw risk market-regime",
    "market-regime": "uw risk market-regime",
    "cumulative-premium-flow": "uw historical cumulative-premium-flow",
    "oi-trend": "uw historical oi-trend",
    "gex": "uw options-structure gex",
    "dex": "uw options-structure dex",
    "multileg": "uw hot-chains multileg",
    "pin-risk": "uw oi pin-risk",
    "vrp": "uw historical vrp",
    "signal-confluence": "uw insights signal-confluence",
    "institutional-accumulation": "uw insights institutional-accumulation",
    "block-stratified": "uw dark-pool block-stratified",
    "price-levels": "uw dark-pool price-levels",
    "earnings-catalyst": "uw screener earnings-catalyst",
    "iv-rank": "uw screener iv-rank",
    "single-leg": "uw options-flow single-leg",
    "sweeps": "uw options-flow sweeps",
    "sweep-persistence": "uw hot-chains sweep-persistence",
    "vanna-charm": "uw options-structure vanna-charm",
    "greek-screener": "uw options-flow greek-screener",
    "pc-ratio-zscore": "uw historical pc-ratio-zscore",
    "iv-percentile-zscore": "uw historical iv-percentile-zscore",
    "opex-concentration": "uw oi opex-concentration",
    "smart-positioning": "uw oi smart-positioning",
    "oi-by-strike": "uw oi oi-by-strike",
    "position-rolls": "uw oi position-rolls",
    "gex-time-series": "uw historical gex-time-series",
    "today-gamma-flip": "uw options-structure today-gamma-flip",
    "decrease-with-volume": "uw oi decrease-with-volume",
    "most-active": "uw hot-chains most-active",
    "bullish-bearish": "uw screener bullish-bearish",
    "conviction-matrix": "uw insights conviction-matrix",
    "price-vs-flow": "uw insights price-vs-flow",
    "earnings-play": "uw insights earnings-play",
    "deep-dive": "uw insights deep-dive",
}


def atomize(s):
    """One citation string -> list of canonical atomic tool ids."""
    if not s:
        return []
    s = PAREN.sub(" ", s)
    out = []
    for part in SPLIT.split(s):
        p = ARG.sub("", part).strip().strip(".").strip()
        p = re.sub(r"\s+", " ", p)
        if not p:
            continue
        low = p.lower()
        # legacy slugged form: "historical_cumulative_premium_flow" -> "uw historical cumulative-premium-flow"
        if "_" in low and not low.startswith(("scripts/", "uw ")) and " " not in low:
            head, _, tail = low.partition("_")
            GROUPS = {"historical", "insights", "options", "hot", "dark", "oi", "risk",
                      "screener", "playbook", "watchlist"}
            if head in GROUPS:
                if head in ("options", "hot", "dark"):
                    grp = f"{head}-{low.split('_')[1]}"
                    sub = "-".join(low.split("_")[2:])
                else:
                    grp, sub = head, tail.replace("_", "-")
                low = f"uw {grp} {sub}"
        low = low.replace("_", "-") if low.startswith("uw ") else low
        if low.startswith("uw "):
            low = re.sub(r"\.[a-z-]+$", "", low)  # market-regime.sector-rotation -> market-regime
            out.append(ALIAS.get(low[3:], low))
            continue
        if low in ALIAS:
            out.append(ALIAS[low]); continue
        if low.startswith("scripts/"):
            out.append(ALIAS.get(low.replace("scripts/", ""), low)); continue
        # bare subcommand-ish tail
        key = low.split("--")[0].strip()
        if key in ALIAS:
            out.append(ALIAS[key]); continue
        out.append(p)
    return out


def norm(t):
    t = t.strip()
    if t.startswith("uw ") and not t.startswith("uw  "):
        return t
    return t


for r in dec:
    ats = set()
    for c in (r.get("tools_cited") or []):
        for a in atomize(c):
            ats.add(norm(a))
    r["_atomic"] = sorted(ats)

CLS = "canonical_class"
by_tool = defaultdict(list)
for r in dec:
    for t in r["_atomic"]:
        by_tool[t].append(r)

base_wr = sum(1 for r in dec if r["outcome"] == "WIN") / len(dec)


def binom_p(k, n, p):
    if n == 0:
        return 1.0
    c = lambda a, b: math.comb(a, b)
    obs = c(n, k) * p**k * (1-p)**(n-k)
    tot = 0.0
    for i in range(n+1):
        pi = c(n, i) * p**i * (1-p)**(n-i)
        if pi <= obs + 1e-12:
            tot += pi
    return min(1.0, tot)


res = []
for t, rs in by_tool.items():
    n = len(rs)
    if n < 5:
        continue
    # class-conditional marginal contribution
    num = den = 0.0
    for cl in {r.get(CLS) or r.get("dominant_signal_class") for r in rs}:
        wi = [r for r in rs if (r.get(CLS) or r.get("dominant_signal_class")) == cl]
        wo = [r for r in dec if (r.get(CLS) or r.get("dominant_signal_class")) == cl and t not in r["_atomic"]]
        if not wi or not wo:
            continue
        d = (sum(1 for r in wi if r["outcome"] == "WIN")/len(wi)
             - sum(1 for r in wo if r["outcome"] == "WIN")/len(wo))
        num += d * len(wi); den += len(wi)
    marg = (num/den*100) if den else None
    wr_with = sum(1 for r in rs if r["outcome"] == "WIN")/n
    others = [r for r in dec if t not in r["_atomic"]]
    wr_wo = sum(1 for r in others if r["outcome"] == "WIN")/len(others)
    k = sum(1 for r in rs if r["outcome"] == "WIN")
    res.append({"tool": t, "n": n, "marginal_contribution_pp": marg,
                "wr_with": wr_with, "wr_without": wr_wo,
                "raw_delta_pp": (wr_with-wr_wo)*100,
                "ubiquity": n/len(dec), "p": binom_p(k, n, wr_wo)})

res.sort(key=lambda x: x["p"])
m = len(res)
for i, r in enumerate(res, 1):
    r["bh_threshold"] = 0.10*i/m
    r["bh_survives"] = r["p"] <= r["bh_threshold"]
# step-up
surv = max([i for i, r in enumerate(res, 1) if r["p"] <= 0.10*i/m], default=0)
for i, r in enumerate(res, 1):
    r["bh_survives"] = i <= surv


def tier(r):
    mc = r["marginal_contribution_pp"]
    if mc is None:
        return "UNSCORED"
    prov = " (prov)" if r["n"] < 8 else ""
    if r["ubiquity"] > 0.60:
        return "UBIQUITY_CONFOUNDED" + prov
    if mc >= 10: return "LOAD-BEARING" + prov
    if mc >= 3: return "SUPPORTIVE" + prov
    if mc <= -5: return "NEGATIVE" + prov
    if abs(mc) <= 2: return "NO-INFO" + prov
    return "SUPPORTIVE" + prov


res.sort(key=lambda x: -(x["marginal_contribution_pp"] or -999))
print(f"base book WR = {base_wr:.3f} on n={len(dec)} decided")
print(f"{'tool':46s} {'n':>4s} {'marg':>7s} {'with':>5s} {'w/o':>5s} {'ubq':>5s} {'p':>6s} BH  TIER")
for r in res:
    r["tier"] = tier(r)
    print(f"{r['tool'][:46]:46s} {r['n']:4d} {r['marginal_contribution_pp']:7.1f} "
          f"{r['wr_with']:.2f} {r['wr_without']:5.2f} {r['ubiquity']:5.2f} "
          f"{r['p']:6.3f} {'Y' if r['bh_survives'] else 'n'}  {r['tier']}")

thin = sorted(((t, len(rs)) for t, rs in by_tool.items() if len(rs) < 5), key=lambda x: -x[1])
trapped = sum(n for _, n in thin)
tot_inst = sum(len(rs) for rs in by_tool.values())
print(f"\nATOMIC coverage: {len(by_tool)} distinct atomic ids / {tot_inst} row-instances")
print(f"  n<5 labels: {len(thin)} ids, {trapped} instances ({trapped/tot_inst*100:.1f}%)")
print(f"  scored (n>=5): {len(res)} ids")
print(f"  BH survivors at FDR 0.10: {sum(1 for r in res if r['bh_survives'])}")
json.dump(res, open(f"{AUD}/phase_4_tools_atomic.jsonl", "w"), indent=0)
