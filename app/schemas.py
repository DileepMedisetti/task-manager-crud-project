# ==========================================
# WHAT IS THIS FILE?
# ------------------------------------------
# This file contains Pydantic Schemas.
#
# Schemas validate the data sent by the client.
#
# WHY DO WE NEED IT?
# ------------------------------------------
# Before inserting data into the database,
# we must check whether the data is valid.
#
# Example:
#
# title should be a string
# description should be a string
#
# If invalid data is received,
# FastAPI automatically returns an error.
# ==========================================

# Import BaseModel from Pydantic.
# Every schema inherits from BaseModel.
from typing import Optional
from pydantic import BaseModel


# ==========================================
# CREATE TASK SCHEMA
# ==========================================
# Used when the client creates a new task.
#
# Example Request:
#
# {
#     "title": "Learn FastAPI",
#     "description": "Complete CRUD project"
# }
class TaskCreate(BaseModel):

    # Task title
    # Must be a string
    title: str

    # Task description
    # Must be a string
    description: str


# ==========================================
# UPDATE TASK SCHEMA
# ==========================================
# Used when updating an existing task.
#
# Example:
#
# PUT /tasks/1
#
# {
#     "title":"Learn SQLAlchemy",
#     "description":"Study ORM"
# }

# ==========================================
# UPDATE TASK SCHEMA (PUT)
# ==========================================
# Used for full updates.
#
# Example:
#
# PUT /tasks/1
#
# All fields are required.
class TaskUpdate(BaseModel):

    title: str
    description: str
    status: str

# ==========================================
# PATCH TASK SCHEMA
# ==========================================
# Used when partially updating a task.
#
# Example:
#
# PATCH /tasks/1
#
# {
#     "status":"Completed"
# }
#
# OR
#
# {
#     "title":"Master FastAPI"
# }
#
# Unlike PUT, every field is optional.
# Only the provided fields will be updated.
class TaskPatch(BaseModel):

    # Optional title
    title: Optional[str] = None

    # Optional description
    description: Optional[str] = None

    # Optional status
    status: Optional[str] = None


# ==========================================
# RESPONSE SCHEMA
# ==========================================
# Used when sending data back to the client.
#
# Example Response:
#
# {
#     "id":1,
#     "title":"Learn FastAPI",
#     "description":"CRUD",
#     "status":"Pending"
# }
class TaskResponse(BaseModel):

    id: int
    title: str
    description: str
    status: str

    # Allows FastAPI to convert SQLAlchemy
    # model objects into this schema.
    model_config = {
        "from_attributes": True
    }
    