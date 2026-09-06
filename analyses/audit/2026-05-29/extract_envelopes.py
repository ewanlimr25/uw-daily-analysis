#!/usr/bin/env python3
"""Phase 1 envelope extractor — deterministic normalization of decision.json sidecars.

Each call object in a validated envelope already IS the normalized Phase-1 row.
We map it to the audit schema, carrying envelope-only audit dimensions
(fundamentals_verdict, debate_residual_confidence, fz_context, breadth_cross_check,
gate_verdicts -> gates_fired). Emits one JSON object per line to stdout.
"""
import json
import sys
from pathlib import Path

ENVELOPES = [
    "analyses/daily/2026-05-25/decision.json",
    "analyses/daily/2026-05-26/decision.json",
    "analyses/daily/2026-05-27/decision.json",
    "analyses/daily/2026-05-28/decision.json",
    "analyses/daily/2026-05-29/decision.json",
    "analyses/weekly/2026-W22/decision.json",
]


def gates_fired(gate_verdicts):
    """A gate 'fired' if its verdict is not a no-op / CONFIRM-0."""
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
    ags = []
    for c in components or []:
        a = c.get("source_agent")
        if a:
            ags.append(a)
    return sorted(set(ags))


def main():
    rows = []
    for path in ENVELOPES:
        p = Path(path)
        if not p.exists():
            print(f"WARN missing {path}", file=sys.stderr)
            continue
        d = json.load(open(p))
        report_kind = d.get("report_kind", "daily")
        # Weekly reports date to the Friday close, which collides with the same-day
        # daily report_date. Key weekly rows by iso_week to keep identities clean.
        if report_kind == "weekly":
            report_date = d.get("iso_week") or d.get("report_date")
        else:
            report_date = d.get("report_date") or d.get("iso_week")
        regime = d.get("regime")
        vrp = d.get("vrp_classification")
        breadth = d.get("breadth_cross_check")
        macro_event = d.get("macro_event_risk")
        report_path = d.get("report_path", str(p.parent / "report.md"))
        for c in d.get("calls", []):
            comps = c.get("score_components", [])
            gv = c.get("gate_verdicts", {})
            row = {
                "report_date": report_date,
                "report_kind": report_kind,
                "report_path": report_path,
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
                "regime_at_entry": regime,
                "vrp_at_entry": vrp,
                "gates_fired": gates_fired(gv),
                "gate_verdicts": gv,
                "fundamentals_verdict": c.get("fundamentals_verdict"),
                "debate_residual_confidence": c.get("debate_residual_confidence"),
                "fz_context": c.get("fz_context"),
                "breadth_cross_check": breadth,
                "macro_event_risk": macro_event,
                "legacy_format": False,
                "source": "envelope",
            }
            rows.append(row)
    for r in rows:
        print(json.dumps(r))
    print(f"# extracted {len(rows)} envelope rows from {len(ENVELOPES)} files", file=sys.stderr)


if __name__ == "__main__":
    main()
