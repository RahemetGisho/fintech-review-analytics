# Fintech Review Analytics

Customer Experience Analytics for Ethiopian Fintech Applications using Google Play Store Reviews.

---

# 📌 Project Overview

This project analyzes customer reviews from Ethiopian banking applications on the Google Play Store and transforms raw customer feedback into actionable business insights using:

- Web Scraping
- Data Preprocessing
- Sentiment Analysis
- Thematic Analysis
- PostgreSQL Database Engineering
- Data Visualization & Business Insights

The project focuses on three Ethiopian banks:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

---

# 📁 Project Structure

```text
fintech-review-analytics/
├── .github/
│   └── workflows/
│       └── unittests.yml
├── data/
│   ├── raw/
│   ├── processed/
│   └── analyzed/
├── notebooks/
│   ├── task2_analysis.ipynb
│   └── task4_insights.ipynb
├── sql/
│   ├── schema.sql
│   └── verification_queries.sql
├── src/
│   ├── scraper.py
│   ├── preprocess.py
│   ├── sentiment_analysis.py
│   ├── theme_analysis.py
│   ├── nlp_pipeline.py
│   ├── db_connection.py
│   └── load_to_postgres.py
├── tests/
├── requirements.txt
└── README.md
```

---

# 🛠️ Technologies Used

## Programming & Data Processing

- Python
- pandas
- NumPy

## Web Scraping

- google-play-scraper

## NLP & Machine Learning

- Hugging Face Transformers
- DistilBERT
- NLTK
- scikit-learn

## Database Engineering

- PostgreSQL
- SQLAlchemy
- psycopg2

## Visualization

- Matplotlib
- Seaborn
- WordCloud

## Development Tools

- Git & GitHub
- Jupyter Notebook
- VS Code
- GitHub Actions

---

# 🗂️ Task 1 — Data Collection & Preprocessing

## 🎯 Objective

- Scrape Google Play Store reviews
- Clean and preprocess customer feedback
- Prepare analysis-ready dataset

---

# 📊 Data Collection

Reviews were collected using the `google-play-scraper` Python library.

## Target Applications

| Bank   | App ID                         |
| ------ | ------------------------------ |
| CBE    | `com.combanketh.mobilebanking` |
| BOA    | `com.boa.boaMobileBanking`     |
| Dashen | `com.dashen.dashensuperapp`    |

---

# 📈 Dataset Summary

| Bank      | Reviews  |
| --------- | -------- |
| CBE       | 400      |
| BOA       | 400      |
| Dashen    | 400      |
| **Total** | **1200** |

---

# 🧹 Preprocessing Steps

The following preprocessing operations were performed:

1. Removed duplicate reviews
2. Handled missing values
3. Normalized dates
4. Selected required columns
5. Saved cleaned dataset

---

# 📌 Final Dataset Columns

- `review`
- `rating`
- `date`
- `bank`
- `source`

---

# 📊 Data Quality Summary

| Metric                 | Result |
| ---------------------- | ------ |
| Total Reviews          | 1200   |
| Missing Review Text    | 0      |
| Missing Ratings        | 0      |
| Duplicate Rows Removed | 0      |
| Final Dataset Size     | 1200   |

---

# 🧠 Task 2 — Sentiment & Thematic Analysis

## 🎯 Objective

- Quantify customer sentiment
- Identify recurring themes
- Extract customer pain points
- Build reusable NLP pipeline

---

# 🤖 Sentiment Analysis

## Model Used

```text
distilbert-base-uncased-finetuned-sst-2-english
```

The model classifies reviews into:

- Positive
- Negative
- Neutral

---

# 📌 Sentiment Output Columns

- `review`
- `rating`
- `date`
- `bank`
- `source`
- `sentiment_label`
- `sentiment_score`
- `processed_review`

---

# 🔤 NLP Pipeline

Implemented using NLTK with:

- Tokenization
- Lowercasing
- Stop-word removal
- Lemmatization
- Text normalization

Pipeline file:

```text
src/nlp_pipeline.py
```

---

# 🏷️ Thematic Analysis

## Identified Themes

