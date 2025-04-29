# 🤖 Phase 2: BERT Fake News Detector (AWS SageMaker)

This folder contains the production-ready version of the Fake News Detector using a fine-tuned BERT model.

---

## 🔹 Features

- Model: DistilBERT fine-tuned using HuggingFace Transformers
- Training: Done on Google Colab with GPU
- Deployment: Real-time inference endpoint on AWS SageMaker
- App: Python CLI (menu-based) that calls AWS endpoint
- Secure credential use (no secrets committed)

---

## 🛠 Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Add your AWS credentials securely (env variables or inside `aws_predictor.py` temporarily).

3. Make sure your SageMaker endpoint is active.

4. Run the CLI app:
   ```bash
   python app/aws_predictor.py
   ```

---

## 📋 Notes

- Model files (config.json, tokenizer, etc.) removed from GitHub to reduce size — they're already in model.tar.gz on AWS.
- Includes support for single and batch prediction.
