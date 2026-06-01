# ✈️ Airline Customer Intelligence System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-Deployed-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)

**Transform raw customer feedback into actionable business intelligence — in real time.**

[Live Demo][[Add Link](http://airline-sentiment-engine-fdcpdpamerfygbb6.austriaeast-01.azurewebsites.net)] · [Kaggle Notebook][[Add Link](https://www.kaggle.com/code/hermitsays/airline-customer-intelligence-system)] 

</div>

---

## 🧠 What Is This?

Airlines collect thousands of customer reviews every day — yet most of this signal goes unprocessed, buried in spreadsheets or support queues.

This project builds a **production-grade ML system** that automatically reads customer feedback and answers two critical questions:

> *"How does the customer feel?"* → **Sentiment Classification**
> *"Why do they feel that way?"* → **Reason Prediction**

The result is a fully deployed, containerized REST API that any product or analytics team can plug into — no data science background required.

---

## 🏗️ System Architecture

```
Customer Feedback (raw text)
        │
        ▼
┌───────────────────┐
│   Preprocessing   │  ← Tokenization, stopword removal, TF-IDF vectorization
│   (NLP Pipeline)  │
└────────┬──────────┘
         │
         ├──────────────────────────┐
         ▼                          ▼
┌─────────────────┐       ┌──────────────────────┐
│   Sentiment     │       │   Reason Prediction   │
│  Classifier     │       │       Model           │
│ (Pos/Neu/Neg)   │       │ (Root cause factors)  │
└────────┬────────┘       └──────────┬────────────┘
         └──────────┬────────────────┘
                    ▼
          ┌──────────────────┐
          │   FastAPI Layer  │  ← REST endpoints, input validation, error handling
          └────────┬─────────┘
                   ▼
          ┌──────────────────┐
          │  Docker Container│
          └────────┬─────────┘
                   ▼
          ┌──────────────────┐
          │   Microsoft Azure│  ← Cloud deployment, scalable inference
          └──────────────────┘
```

---

## 🔑 Key Features

- **Dual-model inference** — Runs sentiment classification and reason prediction in a single API call
- **Real-time predictions** — Low-latency FastAPI backend built for production throughput
- **Containerized & portable** — Docker image runs identically in local dev and cloud
- **Azure-deployed** — Live, publicly accessible endpoint hosted on Microsoft Azure
- **Full ML lifecycle** — Covers everything from raw text to cloud-served predictions

---

## 🤖 The Models

### Model 1 — Sentiment Classifier
Predicts whether a piece of customer feedback is **Positive**, **Neutral**, or **Negative**.

| Metric    | Score |
|-----------|-------|
| Accuracy  | `77%` |
| F1 (Macro)| `71%` |
| Classes   | Positive · Neutral · Negative |

### Model 2 — Reason Predictor
Identifies the **primary driver** behind a customer's sentiment — e.g., seat comfort, food quality, staff behavior, delays, etc.

| Metric    | Score |
|-----------|-------|
| Accuracy  | `60%` |
| F1 (Macro)| `52%` |

> Both models were trained with scikit-learn and serialized with `joblib` for fast, consistent loading.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Docker (for containerized run)
- Azure CLI (for cloud deployment)

### Run Locally (Python)

```bash
# 1. Clone the repo
git clone https://github.com/[your-username]/airline-customer-intelligence.git
cd airline-customer-intelligence

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the API server
uvicorn app.main:app --reload --port 8000
```

API is now live at `http://localhost:8000`

### Run with Docker

```bash
# Build the image
docker build -t airline-intelligence .

# Run the container
docker run -p 8000:8000 airline-intelligence
```

---

## 📡 API Reference

### `POST /predict`

Submit customer feedback and receive sentiment + reason predictions.

**Request**
```json
{
  "feedback": "The cabin crew was incredibly helpful, but the flight was delayed by 3 hours."
}
```

**Response**
```json
{
  "sentiment": "Negative",
  "confidence": 0.87,
  "reason": "Flight Delay",
  "reason_confidence": 0.81
}
```

### `GET /health`
Returns API health status. Used by Azure for container liveness checks.

```json
{ "status": "healthy", "model_loaded": true }
```

> Full interactive docs available at `/docs` (Swagger UI) and `/redoc`.

---


---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| ML / NLP | Scikit-learn, Pandas, NumPy |
| API | FastAPI, Uvicorn |
| Serialization | Joblib |
| Containerization | Docker |
| Cloud | Microsoft Azure (Container Apps / App Service) |

---

## 📈 ML Lifecycle Covered

This project walks through the **complete machine learning lifecycle**:

1. **Data Exploration** — Understanding class distributions, missing values, text length analysis
2. **NLP Preprocessing** — Lowercasing, punctuation removal, stopword filtering, lemmatization
3. **Feature Engineering** — TF-IDF vectorization, n-gram tuning
4. **Model Development** — Algorithm selection, hyperparameter tuning, cross-validation
5. **Evaluation** — Confusion matrices, classification reports, per-class F1 scores
6. **Deployment** — FastAPI wrapping, Docker containerization, Azure cloud hosting

---

## 🔗 Links

| Resource | URL |
|---|---|
| 🌐 Live Demo | http://airline-sentiment-engine-fdcpdpamerfygbb6.austriaeast-01.azurewebsites.net |
| 📓 Kaggle Notebook | https://www.kaggle.com/code/hermitsays/airline-customer-intelligence-system |

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<div align="center">

Built with ☕ and Python · Deployed on ☁️ Azure

If you found this useful, drop a ⭐ — it helps more than you think.

</div>
