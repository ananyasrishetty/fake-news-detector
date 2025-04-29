# app/predict.py

import joblib

# Load the trained model
model = joblib.load("model.pkl")

# Sample input
sample_text = """
Pentagon chief Hegseth shared sensitive Yemen war plans in second Signal chat
"""

# Make a prediction
prediction = model.predict([sample_text])[0]

# Show result
label = "Fake" if prediction == 1 else "Real"
print(f"Prediction: {label}")

