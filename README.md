# equity-thesis-tracker

Right story, wrong price. That was my call on GE Vernova (NYSE: GEV). The demand is real, but the stock already pays for more than even strong execution can deliver. On October 1, 2026 I recommended a short at $987.45 with a 12-month target of $746, 25% below. This repo is where I test that call against what actually happened.

## The call

| | |
|---|---|
| Rating | SHORT |
| Price (10/01/26) | $987.45 |
| Price target | $746 (25% downside) |
| Bear / Base / Bull | $441 / $668 / $1,207 |
| Probability | 25% / 50% / 25% |

## Why I'm short

1. **The premium is bigger than the growth gap.** GEV trades at 26x consensus CY27E EBITDA (30x mine) against a 13.3x peer median and 20.6x for Eaton, the highest-rated peer.
2. **Consensus margins run ahead of the company's own guide.** The Street has 17.9% for FY27E. The company guides 12-14% for FY26 and Q2 came in at 11.3%. My segment build gets to 16.0%.
3. **Peak cash flow is being capitalized.** FY26 free cash flow guidance of $11.5-12.5B is lifted by customer down payments and slot reservations. I normalize FY27E to $3.9B.

## How the target is built

Everything runs off FY27E adj. EBITDA. The base case is Eaton's 20.6x on my $8.2B, which gives $668. The bear case holds the margin at the FY26 guide (13%) at Schneider's 16.2x, which gives $441. The bull case is the Street's own $1,207. Weighted 25/50/25, that comes to exactly $746.

## What would prove me wrong

I cover the short if any of these happen:

- FY27 revenue guide at or above the $53B consensus
- Adj. EBITDA margin above 17% for two straight quarters
- Wind reaches EBITDA breakeven before FY27
- The stock hits $1,207 (my stop)

## What this repo does

I'm building this to learn Python, SQL and statistics on a call I actually made. In order:

- [x] 1. Repo setup
- [ ] 2. SQL database of prices, peer multiples and financials for GEV and its peers
- [ ] 3. Valuation code with tests that rebuild the $746 target
- [ ] 4. Event study around Q3 earnings on October 28, 2026
- [ ] 5. Results memo: did the thesis hold up
- [ ] 6. Final cleanup

## Run it

```
pip install -e ".[dev]"
pytest
python -m equity_thesis_tracker
```

Student project. Not investment advice.
