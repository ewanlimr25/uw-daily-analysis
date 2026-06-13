"""Tests for scripts/excess_winrate.py — C12 liquidity floor + C2 excess/cap gate.

The candidate ADV figures below are order-of-magnitude representative, not live quotes:
the micro-ETFs that the 2026-05-20 volume_spike probe surfaced (GIF/BLCN/PEX/IGLD/UTHY/ESGE)
all clear the $5 price floor (~$24-25) but trade well under $50M/day in dollar terms — that
is precisely why they are un-fillable junk for a flow-follower. Large-caps (AMD/MU) trade
multiple $B/day. The exact ADV is fetched at runtime by the agent; these tests pin the
floor's *behavior* on the real probe tickers.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import excess_winrate as ew  # noqa: E402


class LiquidityFloorC12Test(unittest.TestCase):
    def test_micro_etfs_from_volume_spike_probe_excluded(self):
        # The exact set the volume_spike backtest returned (no floor) on 2026-05-20.
        cands = [
            ew.Candidate("GIF", price=24.48, adv_usd=2_000_000),
            ew.Candidate("BLCN", price=24.91, adv_usd=1_000_000),
            ew.Candidate("PEX", price=21.74, adv_usd=1_500_000),
            ew.Candidate("IGLD", price=23.68, adv_usd=800_000),
            ew.Candidate("UTHY", price=39.23, adv_usd=900_000),
            ew.Candidate("ESGE", price=51.34, adv_usd=3_000_000),
        ]
        kept, excluded = ew.apply_liquidity_floor(cands)
        self.assertEqual(kept, [])
        self.assertEqual({c.ticker for c in excluded},
                         {"GIF", "BLCN", "PEX", "IGLD", "UTHY", "ESGE"})

    def test_large_caps_kept(self):
        cands = [
            ew.Candidate("AMD", price=447.58, adv_usd=10_000_000_000),
            ew.Candidate("MU", price=731.99, adv_usd=3_000_000_000),
        ]
        kept, excluded = ew.apply_liquidity_floor(cands)
        self.assertEqual({c.ticker for c in kept}, {"AMD", "MU"})
        self.assertEqual(excluded, [])

    def test_price_floor_catches_sub_5(self):
        # A liquid-by-ADV name under $5 still fails (e.g. MNTK $1.55 from the live screener).
        cands = [ew.Candidate("MNTK", price=1.55, adv_usd=100_000_000)]
        kept, excluded = ew.apply_liquidity_floor(cands)
        self.assertEqual(kept, [])
        self.assertEqual([c.ticker for c in excluded], ["MNTK"])

    def test_exactly_at_floor_passes(self):
        cands = [ew.Candidate("EDGE", price=5.0, adv_usd=ew.MIN_ADV_USD)]
        kept, _ = ew.apply_liquidity_floor(cands)
        self.assertEqual([c.ticker for c in kept], ["EDGE"])

    def test_fail_closed_on_missing_data(self):
        # Unverifiable liquidity fails closed — the desk cannot size what it cannot measure,
        # and an unverified name must not inflate the win-rate denominator.
        self.assertFalse(ew.passes_liquidity_floor(ew.Candidate("X", price=None, adv_usd=1e12)))
        self.assertFalse(ew.passes_liquidity_floor(ew.Candidate("Y", price=100.0, adv_usd=None)))

    def test_win_rate_denominator_excludes_floored_junk(self):
        # Before: 9-name volume_spike set scores the class on junk. After: floor first,
        # then compute WR only over tradable, graded names.
        cands = [
            ew.Candidate("GIF", price=24.48, adv_usd=2_000_000, won=False),
            ew.Candidate("BLCN", price=24.91, adv_usd=1_000_000, won=False),
            ew.Candidate("AMD", price=447.58, adv_usd=10_000_000_000, won=True),
            ew.Candidate("MU", price=731.99, adv_usd=3_000_000_000, won=True),
        ]
        kept, _ = ew.apply_liquidity_floor(cands)
        wins, n, wr = ew.compute_win_rate(kept)
        self.assertEqual((wins, n), (2, 2))  # only AMD/MU counted
        self.assertEqual(wr, 1.0)

    def test_win_rate_none_when_no_graded(self):
        # n == 0 -> win_rate is None; callers MUST guard before threshold comparison.
        kept = [ew.Candidate("A", price=100.0, adv_usd=1e9)]  # won=None (ungraded)
        wins, n, wr = ew.compute_win_rate(kept)
        self.assertEqual((wins, n), (0, 0))
        self.assertIsNone(wr)

    def test_empty_input_partitions_cleanly(self):
        kept, excluded = ew.apply_liquidity_floor([])
        self.assertEqual((kept, excluded), ([], []))

    def test_partition_is_complementary(self):
        # kept + excluded must cover the input exactly once (single-pass partition).
        cands = [
            ew.Candidate("AMD", price=447.0, adv_usd=10_000_000_000),
            ew.Candidate("GIF", price=24.48, adv_usd=2_000_000),
            ew.Candidate("MU", price=731.0, adv_usd=3_000_000_000),
        ]
        kept, excluded = ew.apply_liquidity_floor(cands)
        self.assertEqual(len(kept) + len(excluded), len(cands))
        self.assertEqual({c.ticker for c in kept} | {c.ticker for c in excluded},
                         {"AMD", "GIF", "MU"})


class NConditionalCapC2Test(unittest.TestCase):
    def test_n_below_10_tightened_to_069(self):
        # The C2 fix: n<10 caps at 0.69 (was 0.75) -> below the 0.70 full-size line.
        self.assertEqual(ew.n_conditional_cap(1.00, 8), 0.69)
        self.assertEqual(ew.n_conditional_cap(0.60, 8), 0.60)  # cap never raises a low WR

    def test_n_10_plus_caps_at_absolute_ceiling(self):
        # 2026-06-06 audit P0.1: the prior 0.85/0.90 tiers re-permitted quotes the
        # 2026-05-30 P1.2 ceiling bans (11 post-register rows quoted 0.837-0.933,
        # decided 0-for-3). All n >= 10 now cap at the 0.80 absolute ceiling.
        self.assertEqual(ew.n_conditional_cap(1.00, 12), 0.80)
        self.assertEqual(ew.n_conditional_cap(1.00, 25), 0.80)
        self.assertEqual(ew.n_conditional_cap(0.50, 25), 0.50)

    def test_no_n_path_exceeds_absolute_ceiling(self):
        # Design lock: no sample size, however large, earns a quote above 0.80.
        for n in (1, 9, 10, 19, 20, 49, 89, 1000):
            self.assertLessEqual(ew.n_conditional_cap(1.00, n), ew.ABSOLUTE_WR_CEILING)

    def test_069_cap_maps_to_half_not_full(self):
        self.assertEqual(ew.size_from_winrate(0.69), "half")
        self.assertEqual(ew.size_from_winrate(0.70), "full")


class MarketExcessGateC2Test(unittest.TestCase):
    def test_bullish_flow_uptape_demoted_from_full(self):
        # MEASURED before/after. Live bullish_flow probe: n=8, raw 100%, in an UPTREND where
        # SPY rose over both signal windows -> SPY-long benchmark WR ~1.0 -> excess ~0.
        # BEFORE (old 0.75 cap, no excess gate): 0.75 -> FULL.
        self.assertEqual(ew.size_from_winrate(min(1.00, 0.75)), "full")
        # AFTER: N-cap tightened (0.69 -> half) AND excess gate (excess 0 -> cap half).
        d = ew.size_decision(1.00, 8, benchmark_win_rate=1.00)
        self.assertEqual(d["capped_win_rate"], 0.69)
        self.assertEqual(d["base_size"], "half")
        self.assertEqual(d["excess"], 0.0)
        self.assertEqual(d["final_size"], "half")  # no class full-sizes on a single up-week

    def test_genuine_edge_keeps_full(self):
        # A well-sampled signal that beats the market keeps full size; the quote is
        # bounded at the 0.80 ceiling but 0.80 still clears the 0.70 full line.
        d = ew.size_decision(0.82, 25, benchmark_win_rate=0.55)
        self.assertEqual(d["capped_win_rate"], 0.80)
        self.assertEqual(d["base_size"], "full")
        self.assertGreater(d["excess"], 0)
        self.assertEqual(d["final_size"], "full")

    def test_short_in_uptape_handled_by_raw_floor_not_excess(self):
        # bearish_flow probe: raw 0.286 (short). SPY-short benchmark in an up-tape ~0.0, so
        # excess is POSITIVE (+0.286) -- shorting beat blindly shorting SPY. But raw 0.286 < 0.50
        # so the ladder already floors it to starter; the excess gate must not upgrade it.
        d = ew.size_decision(0.286, 7, benchmark_win_rate=0.0)
        self.assertEqual(d["base_size"], "starter")
        self.assertGreater(d["excess"], 0)
        self.assertEqual(d["final_size"], "starter")

    def test_materially_negative_excess_drops_to_starter(self):
        # Signal underperforms the same-direction market bet by >=10pp -> starter even if raw WR
        # would otherwise size half.
        d = ew.size_decision(0.55, 15, benchmark_win_rate=0.80)
        self.assertEqual(d["base_size"], "half")
        self.assertLessEqual(d["excess"], ew.MATERIALLY_NEGATIVE_EXCESS)
        self.assertEqual(d["final_size"], "starter")

    def test_excess_gate_only_downgrades_never_upgrades(self):
        # Positive excess on a sub-0.50 raw WR must not lift it above starter.
        d = ew.size_decision(0.40, 30, benchmark_win_rate=0.10)
        self.assertEqual(d["final_size"], "starter")

    def test_liquidity_floor_short_circuits_to_skip(self):
        d = ew.size_decision(0.90, 25, benchmark_win_rate=0.40, liquidity_ok=False)
        self.assertEqual(d["final_size"], "skip")
        self.assertEqual(d["excess_gate"], "below_liquidity_floor")

    def test_excess_uses_raw_not_capped_winrate(self):
        # Design lock: excess is RAW signal WR - benchmark, NOT capped WR - benchmark.
        # n=8 raw 1.00 (cap 0.69), benchmark 0.95: raw excess = +0.05 (no penalty);
        # had we used capped, excess would be 0.69-0.95 = -0.26 -> starter. We use raw.
        d = ew.size_decision(1.00, 8, benchmark_win_rate=0.95)
        self.assertEqual(d["excess"], 0.05)
        self.assertEqual(d["base_size"], "half")   # from the 0.69 N-cap
        self.assertEqual(d["final_size"], "half")  # +0.05 excess -> no downgrade

    def test_no_benchmark_falls_back_to_ladder_only(self):
        # When SPY benchmark is unavailable, size on the (tightened-capped) ladder alone.
        d = ew.size_decision(1.00, 8, benchmark_win_rate=None)
        self.assertEqual(d["final_size"], "half")  # 0.69 cap still demotes from full
        self.assertEqual(d["excess_gate"], "no_benchmark")


if __name__ == "__main__":
    unittest.main()
