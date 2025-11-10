# Scalable Model Serving API

This project provides a production-ready blueprint for packaging a trained machine learning model into a high-performance, scalable, and monitored API.

The system uses FastAPI for the API, Docker and Docker Compose for containerization, Prometheus for metrics collection, and Grafana for visualization. It also includes a CI pipeline with GitHub Actions to validate the Docker build on every push and publish release images.

---

## Features

*   **FastAPI:** High-performance asynchronous API framework with automatic Swagger/OpenAPI documentation.
*   **Docker & Docker Compose:** The entire application stack is containerized for portability and easy setup with a single command.
*   **Automated Testing:** Unit tests are included and run with `pytest` to validate model behavior and API endpoints.
*   **Live Monitoring:**
    *   **Prometheus:** Scrapes real-time performance metrics from the API (latency, request counts, etc.).
    *   **Grafana:** Provides a dashboard for visualizing API health and performance metrics.
*   **CI/CD Pipeline:** A GitHub Actions workflow validates the code and Docker image; on merges to `main` it also builds and publishes the Docker image to the GitHub Container Registry (GHCR).
*   **Externalized Configuration:** Runtime settings are managed via environment variables so you can tweak behavior without changing code.
*   **Structured Logging:** Application logs are emitted in JSON format to make them easy to collect, parse, and analyze by logging systems.
*   **Scalable Design:** The architecture is designed to be deployed and scaled in cloud environments.

---

## Getting Started

Follow these instructions to get the entire application stack running on your local machine.

### Prerequisites

*   [Docker Desktop](https://www.docker.com/products/docker-desktop/) must be installed and running.
*   Git for cloning the repository.

### Running the Application

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/harshithluc073/scalable-model-api.git
    cd scalable-model-api
    ```

2.  **Configure the Environment (Optional):**

    If you'd like to customize the project locally, copy the example environment file and edit it:

    ```bash
    copy .env.example .env
    ```

    Then edit the newly created `.env` file to change settings such as the API title, ports, or other runtime values for your local setup. These values are loaded via environment variables when the application and compose stack start.

3.  **Launch the stack using Docker Compose:**
    ```bash
    docker-compose up --build
    ```
    This command will build the FastAPI image, pull the Prometheus and Grafana images, and start all the containers.

---

## How to Use

Once the stack is running, the following endpoints are available:

*   **API Documentation (Swagger UI):**
    *   **URL:** `http://localhost:8000/docs`
    *   Use this interactive UI to send requests to the `/predict` endpoint.

*   **Prometheus UI:**
    *   **URL:** `http://localhost:9090`
    *   Here you can explore collected metrics. Check `Status > Targets` to ensure Prometheus is successfully scraping the API.

*   **Grafana Dashboard:**
    *   **URL:** `http://localhost:3000`
    *   This is where you can build and view dashboards to monitor the API's performance.

---

## Development Guide

### Setting Up a Local Virtual Environment

1. Create a virtual environment and activate it:

     - On Windows (PowerShell):

         ```powershell
         python -m venv .venv
         .\.venv\Scripts\Activate.ps1
         ```

     - On macOS / Linux:

         ```bash
         python3 -m venv .venv
         source .venv/bin/activate
         ```

2. Install development dependencies:

        ```bash
        pip install -r requirements-dev.txt
        ```

### Running Tests

Run the automated test suite with pytest:

```bash
pytest
```

This runs unit tests located in the `tests/` folder and helps validate the API behavior and model code during development.

---

## CI/CD Pipeline

The repository contains a GitHub Actions workflow that automates testing, image build, and publishing. The workflow definition lives at `.github/workflows/ci.yml`.

Pipeline stages:

- **Test:** Runs the `pytest` suite to validate code and catch regressions.
- **Build:** Builds the Docker image for the FastAPI service.
- **Push:** When changes are merged to the `main` branch, the pipeline pushes the built image to the GitHub Container Registry (GHCR) so releases and images are available to downstream deployments.

Published images can be found in the "Packages" section of this repository's GitHub page.

---

## Project Structure

```    scalable-model-api/
├── app/                    # Main application source code
│   ├── ml/                 # Machine learning model code
│   │   └── model.py
│   └── main.py             # FastAPI application entrypoint
├── monitoring/             # Monitoring configuration
│   └── prometheus.yml
├── .github/workflows/      # GitHub Actions CI/CD workflows
│   └── ci.yml
├── .dockerignore
├── .gitignore
├── Dockerfile              # Defines the application container
├── docker-compose.yml      # Defines the entire application stack
├── README.md               # This file
└── requirements.txt        # Python dependencies
