import streamlit as st
import joblib
import numpy as np

model = joblib.load("heart_disease_model.pkl")

st.title("Heart Disease Prediction")

age = st.number_input("Age")
sex = st.selectbox("Sex", [0,1])
cp = st.selectbox("Chest Pain Type", [1,2,3,4])
trestbps = st.number_input("Resting Blood Pressure")
chol = st.number_input("Cholesterol")
fbs = st.selectbox("Fasting Blood Sugar > 120", [0,1])
restecg = st.selectbox("Rest ECG", [0,1,2])
thalach = st.number_input("Max Heart Rate Achieved")
exang = st.selectbox("Exercise Induced Angina", [0,1])
oldpeak = st.number_input("ST Depression")
slope = st.selectbox("Slope", [1,2,3])

if st.button("Predict"):

    input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
                            restecg, thalach, exang, oldpeak, slope]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("High Risk of Heart Disease")
    else:
        st.success("Low Risk of Heart Disease")