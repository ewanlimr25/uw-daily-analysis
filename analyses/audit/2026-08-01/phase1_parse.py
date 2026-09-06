#!/usr/bin/env python3
"""Phase 1 — Inventory & Parse (2026-07-04).

Extract normalized per-call rows from every decision envelope (the authoritative,
machine-resolvable source per the skill). Legacy prose-only reports (pre-2026-05-25
daily, pre-W22 weekly) are recorded as a coverage gap — already resolved by prior
audits and lacking score_components/win_rate.

Stratifies every row by rubric_version (schema >=1.3). Envelopes without the field
are era-banded by report_date against the rubric changelog (freeze = 2026-06-12).
New this run: tag `out_of_regime` (regime string carries OUT-OF-REGIME half-cap) and
`post_freeze` so Phase 3/5 can grade the frozen rubric + the P0.6 half-cap on its
own post-freeze outcomes, and so the late-June PULLBACK/CHOPPY regime shift is
separable from the long single-regime UPTREND tail.
"""
import json, glob, re

AUDIT = "analyses/audit/2026-08-01"
RUBRIC_FREEZE = "2026-06-12"


def era_band(report_date, rubric_version):
    if rubric_version:
        return rubric_version
    if report_date >= "2026-06-12":
        return "2026-06-12"
    if report_date >= "2026-06-06":
        return "pre_freeze_post_0606"
    if report_date >= "2026-05-30":
        return "era_0530_0605"
    if report_date >= "2026-05-25":
        return "era_0525_0529"
    return "legacy_prose"


def regime_bucket(regime):
    """Collapse the verbose regime string into a coarse trend bucket for stratification."""
    if not regime:
        return "unknown"
    r = regime.upper()
    if "CHOPPY" in r:
        return "choppy"
    if "PULLBACK" in r:
        return "pullback_in_uptrend"
    if "UPTREND" in r:
        return "uptrend"
    if "DOWNTREND" in r:
        return "downtrend"
    return "transitional_other"


rows = []
files = sorted(glob.glob("analyses/daily/*/decision.json")) + sorted(glob.glob("analyses/weekly/*/decision.json"))
for f in files:
    d = json.load(open(f))
    rd = d.get("report_date")
    kind = d.get("report_kind", "daily")
    regime = d.get("regime")
    vrp = d.get("vrp_classification")
    rubric_version = d.get("rubric_version")
    era = era_band(rd, rubric_version)
    macro_event_risk = d.get("macro_event_risk", [])
    breadth = d.get("breadth_cross_check", {}) or {}
    out_of_regime = bool(regime and "OUT-OF-REGIME" in regime.upper())
    post_freeze = rd >= RUBRIC_FREEZE
    rbucket = regime_bucket(regime)
    for c in d.get("calls", []):
        comps = c.get("score_components", []) or []
        tools, agents = [], []
        for comp in comps:
            t = comp.get("source_tool") or comp.get("tool")
            a = comp.get("source_agent")
            if t: tools.append(t)
            if a: agents.append(a)
        gv = c.get("gate_verdicts", {}) or {}
        gates_fired = []
        for k, v in gv.items():
            vs = str(v).lower()
            if vs.startswith("no_op") or vs.startswith("pass") or vs == "ok" or vs.startswith("clear"):
                continue
            gates_fired.append(k)
        fz = c.get("fz_context", {}) or {}
        row = {
            "report_date": rd,
            "report_kind": kind,
            "rubric_version": rubric_version,
            "rubric_era": era,
            "post_freeze": post_freeze,
            "out_of_regime": out_of_regime,
            "regime_bucket": rbucket,
            "ticker": c.get("ticker"),
            "section": c.get("section"),
            "horizon": c.get("horizon"),
            "direction": c.get("direction"),
            "tier": c.get("tier"),
            "raw_score": c.get("raw_score"),
            "score_components": comps,
            "n_components": len(comps),
            "sum_points": sum((comp.get("points") or 0) for comp in comps),
            "dominant_signal_class": c.get("dominant_signal_class"),
            "confluence_score": c.get("confluence_score"),
            "claimed_win_rate": c.get("win_rate"),
            "win_rate_uncapped": c.get("win_rate_uncapped"),
            "win_rate_n": c.get("win_rate_n"),
            "win_rate_source": c.get("win_rate_source"),
            "market_excess": c.get("market_excess"),
            "cum_premium_flow_30d": c.get("cum_premium_flow_30d"),
            "cum_premium_flow_90d": c.get("cum_premium_flow_90d"),
            "pre_risk_size": c.get("pre_risk_size"),
            "final_size": c.get("final_size"),
            "gate_verdicts": gv,
            "gates_fired": gates_fired,
            "fundamentals_verdict": c.get("fundamentals_verdict"),
            "debate_residual_confidence": c.get("debate_residual_confidence"),
            "debate_residuals": c.get("debate_residuals"),
            "tools_cited": tools,
            "agents_flagged_by": agents,
            "structure": c.get("structure"),
            "entry_or_trigger": c.get("entry_or_trigger"),
            "invalidation": c.get("invalidation"),
            "thesis_direction": c.get("direction"),
            "regime_at_entry": regime,
            "vrp_at_entry": vrp,
            "macro_event_risk": macro_event_risk,
            "fz_short_float_pct": fz.get("short_float_pct"),
            "fz_days_to_cover": fz.get("days_to_cover"),
            "fz_float_shares": fz.get("float_shares"),
            "fz_squeeze_pressure": fz.get("squeeze_pressure"),
            "fz_recom": fz.get("recom"),
            "fz_upside_to_target_pct": fz.get("upside_to_target_pct"),
            "breadth_pct_green": breadth.get("pct_green"),
            "breadth_divergence_flag": breadth.get("divergence_flag"),
            "source_file": f,
        }
        rows.append(row)

