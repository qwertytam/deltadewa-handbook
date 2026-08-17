---
title: "Structure 2 — Put Spread Tail Hedge"
---

Structure

```text
buy deep OTM put
sell further OTM put
```

Example:

```text
buy 3500 put
sell 2500 put
```

## Purpose

Reduce cost. Carry becomes:

```text
1 to 2% instead of 3 to 5%
```

Trade-off:

```text
cap extreme crash payoff
```

The capped payoff is the visible trade-off. The sold leg also consumes
collateral for as long as the position is open, must be bought back to monetise
the structure, and gives back part of the crash repricing that the long leg
earns. See [Running Structures with Sold Legs](running-structures-with-sold-legs.md).
