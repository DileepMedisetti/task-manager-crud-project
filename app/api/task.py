# ==========================================
# WHAT IS THIS FILE?
# ------------------------------------------
# This file contains API routes (endpoints).
#
# WHY DO WE NEED IT?
# ------------------------------------------
# Clients (Browser, Postman, Mobile App)
# cannot directly access the database.
#
# They send HTTP requests to these routes.
#
# These routes call CRUD functions.
# ==========================================

# APIRouter helps us organize APIs into
# separate files instead of writing
# everything inside main.py.
from fastapi import APIRouter, Depends, HTTPException

# Session is used for database operations.
from sqlalchemy.orm import Session

# Import CRUD functions.
from app import crud

# Import Pydantic Schemas.
from app.schemas import (
    TaskCreate,
    TaskUpdate,
    TaskPatch,
    TaskResponse
)

# Import database dependency.
from app.database import get_db

# ==========================================
# CREATE ROUTER
# ==========================================
# Instead of using app.get(), app.post()
# directly, we use APIRouter.
#
# Later this router will be included
# inside main.py.
router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


# ==========================================
# CREATE TASK
# ==========================================
# POST /tasks
#
# Creates a new task.
@router.post("/", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    return crud.create_task(db, task)


# ==========================================
# GET ALL TASKS
# ==========================================
# GET /tasks
#
# Returns every task.
@router.get("/", response_model=list[TaskResponse])
def get_tasks(
    db: Session = Depends(get_db)
):
    return crud.get_tasks(db)


# ==========================================
# GET SINGLE TASK
# ==========================================
# GET /tasks/1
#
# Returns one task.
@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    db: Session = Depends(get_db)
):

    task = crud.get_task(db, task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


# ==========================================
# UPDATE TASK (PUT)
# ==========================================
# PUT /tasks/1
#
# Replaces the entire task.
#
# The client must send all fields.
@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db)
):

    updated_task = crud.update_task(
        db,
        task_id,
        task
    )

    if updated_task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return updated_task

# ==========================================
# PATCH TASK
# ==========================================
# PATCH /tasks/1
#
# Partially updates an existing task.
#
# The client only sends the fields
# that need to be updated.
#
# Example:
#
# {
#     "status": "Completed"
# }
#
@router.patch("/{task_id}", response_model=TaskResponse)
def patch_task(
    task_id: int,
    task: TaskPatch,
    db: Session = Depends(get_db)
):

    # Call the CRUD function
    updated_task = crud.patch_task(
        db,
        task_id,
        task
    )

    # Return 404 if task doesn't exist
    if updated_task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return updated_task

# ==========================================
# DELETE TASK
# ==========================================
# DELETE /tasks/1
#
# Deletes a task.
@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):

    deleted_task = crud.delete_task(
        db,
        task_id
    )

    if deleted_task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "message": "Task deleted successfully"
    }