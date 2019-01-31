from flask import Flask, jsonify, request
import os, joblib
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({"response": "hello data science"})

@app.route('/predict', methods=['POST'])
def predict():
    request_payload = request.json
    input_features = pd.DataFrame([], columns=column_order)
    input_features = input_features.append(request_payload, ignore_index=True)
    input_features = input_features.fillna(0)

    prediction = model.predict(input_features.values.tolist()).tolist()
    return jsonify({'predicted price (thousands)': prediction})

if __name__ == '__main__':
    model = joblib.load('ex_boston_house_prices/linear_model.joblib') 
    column_order = joblib.load('ex_boston_house_prices/column_order.txt') 

    app.run(port=8080, host='0.0.0.0', debug=True)