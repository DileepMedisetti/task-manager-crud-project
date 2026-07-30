# ==========================================
# WHAT IS THIS FILE?
# ------------------------------------------
# This file contains SQLAlchemy Models.
#
# A model represents a database table.
#
# One Model  =  One Table
#
# WHY DO WE NEED IT?
# ------------------------------------------
# Instead of writing SQL CREATE TABLE queries,
# we create Python classes.
#
# SQLAlchemy converts these classes into
# MySQL tables.
# ==========================================

# Import SQLAlchemy column types
from sqlalchemy import Column, Integer, String, Text

# Import the Base class created in database.py
# Every model must inherit from Base.
from app.database import Base


# ==========================================
# TASK MODEL
# ==========================================
# This class represents the "tasks" table
# in the MySQL database.
class Task(Base):

    # Name of the table in MySQL
    __tablename__ = "tasks"

    # ==============================
    # Table Columns
    # ==============================

    # Primary Key
    # Auto increments automatically
    id = Column(Integer, primary_key=True, index=True)

    # Task title
    # Maximum 100 characters
    # Cannot be NULL
    title = Column(String(100), nullable=False)

    # Task description
    # Can store large text
    description = Column(Text)

    # Task status
    # Example:
    # Pending
    # In Progress
    # Completed
    status = Column(String(30), default="Pending")