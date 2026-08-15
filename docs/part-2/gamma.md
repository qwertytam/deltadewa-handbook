---
title: "Gamma (Γ)"
---

Gamma measures how delta changes when the underlying price changes.

It captures the curvature of the option price with respect to the underlying.

*Example:* “ATM options have high gamma risk.”

Suppose:

```text
Initial delta = 0.30
Gamma = 0.05
```

If the stock rises by \$1:

```text
New delta = 0.35
```

If the stock rises again:

```text
New delta = 0.40
```

## Algebraic Definition for Gamma

$\Gamma = \frac{\partial^2 V}{\partial S^2}$

or equivalently

$\Gamma = \frac{\partial \Delta}{\partial S}$

## Black-Scholes expression

$\Gamma = \frac{e^{-qT} N'(d_1)}{S \sigma \sqrt{T}}$

Where:

- $N'(d_1)$ is the normal probability density function.

## Practical Interpretation for Gamma

Gamma describes **convexity**.

High gamma means:

- delta changes quickly
- option responds strongly to large moves

Properties:

- Highest ATM
- Highest short maturity
