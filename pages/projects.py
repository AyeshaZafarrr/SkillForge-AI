import streamlit as st
from project_data import PROJECTS

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Projects",
    page_icon="🚀",
    layout="wide"
)

# =====================================================
# PREMIUM CSS
# =====================================================

st.markdown("""
<style>

/* Hide Streamlit */

#MainMenu{visibility:hidden;}
header{visibility:hidden;}
footer{visibility:hidden;}

/* Animated Background */

.stApp{

background:linear-gradient(
-45deg,
#0b1120,
#111827,
#1e1b4b,
#0f172a,
#111827
);

background-size:400% 400%;

animation:bg 15s ease infinite;

}

@keyframes bg{

0%{background-position:0% 50%;}

50%{background-position:100% 50%;}

100%{background-position:0% 50%;}

}

/* Fonts */

html,body,[class*="css"]{

color:white;

}

/* Hero Card */

.hero{

background:rgba(255,255,255,.05);

backdrop-filter:blur(18px);

border:1px solid rgba(99,102,241,.35);

padding:35px;

border-radius:22px;

box-shadow:0 0 30px rgba(99,102,241,.15);

animation:heroFloat 5s ease-in-out infinite;

margin-bottom:30px;

}

@keyframes heroFloat{

0%{transform:translateY(0px);}

50%{transform:translateY(-5px);}

100%{transform:translateY(0px);}

}

.hero h1{

font-size:42px;

font-weight:800;

margin-bottom:10px;

color:white;

}

.hero p{

font-size:18px;

color:#d1d5db;

}

/* Search */

.stTextInput input{

background:#172033;

color:white;

border-radius:15px;

border:1px solid #4f46e5;

height:50px;

}

.stTextInput input:focus{

border:1px solid #7c3aed;

box-shadow:0 0 12px #7c3aed;

}

/* Metrics */

[data-testid="stMetric"]{

background:#172033;

padding:18px;

border-radius:15px;

border:1px solid rgba(99,102,241,.25);

}

/* Divider */

hr{

border:1px solid rgba(255,255,255,.08);

}

/* Make Metric Text White */

[data-testid="stMetric"] label{
color:white !important;
}

[data-testid="stMetricValue"]{
color:white !important;
}

[data-testid="stMetricLabel"]{
color:white !important;
}

/* Markdown */

.stMarkdown{
color:white;
}


/* Project Titles */

h1,
h2,
h3,
h4,
h5,
h6{
    color:white !important;
}

/* Streamlit Subheaders */

[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3{
    color:white !important;
}

/* Search Box */

.stTextInput label{
    color:white !important;
    font-weight:600;
}

.stTextInput input{
    color:white !important;
    -webkit-text-fill-color:white !important;
    caret-color:white !important;
}

.stTextInput input::placeholder{
    color:#d1d5db !important;
    opacity:1;
}
</style>
""", unsafe_allow_html=True)




# =====================================================
# GET USER CAREER
# =====================================================

career = st.session_state.get(
    "dream_career",
    "Machine Learning Engineer"
)

projects = PROJECTS.get(career, [])

# =====================================================
# HERO SECTION
# =====================================================

