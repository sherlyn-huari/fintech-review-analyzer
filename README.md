# Digital Payment Apps - User Sentiment Analyzer
![Dashboard](dashboard.png)

## What is this?
Analysis of 899 Google Play reviews from WhatsApp, Paypal, and CashApp to identify user pain points and product improvement opportunities.

## Why?
To practice product thinking with real data and answer: what should the product team fix first?

## Key findings

- 69% of reviews are positive, but payment issues drive most negative feedback
- Paypal has the lowest average rating among the three  apps
- Support complains spike alongside payment issues - likely the same root problem

## Product recommendation
**Priority 1 - Fix payment failures:** 140 reviews mention payment/ transaction issues. This is the #1 driver of negative sentiment.

**Priority 2 - Reduce support load::** Most support complains trace back to payment errors. Fix payments, reduce support tickets automatically.

## Stack
Pyhton . google-play-scraper . pandas . Power BI

## Files
- `src/scraper.py` — data collection
- `src/classify.py` — sentiment and category classification
- `data/reviews_classified.csv` — cleaned dataset