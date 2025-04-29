# 📰 Fake News Detection (Two-Phase ML Project)

This project focuses on detecting whether a news article headline is **Fake** or **Real**, with full end-to-end implementation from model building to cloud deployment.

It consists of two major phases:

---

## 🔹 Phase 1: Basic Logistic Regression + Docker

📁 Folder: `phase1-basic-model-docker/`

- ✅ Built a simple Logistic Regression classifier using the Fake News dataset.
- ✅ Developed a FastAPI application to serve predictions.
- ✅ Dockerized the app using a custom `Dockerfile`.
- ✅ Tested the API locally via `curl` and Postman.
- ✅ Demonstrated foundational ML + deployment principles.

---

## 🔹 Phase 2: Fine-Tuned BERT + AWS SageMaker

📁 Folder: `phase2-bert-sagemaker/`

- ✅ Fine-tuned a `DistilBERT` model using HuggingFace Transformers.
- ✅ Used Google Colab (with GPU) for training.
- ✅ Packaged model artifacts into `model.tar.gz`.
- ✅ Uploaded to AWS S3 and deployed via AWS SageMaker real-time endpoint.
- ✅ Built a dynamic menu-based Python app (`aws_predictor.py`) that calls the SageMaker endpoint for live predictions.

---

## ✅ Features

- Real-time inference powered by AWS SageMaker.
- Fully interactive CLI with single and batch headline checking.
- Secure credential handling and production-ready structure.
- Modular design with clear separation of training, deployment, and frontend logic.

---

## 📦 Repository Structure

```bash
fake-news-detector/
├── phase1-basic-model-docker/
│   └── ... FastAPI + Docker files
│
├── phase2-bert-sagemaker/
│   ├── app/
│   │   └── aws_predictor.py
│   │   └── model-info.txt (optional)
│   ├── model.tar.gz (optional if small)
│   ├── requirements.txt
│   └── README.md
```

---

## 🚀 Getting Started

To use the menu app in Phase 2:

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Open `aws_predictor.py` and add your AWS credentials.

3. Run:
   ```
   python aws_predictor.py
   ```

4. Choose between checking a single or multiple headlines from the menu.

---

## 🎯 Future Enhancements

- Full transition to a BERT-based inference model (replace logistic regression completely).
- Add Streamlit or web interface for public interaction.
- Add CSV export and logs for results.
- Integrate AWS Lambda + API Gateway for REST endpoint deployment.

---

## 🏁 Credits

Built and deployed by Ananya Shetty  
This project demonstrates full-stack ML skills including model training, Dockerization, cloud deployment, and production-grade Python automation.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
