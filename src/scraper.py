from google_play_scraper import reviews, Sort
import pandas as pd

BANK_APPS = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

def scrape_reviews(app_id, bank_name, count=400):
    """
    Scrape reviews from Google Play Store.
    """

    result, _ = reviews(
        app_id,
        lang="en",
        country="et",
        sort=Sort.NEWEST,
        count=count
    )

    processed_reviews = []

    for review in result:
        processed_reviews.append({
            "review": review["content"],
            "rating": review["score"],
            "date": review["at"],
            "bank": bank_name,
            "source": "Google Play"
        })

    return pd.DataFrame(processed_reviews)

all_reviews = []

for bank, app_id in BANK_APPS.items():
    print(f"Scraping reviews for {bank}...")

    bank_reviews = scrape_reviews(app_id, bank)

    print(f"Collected {len(bank_reviews)} reviews")

    all_reviews.append(bank_reviews)

final_df = pd.concat(all_reviews, ignore_index=True)

print(final_df.head())
print(final_df.shape)

final_df.to_csv(
    "data/raw/bank_reviews_raw.csv",
    index=False
)

print("Raw dataset saved successfully.")
