import streamlit as st
from utils import calculate_overall_score

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="SkillForge AI Dashboard",
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

# Hide Streamlit UI

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
career = st.session_state.get("dream_career", "Not Selected")
skills = st.session_state.get("skills", [])

# ==========================================
# AI SCORE CALCULATION
# ==========================================

# Resume Uploaded?
resume_uploaded = "resume" in st.session_state

roadmap_progress = st.session_state.get(
    "roadmap_progress",
    0
)

project_progress = st.session_state.get(
    "project_progress",
    0
)

career_score, missing = calculate_overall_score(
    skills,
    career,
    resume_uploaded,
    roadmap_progress,
    project_progress
)

missing_skills = len(missing)

projects = 5

# ==========================================
# HEADER
# ==========================================

st.markdown(f"""
<div class="dashboard-header">

<div class="badge">
📊 AI Career Dashboard
</div>

<h1 class="dashboard-title">
Welcome, {name} 👋
</h1>

<p class="dashboard-subtitle">
Dream Career : <b>{career}</b>
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# ==========================================
# METRIC CARDS
# ==========================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Career Readiness", f"{career_score}%")

with c2:
    st.metric("Current Skills", len(skills))

with c3:
    st.metric("Missing Skills", missing_skills)

with c4:
    st.metric("Recommended Projects", projects)

st.write("")

# ==========================================
# READINESS SCORE
# ==========================================

st.subheader("🎯 Career Readiness Score")

st.progress(career_score / 100)

st.success(f"Your current career readiness is {career_score}%")
st.write("")

c1, c2 = st.columns(2)

with c1:

    st.subheader("🛣 Roadmap Progress")

    st.progress(roadmap_progress)

    st.caption(f"{int(roadmap_progress*100)}% Completed")

with c2:

    st.subheader("🚀 Project Progress")

    st.progress(project_progress)

    st.caption(f"{int(project_progress*100)}% Completed")

st.write("")

# ==========================================
# STRENGTHS & MISSING SKILLS
# ==========================================

left, right = st.columns(2)

with left:

    st.subheader("💪 Your Strengths")

    if skills:

        for skill in skills:
            st.success(f"✔ {skill}")

    else:

        st.info("No skills added.")

with right:

    st.subheader("📌 Skills to Learn")

    if missing:

        for item in missing:
            st.warning(item.title())

    else:

        st.success("🎉 No missing skills found!")

# ==========================================
# NEXT BUTTON
# ==========================================

if st.button(
    "🛣 Continue to Learning Roadmap",
    use_container_width=True
):
    st.switch_page("pages/roadmap.py")