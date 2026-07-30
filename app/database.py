# ==========================================
# WHAT IS THIS FILE?
# ------------------------------------------
# This file connects our FastAPI application
# to the MySQL database.
#
# WHY DO WE NEED IT?
# ------------------------------------------
# SQLAlchemy needs:
# 1. Database URL
# 2. Engine
# 3. Session
# 4. Base Class
#
# These are created only once and reused
# throughout the project.
# ==========================================

# SQLAlchemy engine is responsible for connecting
# Python with the database.
from sqlalchemy import create_engine

# sessionmaker creates database sessions.
# A session is used to execute SQL operations
# like INSERT, SELECT, UPDATE, DELETE.
from sqlalchemy.orm import sessionmaker

# DeclarativeBase is the base class for all models.
# Every model (Task, User, etc.) will inherit from it.
from sqlalchemy.orm import DeclarativeBase

# Import database configuration values
from app.config import (
    DB_HOST,
    DB_PORT,
    DB_USER,
    DB_PASSWORD,
    DB_NAME,
)

# ==========================================
# DATABASE URL
# ==========================================
# Format:
# mysql+pymysql://username:password@host:port/database_name

DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ==========================================
# CREATE ENGINE
# ==========================================
# Engine is responsible for creating the
# connection between FastAPI and MySQL.

#engine = create_engine(DATABASE_URL)

#=========================

# ==========================================
# CREATE ENGINE
# ==========================================
# Engine is responsible for creating the
# connection between FastAPI and MySQL.
#
# pool_pre_ping=True
# ------------------
# Before using a connection, SQLAlchemy checks
# whether it is still alive.
#
# This is useful for cloud databases like
# Aiven because idle connections can be closed.
#
# connect_args
# ------------
# Aiven requires SSL for secure communication.
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "ssl": {}
    }
)
#=========================

# ==========================================
# CREATE SESSION
# ==========================================
# Every database operation uses a session.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ==========================================
# BASE CLASS
# ==========================================
# Every SQLAlchemy model will inherit from Base.
# Example:
#
# class Task(Base):
#     ...
class Base(DeclarativeBase):
    pass


# ==========================================
# DATABASE SESSION DEPENDENCY
# ==========================================
# This function provides a database session
# to our API routes.
#
# It opens a session before the request
# and closes it after the request finishes.
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()