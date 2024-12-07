import streamlit as st
import matplotlib.pyplot as plt

from predict_page import show_predict_page
from explore_page import show_explore_page
import pickle

model = pickle.load(open('obesity.pkl', 'rb'), encoding='latin1')

def run():
    st.title("Obesity Classification using Machine Learning")

    ## Age
    age = st.number_input('Enter Age')

    
    ## For Gender
    gen_display = ('Female','Male', 'Others')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("Gender",gen_options, format_func=lambda x: gen_display[x])

     ## Height in Cms
    height = st.number_input('Enter Height in Cms', value=0)

    ## Weight in Kilograms
    weight = st.number_input("Enter Weight in Kilograms",value=0)

    ## BMI
    bmi= st.number_input("BMI",value=0)

    ##Physical Activity Level
    phy_level = ('1', '2', '3', '4')
    phy_options = list(range(len(phy_level)))
    phy = st.selectbox("Physical Activity Level",phy_options, format_func=lambda x: phy_level[x])


    if st.button("Submit"):
        features = [[age, gen, height, weight,bmi,phy]]
        print(features)
        prediction = model.predict(features)
        weight = [str(i) for i in prediction]
        ans = ', '.join(weight)
        if ans == 0:
            st.error("Error in the Inputs: Please Try Again")

        else:
            st.success("The predicted Category is:"+" "+ans)
            

run()
