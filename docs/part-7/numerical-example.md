---
title: "Numerical Example"
---

Suppose:

```text
Equity portfolio = $10M
Annual hedge budget = 2%
```

So hedge budget is:

```text
$200k per year
```

#### Strike Ladder Structure

See [example strike ladder](strike-selection.md#the-strike-ladder-concept).

#### Crash Scenario Simulation

| SPX move | Hedge payoff |
| -------- | ------------ |
| -10%     | small        |
| -20%     | \$400k        |
| -30%     | \$1.3M        |
| -40%     | \$3M+         |

See also See [Example tail hedge payoff structure](../part-5/convexity.md#example-tail-hedge-payoff-structure).

The hedge doesn't eliminate losses, but it **dramatically reduces drawdown**.

