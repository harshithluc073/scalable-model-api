# app/main.py

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator


from .ml.model import PlaceholderModel, get_model

# Create an instance of the FastAPI class
app = FastAPI(
    title="Scalable Model Serving API",
    description="A production-ready API for serving machine learning models.",
    version="0.1.0",
)

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