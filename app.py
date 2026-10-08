from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model dan scaler
model = joblib.load("best_rf_model.joblib")
scaler = joblib.load("scaler.joblib")

# Mapping hari ke angka
day_mapping = {
    "Monday": 0, "Tuesday": 1, "Wednesday": 2,
    "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6
}

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            hour = int(request.form["hour"])
            day = day_mapping[request.form["day"]]
            car = int(request.form["car"])
            motor = int(request.form["motor"])
            truck = int(request.form["truck"])
            total = car + motor + truck

            input_data = np.array([[hour, day, car, motor, truck, total]])
            input_scaled = scaler.transform(input_data)
            result = model.predict(input_scaled)[0]

            label_map = {0: "Heavy", 1: "High", 2: "Low", 3: "Normal"}
            prediction = label_map[result]
        except Exception as e:
            prediction = f"Terjadi error: {e}"

    return render_template("index.html", prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
