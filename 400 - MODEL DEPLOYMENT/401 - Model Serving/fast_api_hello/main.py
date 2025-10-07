# SIMPLE FAST API APP
# 1. Go to fast_api_hello directory in terminal
# 2. $ uvicorn main:app --reload
# 3. Go to "http://localhost:8000/" or $ curl http://localhost:8000/
# 4. Open git bash
# 5. $ curl -X POST "http://localhost:8000/greet?name=Joel"

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/greet")
def greet_user(name: str):
    return{"message": "Hello, " + name + "!"}