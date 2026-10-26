import html
import re

import pandas as pd
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS


def strip_html(text):
    """Turn HTML entities into characters and replace tags like <br/> with a space.
    Keeps case and punctuation, so the result can go to VADER."""
    if not isinstance(text, str):
        return ""
    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def clean_text(text):
    """Lowercase, letters only. Used for word counts and keyword checks."""
    text = strip_html(text).lower()
    text = re.sub(r"[^a-z\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def looks_english(text, min_share=0.2):
    """Rough language check: at least 20% of the words are common English stop words.
    Reviews in Spanish, Portuguese or French score close to zero."""
    words = clean_text(text).split()
    if len(words) < 3:
        return False
    return sum(w in ENGLISH_STOP_WORDS for w in words) / len(words) >= min_share


def load_reviews(raw_folder):
    """Read the Inside Airbnb reviews and join the listing details we use.
    Drops reviewer names and ids, which the analysis does not need."""
    reviews = pd.read_csv(f"{raw_folder}/reviews.csv.gz",
                          usecols=["listing_id", "id", "date", "comments"],
                          parse_dates=["date"])
    listings = pd.read_csv(f"{raw_folder}/listings.csv.gz",
                           usecols=["id", "neighbourhood_cleansed", "property_type", "room_type",
                                    "review_scores_rating", "review_scores_cleanliness",
                                    "review_scores_communication", "review_scores_checkin",
                                    "review_scores_location"])
    listings = listings.rename(columns={"id": "listing_id"})
    return reviews.merge(listings, on="listing_id", how="inner")
