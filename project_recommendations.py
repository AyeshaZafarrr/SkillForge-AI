import streamlit as st
from project_data import PROJECTS

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI Project Recommendations",
    page_icon="💡",
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

projects = PROJECTS.get(
    career,
    PROJECTS["Machine Learning Engineer"]
)

# ==========================================
# HEADER
# ==========================================

st.markdown(f"""
<div class="user-header">

<div class="badge">
💡 AI Project Hub
</div>

<h1 class="user-title">
Recommended Projects
</h1>

<h3 class="user-subtitle">
Welcome <b>{name}</b> 👋 <br>
Build these projects to become a successful <b>{career}</b>.
</h3>

</div>
""", unsafe_allow_html=True)

st.write("")
# ==========================================
# PROJECT STATS
# ==========================================

total_projects = len(projects)

completed = sum(
    st.session_state.get(f"project_{i}", False)
    for i in range(total_projects)
)

progress = completed / total_projects if total_projects else 0

st.session_state["project_progress"] = progress

st.markdown("## 📊 Your Project Progress")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Recommended Projects", total_projects)

with c2:
    st.metric("Completed", completed)

with c3:
    st.metric("Progress", f"{int(progress*100)}%")

st.progress(progress)

st.write("")

# ==========================================
# PROJECT CARDS
# ==========================================

st.markdown("## 🚀 AI Recommended Projects")

for i, project in enumerate(projects):

    with st.container(border=True):

        st.subheader(project["title"])

        st.write(project["description"])

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Difficulty",
                project["difficulty"]
            )

        with col2:
            st.metric(
                "Skills",
                len(project["skills"])
            )

        st.markdown(
            "**Skills you'll practice:**"
        )

        st.write(" • ".join(project["skills"]))

        b1, b2, b3 = st.columns(3)

        with b1:
            st.link_button(
                "💻 GitHub",
                project["github"],
                use_container_width=True
            )

        with b2:
            st.link_button(
                "📺 YouTube",
                project["youtube"],
                use_container_width=True
            )

        with b3:
            st.link_button(
                "📖 Documentation",
                project["docs"],
                use_container_width=True
            )

        st.checkbox(
            "✅ Mark Project as Completed",
            key=f"project_{i}"
        )

    st.write("")
    # ==========================================
# AI CAREER TIPS
# ==========================================

st.markdown("---")
st.markdown("## 💡 AI Recommendations")

tips = [
    "✅ Upload every completed project to GitHub.",
    "✅ Write a detailed README for each repository.",
    "✅ Deploy at least 2–3 projects online.",
    "✅ Share your projects on LinkedIn.",
    "✅ Keep improving your portfolio regularly.",
]

for tip in tips:
    st.success(tip)

# ==========================================
# ACHIEVEMENT MESSAGE
# ==========================================

if completed == total_projects and total_projects > 0:

    st.balloons()

    st.success("""
🎉 Congratulations!

You've completed every recommended project for your learning path.

You're building a strong portfolio that will significantly improve your job readiness.
""")

elif completed > 0:

    st.info(
        f"Great progress! You've completed {completed} of {total_projects} recommended projects."
    )

else:

    st.warning(
        "Start with your first project today. Consistency beats perfection!"
    )

# ==========================================
# NEXT STEP
# ==========================================

st.markdown("---")

st.markdown("## 📄 Ready for Resume Analysis?")

st.write("""
Now that you've explored your recommended projects, the next step is to improve your resume.

SkillForge AI will analyze your profile and provide:

- 📈 Resume Strength Score
- 🎯 Missing Skills
- 💼 Career Improvement Suggestions
- 📚 Recommended Certifications
- 🌐 LinkedIn & GitHub Tips
- 🚀 Personalized Career Advice
""")

st.write("")

if st.button(
    "➡ Continue to Resume Suggestions",
    use_container_width=True
):
    st.switch_page("pages/resume_suggestions.py")

# ==========================================
# FOOTER
# ==========================================

st.write("")
st.write("")

st.markdown("""
---
<center>

<b>SkillForge AI</b><br>

AI-Powered Career Development Platform

</center>
""", unsafe_allow_html=True)