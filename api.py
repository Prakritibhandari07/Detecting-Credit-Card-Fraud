import pickle
import numpy as np
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


# --------------------------------------------------
# Load Model
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model.pkl"

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)


# --------------------------------------------------
# FastAPI App
# --------------------------------------------------

app = FastAPI(
    title="Credit Card Fraud Detection API",
    description=(
        "Machine Learning API that predicts whether a credit card "
        "transaction is legitimate or fraudulent."
    ),
    version="1.0.0"
)


# --------------------------------------------------
# Request Schema
# --------------------------------------------------

class TransactionRequest(BaseModel):
    features: list[float] = Field(
        ...,
        min_length=30,
        max_length=30,
        description=(
            "30 values in this order: "
            "Time, V1-V28, Amount"
        )
    )


# --------------------------------------------------
# Home Endpoint
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "Credit Card Fraud Detection API",
        "status": "running",
        "docs": "/docs"
    }


# --------------------------------------------------
# Health Check
# --------------------------------------------------

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": True
    }


# --------------------------------------------------
# Prediction Endpoint
# --------------------------------------------------

@app.post("/predict")
def predict(transaction: TransactionRequest):

    try:
        features = np.asarray(
            transaction.features,
            dtype=np.float64
        ).reshape(1, -1)

        # Make prediction
        prediction = int(model.predict(features)[0])

        # Fraud probability
        fraud_probability = None

        if hasattr(model, "predict_proba"):
            probability = model.predict_proba(features)[0]
            fraud_probability = float(probability[1])

        # Prepare response
        if prediction == 0:
            label = "Legitimate Transaction"
        else:
            label = "Fraudulent Transaction"

        response = {
            "prediction": prediction,
            "label": label
        }

        if fraud_probability is not None:
            response["fraud_probability"] = round(
                fraud_probability, 4
            )

        return response

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Prediction failed: {str(e)}"
        )

               
