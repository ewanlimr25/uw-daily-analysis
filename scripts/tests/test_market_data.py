"""Tests for scripts/market_data.py — no network access (the fetcher is injected)."""

from __future__ import annotations

import json
import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import market_data as md  # noqa: E402
from excess_winrate import MIN_ADV_USD, MIN_PRICE  # noqa: E402

# 2026-07-24 = 1784908800 UTC; one session per 86400 for test purposes.
_T0 = 1784908800


def chart(closes, volumes=None, opens=None, highs=None, lows=None, start=_T0):
    """Build a Yahoo-shaped chart payload string with len(closes) sessions."""
    n = len(closes)
    volumes = volumes if volumes is not None else [1_000_000] * n
    return json.dumps(
        {
            "chart": {
                "error": None,
                "result": [
                    {
                        "timestamp": [start + i * 86400 for i in range(n)],
                        "indicators": {
                            "quote": [
                                {
                                    "open": opens if opens is not None else closes,
                                    "high": highs if highs is not None else closes,
                                    "low": lows if lows is not None else closes,
                                    "close": closes,
                                    "volume": volumes,
                                }
                            ]
                        },
                    }
                ],
            }
        }
    )


def fetcher(mapping, calls=None):
    """Return a fetch(url) that dispatches on the symbol embedded in the URL."""

    def _f(url: str) -> str:
        if calls is not None:
            calls.append(url)
        for sym, payload in mapping.items():
            if f"/chart/{sym}?" in url:
                if isinstance(payload, Exception):
                    raise payload
                return payload
        raise OSError("404 not found")

    return _f


class TestParseChart(unittest.TestCase):
    def test_parses_bars_oldest_first(self):
        bars = md.parse_chart(chart([10.0, 11.0, 12.0]))
        self.assertEqual(len(bars), 3)
        self.assertEqual(bars[0].close, 10.0)
        self.assertEqual(bars[-1].close, 12.0)
        self.assertEqual(bars[0].date, "2026-07-24")

    def test_drops_rows_with_null_close_or_volume(self):
        # A null close (halt) and a null volume (in-progress bar) must both vanish, not zero out.
        bars = md.parse_chart(chart([10.0, None, 12.0, 13.0], volumes=[1, 1, None, 4]))
        self.assertEqual([b.close for b in bars], [10.0, 13.0])

    def test_missing_ohlc_falls_back_to_close(self):
        payload = json.dumps(
            {
                "chart": {
                    "result": [
                        {
                            "timestamp": [_T0],
                            "indicators": {"quote": [{"close": [5.0], "volume": [7.0]}]},
                        }
                    ]
                }
            }
        )
        bar = md.parse_chart(payload)[0]
        self.assertEqual((bar.open, bar.high, bar.low, bar.close), (5.0, 5.0, 5.0, 5.0))

    def test_rejects_error_payload(self):
        bad = json.dumps({"chart": {"error": {"code": "Not Found"}, "result": None}})
        with self.assertRaises(ValueError):
            md.parse_chart(bad)

    def test_rejects_non_json_and_empty_result(self):
        with self.assertRaises(ValueError):
            md.parse_chart("<html>rate limited</html>")
        with self.assertRaises(ValueError):
            md.parse_chart(json.dumps({"chart": {"result": []}}))

    def test_rejects_all_null_rows(self):
        with self.assertRaises(ValueError):
            md.parse_chart(chart([None, None], volumes=[None, None]))


class TestDollarADV(unittest.TestCase):
    def test_is_dollar_volume_not_share_count(self):
        bars = md.parse_chart(chart([10.0, 10.0], volumes=[1_000_000, 3_000_000]))
        adv, n = md.dollar_adv(bars, window=2)
        self.assertEqual(n, 2)
        self.assertAlmostEqual(adv, (10e6 + 30e6) / 2)  # $20M, not 2M shares

    def test_uses_only_the_trailing_window(self):
        bars = md.parse_chart(chart([1.0] * 5 + [100.0] * 20, volumes=[1_000_000] * 25))
        adv, n = md.dollar_adv(bars, window=20)
        self.assertEqual(n, 20)
        self.assertAlmostEqual(adv, 100e6)  # the five $1 sessions are outside the window

    def test_short_history_reports_n_used(self):
        bars = md.parse_chart(chart([10.0] * 3))
        adv, n = md.dollar_adv(bars, window=20)
        self.assertEqual(n, 3)
        self.assertIsNotNone(adv)

    def test_empty_is_none(self):
        self.assertEqual(md.dollar_adv([], window=20), (None, 0))


