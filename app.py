# app.py

import streamlit as st
import pandas as pd
from sdv.tabular import GaussianCopula
import matplotlib.pyplot as plt

# Title
st.title("?? MediSynth - Synthetic Medical Data Platform")
st.markdown("Localized for **Turkey and the MENA Region**")

# Sidebar for language selection
language = st.sidebar.selectbox("?? Select Language", ["English", "Turkish", "Arabic", "French"])

# Language to filename mapping
file_map = {
    "English": "diabetes_translated_english.csv",
    "Turkish": "diabetes_translated_turkish.csv",
    "Arabic": "diabetes_translated_arabic.csv",
    "French": "diabetes_translated_french.csv"
}

# Load real data
real_df = pd.read_csv(file_map[language])

# Show real data
st.subheader("?? Real Sample Data")
st.dataframe(real_df)

# Generate synthetic data button
if st.button("?? Generate Synthetic Data"):
    with st.spinner("Generating synthetic data..."):
        # Load English version for modeling (non-translated column names)
        df_model = pd.read_csv("diabetes_translated_english.csv")

        # Fit the model
        model = GaussianCopula()
        model.fit(df_model)

        # Generate synthetic data
        synthetic_df = model.sample(300)

        # Use translated column names for the selected language
        synthetic_df.columns = real_df.columns

        st.success("Synthetic data generated!")

        # Show synthetic data
        st.subheader("?? Synthetic Data")
        st.dataframe(synthetic_df)

        # Visualization: Distribution of Diabetes Outcome (if available)
        if "Diabetes Outcome" in synthetic_df.columns:
            st.subheader("?? Diabetes Outcome Distribution")
            outcome_counts = synthetic_df["Diabetes Outcome"].value_counts()
            fig, ax = plt.subplots()
            outcome_counts.plot(kind='bar', ax=ax)
            ax.set_xlabel("Outcome")
            ax.set_ylabel("Count")
            st.pyplot(fig)

        # Download button
        st.download_button(
            label="?? Download Synthetic Data as CSV",
            data=synthetic_df.to_csv(index=False).encode('utf-8'),
            file_name="synthetic_data.csv",
            mime="text/csv"
        )
