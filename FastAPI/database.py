"""
Database configuration for FastAPI.

Creates a connection to the database,
creates a database engine,
and provides a database session for API endpoints.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./database.db"

# Create database engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Create database session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for database models
Base = declarative_base()


# Provide a database session to FastAPI endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()