st.markdown(f"""
<div class="hero">

<h1>🚀 {career} Projects</h1>

<p>
Build industry-level projects recommended by AI.
Complete these projects to strengthen your portfolio
and become job-ready.
</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# SEARCH
# =====================================================
search = st.text_input(
    "🔍 Search Projects",
    placeholder="Type a project name..."
)

if search:

    filtered = [
        p for p in projects
        if search.lower() in p["title"].lower()
    ]

    if filtered:
        projects = filtered
    else:
        st.error("❌ This project is currently not available in SkillForge AI.")
        st.stop()
# =====================================================
# PROJECT CARDS
# =====================================================
# =====================================================
# PROJECT CARDS
# =====================================================

for project in projects:

    st.markdown("""
    <style>

    .project-card{

        background:rgba(255,255,255,.05);

        border:1px solid rgba(124,58,237,.25);

        backdrop-filter:blur(15px);

        border-radius:22px;

        padding:28px;

        margin-bottom:25px;

        transition:.35s;

        box-shadow:0 0 25px rgba(124,58,237,.10);

    }

    .project-card:hover{

        transform:translateY(-6px);

        border:1px solid #8b5cf6;

        box-shadow:0 0 35px rgba(139,92,246,.35);

    }

    .badge{

        display:inline-block;

        padding:6px 14px;

        border-radius:30px;

        background:#7c3aed;

        color:white;

        font-size:13px;

        font-weight:700;

        margin-bottom:12px;

    }

    .skill{

        display:inline-block;

        background:#1e293b;

        color:#fff;

        padding:7px 14px;

        border-radius:30px;

        margin:4px;

        font-size:13px;

        border:1px solid rgba(255,255,255,.1);

    }

    </style>
    """, unsafe_allow_html=True)

    with st.container():

        st.markdown('<div class="project-card">', unsafe_allow_html=True)

        st.subheader(project["title"])

        st.write(project["description"])

        col1,col2=st.columns(2)

        with col1:

            difficulty=project["difficulty"]

            if difficulty=="Beginner":

                st.success("🟢 Beginner")

            elif difficulty=="Intermediate":

                st.warning("🟠 Intermediate")

            else:

                st.error("🔴 Advanced")

        with col2:

            st.markdown("### 🧠 Skills")

            skills_html=""

            for skill in project["skills"]:

                skills_html+=f'<span class="skill">{skill}</span>'

            st.markdown(skills_html,unsafe_allow_html=True)

        c1,c2,c3=st.columns(3)

        with c1:

            st.link_button(
                "💻 GitHub",
                project["github"],
                use_container_width=True
            )

        with c2:

            st.link_button(
                "📺 YouTube",
                project["youtube"],
                use_container_width=True
            )

        with c3:

            st.link_button(
                "📖 Documentation",
                project["docs"],
                use_container_width=True
            )

        st.markdown("</div>",unsafe_allow_html=True)
    # =====================================================
# AI REPORT SECTION
# =====================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<style>

.report-card{

background:linear-gradient(135deg,#1e1b4b,#111827,#172554);

border:1px solid rgba(99,102,241,.35);

border-radius:22px;

padding:40px;

text-align:center;

box-shadow:0 0 30px rgba(99,102,241,.20);

animation:reportFloat 5s ease-in-out infinite;

margin-top:20px;

margin-bottom:30px;

}

@keyframes reportFloat{

0%{transform:translateY(0px);}

50%{transform:translateY(-6px);}

100%{transform:translateY(0px);}

}

.report-title{

font-size:34px;

font-weight:700;

color:white;

margin-bottom:15px;

}

.report-text{

font-size:18px;

line-height:1.8;

color:#d1d5db;

}

.footer-text{

text-align:center;

color:#94a3b8;

font-size:15px;

margin-top:30px;

margin-bottom:10px;

}

</style>
""", unsafe_allow_html=True)

st.markdown("""

<div class="report-card">

<div class="report-title">
🤖 AI Career Report
</div>

<div class="report-text">

You've explored your recommended projects.

Now let AI analyze your complete profile and generate a professional career report including:

<br><br>

✅ Skills Assessment

<br>

📊 Job Readiness Score

<br>

💪 Strengths & Weaknesses

<br>

🚀 Personalized Career Recommendations

<br>

📈 Learning Progress Analysis

</div>

</div>

""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

left,center,right=st.columns([1,2,1])

with center:

    if st.button(
        "🚀 Generate My AI Career Report",
        type="primary",
        use_container_width=True
    ):

        st.switch_page("pages/report.py")

st.markdown("""

<div class="footer-text">

Made with ❤️ using Streamlit • SkillForge AI

</div>

""", unsafe_allow_html=True)