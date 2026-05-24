"""Tests for scripts/finnhub_enrich.py pure transforms and assessment."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import finnhub_enrich as fe  # noqa: E402

AS_OF = "2026-05-23"


class TransformTest(unittest.TestCase):
    def test_summarize_metrics_keeps_numeric_only(self):
        resp = {"metric": {"peBasicExclExtraTTM": 30.5, "roeTTM": 0.42,
                           "totalDebt/totalEquityAnnual": 55.0, "junk": "n/a", "missing": None}}
        out = fe.summarize_metrics(resp)
        self.assertEqual(out["pe_ttm"], 30.5)
        self.assertEqual(out["debt_to_equity"], 55.0)
        self.assertNotIn("junk", out)

    def test_summarize_earnings_lookahead_guard_and_order(self):
        rows = [
            {"period": "2026-06-30", "surprisePercent": 5.0},   # future → dropped
            {"period": "2026-03-31", "surprisePercent": 2.0},
            {"period": "2025-12-31", "surprisePercent": -1.0},
        ]
        out = fe.summarize_earnings(rows, AS_OF)
        self.assertEqual([r["period"] for r in out], ["2026-03-31", "2025-12-31"])

    def test_summarize_insider_filters_future_and_sorts(self):
        resp = {"data": [
            {"year": 2026, "month": 7, "mspr": 40},   # future → dropped
            {"year": 2026, "month": 4, "mspr": -35},
            {"year": 2026, "month": 3, "mspr": -30},
        ]}
        out = fe.summarize_insider(resp, AS_OF)
        self.assertEqual([(r["year"], r["month"]) for r in out], [(2026, 3), (2026, 4)])

    def test_summarize_news_caps_and_orders(self):
        articles = [{"datetime": 1000 + i, "headline": f"h{i}", "summary": "x" * 400}
                    for i in range(30)]
        out = fe.summarize_news(articles, AS_OF)
        self.assertEqual(len(out), fe.MAX_NEWS)
        self.assertEqual(out[0]["headline"], "h29")  # newest first
        self.assertLessEqual(len(out[0]["summary"]), 280)

    def test_next_earnings_date_picks_earliest_future(self):
        resp = {"earningsCalendar": [{"date": "2026-08-20"}, {"date": "2026-05-28"},
                                     {"date": "2026-02-01"}]}
        self.assertEqual(fe.next_earnings_date(resp, AS_OF), "2026-05-28")


class AssessTest(unittest.TestCase):
    def test_miss_streak_and_imminent_earnings_and_selling(self):
        earnings = [{"period": f"2026-0{q}-01", "surprise_pct": -3.0} for q in (4, 3, 2, 1)]
        insider = [{"year": 2026, "month": m, "mspr": -40} for m in (2, 3, 4)]
        out = fe.assess({"debt_to_equity": 250.0, "rev_growth_yoy": -8.0},
                        earnings, insider, "2026-05-28", AS_OF)
        self.assertEqual(out["earnings_trend"], "miss_streak")
        self.assertEqual(out["insider_signal"], "selling")
        self.assertEqual(out["leverage_flag"], "elevated")
        self.assertEqual(out["days_to_earnings"], 5)
        self.assertTrue(any("earnings in 5d" in c for c in out["caution_flags"]))
        self.assertTrue(any("MSPR" in b for b in out["bearish_factors"]))
        self.assertTrue(any("negative revenue growth" in b for b in out["bearish_factors"]))

    def test_beat_streak_and_buying(self):
        earnings = [{"period": f"2026-0{q}-01", "surprise_pct": 4.0} for q in (4, 3, 2, 1)]
        insider = [{"year": 2026, "month": m, "mspr": 35} for m in (2, 3, 4)]
        out = fe.assess({"rev_growth_yoy": 25.0}, earnings, insider, None, AS_OF)
        self.assertEqual(out["earnings_trend"], "beat_streak")
        self.assertEqual(out["insider_signal"], "buying")
        self.assertIsNone(out["days_to_earnings"])
        self.assertTrue(any("revenue growth" in b for b in out["bullish_factors"]))

    def test_unknown_when_empty(self):
        out = fe.assess({}, [], [], None, AS_OF)
        self.assertEqual(out["earnings_trend"], "unknown")
        self.assertEqual(out["insider_signal"], "unknown")
        self.assertEqual(out["leverage_flag"], "unknown")


class EnrichTest(unittest.TestCase):
    def test_enrich_with_injected_getter(self):
        def fake_getter(url):
            if "/stock/metric" in url:
                return {"metric": {"peBasicExclExtraTTM": 28.0, "rev_growth_yoy": 12.0}}
            if "/stock/earnings" in url:
                return [{"period": "2026-03-31", "surprisePercent": 3.0}]
            if "/stock/insider-sentiment" in url:
                return {"data": [{"year": 2026, "month": 4, "mspr": 10}]}
            if "/company-news" in url:
                return [{"datetime": 1747000000, "headline": "Upgrade", "source": "X"}]
            if "/calendar/earnings" in url:
                return {"earningsCalendar": [{"date": "2026-06-15"}]}
            raise AssertionError(f"unexpected url {url}")

        out = fe.enrich("nvda", AS_OF, 14, "KEY", getter=fake_getter)
        self.assertEqual(out["ticker"], "NVDA")
        self.assertTrue(out["available"])
        self.assertEqual(out["metrics"]["pe_ttm"], 28.0)
        self.assertEqual(out["assessment"]["next_earnings_date"], "2026-06-15")
        self.assertEqual(out["errors"], [])

    def test_premium_endpoint_degrades_gracefully(self):
        def fake_getter(url):
            if "/stock/metric" in url:
                raise fe.FinnhubPremiumError("403")
            return {} if "calendar" in url or "insider" in url else []
        out = fe.enrich("AAPL", AS_OF, 7, "KEY", getter=fake_getter)
        self.assertTrue(out["available"])
        self.assertEqual(out["metrics"], {})
        self.assertTrue(any("requires paid plan" in e for e in out["errors"]))

    def test_is_us_ticker(self):
        self.assertTrue(fe.is_us_ticker("NVDA"))
        self.assertFalse(fe.is_us_ticker("SHOP.TO"))


if __name__ == "__main__":
    unittest.main()
