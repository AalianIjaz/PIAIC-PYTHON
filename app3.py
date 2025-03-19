import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("Simple Data Dashboard")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Data Preview")
    st.write(df.head())
    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    column =df.columns.tolist()

    selected_column = st.selectbox("Select column to filter by", column)
    unique_values = df[selected_column].unique()
    selected_values = st.selectbox("Select value", unique_values)

    filtered_data = df[df[selected_column] == selected_values]
    st.write(filtered_data)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", column)
    y_column = st.selectbox("Select y-axis column", column)
  

    if st.button("Generate Plot"):
      st.line_chart(filtered_data.set_index(x_column)[y_column])

    else:
      st.write("Waiting on file upload...")

