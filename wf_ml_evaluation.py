import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
import joblib

print("wf_ml_evaluation.py is running")

# Load processed data
data = pd.read_csv("data_processed/table1_processed.csv")

# Remove commas from numeric columns
numeric_columns = ["Total Crashes", "Fatal Crashes", "Injury Crashes", "PDO Crashes"]
data[numeric_columns] = data[numeric_columns].replace({",": ""}, regex=True).astype(int)

# Drop the "Total Crashes" column
data = data.drop(columns=["Total Crashes"])
# Exclude the last row
data = data.iloc[:-1, :]

# Features (X) and target column (y)
X = data.drop(columns=["Fatal Crashes", "Injury Crashes", "PDO Crashes"])
y = data[["Fatal Crashes", "Injury Crashes", "PDO Crashes"]]

x_train = X
y_train = y

# Split the data into training and test sets
X_train, x_test, Y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save training and test sets
x_train.to_csv("data_processed/X_train.csv", index=False)
x_test.to_csv("data_processed/X_test.csv", index=False)
y_train.to_csv("data_processed/y_train.csv", index=False)
y_test.to_csv("data_processed/y_test.csv", index=False)

print("Training and testing data generated in data_processed folder.")

# Run training.py
os.system("python3 wf_ml_training.py")
print("wf_ml_training.py is running")
# Run prediction.py
os.system("python3 wf_ml_prediction.py")
print("wf_ml_prediction.py is running")

# Load the true labels
y_test = pd.read_csv("data_processed/y_test.csv")

# Load predictions
predictions = pd.read_csv("data_processed/predictions.csv")

print("Computing Accuracy and F1-score metrics.")

# Compute accuracy and F1-score for each target column
accuracy = {}
f1 = {}

for column in y_test.columns:
    accuracy[column] = accuracy_score(y_test[column], predictions[column]) * 100  # Convert to percentage
    f1[column] = f1_score(y_test[column], predictions[column], average='weighted')   # Convert to percentage

# Compute average accuracy and F1-score
average_accuracy = sum(accuracy.values()) / len(accuracy)
average_f1 = sum(f1.values()) / len(f1)

# Create and write to summary.txt
with open("evaluation/summary.txt", "w") as file:
    file.write(f"\t\tRandom Forest Model\n")
    file.write(f"Average Accuracy: {average_accuracy:.2f}%\n")
    file.write(f"Average F1-score: {average_f1:.2f}\n")

print("Accuracy and F1-score generated and saved in summary.txt under evalution folder.")

# Construct alternative models for tuning
print("Constructing alternative models for tuning.")

# 1. Tuned Random Forest Model
print("1. Training Tuned Random Forest Model.")
param_grid = {
    'classifier__n_estimators': [50, 100, 200],
    'classifier__max_depth': [10, 20, 30],
}

pipeline = joblib.load("models/random_forest_model.joblib")
grid_search = GridSearchCV(pipeline, param_grid, cv=3, scoring='accuracy', n_jobs=-1)
grid_search.fit(x_train, y_train)

tuned_model = grid_search.best_estimator_
tuned_predictions = tuned_model.predict(x_test)

# Compute accuracy and F1-score for each target column separately
accuracy = {}
f1 = {}

for i, column in enumerate(y_test.columns):
    accuracy[column] = accuracy_score(y_test[column], tuned_predictions[:, i]) * 100  # Convert to percentage
    f1[column] = f1_score(y_test[column], tuned_predictions[:, i], average='weighted') * 100  # Convert to percentage

# Append results to summary.txt
with open("evaluation/summary.txt", "a") as file:
    file.write(f"\n\t\tAlternative Models\n")
    file.write(f"\n1. Tuned Random Forest Model Results:\n")
    for column in y_test.columns:
        file.write(f"{column} Accuracy: {accuracy[column]:.2f}%\n")
        file.write(f"{column} F1-score: {f1[column]:.2f}\n")

# # 2. Gradient Boosting Model
# print("Training Gradient Boosting Model.")
# gb_model = GradientBoostingClassifier(random_state=42)

# # You may need to preprocess the data differently for Gradient Boosting
# # For example, using one-hot encoding for categorical features
# X_train_gb = pd.get_dummies(X_train)
# x_test_gb = pd.get_dummies(x_test)

# gb_model.fit(X_train_gb, y_train)
# gb_predictions = gb_model.predict(x_test_gb)
# gb_accuracy = accuracy_score(y_test, gb_predictions) * 100
# gb_f1 = f1_score(y_test, gb_predictions, average='weighted') * 100

# with open("evaluation/summary.txt", "a") as file:
#     file.write(f"Gradient Boosting Model Accuracy: {gb_accuracy:.2f}%\n")
#     file.write(f"Gradient Boosting Model F1-score: {gb_f1:.2f}\n")

# # 3. Feature Subset Model
# print("Training Feature Subset Model.")
# feature_subset_model = joblib.load("models/random_forest_model.joblib")
# feature_subset_model.named_steps['preprocessor'].transformers.pop(1)  # Remove OneHotEncoder for feature subset

# # Ensure that you preprocess the data accordingly for the feature subset model
# X_train_subset = feature_subset_model.named_steps['preprocessor'].transform(X_train)
# x_test_subset = feature_subset_model.named_steps['preprocessor'].transform(x_test)

# feature_subset_model.named_steps['classifier'].max_features = 0.5  # Example: Use 50% of features
# feature_subset_model.fit(X_train_subset, y_train)

# feature_subset_predictions = feature_subset_model.predict(x_test_subset)
# feature_subset_accuracy = accuracy_score(y_test, feature_subset_predictions) * 100
# feature_subset_f1 = f1_score(y_test, feature_subset_predictions, average='weighted') * 100

# with open("evaluation/summary.txt", "a") as file:
#     file.write(f"Feature Subset Model Accuracy: {feature_subset_accuracy:.2f}%\n")
#     file.write(f"Feature Subset Model F1-score: {feature_subset_f1:.2f}\n")

# print("Alternative models constructed and results saved in summary.txt.")



