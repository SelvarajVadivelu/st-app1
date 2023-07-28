import streamlit as st
import pandas as pd
import numpy as np
st.title("This is My App")
df = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)
spectra = st.file_uploader("upload file", type={"csv", "txt"})
spectra_df = pd.read_csv(spectra)
st.write(spectra_df)
