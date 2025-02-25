import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Welcome to this app")

# Upload Of file
uploaded_file = st.file_uploader("Choose a CSV file", type=["CSV", "xlsx"])

if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):    #File is csv
        df= pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"): #File is in excel
        df =pd.read_excel(uploaded_file)
    else:
        st.write("Unwanted File")


        # Preview the Data
    st.subheader("Data Preview")
    st.write(df.head())

        # Data Summary
    st.subheader("Data Summary")
    st.write(df.describe())

        # Filter The Data
    st.subheader("Filter Data")
    coloumns = df.columns.to_list()
    selected_coloumn = st.selectbox("Select column to filter by", coloumns)
    unique_values = df[selected_coloumn].unique()
    selected_values= st.selectbox("Select Value", unique_values)

    filtered_df = df[df[selected_coloumn] == selected_values]
    st.write(filtered_df)


else:
    st.write("Please upload the file....") 