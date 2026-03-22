import streamlit as st
import random

# Title
st.title("💖 Para el amor de mi vida, mi Pri bonita💖")

st.write("Haz clic para recibir un mensajito bonito 🥰")

# List of phrases
frases = [
    "Eres lo mejor que me ha pasado 💖",
    "Cada día contigo es mi favorito 🌹",
    "Tu sonrisa ilumina mi mundo ✨",
    "Contigo todo tiene sentido 💕",
    "Eres mi lugar favorito en el mundo 🌎",
    "Me encantas más de lo que las palabras pueden decir 😍",
    "Si volviera a nacer, te elegiría otra vez 💞",
    "Eres mi casualidad más bonita 💘",
    "Amarte es mi cosa favorita 💓"
]

# Button
if st.button("Dame amor 💌"):
    frase = random.choice(frases)
    st.success(frase)