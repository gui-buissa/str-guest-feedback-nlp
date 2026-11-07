# Data

## Source files (private)

[Inside Airbnb](https://insideairbnb.com/get-the-data/), Broward County, Florida. Local files are labeled June 29, 2026; the review file contains dates through July 1, 2026. Keep this discrepancy visible when describing the snapshot.

| File | Rows | Columns | Contents |
|---|---:|---:|---|
| `reviews.csv.gz` | 703,651 | 6 | Review ID, listing ID, date, reviewer fields and comments |
| `listings.csv.gz` | 17,698 | 90 | Listing attributes, location, host fields and listing-level review sub-scores |

The review file covers 14,257 listing IDs. Joining reviews to the current listings file leaves 253 unmatched reviews (about 0.04%). The source dates span August 23, 2011 through July 1, 2026; Phase III uses reviews from 2023 onward and a rough English-text filter.

The team does not republish source data. Obtain the matching source files through Inside Airbnb and place them in `data/raw/`. That directory is ignored by Git. File exclusions do not replace checking notebook outputs before publication.

## Phase III private working files

`data/raw/phase3/` holds the sample manifests, 10,000 sampled reviews, separate 20-review pilot, 30-review comparison set, raw API responses, review decisions and annotation files. The main sample uses seed 42. It has no VADER oversampling and no weights.

`human_label_Gui_Manoj.xlsx` is the team's completed comparison file, sheet `Rotulos`. `negative_check_163d7aa8fd7ccec2.csv` contains the 20-negative spot check. These files include real text and stay private, along with readable HTML review reports and the separate AI-filled example. A collaborator needs these private working files to reproduce the cached run, but can read the public aggregate notebook and HTML without them.

## Invented examples (public)

- `sample_mock.csv`: 12 invented reviews used in Phase II and development; marked synthetic.
- `claude_prompt_test_mock.json`: saved Phase II responses for invented examples.
- `synthetic_expectations_phase3.json`: development expectations for the original examples.
- `synthetic_extra_cases_phase3.json`: four additional invented cases, giving 16 Phase III examples.

Invented examples are not observations, do not enter market percentages and are not independent accuracy tests. Source data, API keys and real-review outputs are not included in these public examples.
