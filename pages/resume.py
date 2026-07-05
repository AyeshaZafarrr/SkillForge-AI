import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Resume Upload",
    page_icon="📄",
    layout="wide"
)

# =====================================================
# LOAD CSS
# =====================================================

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# =====================================================
# HIDE STREAMLIT
# =====================================================

st.markdown("""
<style>
#MainMenu{visibility:hidden;}
header{visibility:hidden;}
footer{visibility:hidden;}
</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class="user-header">

<div class="badge">
📄 Step 3 of 4
</div>

<h1 class="user-title">
Resume Upload
</h1>

<h3 class="user-subtitle">
Upload your latest resume for AI analysis
</h3>

</div>
""", unsafe_allow_html=True)

st.caption("Step 3 of 4 • Resume Upload")

# =====================================================
# UPLOAD
# =====================================================

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

st.info("""
Your resume will be analyzed to provide:

✅ ATS Score

✅ Missing Skills

✅ Resume Improvement Suggestions

✅ Career Match Analysis
""")

# =====================================================
# AFTER UPLOAD
# =====================================================

if resume is not None:

    st.session_state["resume"] = resume

    st.success("✅ Resume uploaded successfully!")

    st.write(f"**Selected File:** {resume.name}")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅ Back to Education", use_container_width=True):
            st.switch_page("pages/education.py")

    with col2:
        if st.button("🚀 Continue to AI Analysis", use_container_width=True):
            st.switch_page("pages/analysis.py")