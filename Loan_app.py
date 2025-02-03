import streamlit as st
import numpy as np
import pickle


model = pickle.load(open("C:/Users/Mahesh/Downloads/Capstone project 2/new_trained_model.sav",'rb'))
                         
def loan_prediction(input_data):

    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]==0):
        return 'SOORY. You are not eligible for loan'
    else:
        return 'CONGRATULATIONS! You are eligible for loan'

def main():
    st.title("💰KNOW YOUR LOAN ELIGIBILITY")

    Gender = st.text_input("Select gender")
    Married = st.text_input("Married")
    Dependents = st.text_input("Dependents")
    Education = st.text_input("Education")
    Self_Employed = st.text_input("Self_Employed")
    Applicant_income = st.text_input("Enter Your Income ")
    Loan_amount = st.text_input("Enter Your Required Loan amount ")
    Loan_amount_Term = st.text_input("Enter Your Loan term in months ")
    Credit_History = st.text_input("Select Previous Credit_History if any")
    Property_Area = st.text_input("Property_Area")

    

    result=''


    if st.button('check loan status'):
        result=loan_prediction([Gender, Married, Dependents, Education, Self_Employed,
       Applicant_income,Loan_amount,Loan_amount_Term,Credit_History, Property_Area])
    
    st.success(result)
    


if __name__=='__main__':
    main()



