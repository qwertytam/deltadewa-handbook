---
title: "Structure 4 — Volatility Instrument Hedge"
---

Instead of SPX puts, funds may use:

```text
VIX futures
VIX options
variance swaps
```

Reason: Volatility spikes faster than price drops.

Example:

```text
SPX -20%
VIX 20 → 70
```

These strategies require **more active management**.

Note: Variance swaps are traded OTC and typically require ISDA master agreements, limiting their access to only larger, more sophisticated institutions.

#### Comparing VIX Derivatives to SPX Puts

| Dimension                | SPX Puts                 | VIX Futures / Options                                  |
| ------------------------ | ------------------------ | ------------------------------------------------------ |
| What they protect        | Portfolio dollar losses  | Volatility spikes                                      |
| Payoff mechanism         | Delta + vega + skew      | Pure vol exposure                                      |
| Basis risk               | Low (for SPX portfolios) | High — vol can spike without proportional drawdown     |
| Roll cost                | Low in low-vol regimes   | Persistent contango in VIX futures generates roll cost |
| Active management needed | Moderate                 | High                                                   |
| Liquidity in a crash     | Deep                     | Can thin out significantly                             |

VIX instruments can be effective when the primary concern is a sharp, rapid volatility spike rather than a sustained drawdown. They can outperform SPX puts in very fast crashes but underperform in slow-grinding bear markets where volatility rises only moderately (e.g., 2022).

#### Trend-Following as a Tail Hedge Complement

An increasingly common approach among institutional allocators is to allocate a portion of the portfolio to **managed futures or trend-following strategies** alongside or instead of options-based tail hedges. These strategies:

- Carry no theta cost — they are not option-based
- Tend to perform well in prolonged trending markets, including sustained equity downturns
- Have historically provided diversification during extended bear markets such as 2008 and 2022
- Do not provide convex payoffs — protection scales approximately linearly with trend duration, not with crash velocity

The primary limitation is that trend-following does not provide the fast, convex payoff that options generate in rapid crashes. In a fast crash (e.g., 2020), trend strategies may be whipsawed before they can establish a short position. Options provide protection from the first day of the crash; trend strategies need time.

A hybrid approach — a reduced options allocation supplemented by a managed futures allocation — can lower overall carry cost while maintaining crash protection across both fast and slow bear market regimes.

