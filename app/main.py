# app/main.py

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator
import structlog


from .ml.model import PlaceholderModel, get_model
from .config import settings, configure_logging

# Create an instance of the FastAPI class
app = FastAPI(
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version=settings.API_VERSION,
)

configure_logging()
log = structlog.get_logger(__name__)

# --- Pydantic Models for Input and Output ---
Instrumentator().instrument(app).expose(app)

class PredictionRequest(BaseModel):
    text: str

class PredictionResponse(BaseModel):
    input_text: str
    prediction: int

class StatusMessage(BaseModel):
    status: str
    message: str

# --- API Endpoints ---

@app.get("/", response_model=StatusMessage, tags=["General"])
def read_root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"status": "ok", "message": "Welcome to the Scalable Model Serving API!"}

@app.get("/health", response_model=StatusMessage, tags=["General"])
def health_check():
    """
    Health check endpoint to confirm the API is running.
    """
    return {"status": "ok", "message": "API is healthy and running."}

@app.post("/predict", response_model=PredictionResponse, tags=["Machine Learning"])
def predict(
    request: PredictionRequest,
    model: PlaceholderModel = Depends(get_model)
):
    """
    Takes text input and returns a prediction from the model.
    """
    prediction_result = model.predict(request.text)
    return prediction_result