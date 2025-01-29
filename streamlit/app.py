import streamlit as st
import pandas as pd
import numpy as np


## Title of the app
st.title("Hello Streamlit")

## Display a simple text
st.write("This is a simple text")

## create a simple data frame
df = pd.DataFrame({
    'first Column':[1,2,3,5],
    'second column':[10,20,30,40]
})

## Display the dataframe
st.write("There is dataframe")
st.write(df)


## create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=['a', 'b', 'c']
)
st.line_chart(chart_data)