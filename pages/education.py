import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Education",
    page_icon="🎓",
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
🎓 Step 2 of 4
</div>

<h1 class="user-title">
Education Details
</h1>

<h3 class="user-subtitle">
Tell us about your academic background
</h3>

</div>
""", unsafe_allow_html=True)

st.caption("Step 2 of 4 • Education")

# =====================================================
# FORM
# =====================================================

with st.form("education_form"):

    st.markdown("## 🎓 Education Information")

    degree = st.selectbox(
        "Highest Qualification",
        [
            "Matric",
            "Intermediate",
            "Diploma",
            "Bachelor's",
            "Master's",
            "PhD"
        ]
    )

    field = st.text_input(
        "Field of Study",
        placeholder="Computer Science"
    )

    institute = st.text_input(
        "Institute / University",
        placeholder="University Name"
    )

    cgpa = st.text_input(
        "CGPA / Percentage",
        placeholder="3.75 CGPA"
    )

    graduation = st.number_input(
        "Graduation Year",
        min_value=2000,
        max_value=2035,
        value=2026
    )

    certificates = st.text_area(
        "Certificates (Optional)",
        placeholder="IBM Data Fundamentals, AWS Cloud Practitioner..."
    )

    submitted = st.form_submit_button(
        "🚀 Save & Continue",
        use_container_width=True
    )

# =====================================================
# AFTER SUBMIT
# =====================================================

if submitted:

    st.session_state["degree"] = degree
    st.session_state["field"] = field
    st.session_state["institute"] = institute
    st.session_state["cgpa"] = cgpa
    st.session_state["graduation"] = graduation
    st.session_state["certificates"] = certificates

    st.success("✅ Education saved successfully!")

    st.markdown("### 📚 Education Summary")

    st.markdown(f"""
**🎓 Qualification:** {degree}

**📖 Field:** {field}

**🏫 Institute:** {institute}

**📊 CGPA / Percentage:** {cgpa}

**📅 Graduation Year:** {graduation}

**🏆 Certificates:** {certificates if certificates else "None"}
""")

    st.write("")

if st.button(
    "➡ Continue to Resume",
    use_container_width=True
):
    st.switch_page("pages/resume.py")