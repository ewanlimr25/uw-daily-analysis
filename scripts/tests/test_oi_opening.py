"""Tests for scripts/oi_opening.py — C4 OI-confirmed-opening gate."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import oi_opening as oi  # noqa: E402


class OpeningConfirmedTest(unittest.TestCase):
    def test_building_trend_confirms(self):
        self.assertTrue(oi.oi_opening_confirmed(delta_oi=None, day_contract_volume=None, oi_trend="BUILDING"))

    def test_falling_trend_rejects_even_with_high_ratio(self):
        # OI shrinking = closing-dominant, regardless of a high ΔOI/volume snapshot.
        self.assertFalse(oi.oi_opening_confirmed(delta_oi=1000, day_contract_volume=100, oi_trend="FALLING"))

    def test_ratio_above_fraction_confirms(self):
        # ΔOI 30k on 100k day volume = 0.30 >= 0.20 -> opening-dominant.
        self.assertTrue(oi.oi_opening_confirmed(delta_oi=30_000, day_contract_volume=100_000))

    def test_ratio_below_fraction_is_churn(self):
        # high volume, tiny OI change = day-trading churn, not opening.
        self.assertFalse(oi.oi_opening_confirmed(delta_oi=5_000, day_contract_volume=100_000))

    def test_negative_delta_oi_is_closing(self):
        self.assertFalse(oi.oi_opening_confirmed(delta_oi=-20_000, day_contract_volume=100_000))

    def test_fail_closed_on_missing_data(self):
        self.assertFalse(oi.oi_opening_confirmed(delta_oi=None, day_contract_volume=None, oi_trend=None))
        self.assertFalse(oi.oi_opening_confirmed(delta_oi=10_000, day_contract_volume=0))

    def test_unknown_trend_falls_through_to_ratio(self):
        # uw-pp may emit FLAT/STABLE/SIDEWAYS — the gate must fall through to the ΔOI ratio,
        # not confirm or reject on the unknown label.
        self.assertTrue(oi.oi_opening_confirmed(delta_oi=300, day_contract_volume=1000, oi_trend="SIDEWAYS"))
        self.assertFalse(oi.oi_opening_confirmed(delta_oi=100, day_contract_volume=1000, oi_trend="FLAT"))

    def test_exactly_at_fraction_confirms(self):
        self.assertTrue(oi.oi_opening_confirmed(delta_oi=200, day_contract_volume=1000))  # 0.20 == 0.20

    def test_trend_normalization_case_and_whitespace(self):
        self.assertTrue(oi.oi_opening_confirmed(delta_oi=None, day_contract_volume=None, oi_trend="  building "))


class OpeningGateSizeTest(unittest.TestCase):
    def test_gate_only_applies_to_flow_classes(self):
        r = oi.opening_gate_size("full", "dark_pool_accumulation", oi_trend="FALLING")
        self.assertFalse(r["applies"])
        self.assertEqual(r["final_size"], "full")  # untouched

    def test_unconfirmed_flow_capped_to_half(self):
        # AMD-style: bullish_flow but suppose OI churning -> cap half.
        r = oi.opening_gate_size("full", "bullish_flow", delta_oi=2_000, day_contract_volume=100_000)
        self.assertTrue(r["applies"])
        self.assertFalse(r["opening_confirmed"])
        self.assertEqual(r["final_size"], "half")

    def test_confirmed_flow_keeps_size(self):
        # AMD actual: +81k OI BUILDING -> opening confirmed -> size preserved.
        r = oi.opening_gate_size("full", "bullish_flow", oi_trend="BUILDING")
        self.assertTrue(r["opening_confirmed"])
        self.assertEqual(r["final_size"], "full")

    def test_gate_never_upgrades(self):
        # confirmed opening must not raise a starter to full.
        r = oi.opening_gate_size("starter", "bearish_flow", oi_trend="BUILDING")
        self.assertEqual(r["final_size"], "starter")

    def test_unconfirmed_below_half_unchanged(self):
        r = oi.opening_gate_size("starter", "bullish_flow", delta_oi=0, day_contract_volume=100_000)
        self.assertEqual(r["final_size"], "starter")  # already below half, cap is a no-op


if __name__ == "__main__":
    unittest.main()
