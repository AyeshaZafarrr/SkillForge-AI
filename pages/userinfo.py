import streamlit as st

# =====================================================
# LOAD CSS
# =====================================================

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

header{
visibility:hidden;
}

footer{
visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================
st.markdown("""
<div class="user-header">

<div class="badge">
✨ Step 1 of 4
</div>

<h1 class="user-title">
🧠 User Information
</h1>

<h3 class="user-subtitle">
Build your AI Career Profile
</h3>

<div class="progress-container">
<div class="progress-fill"></div>
</div>

</div>
""", unsafe_allow_html=True)

st.caption("Step 1 of 4 • User Information")

# =====================================================
# FORM
# =====================================================
st.markdown('<div class="form-container">', unsafe_allow_html=True)
with st.form("user_form"):

    # -----------------------------
    # Personal Information
    # -----------------------------

    st.markdown("## 👤 Personal Information")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input(
            "Full Name",
            placeholder="Enter your full name"
        )

    with col2:
        email = st.text_input(
            "Email Address",
            placeholder="Enter your email"
        )

    # -----------------------------
    # Professional Information
    # -----------------------------

    st.markdown("## 💼 Professional Information")

    col1, col2 = st.columns(2)

    with col1:

        role = st.selectbox(
            "Current Role",
            [
                "Student",
                "Python Developer",
                "Data Analyst",
                "Data Scientist",
                "Machine Learning Engineer",
                "AI Engineer",
                "Backend Developer",
                "Full Stack Developer",
                "Cloud Engineer",
                "DevOps Engineer",
                "Software Engineer",
                "Other"
            ]
        )

    with col2:

        experience = st.selectbox(
            "Experience Level",
            [
                "Beginner",
                "Intermediate",
                "Advanced"
            ]
        )

    custom_role = ""

    if role == "Other":
        custom_role = st.text_input(
            "Custom Role"
        )

    # -----------------------------
    # Skills & Career
    # -----------------------------

    st.markdown("## 🎯 Skills & Career Goal")

    col1, col2 = st.columns(2)

    with col1:

        skills = st.multiselect(
            "Current Skills",
            [
                "Python",
                "SQL",
                "Excel",
                "Power BI",
                "Tableau",
                "Pandas",
                "NumPy",
                "Machine Learning",
                "Deep Learning",
                "TensorFlow",
                "PyTorch",
                "Statistics",
                "Data Analysis",
                "AWS",
                "Docker",
                "Git",
                "Linux",
                "Streamlit"
            ]
        )

        custom_skills = st.text_area(
            "Other Skills (Optional)",
            placeholder="Example: Flask, FastAPI"
        )

    with col2:

        career = st.selectbox(
            "Dream Career",
            [
                "AI Engineer",
                "Machine Learning Engineer",
                "Data Scientist",
                "Data Analyst",
                "Python Developer",
                "Backend Developer",
                "Full Stack Developer",
                "Cloud Engineer",
                "DevOps Engineer",
                "Software Engineer",
                "Other"
            ]
        )

        custom_career = ""

        if career == "Other":
            custom_career = st.text_input(
                "Custom Dream Career"
            )

    # -----------------------------
    # Review
    # -----------------------------

    st.markdown("---")

    st.markdown("## 📋 Review & Confirmation")

    st.info("Please verify your information before continuing.")

    confirm = st.checkbox(
        "I confirm that the above information is correct."
    )

    submitted = st.form_submit_button(
        "🚀 Continue",
        use_container_width=True
    )
st.markdown("</div>", unsafe_allow_html=True)
# =====================================================
# AFTER SUBMIT
# =====================================================
if submitted:

    # ---------------- Validation ---------------- #

    if not confirm:
        st.warning("⚠ Please confirm your information first.")

    elif name.strip() == "" or email.strip() == "":
        st.error("Please enter your Name and Email.")

    else:

        # ---------------- Final Values ---------------- #

        final_role = custom_role if role == "Other" else role
        final_career = custom_career if career == "Other" else career

        final_skills = skills.copy()

        if custom_skills.strip():
            extra = [
                x.strip()
                for x in custom_skills.split(",")
                if x.strip()
            ]
            final_skills.extend(extra)

        # ---------------- Save ---------------- #

        st.session_state["name"] = name
        st.session_state["email"] = email
        st.session_state["current_role"] = final_role
        st.session_state["skills"] = final_skills
        st.session_state["experience"] = experience
        st.session_state["dream_career"] = final_career

        # ---------------- Success ---------------- #

        st.success("✅ Information saved successfully!")
        st.session_state["userinfo_completed"] = True

        st.balloons()

        # ---------------- Summary ---------------- #

        st.markdown(f"""
        <div class="review-box">

        <h2>👤 User Summary</h2>

        <p><b>👤 Name:</b> {name}</p>

        <p><b>📧 Email:</b> {email}</p>

        <p><b>💼 Current Role:</b> {final_role}</p>

        <p><b>🧠 Skills:</b> {", ".join(final_skills)}</p>

        <p><b>📈 Experience:</b> {experience}</p>

        <p><b>🎯 Dream Career:</b> {final_career}</p>

        </div>
        """, unsafe_allow_html=True)

       # =====================================================
# CONTINUE TO EDUCATION
# =====================================================

if st.session_state.get("userinfo_completed", False):

    st.markdown("---")

    if st.button(
        "➡ Continue to Education",
        use_container_width=True,
        key="goto_education"
    ):
        st.switch_page("pages/education.py")