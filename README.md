# Scalable Model Serving API

This project provides a production-ready blueprint for packaging a trained machine learning model into a high-performance, scalable, and monitored API.

The system uses FastAPI for the API, Docker and Docker Compose for containerization, Prometheus for metrics collection, and Grafana for visualization. It also includes a CI pipeline with GitHub Actions to validate the Docker build on every push.

---

## Features

*   **FastAPI:** High-performance asynchronous API framework with automatic Swagger/OpenAPI documentation.
*   **Docker & Docker Compose:** The entire application stack is containerized for portability and easy setup with a single command.
*   **Live Monitoring:**
    *   **Prometheus:** Scrapes real-time performance metrics from the API (latency, request counts, etc.).
    *   **Grafana:** Provides a dashboard for visualizing API health and performance metrics.
*   **CI/CD:** A GitHub Actions workflow automatically validates the Docker build on every push to the `main` branch.
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

2.  **Launch the stack using Docker Compose:**
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
