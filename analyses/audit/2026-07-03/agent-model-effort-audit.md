# Fleet Model & Effort Audit — 2026-07-03

**Scope:** the 16 project-local agents in `.claude/agents/` as used by `/daily-analysis` and `/weekly-analysis`, plus the orchestrating session itself.
**Question:** what `model:` and `effort:` should each agent pin, instead of inheriting the session model (currently Claude Fable 5 — premium tier) into every spawn.
**Method:** one analyst per agent (armed with the agent's full definition file, the 2026-07-02 live-run telemetry, and the calibration-audit history), then a three-lens adversarial judge panel (calibration-risk / cost-efficiency / mechanics), then synthesis. Raw matrix + verdicts: `agent-model-audit-matrix.json` (this folder). Config mechanics verified against current Claude Code docs (sub-agents.md).
**Status: APPLIED 2026-07-03** (user-approved same day). All 16 frontmatter pins live; the four supporting edits (accumulation-hunter closing-cross rule, weekly Model-routing rewrite + annotation strip, daily-analysis routing pointer, gamma-flip-tracker prose fix) are in. §6 migration governance is now the active obligation: the next `/calibration-audit` must add the model-transition section.

---

## 0. Verified config mechanics (this determines what's implementable)

- `model:` frontmatter in `.claude/agents/*.md` — accepts aliases **`sonnet` / `opus` / `haiku` / `fable`**, full model IDs, or `inherit`. **Default when omitted = `inherit`** → every agent today runs on the session model. Precedence: `CLAUDE_CODE_SUBAGENT_MODEL` env > per-invocation `model` param > frontmatter > session model.
- `effort:` frontmatter — **exists** (v2.1.x): `low` / `medium` / `high` / `xhigh` / `max` (availability varies by model). Inherits session when omitted; **overrides session when set**. This is the per-agent reasoning dial.
- Extended-thinking on/off itself inherits from the session with **no per-agent override** — `effort` is the only per-agent knob.
- **Consequence 1:** the weekly command's "Model routing" table (lines 37–60) is *mechanically inert as written* — "Pass the model assignment in each agent's prompt header (`Model: claude-sonnet-4-6, extended_thinking: false`)" does not change the spawned model. Every weekly run to date has run the whole fleet on the inherited session model, same as daily. The table is also stale (retired model name, thinking-on/off era).
- **Consequence 2:** frontmatter pins apply to ad-hoc invocations too ("show me sweeps" → sweep-tracker), which is desirable: several Phase-1 downgrades are safe *partly because* Phase-2 gates re-audit their feeds, and ad-hoc use has no such backstop — a pinned floor keeps ad-hoc behavior sane.

## 1. Evidence base

**2026-07-02 live run (all agents on inherited Fable, ~1.43M subagent tokens/run):**

| Agent | Tokens | Tools | Wall-clock | Spawns/run |
|---|---|---|---|---|
| signal-confluence-quant | 124.7k | 14 | 926s | 1 |
| accumulation-hunter | 123.7k | 29 | 357s | 1 |
| leap-positioning-radar | 103.4k | 24 | 240s | 1 |
| contrarian-scanner | 88.8k | 18 | 227s | 1 |
| multileg-strategist | 80.4k | 15 | 279s | 1 |
| sweep-tracker | 79.5k | 12 | 226s | 1 |
| vol-surface-scout | 77.5k | 16 | 493s | 1 |
| earnings-scout | 67.7k | 12 | 278s | 1 |
| risk-monitor | 66.2k | 13 | 253s | 1 |
| sector-rotation-strategist | 64.6k | 3 (batched) | 197s | 1 |
| fundamentals-gate | 60.7k | 14 | 271s | 1 |
| dealer-positioning-strategist | 60.3k | 20 | 329s | 1 |
| gamma-flip-tracker | 54.0k | 11 | 172s | 1 |
| bull-researcher | 26–38k each | 0–4 | 71–147s | **5** |
| bear-researcher | 26–38k each | 0–3 | 52–129s | **5** |
| opex-pin-strategist | (not spawned; ~1 wk/month) | — | — | 0–1 |

Debate pair ≈ **300k tokens/run aggregate** — the largest cost block after the quant. Weekly cadence ≈ 5 daily + 1 weekly runs ≈ **8.6M subagent tokens/week**, all currently at premium rates.

**Audit-history anchors used by every analyst:** the dealer +3 line was demoted/mechanized (P0.4) because pre-mechanization output scored levels as flips; a vol-lane win-rate cap leaked at emission (P0.1); Phase-1 agents once wrote files/watchlists unprompted (W23 incident → standing no-file-writes rule); quant compliance measured ~perfect on the inherited premium model (06-20 audit); the calibration loop grades every emitted number, so honest refusals > fluent overclaims.

## 2. Final configuration (synthesis of matrix + judge panel)

| Agent | `model:` | `effort:` | Was (matrix / judges) | Deciding logic |
|---|---|---|---|---|
| **signal-confluence-quant** | **fable** | **high** | fable/high; cost lens argued opus | **Maximum blast radius**: every win_rate, tier, size, Σ-invariant, and score component in `decision.json` originates here; /calibration-audit grades each emission; documented failure classes (Σ mismatch, cap leaks, double-counted conflicts) are silent-drift shaped. ~20 interacting hard rules (clean-query protocol, union-median thresholds, three stacking caps). "Compliance ~perfect" was measured **on the premium tier** — the one place not to run the experiment. 125k tok/run marginal cost is a rounding error vs the risk. |
| **risk-monitor** | **fable** | **high** | fable/high; cost lens argued opus | Terminal sizing node, **only state-mutating agent** (watchlist feeds tomorrow's correlation/exit loop), 9-key gate verdicts whose *content* (not presence) is what the schema can't validate — wrong no-ops are uncatchable downstream. Second-most protocol-dense file. 66k tok/run to insure the whole pipeline's last gate. |
| **multileg-strategist** | **opus** | **high** | opus/high; cost lens argued sonnet | The one Phase-1 exception kept above sonnet. Its skill is structure *inference* (boxes vs conviction, ratio ladders, BWB attribution, refuse-to-infer on ambiguous sides) — pattern-recognition skepticism, the fastest-degrading capability class — and it feeds the **+2 line, the largest live award and the only line that put a name above the floor on 07-02**. Failure direction is symmetric and nothing downstream re-reads the chains. Budget fallback: sonnet/high. |
| **accumulation-hunter** | **sonnet**¹ | **high** | opus/high; cost lens: sonnet conditional | ¹ **Conditional on a 5-line file edit first** (§4): the 07-02 closing-cross catch (20:00–20:22Z prints = quarter-start benchmark flow, not accumulation) was verified by the judges as the *only genuinely unwritten* judgment win in Phase 1 — codify it, and every remaining duty (≥50 matrix floor, tier gate, C28 floors, C19 side discipline) is a bright-line rule sonnet holds. Until the edit lands: **opus/high**. Feeds the load-bearing +3 conjunction, but the quant independently re-verifies the cum-flow leg. |
| sweep-tracker | sonnet | high | sonnet/high (unanimous) | 0-point since P0.3; residual scored surface is the C4 `opening_confirmed` tag (quant caps flow classes on it) and the hedge-flow filter — ~10 written rules, well inside sonnet range. High (not medium) effort: the conditional-verification fetches (index cum-flow checks) are the first casualty of a thin budget. |
| contrarian-scanner | sonnet | high | sonnet/high (unanimous) | One frozen −2 line, C13-routed and re-audited by the quant; VRP abort, trajectory reconstruction, continuation-vs-fade mechanism all spelled out verbatim in the file. |
| earnings-scout | sonnet | high | sonnet/high (unanimous) | Hygiene protocol is fully proceduralized (0DTE drop, tenor floors, manual kink reads); feeds one +1 line; risk-monitor re-applies the panic gate independently. |
| dealer-positioning-strategist | sonnet | high | opus/high; cost lens: sonnet — adopted | Weakest opus case per the judges: the scored feed is a **fully mechanized two-condition test** (sign-run count + 0.25×-median floor) with exact dated-citation evidence strings. The mechanization exists precisely so a mid-tier model can execute it; the celebrated 07-02 refusals were numeric threshold comparisons. |
| sector-rotation-strategist | sonnet | high | sonnet/high (unanimous) | ETF tape is advisory; the +1 leader line is triple-gated downstream. The XLI-split diagnosis was judgment, hence high effort — the stale "mostly mechanical / thinking off" label is wrong. |
| vol-surface-scout | sonnet | **high** (floor: high, not medium) | sonnet/high; risk lens hardened the floor | The fake-kink class (AMAT/ARM/ASML simultaneous wing artifact) is a **correlated** failure that would emit multiple false +1 flags at once and contaminate earnings-scout; the quant never re-reads vol surfaces. Do not run this one at medium. |
| leap-positioning-radar | sonnet | high | opus/high; cost lens: sonnet — adopted | Fail-closed by design (9 gates, required-gate short-circuits); the cheap failure direction is conservative — a missed candidate costs opportunity, not calibration poison. The financing/borrow-synthetic screens are written rules. |
| fundamentals-gate | sonnet | high | opus/high; cost lens: sonnet — adopted | The judgment catches that argued for opus (merger-arb VETO, same-day catalyst contradiction) are now codified duties (memory + file); NA-never-penalizes and the ≥2-of-3 contradiction test are bright lines; debate + risk gates sit downstream. |
| bull-researcher | sonnet | high | pair row: opus/high; split resolved §3 | See §3 — symmetric with bear, escalation trigger pre-registered. |
| bear-researcher | sonnet | high | pair row: opus/high; split resolved §3 | See §3. Never let bear capability fall below bull. |
| gamma-flip-tracker | sonnet | medium | sonnet/medium; risk lens floor = medium | Smallest blast radius (prose-only §2 advisory, 0 points, schema-excluded from `calls[]`) — but it authors the typed `next_session_gex` block the weekly backtest machine-grades, so medium (not low) is the floor. |
| opex-pin-strategist | sonnet | medium | sonnet/medium (unanimous) | Rule-based ranking; but the sign-floored formula (`max(gex_at_pin,0)`, the pre-P1.5 bug class) is protocol arithmetic during the one week its +1 line is live — medium, not low. |
| **Orchestrator (the session running the commands)** | **fable** (opus minimum) | session default | — | Step-0 funnel + liquidity floor, confluence gating, cross-agent synthesis, report authoring, and **envelope authoring against a strict schema** (the 07-02 run needed a validator-fix cycle even on Fable). The two `model: fable` pins make Phase 2's core immune to a cheaper session, but Step 0/3/7/9 quality still tracks the session model. |

**Haiku: viable nowhere.** The cost lens explicitly tested the two best candidates (gamma-flip, opex-pin) and rejected both — each emits typed/enum output with no downstream validator, and haiku's documented weaknesses (multi-constraint compliance, refusing-to-overclaim) map one-to-one onto this fleet's failure history.

## 3. The debate pair — the decision that needed adjudication

Analyst said opus/high (pair), with prose floating a bear=opus / bull=sonnet split. The risk lens **rejected the split with an arithmetic argument that stands**: the gate is the literal comparison `bear_residual ≥ bull_residual` — the bear never adjusts the bull's number, so an inflated sonnet bull at 0.95 defeats an honest opus bear. Capability must stay **symmetric**. The cost lens identified the pair as the largest lever in the fleet (10 spawns/run, ~1.9M tokens/week) and noted the 47-line contracts already encode the residual grid, verbatim-quote requirement, and round-lowering rule.

**Adopted: both sides sonnet/high, symmetric, with two pre-registered guards:**
1. **Escalation trigger (next `/calibration-audit`, model-transition section):** if the debate-residual distribution degrades vs the premium-era baseline — bull first-round residuals inflating to ≥0.85 on names that subsequently lose, or bear residuals collapsing toward the 0.55 bin — escalate **both** sides to opus/high. (Premium-era baseline now on record: bulls 0.55–0.65, bears 0.75–0.85, two consecutive honest 5/5 sweeps.)
2. **Optional mechanical guard in risk-monitor:** flag/cap any first-round `bull_residual ≥ 0.90` (sycophancy tripwire) so an inflated bull cannot unilaterally raise the bar the bear must clear.

Conservative alternative if the desk prefers zero debate-quality risk: both opus/high (~+0.9M premium-tier tokens/week vs adopted).

## 4. Required file edits (propose-only; the config is incomplete without them)

1. **All 16 agent files:** add `model:` + `effort:` frontmatter per §2. (Precedent exists: `calibration-audit.md` already pins `model: opus`.)
2. **`accumulation-hunter.md` — BEFORE its sonnet pin goes live:** add the closing-cross rule, e.g.
   > *DP prints clustered in the ~20:00–20:25Z window at closing-cross prices are benchmark/rebalance flow (quarter-start, index events), NOT stealth accumulation — exclude them from the mega/block-tier read and note the exclusion. (2026-07-02 lesson: the entire mega-tier buy tape was closing-cross flow.)*
3. **`weekly-analysis.md`:** delete/rewrite the "Model routing" section (lines 37–60) — the prompt-header mechanism is inert and the table contradicts the new single source of truth — and strip the `(sonnet, thinking off/on)` annotations from per-agent section headers. Replace with one line: *"Models and effort are pinned per-agent in `.claude/agents/*.md` frontmatter; run the orchestrating session on fable (opus minimum)."*
4. **`daily-analysis.md`:** add the same one-line pointer (it currently has no model language at all).
5. **`gamma-flip-tracker.md` line ~10:** reword the "runs thinking-OFF as a mechanical level read" prose — configuration-by-assertion in a body is the same inert-config class as the weekly table; keep the merge-decline rationale, drop the config claim.
6. **Optional tripwire:** Step 0 of both commands asserts the session model and warns before Phase 2 if the session is below opus (protects orchestrator-level synthesis; the two fable pins already protect the quant/risk core).

## 5. Cost impact (directional — Fable list pricing not public)

Per daily run (~1.43M subagent tokens): **~87% of fleet tokens move off the premium tier** — fable retains ~191k (quant + risk-monitor), opus ~80k (multileg; +124k accumulation-hunter during the transitional period), sonnet ~1.16M. At representative tier ratios (sonnet 1×, opus ~1.7×, fable ≥2.5×), fleet model spend drops roughly **45–60% per run** while wall-clock likely *improves* (sonnet latency < fable on the long-pole quant is the exception — it stays fable). The debate-pair move alone (~300k tokens/run × 10 spawns) is the single largest saving; the two fable pins cost ~13% of tokens and buy insurance on 100% of the envelope.

## 6. Migration governance (both risk and cost lenses converged on this)

- Apply as **one batch**, then require the next `/calibration-audit` to add a **model-transition section**: re-measure quant compliance (Σ invariant, 0.80 cap-at-emission, flow_conflict firing rate — even though the quant didn't move, the *inputs* it audits did), debate-residual distributions vs the premium baseline above, veto/caution FP rate, and spot-check C4 `opening_confirmed` evidence strings against raw ΔOI.
- The W23 no-file-writes rule has **never been load-tested on a sonnet-majority Phase 1** — keep the hard-rule block in every spawn prompt (current command practice) and treat any unprompted write as an immediate escalation-to-opus signal for that agent.
- Floors (`minimum_safe` in the matrix JSON) are for degraded-capacity operation only — each floor documented re-opens the exact failure class it names. Don't run at floors to save money; the savings are already taken at the recommended tiers.

## 7. What the judges corrected (for the record)

- **Anchoring bias confirmed:** five analyst rationales justified opus with "the cost delta is trivial at 1 spawn/run" — individually true, collectively ~3.5M opus tokens/week. Downgrades adopted for dealer-positioning, leap-radar, fundamentals-gate (+ conditional accumulation-hunter): in each case the "judgment win" was traced to a *written rule* the premium model was executing, not free-form judgment.
- **The mechanics judge's "effort is unimplementable" finding was overruled** by doc verification: `effort:` frontmatter exists and overrides the session. Its structural findings (inert weekly table, split the pair rows, fix gamma-flip prose, ad-hoc exposure) were adopted.
- **`model: fable` is a documented alias** — used directly rather than `inherit` + session-dependency, so the quant and risk-monitor stay premium even if a future session runs cheaper. (Tradeoff: ad-hoc invocations of these two also bill premium. That is the correct default for the only envelope-writing and state-mutating agents.)
