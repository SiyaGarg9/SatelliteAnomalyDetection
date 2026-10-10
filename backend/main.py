from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Satellite Telemetry Anomaly Detection API",
    description="Backend API for satellite health monitoring",
    version="1.0.0"
)


class Telemetry(BaseModel):
    temperature: float
    voltage: float
    current: float


@app.get("/")
def home():
    return {
        "message": "Satellite Anomaly Detection API is running"
    }


@app.get("/telemetry")
def get_telemetry():
    return {
        "temperature": [25, 26, 25.5, 27, 28, 29, 31, 30],
        "voltage": [5.1, 5.0, 5.1, 5.0, 4.9, 4.8, 4.7, 4.8],
        "current": [1.2, 1.3, 1.2, 1.4, 1.5, 1.6, 1.8, 1.7]
    }


@app.post("/predict")
def predict(data: Telemetry):

    # Temporary prediction logic
    # Later this will be replaced by your friend's ML model

    if data.temperature > 40 or data.voltage < 4.0:
        score = 0.91
        severity = "CRITICAL"
        status = "ANOMALY"

    elif data.temperature > 35 or data.voltage < 4.5:
        score = 0.67
        severity = "HIGH"
        status = "ANOMALY"

    else:
        score = 0.15
        severity = "NORMAL"
        status = "NORMAL"

    return {
        "anomaly_score": score,
        "status": status,
        "severity": severity
    }
@app.get("/anomalies")
def get_anomalies():
    return [
        {
            "time": "10:25",
            "score": 0.82,
            "severity": "HIGH"
        },
        {
            "time": "11:43",
            "score": 0.91,
            "severity": "CRITICAL"
        },
        {
            "time": "13:12",
            "score": 0.45,
            "severity": "WARNING"
        }
    ]

@app.get("/model-performance")
def model_performance():
    return [
        {
            "model": "Isolation Forest",
            "precision": 0.78,
            "recall": 0.81,
            "f1": 0.79
        },
        {
            "model": "Autoencoder",
            "precision": 0.84,
            "recall": 0.86,
            "f1": 0.85
        },
        {
            "model": "LSTM Autoencoder",
            "precision": 0.89,
            "recall": 0.91,
            "f1": 0.90
        }
    ]