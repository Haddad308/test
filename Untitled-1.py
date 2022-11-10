import streamlit as st 
import sklearn
import joblib

model = joblib.load("model.h5")
scalar = joblib.load("scalar.h5")

st.markdown(f"{model.predict(scalar.transform([[19,0,24,0,1,0,1,1,0]]))[0]}")