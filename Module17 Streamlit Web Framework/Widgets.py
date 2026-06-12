import streamlit as st 
import numpy as np 
import pandas as pd 

st.title("Streamlit Text Input") 

name = st.text_input("Enter your name: ") 


age = st.slider("Select your age:",0,100,25) 

options = ["Python", "Java", "C++", "Javascript"] 
choice = st.selectbox("Choose your favourite language: ", options) 
st.write(f"You selected {choice}") 



if name: 
    st.write(f"Hello, {name}")  

data = {
    "Name": ["John", "Jake", "Jane", "Jill"], 
    "Age": [28, 25, 34, 40], 
    "City": ["New York", "Los Angeles", "Chicago", "Houston"] 
} 

df = pd.DataFrame(data)  
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file = st.file_uploader("Chooose a CSV file", type = 'csv') 

if uploaded_file is not None: 
    df = pd.read_csv(uploaded_file) 
    st.write(df) 
