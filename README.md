# Guest Review Analytics for Short-Term Rentals

**Check In, Check Out — Guilherme Buissa and Manoj Sandra**

INFO 4360 Complex Data Analytics, University of Denver. Phase III analysis completed; presentation and final report in preparation.

## Business question

What do guests praise and criticize, where do complaint patterns differ, and what should a short-term rental operations team investigate first?

The stakeholder is a South Florida property operator's operations lead. Public Broward County market data provides context. We cannot identify which listings belong to the company, and do not claim to measure its own performance. The analysis follows **Path B: understanding and extraction**, rather than prediction. We did not train or fine-tune a new model.

## Data and method

Inside Airbnb reviews and listings from Broward County, Florida. The local source files contain 703,651 reviews and 17,698 listings. The files are labeled June 29, 2026, while review dates extend through July 1, 2026. Source details are in [data/README.md](data/README.md).

Reviews are joined to listings, cleaned and restricted to 2023 onward using a rough English-text filter. From 408,181 eligible reviews, we draw 10,000 random reviews with seed 42. No VADER-based selection, extra negative sampling or weighting is used in Phase III. The sample covers 5,175 listings before output validation.

Claude labels sentiment separately for cleanliness, maintenance, host communication, check-in, location, noise, parking and Other. Mentioned aspects receive Positive, Negative or Neutral plus a supporting quote. Unmentioned aspects are Absent. When one aspect has both praise and a complaint, it counts as Negative. Repeated aspect entries are consolidated, preserving their evidence.

## Main results

| Finding | Observed result | Proposed action |
|---|---|---|
| Maintenance | 696/9,971 valid reviews (6.98%). December–March: 334/4,063 (8.22%); April–November: 362/5,908 (6.13%). The direction also holds for complete years 2023–2025 | Review equipment function and property condition before arrivals; consider a pre-December inspection schedule |
| Area patterns | At least one complaint in 102/394 Hallandale Beach reviews (25.9%), 425/2,057 Hollywood reviews (20.7%) and 517/3,640 Fort Lauderdale reviews (14.2%) | Investigate recent complaints at relevant properties rather than infer an area causes problems |
| Condo arrival process | Check-in complaints: 50/942 entire condos (5.31%), 100/3,258 entire rental units (3.07%) and 53/3,368 entire homes (1.57%) | Review arrival instructions and building access; a one-page arrival guide is a proposed intervention |

Other contains 805 negative reviews (8.07%), but mixes many subjects. It needs qualitative review before specific recommendations. Comparisons by current host listing count are supplementary context, not causal results or performance targets.

Counts describe reviews, not unique guests or listings. Groups differ in property mix and time; several reviews can belong to the same listing. Review dates approximate timing and are not stay dates. Suggested interventions have not been tested for effects on ratings, bookings or profit.

## Evaluation and limits

- Development used 16 invented reviews and a separate 20-review real pilot.
- Of the 10,000 main outputs, 9,971 pass format and quote checks; 29 fail the contiguous-quote requirement and remain unknown. Valid quotes do not guarantee correct interpretation.
- Agreement with the team's 30-review labels is 228/240 (95%), or 67/79 (84.81%) excluding jointly absent aspects. These are agreement measures, not proven accuracy. The notebook documents the evaluation procedure and its limitations.
- Gui confirmed 18 of 20 sampled Negative decisions, with clarification from an assistant during the review. This spot check cannot measure missed complaints or overall accuracy.
- Listing-level sub-scores provide a rough consistency check, not individual-review ground truth. A diagnostic subset gives equal weight to 282 listings with at least five valid sampled reviews; it does not represent all properties.
- VADER and keyword analysis in Phase II were exploratory. Its 2.4% negative sentiment is not the share of reviews containing complaints, and cleanliness keyword mentions do not establish the leading complaint.
- The long run took approximately 2 hours 55 minutes. Estimated main-sample cost was USD 2.3043, including the 30 comparison reviews, using classroom rates. Provider billing is authoritative.

## Read and reproduce

Start with [the Phase III notebook](notebooks/phase3_aspect_analysis.ipynb) or its [HTML export](notebooks/phase3_aspect_analysis.html). Their saved aggregate outputs can be read without executing code. [Phase II](notebooks/phase2_exploration.ipynb) remains as historical exploration.

For local execution, install the packages in `requirements.txt` in the course Python environment. Place the original source files in `data/raw/`. Reading the saved Phase III analysis through code also requires private sample manifests, model-response caches, annotation files and review decisions under `data/raw/phase3/`, shared separately by the team. A fresh clone does not include these private files and cannot reproduce the saved calls from the public files alone.

Keep **RUN_SYNTHETIC, RUN_PILOT, RUN_EVALUATION and RUN_MAIN set to False** when reading cached results. Live API use requires an authorized key in the local `.env`, completed reviews of preceding stages and explicit activation of one stage only. Never use Run All with any API switch set to True. API calls may incur charges; rerunning is not needed to read published results.

## Repository contents

- `notebooks/`: Phase II exploration and Phase III analysis/report, plus the HTML export.
- `src/`: preprocessing and Phase III helpers, including definitions, prompt, validation and aggregation.
- `data/`: source documentation and invented examples only.
- `requirements.txt`, `.gitignore`, `LICENSE`: environment, private-file exclusions and code license.

Real reviews, original datasets, labels linked to review text, response caches and API keys stay in ignored local files. Share them privately within the team, not through GitHub. The MIT license covers the project code, not third-party source data.

## Remaining work

Select final visuals and rehearse the November 10 presentation. Complete the final report after presentation feedback. The team completed an exploratory reading of 20 Other complaints; this does not establish topic prevalence across all 805. The notebook's AI Usage Log records the tools, tasks, checks and decisions.
