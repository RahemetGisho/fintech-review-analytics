# Fintech Review Analytics

Customer Experience Analytics for Ethiopian Fintech Applications using Google Play Store Reviews.

---

# Project Overview

This project analyzes customer reviews from Ethiopian banking applications on the Google Play Store. The goal is to transform raw customer feedback into actionable business insights through:

- Web Scraping
- Data Preprocessing
- Sentiment Analysis
- Thematic Analysis
- PostgreSQL Database Engineering
- Business Intelligence & Visualization

The project focuses on three Ethiopian banks:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

---

# Project Structure

```text
fintech-review-analytics/
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── unittests.yml
├── data/
│   ├── raw/
│   ├── processed/
│   └── analyzed/
├── notebooks/
│   ├── __init__.py
│   ├── task2_analysis.ipynb
│   └── README.md
├── scripts/
│   ├── __init__.py
│   └── README.md
├── sql/
│   ├── schema.sql
│   └── verification_queries.sql
├── src/
│   ├── __init__.py
│   ├── scraper.py
│   ├── preprocess.py
│   ├── sentiment_analysis.py
│   ├── theme_analysis.py
│   ├── nlp_pipeline.py
│   ├── db_connection.py
│   └── load_to_postgres.py
├── tests/
│   ├── __init__.py
│   ├── test_basic.py
│   └── test_preprocess.py
├── .gitignore
├── requirements.txt
└── README.md
```

---

# Technologies Used

## Programming & Data Processing

- Python
- pandas
- NumPy

## Web Scraping

- google-play-scraper

## Natural Language Processing

- Hugging Face Transformers
- DistilBERT
- NLTK
- scikit-learn

## Database Engineering

- PostgreSQL
- SQLAlchemy
- psycopg2

## Testing & CI/CD

- pytest
- GitHub Actions

## Development Tools

- Git & GitHub
- Jupyter Notebook
- VS Code

---

# Task 1 — Data Collection and Preprocessing

## Objective

The objective of Task 1 was to:

- Scrape customer reviews from Google Play Store
- Clean and preprocess the data
- Prepare an analysis-ready dataset
- Apply proper GitHub workflow and CI/CD practices

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

---

# Data Collected

The following fields were collected:

- Review text
- Rating (1–5)
- Review date
- Bank name
- Source

---

# Scraping Configuration

- Language: English
- Country: Ethiopia (`et`)
- Sort Order: Newest Reviews
- Reviews Collected: 400 per bank

---

# Total Reviews Collected

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
5. Saved cleaned dataset for downstream analysis

---

# Final Cleaned Dataset Columns

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

The dataset satisfies the project KPI requirement of collecting more than 1200 reviews with less than 5% missing data.

---

# Task 2 — Sentiment and Thematic Analysis

## Objective

The objective of Task 2 was to:

- Quantify customer sentiment
- Identify recurring business themes
- Extract customer pain points and satisfaction drivers
- Build a reusable NLP pipeline

---

# Sentiment Analysis

## Model Used

The project used:

```text
distilbert-base-uncased-finetuned-sst-2-english
```

from Hugging Face Transformers.

This transformer model was selected because it:

- provides strong sentiment classification performance
- is lightweight and efficient
- performs well on short customer reviews

---

# Sentiment Classification

Each review was classified into:

- Positive
- Negative

Additionally:

- sentiment confidence scores were generated for every review

---

# Sentiment Analysis Output

The sentiment analysis dataset contains:

- `review`
- `rating`
- `date`
- `bank`
- `source`
- `sentiment_label`
- `sentiment_score`
- `processed_review`

---

# NLP Pipeline

A modular NLP pipeline was implemented using NLTK.

The pipeline performs:

- tokenization
- lowercasing
- stop-word removal
- optional lemmatization
- text normalization

The pipeline was implemented inside:

```text
src/nlp_pipeline.py
```

---

# Thematic Analysis

## Objective

Thematic analysis was used to identify recurring business-relevant customer concerns and satisfaction patterns.

---

# Theme Identification

The following themes were identified:

- Account Access Issues
- Transaction Performance
- UI & Design
- Customer Support
- Feature Requests

---

# Keyword Extraction

TF-IDF and n-gram extraction were used to identify significant keywords and recurring phrases such as:

- login error
- slow transfer
- easy interface
- fingerprint login
- customer support

---

# Grouping Logic

Keywords with similar semantic meaning were grouped into broader business themes.

Example:

| Keywords                | Theme                   |
| ----------------------- | ----------------------- |
| login, otp, password    | Account Access Issues   |
| transfer, payment, slow | Transaction Performance |
| ui, interface, design   | UI & Design             |

---

# Final Thematic Analysis Dataset

The final thematic analysis dataset contains:

- `review_id`
- `review_text`
- `sentiment_label`
- `sentiment_score`
- `identified_theme`

---

# Task 3 — PostgreSQL Database Integration

## Objective

The objective of Task 3 was to:

- design a relational database schema
- store processed review data persistently
- simulate a real-world data engineering workflow

---

# PostgreSQL Database Setup

A PostgreSQL database named:

```text
bank_reviews
```

was created locally.

---

# Database Schema

## Banks Table

Stores metadata about each bank application.

### Columns

| Column    | Description      |
| --------- | ---------------- |
| bank_id   | Primary Key      |
| bank_name | Bank Name        |
| app_name  | Application Name |

---

## Reviews Table

Stores processed customer review data.

### Columns

| Column           | Description              |
| ---------------- | ------------------------ |
| review_id        | Primary Key              |
| bank_id          | Foreign Key              |
| review_text      | Customer Review          |
| rating           | User Rating              |
| review_date      | Review Date              |
| sentiment_label  | Sentiment Classification |
| sentiment_score  | Sentiment Confidence     |
| identified_theme | Extracted Theme          |
| source           | Review Source            |

---

# Database Engineering Workflow

The PostgreSQL ETL workflow performs:

1. Load processed review data
2. Generate review IDs
3. Merge thematic analysis output
4. Map bank IDs
5. Transform schema
6. Insert records into PostgreSQL

---

# SQL Verification Queries

Verification queries were executed to:

- count reviews per bank
- compute average ratings
- validate missing values

---

# Running the Project

## Clone Repository

```bash
git clone https://github.com/RahemetGisho/fintech-review-analytics.git
cd fintech-review-analytics
```

---

# Create Virtual Environment

## Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Web Scraper

```bash
python src/scraper.py
```

---

# Run Preprocessing

```bash
python src/preprocess.py
```

---

# Run Sentiment Analysis

```bash
python -m src.sentiment_analysis
```

---

# Run Theme Analysis

```bash
python -m src.theme_analysis
```

---

# Run PostgreSQL Loader

```bash
python -m src.load_to_postgres
```

---

# Run Tests

```bash
pytest
```

---

# CI/CD Pipeline

GitHub Actions is configured to:

- install dependencies
- run automated tests
- validate project integrity on every push to `main`

Workflow file:

```text
.github/workflows/unittests.yml
```

---

# Limitations Encountered

- Some reviews contain emojis and multilingual text.
- Transformer models may misclassify short or ambiguous reviews.
- Google Play review availability depends on public review access.
- Review ordering may change over time as new reviews are added.

---

# Future Work

Future project improvements may include:

- Interactive dashboards
- Advanced topic modeling
- Recommendation systems
- Real-time review monitoring
- Comparative banking analytics
- Customer churn prediction

---
