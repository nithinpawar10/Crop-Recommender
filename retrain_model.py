import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load dataset
data = pd.read_csv("Crop_recommendation.csv")
X = data.drop("label", axis=1)
y = data["label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Decision Tree model
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train)

# Save model
with open("DecisionTree_model.pkl", "wb") as f:
    pickle.dump(dt_model, f)

print("✅ DecisionTree model retrained and saved successfully!")
