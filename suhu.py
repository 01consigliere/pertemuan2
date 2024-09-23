import streamlit as st

x = st.number_input("masukkan angka")
satuan = st.selectbox(
    "piilih satuan",
    ("C", "F", "R", "K"))
st.write("The current number is ", x, satuan)
