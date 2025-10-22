from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load('predi_salaire_model.pkl')
model_columns = joblib.load('salaire_model_columns.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    json_ = request.json
    query_df = pd.DataFrame([json_])

    query_processed = pd.get_dummies(query_df).reindex(columns=model_columns, fill_value=0)

    prediction = model.predict(query_processed)

    return jsonify({'prediction': str(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)