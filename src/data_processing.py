import pandas as pd
import os

def extract_data(input_path='data/raw/sample_data.csv', output_path='data/raw/extracted_data.csv'):
    """Extract data from source location"""
    # In a real scenario, this might fetch data from an API or database
    df = pd.read_csv(input_path)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    return output_path

def transform_data(input_path='data/raw/extracted_data.csv', output_path='data/processed/transformed_data.csv'):
    """Transform the data (simple example)"""
    df = pd.read_csv(input_path)
    
    # Simple transformation - normalize numeric features
    for col in ['feature1', 'feature2', 'feature3']:
        if col in df.columns:
            df[col] = (df[col] - df[col].mean()) / df[col].std()
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    return output_path

def load_data(input_path='data/processed/transformed_data.csv', output_path='data/processed/final_data.csv'):
    """Load data into final destination"""
    df = pd.read_csv(input_path)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Data processing complete. Final data saved to {output_path}")
    return output_path