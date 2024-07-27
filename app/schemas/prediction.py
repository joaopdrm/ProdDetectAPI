from pydantic import BaseModel
from typing import List

class PredictionRequest(BaseModel):

    image_path: str

class PredictionResponse(BaseModel):

    labels: List[str]
    scores: List[float]
    