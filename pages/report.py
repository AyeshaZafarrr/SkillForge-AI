import streamlit as st
from resume_data import RESUME_DATA
from utils import calculate_overall_score
from pdf_generator import generate_pdf
# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Final AI Career Report",
    page_icon="📊",
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
email = st.session_state.get("email", "Not Provided")
career = st.session_state.get(
    "dream_career",
    "Machine Learning Engineer"
)

skills = st.session_state.get("skills", [])

resume = RESUME_DATA.get(
    career,
    RESUME_DATA["Machine Learning Engineer"]
)

resume_score = resume["resume_score"]
certifications = resume["certifications"]

# ==========================================
# AI SCORE
# ==========================================

resume_uploaded = "resume" in st.session_state

roadmap_progress = st.session_state.get(
    "roadmap_progress",
    0
)

project_progress = st.session_state.get(
    "project_progress",
    0
)

career_score, missing_skills = calculate_overall_score(
    skills,
    career,
    resume_uploaded,
    roadmap_progress,
    project_progress
)

# ==========================================
# HEADER
# ==========================================

st.markdown(f"""
<div class="user-header">

<div class="badge">
🏆 Final AI Career Report
</div>

<h1 class="user-title">
Congratulations, {name}! 🎉
</h1>

<h3 class="user-subtitle">
Your personalized AI career report is ready.
</h3>

</div>
""", unsafe_allow_html=True)

st.write("")
# ==========================================
# USER SUMMARY
# ==========================================

st.markdown("## 👤 User Summary")

c1, c2 = st.columns(2)

with c1:
    st.info(f"**👤 Name:** {name}")
    st.info(f"**📧 Email:** {email}")

with c2:
    st.info(f"**🎯 Dream Career:** {career}")
    st.info(f"**🧠 Current Skills:** {len(skills)}")

st.write("")

# ==========================================
# AI SCORES
# ==========================================
st.markdown("## 🧠 AI Verdict")

if career_score >= 85:

    st.success(
        "Excellent! Your profile is highly competitive for internships and entry-level jobs."
    )

elif career_score >= 70:

    st.info(
        "You're on the right track. Completing your roadmap and projects will significantly strengthen your profile."
    )

else:

    st.warning(
        "Focus on learning the missing skills, building projects, and improving your resume before applying."
    )
st.markdown("## 📊 AI Assessment")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Career Readiness",
        f"{career_score}%"
    )

with c2:
    st.metric(
        "Resume Score",
        f"{resume_score}%"
    )

with c3:
    st.metric(
        "Missing Skills",
        len(missing_skills)
    )

st.write("")

st.markdown("### 🎯 Career Readiness")

st.progress(career_score / 100)
st.write("")

st.markdown("### 📈 AI Performance Breakdown")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Resume Uploaded",
        "✅ Yes" if resume_uploaded else "❌ No"
    )

with c2:
    st.metric(
        "Roadmap Completion",
        f"{int(roadmap_progress*100)}%"
    )

with c3:
    st.metric(
        "Projects Completion",
        f"{int(project_progress*100)}%"
    )

st.success(
    f"Your overall AI Career Readiness is **{career_score}%**."
)

st.write("")


# ==========================================
# CURRENT SKILLS
# ==========================================

st.markdown("## 💪 Your Current Skills")

if skills:

    cols = st.columns(2)

    for i, skill in enumerate(skills):

        with cols[i % 2]:
            st.success(f"✅ {skill}")

else:

    st.warning("No skills found.")

st.write("")

# ==========================================
# MISSING SKILLS
# ==========================================

st.markdown("## 📌 Skills To Learn")

cols = st.columns(2)

for i, skill in enumerate(missing_skills):

    with cols[i % 2]:
        st.warning(f"📍 {skill}")

st.write("")

# ==========================================
# RECOMMENDED CERTIFICATIONS
# ==========================================

st.markdown("## 🎓 Recommended Certifications")

for cert in certifications:

    st.success(f"🏆 {cert}")

st.write("")
# ==========================================
# AI CAREER RECOMMENDATIONS
# ==========================================

st.markdown("## 🤖 AI Career Recommendations")
st.markdown("## ⭐ Overall AI Evaluation")

if career_score >= 90:

    st.success(
        "Outstanding! Your profile is close to industry-ready."
    )

elif career_score >= 75:

    st.info(
        "Very Good! Complete the remaining roadmap and projects."
    )

elif career_score >= 60:

    st.warning(
        "Good start. Continue improving your technical skills."
    )

else:

    st.error(
        "Your profile still needs significant improvement."
    )

recommendations = [
    "Build at least 5 real-world portfolio projects.",
    "Keep your GitHub repositories updated regularly.",
    "Optimize your LinkedIn profile with projects and certifications.",
    "Practice coding and technical interview questions weekly.",
    "Contribute to open-source projects whenever possible.",
    "Earn at least one industry-recognized certification.",
    "Continue learning consistently and stay updated with new technologies."
]

for rec in recommendations:
    st.success(f"✅ {rec}")

st.write("")

# ==========================================
# NEXT STEPS CHECKLIST
# ==========================================

st.markdown("## 🚀 Your Next Steps")

steps = [
    "Complete your Learning Roadmap",
    "Finish all recommended projects",
    "Improve your Resume",
    "Earn Certifications",
    "Update LinkedIn",
    "Update GitHub Portfolio",
    "Start applying for internships and jobs"
]

for step in steps:
    st.checkbox(step, key=f"step_{step}")

st.write("")

# ==========================================
# FINAL MESSAGE
# ==========================================

st.markdown("---")

st.success(f"""
# 🎉 Congratulations, {name}!

SkillForge AI has analyzed your profile and created a personalized career roadmap.

You now have:

✅ AI Career Assessment

✅ Personalized Learning Roadmap

✅ Recommended Projects

✅ Resume Suggestions

✅ Certification Recommendations

✅ Career Improvement Plan

Keep learning consistently, build projects, and showcase your work.
Every completed project brings you closer to becoming a successful **{career}**.
""")

# ==========================================
# DOWNLOAD REPORT (WORKING)
# ==========================================

st.markdown("## 📄 Download Report")

if st.button("📥 Generate PDF Report", use_container_width=True):

    pdf_buffer = generate_pdf(
        name=name,
        email=email,
        career=career,
        career_score=career_score,
        resume_score=resume_score,
        skills=skills,
        missing_skills=missing_skills,
        certifications=certifications
    )

    st.download_button(
        label="⬇ Download Your AI Report (PDF)",
        data=pdf_buffer,
        file_name="SkillForge_AI_Report.pdf",
        mime="application/pdf",
        use_container_width=True
    )

# ==========================================
# NAVIGATION
# ==========================================

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "🏠 Back to Dashboard",
        use_container_width=True
    ):
        st.switch_page("pages/dashboard.py")

with col2:

    if st.button(
        "🛣️ View Learning Roadmap",
        use_container_width=True
    ):
        st.switch_page("pages/roadmap.py")

# ==========================================
# FOOTER
# ==========================================

st.write("")
st.write("")

st.markdown("""
---
<center>

# 🚀 SkillForge AI

### Your Personalized AI Career Coach

Built with ❤️ using Python & Streamlit

© 2026 SkillForge AI

</center>
""", unsafe_allow_html=True)