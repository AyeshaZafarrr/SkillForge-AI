import streamlit as st
from resume_data import RESUME_DATA

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Resume Suggestions",
    page_icon="📄",
    layout="wide"
)

# ==========================================
# LOAD CSS
# ==========================================

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ==========================================
# HIDE STREAMLIT
# ==========================================

st.markdown("""
<style>
#MainMenu{visibility:hidden;}
header{visibility:hidden;}
footer{visibility:hidden;}
</style>
""", unsafe_allow_html=True)

# ==========================================
# USER DATA
# ==========================================

name = st.session_state.get("name", "User")

career = st.session_state.get(
    "dream_career",
    "Machine Learning Engineer"
)

resume_info = RESUME_DATA.get(
    career,
    RESUME_DATA["Machine Learning Engineer"]
)

# ==========================================
# HEADER
# ==========================================

st.markdown(f"""
<div class="user-header">

<div class="badge">
📄 AI Resume Review
</div>

<h1 class="user-title">
Resume Suggestions
</h1>

<h3 class="user-subtitle">
Welcome <b>{name}</b> 👋<br>
Let's improve your resume for becoming a <b>{career}</b>.
</h3>

</div>
""", unsafe_allow_html=True)

st.write("")
# ==========================================
# RESUME SCORE
# ==========================================

st.markdown("## 📊 Resume Strength Score")

score = resume_info["resume_score"]

c1, c2 = st.columns([3, 1])

with c1:
    st.progress(score / 100)

with c2:
    st.metric("Score", f"{score}%")

if score >= 85:
    st.success("Excellent! Your resume is already strong.")
elif score >= 70:
    st.info("Good foundation. A few improvements can make it stand out.")
else:
    st.warning("Your resume needs improvement before applying to jobs.")

st.write("")

# ==========================================
# MISSING SKILLS
# ==========================================

st.markdown("## 🚀 Skills You Should Learn")

skills = resume_info["missing_skills"]

cols = st.columns(2)

for i, skill in enumerate(skills):
    with cols[i % 2]:
        st.warning(f"📌 {skill}")

st.write("")

# ==========================================
# RECOMMENDED CERTIFICATIONS
# ==========================================

st.markdown("## 🏆 Recommended Certifications")

for cert in resume_info["certifications"]:
    st.success(f"🎓 {cert}")

st.write("")
# ==========================================
# AI RESUME IMPROVEMENT TIPS
# ==========================================

st.markdown("## 📝 AI Resume Improvement Tips")

for tip in resume_info["resume_tips"]:
    st.info(f"✅ {tip}")

st.write("")

# ==========================================
# LINKEDIN TIPS
# ==========================================

st.markdown("## 💼 LinkedIn Profile Tips")

for tip in resume_info["linkedin"]:
    st.success(f"💡 {tip}")

st.write("")

# ==========================================
# GITHUB TIPS
# ==========================================

st.markdown("## 💻 GitHub Portfolio Tips")

for tip in resume_info["github"]:
    st.success(f"🚀 {tip}")

st.write("")

# ==========================================
# AI CAREER SUMMARY
# ==========================================

st.markdown("---")

st.markdown("## 🤖 AI Career Summary")

st.info(f"""
Based on your current profile, you're on a strong path toward becoming a **{career}**.

To maximize your chances of getting internships and job offers:

• Improve the missing technical skills.
• Complete the recommended certifications.
• Build and deploy portfolio projects.
• Keep your GitHub active.
• Optimize your LinkedIn profile.
• Update your resume after every major project.
""")

# ==========================================
# NEXT STEP
# ==========================================

st.write("")

if st.button(
    "📊 Generate Final AI Career Report",
    use_container_width=True
):
    st.switch_page("pages/report.py")

# ==========================================
# FOOTER
# ==========================================

st.write("")
st.write("")

st.markdown("""
---
<center>

### 🚀 SkillForge AI

Your Personalized AI Career Coach

Made with ❤️ using Streamlit & Python

</center>
""", unsafe_allow_html=True)