import streamlit as st

x = st.number_input("masukkan angka")
sx = st.text_input(
    "masukkan satuan")
st.write("kamu punya", x, sx)
sy = st.selectbox(
    "piilih satuan",
    ("C", "F", "R", "K"))
y = 0
if(sx=="C"):
    if(sy=="C"):
        y = x
    elif(sy=="R"):
        y = 4*x/5
    elif(sy=="F"):
        y = (9*x/5) + 32
    elif(sy=="K"):
        y = x + 273

    
