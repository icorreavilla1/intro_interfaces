import streamlit as st
from PIL import Image

st.title("MY FIRST APP")
st.header ("Hola, como va todo?")
st.write("Diferente tipo de letra")
image = Image.open("image1.jpeg")
st.image(image, caption="cool cool")

texto = st.text_input("Hola hola", "este es mi texto")
st.write("El texto escrito es: ", texto)
