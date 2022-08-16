import streamlit as st 
from predict_page import show_predict_page
from explore_page import show_explore_page

options = st.sidebar.selectbox("Explore or Predict", {'Predict', 'Explore'})

if( options == "Predict"):
    show_predict_page()
else:
    show_explore_page()