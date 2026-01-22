import streamlit as st
import random
import base64
import datetime

st.set_page_config(page_title="¿Quieres ser mi San Valentín? 💘", page_icon="🌹")

# --- CSS for floating flowers ---
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
</style>
""", unsafe_allow_html=True)

def play_music(file_path):
    with open(file_path, "rb") as f:
        audio_bytes = f.read()
    audio_base64 = base64.b64encode(audio_bytes).decode()
    audio_html = f"""
    <audio autoplay loop>
        <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
    </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

# --- Header / Question ---
st.markdown("## 🌹🌹 Hola Pri 🌹🌹")
st.markdown("### 👉 *Te quiero hacer una pregunta… pero con flores* 😌💐")
st.markdown("## 🌹🌹 ¿Quieres ser mi San Valentín? 🌹🌹")
st.markdown("🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹")
#st.audio("media/quieres.mp3", autoplay=True, loop=True)
# --- Session state ---
if "answered" not in st.session_state:
    st.session_state.answered = False

# 👉 ANSWER PLACEHOLDER (RIGHT AFTER QUESTION)
answer_area = st.empty()

# --- Buttons ---
if not st.session_state.answered:
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Sí 💖"):
            st.session_state.answered = True

    with col2:
        if st.button("No 😅"):
            frases = [
                "¿Segura? 🥺🌹",
                "Piénsalo con calma 😌",
                "Hay flores involucradas 💐",
                "Prometo plan bonito ✨",
                "Última oportunidad 😏"
            ]
            answer_area.warning(random.choice(frases))

# --- YES RESULT (shows under the question) ---
if st.session_state.answered:
    with answer_area.container():
        st.balloons()

        flores = ["🌹", "🌸", "💐", "🌺", "🌷", "💖", "💘", "❤️", "✨", "😍"]
        for i in range(25):
            st.markdown(
                f"<div class='flower' style='left:{random.randint(0,100)}%; animation-delay:{random.random()*3}s; font-size:{random.choice([28,30,34])}px'>{random.choice(flores)}</div>",
                unsafe_allow_html=True
            )
        play_music("media/quieres.mp3")
        st.success("💘 ¡¡Tenemos San Valentín!! 💘")
        st.markdown("### 🌹 Cita confirmada 🌹")
        st.markdown("Prometo plan bonito ✨, 😌💐")

        plan = st.radio(
        "¿Qué se te antoja más? 😌",
        ["Cenita 🍝", "Café bonito ☕", "Película 🎬", "Sorpresa 😏"])
        st.markdown(f"✨ Perfecto… tomo nota: **{plan}**")

        days = (datetime.date(2026, 2, 14) - datetime.date.today()).days
        st.markdown(f"⏳ Faltan **{days} días**")



st.markdown("""
> *Me gusta pasar tiempo contigo  
> y quería hacerlo especial* 💐
""")