- Account Access Issues
- Transaction Performance
- UI & Design
- Customer Support
- Feature Requests

---

# 🔑 Keyword Extraction

TF-IDF and n-gram extraction identified recurring keywords such as:

- login error
- slow transfer
- easy interface
- fingerprint login
- customer support

---

# 📌 Final Thematic Dataset

- `review_id`
- `review_text`
- `sentiment_label`
- `sentiment_score`
- `identified_theme`

---

# 🗄️ Task 3 — PostgreSQL Database Integration

## 🎯 Objective

Store processed review data in PostgreSQL.

---

# 🧱 Database Schema

## 🏦 Banks Table

| Column    | Description     |
| --------- | --------------- |
| bank_id   | Primary Key     |
| bank_name | Bank Name       |
| app_name  | Mobile App Name |

---

## 📝 Reviews Table

| Column           | Description      |
| ---------------- | ---------------- |
| review_id        | Primary Key      |
| bank_id          | Foreign Key      |
| review_text      | Customer Review  |
| rating           | Star Rating      |
| review_date      | Review Date      |
| sentiment_label  | NLP Sentiment    |
| sentiment_score  | Confidence Score |
| identified_theme | Extracted Theme  |
| source           | Review Source    |

---

# ⚙️ ETL Workflow

The PostgreSQL ETL pipeline performs:

1. Load cleaned dataset
2. Generate review IDs
3. Map bank names to `bank_id`
4. Merge sentiment and thematic outputs
5. Insert records into PostgreSQL

---

# 🧪 SQL Validation

Verification queries were used to:

- Count reviews per bank
- Compute average ratings
- Check null values

---

# 📈 Task 4 — Insights & Recommendations

## 🎯 Objective

Convert review analysis into business-actionable insights.

---

# 📊 Satisfaction Drivers

## 🟦 Commercial Bank of Ethiopia (CBE)

### Drivers

- Positive UI and usability feedback
- Smooth app navigation experience

---

## 🟩 Bank of Abyssinia (BOA)

### Drivers

- Helpful customer support feedback
- Good usability experience

---

## 🟨 Dashen Bank

### Drivers

- Easy-to-use interface
- Positive transaction experience

---

# ❌ Pain Points

## 🟦 Commercial Bank of Ethiopia (CBE)

### Pain Points

- OTP and login failures
- Slow transaction processing

---

## 🟩 Bank of Abyssinia (BOA)

### Pain Points

- Authentication issues
- Slow app response time

---

## 🟨 Dashen Bank

### Pain Points

- App lag during transactions
- Performance instability

---

# 💡 Recommendations

## 🟦 CBE

- Improve OTP delivery infrastructure
- Optimize transaction processing speed

---

## 🟩 BOA

- Strengthen authentication reliability
- Introduce AI chatbot support

---

## 🟨 Dashen

- Improve backend scalability
- Optimize API performance

---

# 📊 Visualizations

The project includes:

1. Sentiment Distribution by Bank
2. Rating Distribution Boxplots
3. Theme Frequency Analysis
4. WordCloud Visualizations
5. Sentiment Trend Analysis

---

# 🚀 Running the Project

## Clone Repository

```bash
git clone https://github.com/RahemetGisho/fintech-review-analytics.git
cd fintech-review-analytics
```

---

# 🐍 Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Pipeline

```bash
python src/scraper.py
python src/preprocess.py
python -m src.sentiment_analysis
python -m src.theme_analysis
python -m src.load_to_postgres
```

---

# 🧪 Testing

```bash
pytest
```

---

# ⚙️ CI/CD Pipeline

GitHub Actions automatically:

- installs dependencies
- runs tests
- validates project integrity

Workflow file:

```text
.github/workflows/unittests.yml
```

---

# ⚠️ Limitations

- Short reviews reduce NLP accuracy
- Some themes are grouped under “Other”
- Multilingual text affects sentiment classification
- Limited time-series depth for trend analysis

---

# 🔮 Future Work

- Interactive dashboards (Power BI / Streamlit)
- Advanced topic modeling (LDA / NMF)
- Real-time review monitoring system
- AI-powered customer support chatbot
- Customer churn prediction models
