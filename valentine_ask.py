import streamlit as st
import random

st.set_page_config(page_title="Lo Siento 💌", page_icon="💐")

# --- CSS for floating flowers and text styling ---
st.markdown("""
<style>
@keyframes float {
  0% {transform: translateY(100vh); opacity: 0;}
  50% {opacity: 1;}
  100% {transform: translateY(-10vh); opacity: 0;}
}
.flower {
  position: fixed;
  font-size: 30px;
  animation: float 6s linear infinite;
}
body {
  background: #fff0f5;
  color: #4b0082;
  font-family: 'Helvetica', sans-serif;
}
h2, h3 {
  text-align: center;
}
p {
  font-size: 18px;
  line-height: 1.6;
  text-align: center;
}
</style>
""", unsafe_allow_html=True)

# --- Floating flowers ---
#flores = ["🌹", "🌸", "💐", "🌺", "🌷", "💖", "💘", "❤️", "✨", "😍"]
flores = ["🌸", "🌿", "😔", "😓", "💧", "💔", "🍃", "🌷", "🌼"]
for i in range(25):
    st.markdown(
        f"<div class='flower' style='left:{random.randint(0,100)}%; animation-delay:{random.random()*3}s; font-size:{random.choice([28,30,34,36])}px'>{random.choice(flores)}</div>",
        unsafe_allow_html=True
    )

# --- Header / Apology ---
st.markdown("## 💌 Hola Pri 💌")
st.markdown("### Quiero hablar desde el corazón 😔💐")

# --- Apology Text ---
st.markdown("""
Querida Pri,  

Quiero sinceramente disculparme por mi comportamiento este fin de semana.  
Fui egoísta, intolerante y dejé que el miedo de perderte consumiera mis acciones y palabras.  
Sé que actué mal y que lo que dije estuvo muy mal; lamento haberte herido y hacerte sentir tan mal estos días.  
Tú mereces algo mejor.  

No quiero justificarme, pero sí quiero que sepas que mi miedo a perderte me cegó y me hizo actuar de una forma que no refleja quién realmente quiero ser.  

Sé que tal vez no pueda recuperar lo que tuvimos, pero quiero que sepas que estoy dispuesto a poner esfuerzo para cambiar y ser mejor.  
Aunque tú ya no estés conmigo, voy a buscar ser la mejor versión de mí mismo, la versión que siempre quise ser contigo.  
Deseo aprender de mis errores, crecer y demostrar con acciones que puedo ser alguien que merezca tu confianza y cariño, aunque ya no quieras estar en mi vida.  

No hay excusa para lastimarte con mi comportamiento, y lamento profundamente haber generado tristeza y frustración.  
Ojalá puedas sentir en estas palabras mi arrepentimiento y mi deseo sincero de enmendar lo que hice.  
Estos días he estado pensando en todo lo que vivimos juntos y en lo que quería vivir contigo, y sólo puedo sentir tristeza y arrepentimiento por haber perdido todo por no saber manejar mis emociones.  

Quisiera poder **volver al inicio**, entender lo que salió mal y arreglarlo, porque como dice la canción The Scientist de Coldplay, “nobody said it was easy” y me doy cuenta de que el tiempo y mis errores me han enseñado mucho.  
Quisiera **dar marcha atrás** y hacerlo todo bien, pero mientras tanto sigo aprendiendo y buscando ser mejor.  

Gracias por tomarte el tiempo de leer esto. Gracias por el tiempo que compartimos; nunca dejarás de ser el amor de mi vida ni dejaré de amarte.  
Espero que algún día pueda tener la oportunidad de que todo vuelva a ser como antes. Sé que estoy pidiendo mucho, pero la verdad es que no quiero vivir una vida sin ti. Mientras tanto, seguiré trabajando para ser la mejor versión de mí mismo.  

Con todo mi respeto, amor y cariño,  
Lalo 💖
""")