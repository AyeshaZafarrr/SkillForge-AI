import streamlit as st
import time

st.markdown("""
<style>

/* ===== GLOBAL BACKGROUND ===== */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

/* ===== REMOVE STREAMLIT HEADER ===== */
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}

/* ===== PAGE TITLE FIX ===== */
h1, h2, h3 {
    color: white !important;
}

/* ===== INPUT BOX STYLE ===== */
input, textarea {
    background-color: #111827 !important;
    color: white !important;
    border-radius: 10px !important;
}

/* ===== SELECTBOX ===== */
div[data-baseweb="select"] {
    background-color: #111827 !important;
    color: white !important;
}

/* ===== BUTTON STYLE ===== */
.stButton>button {
    background: linear-gradient(90deg, #6366f1, #3b82f6);
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.05);
}

/* ===== CARD STYLE ===== */
.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
    backdrop-filter: blur(10px);
}

/* ===== ANIMATION TEXT ===== */
.glow-text {
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    color: #60a5fa;
    animation: glow 2s infinite alternate;
}

@keyframes glow {
    from {text-shadow: 0 0 5px #60a5fa;}
    to {text-shadow: 0 0 20px #3b82f6;}
}

</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="About SkillForge AI",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>

.main {
    background: radial-gradient(circle, #0f172a, #1e293b);
}

/* Center card */
.about-box {
    background: rgba(255,255,255,0.05);
    padding: 40px;
    border-radius: 20px;
    text-align: center;
    color: white;
    box-shadow: 0px 0px 25px rgba(0,0,0,0.3);
}

/* Animated text */
.glow-text {
    font-size: 32px;
    font-weight: 800;
    color: #60a5fa;
    animation: glow 2s infinite alternate;
}

@keyframes glow {
    from { text-shadow: 0 0 10px #3b82f6; }
    to { text-shadow: 0 0 25px #60a5fa; }
}

/* Footer animation */
.footer-text {
    margin-top: 30px;
    font-size: 18px;
    opacity: 0;
    animation: fadeIn 3s forwards;
}

@keyframes fadeIn {
    to { opacity: 1; }
}

/* Floating developer text */
.dev {
    font-size: 20px;
    color: #a78bfa;
    font-weight: bold;
    animation: float 3s infinite ease-in-out;
}

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>About SkillForge AI</h1>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown("""
### 🚀 About SkillForge AI

SkillForge AI is your intelligent career companion that helps you:

- 🎯 Build in-demand skills  
- 📊 Track career progress  
- 📄 Improve your resume  
- 🛣️ Generate learning roadmaps  
- 💼 Become job-ready faster  

""")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown("""
### 💡 What makes it special?

- AI-powered scoring system  
- Personalized recommendations  
- Real-world career mapping  
- Project suggestions based on your level  
""")

st.markdown("</div>", unsafe_allow_html=True)

# ===== ANIMATED DEVELOPER SECTION =====
st.markdown("""
<div class="glow-text">
✨ Designed & Developed by Ayesha Zafar ✨
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; margin-top:20px; color:#94a3b8;'>
Thank you for using SkillForge AI ❤️
</div>
""", unsafe_allow_html=True)