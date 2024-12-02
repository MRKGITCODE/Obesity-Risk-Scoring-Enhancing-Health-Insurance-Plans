# import libraries

import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# function to load model

def load_model():
    with open('model_and_encoders.pkl', 'rb') as f:
        data = pickle.load(f)
    return data


# function for prediction page

def show_predict_page():
    st.title("Obesity Prediction")
    
    st.write("""### We need some information to predict what scale you are on """)

# add select box for the features
# tuples with feature options
    # gendered =  ("Male", "Female")
    # family_history_with_overweight = ("yes", "no")
    # FAVC = ("yes", "no")
    # CAEC = ("Sometimes","Frequently","Always","no")
    # SMOKE = ("yes", "no")
    # SCC = ("yes", "no")
    # CALC = ("Sometimes","Frequently","Always","no")
    # MTRANS = ("Public Transportation", "Automobile", "Walking", "Motorbike", "Bike")

    Gender = st.selectbox("Gender", ("Male", "Female"))
    family_history_with_overweight = st.selectbox("Overweight Family History", ("yes", "no"))
    FAVC = st.selectbox("High Calorie Consumption", ("yes", "no"))
    CAEC = st.selectbox("Food Between Meals", ("Sometimes","Frequently","Always","no"))
    SMOKE = st.selectbox("Smokes", ("yes", "no"))
    SCC = st.selectbox("Monitors Calories", ("yes", "no"))
    CALC = st.selectbox("Alcohol Consumption", ("Sometimes","Frequently","Always","no"))
    MTRANS = st.selectbox("Transportation", ("Public Transportation", "Automobile", "Walking", "Motorbike", "Bike"))

# sliders
    age = st.slider("Age", 0, 128, 20) 
    height = st.slider("Height", 1, 60, 20)
    Weight = st.slider("Weight", 1, 60, 20)
    FCVC = st.slider("Vegetable Consumption Frequency", 0, 3, 1)
    NCP = st.slider("No. of Main Meals", 0, 4, 1)
    CH2O = st.slider("Water Daily", 0, 3, 1)
    FAF = st.slider("Physical Activity Frequency", 0, 3, 1)
    TUE = st.slider("Time Using Technology", 0, 24, 1)

# add prediction button
    OK = st.button("Predict")
    if OK:

# execute
        data = load_model()

# access diferrent keys
        model = data["model"]
        label_encoder = data["label_encoders"]

        new_data = np.array([[Gender, age, height, Weight, family_history_with_overweight, FAVC, FCVC, NCP, CAEC, SMOKE, CH2O, SCC, 
                      FAF, TUE, CALC, MTRANS]])
        new_df = pd.DataFrame(new_data, columns=['Gender', 'Age', 'Height', 'Weight', 'family_history_with_overweight', 
                                         'FAVC', 'FCVC', 'NCP', 'CAEC', 'SMOKE', 'CH2O', 'SCC', 'FAF', 
                                         'TUE', 'CALC', 'MTRANS'])

        categorical_cols = new_df.select_dtypes(include=["object"]).columns.tolist()
        target = "NObeyesdad"
        if target in categorical_cols:
            categorical_cols.remove(target)

        label_encoders = {}
        for col in categorical_cols:
            label_encoders[col] = LabelEncoder()
            new_df[col] = label_encoders[col].fit_transform(new_df[col])


        obesity = model.predict(new_df)

        st.subheader(f"Your estimated status is {obesity[0]}")



