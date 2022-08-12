import streamlit as st
import pickle
from streamlit_option_menu import option_menu
import numpy as np

load_model = pickle.load(open('./data/model.pkl', 'rb')) 


select = st.sidebar.selectbox('Select a disease to predict', ['Diabetes', 'Random Forest', 'KNN', 'SVM', 'Naive Bayes'])
def diabetics_or_not(input_data):
    # input_data = [5,166,72,19,175,25.8,0.587,51]
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = load_model.predict(input_data_reshaped)
    print(prediction)
    if prediction[0] == 1:
        return 'They are suffering from diabetes'
    else:
        return 'Non-Diabetic'
    


def main():
    st.title('Diabetes Prediction')
    
    
    # get the data
    pregnancies = st.text_input('Pregnancies')
    glucose = st.text_input('Glucose')
    blood_pressure = st.text_input('Blood Pressure')
    skinthickness = st.text_input('Skin Thickness')
    insulin = st.text_input('Insulin')
    bmi = st.text_input('BMI')
    diabetiespedigifunction = st.text_input('Diabetes Pedigree Function')
    age = st.text_input('Age')
    
    
    
    # prediction
    diagnosis = ''
    if st.button("Diabetic Results"):
        diagnosis = diabetics_or_not([pregnancies, glucose, blood_pressure, skinthickness, insulin, bmi, diabetiespedigifunction, age])
        
    st.success(diagnosis)
    

if __name__ == '__main__':
    main()