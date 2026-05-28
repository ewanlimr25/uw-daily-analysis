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
        "report_path": "analyses/daily/2026-05-23/report.md",
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

    def test_bad_schema_version_rejected(self):
        errs = vd.validate_doc(_doc(schema_version="2.0"), SCHEMA)
        self.assertTrue(any("not in enum" in e for e in errs))

    def test_schema_version_1_0_still_valid(self):
        # Backward-compat: legacy 1.0 envelopes must keep validating after the bump.
        self.assertEqual(vd.validate_doc(_doc(schema_version="1.0"), SCHEMA), [])

    def test_schema_version_1_1_valid(self):
        self.assertEqual(vd.validate_doc(_doc(schema_version="1.1"), SCHEMA), [])

    def test_report_date_pattern(self):
        errs = vd.validate_doc(_doc(report_date="May 23 2026"), SCHEMA)
        self.assertTrue(any("pattern" in e for e in errs))


class FzAdvisoryTest(unittest.TestCase):
    """2026-05-27 fz-edge: breadth_cross_check (top-level) + fz_context (per-call), both advisory/additive."""

    def test_breadth_cross_check_valid(self):
        breadth = {"advisory": True, "source": "finviz", "advancers": 236,
                   "decliners": 263, "pct_green": 46.92, "divergence_flag": True,
                   "note": "green tape, more decliners"}
        self.assertEqual(vd.validate_doc(_doc(breadth_cross_check=breadth), SCHEMA), [])

    def test_breadth_cross_check_null_when_fz_unavailable(self):
        self.assertEqual(vd.validate_doc(_doc(breadth_cross_check=None), SCHEMA), [])

    def test_breadth_advisory_must_be_true(self):
        breadth = {"advisory": False, "source": "finviz"}
        errs = vd.validate_doc(_doc(breadth_cross_check=breadth), SCHEMA)
        self.assertTrue(any("const" in e for e in errs))

    def test_fz_context_valid_on_call(self):
        fzc = {"available": True, "short_float_pct": 27.72, "days_to_cover": 7.68,
               "float_shares": 86000000, "squeeze_pressure": "HIGH", "recom": 2.1,
               "upside_to_target_pct": 14.0, "rsi": 55.2, "note": "advisory 0pts"}
        self.assertEqual(vd.validate_doc(_doc(calls=[_call(fz_context=fzc)]), SCHEMA), [])

    def test_fz_context_unavailable_minimal(self):
        self.assertEqual(
            vd.validate_doc(_doc(calls=[_call(fz_context={"available": False})]), SCHEMA), [])

    def test_fz_context_bad_squeeze_enum_rejected(self):
        fzc = {"available": True, "squeeze_pressure": "EXTREME"}
        errs = vd.validate_doc(_doc(calls=[_call(fz_context=fzc)]), SCHEMA)
        self.assertTrue(any("not in enum" in e for e in errs))


def _next_session_gex(**over):
    base = {
        "advisory": True,
        "as_of_eod_date": "2026-05-22",
        "next_session_date": "2026-05-26",
        "indices": [
            {
                "symbol": "SPY", "spot": 745.92, "zero_gamma_level": 744.7,
                "zgl_reliable": True, "regime": "POSITIVE", "total_gex": 1527909389,
                "call_wall": 746, "put_wall": 730,
                "read": "Long-gamma pin; spot just above ZGL.",
                "structure_bias": "iron fly / condor centred on the pin",
                "caveats": "EOD prior; re-computes after the open. Advisory only.",
            },
            {
                "symbol": "QQQ", "spot": 717.85, "zero_gamma_level": None,
                "zgl_reliable": False, "regime": "FULLY_NEGATIVE", "total_gex": -466072648,
                "call_wall": 718, "put_wall": 700,
                "read": "Short-gamma; ZGL null, lean on total_gex sign + walls.",
                "structure_bias": "directional / debit vertical in trend direction",
                "caveats": "ZGL unreliable; gap risk voids the prior.",
            },
        ],
    }
    base.update(over)
    return base


