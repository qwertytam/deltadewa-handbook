---
title: "Charm"
---

Charm measures how delta changes as time passes.

$\text{Charm} = \frac{\partial^2 V}{\partial S\ \partial t}$

Where:

- $\tau = T - t$
- $\tau$ is time to expiry, decreasing
- \$T$ total maturity
- \$t$ calendar time, moving forward

Interpretation:

Even if price does not move:

- Delta drifts over time.

In practice, charm is what causes put deltas to drift toward zero as expiration approaches even without price movement — creating the need for rolling that See PART VII discusses.

