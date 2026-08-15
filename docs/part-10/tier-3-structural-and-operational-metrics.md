---
title: "Tier 3 — Structural and Operational Metrics"
---

Useful for implementation, but not critical.

## 9. Skew Exposure / Beta

See [Skew Exposure / Beta](../part-6/skew-exposure-beta.md) for details.

## 10. Net Delta Exposure

See [Net Delta](../part-6/net-delta.md) for details.

## 11. Hedge Rebalance Triggers

See [Market Rally Rebalance Triggers](../part-7/rolling-rules.md#rule-2-market-rally-rebalance-trigger) for the detailed action framework

### Trigger Definition

Hedge rebalance triggers define when the hedge program adjusts positions.

Tail hedges are rarely static; they require systematic rebalancing rules.

### Typical Trigger Types

#### 1. Time-based roll

Example:

```text
buy 18-month puts
roll when maturity < 9 months
```

Avoids entering the high theta decay zone.

#### 2. Strike drift trigger

If the market rallies:

```text
puts become very deep OTM
```

Example rule:

```text
if strike distance > 45% OTM
roll hedge closer to spot
```

#### 3. Crash monetization

If hedge value exceeds a threshold:

```text
hedge profit > 3× cost
```

Example action:

```text
sell part of hedge
lock gains
re-establish later
```

#### 4. Convexity threshold

If crash convexity falls below target:

```text
increase hedge size
```

### Trigger Interpretation

Rebalance rules ensure the hedge:

```text
maintains target convexity
controls carry cost
preserves liquidity
```
