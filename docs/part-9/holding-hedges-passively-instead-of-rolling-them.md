---
title: "Holding Hedges Passively Instead Of Rolling Them"
---

A common error by investors is to:

```text
buy 2-year puts
wait
watch them decay
```

Professional hedge programs **continuously manage maturity and strike**.

Why? Because time decay accelerates dramatically as options approach expiry.

For ATM options, Theta and Gamma roughly scale with:

$\Theta \propto \frac{1}{\sqrt{T}}$

$\Gamma \propto \frac{1}{\sqrt{T}}$

for ATM options under Black-Scholes.

Tail funds typically **roll hedges before this decay phase**.

