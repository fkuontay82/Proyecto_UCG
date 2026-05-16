import streamlit as st
import pandas as pd
import libreria.funciones as lf

st.title("Proyecto final UCG")
st.sidebar.title("Parámetros")
st.sidebar.image("Logo Python2.png")
uploaded_files = st.file_uploader(
    "Upload data", accept_multiple_files=True, type="csv"
)
for uploaded_file in uploaded_files:
    df = pd.read_csv(uploaded_file)
    st.write(df)
cuota = lf.cuota_prestamo(1000, 0.10,2,12)
st.write(cuota)
