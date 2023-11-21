import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# Load training data
X_train = pd.read_csv("data_processed/X_train.csv")
y_train = pd.read_csv("data_processed/y_train.csv")

# One-Hot Encoding for categorical column
categorical_features = ["First Harmful Event Type"]
numeric_features = X_train.columns.difference(categorical_features)

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

# Create a pipeline with preprocessing and the random forest classifier
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Train the model
pipeline.fit(X_train, y_train)

# Save the model
joblib.dump(pipeline, "models/random_forest_model.joblib")

print("Model is created and saved in models folder.")
