#  Heart Disease Risk Prediction System

This web application predicts the likelihood of heart disease based on user inputs such as age, sex, chest pain type, cholesterol levels, and more. It uses a machine learning model trained on real medical data to provide predictions along with confidence scores.

## 🚀 Features

- 🏥 Predicts heart disease risk with confidence
- 📊 Trained machine learning model (`model.pkl`)
- 🔠 Label encoding for categorical inputs (`encoders.pkl`)
- 💻 Built with Python and Flask
- 🎨 Clean, responsive medical-style UI with HTML/CSS
- 🧼 Strong input validation and error handling
- 🔁 Form resets after each prediction automatically

## 🧠 Technologies Used

| Technology      | Purpose                           |
|-----------------|-----------------------------------|
| Python          | Backend & ML logic                |
| Flask           | Web framework                     |
| HTML/CSS        | Frontend UI                       |
| scikit-learn    | Machine Learning                  |
| NumPy & Pandas  | Data processing                   |
| joblib          | Model and encoder serialization   |

## 📂 Files Included

- `app.py`: Flask backend (routes, prediction logic, form handling)
- `model.py`: Script used to train the ML model and save artifacts
- `model.pkl`: Trained ML model
- `encoders.pkl`: Label encoders for categorical fields
- `Folder Structure`: Contain the sturcture of the folder
- `uci.csv`: Dataset used for training the model
- `templates/index.html`: Frontend UI with form and result display
- `requirements.txt`: Python dependency list

## 🧪 How to Run Locally

1. **Clone the Repository**

```bash
git clone https://github.com/umarsubhani369/Heart-Disease-Risk-Prediction.git
cd Heart-Disease-Risk-Prediction


Install Requirements
pip install -r requirements.txt

Run the Flask App
python app.py

