import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from src.nlp_pipeline import preprocess_text

df = pd.read_csv(
    "data/analyzed/sentiment_analysis.csv"
)

df["review_id"] = range(1, len(df) + 1)

df["processed_review"] = df["review"].apply(
    preprocess_text
)


def identify_theme(text):

    text = str(text).lower()

    if any(word in text for word in [
        "login", "password", "otp", "access"
    ]):
        return "Account Access Issues"

    elif any(word in text for word in [
        "transfer", "slow", "transaction", "payment"
    ]):
        return "Transaction Performance"

    elif any(word in text for word in [
        "ui", "design", "interface", "easy"
    ]):
        return "UI & Design"

    elif any(word in text for word in [
        "support", "service", "help"
    ]):
        return "Customer Support"

    elif any(word in text for word in [
        "feature", "fingerprint", "update"
    ]):
        return "Feature Requests"

    else:
        return "Other"
    

df["identified_theme"] = df[
    "processed_review"
].apply(identify_theme)


banks = df["bank"].unique()

bank_keywords = {}

for bank in banks:

    bank_df = df[df["bank"] == bank]

    vectorizer = TfidfVectorizer(
        max_features=15,
        ngram_range=(1, 2)
    )

    tfidf_matrix = vectorizer.fit_transform(
        bank_df["processed_review"]
    )

    keywords = vectorizer.get_feature_names_out()

    bank_keywords[bank] = keywords

    print(f"\n========== {bank} ==========")

    print(keywords)


for bank in banks:

    print(f"\n========== THEMES FOR {bank} ==========")

    bank_themes = df[df["bank"] == bank][
        "identified_theme"
    ].value_counts()

    print(bank_themes)



final_df = df[[
    "review_id",
    "review",
    "sentiment_label",
    "sentiment_score",
    "identified_theme"
]]

final_df.columns = [
    "review_id",
    "review_text",
    "sentiment_label",
    "sentiment_score",
    "identified_theme"
]


final_df.to_csv(
    "data/analyzed/final_thematic_analysis.csv",
    index=False
)

print("\nFinal thematic analysis dataset saved.")