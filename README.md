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

## Phase 2 results so far

Full details in [`notebooks/phase2_exploration.ipynb`](notebooks/phase2_exploration.ipynb).

* Only about 2.4% of recent English reviews are negative (VADER), so complaints are rare and easy to miss.
* Cleanliness shows up in 42% of the negative reviews, the most common complaint. Maintenance is mentioned less, but when it is, it is the most likely to be negative.
* Homes with a cleanliness score below 4.5 get 5.3% negative reviews, against 1.2% for homes above 4.8, so the text carries real signal.
* A first test of the Claude aspect prompt on 12 made-up reviews agreed with our expected labels on 95% of the decisions, at about $0.0002 per review.

## Plan for Phase 3

1. Aspect-based sentiment with the Claude API on about 1,500 recent English reviews: for each aspect (cleanliness, maintenance, host communication, check-in, location, plus noise and parking after the Phase 2 test), Claude says positive, negative or not mentioned. Because complaints are rare, the sample adds extra reviews with low VADER scores, weighted back down when we report shares.
2. Hand-check 100 of Claude's labels and report how often we agree, aspect by aspect.
3. Break down negative mentions by area, property type and season, and turn them into recommendations for the COO.

## How to run

1. Install Python 3.13 and the packages: `pip install -r requirements.txt`
2. Download `reviews.csv.gz` and `listings.csv.gz` (see [`data/README.md`](data/README.md)) into `data/raw/`.
3. Optional, only to rerun the Claude test: create a file named `.env` in the repo folder with one line, `ANTHROPIC_API_KEY=your-key`. It is listed in `.gitignore`. Without a key the notebook skips the API call and loads the saved results.
4. Open `notebooks/phase2_exploration.ipynb` and run all cells. It takes about two minutes.

## Repository

```
data/        data description, made-up sample reviews, the Claude test results, and a git-ignored raw/ folder
notebooks/   phase2_exploration.ipynb: data exploration, text mining and the Phase 3 plan
src/         preprocessing.py: reusable cleaning and loading functions
LICENSE      MIT license
README.md    this file
requirements.txt
```

## Progress

* Oct 3: problem, data and repository set up (Phase 1).
* Oct 20: switched to Path B after the Phase 1 feedback.
* Oct 21: Manoj cloned the repo and reviewed the Path B plan.
* Oct 26: Phase 2 notebook with data exploration, keyword, sentiment and aspect analysis, the Phase 3 plan and a first Claude prompt test.

## Team

* Guilherme Buissa
* Manoj Sandra
