# Project Folder Structure

task_manager/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   │
│   └── api/
│       ├── __init__.py
│       └── task.py
│
├── tests/
│
├── .env
├── .gitignore
├── .dockerignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

# Step 1: Create Virtual Environment
Open VS Code Terminal inside your project.
root folder - task_manager/
run: >> python -m venv venv  (or)  py -m venv venv

Python created a separate environment.
task_manager/
│
├── venv/
Everything we install now stays inside this project.

Without a virtual environment,
Package
        ↓
Installed globally
        ↓
Every Python project uses it

# Step 2: Activate Virtual Environment
run: >> venv\Scripts\activate
You'll know it's activated when your terminal looks like:
(venv) C:\Users\...
The (venv) prefix means all Python commands now use the virtual environment.

# Step 3: Install Required Packages
run: >> pip install fastapi uvicorn sqlalchemy pymysql python-dotenv pydantic[email]

to see installed packages,
run: >> pip freeze   (or) pip list **(recommended)

What does each package do,
1.FastApi -> This is the web framework. Without FastAPI, you cannot build APIs.
2.Uvicorn -> FastAPI cannot run by itself. It needs an ASGI server. Uvicorn is that server.
3.SQLAlchemy -> This is the ORM (Object Relational Mapper).
    Instead of writing SQL everywhere,
    SELECT * FROM tasks;
    you'll write Python code like:
    db.query(Task).all()
    SQLAlchemy translates that into SQL.
4.PyMySQL -> This is the MySQL database driver. It lets Python communicate with a MySQL server.
             Without it, FastAPI cannot connect to MySQL.
5.python-dotenv -> Loads values from your .env file.
                Instead of hardcoding:
                password = "123456"
                you'll use:
                DB_PASSWORD=123456
                This is more secure and easier to manage.
6.Pydantic -> Pydantic validates incoming and outgoing data.
            Example:
            User sends:
            {
                "title": 123
            }
            If title should be text, Pydantic rejects the request automatically. 
            Because title should be text (string), not a number.

# Step 4: Save Installed Packages to requirements.txt file
run: >> pip freeze > requirements.txt
Your requirements.txt will contain the exact package versions used in the project.

# Project Flow
    Client
       │
       ▼
    FastAPI
       │
       ▼
    Pydantic
       │
       ▼
    CRUD
      │
      ▼
    SQLAlchemy
       │
       ▼
    MySQL

# Step 5: Development

====================================================================================================
# API Testing Guide

After starting the FastAPI server, open the Swagger UI to test all APIs.

## Swagger URL

```
http://127.0.0.1:8000/docs
```

---

# 1. Home API

### Endpoint

```
GET /
```

### Expected Response

```json
{
  "message": "Welcome to Task Manager API"
}
```

---

# 2. Create Task

### Endpoint

```
POST /tasks/
```

### Request Body

```json
{
  "title": "Learn FastAPI",
  "description": "Complete CRUD Project"
}
```

### Expected Response

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "description": "Complete CRUD Project",
  "status": "Pending"
}
```

---

# 3. Get All Tasks

### Endpoint

```
GET /tasks/
```

### Expected Response

```json
[
  {
    "id": 1,
    "title": "Learn FastAPI",
    "description": "Complete CRUD Project",
    "status": "Pending"
  }
]
```

---

# 4. Get Task by ID

### Endpoint

```
GET /tasks/{task_id}
```

### Example

```
GET /tasks/1
```

### Expected Response

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "description": "Complete CRUD Project",
  "status": "Pending"
}
```

---

# 5. Update Task

### Endpoint

```
PUT /tasks/{task_id}
```

### Example

```
PUT /tasks/1
```

### Request Body

```json
{
  "title": "Master FastAPI",
  "description": "CRUD Completed",
  "status": "Completed"
}
```

### Expected Response

```json
{
  "id": 1,
  "title": "Master FastAPI",
  "description": "CRUD Completed",
  "status": "Completed"
}
```

---

# 6. Edit Task (Partial Update)

### Endpoint

```
PATCH /tasks/{task_id}
```

### Example

```
PATCH /tasks/1
```

### Request Body (Update Status Only)

```json
{
  "status": "Completed"
}
```

### Or Update Title Only

```json
{
  "title": "Master FastAPI"
}
```

### Expected Response

```json
{
  "id": 1,
  "title": "Master FastAPI",
  "description": "Complete CRUD Project",
  "status": "Completed"
}
```

---

# 7. Delete Task

### Endpoint

```
DELETE /tasks/{task_id}
```

### Example

```
DELETE /tasks/1
```

### Expected Response

```json
{
  "message": "Task deleted successfully"
}
```

---

# 8. Verify Deletion

### Endpoint

```
GET /tasks/1
```

### Expected Response

```json
{
  "detail": "Task not found"
}
```

### HTTP Status

```
404 Not Found
```

---

# API Testing Flow

```
POST   /tasks/        → Create a new task
GET    /tasks/        → Retrieve all tasks
GET    /tasks/{id}    → Retrieve a specific task
PUT    /tasks/{id}    → Update an existing task
PATCH  /tasks/{id}    → Partial Update
DELETE /tasks/{id}    → Delete a task
```

---

# Test Order

1. Start the FastAPI server.
2. Open Swagger UI (`/docs`).
3. Test the Home API.
4. Create a new task.
5. Retrieve all tasks.
6. Retrieve a task by ID.
7. Update the task.
8. Delete the task.
9. Verify the task has been deleted.

All CRUD operations can be tested directly from the FastAPI Swagger UI without using external tools like Postman.



