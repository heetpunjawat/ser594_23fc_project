# wf_ml_prediction.py
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("models/random_forest_model.joblib")

# Load the test data
X_test = pd.read_csv("data_processed/X_test.csv")

# Perform predictions
predictions = model.predict(X_test)

# Save predictions to data_processed folder
pd.DataFrame(predictions, columns=["Fatal Crashes", "Injury Crashes", "PDO Crashes"]).to_csv("data_processed/predictions.csv", index=False)

print("Predictions are generated.")

