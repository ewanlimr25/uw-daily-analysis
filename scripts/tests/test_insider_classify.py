"""Tests for scripts/insider_classify.py — C10 opportunistic-vs-routine insider classification."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import insider_classify as ic  # noqa: E402


class IsRoutineTest(unittest.TestCase):
    def test_routine_when_same_month_three_prior_years(self):
        prior = [(2023, 5), (2024, 5), (2025, 5)]  # traded every May
        self.assertTrue(ic.is_routine(5, prior))

    def test_opportunistic_when_fewer_than_three_prior_years(self):
        prior = [(2024, 5), (2025, 5)]  # only 2 prior Mays
        self.assertFalse(ic.is_routine(5, prior))

    def test_opportunistic_when_different_month(self):
        prior = [(2023, 5), (2024, 5), (2025, 5)]
        self.assertFalse(ic.is_routine(8, prior))  # an August trade is off-pattern


class ClassifyTransactionsTest(unittest.TestCase):
    def test_point_in_time_only_prior_years_inform(self):
        # An insider who sold every May 2023-2026; the 2026 May trade is routine (3 priors).
        txns = [ic.InsiderTxn("CFO", y, 5, -1000) for y in (2023, 2024, 2025, 2026)]
        res = ic.classify_transactions(txns)
        latest = [r for r in res if r["year"] == 2026][0]
        self.assertEqual(latest["class"], "routine")
        # The 2023 trade has no priors -> opportunistic.
        first = [r for r in res if r["year"] == 2023][0]
        self.assertEqual(first["class"], "opportunistic")

    def test_off_calendar_buy_is_opportunistic(self):
        txns = [ic.InsiderTxn("CEO", y, 5, -500) for y in (2023, 2024, 2025)]
        txns.append(ic.InsiderTxn("CEO", 2026, 11, +5000))  # a November BUY, off the May pattern
        res = ic.classify_transactions(txns)
        nov = [r for r in res if r["month"] == 11][0]
        self.assertEqual(nov["class"], "opportunistic")


class OpportunisticSignalTest(unittest.TestCase):
    def test_routine_sales_excluded_opportunistic_buy_dominates(self):
        # CFO routine May sales (info-free) + CEO opportunistic Nov buy -> signal should be BUYING.
        txns = [ic.InsiderTxn("CFO", y, 5, -1000) for y in (2023, 2024, 2025, 2026)]
        txns.append(ic.InsiderTxn("CEO", 2026, 11, +8000))  # opportunistic buy
        sig = ic.opportunistic_signal(txns)
        self.assertEqual(sig["n_routine"], 1)        # only the 2026 May sale is routine
        self.assertGreater(sig["opportunistic_mspr_like"], 0)
        self.assertEqual(sig["signal"], "buying")

    def test_unknown_when_no_opportunistic_trades(self):
        txns = [ic.InsiderTxn("CFO", y, 5, -1000) for y in (2023, 2024, 2025, 2026)]
        # the 2026 trade is routine; the 2023-2025 are opportunistic (no 3 priors), so there ARE
        # opportunistic trades -> score not None. Use a case with ALL routine instead:
        txns2 = [ic.InsiderTxn("CFO", y, 5, -1000) for y in range(2020, 2027)]
        sig = ic.opportunistic_signal(txns2)
        # 2020-2022 lack 3 priors (opportunistic); 2023+ routine. So opportunistic exist -> scored.
        self.assertIsNotNone(sig["opportunistic_mspr_like"])
        # truly-empty opportunistic set:
        self.assertIsNone(ic.opportunistic_signal([])["opportunistic_mspr_like"])
        self.assertEqual(ic.opportunistic_signal([])["signal"], "unknown")


if __name__ == "__main__":
    unittest.main()
