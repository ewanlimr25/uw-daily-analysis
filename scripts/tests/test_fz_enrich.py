"""Tests for scripts/fz_enrich.py parsers, field extraction, and enrichment."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import fz_enrich as fz  # noqa: E402

AS_OF = "2026-05-27"

# Trimmed real `fz quote AAPL --agent` payload (see audit 2026-05-27-fz-edge/04 §1).
AAPL_PAYLOAD = {
    "company": "Apple Inc",
    "fundamentals": {
        "Short Float": "0.92%",
        "Short Interest": "134.68M",
        "Short Ratio": "3.05",
        "Shs Float": "14.67B",
        "Shs Outstand": "14.69B",
        "Inst Own": "66.04%",
        "Inst Trans": "0.38%",
        "Insider Own": "0.12%",
        "Insider Trans": "-1.93%",
        "Recom": "1.98",
        "Target Price": "316.07",
        "Price": "310.85",
        "RSI (14)": "78.85",
        "52W High": "311.82 -0.31%",
        "Beta": "1.08",
        "Market Cap": "4565.56B",
        "Earnings": "Apr 30 AMC",
        "P/E": "37.60",          # not in field map -> dropped
    },
}


class ParserTest(unittest.TestCase):
    def test_parse_pct(self):
        self.assertEqual(fz.parse_pct("0.92%"), 0.92)
        self.assertEqual(fz.parse_pct("-1.93%"), -1.93)
        self.assertIsNone(fz.parse_pct("-"))
        self.assertIsNone(fz.parse_pct(None))

    def test_parse_num_takes_leading_token(self):
        self.assertEqual(fz.parse_num("3.05"), 3.05)
        self.assertEqual(fz.parse_num("311.82 -0.31%"), 311.82)  # composite cell
        self.assertIsNone(fz.parse_num("-"))
        self.assertEqual(fz.parse_num(42), 42.0)

    def test_parse_human_suffixes(self):
        self.assertEqual(fz.parse_human("14.67B"), 14.67e9)
        self.assertEqual(fz.parse_human("134.68M"), 134.68e6)
        self.assertEqual(fz.parse_human("500K"), 500e3)
        self.assertIsNone(fz.parse_human("-"))


class ExtractTest(unittest.TestCase):
    def test_extract_keeps_mapped_fields_only(self):
        out = fz.extract_fields(AAPL_PAYLOAD)
        self.assertEqual(out["short_float"], "0.92%")
        self.assertEqual(out["short_ratio"], "3.05")
        self.assertEqual(out["shs_float"], "14.67B")
        self.assertEqual(out["recom"], "1.98")
        self.assertEqual(out["target_price"], "316.07")
        self.assertNotIn("pe", out)  # P/E is not in the gate field map

    def test_extract_handles_missing_fundamentals(self):
        self.assertEqual(fz.extract_fields({}), {})
        self.assertEqual(fz.extract_fields({"fundamentals": "junk"}), {})


class DeriveTest(unittest.TestCase):
    def test_derive_clean_float_low_squeeze(self):
        d = fz.derive(fz.extract_fields(AAPL_PAYLOAD))
        self.assertEqual(d["short_float_pct"], 0.92)
        self.assertEqual(d["days_to_cover"], 3.05)
        self.assertEqual(d["float_shares"], 14.67e9)
        self.assertEqual(d["squeeze_pressure"], "LOW")
        # 316.07 vs 310.85 -> +1.68%
        self.assertEqual(d["upside_to_target_pct"], 1.68)

    def test_derive_high_squeeze(self):
        d = fz.derive({"short_float": "25%", "short_ratio": "8.0"})
        self.assertEqual(d["squeeze_pressure"], "HIGH")

    def test_derive_unknown_when_absent(self):
        d = fz.derive({})
        self.assertEqual(d["squeeze_pressure"], "unknown")
        self.assertIsNone(d["upside_to_target_pct"])


class EnrichTest(unittest.TestCase):
    def test_enrich_with_injected_runner(self):
        def fake_runner(ticker, binary):
            self.assertEqual(ticker, "AAPL")
            return AAPL_PAYLOAD

        out = fz.enrich("aapl", AS_OF, runner=fake_runner)
        self.assertEqual(out["ticker"], "AAPL")
        self.assertTrue(out["available"])
        self.assertTrue(out["fz_available"])
        self.assertEqual(out["fields"]["short_float"], "0.92%")
        self.assertEqual(out["derived"]["squeeze_pressure"], "LOW")
        self.assertIn("semi-monthly", out["freshness_caveat"])

    def test_skip_payload_shape(self):
        out = fz._skip("nvda", AS_OF, "fz CLI not found")
        self.assertEqual(out["ticker"], "NVDA")
        self.assertFalse(out["available"])
        self.assertFalse(out["fz_available"])
        self.assertEqual(out["skip_reason"], "fz CLI not found")


# ---- 2026-07-04 screener-view fallback (W27 §7(8) upstream quote-grid regression) ----

# Real broken `fz quote --agent` shape observed 2026-07-04: only the FIRST snapshot
# column of the 84-field grid survives (14 valuation fields; no SI/analyst/technical).
BROKEN_QUOTE = {
    "company": "Apple Inc",
    "fundamentals": {
        "Market Cap": "4532.96B",
        "Index": "DJIA, S&P 500",
        "Book/sh": "4.35",
        "Income": "112.39B",
    },
}

# Real `fz screen --tickers AAPL --view ownership --agent` row (2026-07-04).
OWNERSHIP_ROW = {
    "Ticker": "AAPL", "Short Float": "0.98%", "Short Ratio": "2.71",
    "Float": "14.67B", "Outstanding": "14.69B",
    "Insider Own": "0.12%", "Insider Trans": "-2.21%",
    "Inst Own": "67.21%", "Inst Trans": "0.00%",
    "Price": "308.63", "Market Cap": "4532.96B",
    "Avg Volume": "53.22M", "Change": "4.84%", "Volume": "75,218,001",
}

# Real `fz screen --tickers AAPL --view technical --agent` row (2026-07-04).
TECHNICAL_ROW = {
    "Ticker": "AAPL", "RSI": "60.26", "SMA20": "4.69%", "SMA50": "5.15%",
    "SMA200": "14.02%", "52W High": "-2.76%", "52W Low": "53.17%",
    "Beta": "1.09", "ATR": "8.74", "Price": "308.63",
    "Change": "4.84%", "Volume": "75,218,001",
}


def _fake_screen(ticker, binary, view):
    return [OWNERSHIP_ROW] if view == "ownership" else [TECHNICAL_ROW]


class ScreenFallbackTest(unittest.TestCase):
    """fz 1.0.0 truncates the quote grid to the first snapshot column; the screener
    ownership/technical views still carry the SI/float/insider/technical fields.
    Analyst fields (Recom / Target Price) exist in NO view -> upstream_gaps."""

    def test_broken_quote_grid_recovers_si_and_technical_via_screen(self):
        out = fz.enrich("AAPL", AS_OF, runner=lambda t, b: BROKEN_QUOTE,
                        screen_runner=_fake_screen)
        self.assertTrue(out["available"])
        self.assertEqual(out["fields"]["short_float"], "0.98%")
        self.assertEqual(out["fields"]["short_ratio"], "2.71")
        self.assertEqual(out["fields"]["shs_float"], "14.67B")
        self.assertEqual(out["fields"]["rsi"], "60.26")
        self.assertEqual(out["derived"]["short_float_pct"], 0.98)
        self.assertEqual(out["derived"]["days_to_cover"], 2.71)
        self.assertEqual(out["derived"]["float_shares"], 14.67e9)
        self.assertEqual(out["derived"]["squeeze_pressure"], "LOW")
        self.assertIn("short_float", out["screen_fallback_used"])
        self.assertIn("rsi", out["screen_fallback_used"])

    def test_analyst_fields_reported_as_upstream_gaps(self):
        out = fz.enrich("AAPL", AS_OF, runner=lambda t, b: BROKEN_QUOTE,
                        screen_runner=_fake_screen)
        self.assertIn("recom", out["upstream_gaps"])
        self.assertIn("target_price", out["upstream_gaps"])
        # short_interest (absolute) and earnings date are equally unrecoverable
        # (no screener column) — the gap report must not under-state (review 2026-07-04).
        self.assertIn("short_interest", out["upstream_gaps"])
        self.assertIn("earnings", out["upstream_gaps"])
        self.assertIsNone(out["derived"]["recom"])
        self.assertIsNone(out["derived"]["upside_to_target_pct"])

    def test_quote_values_win_over_screen_fallback(self):
        # Intact quote grid: quote's Short Float 0.92% must survive even though the
        # ownership view says 0.98% (fallback fills gaps, never overrides).
        out = fz.enrich("AAPL", AS_OF, runner=lambda t, b: AAPL_PAYLOAD,
                        screen_runner=_fake_screen)
        self.assertEqual(out["fields"]["short_float"], "0.92%")
        self.assertEqual(out["fields"]["recom"], "1.98")
        self.assertEqual(out["upstream_gaps"], [])

    def test_screen_failure_never_blocks_enrichment(self):
        def broken_screen(ticker, binary, view):
            raise fz.FzError("screen exploded")

        out = fz.enrich("AAPL", AS_OF, runner=lambda t, b: BROKEN_QUOTE,
                        screen_runner=broken_screen)
        self.assertTrue(out["available"])  # graceful: quote-only payload
        self.assertNotIn("short_float", out["fields"])
        self.assertEqual(out["screen_fallback_used"], [])

    def test_screen_row_matched_by_ticker(self):
        def multi_row_screen(ticker, binary, view):
            other = dict(OWNERSHIP_ROW, Ticker="MSFT", **{"Short Float": "9.99%"})
            return [other, OWNERSHIP_ROW] if view == "ownership" else [TECHNICAL_ROW]

        out = fz.enrich("AAPL", AS_OF, runner=lambda t, b: BROKEN_QUOTE,
                        screen_runner=multi_row_screen)
        self.assertEqual(out["fields"]["short_float"], "0.98%")  # AAPL row, not MSFT

    def test_empty_screen_rows_tolerated(self):
        out = fz.enrich("AAPL", AS_OF, runner=lambda t, b: BROKEN_QUOTE,
                        screen_runner=lambda t, b, v: [])
        self.assertTrue(out["available"])
        self.assertNotIn("short_float", out["fields"])

    # --- 2026-08-01 audit item 5: the doubled-first-letter Ticker artifact ---
    # Live `fz screen --tickers MSFT --view ownership` returns Ticker="MMSFT".
    # Exact-equality matching rejected every row, so the ownership float never
    # reached the envelope and C16 was untestable for four audits.

    def test_screen_row_matched_despite_doubled_first_letter(self):
        def doubled(ticker, binary, view):
            if view == "ownership":
                return [dict(OWNERSHIP_ROW, Ticker="AAAPL")]
            return [dict(TECHNICAL_ROW, Ticker="AAAPL")]

        out = fz.enrich("AAPL", AS_OF, runner=lambda t, b: BROKEN_QUOTE,
                        screen_runner=doubled)
        self.assertEqual(out["fields"]["short_float"], "0.98%")
        self.assertIn("short_float", out["screen_fallback_used"])

    def test_sole_row_accepted_when_ticker_cell_unrecognisable(self):
        def mangled(ticker, binary, view):
            if view == "ownership":
                return [dict(OWNERSHIP_ROW, Ticker="???")]
            return []

        out = fz.enrich("AAPL", AS_OF, runner=lambda t, b: BROKEN_QUOTE,
                        screen_runner=mangled)
        self.assertEqual(out["fields"]["short_float"], "0.98%")

    def test_multi_row_payload_never_guesses(self):
        """The sole-row fallback must not fire when the payload is ambiguous."""
        def two_unmatched(ticker, binary, view):
            if view == "ownership":
                return [dict(OWNERSHIP_ROW, Ticker="???"),
                        dict(OWNERSHIP_ROW, Ticker="!!!")]
            return []

        out = fz.enrich("AAPL", AS_OF, runner=lambda t, b: BROKEN_QUOTE,
                        screen_runner=two_unmatched)
        self.assertNotIn("short_float", out["fields"])

    def test_row_matcher_unit(self):
        self.assertTrue(fz._screen_row_matches("MMSFT", "MSFT"))
        self.assertTrue(fz._screen_row_matches("MSFT", "MSFT"))
        self.assertTrue(fz._screen_row_matches(" aaapl ", "AAPL"))
        self.assertFalse(fz._screen_row_matches("MSFT", "AAPL"))
        self.assertFalse(fz._screen_row_matches("", "AAPL"))
        self.assertFalse(fz._screen_row_matches("AAPL", ""))


class InsiderClusterFlagTests(unittest.TestCase):
    """C18 enabler (2026-08-08 audit P1 #4).

    `fz insider-clusters` reads a LOCAL store whose Ticker cells carry the same
    upstream doubled-first-letter artifact as the screener grid (observed
    2026-08-08: 14 of 14 distinct tickers doubled -- PLTR -> PPLTR, XAIR -> XXAIR).
    Exact-equality matching therefore returned False for every ticker ever
    checked, which is why `insider_cluster_flag` was serialized 15 times and was
    `False` all 15 -- zero variance, and C18 untestable for five audits.
    """

    CLUSTERS = [
        {"Ticker": "PPLTR", "DistinctOwners": 3, "Side": "buy", "Transactions": 5},
        {"Ticker": "XXAIR", "DistinctOwners": 2, "Side": "buy", "Transactions": 2},
    ]

    def test_doubled_first_letter_ticker_matches(self):
        """The bug that blocked C18: PLTR must match the store's PPLTR row."""
        self.assertIs(
            fz.insider_cluster_flag("PLTR", runner=lambda b, d, m, s: self.CLUSTERS),
            True,
        )

    def test_undoubled_ticker_still_matches(self):
        rows = [{"Ticker": "PLTR", "DistinctOwners": 2, "Side": "buy"}]
        self.assertIs(
            fz.insider_cluster_flag("PLTR", runner=lambda b, d, m, s: rows), True
        )

    def test_absent_ticker_is_false_not_none(self):
        """checked-and-absent must be False -- the value C18 needs to contrast."""
        self.assertIs(
            fz.insider_cluster_flag("AAPL", runner=lambda b, d, m, s: self.CLUSTERS),
            False,
        )

    def test_empty_store_is_none_not_false(self):
        """An unpopulated store is a SKIPPED lane, not evidence of no cluster."""
        self.assertIsNone(
            fz.insider_cluster_flag("AAPL", runner=lambda b, d, m, s: [])
        )

    def test_fz_failure_is_none_graceful_skip(self):
        def boom(binary, days, min_buyers, side):
            raise fz.FzError("fz missing")

        self.assertIsNone(fz.insider_cluster_flag("AAPL", runner=boom))

    def test_min_buyers_threshold_respected(self):
        rows = [{"Ticker": "PPLTR", "DistinctOwners": 1, "Side": "buy"}]
        self.assertIs(
            fz.insider_cluster_flag("PLTR", min_buyers=2,
                                    runner=lambda b, d, m, s: rows),
            False,
        )

    def test_side_filter_excludes_opposite_side(self):
        rows = [{"Ticker": "PPLTR", "DistinctOwners": 3, "Side": "sell"}]
        self.assertIs(
            fz.insider_cluster_flag("PLTR", side="buy",
                                    runner=lambda b, d, m, s: rows),
            False,
        )

    def test_malformed_rows_tolerated(self):
        rows = ["not-a-dict", {"no_ticker": 1}, {"Ticker": None}]
        self.assertIs(
            fz.insider_cluster_flag("PLTR", runner=lambda b, d, m, s: rows), False
        )

    def test_blank_ticker_is_none(self):
        self.assertIsNone(
            fz.insider_cluster_flag("", runner=lambda b, d, m, s: self.CLUSTERS)
        )


if __name__ == "__main__":
    unittest.main()
