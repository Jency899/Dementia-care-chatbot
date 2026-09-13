# app.py

import streamlit as st
from emotion_detector import detect_emotion
from memory_module import MemoryModule
from prompt_builder import build_prompt
from response_controller import clean_response
from model_handler import ModelHandler
from summarizer import DailySummarizer
from datetime import datetime

st.set_page_config(
    page_title="Dementia Care Assistant",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&family=Quicksand:wght@500;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stApp {
    background: linear-gradient(135deg, #e8f0fe 0%, #fce4ec 50%, #e8f5e9 100%);
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1a237e 0%, #283593 60%, #3949ab 100%) !important;
    box-shadow: 4px 0 20px rgba(26,35,126,0.3);
}
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] div,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] li,
[data-testid="stSidebar"] pre,
[data-testid="stSidebar"] code {
    color: white !important;
}
[data-testid="stSidebar"] .stButton > button {
    background: rgba(255,255,255,0.12) !important;
    color: white !important;
    border: 1px solid rgba(255,255,255,0.25) !important;
    border-radius: 12px !important;
    width: 100% !important;
    font-family: 'Nunito', sans-serif !important;
    font-weight: 600 !important;
    transition: all 0.3s !important;
    margin-bottom: 6px !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(255,255,255,0.25) !important;
    transform: translateX(4px) !important;
}
[data-testid="stSidebar"] .stMarkdown,
[data-testid="stSidebar"] .stMarkdown p,
[data-testid="stSidebar"] .element-container {
    color: white !important;
}

/* ── Text area in sidebar ── */
[data-testid="stSidebar"] textarea {
    background: white !important;
    color: #1b5e20 !important;
    border-radius: 10px !important;
    border: 2px solid #66bb6a !important;
    font-size: 0.82em !important;
    font-family: 'Nunito', sans-serif !important;
    line-height: 1.6 !important;
}
[data-testid="stSidebar"] .stTextArea label {
    color: white !important;
    font-weight: 600 !important;
}

/* ── Header ── */
.header-card {
    background: linear-gradient(135deg, #1a237e 0%, #7b1fa2 100%);
    border-radius: 20px;
    padding: 24px 32px;
    margin-bottom: 20px;
    box-shadow: 0 8px 32px rgba(26,35,126,0.25);
    color: white;
}
.header-title {
    font-family: 'Quicksand', sans-serif;
    font-size: 2em;
    font-weight: 700;
    margin: 0;
    color: white;
}
.header-sub {
    font-size: 0.95em;
    opacity: 0.8;
    margin-top: 4px;
    color: white;
}

/* ── Chat messages ── */
[data-testid="stChatMessage"] {
    background: white !important;
    border-radius: 16px !important;
    margin: 6px 0 !important;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06) !important;
    border: 1px solid #e8eaf6 !important;
    padding: 4px 8px !important;
}
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
    background: linear-gradient(135deg, #e8eaf6, #ede7f6) !important;
    border-color: #c5cae9 !important;
}

/* ── Chat input ── */
[data-testid="stChatInput"] textarea {
    border-radius: 14px !important;
    border: 2px solid #c5cae9 !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 1em !important;
    background: white !important;
    color: #1a237e !important;
}
[data-testid="stChatInput"] textarea:focus {
    border-color: #3949ab !important;
    box-shadow: 0 0 0 3px rgba(57,73,171,0.15) !important;
}

/* ── Sidebar info cards ── */
.info-card {
    background: rgba(255,255,255,0.12);
    border-radius: 14px;
    padding: 14px;
    margin-bottom: 14px;
    border: 1px solid rgba(255,255,255,0.2);
    text-align: center;
}
.info-card-title {
    font-size: 0.7em;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: rgba(255,255,255,0.6) !important;
    margin-bottom: 6px;
}
.info-card-value {
    font-size: 1.3em;
    font-weight: 800;
    color: white !important;
}

