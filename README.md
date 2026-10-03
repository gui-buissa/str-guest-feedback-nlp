# Short-Term Rental Guest Feedback: Text Analytics

Text analytics on short-term rental guest reviews: what do guests complain about, and can we flag it automatically?

*Course project, INFO 4360 Complex Data Analytics, University of Denver (Phase 1: problem and data).*

## The problem

A company that manages about 300 short-term rental homes in Florida collects thousands of guest reviews, but nobody turns them into action. Operations fixes problems one at a time, and the same complaints keep coming back.

Star ratings do not help here. In the Broward County data, every review sub-score averages between 4.65 and 4.82 out of 5, so almost every home looks excellent. The useful information is in the review text.

**Stakeholder:** the COO of the rental company, who decides where to spend on maintenance, cleaning and guest support.

**Why it matters:** catching the most common complaint types early means fewer repeat problems, fewer refunds, and better reviews and rebookings.

## Questions

Exploratory:

1. What do guests complain about, and how often?
2. Does the mix of complaints change by area and property type?
3. Has the mix changed over time?
4. Does each complaint type pull down the sub-score it should, for example cleanliness complaints and the cleanliness score?

Prediction (Path A):

5. Can the text of a home's reviews predict whether it falls below the market median in cleanliness, and which words drive that?

## Data

Inside Airbnb, Broward County, Florida (scraped 2026-06-29): 703,651 guest reviews of 14,257 homes, plus a listings file with 17,698 homes and 90 columns. Details and download instructions are in [`data/README.md`](data/README.md). The real data is not stored in this repository.

## Planned tools

There are no ready-made complaint labels, so the plan is:

1. Use the Claude API to label a small sample of reviews by complaint type.
2. Train a lighter classifier (TF-IDF with logistic regression) on those labels, so new reviews can be scored without calling the API each time.
3. Use classical NLP (keyword counts, spaCy, VADER) to explore and check the results.

The plan can change as the project moves forward.

## Repository

```
data/       data description, mock sample, and a git-ignored raw/ folder
README.md   this file
```

## Team

* Guilherme Buissa
* Manoj Sandra
