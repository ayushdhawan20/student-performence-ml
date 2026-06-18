import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

data = pd.read_csv("data.csv")

X = data[["attendance", "study_hours", "marks"]]
y = data["result"]

model = DecisionTreeClassifier()

model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("Model Trained Successfully!")