.stat-row {
    display: flex;
    gap: 10px;
    margin-bottom: 14px;
}
.stat-box {
    flex: 1;
    background: rgba(255,255,255,0.1);
    border-radius: 12px;
    padding: 12px 8px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.15);
}
.stat-num {
    font-size: 1.5em;
    font-weight: 800;
    color: white !important;
}
.stat-lbl {
    font-size: 0.65em;
    color: rgba(255,255,255,0.6) !important;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.section-label {
    font-size: 0.68em;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: rgba(255,255,255,0.5) !important;
    margin: 18px 0 10px 0;
    font-weight: 700;
}

/* ── Welcome box ── */
.welcome-box {
    text-align: center;
    padding: 40px 20px;
    background: white;
    border-radius: 20px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.06);
    border: 1px solid #e8eaf6;
    margin-bottom: 16px;
}
</style>
""", unsafe_allow_html=True)

# ─── Cache & Session ────────────────────────────────────────────
@st.cache_resource
def load_model():
    return ModelHandler()

if "memory" not in st.session_state:
    st.session_state.memory = MemoryModule()
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "summarizer" not in st.session_state:
    st.session_state.summarizer = DailySummarizer()
if "show_gen_summary" not in st.session_state:
    st.session_state.show_gen_summary = ""
if "show_last_summary" not in st.session_state:
    st.session_state.show_last_summary = ""

st.session_state.model = load_model()

# ─── Sidebar ───────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center;padding:16px 0 24px;">
        <div style="font-size:3em;">🧠</div>
        <div style="font-family:'Quicksand',sans-serif;font-size:1.1em;
                    font-weight:700;color:white;line-height:1.3;">
            Dementia Care<br>Assistant
        </div>
    </div>
    <hr style="border-color:rgba(255,255,255,0.15);margin-bottom:20px;">
    """, unsafe_allow_html=True)

    # Emotion display
    emotion_display = st.session_state.memory.get_last_emotion()
    emotion_emoji = {
        "lonely":  "😔", "confused": "😕", "sad":     "😢",
        "anxious": "😟", "happy":    "😊", "neutral": "😐",
        "general": "💬"
    }
    emoji = emotion_emoji.get(emotion_display, "💬")

    st.markdown(f"""
    <div class="info-card">
        <div class="info-card-title">Current Emotion</div>
        <div style="font-size:2.2em;margin:6px 0;">{emoji}</div>
        <div class="info-card-value">{emotion_display.capitalize()}</div>
    </div>
    """, unsafe_allow_html=True)

    # Stats row
    total = len(st.session_state.memory.get_full_history())
    now_time = datetime.now().strftime("%H:%M")
    st.markdown(f"""
    <div class="stat-row">
        <div class="stat-box">
            <div class="stat-num">{total}</div>
            <div class="stat-lbl">Messages</div>
        </div>
        <div class="stat-box">
            <div class="stat-num">{now_time}</div>
            <div class="stat-lbl">Time</div>
        </div>
    </div>
    <div class="section-label">🛠 Actions</div>
    """, unsafe_allow_html=True)

    # Buttons
    if st.button("📋 Generate Daily Summary"):
        history = st.session_state.memory.get_full_history()
        summary = st.session_state.summarizer.save_summary(history)
        st.session_state.show_gen_summary = summary
        st.session_state.show_last_summary = ""

    if st.session_state.show_gen_summary:
        st.text_area(
            "📋 Daily Summary",
            st.session_state.show_gen_summary,
            height=220
        )

    if st.button("📂 Load Last Summary"):
        summary = st.session_state.summarizer.load_latest_summary()
        st.session_state.show_last_summary = summary
        st.session_state.show_gen_summary = ""

    if st.session_state.show_last_summary:
        st.text_area(
            "📂 Last Summary",
            st.session_state.show_last_summary,
            height=220
        )

    if st.button("🗑️ Clear Conversation"):
        st.session_state.chat_history = []
        st.session_state.memory.clear()
        st.session_state.show_gen_summary = ""
        st.session_state.show_last_summary = ""
        st.rerun()

    st.markdown("""
    <div style="margin-top:30px;text-align:center;
                color:rgba(255,255,255,0.3);font-size:0.72em;">
        Powered by FLAN-T5 + Empathetic AI
    </div>
    """, unsafe_allow_html=True)

# ─── Header ─────────────────────────────────────────────────────
st.markdown("""
<div class="header-card">
    <div style="display:flex;align-items:center;gap:16px;">
        <div style="font-size:2.8em;">🧠</div>
        <div>
            <div class="header-title">Dementia Care Assistant</div>
            <div class="header-sub">
                A compassionate, emotion-aware companion — always here for you
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─── Welcome Screen ─────────────────────────────────────────────
if not st.session_state.chat_history:
    st.markdown("""
    <div class="welcome-box">
        <div style="font-size:3em;">💙</div>
        <div style="font-size:1.2em;font-weight:700;
                    color:#3949ab;margin-top:10px;">
            Hello! I'm here for you.
        </div>
        <div style="color:#9e9e9e;margin-top:8px;font-size:0.95em;">
            Feel free to share how you're feeling today.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ─── Chat History ───────────────────────────────────────────────
for message in st.session_state.chat_history:
    avatar = "🧑" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])
        if message.get("time"):
            st.caption(message["time"])

# ─── Chat Input ───
user_input = st.chat_input("💬 How are you feeling today?")

if user_input:
    now = datetime.now().strftime("%H:%M")

    with st.chat_message("user", avatar="🧑"):
        st.markdown(user_input)
        st.caption(now)

    st.session_state.chat_history.append({
        "role": "user",
        "content": user_input,
        "time": now
    })

    emotion        = detect_emotion(user_input)
    memory_context = st.session_state.memory.get_context_summary()
    prompt         = build_prompt(user_input, emotion, memory_context)
    raw_response   = st.session_state.model.generate(prompt, emotion)
    final_response = clean_response(raw_response, emotion, user_input)

    st.session_state.memory.update(user_input, emotion, final_response)

    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(final_response)
        st.caption(now)

    st.session_state.chat_history.append({
        "role": "assistant",
        "content": final_response,
        "time": now
    })

    st.rerun()