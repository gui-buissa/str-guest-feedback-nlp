# Data

## Source

[Inside Airbnb](https://insideairbnb.com/get-the-data/), Broward County, Florida, scraped on 2026-06-29.

| File | Rows | Columns | What it has |
|---|---|---|---|
| `reviews.csv.gz` | 703,651 | 6 | One row per guest review: `listing_id`, `id`, `date`, `reviewer_id`, `reviewer_name`, `comments` |
| `listings.csv.gz` | 17,698 | 90 | One row per listing: neighborhood, property type, price, host info, and the review sub-scores |

The reviews cover 2011-08-23 to 2026-07-01 and 14,257 different listings. The text field is `comments`. Joining the two files on `listing_id` leaves out 253 reviews (0.04%), which belong to 8 listings that are missing from the listings file.

## The real data is not in this repository

Inside Airbnb asks users not to republish its data, so this repository does not include it. To reproduce the analysis, download both files once from the link above and put them in `data/raw/`. That folder is listed in `.gitignore`, so Git never uploads it.

Please cite the data as: *Inside Airbnb, Broward County, FL, 2026-06-29, insideairbnb.com*.

## `sample_mock.csv`

Twelve made-up reviews that only show the format of the real data (a few columns from `reviews.csv.gz` joined with a few columns from `listings.csv.gz`). They are synthetic, marked with `synthetic = yes`, and not real guest reviews.
