import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("Student_Performance.csv")
if df['extra_Curr'].dtype == 'O':
    df['extra_Curr'] = df['extra_Curr'].map({'Yes': 1, 'No': 0})

X = df[['hrs_Studied', 'prev_score', 'sleep', 'sample_practiced', 'extra_Curr']]
y = df['Result']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained inside the container!")
