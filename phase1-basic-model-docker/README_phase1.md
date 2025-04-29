# 🧱 Phase 1: Fake News Detection with Logistic Regression + Docker

This folder contains the first version of the Fake News Detector.

---

## 🔹 Features

- Model: Logistic Regression (scikit-learn)
- Dataset: Fake News Dataset (Kaggle)
- App: FastAPI backend
- Deployment: Dockerized with a clean `Dockerfile`
- Testing: Used Postman and curl to hit local endpoints

---

## 🔧 Usage

1. Build Docker image:
   ```bash
   docker build -t fake-news-api .
   ```

2. Run container:
   ```bash
   docker run -p 8000:8000 fake-news-api
   ```

3. Use Postman or curl to send POST requests to:
   ```
   http://localhost:8000/predict
   ```

---

## 📋 Notes

- This version used basic ML and pattern matching — not deep learning.
- Good for showing understanding of Docker + ML API building.

---
