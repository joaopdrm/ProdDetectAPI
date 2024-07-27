from fastapi import FastAPI
from app.services.prediction import get_prediction
from app.schemas.prediction import PredictionRequest, PredictionResponse

app = FastAPI()

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    return get_prediction(request)