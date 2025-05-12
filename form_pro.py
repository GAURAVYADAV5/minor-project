from flask_wtf import FlaskForm

from wtforms import(SelectField,IntegerField,SubmitField,FloatField)
from wtforms.validators import DataRequired,optional

import pandas as pd
data=pd.read_csv("heart.csv")

data=data.drop(columns=["Target"])


class PredictForm(FlaskForm):
    age=IntegerField(
        label="Age",
        validators=[DataRequired()]
    )    
    sex=SelectField(
        label="Sex",
        choices=["Male","Female"],
        validators=[DataRequired(),optional()]

    )
    chest_pain=SelectField(
        label="Chest_Pain",
        choices=data.Chest_Pain.unique().tolist(),
        validators=[DataRequired(),optional()]

    )
    resting_blood_pressur=IntegerField(
        label="Resting_Blood_Pressur",
        
        validators=[DataRequired()]

    )
    cholesterol=IntegerField(
        label="Cholesterol",
        
        validators=[DataRequired()]
    )
    fasting_blood_sugar=SelectField(
        label="Fasting_Blood_Sugar",
        choices=data.Fasting_Blood_Sugar.unique().tolist(),
        validators=[DataRequired(),optional()]

    )
    electrocardiographic_results=SelectField(
        label="Electrocardiographic_Results",

        choices=data.Electrocardiographic_Results.unique().tolist(),
        validators=[DataRequired(),optional()]

    )
    heart_rate=IntegerField(
        label="Heart_Rate",
        
        validators=[DataRequired()]
    )
    exercise_induced_angina=SelectField(
        label="Exercise_Induced_Angina",
        choices=data.Exercise_Induced_Angina.unique().tolist(),
        validators=[DataRequired(),optional()]

    )
    st_depression=FloatField(
        label="ST_Depression",
        
        validators=[DataRequired(),optional()]
    )
    slope=SelectField(
        label="Slope",
        choices=data.Slope.unique().tolist(),
        validators=[DataRequired(),optional()]

    )
    ca=SelectField(
        label="Coronary_Artery",
        choices=data.Ca.unique().tolist(),
        validators=[DataRequired(),optional()]

    )
    thal=SelectField(
        label="Thalassemia,",
        choices=data.Thal.unique().tolist(),
        validators=[DataRequired(),optional()]

    )        
    

    
    submit=SubmitField("Predict")