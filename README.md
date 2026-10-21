# Short-Term Rental Guest Feedback: Text Analytics

Text analytics on short-term rental guest reviews: what do guests complain about, where and when, and what should the operator fix first?

*Course project, INFO 4360 Complex Data Analytics, University of Denver (Phase 2: development).*

## The problem

A company that manages about 300 short-term rental homes in South Florida collects thousands of guest reviews, but nobody turns them into action. Operations fixes problems one at a time, and the same complaints keep coming back.

Star ratings do not help here. In the Broward County data, every review sub-score averages between 4.65 and 4.82 out of 5, so almost every home looks excellent. The useful information is in the review text.

**Stakeholder:** the COO of the rental company, who decides where to spend on maintenance, cleaning and guest support.

**Why it matters:** catching the most common complaint types early means fewer repeat problems, fewer refunds, and better reviews and rebookings.

## Analysis path: B (understanding and extraction)

We changed from Path A to Path B after the Phase 1 feedback. The COO does not need a model that predicts a cleanliness score that already exists. The COO needs to know what guests complain about, where it happens and whether it is getting worse, so the main deliverable is a set of patterns with clear, numbered recommendations.

## Questions

1. What do guests praise and complain about, and how often? We look at fixed aspects: cleanliness, maintenance, host communication, check-in and location.
2. Does the mix change by area and type of home?
3. Has it changed over time, for example by season?
4. Check: do complaints about an aspect match the matching sub-score, for example cleanliness complaints and the cleanliness score? If they do not, that is a warning about the labels.

## Data

Inside Airbnb, Broward County, Florida (scraped 2026-06-29): 703,651 guest reviews of 14,257 homes, plus a listings file with 17,698 homes and 90 columns. Details and download instructions are in [`data/README.md`](data/README.md). The real data is not stored in this repository.

## Planned tools

1. Classical NLP to explore the text: keyword counts, word clouds and VADER sentiment as a baseline.
2. Aspect-based sentiment with the Claude API on a sample of reviews: for each aspect, Claude says positive, negative or not mentioned, using a fixed list of aspects with short definitions. Most reviews are positive, so the sample will include extra reviews that are likely to contain complaints (for example, low VADER scores).
3. We will check a sample of Claude's labels by hand and report how often we agree.

The plan can change as the project moves forward.

## Repository

```
data/       data description, mock sample, and a git-ignored raw/ folder
LICENSE     MIT license
README.md   this file
```

## Progress

* Oct 3: problem, data and repository set up (Phase 1).
* Oct 20: switched to Path B after the Phase 1 feedback.

## Team

* Guilherme Buissa
* Manoj Sandra
