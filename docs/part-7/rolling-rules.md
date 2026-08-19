---
title: "Rolling Rules"
---

As discussed in See [Volatility Roll Yield](volatility-roll-yield.md) above, total carry includes theta decay, roll yield, and transaction costs. The rolling rules below operate within that framework.

Most programs roll on **time or moneyness triggers**. Hedge programs rarely hold options to expiry.

Most institutional programs use time-based rolling as the primary rule.

## Rule 1 — Time-Based Roll { #rule-1-time-based-roll }

Rolling early preserves **convexity per dollar of cost**.

Typical roll rule:

```text
buy 18-month puts
roll when 9 to 12 months remain
```

Alternatively:

```text
Maintain constant 12‑month maturity
Roll every quarter
```

Advantages:

```text
stable exposure
predictable carry
```

This avoids rolling just before theta acceleration in the final weeks of option life. As time decreases, decay increases rapidly.

Note on the gamma-theta trade-off: the standard time-based roll rule is designed for puts that are still deep OTM. However, if the market has declined modestly during the holding period and the puts have moved closer to the money, the position accumulates favorable gamma — meaning the hedge is becoming more responsive to further declines. In this specific case, rolling mechanically at the 9-months-remaining trigger may sacrifice a valuable gamma position. Investors may reasonably choose to delay the roll by several weeks if (a) the time trigger is not yet urgent and (b) the put has moved meaningfully nearer to the money. The key check is whether crash convexity at current spot still meets the IPS target; if it does, the hold decision has a logical basis.

!!! note
    Roll timing here is expressed as **remaining** maturity, not elapsed time
    since purchase. Any tool or dashboard that automates this rule should
    confirm its own trigger measures time-to-maturity, not time held, before
    relying on it.

## Rule 2 — Market Rally Rebalance Trigger { #rule-2-market-rally-rebalance-trigger }

