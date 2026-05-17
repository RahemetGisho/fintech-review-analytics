CREATE TABLE banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name VARCHAR(100) NOT NULL,
    app_name VARCHAR(200) NOT NULL
);

CREATE TABLE reviews (
    review_id INTEGER PRIMARY KEY,
    bank_id INTEGER REFERENCES banks (bank_id),
    review_text TEXT NOT NULL,
    rating INTEGER NOT NULL,
    review_date DATE,
    sentiment_label VARCHAR(20),
    sentiment_score FLOAT,
    identified_theme VARCHAR(100),
    source VARCHAR(100)
);

bank_id INTEGER REFERENCES banks (bank_id)