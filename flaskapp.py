import pickle
import pandas as pd
import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get form data
    age = float(request.form["xxxxxxxxxxxxx"])
    sex = 1 if request.form["xxxxxxxxxxxxxx"] == "male" else 0
    bmi = float(request.form["xxxxxxxxxxxxx"])
    children = int(request.form["xxxxxxxxxxxxxx"])
    smoker = 1 if request.form["xxxxxxxxxxxxxx"] == "no" else 0
    region = int(request.form["xxxxxxxxxxxxxxx"])

    # Prepare features for prediction
   
    feature_names = ["age", "sex", "bmi", "children", "smoker", "region"]
    features = pd.DataFrame([[age, sex, bmi, children, smoker, region]], columns=feature_names)

    # Predict charges
    prediction = model.predict(features)
    #  Format to float and 2 decimal places
    formatted_prediction = f"The predicted value is ${round(float(prediction), 2)}"


    return render_template("result.html", prediction=formatted_prediction)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

