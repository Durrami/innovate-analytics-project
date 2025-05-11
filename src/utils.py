import os
import pandas as pd
import numpy as np

def create_sample_data(n_samples=100, output_path='data/raw/sample_data.csv'):
    """Create a sample dataset if none exists"""
    if os.path.exists(output_path):
        print(f"Sample data already exists at {output_path}")
        return
    
    # Generate synthetic data
    np.random.seed(42)
    feature1 = np.random.normal(loc=5.0, scale=1.0, size=n_samples)
    feature2 = np.random.normal(loc=3.0, scale=0.5, size=n_samples)
    feature3 = np.random.normal(loc=2.0, scale=1.5, size=n_samples)
    
    # Create target based on features (simple rule)
    target = (feature1 + feature2 > feature3).astype(int)
    
    # Create DataFrame
    df = pd.DataFrame({
        'id': range(1, n_samples + 1),
        'feature1': feature1,
        'feature2': feature2,
        'feature3': feature3,
        'target': target
    })
    
    # Save to CSV
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Sample data created and saved to {output_path}")