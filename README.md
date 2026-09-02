# 💳 Credit Card Fraud Detection

A machine learning application that detects potentially fraudulent credit card transactions using Logistic Regression. The trained model is exposed through a FastAPI REST API and integrated with a Streamlit web interface for real-time predictions.

## 🚀 Live Demo

### 🌐 Streamlit Application
https://detecting-credit-card-fraud-vgwrhrds5kvclfbghrt6gu.streamlit.app/

### ⚡ FastAPI
https://detecting-credit-card-fraud.onrender.com/

### 📚 API Documentation
https://detecting-credit-card-fraud.onrender.com/docs

---

## 📌 Project Overview

Credit card fraud detection is a binary classification problem where transactions are classified as either:

- `0` → Legitimate Transaction
- `1` → Fraudulent Transaction

The dataset contains highly imbalanced transaction data, with fraudulent transactions representing only a very small portion of all transactions.

To address this imbalance, a balanced dataset was created by sampling legitimate transactions and combining them with fraudulent transactions before training the model.

The final application provides a simple interface where users can enter transaction features and receive a prediction from the deployed machine learning model.

---

## 🏗️ System Architecture

```text
                    User
                     │
                     ▼
            ┌─────────────────┐
            │    Streamlit    │
            │   Web Interface │
            └────────┬────────┘
                     │
                     │ HTTP POST
                     ▼
            ┌─────────────────┐
            │     FastAPI     │
            │    REST API     │
            └────────┬────────┘
                     │
                     ▼
            ┌─────────────────┐
            │  ML Pipeline    │
            │ StandardScaler  │
            │       +         │
            │ LogisticReg.    │
            └────────┬────────┘
                     │
                     ▼
             Prediction Result
              ┌──────┴──────┐
              ▼             ▼
         Legitimate       Fraudulent
