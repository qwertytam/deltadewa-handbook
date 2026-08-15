---
title: "Institutional Hedge Dashboards"
---

Running a tail-hedge program day to day means condensing everything in the earlier parts — Greeks, volatility regime, structure design, sizing — into a small set of numbers that can be checked at a glance.

This part assembles those numbers into a **dashboard**, organized by priority:

| Tier | Focus                    | Example metrics                                      |
| ---- | ------------------------ | ---------------------------------------------------- |
| 1    | Core hedge economics     | Crash convexity, theta carry, vega sufficiency       |
| 2    | Market environment       | Volatility regime, skew percentile, forward variance |
| 3    | Structural / operational | Skew exposure, net delta, rebalance triggers         |
| 4    | Tactical / optional      | Liquidity risk, delta drift, vega term exposure      |

A decision matrix ties the Tier 2 environment metrics together into simple guidance — when protection is historically cheap versus expensive — and a worked dashboard example shows how the full set reads in practice.

The goal is the same instinct repeated throughout the handbook: **buy protection when it is cheap and calm, not after markets have already fallen.**
