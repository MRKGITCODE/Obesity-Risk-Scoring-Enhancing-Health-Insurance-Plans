import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px



@st.cache_data
# function to load data
def load_data():
    obesity = pd.read_csv('ObesityDataSet.csv')
    obesity = obesity.drop_duplicates()
    obesity.duplicated().sum()

    obesity["Age"] = obesity['Age'].astype(int)
    obesity["FCVC"] = obesity['FCVC'].astype(int)
    obesity["NCP"] = obesity['NCP'].astype(int)
    obesity["CH2O"] = obesity['CH2O'].astype(int)
    obesity["TUE"] = obesity['TUE'].astype(int)
    obesity["FAF"] = obesity['FAF'].astype(int)
    
    obesity.rename(columns={'family_history_with_overweight': 'Family_history_with_overweight'}, inplace=True)
    return obesity
obesity = load_data()

def show_explore_page():
    st.title("Explore the data of obesity levels in people from the countries of Mexico, Peru and Colombia")

    st.write(""" ### Kaggle Obesity Dataset""")

    # Calculates the frequency of gender in the dataset.
    data = obesity["Gender"].value_counts()

    # setting figure
    fig, axs = plt.subplots(3, 1, figsize=(8, 18))

    # pie chart
    axs[0].pie(data, labels = data.index, autopct="%.1f%%", shadow = True, startangle = 90)
    axs[0].axis("equal")

    # gendered age distribution
    sns.histplot(data=obesity, x="Age", hue="Gender", ax=axs[1], kde=True, bins=20)
    axs[1].set_title("Mean Age Distribution")

    # average weight
    sns.barplot(data=obesity, x="Gender", y="Weight", ax=axs[2])
    axs[2].set_title("Average Weight by Gender")


    plt.tight_layout() 
    
    st.write("""#### Gendered Distribution""")

    st.pyplot(fig)




