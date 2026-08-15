---
title: "Maturity Selection"
---

Tail hedges usually use **long-dated options**.

Typical maturities:

| Maturity       | Purpose                     |
| -------------- | --------------------------- |
| 6 to 12 months | tactical hedging            |
| ~18 months     | common institutional choice |
| ~24 months     | strong vega exposure        |

Most funds choose 18 to 24 months to provide:

```text
high vega
low theta (on a relative basis)
stable convexity
```

This is why **LEAPS are common** in institutional programs.

See [LEAPS](../part-1/exercise-settlement.md#leaps) for further details.

!!! note

    Long maturities have low theta on a relative or % basis, but the total absolute premium paid may be larger.

## Maturity / Time Ladder

Instead of a **single maturity**, some funds use a **time ladder as well**.

| Maturity  | Allocation |
| --------- | ---------- |
| 12 months | 30%        |
| 18 months | 40%        |
| 24 months | 30%        |

This smooths **roll risk**.
