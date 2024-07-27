from app.utils.loader import load_model, predict
from app.schemas.prediction import PredictionRequest, PredictionResponse

model = load_model()

def get_prediction(request: PredictionRequest) -> PredictionResponse:

    labels, scores = predict(model, request.image_path)
    return PredictionResponse(labels=labels, scores=scores)
