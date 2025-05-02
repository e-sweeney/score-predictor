from flask import Flask, request, render_template
import numpy as np
from joblib import load

app = Flask(__name__)
model = load("StudentScore.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    hours = float(request.form['hours'])
    prediction = model.predict(np.array([[hours]]))[0]
    return render_template('result.html', hours=hours, prediction=round(prediction, 2))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

