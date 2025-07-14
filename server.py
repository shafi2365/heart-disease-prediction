from flask import Flask, render_template, request
import numpy as np
import pickle
import mysql.connector

app = Flask(__name__)

# Load the model
model = pickle.load(open("model.pkl", "rb"))

# MySQL DB connection
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",       # 🔁 Replace this
    password="Ghazii7422",   # 🔁 Replace this
    database="heart_disease_db"
)
cursor = db.cursor()

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
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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




if __name__ == '__main__':
    app.run(debug=True)



# from flask import Flask, render_template, request
# import numpy as np
# import pickle

# app = Flask(__name__)


# model = pickle.load(open("model.pkl", "rb"))

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=["POST"])
# def predict():
#     try:
       
#         name = request.form["name"]
#         parentage = request.form["parentage"]
#         address = request.form["address"]
#         age = request.form["age"]

        
#         features = [
#             float(age),
#             float(request.form["sex"]),
#             float(request.form["cp"]),
#             float(request.form["trestbps"]),
#             float(request.form["chol"]),
#             float(request.form["fbs"]),
#             float(request.form["restecg"]),
#             float(request.form["thalach"]),
#             float(request.form["exang"]),
#             float(request.form["oldpeak"]),
#             float(request.form["slope"]),
#             float(request.form["ca"]),
#             float(request.form["thal"])
#         ]

#         final = np.array([features])
#         prediction = model.predict(final)
#         result = "Patient has Heart Disease" if prediction[0] == 1 else "Patient does NOT have Heart Disease"

        
#         return render_template(
#             "result.html",
#             prediction_text=result,
#             name=name,
#             parentage=parentage,
#             address=address,
#             age=age
#         )

#     except Exception as e:
#         return f"<h2>Error: {str(e)}</h2>"


# if __name__ == '__main__':
#     app.run(debug=True)




