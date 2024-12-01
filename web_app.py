import numpy as np
import pickle
import streamlit as st


load_mod = pickle.load(open('tranied_model.sav', 'rb'))

def load_model(input):
    
    input_arr = np.asarray(input)
    input_resize = input_arr.reshape(1,-1)
    classifier_input = load_mod.predict(input_resize)
    if classifier_input[0] == 1:
        return "This perosn have Diabetic..."
    else:
        return "This person have'nt Diabetic..."


def main():
    
    
    st.title("Daiabets Prediction System Web App") 
    
    
    Pregnancies = st.text_input("Pregnancies: ")
    Glucose = st.text_input("Glucose: ")
    BloodPressure = st.text_input("BloodPressure: ")
    SkinThickness = st.text_input("SkinThickness: ")
    Insulin = st.text_input("Insulin: ")
    BMI = st.text_input("BMI: ")
    DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction: ")
    Age = st.text_input("Age: ")
    
    daignosis = ''
    
    input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
    
    if st.button("Daibetes result"):
        daignosis = load_model(input)
        st.success(daignosis)
    

if __name__ == '__main__':
    main()
    

