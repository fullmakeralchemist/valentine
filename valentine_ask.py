import streamlit as st
import random

# --- STYLE (background + readability + design) ---
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffe6f0, #ffccdd);
        text-align: center;
        font-family: Arial, sans-serif;
    }

    h1 {
        color: #cc0066;
        font-size: 3.2em;
        font-weight: bold;
    }

    p {
        color: #333333;
        font-size: 1.5em;
        font-weight: 500;
    }

    .stButton>button {
        background-color: #ff4d88;
        color: white;
        border-radius: 12px;
        height: 3.2em;
        width: 220px;
        font-size: 1.2em;
        font-weight: bold;
    }

    .mensaje {
        font-size: 2em;
        color: #000000;
        font-weight: bold;
        margin-top: 20px;
    }

    .floating {
        position: fixed;
        bottom: -50px;
        font-size: 2rem;
        animation-name: floatUp;
        animation-timing-function: linear;
        animation-iteration-count: infinite;
        opacity: 0.8;
        pointer-events: none;
    }

    @keyframes floatUp {
        0% {
            transform: translateY(0);
            opacity: 0;
        }
        10% {
            opacity: 1;
        }
        100% {
            transform: translateY(-110vh);
            opacity: 0;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- TITLE ---
st.title("💖 Para el amor de mi vida, mi Pri bonita 💖")

st.write("Priscila, esto es solo para hacerte sonreír un poquito más cada día 🥰")

# --- PHRASES ---
frases = [
    "Eres lo mejor que me ha pasado 💖",
    "Cada día contigo es mi favorito 🌹",
    "Tu sonrisa ilumina mi mundo ✨",
    "Contigo todo tiene sentido 💕",
    "Eres mi lugar favorito en el mundo 🌎",
    "Me encantas más de lo que las palabras pueden decir 😍",
    "Si volviera a nacer, te elegiría otra vez 💞",
    "Eres mi casualidad más bonita 💘",
    "Amarte es mi cosa favorita 💓",
    "Eres mi paz en este mundo loco 💗",
    "No hay nadie como tú, Pri bonita 💕",
    "Contigo quiero todo 💖"
]

# --- SESSION STATE ---
if "frase" not in st.session_state:
    st.session_state.frase = "Haz clic en el botón para recibir amor 💌"

# --- BUTTON ---
if st.button("Dame amor 💌"):
    st.session_state.frase = random.choice(frases)

# --- SHOW MESSAGE (custom style instead of green box) ---
st.markdown(f"<div class='mensaje'>{st.session_state.frase}</div>", unsafe_allow_html=True)

# --- FLOATING EMOJIS ---
flores = ["🌹", "🌸", "💐", "🌺", "🌷", "💖", "💘", "❤️", "✨", "😍"]

floating_html = ""
for i in range(25):
    emoji = random.choice(flores)
    left = random.randint(0, 100)
    duration = random.randint(8, 15)
    delay = random.randint(0, 5)

    floating_html += f"""
    <div class="floating" style="
        left:{left}%;
        animation-duration:{duration}s;
        animation-delay:{delay}s;">
        {emoji}
    </div>
    """

st.markdown(floating_html, unsafe_allow_html=True)