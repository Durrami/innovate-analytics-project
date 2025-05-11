import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os
import mlflow
import mlflow.sklearn

def train_model(data_path='data/processed/final_data.csv', model_path='models/model.pkl'):
    """Train a simple classification model and track with MLflow"""
    # Start MLflow run
    mlflow.start_run()
    
    # Load data
    df = pd.read_csv(data_path)
    X = df.drop('target', axis=1)
    if 'id' in X.columns:
        X = X.drop('id', axis=1)
    y = df['target']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model (simple RandomForest)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    # Log parameters, metrics, and model with MLflow
    mlflow.log_param("n_estimators", 100)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(model, "random-forest-model")
    
    # Save model to disk
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)
    
    # End MLflow run
    mlflow.end_run()
    
    print(f"Model trained with accuracy: {accuracy:.4f}")
    print(f"Model saved to: {model_path}")
    return model, accuracy

def predict(model_path='models/model.pkl', data_path=None, data=None):
    """Make predictions using the trained model"""
    # Load the model
    model = joblib.load(model_path)
    
    # Load data or use provided data
    if data is None and data_path is not None:
        data = pd.read_csv(data_path)
        if 'id' in data.columns and 'target' in data.columns:
            data = data.drop(['id', 'target'], axis=1, errors='ignore')
    
    # Make predictions
    predictions = model.predict(data)
    return predictions