# Innovate Analytics ML Project

This repository contains the complete MLOps implementation for Innovate Analytics' machine learning system.

## Project Overview

This system implements a complete machine learning pipeline, from data processing to model training and deployment, using MLOps best practices including:

- CI/CD with GitHub Actions and Jenkins
- Containerization with Docker
- Orchestration with Kubernetes
- Data pipeline with Airflow
- Experiment tracking with MLflow

## Getting Started

### Prerequisites

- Python 3.10+
- Docker
- Kubernetes/Minikube
- Jenkins
- Airflow
- MLflow

### Installation

1. Clone the repository:
git clone https://github.com/durrami/innovate-analytics-project.git
cd innovate-analytics-project

2. Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

### Running the Pipeline

1. Start Airflow:
airflow standalone

2. Start MLflow:
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns

3. Run the Airflow DAG to process data and train the model:
airflow dags trigger ml_pipeline

4. Build and run the Docker container:
docker build -t innovate-analytics/ml-app .
docker run -p 8000:8000 innovate-analytics/ml-app

5. Deploy to Kubernetes:
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml

## Development Workflow

1. Create a feature branch from `dev`:
git checkout -b feature/your-feature-name

2. Make changes and commit them:
git add .
git commit -m "Your descriptive commit message"

3. Push your branch and create a Pull Request into `dev`:
git push -u origin feature/your-feature-name

4. After review and approval, merge into `dev`
5. For releases, create a PR from `dev` to `test`, then from `test` to `main`

## API Usage

Once deployed, the API can be accessed at:
- Locally: http://localhost:8000
- Kubernetes: http://your-cluster-ip/

Predict endpoint:
- POST /predict
- Input: JSON with feature values
- Output: Prediction results

Example:
curl -X POST http://localhost:8000/predict 
-H "Content-Type: application/json" 
-d '[{"feature1": 5.1, "feature2": 3.5, "feature3": 1.4}]'

## Project Structure

- `.github/workflows/`: CI pipeline with GitHub Actions
- `airflow/dags/`: Airflow DAG definitions
- `data/`: Data storage
- `kubernetes/`: Kubernetes deployment files
- `models/`: Trained model storage
- `src/`: Source code
- `tests/`: Unit and integration tests