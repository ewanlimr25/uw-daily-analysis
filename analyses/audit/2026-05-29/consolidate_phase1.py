#!/usr/bin/env python3
"""Phase 1 consolidation: merge envelope + legacy JSONL, normalize, dedup, stat.

- Derives `ticker_base` (strips -LEAP / -HEDGE / -0DTE / _HEDGE etc. disambiguation
  suffixes the prose workers added) for outcome resolution. Keeps the original
  disambiguated key as `call_key`.
- Dedups on (report_date, report_kind, call_key).
- Emits phase_1_inventory.jsonl and a stats blob to stdout.
"""
import json
import re
import sys
import collections
from pathlib import Path

AUDIT = Path("analyses/audit/2026-05-29")
SOURCES = [
    AUDIT / "_envelope_rows.jsonl",
    AUDIT / "_legacy_A.jsonl",
    AUDIT / "_legacy_B.jsonl",
    AUDIT / "_legacy_C.jsonl",
    AUDIT / "_legacy_D.jsonl",
    AUDIT / "_legacy_E.jsonl",
    AUDIT / "_legacy_F.jsonl",
    AUDIT / "_legacy_G.jsonl",
]

SUFFIX_RE = re.compile(r"[-_](LEAP|HEDGE|0DTE|DTE|SWING|VOL|PIN)$", re.IGNORECASE)


def base_ticker(t):
    if not t:
        return t
    return SUFFIX_RE.sub("", t).strip()


def main():
    rows = []
    bad = 0
    per_source = collections.Counter()
    for src in SOURCES:
        if not src.exists():
            print(f"WARN missing {src}", file=sys.stderr)
            continue
        for ln in open(src):
            ln = ln.strip()
            if not ln or ln.startswith("#"):
                continue
            try:
                r = json.loads(ln)
            except json.JSONDecodeError as e:
                bad += 1
                print(f"BAD JSON in {src.name}: {e}", file=sys.stderr)
                continue
            r["_src"] = src.name
            per_source[src.name] += 1
            rows.append(r)

    # normalize
    for r in rows:
        raw_t = r.get("ticker")
        r["call_key"] = raw_t
        r["ticker_base"] = base_ticker(raw_t)

    def richness(r):
        """Higher = prefer to keep on a same-key collision (audited > prose row)."""
        s = 0
        if r.get("source") == "envelope":
            s += 100
        if r.get("score_components"):
            s += 10
        if r.get("raw_score") is not None:
            s += 5
        if r.get("claimed_win_rate") is not None:
            s += 2
        # actionable sections beat watch/disqualified
        if r.get("section") not in ("watch_only", "leap_disqualified"):
            s += 3
        return s

    # Key on (date, kind, call_key, horizon): distinct-horizon trades on the same
    # ticker (e.g. AAPL swing + AAPL 0DTE + AAPL LEAP) stay separate because they
    # resolve on different windows; true §3-vs-§7 same-horizon dupes collapse to the
    # richer (audited) row per the skill's "prefer §7" rule.
    best = {}
    dup_drops = []
    for r in rows:
        key = (r.get("report_date"), r.get("report_kind"), r.get("call_key"), r.get("horizon"))
        if key not in best:
            best[key] = r
        else:
            dup_drops.append(key)
            if richness(r) > richness(best[key]):
                best[key] = r
    deduped = list(best.values())

    out = AUDIT / "phase_1_inventory.jsonl"
    with open(out, "w") as f:
        for r in deduped:
            f.write(json.dumps(r) + "\n")

    # stats
    stats = {
        "total_rows_read": len(rows),
        "bad_json": bad,
        "after_dedup": len(deduped),
        "dup_drops": len(dup_drops),
        "per_source": dict(per_source),
        "by_report_kind": dict(collections.Counter(r.get("report_kind") for r in deduped)),
        "by_horizon": dict(collections.Counter(r.get("horizon") for r in deduped)),
        "by_section": dict(collections.Counter(r.get("section") for r in deduped)),
        "by_tier": dict(collections.Counter(r.get("tier") for r in deduped)),
        "by_signal_class": dict(collections.Counter(r.get("dominant_signal_class") for r in deduped)),
        "by_direction": dict(collections.Counter(r.get("thesis_direction") for r in deduped)),
        "legacy_vs_envelope": dict(collections.Counter(r.get("source") for r in deduped)),
        "with_raw_score": sum(1 for r in deduped if r.get("raw_score") is not None),
        "with_claimed_wr": sum(1 for r in deduped if r.get("claimed_win_rate") is not None),
        "with_score_components": sum(1 for r in deduped if r.get("score_components")),
        "n_reports": len(set((r.get("report_date"), r.get("report_kind")) for r in deduped)),
    }
    # per-report row counts
    per_report = collections.Counter((r.get("report_kind"), r.get("report_date")) for r in deduped)
    stats["per_report"] = {f"{k[0]}/{k[1]}": v for k, v in sorted(per_report.items())}
    print(json.dumps(stats, indent=1))
    if dup_drops:
        print("DUP DROPS:", dup_drops, file=sys.stderr)


if __name__ == "__main__":
    main()
