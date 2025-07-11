from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return "✅ Model is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array([data['features']])
    prediction = model.predict(features)
    return jsonify({'prediction': prediction.tolist()})
if __name__ =='__main__':
    app.run(debug=True)