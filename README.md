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


# Running Project on Docker
# 🐳 Running the Project with Docker

## Step 1: Build the Docker Image

Build the Docker image from the project directory.

```bash
docker build -t task_management_fastapi_crud_project .
```

### Explanation

- `docker build` → Builds a Docker image.
- `-t` → Assigns a name (tag) to the image.
- `task_management_fastapi_crud_project` → Name of the Docker image.
- `.` → Uses the current directory as the build context.

---

## Step 2: Verify the Docker Image

```bash
docker images
```

This command lists all Docker images available on your system.

Example:

```text
REPOSITORY                              TAG       IMAGE ID
task_management_fastapi_crud_project    latest    ff23caff9cf6
```

---

## Step 3: Run the Docker Container

```bash
docker run --env-file .env -d -p 8000:8000 --name task-manager-api task_management_fastapi_crud_project
```

### Explanation

- `docker run` → Creates and starts a container from the image.
- `--env-file .env` → Loads environment variables from the `.env` file.
- `-d` → Runs the container in detached (background) mode.
- `-p 8000:8000` → Maps port 8000 of the host to port 8000 of the container.
- `--name task-manager-api` → Assigns a custom name to the container.
- `task_management_fastapi_crud_project` → Name of the Docker image.

---

## Step 4: Verify the Running Container

```bash
docker ps
```

This command shows all currently running Docker containers.

Example:

```text
CONTAINER ID   IMAGE                                  STATUS
7f2241f53328   task_management_fastapi_crud_project   Up 30 seconds
```

---

## Step 5: Open the API Documentation

Open your browser and visit:

```
http://localhost:8000/docs
```

Swagger UI will open, allowing you to test all CRUD APIs.

---

# Useful Docker Commands

## View Running Containers

```bash
docker ps
```

Displays all running containers.

---

## View All Containers

```bash
docker ps -a
```

Displays both running and stopped containers.

---

## View Docker Images

```bash
docker images
```

Lists all Docker images.

---

## View Container Logs

```bash
docker logs task-manager-api
```

Displays application logs from the container.

---

## Stop the Container

```bash
docker stop task-manager-api
```

Stops the running container.

---

## Start the Container

```bash
docker start task-manager-api
```

Starts an existing stopped container.

---

## Restart the Container

```bash
docker restart task-manager-api
```

Restarts the container.

---

## Remove the Container

```bash
docker rm task-manager-api
```

Deletes the stopped container.

> **Note:** Stop the container before removing it.

---

## Remove the Docker Image

```bash
docker rmi task_management_fastapi_crud_project
```

Deletes the Docker image.

> **Note:** Remove any containers using the image before deleting it.

---

# Complete Docker Workflow

```bash
# Build Docker Image
docker build -t task_management_fastapi_crud_project .

# Verify Image
docker images

# Run Docker Container
docker run --env-file .env -d -p 8000:8000 --name task-manager-api task_management_fastapi_crud_project

# Verify Running Container
docker ps

# Open Swagger UI
http://localhost:8000/docs

# Stop Container
docker stop task-manager-api

# Start Container
docker start task-manager-api

# Restart Container
docker restart task-manager-api

# View Logs
docker logs task-manager-api

# View All Containers
docker ps -a

# Remove Container
docker rm task-manager-api

# Remove Docker Image
docker rmi task_management_fastapi_crud_project
```

---

## Environment Variables

This project uses a `.env` file to store sensitive configuration such as database credentials.

Run the container with:

```bash
docker run --env-file .env -d -p 8000:8000 --name task-manager-api task_management_fastapi_crud_project
```

The `.env` file is excluded from GitHub using `.gitignore` to protect sensitive information. During deployment (e.g., Render), the same values should be configured as environment variables in the hosting platform instead of uploading the `.env` file.

