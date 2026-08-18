---
title: "Realized Carry Methodology"
---

Realized carry is what the hedge **actually cost** over a period that has
already happened, measured from the program's own position history. It is a
backward-looking accounting figure, and it is the only one of the handbook's
three carry measures that can be reconciled against a brokerage statement.

See [Ratio Disambiguation](../part-6/ratio-disambiguation.md) for how it differs
from the other two. The distinction matters more than it sounds: the three
numbers answer different questions, are computed from different inputs, and will
not agree.

| Measure | Direction | Computed from | Answers |
| --- | --- | --- | --- |
| [Theta Carry](../part-6/theta-carry-insurance-cost.md) | Forward | The current book's model Greeks | What is this book accruing per day, right now? |
| Annual carry budget (backtesting) | Hypothetical | A simulated roll schedule over history | What would this design have cost? |
| **Realized carry** | Backward | Actual fills and actual marks | What did this program cost? |

## Why a Separate Measure Is Needed

Theta is a model derivative of a book that exists today. Extrapolating it over a
past period answers "what would this cost have been, had the book been this book
the whole time and had the model been right" — which is not a question anyone
asked. Three things break the extrapolation:

- **The book changed.** Rolls, additions and monetizations mean the position
  accruing theta in March was not the position accruing it in September.
- **The model is not the market.** Realized decay differs from modelled decay
  whenever implied volatility moves, and the term structure adds a roll-yield
  component that theta does not see — see
  [Volatility Roll Yield](volatility-roll-yield.md).
- **Frictions are real and theta has none.** Commissions, exchange fees and the
  bid-ask spread crossed on every roll are pure cost, and they are invisible to
  any Greek.

A program that reports theta-derived carry as though it were realized cost will
understate what it spent, and will be unable to explain the difference when
someone reconciles against the statements.

## The Identity

Over a period from $t_0$ to $t_1$, let:

$V_0$ = mark-to-market value of the hedge book at $t_0$

$V_1$ = mark-to-market value of the hedge book at $t_1$

$P$ = total cash **paid** for hedge positions opened during the period,
including commissions and fees

$R$ = total cash **received** from hedge positions closed, expired or assigned
during the period, net of commissions and fees

Then the realized cost of carrying the hedge over that period is:

$$\text{Realized Carry}_{\$} = V_0 + P - R - V_1$$

Expressed against the portfolio and annualised:

$$\text{Realized Carry} = \frac{V_0 + P - R - V_1}{\text{Portfolio Value}}
\times \frac{365}{\text{Days in Period}}$$

The identity is worth reading twice, because it is the whole method. Value that
entered the book — the opening mark plus everything bought — less value that
left it, either as cash out the door or as the closing mark. Everything else on
this page is bookkeeping in service of getting those four terms right.

!!! note

    The sign convention is that a **positive** realized carry is a cost. In a
    crash the term $R - V_1$ can dominate and the figure goes negative, which
    is correct: the hedge paid, and that period's carry was a gain. A program
    that reports carry as a strictly positive number has hidden its best
    quarter.

## What the Position History Must Record

The identity needs actual fills, not intentions. Every event that moves cash or
changes the book must be recorded with its date, and at minimum:

| Event | What must be captured |
| --- | --- |
| Open | Contract, quantity, premium paid, commissions and fees |
| Close (full or partial) | Contract, quantity closed, proceeds received, costs |
| Expiry worthless | Contract, quantity, and the fact that proceeds were zero |
| Exercise or assignment | Settlement amount and direction; see [Exercise & Settlement](../part-1/exercise-settlement.md) |
| Roll | Recorded as **two** events — see below |
| Period-end mark | Every open position, marked on a stated and consistent basis |

The last row is the one most often skipped and the one that most often breaks
the number.

### Rolls Are Two Events, Not One

A roll closes one position and opens another. Recording it as a single "roll
cost" of the net debit loses the information needed to attribute cost later: how
much was received for the expiring position, how much was paid for the new one,
and what the spread cost to cross. Record the close and the open separately,
each at its own fill price, even when the broker executed them as one net-priced
package — see
[Legging In](../appendices/a1-additional-terminology.md#legging-in) for why the
package price is not the same thing as two independent fills.

The net debit remains recoverable by subtraction. The reverse is not true.

### Partial Closes Need a Cost Basis Rule

Selling a quarter of a rung requires deciding which quarter was sold. The
realized-carry identity does not care — $R$ is the cash received either way —
but any per-position attribution built on top of it does, and so does tax
reporting, where the choice is usually not free. Pick one rule, state it, and
apply it consistently. See
[A3 Tax Considerations for Hedging Instruments](../appendices/a3-tax-considerations-for-hedging-instruments.md).

### Open Positions Must Be Marked, Not Ignored

A period almost never begins and ends with a flat book, so $V_0$ and $V_1$ are
load-bearing. Dropping them — measuring realized carry as premiums paid less
proceeds received — produces a figure that says a program spent heavily in the
quarter it bought its ladder and nothing at all in the quarters it held one.

The marking basis must be stated and must be the same at both ends of the
period. Mid-market is the usual choice. Marking at the bid systematically
understates $V_1$ and so overstates carry, which flatters nobody but does make
the series incomparable to one marked at mid.

!!! warning

    Consecutive periods must share their boundary mark: this period's $V_1$ has
    to be next period's $V_0$, computed once and reused. Re-deriving the
    boundary independently at each end lets a discrepancy fall between two
    periods, where it appears in neither and quietly breaks the property that
    the annual figure is the sum of its quarters.

## Reporting Gross and Net Separately

The identity as written nets everything into one number, and $R$ contains both
routine proceeds — expiries, scheduled rolls — and discretionary monetization
gains harvested in stress. Netting those together is the reporting failure
described in
[Evaluating and Testing Tail Hedge Strategies](evaluating-and-testing-tail-hedge-strategies.md#including-monetization-in-the-estimate):
it obscures the cost of protection in quiet years and the value of the payoff in
crisis years at the same time.

Partition $R$ into $R_{routine}$ and $R_{monetization}$ and report two figures:

$$\text{Gross Realized Carry}_{\$} = V_0 + P - R_{routine} - V_1$$

$$\text{Net Realized Carry}_{\$} = \text{Gross Realized Carry}_{\$} - R_{monetization}$$

The gross figure is the insurance premium and belongs against the carry budget.
The net figure is the economic outcome. Both are legitimate; presenting only the
net one makes a program look cheapest precisely in the years its protection was
tested, which is the opposite of informative.

The partition is a judgement about *why* a position was closed, so the rule for
making it should be written down before the crisis rather than during it.

## Reconciliation

Realized carry computed from the position history should tie to the accounts. If
it does not, the position history is incomplete — which is the useful finding,
because every later figure built on that history is wrong too.

The check: over any period, the change in hedge book value plus net cash flows
must equal the realized carry with the sign reversed. Reconcile at least
annually, and after any month containing a roll, a partial close or an
assignment. Common causes of a break:

- fees booked to the account but never captured against a position;
- an assignment or exercise recorded as an expiry;
- a roll captured as one net event, with the two legs' fills lost;
- a boundary mark recomputed rather than carried forward.

!!! note

    Attempting this reconstruction for the first time some years into a program
    is materially harder than recording it from the start, and in places
    impossible — historical marks for a specific contract on a specific past
    date are not always recoverable after the fact. The position history is
    cheap to keep and expensive to recreate.
