---
title: "Continuity Planning"
---

A hedge program has an operator, and operators become unavailable. This page is
a template for the document that lets someone else take over — or safely do
nothing — while positions are open. It sets out what such a document must cover
and why; every specific in it is a blank you fill in privately.

The completed document is not part of this handbook and should not resemble it.
It names your broker, your account, your positions and your people. What follows
is the general structure and the reasoning behind each part.

This is a different failure from the one in
[Behavioral Risks — Abandoning the Program](../part-9/behavioral-risks-abandoning-the-program.md).
Abandonment is a decision someone makes. Incapacity leaves a non-specialist
holding open derivative positions with no framework for deciding anything, which
is a worse starting point and a more urgent one.

## The Three Paths, and What Each Commits To

Whoever inherits the program has three options. State all three in your
document, say which you would choose, and say why — a successor who understands
the reasoning can adapt it; one following an instruction cannot.

| Path | What it means | What it commits the household to |
| ---- | ------------- | -------------------------------- |
| Wind down | Close the positions and stop | A one-off execution task, then nothing. The portfolio is unhedged from that point |
| Run off | Hold what exists to expiry, roll nothing | No decisions and no new premium. Protection decays to zero on a known date |
| Maintain | Keep the program running to its rules | Ongoing premium, ongoing rolls, and a competent person who has agreed to do it |

The non-obvious point is that **maintain is only available if a specific
competent person has already agreed to run it**. A program left nominally
running with nobody watching is worse than either of the other two: it keeps
paying the cost of protection while the protection decays, and it accumulates
roll dates nobody is watching for. If you cannot name someone who has agreed,
your document should say the choice is between winding down and running off.

Run off is the path most people underrate. It requires no expertise, no
decisions and no further spending, and for a book with the right structure it is
safe for as long as the longest-dated position has left to run. Whether that is
true of your book is the subject of the next section.

## How Long Inaction Is Safe

This is the section that does the real work, because it tells a successor
whether they have months to find advice or days. It turns on one structural
question: **does the book contain sold options, and is each sold option paired
with a bought option of the same type and expiry at a better strike?**