with open(f"{AUDIT}/phase_1_inventory.jsonl", "w") as out:
    for r in rows:
        out.write(json.dumps(r) + "\n")

# ticker universe for the OHLC fetcher
tickers = sorted({r["ticker"] for r in rows if r["ticker"]})
json.dump(tickers, open(f"{AUDIT}/_tickers.json", "w"))


def tally(rows, key):
    t = {}
    for r in rows:
        v = r.get(key)
        if isinstance(v, list): v = tuple(v) if v else "none"
        t[v] = t.get(v, 0) + 1
    return dict(sorted(t.items(), key=lambda kv: -kv[1]))


print("TOTAL ROWS:", len(rows), "| envelopes:", len(files), "| unique tickers:", len(tickers))
print("BY KIND:", tally(rows, "report_kind"))
print("BY RUBRIC_ERA:", tally(rows, "rubric_era"))
print("BY REGIME_BUCKET:", tally(rows, "regime_bucket"))
print("POST_FREEZE rows:", sum(1 for r in rows if r["post_freeze"]),
      "| OUT_OF_REGIME rows:", sum(1 for r in rows if r["out_of_regime"]))
print("BY HORIZON:", tally(rows, "horizon"))
print("BY SECTION:", tally(rows, "section"))
print("BY TIER:", tally(rows, "tier"))
print("BY DIRECTION:", tally(rows, "direction"))
print("BY SIGNAL_CLASS:")
for k, v in tally(rows, "dominant_signal_class").items():
    print(f"   {k}: {v}")
print("BY FUND_VERDICT:", tally(rows, "fundamentals_verdict"))
print("BY FINAL_SIZE:", tally(rows, "final_size"))
print("BY WIN_RATE_SOURCE:", tally(rows, "win_rate_source"))
mismatch = [r for r in rows if r["raw_score"] is not None and r["sum_points"] != r["raw_score"] and r["n_components"] > 0]
print("SUM_POINTS != RAW_SCORE (n_comp>0):", len(mismatch))
for r in mismatch[:10]:
    print(f"   {r['report_date']} {r['ticker']}: sum={r['sum_points']} raw={r['raw_score']}")
wr = [r for r in rows if r["claimed_win_rate"] is not None]
print("ROWS WITH claimed_win_rate:", len(wr))
print("POST-FREEZE BY TIER:", tally([r for r in rows if r["post_freeze"]], "tier"))
