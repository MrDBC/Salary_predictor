import streamlit as st
import pickle
import numpy as np 

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
regressor = data["model"]
le_country= data['le_country']
le_education = data['le_education']


def show_predict_page():
    st.title("Software Developer Salary Predictor")

    st.write("""### Provide some info. to predict salary""")

    countries = (
        "India",
        "United States of America",
        "Germany",
        "United Kingdom of Great Britain and Northern Ireland",
        'Canada',
        "France",
        'Brazil',
        'Spain',
        'Netherlands',
        'Australia',
        'Italy',
        'Poland',
        'Sweden',
        'Russian Federation',
        'Switzerland',
    )

    education =(
        'Master’s degree', 
        'Bachelor’s degree', 
        'Less than a Bachelors',
        'Post grad',
    )

    country = st.selectbox("Country", countries)
    education = st.selectbox("Level of Education", education)
    experience = st.slider("Years Of Experience", 0, 50, 3)

    clicked = st.button("Predict Salary")
    if clicked:
        X= np.array( [[country, education, experience]])
        X[:, 0]= le_country.transform(X[:, 0])
        X[:, 1]= le_education.transform([X[: , 1]])
        X= X.astype(float)
    
        salary = regressor.predict(X)
        st.subheader(f"Estimated salary = ${salary[0]: .2f}")

    