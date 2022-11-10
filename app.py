import streamlit as st 
import sklearn
import joblib

model = joblib.load("model.h5")
scalar = joblib.load("scalar.h5")

st.markdown(f"ركز يا عبد الكرييييم ")