class TestPctChange(unittest.TestCase):
    def test_one_and_five_session_returns(self):
        bars = md.parse_chart(chart([100.0, 101.0, 102.0, 103.0, 104.0, 110.0]))
        self.assertAlmostEqual(md.pct_change(bars, 1), 100 * (110 / 104 - 1))
        self.assertAlmostEqual(md.pct_change(bars, 5), 10.0)

    def test_none_when_history_too_short(self):
        bars = md.parse_chart(chart([100.0, 101.0]))
        self.assertIsNone(md.pct_change(bars, 5))

    def test_none_on_nonpositive_sessions(self):
        bars = md.parse_chart(chart([100.0, 101.0]))
        self.assertIsNone(md.pct_change(bars, 0))


class TestRealizedVol(unittest.TestCase):
    def test_zero_for_a_flat_series(self):
        bars = md.parse_chart(chart([50.0] * 25))
        self.assertAlmostEqual(md.realized_vol(bars, 20), 0.0)

    def test_annualizes_by_sqrt_252(self):
        # Alternating +/-1% closes: population stdev of log returns x sqrt(252).
        closes = [100.0 * (1.01 if i % 2 else 1.0 / 1.01) for i in range(1, 26)]
        bars = md.parse_chart(chart(closes))
        rv = md.realized_vol(bars, 20)
        rets = [math.log(b.close / a.close) for a, b in zip(bars[-21:], bars[-20:])]
        import statistics

        expected = statistics.pstdev(rets) * math.sqrt(252) * 100
        self.assertAlmostEqual(rv, expected, places=6)

    def test_none_when_too_few_returns(self):
        bars = md.parse_chart(chart([10.0, 11.0]))
        self.assertIsNone(md.realized_vol(bars, 20))


class TestC12Verdict(unittest.TestCase):
    def _data(self, close, adv):
        return md.SymbolData(
            symbol="X", available=True, last_close=close, adv_usd=adv, last_date="2026-07-24"
        )

    def test_passes_above_both_floors(self):
        ok, reason = self._data(10.0, 60e6).c12_verdict()
        self.assertTrue(ok)
        self.assertEqual(reason, "pass")

    def test_fails_sub_five_dollar_price(self):
        ok, reason = self._data(4.27, 900e6).c12_verdict()  # CBRG 2026-07-24
        self.assertFalse(ok)
        self.assertIn("< 5.00", reason)

    def test_fails_sub_floor_adv(self):
        ok, reason = self._data(12.24, 8.6e6).c12_verdict()  # LXU 2026-07-24
        self.assertFalse(ok)
        self.assertIn("$8.6M", reason)

    def test_boundary_is_inclusive(self):
        self.assertTrue(self._data(MIN_PRICE, MIN_ADV_USD).c12_verdict()[0])

    def test_fail_closed_when_unmeasurable(self):
        # The whole point of C12: a name we cannot measure is DROPPED, not passed.
        self.assertFalse(md.SymbolData("X", available=False, reason="404").c12_verdict()[0])
        self.assertFalse(self._data(None, 60e6).c12_verdict()[0])
        self.assertFalse(self._data(10.0, None).c12_verdict()[0])


class TestExceptionCoverage(unittest.TestCase):
    """http.client.HTTPException is NOT an OSError subclass, so it needs explicit coverage or it
    escapes measure() and breaks the always-exit-0 contract (review finding, reproduced live)."""

    def test_incomplete_read_is_caught_not_propagated(self):
        import http.client

        d = md.measure("X", fetch=fetcher({"X": http.client.IncompleteRead(b"partial")}))
        self.assertFalse(d.available)
        self.assertIn("IncompleteRead", d.reason)
        self.assertFalse(d.c12_verdict()[0])

    def test_bad_status_line_is_caught(self):
        import http.client

        d = md.measure("X", fetch=fetcher({"X": http.client.BadStatusLine("garbage")}))
        self.assertFalse(d.available)

    def test_http_error_and_timeout_are_caught(self):
        import urllib.error

        for exc in (
            urllib.error.HTTPError("u", 429, "Too Many Requests", {}, None),
            urllib.error.URLError("dns"),
            TimeoutError("slow"),
        ):
            self.assertFalse(md.measure("X", fetch=fetcher({"X": exc})).available)

    def test_report_survives_a_raising_fetcher_for_every_symbol(self):
        import http.client

        rep = md.build_report(
            ["A", "B"], fetch=fetcher({"A": http.client.IncompleteRead(b""), "B": OSError("x")})
        )
        self.assertEqual(rep["c12_pass"], [])
        self.assertEqual(len(rep["c12_fail"]), 2)

    def test_range_is_url_quoted(self):
        calls: list[str] = []
        md.measure("X", fetch=fetcher({"X": chart([10.0] * 3)}, calls), range_="2 mo")
        self.assertIn("range=2%20mo", calls[0])


