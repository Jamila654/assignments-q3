#type: ignore
import streamlit as st
import pandas as pd

def main():
    st.title("Data Sweeper 🧹")
    st.write("Upload a CSV file to clean your data!")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.subheader("Original Data")
        st.write(df)
        
        st.subheader("Cleaning Options")
        remove_missing_values = st.checkbox("Remove rows with missing values")
        remove_dupilicate_values = st.checkbox("Remove duplicate rows")
        
        cleaned_df = df.copy()
        if remove_missing_values:
            cleaned_df = cleaned_df.dropna()
            st.write(f"Removed {len(df) - len(cleaned_df)} rows with missing values.")
        if remove_dupilicate_values:
            initial_length = len(cleaned_df)
            cleaned_df = cleaned_df.drop_duplicates()
            st.write(f"Removed {initial_length - len(cleaned_df)} duplicate rows.")
            
        st.subheader("Cleaned Data")
        st.write(cleaned_df)
        csv = cleaned_df.to_csv(index=False)
        st.download_button(
            label="Download Cleaned Data",
            data=csv,
            file_name="cleaned_data.csv",
            mime="text/csv"
        )
        
main()