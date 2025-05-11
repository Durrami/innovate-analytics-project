FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Create necessary directories
RUN mkdir -p data/raw data/processed models

# Make sure the ML model exists
RUN python -c "from src.utils import create_sample_data; from src.data_processing import extract_data, transform_data, load_data; from src.model import train_model; create_sample_data(); extract_data(); transform_data(); load_data(); train_model()"

# Expose port for API
EXPOSE 8000

# Run the Flask app
CMD ["python", "src/app.py"]