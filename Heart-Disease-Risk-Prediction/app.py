# app.py
from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and encoders
model = joblib.load('model.pkl')
encoders = joblib.load('encoders.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            # Get form data
            data = {
                'age': int(request.form['age']),
                'sex': request.form['sex'],
                'chest_pain_type': request.form['chest_pain_type'],
                'resting_blood_pressure': int(request.form['resting_blood_pressure']),
                'cholestoral': int(request.form['cholestoral']),
                'rest_ecg': request.form['rest_ecg'],
                'Max_heart_rate': int(request.form['max_heart_rate']),  # <- match with lowercase name
                'oldpeak': float(request.form['oldpeak']),
                'thalassemia': request.form['thalassemia'],
            }

            # Encode categorical values (if values are already int, convert to int safely)
            for col in ['sex', 'chest_pain_type', 'rest_ecg', 'thalassemia']:
                if data[col] not in [0, 1, 2, 3]:  # string inputs
                    data[col] = encoders[col].transform([data[col]])[0]
                else:
                    data[col] = int(data[col])

            # Prepare data for prediction
            input_features = np.array([[data[col] for col in model.feature_names_in_]])
            prediction = model.predict(input_features)[0]
            prediction_proba = model.predict_proba(input_features)[0][1]

            # Result label
            if prediction == 0:
                result = f"No Risk (Confidence: {(1 - prediction_proba) * 100:.1f}%)"
            else:
                result = f"At Risk (Confidence: {prediction_proba * 100:.1f}%)"

        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
