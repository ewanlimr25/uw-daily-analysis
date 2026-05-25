"""Tests for scripts/vol_regime_scaler.py — C5 (VRP percentile) + C9 (term-slope) scalers."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import vol_regime_scaler as v  # noqa: E402


class TercileTest(unittest.TestCase):
    def test_boundaries(self):
        self.assertEqual(v.tercile(0.0), "LOW")
        self.assertEqual(v.tercile(1 / 3), "LOW")     # <= 1/3
        self.assertEqual(v.tercile(0.5), "MID")
        self.assertEqual(v.tercile(2 / 3), "HIGH")    # >= 2/3
        self.assertEqual(v.tercile(1.0), "HIGH")


class PremiumSellingScalarTest(unittest.TestCase):
    def test_rich_vrp_full_sell(self):
        r = v.premium_selling_scalar(0.90)
        self.assertEqual(r["vrp_tercile"], "HIGH")
        self.assertEqual(r["scalar"], 1.0)
        self.assertTrue(r["advisory"])

    def test_cheap_vrp_stand_aside(self):
        r = v.premium_selling_scalar(0.10)
        self.assertEqual(r["vrp_tercile"], "LOW")
        self.assertEqual(r["scalar"], 0.0)

    def test_mid_vrp_half(self):
        self.assertEqual(v.premium_selling_scalar(0.5)["scalar"], 0.5)

    def test_steep_slope_derisks_rich_vrp(self):
        # rich VRP would be 1.0, but a HIGH slope-percentile (steep backwardation) trims to 0.5.
        r = v.premium_selling_scalar(0.90, slope_percentile=0.90)
        self.assertEqual(r["vrp_tercile"], "HIGH")
        self.assertEqual(r["slope_tercile"], "HIGH")
        self.assertEqual(r["scalar"], 0.5)

    def test_none_vrp_advisory_no_scalar(self):
        r = v.premium_selling_scalar(None)
        self.assertIsNone(r["scalar"])
        self.assertTrue(r["advisory"])


class TercileMonotoneGateTest(unittest.TestCase):
    def test_advisory_below_min_n(self):
        wr = {"LOW": 0.4, "MID": 0.5, "HIGH": 0.6}
        n = {"LOW": 5, "MID": 5, "HIGH": 5}  # n=15 < 30
        res = v.tercile_winrate_monotone(wr, n)
        self.assertFalse(res["activate_live_scaler"])
        self.assertEqual(res["status"], "ADVISORY_ONLY")

    def test_advisory_when_not_monotone(self):
        wr = {"LOW": 0.6, "MID": 0.4, "HIGH": 0.5}  # not monotone
        n = {"LOW": 12, "MID": 12, "HIGH": 12}
        res = v.tercile_winrate_monotone(wr, n)
        self.assertFalse(res["monotone_high_ge_mid_ge_low"])
        self.assertFalse(res["activate_live_scaler"])

    def test_live_when_monotone_and_n_ge_30(self):
        wr = {"LOW": 0.40, "MID": 0.55, "HIGH": 0.70}
        n = {"LOW": 12, "MID": 12, "HIGH": 12}  # n=36
        res = v.tercile_winrate_monotone(wr, n)
        self.assertTrue(res["monotone_high_ge_mid_ge_low"])
        self.assertTrue(res["activate_live_scaler"])
        self.assertEqual(res["status"], "LIVE")

    def test_advisory_when_a_tercile_missing(self):
        wr = {"LOW": 0.4, "HIGH": 0.7}  # MID missing -> None
        n = {"LOW": 20, "HIGH": 20}
        res = v.tercile_winrate_monotone(wr, n)
        self.assertFalse(res["activate_live_scaler"])


if __name__ == "__main__":
    unittest.main()
