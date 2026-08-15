---
title: "Tier 1 — Core Hedge Metrics"
---

These determine hedge effectiveness and the core economics.

#### 1. Crash Convexity Chart

How much payoff in large crashes.

See [Crash Convexity](../part-6/crash-convexity.md) for further detail.

#### 2. Crash Scenario Table & Payoff Ratio

The table simulates portfolio performance under market crashes.

##### Table Structure

| SPX Move | Portfolio P&L | Hedge P&L | Net P&L |
| -------- | ------------- | --------- | ------- |
| +20%     | +\$2.0M        | -\$45k     | +\$1.95M |
| +10%     | +\$1.0M        | -\$30k     | +\$970k  |
| -5%      | -\$500k        | +\$30k     | -\$470k  |
| -10%     | -\$1M          | +\$120k    | -\$880k  |
| -20%     | -\$2M          | +\$650k    | -\$1.35M |
| -35%     | -\$3.5M        | +\$2M      | -\$1.5M  |

See [Example tail hedge payoff structure](#2-crash-scenario-table-payoff-ratio)

##### Key Insight

Options produce convex payoffs:

- small moves → small protection
- crashes → accelerating (convex) hedge payoff

This convex structure is the foundation of tail hedging [[Gateway/GIA]](../footnotes/index.md#gateway).

See [Crash Payoff Ratio / Tail Hedge Effectiveness](../part-6/crash-payoff-ratio-tail-hedge-effectiveness.md) for details on payoff ratio.

#### 3. Theta Carry (Insurance Cost)

See [Theta Carry / Insurance Cost](../part-6/theta-carry-insurance-cost.md)

#### 4. Vega Sufficiency Gauge

See [Vega Sufficiency](../part-6/vega-sufficiency.md) for definition details.

##### Dashboard Display

```text
VEGA SUFFICIENCY

Low <-----|-----> High
          ^
        current
```

#### 5. Carry vs. Convexity Chart

This is the **core trade-off in tail hedging**. It determines **whether the hedge economics are attractive**.

```text
maximize convexity
minimize carry
```

See [Crash Convexity](../part-6/crash-convexity.md) and See [Theta Carry](../part-6/theta-carry-insurance-cost.md) for definitions of convexity and carry.

##### Mathematical Definition of the Ratio

$\text{Carry-Convexity Ratio} = \frac{\text{Convexity}}{\text{Carry}}$

<a id="convexity-carry-worked-example"></a>

If crash convexity at −25% SPX is 22% and annual carry is 3%, then the ratio is:

```text
22% / 3% = 7.3
```

##### Interpretation of the Ratio

| Ratio  | Meaning    |
| ------ | ---------- |
| < 3    | poor hedge |
| 3 to 6 | acceptable |
| > 6    | attractive |

Tail funds prefer **high convexity relative to cost**.

Typical values:

| Metric          | Typical hedge    |
| --------------- | ---------------- |
| Carry           | 1 to 3% per year |
| Crash convexity | 15 to 40%        |

##### Dashboard Visualization

```text
Convexity
   ^
   |
   |      GOOD
   |
   |
   | BAD
   +------------------> Carry
```

Best hedges sit **top-left**.