class TestMeasureAndReport(unittest.TestCase):
    def test_measure_populates_derived_fields(self):
        f = fetcher({"BE": chart([100.0] * 20 + [184.89], volumes=[20_000_000] * 21)})
        d = md.measure("BE", fetch=f)
        self.assertTrue(d.available)
        self.assertEqual(d.last_close, 184.89)
        self.assertEqual(d.last_date, "2026-08-13")
        self.assertIsNotNone(d.adv_usd)
        self.assertIn("rv20", d.realized_vol)

    def test_measure_never_raises_on_fetch_failure(self):
        d = md.measure("NOPE", fetch=fetcher({"NOPE": OSError("HTTP 429 rate limited")}))
        self.assertFalse(d.available)
        self.assertIn("429", d.reason)
        self.assertFalse(d.c12_verdict()[0])

    def test_report_splits_pass_and_fail(self):
        f = fetcher(
            {
                "AAA": chart([100.0] * 21, volumes=[5_000_000] * 21),  # $500M ADV -> pass
                "BBB": chart([3.0] * 21, volumes=[5_000_000] * 21),  # sub-$5 -> fail
                "CCC": chart([50.0] * 21, volumes=[1_000] * 21),  # $50k ADV -> fail
                "DDD": OSError("boom"),  # unmeasurable -> fail-closed
            }
        )
        rep = md.build_report(["AAA", "BBB", "CCC", "DDD"], fetch=f)
        self.assertEqual(rep["c12_pass"], ["AAA"])
        self.assertEqual({r["symbol"] for r in rep["c12_fail"]}, {"BBB", "CCC", "DDD"})
        self.assertEqual(rep["n_requested"], 4)

    def test_report_is_json_serializable_and_skips_blanks(self):
        rep = md.build_report(["AAA", "  "], fetch=fetcher({"AAA": chart([10.0] * 21)}))
        self.assertEqual(rep["n_requested"], 1)
        json.dumps(rep)  # must not raise

    def test_caret_symbols_survive_url_quoting(self):
        calls: list[str] = []
        md.measure("^VIX", fetch=fetcher({"^VIX": chart([18.0] * 21)}, calls))
        self.assertIn("/chart/^VIX?", calls[0])

    def test_as_of_truncates_the_series_for_reproducibility(self):
        # 5 sessions from 2026-07-24; pinning to the 2nd must ignore the later three.
        f = fetcher({"X": chart([10.0, 20.0, 30.0, 40.0, 50.0])})
        pinned = md.measure("X", fetch=f, as_of="2026-07-25")
        self.assertEqual(pinned.last_date, "2026-07-25")
        self.assertEqual(pinned.last_close, 20.0)
        unpinned = md.measure("X", fetch=f)
        self.assertEqual(unpinned.last_close, 50.0)

    def test_as_of_before_all_history_fails_closed(self):
        f = fetcher({"X": chart([10.0, 20.0])})
        d = md.measure("X", fetch=f, as_of="2020-01-01")
        self.assertFalse(d.available)
        self.assertIn("as_of", d.reason)
        self.assertFalse(d.c12_verdict()[0])

    def test_as_of_changes_the_c12_verdict_when_price_crossed_the_floor(self):
        # The real 2026-07-24 CBRG case: $4.27 then (sub-$5, FAIL) -> $5.25 later (would PASS).
        f = fetcher({"CBRG": chart([4.27, 5.25], volumes=[20_000_000] * 2)})
        rep_pinned = md.build_report(["CBRG"], fetch=f, as_of="2026-07-24")
        rep_live = md.build_report(["CBRG"], fetch=f)
        self.assertEqual(rep_pinned["c12_pass"], [])
        self.assertEqual(rep_live["c12_pass"], ["CBRG"])

    def test_as_of_is_echoed_in_the_report(self):
        rep = md.build_report(["X"], fetch=fetcher({"X": chart([10.0] * 21)}), as_of="2026-07-24")
        self.assertEqual(rep["as_of"], "2026-07-24")

    def test_index_symbols_fail_c12_on_zero_volume_by_design(self):
        # ^VIX has no share volume; a 0 ADV must FAIL rather than pass or crash.
        f = fetcher({"^VIX": chart([18.58] * 21, volumes=[0] * 21)})
        rep = md.build_report(["^VIX"], fetch=f)
        self.assertEqual(rep["c12_pass"], [])
        self.assertIn("adv", rep["c12_fail"][0]["reason"])

    def test_cli_exits_zero_and_prints_json(self):
        import contextlib
        import io

        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            # Real network call is avoided: an unresolvable symbol still exits 0 by contract.
            rc = md.main(["--symbols", "___NOT_A_TICKER___", "--compact"])
        self.assertEqual(rc, 0)
        self.assertIn("c12_fail", json.loads(buf.getvalue()))


if __name__ == "__main__":
    unittest.main()
