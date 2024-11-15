import os

class Config:
    DB_PORT = os.getenv('DB_PORT')
    DB_HOST = os.getenv('DB_HOST')
    DB_USER = os.getenv('DB_USER')
    DB_PASS = os.getenv('DB_PASS')
    DB_NAME = os.getenv('DB_NAME')

    # Ensure all necessary variables are loaded
    if not all([DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME]):
        raise ValueError("One or more environment variables are missing!")

    # Add SSL mode for Azure PostgreSQL
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=require"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
