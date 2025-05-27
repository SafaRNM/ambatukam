import streamlit as st

st.title("safahub")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.image("a463cdb2-d067-4550-848b-1c11fae6455d.jpeg", width=250)

st.title("Aplikasi Sederhana")
st.header("Aplikasi Nilai Genap/Ganjil")
angka = st.number_input("Tulis Sebuah Angka:", value=0, step=1)

if (angka % 2) ==0:
    st.write(f"{angka} adalah Bilangan Genap")
else: 
    st.write(f"{angka} adalah Bilangan Ganjil
