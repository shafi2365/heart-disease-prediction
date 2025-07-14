# ❤️ Heart Disease Prediction Web App

This project is a **Flask-based web application** that predicts the likelihood of heart disease based on patient medical data. It uses a machine learning model (`model.pkl`) and stores patient details and prediction results in an SQLite database.

🔗 **GitHub Repository:** [https://github.com/shafi2365/heart-disease-prediction](https://github.com/shafi2365/heart-disease-prediction)

---

## 🚀 Features

✅ Predicts if a patient is likely to have heart disease.  
✅ Saves patient personal and medical details along with prediction results to a local SQLite database.  
✅ Displays all previous prediction records on a dedicated page.  
✅ Simple and user-friendly web interface built with HTML templates.

---

## 📂 Project Structure

```

heart-disease-prediction/
├── templates/
│   ├── index.html         # Home page with input form
│   ├── result.html        # Shows prediction result
│   └── records.html       # Displays saved records from the database
├── model.pkl              # Pre-trained ML model
├── heart\_disease.db       # SQLite database file (created automatically)
├── app.py                 # Flask application
└── README.md              # Project documentation

````

---

## ⚙️ How it works

1. User enters patient information and medical data on the home page.
2. The data is passed to the machine learning model to predict the likelihood of heart disease.
3. Results, along with the provided data, are saved in an SQLite database.
4. Users can view past predictions on the `/records` page.

---

## 📦 Installation & Running Locally

1. **Clone the repository**
```bash
git clone https://github.com/shafi2365/heart-disease-prediction.git
cd heart-disease-prediction
````

2. **Install required dependencies**

```bash
pip install -r requirements.txt
```

*(Create `requirements.txt` if not present, e.g.: Flask, numpy, pickle-mixin, etc.)*

3. **Run the app**

```bash
python app.py
```

4. Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧠 Model

The app uses a pre-trained machine learning model saved as `model.pkl`.
You can replace it with your own trained model if needed.

---

## 🗄️ Database

An SQLite database (`heart_disease.db`) stores:

* Patient personal info (name, parentage, address, age)
* Medical features (sex, cp, trestbps, chol, etc.)
* Prediction result

The table is automatically created when you run the app for the first time.

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

## ✏️ Author

**Mohammed Shafi Ganie**
GitHub: [@shafi2365](https://github.com/shafi2365)

---

## 🌟 Contributions

Contributions, issues, and feature requests are welcome!
Feel free to open an issue or submit a pull request.

