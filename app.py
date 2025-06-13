import streamlit as st
import pandas as pd

# --- Page Config ---
st.set_page_config(
    page_title="MediSynth - Synthetic Medical Data Generator",
    layout="wide"
)

# --- App Header ---
st.markdown("<h1 style='text-align: center; color: teal;'>🧪 MediSynth</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Synthetic Medical Data Generator Prototype</h4>", unsafe_allow_html=True)
st.markdown("---")

# --- Language and Country Selection ---
language = st.selectbox("🌐 Choose language", ["English", "Arabic", "Turkish", "French"])
country = st.selectbox("🌍 Choose country", ["Turkey", "Egypt", "Lebanon", "Jordan"])

# --- Mapping language to file name ---
file_map = {
    "English": "diabetes_translated_english.csv",
    "Arabic": "diabetes_translated_arabic.csv",
    "Turkish": "diabetes_translated_turkish.csv",
    "French": "diabetes_translated_french.csv"
}

# --- Load the data file based on language ---
@st.cache_data
def load_data(file_name):
    return pd.read_csv(file_name)

try:
    df = load_data(file_map[language])
except FileNotFoundError:
    st.error(f"Could not find file: {file_map[language]}")
    st.stop()

# --- Display Data ---
st.subheader(f"📄 Synthetic Diabetes Data for {country} ({language})")
st.dataframe(df, use_container_width=True)

# --- Visualizations ---
st.subheader("📊 Visualizations")

if "Age" in df.columns:
    st.write("### Age Distribution")
    st.bar_chart(df["Age"])

if "Glucose" in df.columns:
    st.write("### Glucose Levels")
    st.line_chart(df["Glucose"])

if "BMI" in df.columns:
    st.write("### BMI Distribution")
    st.area_chart(df["BMI"])

if "Diabetes Outcome" in df.columns:
    st.write("### Diabetes Outcome (0 = No, 1 = Yes)")
    outcome_counts = df["Diabetes Outcome"].value_counts().sort_index()
    st.bar_chart(outcome_counts)

# --- Download Button ---
st.subheader("⬇️ Download Data")
st.download_button(
    label="Download CSV",
    data=df.to_csv(index=False).encode('utf-8'),
    file_name=f'synthetic_diabetes_data_{country}_{language}.csv',
    mime='text/csv'
)

# --- Footer with app name ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>MediSynth © 2025 - Synthetic Medical Data Generator</p>", unsafe_allow_html=True)
