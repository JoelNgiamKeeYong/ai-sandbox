# flask_app.py

# --------------------------------------------------------------------------------------------------------------------------------------
# ✅ HOW TO RUN THIS APP
# --------------------------------------------------------------------------------------------------------------------------------------
#
# - Flask is a lightweight web framework for building APIs and web applications in Python.
# - This project demonstrates how to build and serve a machine learning model using Flask.
# - It uses the classic Iris flower classification dataset to train a Random Forest classifier,
#   then exposes an API endpoint to make predictions from user input.
#
# ▶️ Step 1: Install dependencies
#     pip install flask scikit-learn pandas
#
# ▶️ Step 2: Run the Flask development server
#     python flask_app.py
#
#     This will start the app on: http://127.0.0.1:5000
#
# ▶️ Step 3: Test it!
#     • Open your browser to: http://127.0.0.1:5000
#     • Send a POST request to /predict
#
#     🔸 Example test with curl (Linux/macOS/Git Bash):
#         curl -X POST "http://127.0.0.1:5000/predict" \
#              -H "Content-Type: application/json" \
#              -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
#
#     🔸 Example test with Windows PowerShell:
#         curl.exe --% -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d "{\"features\": [5.1, 3.5, 1.4, 0.2]}"
#
# --------------------------------------------------------------------------------------------------------------------------------------

from flask import Flask, request, jsonify
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

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
# ✅ DEFINE ROUTES
# --------------------------------------------------------------------------------------------------------------------------------------

@app.route('/')
def home():
    """
    GET /
    Display a simple welcome message and usage instructions.
    """
    return """
    <h2>🌼 Flask ML Prediction API</h2>
    <p>Send a POST request to <code>/predict</code> with JSON:</p>
    <pre>{ "features": [5.1, 3.5, 1.4, 0.2] }</pre>
    """

@app.route('/predict', methods=['POST'])
def predict():
    """
    POST /predict
    Accepts a JSON object with 4 feature values and returns the predicted class.
    """
    try:
        data = request.get_json()
        features = data.get('features')

        # Validate input length
        if not features or len(features) != len(FEATURE_NAMES):
            return jsonify({'error': f'Expected {len(FEATURE_NAMES)} features: {FEATURE_NAMES}'}), 400

        # Make prediction
        input_df = pd.DataFrame([features], columns=FEATURE_NAMES)
        class_index = int(model.predict(input_df)[0])
        class_name = TARGET_NAMES[class_index]

        return jsonify({
            "class_index": class_index,
            "class_name": class_name,
            "input_features": dict(zip(FEATURE_NAMES, features))
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# --------------------------------------------------------------------------------------------------------------------------------------
# ✅ RUN SERVER
# --------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True, port=5000)
