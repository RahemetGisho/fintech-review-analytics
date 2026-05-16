# Fintech Review Analytics

Customer Experience Analytics for Ethiopian Fintech Applications using Google Play Store Reviews.

## Project Overview

This project analyzes customer reviews from Ethiopian banking applications on the Google Play Store. The goal is to transform raw customer feedback into actionable business insights through web scraping, preprocessing, sentiment analysis, thematic analysis, database engineering, and visualization.

The project focuses on three banks:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

---

# Task 1 — Data Collection and Preprocessing

## Objective

The objective of Task 1 is to:

- Scrape customer reviews from Google Play Store
- Clean and preprocess the data
- Prepare an analysis-ready dataset
- Maintain proper GitHub workflow and CI/CD practices

---

# Project Structure

```text
fintech-review-analytics/
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── unittests.yml
├── .gitignore
├── requirements.txt
├── README.md
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── __init__.py
│   └── README.md
├── src/
│   ├── __init__.py
│   ├── scraper.py
│   └── preprocess.py
├── tests/
│   ├── __init__.py
│   ├── test_basic.py
│   └── test_preprocess.py
└── scripts/
    ├── __init__.py
    └── README.md
```

---

# Technologies Used

- Python
- pandas
- google-play-scraper
- pytest
- GitHub Actions
- Git & GitHub

---

# Data Collection Methodology

## Data Source

Reviews were collected from the Google Play Store using the `google-play-scraper` Python library.

## Target Applications

| Bank   | App ID                         |
| ------ | ------------------------------ |
| CBE    | `com.combanketh.mobilebanking` |
| BOA    | `com.boa.boaMobileBanking`     |
| Dashen | `com.dashen.dashensuperapp`    |

## Data Collected

The following fields were collected:

- Review text
- Rating (1–5)
- Review date
- Bank name
- Source

## Scraping Configuration

- Language: English
- Country: Ethiopia (`et`)
- Sort Order: Newest reviews
- Reviews Collected: 400 per bank

## Total Reviews

| Bank   | Reviews |
| ------ | ------- |
| CBE    | 400     |
| BOA    | 400     |
| Dashen | 400     |
| Total  | 1200    |

---

# Preprocessing Steps

The following preprocessing operations were performed:

1. Removed duplicate reviews
2. Handled missing values
3. Normalized dates to `YYYY-MM-DD`
4. Selected required columns only
5. Saved cleaned dataset for analysis

## Final Dataset Columns

- `review`
- `rating`
- `date`
- `bank`
- `source`

---

# Data Quality Summary

| Metric                 | Result |
| ---------------------- | ------ |
| Total Reviews          | 1200   |
| Missing Review Text    | 0      |
| Missing Ratings        | 0      |
| Duplicate Rows Removed | 0      |
| Final Dataset Size     | 1200   |

The dataset satisfies the project KPI requirement of collecting over 1200 reviews with less than 5% missing data.

---

# Running the Project

## Clone Repository

```bash
git clone https://github.com/RahemetGisho/fintech-review-analytics.git
cd fintech-review-analytics
```

## Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Scraper

```bash
python src/scraper.py
```

---

# Run Preprocessing

```bash
python src/preprocess.py
```

---

# Run Tests

```bash
pytest
```

---

# CI/CD

GitHub Actions is configured to:

- install dependencies
- run automated tests
- validate pipeline integrity on push to `main`

Workflow file:

```text
.github/workflows/unittests.yml
```

---

# Limitations Encountered

- Some reviews contained emojis and multilingual text.
- Google Play review availability depends on app activity and public review access.
- Review ordering may change over time as new reviews are posted.

---

# Future Work

The next stages of the project will include:

- Sentiment Analysis
- Thematic Analysis
- PostgreSQL Database Integration
- Visualization & Business Insights
- Recommendation System

---
