import pandas as pd
import joblib
import streamlit as st

model=joblib.load('loan_data.pkl')

loan_id=st.number_input("Enter loan_id: ")
no_of_dependents=st.number_input("Enter number of dependents: ")
income_annum=st.number_input("What is you total annual income: ")
loan_amount=st.number_input("Enter loan amount: ")
loan_term=st.number_input("Enter loan duration: ")
cibil_score=st.number_input("")
residential_assets_value=st.number_input("Enter residential colateral value: ")
commercial_assets_value=st.number_input("Enter commercial assets value: ")
luxury_assets_value=st.number_input("Enter luxury assets value: ")
bank_asset_value=st.number_input("Enter bank asset value")

if st.button('submit'):
    dt=pd.DataFrame({
    'loan_id':[loan_id],
    'no_of_dependents':[no_of_dependents],
    'income_annum':[income_annum],
    'loan_amount':[loan_amount],
    'loan_term':[loan_term],
    'cibil_score':[cibil_score]
    'residential_assets_value':[residential_assets_value],
    'commercial_assets_value':[commercial_assets_value],
    'luxury_assets_value':[luxury_assets_value],
    'bank_asset_value':[bank_asset_value],
    })
    result=model.predict(dt)
    if result==1:
        st.success('Your loan request is approved')
    else:
        st.success('Sorry!, Your loan request is rejected')