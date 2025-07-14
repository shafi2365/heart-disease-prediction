import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
import os

# Load dataset
df = pd.read_csv("C:/Users/emoli/Downloads/dieseas/heart_cleveland_upload.csv")  # Ensure this path is correct

# Separate features and label
X = df.drop('condition', axis=1)
y = df['condition']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save model to file
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained and saved to model.pkl")
