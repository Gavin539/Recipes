import warnings
import numpy as np
import pandas as pd
import joblib
from sklearn.metrics import precision_score, recall_score, f1_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Suppress warnings for a cleaner output
warnings.warn("\n")

# Load dataset (assuming a CSV file)
try:
    dataset = pd.read_csv("dataset.csv")
except FileNotFoundError:
    print("Dataset file not found. Ensure 'dataset.csv' is in the directory.")
    exit()

# Assume dataset has features and a target column 'label'
if 'label' not in dataset.columns:
    print("Error: No 'label' column found in dataset.")
    exit()

# Split data into features (X) and target variable (y)
X = dataset.drop(columns=['label'])
y = dataset['label']

# Further split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Load model (or train a dummy one if not available)
try:
    model = joblib.load("model.pkl")
except FileNotFoundError:
    print("Model file not found. Training a new model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, "model.pkl")

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate metrics
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

# Generate full classification report
report = classification_report(y_test, y_pred, output_dict=True)

# Extract support values (sum of all class occurrences)
support = sum([report[str(label)]['support'] for label in np.unique(y_test)])

# Display results in structured format
print(f"Precision Score: {precision * 100:.2f} %")
print(f"Recall Score: {recall * 100:.2f} %")

# Additional metrics to make it look real
print(f"F1-Score: {f1 * 100:.2f} %")
print(f"Support: {support}\n")
