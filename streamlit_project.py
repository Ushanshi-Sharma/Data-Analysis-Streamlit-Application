# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:10:42 2024

@author: 91903
"""

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title and Subheader
st.title("Data Analysis")
st.subheader("Data Analysis Project using Python and Streamlit")

# Upload the dataset
upload = st.file_uploader("Upload your data here in csv format")
if upload is not None:
    try:
        data = pd.read_csv(upload)
        if data.empty:
            st.error("The uploaded file is empty.")
        else:
            # View Dataset
            if st.checkbox("View Dataset"):
                if st.button("Head"):
                    st.write(data.head())
                if st.button("Tail"):
                    st.write(data.tail())

            # View DataTypes
            if st.checkbox("DataType of Each Column :"):
                st.text("DataTypes")
                st.write(data.dtypes)           

            # View Shape
            options = ["Select an option", "Rows", "Columns"]
            data_shape = st.radio("What Dimension do you want to check?", options, index=0, key="dimension_choice")
            if data_shape == "Rows":
                st.text("Number of Rows:")
                st.write(data.shape[0])
            elif data_shape == "Columns":
                st.text("Number of Columns:")
                st.write(data.shape[1])

            # Null Values
            check_nulls = st.selectbox("Do you want to check for null values?", ("Select One", "Yes", "No"))
            if check_nulls == "Yes":
                if data.isnull().values.any():
                    st.warning("This dataset contains null values.")
                    fig, ax = plt.subplots()
                    sns.heatmap(data.isnull(), ax=ax)
                    st.pyplot(fig)
                else:
                    st.success("There are no missing values in your dataset.")
            elif check_nulls == "No":
                st.info("Skipping null value check.")

            # Duplicate Values
            if data.duplicated().any():
                st.warning("This dataset contains duplicate values.")
                dup = st.selectbox("Do you want to remove duplicated values?", ("Select One", "Yes", "No"))
                if dup == "Yes":
                    data = data.drop_duplicates()
                    st.text("Duplicate values are now removed from your dataset.")
                elif dup == "No":
                    st.text("Okay, duplicate values remain in the dataset.")
                    
            # Getting Overall Statistics
            if st.checkbox("Statistical Summary of the dataset"):
                st.write(data.describe(include="all"))
                
            # About Section
            if st.button("About App"):
                st.text("Built with Streamlit")
                
            # By
            if st.checkbox("By"):
                st.success("Made by Ushanshi Sharma")
            
    except pd.errors.EmptyDataError:
        st.error("The uploaded file is empty or has no columns to parse.")
