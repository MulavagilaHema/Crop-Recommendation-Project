from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Load the trained machine learning model
model = joblib.load('crop_recommendation_model.pkl')  # Ensure this file exists

# Define the route for predicting crops
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve data from the JSON request
        data = request.get_json()

        # Extract feature values from the JSON
        N = float(data['N'])
        P = float(data['P'])
        K = float(data['K'])
        temperature = float(data['temperature'])
        humidity = float(data['humidity'])
        ph = float(data['ph'])
        rainfall = float(data['rainfall'])

        # Prepare the feature array for prediction
        features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

        # Use the model to predict the crop
        predicted_crop = model.predict(features)[0]

        # Return the prediction as a JSON response
        return jsonify({'predicted_crop': predicted_crop})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
