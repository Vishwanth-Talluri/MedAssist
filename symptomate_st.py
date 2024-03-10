import streamlit as st
import pandas as pd
import numpy as np
import csv

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


data=pd.read_csv("Training_data.csv")
X = data.drop(columns='prognosis', axis=1)
Y = data['prognosis']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=42)
rf= RandomForestClassifier(random_state=42)
model = rf.fit(X_train,Y_train)
all_symptoms=list(X_train.columns)
input_d=[]
st.sidebar.write("Welcome to the website")
st.header("Symptomate")
status=0
with st.form("my_form"):
    input_d=st.multiselect("Select ths symptoms",all_symptoms)
    status=st.form_submit_button("Submit")

input_data= np.asarray(input_d)
input_data_reshaped = input_data.reshape(1,-1)
X_train_prediction = model.predict(X_train)
symptoms_dict = {symptom: 1 if symptom in input_data_reshaped else 0 for symptom in all_symptoms}
user_df = pd.DataFrame([symptoms_dict])
prediction = model.predict(user_df)
if(status and len(input_data)>=2):
    newStyle=(f'<h3>Your possible diagnosis is <span style="color:red;font-weight:600;">{prediction[0]}</span></h3>')
    st.markdown(newStyle,unsafe_allow_html=True)
    st.markdown('''The do's and dont's are as follows''')
    
    # Define the disease name to search for
    disease = prediction[0]

    # Open the csv file in read mode
    with open('DND2.csv', 'r') as file:
        # Create a csv reader object
        reader = csv.reader(file)
        # Loop through each row in the csv file
        
        for row in reader:
        # Check if the disease name matches the value in the first column
            if disease == row[0]:
                # Create two columns
                col1, col2 = st.columns(2)
                # Write the dos in the first column
                with col1:
                    st.subheader('Do\'s')
                    l = row[1].split('@')
                    for j in l:
                        st.write(j)
                # Write the donts in the second column
                with col2:
                    st.subheader('Don\'ts')
                    l = row[2].split('@')
                    for j in l:
                        st.write(j)
                # Break the loop
                break

            else:
                # Print or return a message indicating that the disease is not in the file
                print(f'{disease} is not in the file.')

    

  

    

elif(len(input_data)>0):
    st.markdown(f"""You probably are suffering from {prediction[0]}
""")
    newStyle=('<p style="color:green";>Enter other symptoms if any</p>')
    st.markdown(newStyle,unsafe_allow_html=True)