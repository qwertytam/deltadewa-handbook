---
title: "Convexity Budget and Premium Budget"
---

Institutional tail hedge programs typically operate under two constraints:

1. Premium Budget
2. Convexity Target

#### Premium Budget

The premium budget defines the acceptable annual cost of maintaining the hedge program.

Most institutional tail hedge programs target a premium budget in the range of 1% to 3%, with richer close-to-the-money programs reaching ~4%.

Note on cash management: premium is typically paid in advance when options are purchased. The portion of the annual hedge budget not yet deployed — for example, budget reserved for future quarterly rolls — should be held in short-duration, high-quality instruments (money market funds or short-term Treasuries) rather than left idle. At current yields, a 1–2% carry budget held in short-term Treasuries for several months before deployment generates income that partially offsets the net theta cost of the program. This is a small but real benefit that improves the program's effective economics.

#### Convexity Target

The convexity target defines the expected hedge payoff under a defined crash scenario.

Example targets:

- +3% portfolio return during a −15% equity drawdown
- +5% portfolio return during a −20% equity drawdown
- +10% portfolio return during a −30% equity drawdown

#### Implementation

Hedges are sized so that:

```text
Scenario Payoff ≥ Convexity Target  
Expected Cost ≤ Premium Budget
```

This dual-constraint approach prevents two common problems:

- Overspending on hedges that rarely pay off  
- Holding hedges that are too small to matter in a crash

