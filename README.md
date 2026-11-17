# Guest Review Analytics for Short-Term Rentals

**Check In, Check Out — Guilherme Buissa and Manoj Sandra**

INFO 4360 Complex Data Analytics, University of Denver. Phase III analysis and presentation completed. Final report reviewed for submission.

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

Other contains 805 negative reviews (8.07%), but mixes many subjects. A guided reading of 20 randomly sampled Other-negative reviews illustrates its variety; it does not establish topic prevalence across all 805. Comparisons by current host listing count are supplementary context, not causal results or performance targets.

Counts describe reviews, not unique guests or listings. Groups differ in property mix and time; several reviews can belong to the same listing. Review dates approximate timing and are not stay dates. Suggested interventions have not been tested for effects on ratings, bookings or profit.

## Evaluation and limits

- Development used 16 invented reviews and a separate 20-review real pilot.
- Of the 10,000 main outputs, 9,971 pass format and quote checks; 29 fail the contiguous-quote requirement and remain unknown. Valid quotes do not guarantee correct interpretation.
- Agreement with the team's 30-review labels is 228/240 (95%), or 67/79 (84.81%) excluding jointly absent aspects. These are agreement measures, not proven accuracy. The notebook documents the evaluation procedure and its limitations.
- Gui confirmed 18 of 20 sampled Negative decisions, with clarification from an assistant during the review. This spot check cannot measure missed complaints or overall accuracy.
- Listing-level sub-scores provide a rough consistency check, not individual-review ground truth. A diagnostic subset gives equal weight to 282 listings with at least five valid sampled reviews; it does not represent all properties.
- VADER and keyword analysis in Phase II were exploratory. Its 2.4% negative sentiment is not the share of reviews containing complaints, and cleanliness keyword mentions do not establish the leading complaint.
- The long run took approximately 2 hours 55 minutes. Estimated main-sample cost was USD 2.3043, including the 30 comparison reviews, using classroom rates. Provider billing is authoritative.

## How to Run

To read the results, open [the notebook](notebooks/phase3_final_report.ipynb) on GitHub or download [the HTML report](notebooks/phase3_final_report.html) and open it in a browser. No installation, private data or API key is needed. [Phase II](notebooks/phase2_exploration.ipynb) contains the earlier exploration.

To execute the analysis locally, follow these steps.

1. **Download the project**

   ```bash
   git clone https://github.com/gui-buissa/str-guest-feedback-nlp.git
   cd str-guest-feedback-nlp
   ```

2. **Install the packages**

   Use Python 3.13, as in the course environment. These commands work in Windows PowerShell and macOS/Linux terminals:

   ```bash
   python -m venv .venv
   ```

   Windows PowerShell:

   ```powershell
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

   macOS/Linux:

   ```bash
   .venv/bin/python -m pip install -r requirements.txt
   ```

3. **Add the private files**

   Obtain the matching Broward County source files from [Inside Airbnb](https://insideairbnb.com/get-the-data/), following [data/README.md](data/README.md). Place `reviews.csv.gz` and `listings.csv.gz` in `data/raw/`.

   Executing the saved analysis also requires the team's private sample manifests, response caches, completed annotation files and review decisions in `data/raw/phase3/`. Request these files privately from the team. A public clone alone can display the published results but cannot execute the full cached analysis. The invented examples are development tests, not a replacement for these files.

4. **Open the notebook**

   In VS Code with the Python and Jupyter extensions, open `notebooks/phase3_final_report.ipynb` and select the `.venv` Python environment as its kernel.

5. **Use saved responses**

   Confirm that all four switches are set as follows before choosing Run All:

   ```python
   RUN_SYNTHETIC = False
   RUN_PILOT = False
   RUN_EVALUATION = False
   RUN_MAIN = False
   ```

   With the private files in place and all switches off, execution reads saved responses without calling the API. No key is needed for this mode.

Live API use is optional and may incur charges. It requires an authorized key in the local `.env` file, approval of the preceding stages and activation of one stage only. Never choose Run All with any API switch set to True. Keep keys and private files out of GitHub.

## Repository contents

- `notebooks/`: Phase II exploration and Phase III analysis/report, plus the HTML export.
- `src/`: preprocessing and Phase III helpers, including definitions, prompt, validation and aggregation.
- `data/`: source documentation and invented examples only.
- `requirements.txt`, `.gitignore`, `LICENSE`: environment, private-file exclusions and code license.

Real reviews, original datasets, labels linked to review text, response caches and API keys stay in ignored local files. Share them privately within the team, not through GitHub. The MIT license covers the project code, not third-party source data.

## Final submission

The final report is the Phase III notebook, written in blog style, with its HTML export. Submission is due Wednesday, November 18, 2026, at 23:59 (course deadline confirmed by the team). Publish the reviewed repository changes and upload both the notebook and HTML to Canvas. Regenerate the HTML after the final text review. The notebook's AI Usage Log records tools, tasks, checks and decisions.
