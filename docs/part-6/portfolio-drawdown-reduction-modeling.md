---
title: "Portfolio Drawdown Reduction Modeling"
---

A key goal of tail hedging is **reducing portfolio drawdowns**.

A tail hedging program should be judged on its ability to:

- reduce extreme drawdowns
- stabilize portfolio returns
- improve long-term compounding

Because of this, many institutional hedge programs measure performance primarily in terms of **portfolio tail-risk reduction** rather than hedge profit alone.

The primary quantitative tool for measuring drawdown is maximum drawdown.

#### Maximum Drawdown Formula

Maximum drawdown:

```text
MDD = (Peak − Trough) / Peak
```

Example:

```text
Portfolio peak = $10M
Portfolio trough = $7M
Drawdown = 30%
```

#### Hedged Portfolio Example

Without hedge:

```text
drawdown = 30%
```

With hedge:

```text
equity loss = −30%
hedge payoff = +15%
net drawdown = −15%
```

The hedge cut the drawdown **in half**.

#### Compound Return Improvement

Reducing drawdowns improves long-term growth because the portfolio needs smaller recoveries.

Example:

| Drawdown | Required recovery |
| -------- | ----------------- |
| −10%     | +11%              |
| −20%     | +25%              |
| −50%     | +100%             |

Tail hedging can therefore improve **compound portfolio returns** even if hedges lose money individually.

