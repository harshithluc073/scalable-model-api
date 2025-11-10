# app/config.py

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Defines the application's configuration settings.
    Pydantic will automatically attempt to load these from environment variables.
    """
    # Load environment variables from a .env file if it exists (for local dev)
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # --- Application Settings ---
    API_TITLE: str = "Scalable Model Serving API"
    API_DESCRIPTION: str = "A production-ready API for ML models."
    API_VERSION: str = "0.1.0"

    # --- Model Settings ---
    MODEL_VERSION: str = "1.0.0-placeholder"

# Create a single, reusable instance of the settings
settings = Settings()