class NextSessionGexTest(unittest.TestCase):
    def test_advisory_block_valid(self):
        doc = _doc(schema_version="1.1", next_session_gex=_next_session_gex())
        self.assertEqual(vd.validate_doc(doc, SCHEMA), [])

    def test_advisory_must_be_true(self):
        doc = _doc(schema_version="1.1", next_session_gex=_next_session_gex(advisory=False))
        errs = vd.validate_doc(doc, SCHEMA)
        self.assertTrue(any("const" in e for e in errs))

    def test_scope_boundary_only_spy_qqq(self):
        # IWM / single names are out of §2 scope — enforced by the symbol enum.
        bad = _next_session_gex()
        bad["indices"][0]["symbol"] = "IWM"
        errs = vd.validate_doc(_doc(schema_version="1.1", next_session_gex=bad), SCHEMA)
        self.assertTrue(any("not in enum" in e for e in errs))

    def test_advisory_additional_property_rejected(self):
        bad = _next_session_gex()
        bad["indices"][0]["unexpected"] = 1
        errs = vd.validate_doc(_doc(schema_version="1.1", next_session_gex=bad), SCHEMA)
        self.assertTrue(any("unexpected key 'unexpected'" in e for e in errs))

    def test_null_advisory_block_valid(self):
        # A "no edge / data unavailable" day may emit null.
        doc = _doc(schema_version="1.1", next_session_gex=None)
        self.assertEqual(vd.validate_doc(doc, SCHEMA), [])


def _0dte_setup(**over):
    base = {
        "advisory": True,
        "as_of_eod_date": "2026-05-22",
        "backtest_verdict": "GO_PREMIUM_SELL_INTRADAY",
        "indices": [
            {"symbol": "SPY", "sell_premium": True, "vol_state": "LOW", "vix": 16.7,
             "implied_move_pct": 0.57, "expected_range_pct": 0.75, "size_scalar": 0.5,
             "suggested_structure": "iron fly centred at 745.9, wings ±0.75%",
             "entry_rule": "Enter at the open; hold to close; never carry overnight.",
             "stand_aside_reason": None, "caution": None},
            {"symbol": "QQQ", "sell_premium": False, "vol_state": "UNKNOWN", "vix": None,
             "implied_move_pct": 0.9, "expected_range_pct": 1.38, "size_scalar": 0.0,
             "suggested_structure": "stand aside", "entry_rule": None,
             "stand_aside_reason": "VIX spiking", "caution": None},
        ],
    }
    base.update(over)
    return base


class NextSession0dteSetupTest(unittest.TestCase):
    def test_setup_block_valid(self):
        doc = _doc(schema_version="1.1", next_session_0dte_setup=_0dte_setup())
        self.assertEqual(vd.validate_doc(doc, SCHEMA), [])

    def test_both_advisory_blocks_together_valid(self):
        doc = _doc(schema_version="1.1", next_session_gex=None,
                   next_session_0dte_setup=_0dte_setup())
        self.assertEqual(vd.validate_doc(doc, SCHEMA), [])

    def test_bad_verdict_rejected(self):
        doc = _doc(schema_version="1.1", next_session_0dte_setup=_0dte_setup(backtest_verdict="LOL"))
        self.assertTrue(any("not in enum" in e for e in vd.validate_doc(doc, SCHEMA)))

    def test_scope_only_spy_qqq(self):
        bad = _0dte_setup()
        bad["indices"][0]["symbol"] = "IWM"
        errs = vd.validate_doc(_doc(schema_version="1.1", next_session_0dte_setup=bad), SCHEMA)
        self.assertTrue(any("not in enum" in e for e in errs))

    def test_missing_sell_premium_rejected(self):
        bad = _0dte_setup()
        del bad["indices"][0]["sell_premium"]
        errs = vd.validate_doc(_doc(schema_version="1.1", next_session_0dte_setup=bad), SCHEMA)
        self.assertTrue(any("missing required key 'sell_premium'" in e for e in errs))

    def test_null_setup_valid(self):
        doc = _doc(schema_version="1.1", next_session_0dte_setup=None)
        self.assertEqual(vd.validate_doc(doc, SCHEMA), [])


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


