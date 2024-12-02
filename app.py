import streamlit as st
import matplotlib.pyplot as plt

from predict_page import show_predict_page
from explore_page import show_explore_page

# adding a sidebar
# save selection in variable
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", ["Predict", "Explore"])


    if page == "Predict":
        show_predict_page()
    else:
        show_explore_page()

        
if __name__ == "__main__":
    main()