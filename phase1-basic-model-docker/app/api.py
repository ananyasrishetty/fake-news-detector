# app/api.py

from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load your trained model
model = joblib.load("model.pkl")

# Define input structure
class NewsRequest(BaseModel):
    text: str

# Create FastAPI app
app = FastAPI()

@app.post("/predict")
def predict_news(request: NewsRequest):
    # Get prediction probabilities
    proba = model.predict_proba([request.text])[0]
    
    # If prob. of class 1 (fake) > 0.5 → predict fake
    prediction = int(proba[1] > 0.5)
    
    # Pick the confidence for the predicted class
    confidence = round(proba[1] if prediction == 1 else 1 - proba[1], 4)
    
    label = "Fake" if prediction == 1 else "Real"
    return {"label": label, "confidence": confidence}
