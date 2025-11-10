# tests/test_main.py

from fastapi.testclient import TestClient
from app.main import app

# Create a single client instance for all tests
client = TestClient(app)

def test_health_check():
    """
    Tests that the /health endpoint is working correctly.
    """
    response = client.get("/health")
    
    # Assert that the status code is 200 OK
    assert response.status_code == 200
    # Assert that the response JSON is as expected
    assert response.json() == {"status": "ok", "message": "API is healthy and running."}


def test_predict_success():
    """
    Tests a successful prediction from the /predict endpoint.
    """
    payload = {"text": "This is a test"}
    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["input_text"] == "This is a test"
    assert response_data["prediction"] == 14 # len("This is a test")


def test_predict_validation_error():
    """
    Tests the /predict endpoint with invalid input data.
    FastAPI should return a 422 Unprocessable Entity error.
    """
    # The 'text' field is missing from the payload
    payload = {"invalid_key": "some value"}
    response = client.post("/predict", json=payload)

    # Assert that the status code is 422, indicating a validation error
    assert response.status_code == 422