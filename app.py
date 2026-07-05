import streamlit as st

st.set_page_config(
    page_title="SkillForge AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)



# =====================================================
# LOAD CSS
# =====================================================

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# =====================================================
# HIDE STREAMLIT DEFAULT ELEMENTS
# =====================================================

st.markdown("""
<style>
#MainMenu{visibility:hidden;}
header{visibility:hidden;}
footer{visibility:hidden;}
</style>
""", unsafe_allow_html=True)

# =====================================================
# HERO SECTION
# =====================================================

left, right = st.columns([1.45, 0.95], gap="large")

with left:

    st.markdown("""
    <div class="badge">
        🚀 Your AI Career Companion
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h1 class="hero-title">
        Build your AI Career <br>
        <span>Profile in Minutes</span>
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p class="hero-text">
        Get personalized skill analysis, career roadmaps,
        and AI-powered recommendations tailored specifically
        for your dream career.
    </p>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button(
        "🚀 Start Analysis",
        use_container_width=True
    ):
        st.switch_page("pages/userinfo.py")

with right:

    st.image(
        "assets/images/ai_robot.png",
        use_container_width=True
    )

# =====================================================
# SPACE
# =====================================================

st.write("")
st.write("")

# =====================================================
# FEATURE CARDS
# =====================================================

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="feature-card">
        <div class="icon">📊</div>
        <h4>Skill Analysis</h4>
        <p>
        Identify your strengths and discover
        missing skills instantly.
        </p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="feature-card">
        <div class="icon">🛣️</div>
        <h4>Career Roadmap</h4>
        <p>
        Receive a personalized learning roadmap
        based on AI recommendations.
        </p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="feature-card">
        <div class="icon">✨</div>
        <h4>AI Recommendations</h4>
        <p>
        Get projects, certifications,
        and career guidance instantly.
        </p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# SPACE
# =====================================================

st.write("")
st.write("")

# =====================================================
# STATS
# =====================================================

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">150+</div>
        <div class="metric-label">Skills Covered</div>
    </div>
    """, unsafe_allow_html=True)

with s2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">25+</div>
        <div class="metric-label">Career Paths</div>
    </div>
    """, unsafe_allow_html=True)

with s3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">500+</div>
        <div class="metric-label">Projects</div>
    </div>
    """, unsafe_allow_html=True)

with s4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">95%</div>
        <div class="metric-label">Accuracy</div>
    </div>
    """, unsafe_allow_html=True)


# FOOTER
# =====================================================

st.write("")
st.write("")

st.markdown("""
<hr>

<center>

<b>Designed & Developed by Ayesha Zafar</b><br><br>

Powered by Python • Streamlit • AI

</center>
""", unsafe_allow_html=True)