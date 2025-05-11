from flask import Flask, request, jsonify
import pandas as pd
import joblib
import os
from model import predict

app = Flask(__name__)

MODEL_PATH = 'models/model.pkl'

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    try:
        # Get input data from request
        data = request.json
        df = pd.DataFrame(data)
        
        # Make predictions
        predictions = predict(model_path=MODEL_PATH, data=df)
        
        # Return predictions
        return jsonify({
            'status': 'success',
            'predictions': predictions.tolist()
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

if __name__ == '__main__':
    # Ensure model exists (for testing purposes)
    if not os.path.exists(MODEL_PATH):
        print(f"Warning: Model not found at {MODEL_PATH}. Make sure to train it first.")
        os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
        # Create a dummy model for demonstration
        from sklearn.ensemble import RandomForestClassifier
        dummy_model = RandomForestClassifier(n_estimators=100, random_state=42)
        dummy_model.fit([[1, 2, 3]], [0])  # Dummy training
        joblib.dump(dummy_model, MODEL_PATH)
    
    # Run the Flask app
    app.run(host='0.0.0.0', port=8000, debug=True)