from flask import Flask, render_template
from form_pro import PredictForm
import pandas as pd
import joblib

# Load trained model and transformer
model = joblib.load("model.joblib")
transforrmer = joblib.load("transformer.joblib")
ss= joblib.load("standardscaler.joblib")


app = Flask(__name__)
app.config["SECRET_KEY"] = "CIGAR"

@app.route("/")
def home():
    return render_template("home.html", title="Home")
@app.route("/information")
def information():
    return render_template("about.html",title="Information")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    form_pro = PredictForm()
    message = ""

    if form_pro.validate_on_submit():
        
        data = pd.DataFrame([{
            "Age": form_pro.age.data,
            "Sex": form_pro.sex.data,
            "Chest_Pain": form_pro.chest_pain.data,
            "Resting_Blood_Pressur": form_pro.resting_blood_pressur.data,
            "Cholesterol": form_pro.cholesterol.data,
            "Fasting_Blood_Sugar": form_pro.fasting_blood_sugar.data,
            "Electrocardiographic_Results": form_pro.electrocardiographic_results.data,
            "Heart_Rate": form_pro.heart_rate.data,
            "Exercise_Induced_Angina": form_pro.exercise_induced_angina.data,
            "ST_Depression": form_pro.st_depression.data,
            "Slope": form_pro.slope.data,
            "Ca": form_pro.ca.data,
            "Thal": form_pro.thal.data
            
        }])

        
        data_transformed = transforrmer.transform(data)
        data_scaler = ss.transform(data_transformed)

       
        predict = model.predict(data_scaler)
        message = f"Result_{predict[0]}"
    else:
        message = "Please Enter Valid Input"

    return render_template("mi_poj.html", title="Predict", form=form_pro, output=message)

if __name__ == "__main__":
    app.run(debug=True)
