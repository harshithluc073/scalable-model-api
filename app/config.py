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


# app/config.py (add to the bottom)

import logging
import sys
import structlog

# --- LOGGING CONFIGURATION ---

def configure_logging():
    """
    Configures structured logging for the entire application.
    """
    # Define the processing chain for log records.
    shared_processors = [
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
    ]

    # Configure structlog to wrap Python's standard logging.
    structlog.configure(
        processors=[
            *shared_processors,
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

    # Define the formatter for the logs. We use JSON for production-readiness.
    formatter = structlog.stdlib.ProcessorFormatter(
        processor=structlog.processors.JSONRenderer(),
        foreign_pre_chain=shared_processors,
    )

    # Create a handler to output logs to the console (stdout).
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    # Get the root logger and add our configured handler.
    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.INFO)

    print("Structured logging configured.")