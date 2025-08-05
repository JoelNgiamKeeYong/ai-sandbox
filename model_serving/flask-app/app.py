# app.py

# Import necessary libraries
from flask import Flask, request, jsonify                   # Flask core modules
from sklearn.datasets import load_iris                      # Dataset for demonstration
import pandas as pd                                         # Data handling
import joblib                                               # For saving/loading models
import os                                                   # Path handling

# Initialize Flask application
app = Flask(__name__)

# Define path to the pre-trained model
MODEL_PATH = os.path.join('model', 'trained_model.pkl')

# Load the model into memory once at server startup
# This avoids reloading the model on every request
model = joblib.load(MODEL_PATH)

# Load feature names and target class names from the original dataset
# This ensures consistency between training and prediction
iris = load_iris()
FEATURE_NAMES = iris.feature_names       # e.g., ['sepal length (cm)', ...]
TARGET_NAMES = iris.target_names         # e.g., ['setosa', 'versicolor', 'virginica']

# Prediction function
def predict(features: list) -> dict:
    """
    Predict the iris class based on 4 numerical features.
    
    Arguments:
    - features: A list of 4 float values representing measurements
    
    Returns:
    - A dictionary with both the predicted class index and class name
    """
    # Create a one-row DataFrame with feature names
    input_df = pd.DataFrame([features], columns=FEATURE_NAMES)

    # Predict class index (e.g., 0, 1, or 2)
    class_index = int(model.predict(input_df)[0])

    # Map index to actual class name
    class_name = TARGET_NAMES[class_index]

    return {'class_index': class_index, 'class_name': class_name}


# Flask routes

@app.route('/')
def home():
    """
    GET /
    Display a simple HTML message explaining how to use the API.
    """
    return """
    <h2>Flask ML Prediction API</h2>
    <p>Send a POST request to <code>/predict</code> with a JSON body like:</p>
    <pre>{"features": [5.1, 3.5, 1.4, 0.2]}</pre>
    """

@app.route('/predict', methods=['POST'])
def predict_route():
    """
    POST /predict
    Accepts a JSON object with 4 feature values and returns the predicted class.
    """
    data = request.get_json()              # Parse incoming JSON
    features = data.get('features')        # Extract 'features' list

    # Validate input
    if not features or len(features) != 4:
        return jsonify({'error': 'Invalid input, expected 4 features.'}), 400

    # Make prediction and return result
    result = predict(features)
    return jsonify({'prediction': result})


# Run the Flask App
if __name__ == '__main__':
    # Run the Flask dev server on localhost, port 5000
    # Debug mode auto-reloads the server when code changes
    app.run(debug=True, port=5000)
