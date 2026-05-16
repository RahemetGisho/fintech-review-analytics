import pandas as pd


def test_drop_missing_values():
    df = pd.DataFrame({
        "review": ["good", None],
        "rating": [5, 4]
    })

    cleaned = df.dropna(subset=["review", "rating"])

    assert len(cleaned) == 1