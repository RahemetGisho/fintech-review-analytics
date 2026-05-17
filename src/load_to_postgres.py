import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError


# =========================================
# DATABASE CONFIGURATION
# =========================================

DB_USER = "postgres"
DB_PASSWORD = "Kullefst9493"
DB_HOST = "localhost"
DB_PORT = "5433"
DB_NAME = "bank_reviews"

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

print("Database connection successful.")


# =========================================
# LOAD PROCESSED REVIEWS
# =========================================

reviews_df = pd.read_csv(
    "data/analyzed/processed_reviews.csv"
)

print("\nProcessed Reviews Loaded")
print(reviews_df.head())


# =========================================
# CREATE REVIEW IDs
# =========================================

reviews_df["review_id"] = range(
    1,
    len(reviews_df) + 1
)


# =========================================
# LOAD THEMATIC ANALYSIS DATA
# =========================================

themes_df = pd.read_csv(
    "data/analyzed/final_thematic_analysis.csv"
)

print("\nThematic Analysis Loaded")
print(themes_df.head())


# =========================================
# MERGE IDENTIFIED THEMES
# =========================================

reviews_df = reviews_df.merge(

    themes_df[[
        "review_id",
        "identified_theme"
    ]],

    on="review_id",
    how="left"
)


# =========================================
# MAP BANK IDs
# =========================================

bank_mapping = {
    "CBE": 1,
    "BOA": 2,
    "Dashen": 3
}

reviews_df["bank_id"] = reviews_df[
    "bank"
].map(bank_mapping)


# =========================================
# SELECT REQUIRED DATABASE COLUMNS
# =========================================

final_df = reviews_df[[
    "review_id",
    "bank_id",
    "review",
    "rating",
    "date",
    "sentiment_label",
    "sentiment_score",
    "identified_theme",
    "source"
]]


# =========================================
# RENAME COLUMNS TO MATCH POSTGRESQL
# =========================================

final_df.columns = [
    "review_id",
    "bank_id",
    "review_text",
    "rating",
    "review_date",
    "sentiment_label",
    "sentiment_score",
    "identified_theme",
    "source"
]


# =========================================
# VERIFY FINAL DATAFRAME
# =========================================

print("\nFinal DataFrame")
print(final_df.head())

print("\nColumns:")
print(final_df.columns)

print("\nShape:")
print(final_df.shape)


# =========================================
# INSERT DATA INTO POSTGRESQL
# =========================================

try:

    final_df.to_sql(
        "reviews",
        engine,
        if_exists="append",
        index=False
    )

    print("\nReviews table populated successfully.")

except IntegrityError:

    print("\nDuplicate review IDs detected.")


print("\nData loading completed.")