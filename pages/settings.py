import streamlit as st

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
    page_title="Settings",
    page_icon="⚙️",
    layout="wide"
)

# =========================
# CUSTOM STYLING (IMPORTANT FIX)
# =========================

st.markdown("""
<style>

/* Background */
.main {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

/* Title */
h1, h2, h3 {
    color: white !important;
}

/* Labels FIX (THIS is what was missing) */
[data-testid="stTextInput"] label,
[data-testid="stSelectbox"] label {
    color: #ffffff !important;
    font-weight: 600;
}

/* Input box styling */
input, textarea {
    background-color: #111827 !important;
    color: white !important;
    border-radius: 10px !important;
}

/* Button styling */
.stButton>button {
    background: linear-gradient(90deg, #6366f1, #3b82f6);
    color: white;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.05);
}

/* Card look */
.block-container {
    padding: 2rem;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SETTINGS UI
# =========================

st.markdown("<h1 style='text-align:center;'>⚙️ Settings</h1>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown("### 👤 Update Your Profile Settings")

name = st.text_input("Name")
email = st.text_input("Email")

career = st.selectbox(
    "Dream Career",
    [
        "Machine Learning Engineer",
        "AI Engineer",
        "Data Analyst",
        "Python Developer",
        "Backend Developer",
        "Cloud Engineer",
        "DevOps Engineer"
    ]
)

st.markdown("</div>", unsafe_allow_html=True)

if st.button("💾 Save Settings"):

    st.session_state["name"] = name
    st.session_state["email"] = email
    st.session_state["dream_career"] = career

    st.success("Settings saved successfully ✅")