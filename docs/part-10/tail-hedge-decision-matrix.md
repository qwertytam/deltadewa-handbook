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

The words in the first two columns are bands, not impressions, and the matrix is
only executable once they are read as numbers:

| Word    | Volatility Regime (VIX) | Skew Percentile       |
| ------- | ----------------------- | --------------------- |
| Low     | < 15                    | < 30%                 |
| Normal  | 15 to 25                | 30 to 70%             |
| High    | > 25                    | > 70%                 |
| Extreme | > 40                    | > 90%, panic pricing  |

The skew percentile column is the banding owned by
[Skew Percentile](../part-3/volatility-skew.md#skew-percentile), with *Extreme*
being that page's top rung rather than a fourth band. The VIX column follows the
same cut points as the entry decision tree below.

!!! note "Monetization on this page always means partial"

    Wherever this page says to monetize, it means monetizing in stages under
    the schedule in
    [Typical Monetization Triggers](../part-8/typical-monetization-triggers.md),
    retaining a small tail position throughout. The entire hedge is never
    closed in a single transaction — see
    [Profits Versus Convexity](../part-8/profits-versus-convexity-when-to-take-and-when-to-hold.md#principles-for-deciding)
    for the rule and the reasoning.

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
VIX = 45
Skew percentile = 93%
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
| VIX > 40  | Stop — do not buy new protection; monetize per the staged schedule in Part VIII                                          |
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
- **VIX > 40: Monetize in stages, never in full** — see [Profits Versus Convexity](../part-8/profits-versus-convexity-when-to-take-and-when-to-hold.md#principles-for-deciding)
- **Term structure inverted: Roll costs lower — consider refreshing ladder earlier**
