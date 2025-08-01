import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
data = pd.read_csv("Crop_recommendation.csv")
X = data.drop("label", axis=1)
y = data["label"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Decision Tree
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train)
with open("DecisionTree_model.pkl", "wb") as f:
    pickle.dump(dt_model, f)

# Random Forest
rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)
with open("RF_model.pkl", "wb") as f:
    pickle.dump(rf_model, f)

# Naive Bayes
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)
with open("NaiveBayes_model.pkl", "wb") as f:
    pickle.dump(nb_model, f)

# Logistic Regression (optional)
log_model = LogisticRegression(max_iter=200)
log_model.fit(X_train, y_train)
with open("LogReg_model.pkl", "wb") as f:
    pickle.dump(log_model, f)

print("✅ All models retrained and saved successfully!")
