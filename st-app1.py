import streamlit as st
import pandas as pd
st.title("This is My App")
spectra = st.file_uploader("upload file", type={"csv", "txt"})
#spectra_df = pd.read_csv(spectra)
#st.write(spectra_df)
