import pickle
import numpy as np
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


# Load model
MODEL_PATH = Path(__file__).resolve().parent / "model.pkl"

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)


# FastAPI application
app = FastAPI(
    title="Credit Card Fraud Detection API",
    description="Machine Learning API for detecting fraudulent credit card transactions.",
    version="1.0.0"
)


class TransactionRequest(BaseModel):
    features: list[float] = Field(
        ...,
        min_length=30,
        max_length=30,
        description="30 values: Time, V1-V28, Amount"
    )


@app.get("/")
def home():
    return {
        "message": "Credit Card Fraud Detection API",
        "status": "running",
        "docs": "/docs"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": True
    }


@app.post("/predict")
def predict(transaction: TransactionRequest):

    try:
        features = np.asarray(
            transaction.features,
            dtype=np.float64
        ).reshape(1, -1)

        prediction = int(model.predict(features)[0])

        label = (
            "Fraudulent Transaction"
            if prediction == 1
            else "Legitimate Transaction"
        )

        result = {
            "prediction": prediction,
            "label": label
        }

        if hasattr(model, "predict_proba"):
            probability = float(
                model.predict_proba(features)[0][1]
            )
            result["fraud_probability"] = round(probability, 4)

        return result

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Prediction failed: {e}"
        )