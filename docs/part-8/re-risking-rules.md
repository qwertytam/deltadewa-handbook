---
title: "Re-Risking Rules"
---

After monetization, programs usually **re-establish protection once volatility normalizes**.

Example framework:

| Condition             | Action                    |
| --------------------- | ------------------------- |
| VIX < 15              | rebuild hedge post crisis |
| Skew percentile < 30% | rebuild hedge post crisis |
| Market stabilizes     | reset strike ladder       |

Re-risking is usually **gradual**, occurring slower than normal accumulation.

Example:

```text
rebuild 50% of hedge first
add remaining when volatility stabilizes and skew reduces
```

This cycle is what allows systematic tail-hedging programs to remain sustainable over long horizons.

