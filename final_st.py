import streamlit as st
import pickle
import pandas as pd
from streamlit_option_menu import option_menu
import numpy as np

# loading models
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))

# sidebar
with st.sidebar:
    selected_section = option_menu('Select a section', ['Home', 'Symptomate', 'Disease Prediction Models'], icons=['house-add-fill','person-plus-fill', 'grid-fill'], default_index=0)

# Main body of the app
if selected_section == 'Home':
    st.header("MedAssist")
    st.markdown("""MedAssist helps you predict the likelihood of having certain diseases based on your symptoms and risk factors.It contains two major models that provide accurate and reliable results:""")
    st.markdown("""### Symptomate:""")
    st.markdown("""Symptompate, a user-friendly application, is tailored for individuals seeking a quick and flexible assessment of their current medical diagnosis based on symptoms.""")
    st.markdown("""Symptompate is designed to assist users in getting an initial understanding of potential health issues based on the symptoms they report.""")
    st.markdown("""### Multi Disease Predictor:""")
    st.markdown("""The multiple disease predictor serves as a valuable tool for individuals who have previously visited a doctor and wish to monitor their current health condition and improvements.\n 
The models, designed specifically for predicting diabetes and heart disease, provide users with an assessment of their likelihood of having these conditions based on the entered details. \n
\n""")
    newStyle='<p><b>Diabetes Predictor</b></p><p><b>Heart Disease Predictor</b></p>'
    st.markdown(newStyle,unsafe_allow_html=True)

    
elif selected_section == 'Symptomate':
    with open("dummy.py","r") as f:
        exec(f.read())


elif selected_section == 'Disease Prediction Models':
    st.header("Disease Prediction Models")
    selected_model = option_menu('Select a specific model', ['Diabetes Prediction Model', 'Heart Disease Prediction Model'], icons=['activity', 'heart-fill'], default_index=0)

    if selected_model == 'Diabetes Prediction Model':
        st.title('Diabetes Prediction Model')
        c1,c2,c3=st.columns(3)
        with c1:
            Pregnancies = st.text_input("No of pregnancies")
        with c2:
            Glucose = st.text_input("Glucose level")
        with c3:
            BloodPressure = st.text_input("BP level (mm Hg)")
        with c1:
            SkinThickness = st.text_input("Skin thickness value (mm)")
        with c2:
            Insulin = st.text_input("Insulin level (mu U/ml)")
        with c3:
            BMI = st.text_input("BMI value")
        with c1:
            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        with c2:
            Age = st.text_input('Your age')

        # creating a button for prediction
        if st.button("Check"):
            st.markdown("## Result: :point_down:")
            diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            if diabetes_prediction[0]==1:
                st.error('Your test results are diabetic positive')
            else:
                st.success('Your test results are diabetic negative')
        st.subheader("Find more about the attributes")
        st.write("No. of pregnancies: Total number of times a person has been pregnant")
        st.write("Glucose level: Glucose levels refer to the concentration of glucose (sugar) in the blood and is measured in milligrams per deciliter (mg/dL)")
        st.write("BP level: Blood Pressure Level is measured millimeters of mercury (mmHg)")
        st.write("Skin thickness: Skin thickness ranges from 0.5 mm to 4 mm ")
        st.error("Enter the mean value to get approximate results if you don't know the skin thickness")
        st.write("Insulin level: Insulin level refers to the amount of insulin present in the blood typically measured in picomoles per liter (pmol/L) or microunits per milliliter (uU/mL) in most laboratories.")
        
        
    elif selected_model == 'Heart Disease Prediction Model':
        st.title('Heart Disease Prediction Model')
        c1,c2,c3=st.columns(3)
        with c1:
            Age = st.number_input("Your age",value=None)
        with c2:
            Sex = st.number_input("Your sex",value=None)
        with c3:
            CP = st.number_input("Chest Pain type",value=None)
        with c1:
            RestingBloodPressure = st.number_input("Resting Blood Pressure value",value=None)
        with c2:
            SerumCholestoral = st.number_input("Serum cholestoral (mg/dl)",value=None)
        with c3:
            FastingBloodSugar = st.number_input("Fasting Blood Sugar (mg/dl)",value=None)
        with c1:
            RER = st.number_input("Resting Electrocardiographic results ",value=None)
        with c2:
            MaxHeartRate = st.number_input("Maximum heart rate achieved",value=None)
        with c3:
            EIA = st.number_input("Exercise Induced Angina",value=None)
        with c1:
            OldPeak = st.number_input("ST depression induced by exercise",value=None)
        with c2:
            Slope = st.number_input("Slope of the peak exercise ST segment",value=None)
        with c3:
            CA = st.number_input("Major vessels colored by flourosopy",value=None)
        with c1:
            Thal = st.number_input("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect",value=None)
        

        # creating the prediction model
        if st.button("Check"):
            st.markdown("## Result: :point_down:")
            heart_disease_prediction = heart_disease_model.predict([[Age, Sex, CP, RestingBloodPressure, SerumCholestoral, FastingBloodSugar, RER, MaxHeartRate, EIA, OldPeak, Slope, CA, Thal]])
            if heart_disease_prediction[0]==1:
                st.error('You have Heart disease')
            else:
                st.success('You do not have Heart disease')
        st.subheader("Find more about the attributes")
        st.write("Resting Blood Pressure Value: Resting Blood Pressure (RBP) is a numerical value representing the blood pressure of an individual at rest. It is typically measured in millimeters of mercury (mmHg)")
        st.write("Serum Cholestrol: Serum cholesterol is a measurement of the amount of cholesterol in the blood and is usually measured in milligrams per deciliter (mg/dL) of blood")
        st.write("Fasting Blood Sugar: Fasting Blood Sugar (FBS) is the level of glucose in the blood after fasting for a certain period, typically 8 hours and is measured in milligrams per deciliter (mg/dL)")
        st.write("Resting Electrocardiographic Result: Resting electrocardiographic results (ECG or EKG) refer to the electrical activity of the heart recorded from electrodes placed on the skin")
        st.write("Maximum heart rate achieved-Maximum Heart Rate Achieved is the highest heart rate recorded during an activity. It is typically measured in beats per minute (bpm)")
        st.write("Exercise Induced Angina-Exercise: Induced angina is chest pain or discomfort that occurs when the heart muscle doesn't receive enough oxygen-rich blood during physical exertion.")
        st.write("ST depression induced by exercise: ST depression induced by exercise  diagnostic criterion for coronary artery disease, indicating inadequate blood flow to the heart during exercise.")
        st.write("Slope of the peak exercise ST segment: It is used as a diagnostic indicator for coronary artery disease, with different slope patterns indicating different degrees of myocardial ischemia.")
        st.write("Major vessels colored by fluoroscopy: Major vessels colored by fluoroscopy refers to a technique that uses X-rays to obtain real-time moving images of the internal structures of a patient.")