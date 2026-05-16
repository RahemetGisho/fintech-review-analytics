import pandas as pd
from transformers import pipeline

df = pd.read_csv("data/processed/bank_reviews_cleaned.csv")

print(df.head())
print(df.shape)

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_sentiment(text):
    """
    Analyze sentiment using DistilBERT.
    """

    result = classifier(str(text))[0]

    label = result["label"]
    score = result["score"]

    # Convert low-confidence predictions into neutral
    if score < 0.60:
        label = "NEUTRAL"

    return label, score


sentiment_results = df["review"].apply(analyze_sentiment)

df["sentiment_label"] = sentiment_results.apply(lambda x: x[0])
df["sentiment_score"] = sentiment_results.apply(lambda x: x[1])



print(df[[
    "review",
    "sentiment_label",
    "sentiment_score"
]].head())


bank_sentiment = df.groupby("bank")["sentiment_score"].mean()

print("\nAverage Sentiment Score by Bank:")
print(bank_sentiment)


rating_sentiment = df.groupby("rating")["sentiment_score"].mean()

print("\nAverage Sentiment Score by Rating:")
print(rating_sentiment)


df.to_csv(
    "data/analyzed/sentiment_analysis.csv",
    index=False
)

print("Sentiment analysis results saved.")


