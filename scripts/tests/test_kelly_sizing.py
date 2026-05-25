"""Tests for scripts/kelly_sizing.py — C3 expectancy + fractional-Kelly (advisory until n>=30)."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import kelly_sizing as k  # noqa: E402


class PayoffExpectancyTest(unittest.TestCase):
    def test_payoff_ratio(self):
        self.assertEqual(k.payoff_ratio(9.0, 3.0), 3.0)
        self.assertEqual(k.payoff_ratio(9.0, -3.0), 3.0)  # loss magnitude

    def test_payoff_ratio_none_without_losses(self):
        self.assertIsNone(k.payoff_ratio(9.0, 0.0))

    def test_expectancy_sign(self):
        # 55% at 3:1 payoff: 0.55*9 - 0.45*3 = 4.95 - 1.35 = +3.6 (positive EV)
        self.assertAlmostEqual(k.expectancy(0.55, 9.0, 3.0), 3.6, places=3)
        # 70% at 1:1: 0.70*1 - 0.30*1 = +0.40
        self.assertAlmostEqual(k.expectancy(0.70, 1.0, 1.0), 0.40, places=3)


class KellyTest(unittest.TestCase):
    def test_full_kelly_formula(self):
        # W=0.55, R=3 -> 0.55 - 0.45/3 = 0.55 - 0.15 = 0.40
        self.assertAlmostEqual(k.full_kelly(0.55, 3.0), 0.40, places=4)

    def test_full_kelly_zero_when_no_edge(self):
        # W=0.40, R=1 -> 0.40 - 0.60 = -0.20 (negative edge)
        self.assertLess(k.full_kelly(0.40, 1.0), 0)
        self.assertEqual(k.full_kelly(0.5, None), 0.0)
        self.assertEqual(k.full_kelly(0.5, 0.0), 0.0)

    def test_capped_half_kelly_floors_at_zero(self):
        # negative full-Kelly -> floored to 0 (don't take the trade)
        self.assertEqual(k.capped_half_kelly(0.40, 1.0), 0.0)

    def test_capped_half_kelly_halves_and_caps(self):
        # W=0.55 R=3 -> f*=0.40 -> half=0.20 -> under the 0.25 cap
        self.assertAlmostEqual(k.capped_half_kelly(0.55, 3.0), 0.20, places=4)
        # huge edge -> half-Kelly 0.474 capped at the 0.25 single-name cap (binds)
        self.assertEqual(k.capped_half_kelly(0.95, 20.0), 0.25)

    def test_55_at_3to1_dominates_70_at_1to1_on_expectancy(self):
        # The motivating C3 example is about EXPECTANCY (Kelly fraction is payoff-ratio-invariant
        # and can coincide): 55% at 3:1 (avg win 9 / loss 3) crushes 70% at 1:1 on EV.
        self.assertGreater(k.expectancy(0.55, 9.0, 3.0), k.expectancy(0.70, 1.0, 1.0))

    def test_higher_payoff_ratio_raises_kelly(self):
        # Holding W fixed, a higher payoff ratio gives a larger Kelly fraction.
        self.assertGreater(k.capped_half_kelly(0.55, 5.0), k.capped_half_kelly(0.55, 1.5))

    def test_size_bucket_mapping(self):
        self.assertEqual(k.kelly_to_size_bucket(0.0), "skip")
        self.assertEqual(k.kelly_to_size_bucket(0.40, max_fraction=0.5), "full")    # 0.8 of cap
        self.assertEqual(k.kelly_to_size_bucket(0.20, max_fraction=0.5), "half")    # 0.4 of cap
        self.assertEqual(k.kelly_to_size_bucket(0.05, max_fraction=0.5), "starter")  # 0.1 of cap


class TierExpectancyGateTest(unittest.TestCase):
    def _calls(self, spec):
        out = []
        for tier, pnls in spec.items():
            for p in pnls:
                out.append(k.ClosedCall(tier=tier, realized_pnl_pct=p, won=p > 0))
        return out

    def test_advisory_when_below_min_n(self):
        calls = self._calls({"HIGH": [3, 2], "MEDIUM": [1], "LOW": [-1]})  # n=4 < 30
        res = k.tier_expectancy_monotone(calls)
        self.assertFalse(res["activate_live_sizer"])
        self.assertEqual(res["status"], "ADVISORY_ONLY")

    def test_advisory_when_not_monotone_even_if_n_ge_30(self):
        # tier inversion (HIGH < MED) — the 2026-05-23 failure mode — must NOT activate live.
        spec = {"HIGH": [0.5] * 12, "MEDIUM": [2.0] * 12, "LOW": [0.1] * 8}  # n=32, HIGH<MED
        res = k.tier_expectancy_monotone(self._calls(spec))
        self.assertEqual(res["n_closed"], 32)
        self.assertFalse(res["monotone_high_ge_med_ge_low"])
        self.assertFalse(res["activate_live_sizer"])

    def test_live_when_monotone_and_n_ge_30(self):
        spec = {"HIGH": [3.0] * 12, "MEDIUM": [1.5] * 12, "LOW": [0.2] * 8}  # n=32, monotone
        res = k.tier_expectancy_monotone(self._calls(spec))
        self.assertEqual(res["n_closed"], 32)
        self.assertTrue(res["monotone_high_ge_med_ge_low"])
        self.assertTrue(res["activate_live_sizer"])
        self.assertEqual(res["status"], "LIVE")

    def test_advisory_when_a_tier_empty(self):
        spec = {"HIGH": [3.0] * 20, "MEDIUM": [1.0] * 15}  # no LOW closed calls
        res = k.tier_expectancy_monotone(self._calls(spec))
        self.assertFalse(res["activate_live_sizer"])

    def test_unknown_tier_calls_excluded_from_n(self):
        # DROP / watch_only calls are not sized tiers — they must not count toward n or activation.
        calls = self._calls({"HIGH": [3.0] * 12, "MEDIUM": [1.5] * 12, "LOW": [0.2] * 8})
        calls += [k.ClosedCall(tier="DROP", realized_pnl_pct=99.0, won=True) for _ in range(50)]
        res = k.tier_expectancy_monotone(calls)
        self.assertEqual(res["n_closed"], 32)  # the 50 DROP calls are excluded
        self.assertTrue(res["activate_live_sizer"])


if __name__ == "__main__":
    unittest.main()
