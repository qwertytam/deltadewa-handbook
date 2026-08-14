---
title: "Structure Comparison Table"
---

| Structure       | Annual Cost         | Protection Level             | Upside Cap | Best Use Case                                  |
| --------------- | ------------------- | ---------------------------- | ---------- | ---------------------------------------------- |
| Long OTM puts   | High                | Full convexity, no cap       | None       | Core tail protection program                   |
| Put spread      | Medium              | Capped at spread width       | None       | Cost-constrained tail hedge                    |
| Collar          | Low / zero          | Limited — put provides floor | Yes        | Concentrated position risk reduction           |
| VIX derivatives | Medium              | Vol-spike exposure           | None       | Rapid crash volatility hedge                   |
| Dynamic overlay | Lower long-run cost | Moderate                     | None       | Active programs willing to monetize frequently |

Key trade-offs:

- **Long puts** maximize convexity and skew exposure but carry the highest theta cost.
- **Put spreads** reduce carry but cap the payoff in extreme crashes — the short put limits gains below its strike.
- **Collars** are approximately cost-neutral but sacrifice rally participation and create tax complexity; unsuitable as a permanent overlay.
- **VIX derivatives** can outperform in rapid crashes but have persistent roll costs in contango and high basis risk relative to portfolio losses.

