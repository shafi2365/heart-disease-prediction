from flask import Flask, render_template, request
import numpy as np
import pickle
import sqlite3

app = Flask(__name__)

# Load the model
model = pickle.load(open("model.pkl", "rb"))

# SQLite DB connection
db = sqlite3.connect('heart_disease.db', check_same_thread=False)
cursor = db.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    parentage TEXT,
    address TEXT,
    age INTEGER,
    sex INTEGER,
    cp INTEGER,
    trestbps INTEGER,
    chol INTEGER,
    fbs INTEGER,
    restecg INTEGER,
    thalach INTEGER,
    exang INTEGER,
    oldpeak REAL,
    slope INTEGER,
    ca INTEGER,
    thal INTEGER,
    result TEXT
)
""")
db.commit()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=["POST"])
def predict():
    try:
        # Personal info
        name = request.form["name"]
        parentage = request.form["parentage"]
        address = request.form["address"]
        age = request.form["age"]

        # Medical info
        sex = int(request.form["sex"])
        cp = int(request.form["cp"])
        trestbps = int(request.form["trestbps"])
        chol = int(request.form["chol"])
        fbs = int(request.form["fbs"])
        restecg = int(request.form["restecg"])
        thalach = int(request.form["thalach"])
        exang = int(request.form["exang"])
        oldpeak = float(request.form["oldpeak"])
        slope = int(request.form["slope"])
        ca = int(request.form["ca"])
        thal = int(request.form["thal"])

        features = [
            float(age), sex, cp, trestbps, chol, fbs,
            restecg, thalach, exang, oldpeak, slope, ca, thal
        ]

        final = np.array([features])
        prediction = model.predict(final)
        result = "Patient has Heart Disease" if prediction[0] == 1 else "Patient does NOT have Heart Disease"

        # Store into DB
        insert_query = """
            INSERT INTO predictions (
                name, parentage, address, age, sex, cp, trestbps, chol, fbs,
                restecg, thalach, exang, oldpeak, slope, ca, thal, result
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        values = (
            name, parentage, address, int(age), sex, cp, trestbps, chol, fbs,
            restecg, thalach, exang, oldpeak, slope, ca, thal, result
        )
        cursor.execute(insert_query, values)
        db.commit()

        return render_template(
            "result.html",
            prediction_text=result,
            name=name,
            parentage=parentage,
            address=address,
            age=age
        )

    except Exception as e:
        return f"<h2>Error: {str(e)}</h2>"
    
@app.route('/records')
def records():
    try:
        cursor.execute("SELECT * FROM predictions ORDER BY id DESC")
        rows = cursor.fetchall()
        return render_template('records.html', records=rows)
    except Exception as e:
        return f"<h2>Error fetching records: {str(e)}</h2>"


if __name__ == '__main__':
    app.run(debug=True)
