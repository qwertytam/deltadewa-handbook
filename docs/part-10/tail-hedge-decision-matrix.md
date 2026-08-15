---
title: "Tail Hedge Decision Matrix"
---

Institutional tail-risk programs typically adjust hedge allocation based on three key market variables:

```text
volatility level
skew level
forward volatility
```

These variables determine whether crash protection is **cheap or expensive**.

A simple decision matrix combines them.

| Volatility Regime | Skew Percentile | Forward Variance | Typical Action                 |
| ----------------- | --------------- | ---------------- | ------------------------------ |
| Low               | Low             | Low              | Aggressively accumulate hedges |
| Low               | High            | Normal           | Buy selectively                |
| Normal            | Low             | Normal           | Maintain hedge                 |
| High              | High            | High             | Avoid new purchases            |
| High              | Extreme         | High             | Monetize existing hedges       |

Example interpretation:

```text
VIX = 14
Skew percentile = 18%
Forward variance = low
```

Conclusion:

```text
protection historically cheap → increase hedge allocation
```

Conversely:

```text
VIX = 40
Skew percentile = 90%
```

Conclusion:

```text
crash protection extremely expensive → monetize hedges
```

This framework helps prevent the most common mistake:

```text
buying protection after markets already fall
```

## Entry Timing Decision Tree

The matrix above can be converted into sequential decision rules:

**Step 1 — Check VIX level:**

| VIX Level | Initial Guidance                                                                                                         |
| --------- | ------------------------------------------------------------------------------------------------------------------------ |
| VIX > 40  | Stop — monetize existing hedges; do not buy new protection                                                               |
| VIX 25–40 | Caution — avoid new purchases unless a roll is urgently required; if roll required, reduce size and consider put spreads |
| VIX 15–25 | Proceed to Step 2                                                                                                        |
| VIX < 15  | Proceed to Step 2 with increased urgency to accumulate                                                                   |

**Step 2 — Check skew percentile (if VIX ≤ 25):**

| Skew Percentile | Guidance                                                                   |
| --------------- | -------------------------------------------------------------------------- |
| > 70%           | Buy selectively or defer — deep OTM puts are expensive relative to history |
| 30–70%          | Maintain program; normal accumulation pace                                 |
| < 30%           | Accumulate more aggressively — protection is historically cheap            |

**Step 3 — Check term structure:**

| Term Structure Shape   | Guidance                                                                   |
| ---------------------- | -------------------------------------------------------------------------- |
| Inverted (crisis)      | Roll costs are lower; consider rolling sooner if positions need refreshing |
| Flat                   | Normal conditions; proceed as planned                                      |
| Steeply upward sloping | Roll costs are higher; consider reducing roll frequency or size            |

Explicit rules derived from this tree:

- **VIX > 25: Avoid new hedge purchases**
- **VIX < 15 + skew percentile < 30%: Increase allocation aggressively**
- **VIX > 40: Monetize existing positions**
- **Term structure inverted: Roll costs lower — consider refreshing ladder earlier**
