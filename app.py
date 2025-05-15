import streamlit as st
import pandas as pd
import zipfile
import os

# --- Konfigurasi Halaman Streamlit (Opsional tapi bikin rapi) ---
# st.set_page_config(
#     page_title="Auto EDA & Data Cleaning App",
#     page_icon="📊", # Bisa ganti icon emoji sesuka lo!
#     layout="wide", # Ini biar layout halamannya pake lebar penuh
#     initial_sidebar_state="expanded" # Sidebar mau langsung kebuka atau nggak
# )

st.markdown(
    "<h1 style='text-align: center;'>Auto EDA App</h1>",
    unsafe_allow_html=True,
)
st.markdown("---")

# --- Component File Uploader ---
st.subheader("Upload Your Data File(s)")
st.info("Supports CSV, XLSX, and ZIP files containing CSV/XLSX.")

uploaded_file = st.file_uploader(
    "Drag and drop files here or click to browse",
    type=["csv", "xlsx", "zip"],
    accept_multiple_files=True,
)

# --- Logic after File uploaded ---
if uploaded_file:
    if len(uploaded_file) > 1:
        st.write(f"You have uploaded {len(uploaded_file)} files.")
        # TODO: Nanti di sini kita handle logic buat file ZIP atau banyak file CSV/XLSX
        st.warning(
            "Handling multiple files (including ZIP) is not fully implemented yet. Processing the first file for preview."
        )
        file_to_process = uploaded_file[0]
    else:
        file_to_process = uploaded_file[0]
        st.write(f"You have uploaded: **{file_to_process.name}**")

    # TODO: Di sini nanti logic buat baca file_to_process (CSV/XLSX) pake pandas
    # dan nampilin preview data, describe, missing values, dll (Task 2.3 - 2.9)

    st.success("File uploaded successfully! Ready for processing...")
else:
    st.info("Waiting for file upload...")
