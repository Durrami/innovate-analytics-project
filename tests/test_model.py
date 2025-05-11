import os
import sys
import pandas as pd
import numpy as np
import pytest

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_processing import extract_data, transform_data, load_data
from src.model import train_model, predict
from src.utils import create_sample_data

def test_data_processing_pipeline():
    """Test the entire data processing pipeline"""
    # Create sample data
    create_sample_data(n_samples=20, output_path='data/raw/test_sample.csv')
    
    # Run pipeline
    extracted_path = extract_data(
        input_path='data/raw/test_sample.csv', 
        output_path='data/raw/test_extracted.csv'
    )
    transformed_path = transform_data(
        input_path=extracted_path, 
        output_path='data/processed/test_transformed.csv'
    )
    final_path = load_data(
        input_path=transformed_path, 
        output_path='data/processed/test_final.csv'
    )
    
    # Check if final file exists
    assert os.path.exists(final_path)
    
    # Check if data is properly processed
    df = pd.read_csv(final_path)
    assert 'feature1' in df.columns
    assert 'target' in df.columns

def test_model_training():
    """Test model training functionality"""
    # Create test data
    create_sample_data(n_samples=30, output_path='data/raw/test_model.csv')
    extract_data(
        input_path='data/raw/test_model.csv', 
        output_path='data/raw/test_model_extracted.csv'
    )
    transform_data(
        input_path='data/raw/test_model_extracted.csv', 
        output_path='data/processed/test_model_transformed.csv'
    )
    final_path = load_data(
        input_path='data/processed/test_model_transformed.csv', 
        output_path='data/processed/test_model_final.csv'
    )
    
    # Train model
    model, accuracy = train_model(
        data_path=final_path, 
        model_path='models/test_model.pkl'
    )
    
    # Check if model is trained successfully
    assert accuracy > 0.0
    assert os.path.exists('models/test_model.pkl')

def test_model_prediction():
    """Test prediction functionality"""
    # Create test data and model
    create_sample_data(n_samples=10, output_path='data/raw/test_predict.csv')
    df = pd.read_csv('data/raw/test_predict.csv')
    X = df.drop(['id', 'target'], axis=1)
    
    # Ensure model exists
    if not os.path.exists('models/test_model.pkl'):
        test_model_training()
    
    # Make predictions
    predictions = predict(model_path='models/test_model.pkl', data=X)
    
    # Check predictions
    assert len(predictions) == len(X)
    assert all(isinstance(p, (int, np.integer)) for p in predictions)