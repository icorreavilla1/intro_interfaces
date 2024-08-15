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
  st.subheader("Bienvenido")
  st.write("Pueden usar mis datos para fines investigativos")
  resp = st.checkbox("Estoy de acuerdo")
  if resp:
    st.write("Gracias! puedes continuar")

with col2:
  st.subheader("Cuentame, ¿Qué prefieres?")
  modo = st.radio("Escoge una de las opciones", ("Comida Mexicana", "Comida Italiana", "Comida Colombiana"))
  if modo == "Comida Mexicana":
    st.write("La vista es fundamental para tu interfaz")
  if modo == "Comida Italiana":
    st.write("La audicion es fundamental para tu interfaz")
  if modo == "Comida Colombiana":
    st.write("El tacto es fundamental")

st.subheader("Uso de botones")
if st.button ("Presiona el boton"):
  st.write("Gracias por precionar")
else:
  st.write("No has precionado aún")
  
