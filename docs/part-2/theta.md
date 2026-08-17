---
title: "Theta (Θ)"
---

Theta measures how option price changes as time passes.

It captures time decay.

*Example:* “Short options collect theta.”

If:

```text
theta = −0.05
```

Then the option loses:

```text
$0.05 per day
```

assuming other inputs remain constant.

## Algebraic Definition Theta

$\Theta = -\frac{\partial V}{\partial t}$

where $t$ is calendar time.

Annualising daily theta uses the day convention below. Dividing that annualised
figure by portfolio value gives **Theta Carry**, the program-level cost metric
defined in [Theta Carry / Insurance Cost](../part-6/theta-carry-insurance-cost.md).

### Theta Day Convention

Theta is usually annualized using 252 trading days in equity options markets. Some trading desks do quote using calendar year i.e., 365 days.

## Practical Interpretation of Theta

- Long options → negative theta
- Short options → positive theta

Said another way, it **costs money daily to hold long** options.

Time decay **accelerates** as expiration approaches.
