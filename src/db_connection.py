from sqlalchemy import create_engine


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