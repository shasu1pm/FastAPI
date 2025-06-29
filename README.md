# FastAPI Simple Food Order.
A clean FastAPI project demonstrating simple food ordering retrieval and cuisine lookup via REST API, built using FastAPI and Python 3.12 for your backend portfolio.

# 📜 Project Description:
This project implements:
- ✅ A FastAPI backend for retrieving available food items by cuisine.
- ✅ An endpoint to find the cuisine for a given food item.
- ✅ Minimal, clean, easy-to-understand structure for beginners learning FastAPI REST APIs.
---

# 🚀 Features
- ✅ Retrieve food items available under a specific cuisine (/get_items/{cuisine})
- ✅ Retrieve cuisine type for a given food item (/find_cuisine/{item_name})
- ✅ Uses FastAPI with async endpoints for non-blocking performance
- ✅ Enum usage for cuisine consistency
- ✅ Clean, extendable structure for learning REST API design
---

# 🛠️ Requirements
- Python >= 3.12
- FastAPI
- Uvicorn (for running the server)
---

# 🗂️ Project Structure
- graphql
- Copy
- Edit
```
fastapi-simple-food-order/
│
├── main.py              # Main FastAPI application with endpoints
├── pyproject.toml       # Project metadata
└── README.md            # Project overview and usage instructions
```
---

# 🚀 FastAPI CRUD Project Setup (Using UV)
- Set up your **FastAPI CRUD Operations** project cleanly using **UV (Rye)** and **Uvicorn** for your portfolio.
---

## 🗂️ Project Directory

```bash
D: (your directory)
cd Azure AI\3-Fast API CRUD Operations
mkdir "Fast API Project"
cd "Fast API Project"
mkdir restapi
cd restapi
```
- Organizes your FastAPI project in a structured folder.
---

## 🐍 Initialize Project with UV
```bash
uv init
```
- Creates `pyproject.toml` and a virtual environment for clean dependency management.
---

## 📦 Install FastAPI & Uvicorn

```bash
uv add fastapi uvicorn
```
- Installs FastAPI (API framework) and Uvicorn (ASGI server).
---

## 📄 Create `main.py`
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/hello/{name}")
def read_name(name: str):
    return {"message": f"Hello, {name}!"}
```
- Entry point with basic routes for testing.
---

## 🚀 Run API
```bash
uv run main.py
```
- Runs your API for quick testing.
---

## 🔁 Run with Reload (Dev)

```bash
uv run uvicorn main:app --reload
```
- Auto-reloads on file changes during development.
---

## 🌐 Test in Browser

- [http://localhost:8000/](http://localhost:8000/) → `{"message": "Hello, World!"}`
- [http://localhost:8000/hello/shasu](http://localhost:8000/hello/shasu) → `{"message": "Hello, shasu!"}`
---

✅ Your **FastAPI CRUD project is ready to extend** **Shasu!** Your FastAPI CRUD project is now ready 🚀 to extend with internal database integration, authentication, and new API routes as part of your learning path. Keep building and experimenting with confidence. Every line of code you write is a step forward—enjoy the process, showcase your progress proudly, and remember: you’ve got this! 🌱💡🔥
