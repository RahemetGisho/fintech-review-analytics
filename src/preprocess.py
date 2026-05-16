import pandas as pd
df = pd.read_csv("data/raw/bank_reviews_raw.csv")

print("Initial Shape:")
print(df.shape)

before_duplicates = len(df)

df = df.drop_duplicates()

after_duplicates = len(df)

print(f"Removed {before_duplicates - after_duplicates} duplicate rows")

missing_before = df.isnull().sum()

print("Missing Values Before Cleaning:")
print(missing_before)

df = df.dropna(subset=["review", "rating"])

missing_after = df.isnull().sum()

print("Missing Values After Cleaning:")
print(missing_after)

df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

df = df[["review", "rating", "date", "bank", "source"]]

print(df.head())

print("Final Shape:")
print(df.shape)

df.to_csv(
    "data/processed/bank_reviews_cleaned.csv",
    index=False
)

print("Cleaned dataset saved successfully.")