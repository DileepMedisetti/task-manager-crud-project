# ==========================================
# WHAT IS THIS FILE?
# ------------------------------------------
# This is the entry point of our FastAPI
# application.
#
# When we run:
#
# uvicorn app.main:app --reload
#
# FastAPI starts executing this file.
#
# This file:
# 1. Creates the FastAPI app
# 2. Creates database tables
# 3. Registers API routes
# ==========================================

# Import FastAPI
from fastapi import FastAPI

# Import Base and Engine
# Used for creating database tables.
from app.database import Base, engine

# Import Task router
from app.api.task import router as task_router

# ==========================================
# CREATE DATABASE TABLES
# ==========================================
# This creates all tables defined in models.py.
#
# If the table already exists,
# SQLAlchemy does nothing.
#
# During development, this is very useful.
Base.metadata.create_all(bind=engine)

# ==========================================
# CREATE FASTAPI APPLICATION
# ==========================================
app = FastAPI(

    # Project name shown in Swagger UI
    title="Task Manager API",

    # API description
    description="A simple CRUD API built using FastAPI and MySQL.",

    # API version
    version="1.0.0"
)

# ==========================================
# HOME ROUTE
# ==========================================
@app.get("/")
def home():

    return {
        "message": "Welcome to Task Manager API"
    }

# ==========================================
# REGISTER TASK ROUTER
# ==========================================
# This tells FastAPI:
#
# "Include all routes from task.py"
#
# Example:
#
# POST /tasks
#
# GET /tasks
#
# PUT /tasks/{id}
#
# DELETE /tasks/{id}
#
app.include_router(task_router)