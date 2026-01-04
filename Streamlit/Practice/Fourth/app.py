import streamlit as st
import pickle
import numpy as np
import pandas as pd

st.title("ML Models Tutorial")

@st.cache_resource
def load_model():
    with open("D:/CODING_CODES/AIML/Streamlit/Practice/Fourth/model.pkl","rb") as f:
        model = pickle.load(f)
    return model

species = {0: "Setosa", 1: "Versicolor", 2:"Viginica"}

with st.form("input_data"):
    st.subheader("Iris Model Prediction")

    col1, col2 = st.columns(2)

    with col1:
        sepal_len = st.number_input("Sepal Length")
        sepal_wid = st.number_input("Sepal Width")

    with col2:
        petal_len = st.number_input("Petal Length")
        petal_wid = st.number_input("Petal Width")


    submit_btn = st.form_submit_button("Submit")

if submit_btn:

    if not sepal_len:
        st.error("Sepal Length mandatory!")
        st.stop()

    elif not sepal_wid:
        st.error("Sepal Width mandatory!")
        st.stop()

    elif not petal_len:
        st.error("Petal Length mandatory!")
        st.stop()

    elif not petal_wid:
        st.error("Petal Width mandatory!")
        st.stop()

    model = load_model()

    test_input = np.array([sepal_len, sepal_wid, petal_len, petal_wid])

    prediction_id = model.predict([test_input])[0]

    prediction_name = species[prediction_id]

    st.success(f"Prediction: {prediction_name}")



    




    