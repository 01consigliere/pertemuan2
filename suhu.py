import streamlit as st

x = st.number_input("masukkan angka")
sx = st.selectbox(
    "piilih satuan",
    ("C", "F", "R", "K"), key="sx")
st.write("kamu punya", x, sx)
sy = st.selectbox(
    "piilih satuan",
    ("C", "F", "R", "K"), key="sy")
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
if(sx=="F"):
    if(sy=="F"):
        y = x
    elif(sy=="C"):
        y = (x - 32)*5/9
    elif(sy=="R"):
        y = (x - 32)*4/9
    elif(sy=="K"):
        y = ((x - 32)*5/9) + 273
if(sx=="R"):
    if(sy=="R"):
        y = x
    elif(sy=="C"):
        y = (x)*5/4
    elif(sy=="F"):
        y = (x - 32)*9/4
    elif(sy=="K"):
        y = (x*5/4) + 273
if(sx=="K"):
    if(sy=="K"):
        y = x
    elif(sy=="R"):
        y = (x - 273)*4/5
    elif(sy=="F"):
        y = ((9/5)*(x-273))+32
    elif(sy=="C"):
        y = x - 273




st.write( x, " ", sx, "=", y, " ", sy)
