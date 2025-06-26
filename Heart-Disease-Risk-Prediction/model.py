# model.py
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# Load dataset
df = pd.read_csv('uci.csv')

# Encode categorical features
categorical_cols = ['sex', 'chest_pain_type', 'rest_ecg', 'thalassemia']
encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# Map to binary classification (0 = No risk, 1 = Risk)
df['target'] = df['target'].apply(lambda x: 0 if x == 0 else 1)

# Define features and target
X = df.drop(columns=['target'])
y = df['target']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# Train model with anti-overfitting params
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,                # limit depth to avoid overfitting
    min_samples_split=10,       # require more samples to split
    min_samples_leaf=5,         # more samples in leaf node
    max_features='sqrt',        # reduce number of features per split
    class_weight='balanced',    # handle imbalance
    random_state=42
)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Cross-validation score
cv_scores = cross_val_score(model, X, y, cv=5)
cv_mean = cv_scores.mean()

# Feature importance
importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)

# Print results
print("✅ Model Evaluation Summary (with overfitting control)")
print(f"Holdout Accuracy: {accuracy:.4f}")
print(f"Cross-validation Accuracy: {cv_mean:.4f}")
print("\nConfusion Matrix:")
print(conf_matrix)
print("\nClassification Report:")
print(report)
print("\nTop Important Features:")
print(importances)

# Save model and encoders
joblib.dump(model, 'model.pkl')
joblib.dump(encoders, 'encoders.pkl')
