# Making a basic streamlit web app 
import streamlit as st 
import pandas as pd 
import numpy as np  

# Title of the application 
st.title("Hello Streamlit") 

# Dislaying a simple text 
st.write("This is a simple text")  

# Creating a dataframe as: 
df = pd.DataFrame({
    'First Column': [1,2,3,4], 
    'Second Column': [10, 20, 30, 40]
}) 

# Display the dataframe 
st.write("Here is the dataframe") 
st.write(df)  

# Creating a line chart 
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns = ['a', 'b', 'c']
) 
st.line_chart(chart_data) 