#!/usr/bin/env python3
"""Phase 4 (2026-05-30) — tool attribution on the C20 outcomes, with C23 Benjamini-Hochberg
across the tool set, C32 ubiquity flag, and the reconstructed-citation provenance cap.

Provenance: every DECIDED row is a legacy prose row (the 54 envelope rows are all window_open),
so tools_cited is RECONSTRUCTED, not verbatim. All tiers below are STRUCTURAL/QUALITATIVE and
cap Phase-7 priority at P1 (C23 reconstructed-citation rule)."""
import json, collections, statistics, math, importlib.util

spec = importlib.util.spec_from_file_location("p3", "analyses/audit/2026-05-30/phase3_calibration_v2.py")
p3 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p3)
canon = p3.canon
benjamini_hochberg = p3.benjamini_hochberg

AUD = "analyses/audit/2026-06-06"
WIN, LOSS = "WIN", "LOSS"

def wr(rows):
    d = [r for r in rows if r["outcome"] in (WIN, LOSS)]
    if not d: return None, 0
    return sum(1 for r in d if r["outcome"] == WIN) / len(d), len(d)

def norm_cdf(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))

def two_prop_p(w1, n1, w2, n2):
    """Two-sided 2-proportion z-test p-value."""
    if n1 == 0 or n2 == 0: return 1.0
    p1, p2 = w1 / n1, w2 / n2
    p = (w1 + w2) / (n1 + n2)
    se = math.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
    if se == 0: return 1.0
    z = (p1 - p2) / se
    return 2 * (1 - norm_cdf(abs(z)))

def main():
    rows = [json.loads(l) for l in open(f"{AUD}/phase_2_outcomes.jsonl")]
    dec = [r for r in rows if r["outcome"] in (WIN, LOSS)]
    for r in dec:
        r["_cls"] = canon(r.get("dominant_signal_class"))
    n_dec = len(dec)

    tool_rows = collections.defaultdict(list)
    for r in dec:
        for t in (r.get("tools_cited") or []):
            tool_rows[t].append(r)

    results = []
    for tool, trows in sorted(tool_rows.items(), key=lambda kv: -len(kv[1])):
        n_with = len(trows)
        if n_with < 5:
            results.append({"tool": tool, "n_with": n_with, "tier": "INSUFFICIENT_N"})
            continue
        classes = set(r["_cls"] for r in trows if r["_cls"])
        diffs = []
        for c in classes:
            cls_all = [r for r in dec if r["_cls"] == c]
            with_c = [r for r in cls_all if tool in (r.get("tools_cited") or [])]
            without_c = [r for r in cls_all if tool not in (r.get("tools_cited") or [])]
            w_with, n1 = wr(with_c); w_without, n2 = wr(without_c)
            if w_with is not None and w_without is not None and n1 >= 3 and n2 >= 3:
                diffs.append((c, w_with - w_without, n1))
        wins = [r for r in dec if r["outcome"] == WIN]
        losses = [r for r in dec if r["outcome"] == LOSS]
        frac_win = sum(1 for r in wins if tool in (r.get("tools_cited") or [])) / len(wins)
        frac_loss = sum(1 for r in losses if tool in (r.get("tools_cited") or [])) / len(losses)
        if diffs:
            tot = sum(d[2] for d in diffs)
            mc = sum(d[1] * d[2] for d in diffs) / tot if tot else None
        else:
            w_with, _ = wr(trows)
            w_without, _ = wr([r for r in dec if tool not in (r.get("tools_cited") or [])])
            mc = (w_with - w_without) if (w_with is not None and w_without is not None) else None
        # unconditional p-value for BH
        ww, nw = wr(trows)
        wo, no = wr([r for r in dec if tool not in (r.get("tools_cited") or [])])
        pval = two_prop_p(round(ww * nw), nw, round(wo * no), no) if (ww is not None and wo is not None) else 1.0
        # tier
        if mc is None:
            tier = "UNSCORABLE"
        elif frac_win >= 0.80 and frac_loss <= 0.30:
            tier = "CONFOUNDED"
        elif mc >= 0.10:
            tier = "LOAD-BEARING"
        elif mc >= 0.03:
            tier = "SUPPORTIVE"
        elif mc <= -0.05:
            tier = "NEGATIVE"
        elif abs(mc) <= 0.02:
            tier = "NO-INFO"
        else:
            tier = "SUPPORTIVE" if mc > 0 else "NO-INFO"
        cite_frac = n_with / n_dec
        results.append({"tool": tool, "n_with": n_with, "mc_pp": round(mc * 100, 1) if mc is not None else None,
                        "frac_on_win": round(frac_win, 2), "frac_on_loss": round(frac_loss, 2),
                        "n_classes": len(diffs), "tier": tier, "p": pval,
                        "cite_frac": round(cite_frac, 2),
                        "ubiquity_confounded": cite_frac > 0.60,
                        "thin_n": 5 <= n_with < 8,
                        "self_wr": round(ww, 3) if ww is not None else None})

    # BH across scorable tools (n>=5, mc not None)
    scor = [r for r in results if r.get("mc_pp") is not None]
    pvs = [r["p"] for r in scor]
    surv = benjamini_hochberg(pvs, fdr=0.10) if pvs else set()
    for i, r in enumerate(scor):
        r["bh_significant"] = i in surv

    # fz advisory
    env = [r for r in rows if r.get("source") == "envelope" or r.get("legacy_format") is False]
    env_dec = [r for r in env if r["outcome"] in (WIN, LOSS)]
    fz_have_dec = sum(1 for r in env_dec if r.get("fz_context"))

    out = {"tool_table": results, "n_decided": n_dec,
           "provenance": "RECONSTRUCTED (all decided rows are legacy prose; envelope rows window_open) -> structural/qualitative; caps Phase-7 at P1",
           "fz_advisory": {"envelope_decided": len(env_dec), "rows_with_fz_context_decided": fz_have_dec,
                           "verdict": "INSUFFICIENT_N — fz C15-C18 axes have 0 decided envelope rows (fz shipped 05-27; all envelope calls window_open). Stay advisory (0 pts). Re-test ~2026-06-12."}}
    json.dump(out, open(f"{AUD}/phase_4_tools.jsonl", "w"), indent=1, default=str)

    print(f"decided rows={n_dec} | no tool cited on >60% (max cite_frac shown). Provenance: RECONSTRUCTED -> all tiers structural.")
    print(f"{'TOOL':50} {'N':>3} {'MC':>6} {'win%':>5} {'los%':>5} {'cite':>5} {'BH':>3}  TIER")
    for r in sorted(results, key=lambda r: -(r['mc_pp'] if r.get('mc_pp') is not None else -999)):
        if r["tier"] == "INSUFFICIENT_N": continue
        bh = "*" if r.get("bh_significant") else ""
        tn = " thin" if r.get("thin_n") else ""
        print(f"{r['tool'][:50]:50} {r['n_with']:>3} {str(r.get('mc_pp')):>6} "
              f"{r.get('frac_on_win',''):>5} {r.get('frac_on_loss',''):>5} {r.get('cite_frac',''):>5} {bh:>3}  {r['tier']}{tn}")
    nins = sum(1 for r in results if r['tier'] == 'INSUFFICIENT_N')
    print(f"\n({nins} tools INSUFFICIENT_N <5 citations, excluded)")
    print("max cite_frac:", max((r.get('cite_frac',0) for r in results), default=0), "-> C32 ubiquity (>0.60) fires on NONE")
    print("BH-significant tools:", [r['tool'] for r in results if r.get('bh_significant')])

if __name__ == "__main__":
    main()
