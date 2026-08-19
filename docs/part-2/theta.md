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

Conventions differ. Some desks annualise daily theta over 252 trading days,
others over 365 calendar days, and the two answers differ by about 45% for the
same position — so a theta figure is not interpretable until you know which
basis produced it.

**This handbook uses 365 calendar days, and so does the deltadewa
application.** That follows from the definition above: $\Theta$ is the
derivative with respect to *calendar* time, so a calendar-day theta has to be
scaled by calendar days. Multiplying a calendar-day theta by 252 mixes the two
bases and understates annual carry by roughly 31%.

When you take a theta off a broker platform or a pricing model, check its
convention before comparing it to any figure in this handbook.

## Practical Interpretation of Theta

- Long options → negative theta
- Short options → positive theta

Said another way, it **costs money daily to hold long** options.

Time decay **accelerates** as expiration approaches.
