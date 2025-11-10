# app/ml/model.py

class PlaceholderModel:
    """
    A simple placeholder class that mimics a real ML model.
    It "predicts" the length of the input text.
    """
    def __init__(self):
        # In a real scenario, you would load your model from a file here
        # For example: self.model = joblib.load("model.pkl")
        self.model_version = "1.0.0-placeholder"
        print(f"Model version {self.model_version} loaded.")

    def predict(self, text: str) -> dict:
        """
        Simulates a prediction by returning the length of the input text.
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")

        prediction = len(text)
        return {"input_text": text, "prediction": prediction}

# Create a single instance of the model to be used by the API
model = PlaceholderModel()

def get_model():
    """
    Returns the singleton model instance.
    This is a simple way to manage the model's lifecycle.
    """
    return model