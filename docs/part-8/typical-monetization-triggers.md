---
title: "Typical Monetization Triggers"
---

Institutional programs often monetize hedges when any of **three conditions occur**.

## 1. Volatility Spike

Example rule:

```text
VIX doubles from entry level
```

or

```text
VIX > 40
```

Action:

```text
sell 20 to 40% of hedge
```

Reason:

```text
volatility spikes often reverse quickly
```

## 2. Market Drawdown

Example rule:

```text
SPX -15% → monetize 25% of hedge
SPX -25% → monetize another 25%
SPX −35% → monetize most remaining protection
```

This locks in gains while retaining protection.

## 3. Hedge Value Trigger

Example rule:

```text
If hedge MTM > 5% portfolio value
→ realize partial gains
```

This prevents hedge gains from round-tripping.

Alternative rule:

When hedge value rises to

| Hedge Gain | Action           |
| ---------- | ---------------- |
| +100%      | sell 25%         |
| +200%      | sell another 25% |
| +400%      | sell another 25% |
