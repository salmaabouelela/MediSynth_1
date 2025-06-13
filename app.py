# app.py

import streamlit as st
import pandas as pd

# Load your sample data
df = pd.read_csv("your_sample_data.csv")

# Language selection
language = st.selectbox("Choose language", ["English", "Arabic", "Turkish", "French"])

# Mapping language to columns
lang_map = {
    "English": "Disease_EN",
    "Arabic": "Disease_AR",
    "Turkish": "Disease_TR",
    "French": "Disease_FR"
}

# Show data in selected language
st.write("## Synthetic Medical Data")
st.dataframe(df[[lang_map[language], "Region", "Gender", "Age"]])

# Simple visualization
st.write("## Age Distribution")
st.bar_chart(df["Age"])

# Download section
st.write("## Download Data")
st.download_button(
    label="Download CSV",
    data=df.to_csv(index=False).encode('utf-8'),
    file_name='synthetic_data.csv',
    mime='text/csv'
)
