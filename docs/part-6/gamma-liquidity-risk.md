---
title: "Gamma Liquidity Risk"
---

Gamma measures how much delta changes when the market moves. Dealer positioning can strongly influence short-term market dynamics.

Dealer gamma is mostly a **short-dated flow indicator**, not a structural tail-hedging signal.

## Concept

Market makers hedge option exposure.

If dealers are ***long gamma***, they hedge by:

```text
sell rallies
buy dips
```

Result:

```text
stable markets
low realized volatility
```

If they are **short gamma**, dealers hedge by:

```text
buy rallies
sell dips
```

Result:

```text
amplified volatility
```

## Portfolio Metric Definition of Gamma Exposure

$\text{Gamma Exposure} = \sum_i \Gamma_i N_i$

Simplified dashboard approximation:

$GEX = \sum (\Gamma \times OpenInterest)$

because dealer gamma models normally include:

$GEX \approx Gamma \times OI \times contract size \times spot^2 \times 0.01$

Many sites publish estimates.

## Interpretation of Results

Dealer gamma positioning describes market-maker hedging flows rather than the hedge portfolio itself.

| Dealer gamma | Market behavior       |
| ------------ | --------------------- |
| positive     | suppressed volatility |
| negative     | unstable market       |

## Hedge Decision Rule for Gamma Liquidity

Tail funds look at dealer gamma usually as a secondary or tactical overlay, not a core allocation trigger. If they consider it, they may add hedges when:

```text
dealer gamma negative
```

Because this increases crash probability.

!!! note

    Tail hedge allocation decisions are driven primarily by volatility regime, skew levels, and the volatility term structure rather than by Gamma liquidity risk.
