---
title: "Running Structures with Sold Legs"
---

Three of the structures in this Part sell an option: the put spread
([Structure 2](structure-2-put-spread-tail-hedge.md)), the option-carry overlay
([Structure 3](structure-3-option-carry-tail-hedge.md)) and the collar
([Structure 6](structure-6-collar-strategy.md)). Each is presented there as a
payoff shape, which is the right way to compare structures and an incomplete
way to decide whether a program can run one.

A payoff diagram is drawn at expiration and says nothing about the intervening
years. A sold leg consumes buying power, changes what happens when the market
moves against the position, and behaves differently under stress from the long
leg it was meant to subsidise. Those are the questions this page covers. They
apply to any structure with a sold leg and are independent of who is running it.

## How a Sold Leg Consumes Buying Power

A long option is paid for once. A sold option creates an open-ended obligation,
and the account must carry collateral against it for as long as it is open. That
collateral is not a cost in the sense that premium is a cost — it is returned
when the position closes — but it is capital that cannot be doing anything else,
and it is the constraint that most often decides whether a structure is
practical.

Two frameworks exist for computing it, and they answer different questions.

### Strategy-Based Margin

Regulation T governs the credit a broker-dealer may extend, but for
exchange-listed options it does not set the amount. It defers to the rules of
the exchange or securities association on which the option trades
[[Reg T]](../footnotes/index.md#cfr-220-12-options). For members of FINRA, those
rules are Rule 4210, and the resulting framework is called **strategy-based**
margin: each recognised position type has its own formula.

The two formulas that matter here
[[FINRA Rule 4210]](../footnotes/index.md#finra-4210):

- **A recognised spread.** The long leg must be paid for in full. The premium
  received on the short leg may be applied against that cost, and the margin
  required on the short leg is the *lesser of* the uncovered-short requirement
  or the spread's maximum potential loss. For a put spread whose legs share an
  expiration — or whose long leg expires no earlier than the short — the maximum
  loss is capped at the net debit already paid, so the position collapses to
  "paid for in full, nothing further". This is the case usually meant when a put
  spread is described as requiring no margin.
- **An uncovered short.** Where the position does not qualify as a spread, the
  short leg is margined on its own: the current market value of the option plus
  a percentage of the underlying index value, reduced by any amount by which the
  option is out of the money, and floored at the option's market value plus a
  smaller percentage. For broad-based index options the rule sets those
  percentages at 15% and 10% respectively. Narrow-based index and single-equity
  options carry different, generally higher, figures — the broad-based pair
  should not be generalised beyond broad-based indices.

Two structural traps follow from the difference between those two formulas, and
both are easy to walk into while believing the position is a spread:

!!! warning

    A structure only receives spread treatment if it qualifies as a spread under
    the applicable rule. Two common cases do not. A **diagonal or calendar**
    whose short leg outlives its long leg leaves the short leg uncovered for the
    period after the long leg expires. And a **short index call written against
    a diversified equity portfolio** is not covered by that portfolio the way a
    single-stock covered call is covered by its shares: the portfolio is not the
    deliverable, and a cash-settled index option has no deliverable at all. An
    operator should establish how their own margin regime treats an index collar
    before assuming the short call is free.

### Portfolio Margin

Portfolio margin replaces the per-strategy formulas with a risk calculation. The
positions are revalued under a range of hypothetical moves in the underlying,
using a theoretical pricing model, and the requirement is set by the worst
result across that range
[[FINRA 4210 Interpretations]](../footnotes/index.md#finra-4210-interps).

The difference in principle is that strategy-based margin asks *what kind of
position is this*, while portfolio margin asks *what would this position lose*.
For a hedged book the second question usually gives the friendlier answer,
because a long put and a short put at a lower strike genuinely do offset, and a
formula applied leg by leg cannot see that.

Three properties of the regime are worth stating, because they are what an
operator is actually choosing between:

- **The stress range is neither symmetric nor uniform.** For a
  high-capitalisation broad-based index the range is −8% to +6%; for a
  non-high-capitalisation broad-based index it is −10% to +10%. It is not a
  single plus-or-minus figure, and quoting one misstates the rule.
- **Eligibility has a floor.** The regime carries a minimum account equity,
  tiered by whether the firm has full real-time intraday monitoring capability.
  It is not available to every account that would benefit from it.
- **The requirement is not fixed.** It is computed from current prices and
  volatility inputs, so it moves as those move.

That last property deserves the most attention, because it inverts in exactly
the wrong conditions. A risk-based requirement is smallest when volatility is
low and the book looks well hedged, and it rises as volatility expands and the
stress scenarios reprice. A program that sized its short legs against a
calm-market requirement can find that requirement materially larger during the
event the hedge was bought for — the same event that is making the long legs
valuable. Firms with real-time monitoring may recompute and call for collateral
during the session rather than overnight.

!!! note

    Regulatory minimums are floors, not the amount any given broker will
    require. Firms routinely impose house requirements above them, and may raise
    those requirements during a volatility event. The questions to settle before
    running a sold leg are: which regime applies, what the requirement is under
    it today, what it becomes under a severe move, and what the account would
    liquidate to meet a call. The handbook cannot answer any of these — they
    depend on arrangements specific to the program.

## Executing the Legs

A multi-leg structure can reach the market two ways, and the choice matters more
in a fast market than in a calm one.

A **complex order** is a single order specifying every leg and a net price. The
exchange defines it as the concurrent execution of two or more series in the
same underlying for the same account, entered to accomplish one strategy, and
routes it to a book that matches it as a package
[[Cboe Complex Orders]](../footnotes/index.md#cboe-complex-orders). Either the
whole structure executes at the net price, or none of it does.

**Legging in** means working each leg as its own order. It can capture a better
combined price when the market is quiet, because each leg can be worked against
its own bid-ask spread rather than accepting the net quote.

The trade-off is legging risk: the exposure between the first fill and the last.
A partially executed put spread is not a cheaper put spread — it is an outright
long put, or worse, a naked short put, until the second leg fills. In a fast
market that interval is precisely when spreads widen and quotes thin, so the
strategy that looked cheaper in a calm market is the one that fails when it
matters. The general principle:

!!! note

    Establish and unwind multi-leg structures as complex orders at a net price.
    Leg in only when the market is calm, the size is small relative to displayed
    liquidity, and an unintended single-leg position would be tolerable if the
    second leg never filled.

Unwinding deserves the same discipline for a further reason. Monetising a put
spread requires buying back the short leg, and in a crash the short leg is the
one whose implied volatility has expanded most. Selling the long leg first and
leaving the short leg open converts a hedge into a naked short put at the moment
of maximum volatility — the single worst position to hold involuntarily.

## What a Sold Leg Does to Crash Convexity

The obvious cost of the short leg is the capped payoff, which
[Structure 2](structure-2-put-spread-tail-hedge.md) already states. There is a
second, less visible effect that only appears once the structure is repriced
properly in a crash.

In a sell-off the put wing steepens: deep out-of-the-money index puts gain more
implied volatility than at-the-money ones. That steepening is what makes a long
tail ladder valuable, and
[A4 Crash Repricing Methodology](../appendices/a4-crash-repricing-methodology.md)
models it explicitly. A put spread sells the *deeper* strike — the leg that sits
furthest into the steepening part of the surface, and therefore the leg whose
value expands fastest.

The consequence is that a put spread captures a smaller share of the skew
steepening than its strike distance alone suggests. Both legs gain implied
volatility; the sold leg's gain is subtracted. The wider the spread and the
deeper the sold strike, the more of the crash repricing is given back at exactly
the point where the long leg is working hardest. This does not make put spreads
unsuitable — it means their crash convexity should be assessed by repricing both
legs at crash volatilities, never by comparing strike distances or by scaling an
outright put's payoff.
