# fastapi_app.py

# --------------------------------------------------------------------------------------------------------------------------------------
# ✅ HOW TO RUN THIS APP
# --------------------------------------------------------------------------------------------------------------------------------------
#
# - FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.6+.
# - This project demonstrates how to build and serve a machine learning model using FastAPI.
# - It uses the classic Iris flower classification dataset to train a simple Random Forest classifier.
# - It then exposes an API endpoint to make predictions.
#
# ▶️ Step 1: Install dependencies
#     pip install fastapi uvicorn scikit-learn pandas
#
# ▶️ Step 2: Run the FastAPI development server
#     python fastapi_app.py
#
#     This will start the app on: http://127.0.0.1:8000
#
# ▶️ Step 3: Test it!
#     • Interactive API docs: http://127.0.0.1:8000/docs
#     • Manual curl test (Linux/macOS/Git Bash):
#           curl -X POST "http://127.0.0.1:8000/predict" \
#                -H "Content-Type: application/json" \
#                -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
#
#     • Manual curl test (Windows PowerShell):
#           curl.exe --% -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d "{\"features\": [5.1, 3.5, 1.4, 0.2]}"
#
# --------------------------------------------------------------------------------------------------------------------------------------

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import uvicorn
import pandas as pd

# Initialize FastAPI app
app = FastAPI(title="⚡FastAPI ML Model Serving")

# --------------------------------------------------------------------------------------------------------------------------------------
# ✅ LOAD MODEL AND METADATA
# --------------------------------------------------------------------------------------------------------------------------------------

# Load iris dataset and train a model
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

model = RandomForestClassifier()
model.fit(X, y)

FEATURE_NAMES = iris.feature_names
TARGET_NAMES = iris.target_names

# --------------------------------------------------------------------------------------------------------------------------------------
# ✅ DEFINE REQUSEST MODEL
# --------------------------------------------------------------------------------------------------------------------------------------

class PredictionRequest(BaseModel):
    features: List[float]

# --------------------------------------------------------------------------------------------------------------------------------------
# ✅ DEFINE ROUUTES
# --------------------------------------------------------------------------------------------------------------------------------------

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the FastAPI ML Prediction API!",
        "usage": "Send a POST request to /predict with JSON: { 'features': [5.1, 3.5, 1.4, 0.2] }"
    }

@app.post("/predict")
def predict(request: PredictionRequest):
    features = request.features

    # Validate feature length
    if len(features) != len(FEATURE_NAMES):
        raise HTTPException(status_code=400, detail=f"Expected {len(FEATURE_NAMES)} features: {FEATURE_NAMES}")

    # Make prediction
    input_df = pd.DataFrame([features], columns=FEATURE_NAMES)
    class_index = int(model.predict(input_df)[0])
    class_name = TARGET_NAMES[class_index]

    return {
        "class_index": class_index,
        "class_name": class_name,
        "input_features": dict(zip(FEATURE_NAMES, features))
    }

# --------------------------------------------------------------------------------------------------------------------------------------
# ✅ RUN SERVER
# --------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    uvicorn.run("fastapi_app:app", host="127.0.0.1", port=8000, reload=True)
