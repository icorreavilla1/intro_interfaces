import streamlit as st
from PIL import Image

st.title("MY FIRST APP")
st.header ("Hola, como va todo?")
st.write("Diferente tipo de letra")
image = Image.open("image1.jpeg")
st.image(image, caption="cool cool")

texto = st.text_input("Hola hola", "este es mi texto")
st.write("El texto escrito es: ", texto)

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es mi primera columna")
  st.write("Las interfaces multimodales mejoran la experienci del usuario")
  resp = st.checkbox("Estoy de acuerdo")
  if resp:
    st.write("correctooo")

with col2:
  st.subheader("Esta es mi primera columna")
  modo = st.radio("Que modalidad es la principal en tu interfaz", ("Visual", "Auditiva", "Tactil"))
  if modo == "Visual":
    st.write("La vista es fundamental para tu interfaz")
  if modo == "Auditiva":
    st.write("La audicion es fundamental para tu interfaz")
  if modo == "Tactil":
    st.write("El tacto es fundamental")