**Long options only, fully paid.** Inaction is safe through expiry. The premium
is already spent, there is nothing further to pay, and the worst outcome is that
the options expire worthless. Index puts of the kind this handbook describes are
European and cash-settled, so there is no early assignment and no delivery of
anything — see
[Exercise & Settlement](../part-1/exercise-settlement.md#settlement-mechanics).
No margin is consumed, so no margin call can arrive. A successor can leave this
book entirely alone for as long as it takes to get advice.

**Sold puts each paired with a bought put at a higher strike in the same
expiry.** Also safe through expiry. The pair settles to a cash credit or to
zero and cannot produce a bill larger than the width of the spread, which is
already collateralised. What does need watching is the margin requirement: a
sold leg consumes buying power for as long as it is open, and how much depends
on the account's margin regime — see
[Running Structures with Sold Legs](../part-5/running-structures-with-sold-legs.md).
The obligation is bounded; the collateral supporting it still has to stay in
place.

**Anything else.** A sold leg outliving the bought leg that protects it, a sold
call, or any sold position that cannot be matched to a bought position of the
same type and expiry at a better strike: **not safe to leave alone**. These
positions have no bounded worst case, and the deadline for dealing with them is
set by the market rather than by anyone's convenience.

!!! warning

    Write out the case analysis for your own book explicitly, position by
    position, and update it whenever the structure changes. A successor should
    not have to work out from a position list whether every sold leg is paired
    — that inference is exactly what they are least equipped to make, and
    getting it wrong in the reassuring direction is the expensive error.

## Which Deadlines Actually Bind

A successor cannot tell an urgent date from an urgent-looking one. Separate them
explicitly.

| Deadline | Binds because | Missing it costs |
| -------- | ------------- | ---------------- |
| Last trading day of the nearest expiry | The position stops being tradable | The right to choose the exit price |
| Margin call | The broker will act if you do not | Forced liquidation at the broker's timing, not yours |
| Section 1256 year-end mark-to-market | It applies whether or not anyone acts | A tax event nobody planned for or funded |
| Roll dates | Only the program's own rules | Nothing, if the chosen path is run off or wind down |

The last trading day deserves particular attention, because for a standard
monthly index series it is **not** the settlement date and the settlement price
does not exist until the following morning. A successor who plans to sell a
position on the day they think it expires may find it has already stopped
trading. Which series settle in the morning and which in the afternoon, and what
that means for anyone intending to realise a position's value, is set out in
[AM and PM Settled Series](../part-1/exercise-settlement.md#am-and-pm-settled-series)
and [The Operator Principle](../part-1/exercise-settlement.md#the-operator-principle).

!!! warning

    Year-end mark-to-market is the deadline people miss, because doing nothing
    does not defer it. Positions subject to Section 1256 are treated as sold at
    year end whether or not anything was traded, so a successor who decides to
    "wait until things settle down" can still generate a reportable event. See
    [Ignoring Tax Interactions](../part-9/ignoring-tax-interactions.md) for the
    mechanics, and record in your document who prepares the return and what they
    already know about the program.

Roll dates are on the list to be dismissed. They feel urgent because the program
treats them as fixed, but they bind only if the chosen path is *maintain*. A
successor running the book off to expiry can ignore every one of them.

## Closing a Structure Safely

If the path is wind down, one rule matters more than all the rest.

!!! warning

    **A spread is closed as a spread, in a single net-priced order, and never
    one leg at a time.**

Selling the bought leg and leaving the sold leg in place converts a position
with a bounded worst case into one without, in a single click. It is also
exactly what a well-meaning non-specialist does first, because the bought leg is
the one that is worth something and selling it feels like taking money off the
table. In a falling market the sold leg is the one whose price has moved most
against a seller, so this mistake is at its most expensive precisely when
someone is most likely to make it.

Record this rule in your own document in your own words, and record the
mechanics — how the order is entered, and what it is called on the platform in
use — as a blank you fill in. The reasoning, and what a partially executed
structure actually becomes, is in
[Executing the Legs](../part-5/running-structures-with-sold-legs.md#executing-the-legs).

The instruction to give a successor is short: close the whole structure as one
order at a net price, or close nothing and wait for advice. Both are safe. The
middle course is not.

## Handover by Role

Name roles, not people. People change; the roles do not, and a document listing
a person who has retired is worse than one listing the function so a successor
knows who to go and find.

| Role | What they need | What they should not be given |
| ---- | -------------- | ----------------------------- |
| Whoever holds legal authority | The three-path decision and its reasoning; where every other record lives | Nothing withheld — this role decides |
| Custodian or broker | Instructions permitted by the account documentation | Discretion over whether the program continues |
| Options-competent adviser | Position list, structure, the case analysis above | Authority to trade without the legal decision-maker |
| Tax preparer | Instrument types, entity, prior treatment | Trading authority |
| Legal counsel | Entity structure, account documentation | Trading authority |
| Beneficiaries | That the program exists and who is running it | Position-level detail they cannot act on |

Every cell in the middle column is a blank in your document. Fill it with what
that role needs *from you*, not with an example.

## Interviewing an Adviser

If the path is maintain, someone has to be capable of it, and the person
choosing them will not be able to assess expertise directly. Give them
questions whose answers are checkable. Several double as competence tests:

- **Which series settle in the morning and which in the afternoon, and what
  does that change?** Someone who runs index options knows this without
  thinking. It has a right answer.
- **How would you close this put spread?** "As a single net-priced order" is
  the answer. Any proposal to sell one leg first and work the other is
  disqualifying, whatever the reasoning offered.
- **What is the worst outcome if we do nothing for six months?** They should
  reach for the sold-leg question above. If they answer without asking what is
  in the book, they are guessing.
- **What does this program cost per year, and against what is that measured?**
  A cost quoted without its basis is not an answer.
- **What would make you recommend closing it?** Anyone whose answer depends on
  recent market direction is running a view, not a program.

Answers that should worry you: an offer to improve the program's returns; a
recommendation formed before seeing the positions; and any discomfort with the
question about settlement.

## Completion Checklist

Verify the document has no blank left unfilled.

### Decision

- [ ] All three paths described, with the chosen one identified and reasoned
- [ ] If the choice is maintain, the person who will run it has agreed in writing
- [ ] The fallback if that person is unavailable is stated

### Positions

- [ ] Every position listed, with its type, expiry and strike
- [ ] Each sold leg explicitly matched to the bought leg that bounds it, or
      flagged as unmatched
- [ ] The "how long is inaction safe" conclusion stated in one sentence
- [ ] Date of the position list recorded, and a review interval set

### Deadlines

- [ ] Nearest last trading day identified, distinguished from its settlement date
- [ ] Margin arrangement described, and who is notified if a call arrives
- [ ] Year-end tax treatment noted, with the preparer identified by role

### Access and people

- [ ] Each role above filled with a current name and contact
- [ ] Account and custodian details recorded
- [ ] The instruction that a spread is closed as a spread, stated in your words

### Storage

- [ ] The document's own location recorded somewhere the successor will look
- [ ] Review date set, and tied to an existing annual routine

!!! warning

    **Credentials never go in this document — only where they are kept.**
    Logins, passwords, and account access codes belong in whatever system you
    already use for them, and the continuity document records that system's
    location and who can open it. A document containing both the position list
    and the means to trade it is a document you cannot store anywhere safely,
    which in practice means it will be stored somewhere unsafe or not written
    at all.