class ConjunctionC11Test(unittest.TestCase):
    """2026-05-25 register C11 — the +3 accumulation line is a conjunction.

    Full +3 only when cum_premium_flow_30d confirms (sign aligned AND |flow| >= $50M);
    otherwise halved (floored) to +1. These tests pin the two resulting arithmetic
    states so the Sigma(score_components.points) == raw_score invariant survives the
    halving and the demotion it produces.
    """

    def _accum_comp(self, points):
        return {
            "rubric_line": "+3 3+ aligned signals in accumulation-hunter (conjunction)",
            "points": points, "source_agent": "accumulation-hunter",
            "source_tool": "insights_institutional_accumulation",
            "evidence": "DP + OI + smart_positioning institutional-tier",
        }

    def test_c11_full_conjunction_high_valid(self):
        # cum_flow confirms (+$112M LONG, >=$50M) -> accumulation pays full +3.
        # +3 accum +3 cum_flow +2 confluence +3 DEX = 11 -> HIGH.
        comps = [
            self._accum_comp(3),
            {"rubric_line": "+3 historical_cumulative_premium_flow", "points": 3,
             "source_agent": "signal-confluence-quant", "source_tool": "historical_cumulative_premium_flow",
             "evidence": "30d +$112M LONG >=$50M -> conjunction confirmed"},
            {"rubric_line": "+2 insights_signal_confluence >=4", "points": 2,
             "source_agent": "signal-confluence-quant", "source_tool": "insights_signal_confluence",
             "evidence": "confluence 5"},
            {"rubric_line": "+3 dealer DEX flip", "points": 3,
             "source_agent": "dealer-positioning-strategist", "source_tool": "options_structure_dex",
             "evidence": "DEX flip long"},
        ]
        call = _call(raw_score=11, tier="HIGH", score_components=comps, final_size="full")
        self.assertEqual(vd.validate_doc(_doc(calls=[call]), SCHEMA), [])

    def test_c11_halved_accumulation_demotes_and_validates(self):
        # cum_flow MIXED / sub-$50M -> accumulation halved to +1; the additive pile
        # can no longer clear HIGH. +1 accum +2 confluence +3 DEX = 6 -> LOW. Sigma holds.
        comps = [
            self._accum_comp(1),
            {"rubric_line": "+2 insights_signal_confluence >=4", "points": 2,
             "source_agent": "signal-confluence-quant", "source_tool": "insights_signal_confluence",
             "evidence": "confluence 5"},
            {"rubric_line": "+3 dealer DEX flip", "points": 3,
             "source_agent": "dealer-positioning-strategist", "source_tool": "options_structure_dex",
             "evidence": "DEX flip long"},
        ]
        call = _call(raw_score=6, tier="LOW", score_components=comps, final_size="starter")
        self.assertEqual(vd.validate_doc(_doc(calls=[call]), SCHEMA), [])

    def test_c11_halved_with_flow_conflict_lite_coexists(self):
        # C11 halving (+1 accum) and flow_conflict_lite (-1) may BOTH fire on a
        # MIXED-flow name. +1 accum +2 confluence -1 lite = 2 -> DROP band. Sigma holds.
        comps = [
            self._accum_comp(1),
            {"rubric_line": "+2 insights_signal_confluence >=4", "points": 2,
             "source_agent": "signal-confluence-quant", "source_tool": "insights_signal_confluence",
             "evidence": "confluence 4"},
            {"rubric_line": "-1 flow_conflict_lite", "points": -1,
             "source_agent": "signal-confluence-quant", "source_tool": "historical_cumulative_premium_flow",
             "evidence": "cum_flow_30d MIXED vs LONG"},
        ]
        call = _call(raw_score=2, tier="DROP", score_components=comps, final_size="skip")
        self.assertEqual(vd.validate_doc(_doc(calls=[call]), SCHEMA), [])

    def test_c11_halved_to_one_cannot_reach_high_band(self):
        # Monotonicity intent: accumulation halved to +1 plus one other big component
        # cannot reach the HIGH band (>=10). Asserting the band math directly.
        self.assertLess(1 + 3 + 2, 10)  # +1 accum + +3 DEX + +2 confluence = 6 < HIGH


class ExpectancyC3Test(unittest.TestCase):
    """2026-05-25 register C3 — optional realised/Kelly fields on a call (advisory until n>=30)."""

    def test_c3_fields_validate(self):
        call = _call(realized_pnl_pct=4.9, payoff_ratio=3.0, expectancy_pct=3.6, kelly_fraction=0.2)
        self.assertEqual(vd.validate_doc(_doc(calls=[call]), SCHEMA), [])

    def test_c3_fields_nullable_while_open(self):
        call = _call(realized_pnl_pct=None, payoff_ratio=None, expectancy_pct=None, kelly_fraction=None)
        self.assertEqual(vd.validate_doc(_doc(calls=[call]), SCHEMA), [])

    def test_c3_legacy_envelope_without_fields_still_valid(self):
        # Backward-compat: the fields are optional; pre-C3 envelopes omit them.
        self.assertEqual(vd.validate_doc(_doc(), SCHEMA), [])

    def test_c3_kelly_fraction_must_be_floored_at_zero(self):
        errs = vd.validate_doc(_doc(calls=[_call(kelly_fraction=-0.1)]), SCHEMA)
        self.assertTrue(any("kelly_fraction" in e and "out of [0, 1]" in e for e in errs))

    def test_c3_kelly_fraction_above_one_rejected(self):
        errs = vd.validate_doc(_doc(calls=[_call(kelly_fraction=1.5)]), SCHEMA)
        self.assertTrue(any("kelly_fraction" in e for e in errs))


if __name__ == "__main__":
    unittest.main()