See [Hedge Rebalance Triggers](../part-10/tier-3-structural-and-operational-metrics.md#11-hedge-rebalance-triggers) in Part X for how this trigger integrates with the dashboard monitoring framework.

When the market rallies significantly after a hedge is established, several effects compound against the existing position:

1. **Delta collapses.** A put originally 20% OTM may now be effectively 30–40% OTM. Its delta approaches zero and it provides almost no portfolio offset.
2. **Crash convexity deteriorates.** A put with strike at 4,000 when SPX was at 5,000 now requires a ~33% decline from SPX 6,000 to be in-the-money — far beyond the original 20% crash scenario the hedge was sized for.
3. **Theta continues to erode.** The daily cost is unchanged, but the protection purchased is now materially weaker than at inception.

The primary metric to monitor is whether **crash convexity at the current spot** still meets the program's IPS target. If it does not, that is the action trigger — regardless of time remaining or calendar roll rules.

| Market Rally from Hedge Entry | Recommended Action                                                                            |
| ----------------------------- | --------------------------------------------------------------------------------------------- |
| +5 to +10%                    | Monitor — recompute crash convexity at current spot                                           |
| +10 to +15%                   | Review trigger — if convexity target is no longer met, consider rolling strikes up            |
| +15 to +20%                   | Action trigger — strikes are likely too deep OTM; roll the ladder closer to current spot      |
| > +20%                        | Urgent rebalance — original strikes may provide negligible protection; close and re-establish |

**Response options when the trigger is reached:**

- **Roll up to new strikes** — sell the existing deep OTM puts (recouping remaining time and vol value) and buy new puts at a strike appropriate to the current spot level. This resets the hedge at higher cost but restores the crash convexity target.
- **Accept the cost and hold** — if the market rally is viewed as temporary and budget is exhausted, holding existing puts avoids transaction costs but accepts a temporary gap in protection.
- **Convert to a collar** — if premium budget is fully spent, selling an OTM call at the new higher market level can fund a higher-strike protective put at minimal net cost, though upside participation is capped.

Note that rolling up after a rally realizes the carry loss on the original position and resets the hedge at a higher premium. The total carry cost should be recomputed including the realized loss and new premium before deciding whether the roll is within budget.

Rebalancing should be gradual to avoid excessive trading costs.

### Cost of a Roll-Up: Worked Example

Rolling up after a 15% market rally involves selling puts that have lost most of their value and buying new puts at a higher strike that are more expensive. The combined cost often exceeds the original premium paid:

```text
Original hedge (SPX = 5,000):
  Strike: 4,000 put (20% OTM)
  Premium paid: ~$15,000 per contract

After a 15% rally (SPX = 5,750):
  Current value of 4,000 put: ~$2,000 per contract (most value has decayed and delta collapsed)

New hedge (to restore 20% OTM protection):
  Strike: 4,600 put (20% OTM from 5,750)
  Premium: ~$18,000 per contract

Net cost of the roll-up:
  Realized loss on original: $15,000 − $2,000 = $13,000
  New premium: $18,000
  Total cost: ~$31,000 per contract
```

This effectively doubles the carry cost relative to the original hedge entry. Before executing, the investor should confirm this total cost is within the IPS carry budget. If it is not, a partial roll-up (rolling only the nearest-to-money tranche of the ladder) or switching to a put spread for the new position can reduce the cash outlay.

### IPS Exception Clause for Roll-Up Budget Overruns

A strict annual premium cap — whatever [band](typical-hedge-program-targets.md#annual-premium-budget-bands) the program has adopted — can be breached mid-year by a single roll-up after a large equity rally. The IPS should include an explicit exception clause to handle this, so the decision is governed rather than improvised under time pressure.

Suggested IPS language:

> *In the event that a market rally of 15% or more triggers a required re-strike of the hedge ladder, the investment committee is authorized to fund the roll-up cost from one of the following sources, in order of preference: (1) realized equity gains generated during the same rally period; (2) a temporary increase in the annual hedge budget not to exceed an additional 1% of AUM in the calendar year; (3) use of a put spread structure for the new position to reduce net premium outlay. Any exception must be documented and reviewed at the next quarterly hedge program report.*

The key principle: the family office has generated meaningful equity profits in a 15%+ rally. Funding the roll-up from a small portion of those profits is economically coherent — it is the cost of resetting protection on a more valuable portfolio, not an unrelated expense.

### Entry Conditions After a Rally

A practical benefit that partially offsets the higher roll-up cost: a market that has rallied 15% is typically accompanied by lower VIX and, often, lower skew percentile. This means the **conditions for re-establishing protection may be favorable** — precisely the market environment the See [Entry Timing Decision Tree](../part-10/tail-hedge-decision-matrix.md#entry-timing-decision-tree) identifies as ideal for accumulating hedges. Investors should check VIX and skew percentile before executing the roll-up. If VIX has fallen below 15 and skew is below the 30th percentile, the cost of the new position may be lower per unit of crash convexity than the original entry, partially compensating for the realized loss on the old hedge.

## Rule 3 — Crash Monetization

See [Monetizing crashes](../part-8/typical-monetization-triggers.md) for detail.

## Alternative Rules

### Delta-Based Rolling

Example rule:

```text
Roll if the absolute value of option delta exceeds 0.60
```

This prevents hedges from turning into **deep ITM positions**.

### Volatility-Regime Rolling

Example rule:

```text
If VIX < 15 → increase hedge exposure
If VIX 15 to 25 → no action
If VIX 25 to 40 → monetize some part of hedge
If VIX > 40 → look to liquidate hedge in full
```

This rule helps control the long-term carry cost of the hedge program.

### What to Do When Skew Is Expensive

Rolling hedges when skew is elevated (skew percentile above 70%) can significantly increase effective carry cost. Several approaches can mitigate this:

1. **Delay the roll** by several weeks if the roll is not urgently required by time or moneyness triggers. Skew often reverts after volatility spikes, and waiting for a quieter period can reduce the cost of the new hedge materially.
2. **Reduce size at the roll** — buy a smaller position than the full target at expensive skew, then supplement when skew normalizes. This leaves the program temporarily underhedged but reduces carry cost.
3. **Use a put spread for the new position** — when skew is expensive, selling a further OTM put partially offsets the inflated premium at the cost of capping the payoff in an extreme crash.
4. **Roll only part of the position** — if the program has a time ladder across multiple maturities, only roll the tranches that must be rolled and defer the rest.

The guiding principle: a systematic program does not need to roll mechanically on a fixed calendar date. A range of several weeks on either side of the target roll date is acceptable and can save meaningful premium cost when markets are stressed.
