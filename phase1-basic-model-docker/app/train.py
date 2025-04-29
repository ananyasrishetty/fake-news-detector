# app/train.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import joblib

# Load both datasets
fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

# Add labels: 1 = fake, 0 = real
fake["label"] = 1
true["label"] = 0

# Combine them
df = pd.concat([fake, true], axis=0).reset_index(drop=True)

# Shuffle (important!)
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Use 'text' column as input
#X = df['text']
X = df['title'] + " " + df['text']
y = df['label']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', max_df=0.7)),
    ('clf', LogisticRegression(max_iter=1000))
])

# Train
pipeline.fit(X_train, y_train)

# Test
y_pred = pipeline.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")

# Save
joblib.dump(pipeline, 'model.pkl')
