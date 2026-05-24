"""Tests for scripts/validate_decision.py schema + invariant checks."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import json  # noqa: E402
import validate_decision as vd  # noqa: E402

SCHEMA = json.loads(vd.SCHEMA_PATH.read_text(encoding="utf-8"))


def _call(**over):
    base = {
        "ticker": "NVDA",
        "horizon": "swing",
        "direction": "long",
        "tier": "MEDIUM",
        "raw_score": 8,
        "score_components": [
            {"rubric_line": "+3 historical_cumulative_premium_flow", "points": 3,
             "source_agent": "signal-confluence-quant", "source_tool": "historical_cumulative_premium_flow",
             "evidence": "30d +$112M long"},
            {"rubric_line": "+3 accumulation 3-of-3", "points": 3,
             "source_agent": "accumulation-hunter", "source_tool": "insights_institutional_accumulation",
             "evidence": "DP + OI + smart_positioning"},
            {"rubric_line": "+2 multileg directional", "points": 2,
             "source_agent": "multileg-strategist", "source_tool": "hot_chains_multileg",
             "evidence": "bull vertical"},
        ],
        "dominant_signal_class": "dark_pool_accumulation",
        "final_size": "half",
        "thesis": "Institutional accumulation with aligned premium flow.",
        "invalidation": "DEX reverses or breadth < 30%",
    }
    base.update(over)
    return base


def _doc(**over):
    base = {
        "schema_version": "1.0",
        "report_date": "2026-05-23",
        "report_kind": "daily",
        "regime": "TRANSITIONAL UPTREND",
        "report_path": "analyses/2026-05-23.md",
        "calls": [_call()],
    }
    base.update(over)
    return base


class SchemaTest(unittest.TestCase):
    def test_valid_document(self):
        self.assertEqual(vd.validate_doc(_doc(), SCHEMA), [])

    def test_missing_required_top_level(self):
        doc = _doc()
        del doc["regime"]
        errs = vd.validate_doc(doc, SCHEMA)
        self.assertTrue(any("missing required key 'regime'" in e for e in errs))

    def test_bad_enum_horizon(self):
        errs = vd.validate_doc(_doc(calls=[_call(horizon="intraday")]), SCHEMA)
        self.assertTrue(any("not in enum" in e for e in errs))

    def test_additional_property_rejected(self):
        errs = vd.validate_doc(_doc(calls=[_call(extra_field=1)]), SCHEMA)
        self.assertTrue(any("unexpected key 'extra_field'" in e for e in errs))

    def test_bad_schema_version_const(self):
        errs = vd.validate_doc(_doc(schema_version="2.0"), SCHEMA)
        self.assertTrue(any("const" in e for e in errs))

    def test_report_date_pattern(self):
        errs = vd.validate_doc(_doc(report_date="May 23 2026"), SCHEMA)
        self.assertTrue(any("pattern" in e for e in errs))


class InvariantTest(unittest.TestCase):
    def test_points_sum_mismatch(self):
        bad = _call(raw_score=9)  # components still sum to 8
        errs = vd.validate_doc(_doc(calls=[bad]), SCHEMA)
        self.assertTrue(any("!= raw_score" in e for e in errs))

    def test_tier_exceeds_band(self):
        # raw_score 8 only justifies MEDIUM; HIGH must come from >=10.
        bad = _call(tier="HIGH")
        errs = vd.validate_doc(_doc(calls=[bad]), SCHEMA)
        self.assertTrue(any("exceeds band" in e for e in errs))

    def test_tier_demotion_allowed(self):
        # raw_score 10 (HIGH band) demoted to MEDIUM is legal (LB-gate demote).
        comps = _call()["score_components"] + [
            {"rubric_line": "+2 confluence", "points": 2, "source_agent": "signal-confluence-quant",
             "source_tool": "insights_signal_confluence", "evidence": "score 5"}
        ]
        ok = _call(raw_score=10, tier="MEDIUM", score_components=comps)
        self.assertEqual(vd.validate_doc(_doc(calls=[ok]), SCHEMA), [])

    def test_veto_requires_skip_size(self):
        bad = _call(fundamentals_verdict="VETO", final_size="full")
        errs = vd.validate_doc(_doc(calls=[bad]), SCHEMA)
        self.assertTrue(any("VETO but final_size" in e for e in errs))

    def test_veto_with_veto_size_ok(self):
        ok = _call(fundamentals_verdict="VETO", final_size="veto")
        self.assertEqual(vd.validate_doc(_doc(calls=[ok]), SCHEMA), [])


if __name__ == "__main__":
    unittest.main()
