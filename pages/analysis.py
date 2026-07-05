import streamlit as st
import time

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="AI Analysis",
    page_icon="🤖",
    layout="wide"
)

# ==========================
# LOAD CSS
# ==========================

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# Hide Streamlit

st.markdown("""
<style>
#MainMenu{visibility:hidden;}
header{visibility:hidden;}
footer{visibility:hidden;}
</style>
""", unsafe_allow_html=True)

# ==========================
# HEADER
# ==========================

st.markdown("""
<div class="user-header">

<div class="badge">
🤖 Step 4 of 4
</div>

<h1 class="user-title">
AI Career Analysis
</h1>

<h3 class="user-subtitle">
Analyzing your complete profile...
</h3>

</div>
""", unsafe_allow_html=True)

st.write("")

progress = st.progress(0)

status = st.empty()

steps = [
    "👤 Reading Personal Information...",
    "🎓 Checking Education...",
    "📄 Analyzing Resume...",
    "🧠 Evaluating Skills...",
    "🎯 Matching Dream Career...",
    "📊 Calculating Career Readiness...",
    "🚀 Preparing Recommendations...",
    "✅ Analysis Completed!"
]

for i, step in enumerate(steps):

    status.info(step)

    progress.progress((i + 1) * 100 // len(steps))

    time.sleep(0.8)

st.success("Your AI Career Report is Ready!")

st.write("")

if st.button(
    "📊 View Dashboard",
    use_container_width=True
):
    st.switch_page("pages/dashboard.py")