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
             "source_agent": "signal-confluence-quant", "source_tool": "uw historical cumulative-premium-flow",
             "evidence": "30d +$112M long"},
            {"rubric_line": "+3 accumulation 3-of-3", "points": 3,
             "source_agent": "accumulation-hunter", "source_tool": "uw insights institutional-accumulation",
             "evidence": "DP + OI + smart_positioning"},
            {"rubric_line": "+2 multileg directional", "points": 2,
             "source_agent": "multileg-strategist", "source_tool": "uw hot-chains multileg",
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

    def test_schema_version_1_2_valid(self):
        # 2026-05-30 meta-audit bump (C28 distribution_flag).
        self.assertEqual(vd.validate_doc(_doc(schema_version="1.2"), SCHEMA), [])

    def test_schema_version_1_3_valid_with_rubric_version(self):
        # 2026-06-12 audit P0.1: rubric freeze — envelopes stamp the rubric era.
        # 1.3 calls also carry the 9-key gate_verdicts (P1.1 completeness invariant).
        doc = _doc(schema_version="1.3", rubric_version="2026-06-12",
                   calls=[_call(gate_verdicts=_gv())])
        self.assertEqual(vd.validate_doc(doc, SCHEMA), [])

    def test_rubric_version_optional_on_legacy_versions(self):
        # Additive field: 1.2 envelopes without rubric_version must keep validating.
        self.assertEqual(vd.validate_doc(_doc(schema_version="1.2"), SCHEMA), [])

    def test_rubric_version_must_be_string(self):
        errs = vd.validate_doc(_doc(schema_version="1.3", rubric_version=7), SCHEMA)
        self.assertTrue(any("rubric_version" in e and "type" in e for e in errs))

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
        # raw_score 8 only justifies MEDIUM; HIGH must come from >=9
        # (2026-05-30 register P1.3 band, validator synced 2026-06-06 audit P1.1).
        bad = _call(tier="HIGH")
        errs = vd.validate_doc(_doc(calls=[bad]), SCHEMA)
        self.assertTrue(any("exceeds band" in e for e in errs))

    def test_raw_9_high_validates(self):
        # 2026-06-06 audit P1.1: the live rubric's HIGH cut is >=9; the stale >=10 band
        # forced raw-9 calls to be recorded MEDIUM (five such calls in the June cohort).
        comps = _call()["score_components"] + [
            {"rubric_line": "+1 sector leader", "points": 1, "source_agent": "sector-rotation-strategist",
             "source_tool": "uw options-flow sector-flow-persistence", "evidence": "leader, persistence 0.8"}
        ]
        ok = _call(raw_score=9, tier="HIGH", score_components=comps)
        self.assertEqual(vd.validate_doc(_doc(calls=[ok]), SCHEMA), [])

    def test_tier_demotion_allowed(self):
        # raw_score 10 (HIGH band) demoted to MEDIUM is legal (LB-gate demote).
        comps = _call()["score_components"] + [
            {"rubric_line": "+2 confluence", "points": 2, "source_agent": "signal-confluence-quant",
             "source_tool": "uw insights signal-confluence", "evidence": "score 5"}
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


def _gv(**over):
    """A complete 9-key gate_verdicts dict (2026-06-12 P0.6/P1.1)."""
    base = {"regime": "no-op", "vrp": "no-op", "panic": "no-op", "cluster": "no-op",
            "sector": "no-op", "fundamentals": "CONFIRM", "event_risk": "no-op",
            "debate": "no-op", "rubric_regime": "capped half (OUT-OF-REGIME)"}
    base.update(over)
    return base


class GateVerdictCompletenessTest(unittest.TestCase):
    """2026-06-12 audit P1.1 — the schema had been REJECTING the debate key
    (additionalProperties:false without it), which is why it was recorded on
    0/151 envelope calls ever. 1.3+ envelopes must carry all 9 keys on every
    non-DROP call."""

    def test_full_9_key_gate_verdicts_valid(self):
        ok = _call(gate_verdicts=_gv())
        self.assertEqual(vd.validate_doc(_doc(schema_version="1.3", rubric_version="2026-06-12", calls=[ok]), SCHEMA), [])

    def test_debate_and_rubric_regime_keys_accepted(self):
        ok = _call(gate_verdicts=_gv(debate="−1 tier (bear 0.75 ≥ bull 0.65)"))
        self.assertEqual(vd.validate_doc(_doc(schema_version="1.3", rubric_version="2026-06-12", calls=[ok]), SCHEMA), [])

    def test_missing_debate_key_fails_on_1_3(self):
        gv = _gv(); del gv["debate"]
        errs = vd.validate_doc(_doc(schema_version="1.3", rubric_version="2026-06-12",
                                    calls=[_call(gate_verdicts=gv)]), SCHEMA)
        self.assertTrue(any("gate_verdicts" in e and "debate" in e for e in errs))

    def test_missing_gate_verdicts_fails_on_1_3_non_drop(self):
        errs = vd.validate_doc(_doc(schema_version="1.3", rubric_version="2026-06-12",
                                    calls=[_call()]), SCHEMA)
        self.assertTrue(any("gate_verdicts" in e for e in errs))

    def test_drop_tier_exempt_from_gate_verdicts(self):
        ok = _call(tier="DROP", raw_score=2, final_size="skip",
                   score_components=[{"rubric_line": "+2 multileg directional", "points": 2,
                                      "source_agent": "multileg-strategist",
                                      "source_tool": "uw hot-chains multileg", "evidence": "x"}])
        self.assertEqual(vd.validate_doc(_doc(schema_version="1.3", rubric_version="2026-06-12", calls=[ok]), SCHEMA), [])

    def test_legacy_1_2_exempt_from_completeness(self):
        # Pre-1.3 envelopes keep validating without the 9-key requirement.
        self.assertEqual(vd.validate_doc(_doc(schema_version="1.2", calls=[_call()]), SCHEMA), [])


class DebateResidualsPairTest(unittest.TestCase):
    """2026-06-12 audit P1.1 — store debate residuals as a {bull, bear} pair so
    the debate gate's effectiveness can be measured (06-06 P2.1 concurs)."""

    def test_pair_valid(self):
        ok = _call(gate_verdicts=_gv(), debate_residuals={"bull": 0.75, "bear": 0.65},
                   debate_residual_confidence=0.75)
        self.assertEqual(vd.validate_doc(_doc(schema_version="1.3", rubric_version="2026-06-12", calls=[ok]), SCHEMA), [])

    def test_pair_off_bin_rejected(self):
        bad = _call(gate_verdicts=_gv(), debate_residuals={"bull": 0.70, "bear": 0.65})
        errs = vd.validate_doc(_doc(schema_version="1.3", rubric_version="2026-06-12", calls=[bad]), SCHEMA)
        self.assertTrue(any("not in enum" in e for e in errs))

    def test_market_excess_field_accepted(self):
        ok = _call(gate_verdicts=_gv(), market_excess=-0.12)
        self.assertEqual(vd.validate_doc(_doc(schema_version="1.3", rubric_version="2026-06-12", calls=[ok]), SCHEMA), [])


class WinRateSourceVocabTest(unittest.TestCase):
    """2026-06-12 audit P0.3/P1 reconciliation — the quant now emits backtest_clean
    and NA(substrate); the schema enum must accept them (retired values kept for
    pre-1.3 back-compat)."""

    def test_backtest_clean_accepted(self):
        ok = _call(gate_verdicts=_gv(), win_rate=0.58, win_rate_n=37, win_rate_source="backtest_clean")
        self.assertEqual(vd.validate_doc(_doc(schema_version="1.3", rubric_version="2026-06-12", calls=[ok]), SCHEMA), [])

    def test_na_substrate_accepted(self):
        ok = _call(gate_verdicts=_gv(), win_rate=None, win_rate_source="NA(substrate)")
        self.assertEqual(vd.validate_doc(_doc(schema_version="1.3", rubric_version="2026-06-12", calls=[ok]), SCHEMA), [])

    def test_retired_values_still_accepted_for_backcompat(self):
        # pre-1.3 envelopes carrying backtest / fallback_proxy must keep validating.
        ok = _call(win_rate_source="fallback_proxy")
        self.assertEqual(vd.validate_doc(_doc(schema_version="1.2", calls=[ok]), SCHEMA), [])

    def test_garbage_source_rejected(self):
        ok = _call(gate_verdicts=_gv(), win_rate_source="vibes")
        errs = vd.validate_doc(_doc(schema_version="1.3", rubric_version="2026-06-12", calls=[ok]), SCHEMA)
        self.assertTrue(any("win_rate_source" in e and "enum" in e for e in errs))


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
            "source_tool": "uw insights institutional-accumulation",
            "evidence": "DP + OI + smart_positioning institutional-tier",
        }

    def test_c11_full_conjunction_high_valid(self):
        # cum_flow confirms (+$112M LONG, >=$50M) -> accumulation pays full +3.
        # +3 accum +3 cum_flow +2 confluence +3 DEX = 11 -> HIGH.
        comps = [
            self._accum_comp(3),
            {"rubric_line": "+3 historical_cumulative_premium_flow", "points": 3,
             "source_agent": "signal-confluence-quant", "source_tool": "uw historical cumulative-premium-flow",
             "evidence": "30d +$112M LONG >=$50M -> conjunction confirmed"},
            {"rubric_line": "+2 insights_signal_confluence >=4", "points": 2,
             "source_agent": "signal-confluence-quant", "source_tool": "uw insights signal-confluence",
             "evidence": "confluence 5"},
            {"rubric_line": "+3 dealer DEX flip", "points": 3,
             "source_agent": "dealer-positioning-strategist", "source_tool": "uw options-structure dex",
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
             "source_agent": "signal-confluence-quant", "source_tool": "uw insights signal-confluence",
             "evidence": "confluence 5"},
            {"rubric_line": "+3 dealer DEX flip", "points": 3,
             "source_agent": "dealer-positioning-strategist", "source_tool": "uw options-structure dex",
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
             "source_agent": "signal-confluence-quant", "source_tool": "uw insights signal-confluence",
             "evidence": "confluence 4"},
            {"rubric_line": "-1 flow_conflict_lite", "points": -1,
             "source_agent": "signal-confluence-quant", "source_tool": "uw historical cumulative-premium-flow",
             "evidence": "cum_flow_30d MIXED vs LONG"},
        ]
        call = _call(raw_score=2, tier="DROP", score_components=comps, final_size="skip")
        self.assertEqual(vd.validate_doc(_doc(calls=[call]), SCHEMA), [])

    def test_c11_halved_to_one_cannot_reach_high_band(self):
        # Monotonicity intent: accumulation halved to +1 plus one other big component
        # cannot reach the HIGH band (>=10). Asserting the band math directly.
        self.assertLess(1 + 3 + 2, 10)  # +1 accum + +3 DEX + +2 confluence = 6 < HIGH


class DistributionFlagC28Test(unittest.TestCase):
    """2026-05-30 meta-audit C28 — advisory `oi decrease-with-volume` distribution counter-signal.

    Additive optional per-call block, 0 points / 0 tier impact (never in score_components),
    structurally identical-in-discipline to fz_context. These pin valid/null/backward-compat
    and the closing_side enum.
    """

    def test_distribution_flag_present_valid(self):
        df = {"present": True, "source_tool": "uw oi decrease-with-volume",
              "closing_side": "call", "closing_premium": 20769937, "oi_decrease": -61636,
              "note": "META 720C OI -61.6k on 69.9k vol while flow reads long-accumulation"}
        self.assertEqual(vd.validate_doc(_doc(calls=[_call(distribution_flag=df)]), SCHEMA), [])

    def test_distribution_flag_absent_present_minimal(self):
        df = {"present": False}
        self.assertEqual(vd.validate_doc(_doc(calls=[_call(distribution_flag=df)]), SCHEMA), [])

    def test_distribution_flag_null_when_not_evaluated(self):
        self.assertEqual(vd.validate_doc(_doc(calls=[_call(distribution_flag=None)]), SCHEMA), [])

    def test_distribution_flag_backward_compat_absent(self):
        # Pre-C28 envelopes omit the field entirely — must still validate.
        self.assertEqual(vd.validate_doc(_doc(), SCHEMA), [])

    def test_distribution_flag_bad_closing_side_rejected(self):
        df = {"present": True, "closing_side": "straddle"}
        errs = vd.validate_doc(_doc(calls=[_call(distribution_flag=df)]), SCHEMA)
        self.assertTrue(any("not in enum" in e for e in errs))

    def test_distribution_flag_missing_present_rejected(self):
        df = {"closing_side": "call"}
        errs = vd.validate_doc(_doc(calls=[_call(distribution_flag=df)]), SCHEMA)
        self.assertTrue(any("missing required key 'present'" in e for e in errs))

    def test_distribution_flag_never_in_score_components(self):
        # Discipline: the flag is 0-points — it must not be expressed as a score component.
        # A call carrying the flag with components summing to raw_score still validates,
        # proving the flag lives outside the Sigma-invariant.
        df = {"present": True, "note": "advisory"}
        call = _call(distribution_flag=df)  # raw_score 8, components sum 8, flag is extra
        self.assertEqual(vd.validate_doc(_doc(calls=[call]), SCHEMA), [])


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


class ReliabilityFieldTest(unittest.TestCase):
    """2026-06-12 audit P2.3 — win_rate_uncapped preserves the pre-cap rate as a
    structured field so reliability diagrams aren't polluted by the 0.69/0.80 cap
    point-masses (the uncapped value was previously only in audit_trail prose)."""

    def test_uncapped_field_accepted(self):
        ok = _call(gate_verdicts=_gv(), win_rate=0.80, win_rate_uncapped=0.933, win_rate_n=49)
        self.assertEqual(vd.validate_doc(_doc(schema_version="1.3", rubric_version="2026-06-12", calls=[ok]), SCHEMA), [])

    def test_uncapped_null_accepted(self):
        ok = _call(gate_verdicts=_gv(), win_rate=None, win_rate_uncapped=None)
        self.assertEqual(vd.validate_doc(_doc(schema_version="1.3", rubric_version="2026-06-12", calls=[ok]), SCHEMA), [])

    def test_uncapped_must_be_number(self):
        ok = _call(gate_verdicts=_gv(), win_rate_uncapped="0.9")
        errs = vd.validate_doc(_doc(schema_version="1.3", rubric_version="2026-06-12", calls=[ok]), SCHEMA)
        self.assertTrue(any("win_rate_uncapped" in e for e in errs))


class RubricVersionPresenceTest(unittest.TestCase):
    """2026-06-12 audit P2.5 — a 1.3 envelope must stamp rubric_version (the freeze
    era stamp); a missing/null stamp defeats per-era stratification."""

    def test_1_3_requires_rubric_version(self):
        doc = _doc(schema_version="1.3", calls=[_call(gate_verdicts=_gv())])
        # no rubric_version key
        errs = vd.validate_doc(doc, SCHEMA)
        self.assertTrue(any("rubric_version" in e for e in errs))

    def test_1_3_null_rubric_version_rejected(self):
        doc = _doc(schema_version="1.3", rubric_version=None, calls=[_call(gate_verdicts=_gv())])
        errs = vd.validate_doc(doc, SCHEMA)
        self.assertTrue(any("rubric_version" in e for e in errs))

    def test_1_3_with_rubric_version_ok(self):
        doc = _doc(schema_version="1.3", rubric_version="2026-06-12", calls=[_call(gate_verdicts=_gv())])
        self.assertEqual(vd.validate_doc(doc, SCHEMA), [])

    def test_legacy_1_2_no_rubric_version_required(self):
        self.assertEqual(vd.validate_doc(_doc(schema_version="1.2"), SCHEMA), [])


class DeadLetterScoreComponentTest(unittest.TestCase):
    """2026-06-12 audit P2.5 — the regime-conflict and correlation-cluster lines are
    risk-monitor TIER gates (applied in 2d), never score_components. They must never
    re-enter the score carrying nonzero points (the dead-letter finding, P1/F5)."""

    def _comps_with(self, line, pts):
        # base components sum to 8; add the dead-letter line, fix raw_score to match
        base = _call()["score_components"]
        return base + [{"rubric_line": line, "points": pts,
                        "source_agent": "risk-monitor", "source_tool": "uw risk market-regime",
                        "evidence": "x"}]

    def test_regime_conflict_with_points_rejected(self):
        comps = self._comps_with("-3 uw risk market-regime conflicts with trade direction", -3)
        errs = vd.validate_doc(_doc(calls=[_call(raw_score=5, score_components=comps)]), SCHEMA)
        self.assertTrue(any("dead-letter" in e.lower() or "tier gate" in e.lower() for e in errs))

    def test_correlation_cluster_with_points_rejected(self):
        comps = self._comps_with("-1 risk-monitor flags in correlation cluster (corr > 0.7)", -1)
        errs = vd.validate_doc(_doc(calls=[_call(raw_score=7, score_components=comps)]), SCHEMA)
        self.assertTrue(any("dead-letter" in e.lower() or "tier gate" in e.lower() for e in errs))

    def test_dead_letter_line_with_zero_points_allowed(self):
        # a documentation entry carrying explicit 0 points is fine (Σ unaffected)
        comps = self._comps_with("[TIER GATE, 2d] uw risk market-regime conflicts with trade direction", 0)
        self.assertEqual(vd.validate_doc(_doc(calls=[_call(raw_score=8, score_components=comps)]), SCHEMA), [])

    def test_normal_components_not_flagged(self):
        # the existing valid doc (accumulation/cum-flow/multileg) must not trip the check
        self.assertEqual(vd.validate_doc(_doc(), SCHEMA), [])


class DebateResidualBinFloorTest(unittest.TestCase):
    """2026-07-25 audit P1 #5 — the ladder had no bin below 0.55.

    TSLA 2026-07-23 emitted 0.42 / 0.40 — 'neither advocate can make their case', the
    most informative debate output there is — and the schema erased it.
    """

    def test_sub_coin_flip_pair_now_validates(self):
        # The exact TSLA pair, snapped to the extended 0.10-spaced ladder.
        call = _call(debate_residuals={"bull": 0.45, "bear": 0.35},
                     debate_residual_confidence=0.45)
        self.assertEqual(vd.validate_doc(_doc(calls=[call]), SCHEMA), [])

    def test_full_extended_ladder_accepted_on_both_sides(self):
        for value in (0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95):
            call = _call(debate_residuals={"bull": value, "bear": value},
                         debate_residual_confidence=value)
            self.assertEqual(
                vd.validate_doc(_doc(calls=[call]), SCHEMA), [],
                msg=f"residual bin {value} rejected",
            )

    def test_off_ladder_value_still_rejected(self):
        # The ladder is extended, not opened up — 0.42 must be snapped to a bin, not
        # serialized raw. Bin discipline is what makes the gate's arms comparable.
        call = _call(debate_residuals={"bull": 0.42, "bear": 0.40})
        errs = vd.validate_doc(_doc(calls=[call]), SCHEMA)
        self.assertTrue(any("not in enum" in e for e in errs))

    def test_legacy_high_bins_unaffected(self):
        # Backward-compat: extending an enum must not disturb anything already valid.
        call = _call(debate_residuals={"bull": 0.75, "bear": 0.65},
                     debate_residual_confidence=0.75)
        self.assertEqual(vd.validate_doc(_doc(calls=[call]), SCHEMA), [])


class InstrumentationWarningsTest(unittest.TestCase):
    """2026-07-25 audit P1 #5 — silent field drops made C16/C18 ungradeable.

    These are WARNINGS by design: the 52 historical envelopes the audit reads as its
    dataset must keep validating, so a missing key is surfaced without being fatal.
    """

    def test_accumulation_row_missing_c16_c18_keys_warns(self):
        warns = vd.check_instrumentation_warnings(_doc())  # class is dark_pool_accumulation
        self.assertTrue(any("dp_block_to_float_ratio" in w for w in warns))
        self.assertTrue(any("insider_cluster_flag" in w for w in warns))

    def test_explicit_null_satisfies_the_check(self):
        call = _call(dp_block_to_float_ratio=None, insider_cluster_flag=None,
                     debate_residuals={"bull": 0.65, "bear": 0.55})
        warns = vd.check_instrumentation_warnings(_doc(calls=[call]))
        self.assertEqual(warns, [])

    def test_vol_row_missing_implied_move_warns(self):
        call = _call(dominant_signal_class="earnings_vol",
                     dp_block_to_float_ratio=None, insider_cluster_flag=None,
                     debate_residuals={"bull": 0.65, "bear": 0.55})
        warns = vd.check_instrumentation_warnings(_doc(calls=[call]))
        self.assertTrue(any("implied_move" in w for w in warns))

    def test_drop_rows_are_not_warned_for_debate_residuals(self):
        # DROP names exit before the full stack runs — same C54 logic as the audit's
        # missed-gate denominator. Only non-DROP calls owe a debate pair.
        call = _call(tier="DROP", dominant_signal_class="bullish_flow")
        warns = vd.check_instrumentation_warnings(_doc(calls=[call]))
        self.assertEqual(warns, [])

    def test_warnings_never_become_errors(self):
        # The whole point: an envelope with every instrumentation gap is still VALID.
        self.assertEqual(vd.validate_doc(_doc(), SCHEMA), [])
        self.assertTrue(vd.check_instrumentation_warnings(_doc()))


if __name__ == "__main__":
    unittest.main()


class CanonicalClassAndC16ValueWarnings(unittest.TestCase):
    """2026-08-01 audit: P2 #9 class-drift warning + the C16 null-value regression guard."""

    def test_offlist_signal_class_warns_with_alias_hint(self):
        call = _call(dominant_signal_class="dex_flip_long",
                     dp_block_to_float_ratio=None, insider_cluster_flag=None,
                     debate_residuals={"bull": 0.65, "bear": 0.55})
        warns = vd.check_instrumentation_warnings(_doc(calls=[call]))
        hit = [w for w in warns if "not canonical" in w]
        self.assertTrue(hit)
        self.assertIn("dealer_positioning", hit[0])

    def test_canonical_signal_class_does_not_warn(self):
        call = _call(dominant_signal_class="bullish_flow",
                     dp_block_to_float_ratio=None, insider_cluster_flag=None,
                     debate_residuals={"bull": 0.65, "bear": 0.55})
        warns = vd.check_instrumentation_warnings(_doc(calls=[call]))
        self.assertFalse([w for w in warns if "not canonical" in w])

    def test_c16_null_warns_only_when_fz_lane_ran(self):
        base = dict(dominant_signal_class="dark_pool_accumulation",
                    dp_block_to_float_ratio=None, insider_cluster_flag=None,
                    debate_residuals={"bull": 0.65, "bear": 0.55})
        ran = _call(fz_context={"available": True}, **base)
        warns = vd.check_instrumentation_warnings(_doc(calls=[ran]))
        self.assertTrue([w for w in warns if "dp_block_to_float_ratio=null" in w])

    def test_c16_null_silent_on_graceful_fz_skip(self):
        """An explicit null is the contract-mandated value when fz is unavailable."""
        base = dict(dominant_signal_class="dark_pool_accumulation",
                    dp_block_to_float_ratio=None, insider_cluster_flag=None,
                    debate_residuals={"bull": 0.65, "bear": 0.55})
        for fzc in ({"available": False}, None):
            call = _call(fz_context=fzc, **base)
            warns = vd.check_instrumentation_warnings(_doc(calls=[call]))
            self.assertFalse([w for w in warns if "dp_block_to_float_ratio=null" in w])

    def test_c16_populated_value_never_warns(self):
        call = _call(dominant_signal_class="dark_pool_accumulation",
                     fz_context={"available": True},
                     dp_block_to_float_ratio=0.0012, insider_cluster_flag=False,
                     debate_residuals={"bull": 0.65, "bear": 0.55})
        warns = vd.check_instrumentation_warnings(_doc(calls=[call]))
        self.assertFalse([w for w in warns if "dp_block_to_float_ratio" in w])

    def test_these_warnings_are_never_errors(self):
        call = _call(dominant_signal_class="dex_flip_long",
                     fz_context={"available": True}, dp_block_to_float_ratio=None)
        self.assertEqual(vd.validate_doc(_doc(calls=[call]), SCHEMA), [])


class CanonicalSourceToolWarnings(unittest.TestCase):
    """2026-08-15 audit P1 #1 — one canonical tool id per score_component.

    The corpus carried 122 distinct citation strings over 1,225 instances (60 singletons,
    52 concatenations); 155 instances were trapped in n<5 labels and the same tool scored
    opposite Phase-4 tiers under two spellings.
    """

    def _comp(self, tool):
        return {"rubric_line": "+3 x", "points": 3, "source_agent": "a",
                "source_tool": tool, "evidence": "e"}

    def _warns_for(self, tool):
        call = _call(score_components=[self._comp(tool)], raw_score=3, tier="LOW",
                     dominant_signal_class="bullish_flow",
                     debate_residuals={"bull": 0.6, "bear": 0.5})
        return vd.check_instrumentation_warnings(_doc(calls=[call]))

    def test_plus_concatenated_tool_warns(self):
        w = [x for x in self._warns_for(
            "uw options-structure iv-term-structure + uw options-structure term-skew")
            if "names more than one tool" in x]
        self.assertTrue(w)

    def test_slash_and_comma_concatenations_warn(self):
        for tool in ("uw oi position-rolls / biggest-increases",
                     "uw historical vrp, uw options-structure term-skew"):
            hits = [x for x in self._warns_for(tool) if "names more than one tool" in x]
            self.assertTrue(hits, f"expected concat warning for {tool!r}")

    def test_offlist_spelling_warns(self):
        for tool in ("uw options-structure dex (dated)", "historical_cumulative_premium_flow"):
            hits = [x for x in self._warns_for(tool) if "is not canonical" in x]
            self.assertTrue(hits, f"expected off-list warning for {tool!r}")

    def test_canonical_single_tool_is_silent(self):
        for tool in ("uw historical cumulative-premium-flow", "scripts/dex_flip.py"):
            hits = [x for x in self._warns_for(tool)
                    if "is not canonical" in x or "names more than one tool" in x]
            self.assertFalse(hits, f"unexpected warning for canonical {tool!r}")

    def test_source_tool_warnings_are_never_errors(self):
        call = _call(score_components=[self._comp("uw a + uw b")], raw_score=3, tier="LOW")
        self.assertEqual(vd.validate_doc(_doc(calls=[call]), SCHEMA), [])


class BacktestClassSupportWarnings(unittest.TestCase):
    """2026-08-15 audit P1 #2 — a backtest-sourced win_rate is only possible for the five
    classes `uw historical signal-backtest --signal-type` accepts.

    earnings_vol is NOT one of them, yet quoted 0.87 / realised 0.394 on n=109 (BH p<0.001)
    with 12 of 13 quoted rows citing win_rate_source 'backtest'.
    """

    def _warns(self, cls, src):
        call = _call(dominant_signal_class=cls, win_rate=0.87, win_rate_source=src,
                     debate_residuals={"bull": 0.6, "bear": 0.5})
        return [w for w in vd.check_instrumentation_warnings(_doc(calls=[call]))
                if "does not support" in w]

    def test_unsupported_class_with_backtest_source_warns(self):
        for src in ("backtest", "backtest_clean"):
            self.assertTrue(self._warns("earnings_vol", src), f"expected warning for {src}")

    def test_supported_classes_are_silent(self):
        for cls in ("bullish_flow", "bearish_flow", "high_iv_rank",
                    "volume_spike", "dark_pool_accumulation"):
            self.assertFalse(self._warns(cls, "backtest_clean"), f"unexpected warning for {cls}")

    def test_alias_is_collapsed_before_the_support_check(self):
        """dex_flip_long -> dealer_positioning, which is still unsupported: warn once."""
        self.assertTrue(self._warns("dex_flip_long", "backtest_clean"))

    def test_na_substrate_never_warns(self):
        """The honest emission for an unsupported class must be silent."""
        call = _call(dominant_signal_class="earnings_vol", win_rate=None,
                     win_rate_source="NA(substrate)",
                     debate_residuals={"bull": 0.6, "bear": 0.5})
        warns = vd.check_instrumentation_warnings(_doc(calls=[call]))
        self.assertFalse([w for w in warns if "does not support" in w])

    def test_support_warnings_are_never_errors(self):
        call = _call(dominant_signal_class="earnings_vol", win_rate=0.87,
                     win_rate_source="backtest")
        self.assertEqual(vd.validate_doc(_doc(calls=[call]), SCHEMA), [])
