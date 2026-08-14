---
title: "Structure 3 — Option Carry + Tail Hedge"
---

Some funds combine:

```text
short volatility income
+
long crash hedge
```

Example:

```text
sell short-dated options
buy long-dated puts
```

This attempts to **finance the hedge with volatility risk premium**.

Risks:

- See timing mismatch
- See mis-timed short gamma risk
- See margin/collateral pressure in a crisis
- See volatility carry reversal

#### Timing Mismatch

The hedge's income and protection components can be out of sync during a volatility spike, causing a timing mismatch.

#### Short Gamma Risk

The short options may be squeezed first in a volatility spike, generating losses before the long puts have moved sufficiently into profit.

#### Margin/Collateral Pressure

Even if the trade is ultimately profitable, short options can require additional margin exactly when liquidity is most constrained.

#### Volatility Carry Reversal

The See Volatility Risk Premium that funds the hedge can compress or reverse, making the income side unreliable in certain regimes.

