# train_model.py

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load example dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

# Train a simple model
model = RandomForestClassifier()
model.fit(X,y)

# Save the model to a file
joblib.dump(model, 'model/trained_model.pkl')
print("Model trained and saved to model/trained_model.pkl")