import streamlit as st

st.title("Ini adalah aplikasi pertama")
st.header("programmer banyuwangi")

nama = st.text_input("Masukkan nama anda:")

if not nama:
    st.stop()

st.markdown(f"selamat datang <b> {nama}</b>", unsafe_allow_html=True)

agree = st.checkbox('I agree')

if agree:
    st.write('Great!')