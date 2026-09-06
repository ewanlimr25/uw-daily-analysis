#!/usr/bin/env python3
"""Phase 1 (2026-06-06 run) — extend the 2026-05-30 inventory with the 6 new
envelope-backed reports (daily 2026-06-01..06-05 + weekly 2026-W23).

The 05-30 inventory (516 rows, through daily 2026-05-29 + W22) is reused verbatim:
those reports are immutable history and the prior parse passed its own
zero-row/dedup checks. New rows come straight off validated decision.json
envelopes — no prose parsing.
"""
import collections
import json
import re
import sys
from pathlib import Path

AUD = Path("analyses/audit/2026-06-06")
PRIOR = Path("analyses/audit/2026-05-30/phase_1_inventory.jsonl")

NEW_ENVELOPES = [
    "analyses/daily/2026-06-01/decision.json",
    "analyses/daily/2026-06-02/decision.json",
    "analyses/daily/2026-06-03/decision.json",
    "analyses/daily/2026-06-04/decision.json",
    "analyses/daily/2026-06-05/decision.json",
    "analyses/weekly/2026-W23/decision.json",
]

SUFFIX_RE = re.compile(r"[-_](LEAP|HEDGE|0DTE|DTE|SWING|VOL|PIN)$", re.IGNORECASE)


def base_ticker(t):
    if not t:
        return t
    return SUFFIX_RE.sub("", t).strip()


def gates_fired(gate_verdicts):
    if not isinstance(gate_verdicts, dict):
        return []
    fired = []
    for k, v in gate_verdicts.items():
        s = str(v).lower()
        if s.startswith("no-op") or s.startswith("confirm (0)") or s == "confirm":
            continue
        fired.append(f"{k}:{v}")
    return fired


def tools_from_components(components):
    tools = []
    for c in components or []:
        t = c.get("source_tool") or c.get("tool")
        if t:
            tools.append(t)
    return sorted(set(tools))


def agents_from_components(components):
    return sorted({c["source_agent"] for c in (components or []) if c.get("source_agent")})


def extract_envelope(path):
    p = Path(path)
    d = json.load(open(p))
    report_kind = d.get("report_kind", "daily")
    if report_kind == "weekly":
        report_date = d.get("iso_week") or d.get("report_date")
    else:
        report_date = d.get("report_date") or d.get("iso_week")
    rows = []
    for c in d.get("calls", []):
        comps = c.get("score_components", [])
        gv = c.get("gate_verdicts", {})
        rows.append({
            "report_date": report_date,
            "report_kind": report_kind,
            "report_path": d.get("report_path", str(p.parent / "report.md")),
            "ticker": c.get("ticker"),
            "section": c.get("section"),
            "horizon": c.get("horizon"),
            "tier": c.get("tier"),
            "raw_score": c.get("raw_score"),
            "score_components": comps,
            "dominant_signal_class": c.get("dominant_signal_class"),
            "claimed_win_rate": c.get("win_rate"),
            "win_rate_n": c.get("win_rate_n"),
            "win_rate_source": c.get("win_rate_source"),
            "confluence_score": c.get("confluence_score"),
            "cum_premium_flow_30d": c.get("cum_premium_flow_30d"),
            "cum_premium_flow_90d": c.get("cum_premium_flow_90d"),
            "pre_risk_size": c.get("pre_risk_size"),
            "final_size": c.get("final_size"),
            "structure": c.get("structure"),
            "thesis_direction": c.get("direction"),
            "invalidation": c.get("invalidation"),
            "entry_or_trigger": c.get("entry_or_trigger"),
            "key_risks": c.get("key_risks"),
            "thesis": c.get("thesis"),
            "agents_flagged_by": agents_from_components(comps),
            "tools_cited": tools_from_components(comps),
            "regime_at_entry": d.get("regime"),
            "vrp_at_entry": d.get("vrp_classification"),
            "gates_fired": gates_fired(gv),
            "gate_verdicts": gv,
            "fundamentals_verdict": c.get("fundamentals_verdict"),
            "debate_residual_confidence": c.get("debate_residual_confidence"),
            "distribution_flag": c.get("distribution_flag"),
            "fz_context": c.get("fz_context"),
            "breadth_cross_check": d.get("breadth_cross_check"),
            "macro_event_risk": d.get("macro_event_risk"),
            "legacy_format": False,
            "source": "envelope",
            "_src": p.as_posix(),
        })
    return rows


def main():
    prior = [json.loads(l) for l in open(PRIOR) if l.strip()]
    new_rows = []
    for path in NEW_ENVELOPES:
        rows = extract_envelope(path)
        if not rows:
            sys.exit(f"ABORT: zero rows extracted from non-empty envelope {path} — parser bug")
        new_rows.extend(rows)

    for r in new_rows:
        r["call_key"] = r.get("ticker")
        r["ticker_base"] = base_ticker(r.get("ticker"))

    # dedup across the union on (date, kind, call_key, horizon); prefer new envelope rows
    best = {}
    for r in prior + new_rows:
        key = (r.get("report_date"), r.get("report_kind"), r.get("call_key"), r.get("horizon"))
        if key not in best or r.get("_src", "").startswith("analyses/daily/2026-06") \
           or r.get("_src", "").startswith("analyses/weekly/2026-W23"):
            if key in best:
                print(f"DUP collision (kept newer): {key}", file=sys.stderr)
            best[key] = r
    merged = list(best.values())

    out = AUD / "phase_1_inventory.jsonl"
    with open(out, "w") as f:
        for r in merged:
            f.write(json.dumps(r) + "\n")

    stats = {
        "prior_rows": len(prior),
        "new_envelope_rows": len(new_rows),
        "after_dedup": len(merged),
        "by_report_kind": dict(collections.Counter(r.get("report_kind") for r in merged)),
        "by_horizon": dict(collections.Counter(r.get("horizon") for r in merged)),
        "by_section": dict(collections.Counter(r.get("section") for r in merged)),
        "by_tier": dict(collections.Counter(r.get("tier") for r in merged)),
        "by_direction": dict(collections.Counter(r.get("thesis_direction") for r in merged)),
        "legacy_vs_envelope": dict(collections.Counter(r.get("source") for r in merged)),
        "with_claimed_wr": sum(1 for r in merged if r.get("claimed_win_rate") is not None),
        "with_score_components": sum(1 for r in merged if r.get("score_components")),
        "with_fz_context": sum(1 for r in merged if r.get("fz_context")),
        "with_distribution_flag": sum(1 for r in merged if r.get("distribution_flag")),
        "n_reports": len({(r.get("report_date"), r.get("report_kind")) for r in merged}),
        "new_by_report": dict(collections.Counter(
            (r["report_kind"], r["report_date"]) for r in new_rows)),
    }
    sc = collections.Counter(r.get("dominant_signal_class") for r in merged
                             if r.get("dominant_signal_class"))
    stats["top_signal_classes"] = dict(sc.most_common(15))
    print(json.dumps({k: ({str(kk): vv for kk, vv in v.items()} if isinstance(v, dict) else v)
                      for k, v in stats.items()}, indent=1, default=str))


if __name__ == "__main__":
    main()
