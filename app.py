import streamlit as st
dcoderImg='https://raw.githubusercontent.com/raf-ar/raf-st/main/public/img/IMG_20220409_120731.jpg'
st.title("<raf /> Blog")
st.header("Cara Install Streamlit di Dcoder")
st.write("Untuk menginstall Streamlit di Dcoder langkah pertama yang harus dilakuakan adalah menginstall aplikasi Dcoder melalui Google Play Store")
st.image(dcoderImg)
link = '[Install Dcoder](https://play.google.com/store/apps/details?id=com.paprbit.dcoder)'
st.markdown(link, unsafe_allow_html=True)
